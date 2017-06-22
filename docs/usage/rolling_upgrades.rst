Rolling upgrades
################


This document demonstrates how to to a rolling upgrade with zero
downtime for a simple load balanced service.

The methods showcased here are also applicable to more complex
networking setups.

Setup
~~~~~

The example utilizes Netscaler CPX and docker images.

The dependencies needed to run the playbooks are at
the following `github repository`_

.. _github repository: https://github.com/citrix/netscaler-rolling-updates-example


Testbed
~~~~~~~

The testbed is comprised of a Netscaler CPX load balancer and 2 docker containers
that act as the backend servers for the load balanced service.

The logical diagram of the testbed is as follows


::

                          +
                          |
                          |
                          |
                +---------V----------+
                | Load balancer      |
                | lb_vserver_1       |----------+
                | 172.17.0.200:8000  |          |
                +--------------------+          |
                        |                       |
                        |                       |
                        |                       |
                +-------V-----+           +-----V-------+
                | Service 1   |           | Service 2   |
                | server_1    |           | server_2    |
                | port 8000   |           | port 8000   |
                +-------------+           +-------------+
                        |                       |
                        |                       |
                        |                       |
                +-------V-----+           +-----V-------+
                | server_1    |           | server_2    |
                | 172.17.0.3  |           | 172.17.0.4  |
                +-------------+           +-------------+
                        |                       |
                        |                       |
                        |                       |
                        |                       |
                +-------V----------+    +-------V----------+
                | web server 1     |    | web server 2     |
                | 172.17.0.3:8000  |    | 172.17.0.4:8000  |
                +------------------+    +------------------+


In this setup the load balancer virtual server is configured with the
ROUNDROBIN load balancing method and has 2 service members with 50%
weight each.

To check that the load balancer works correctly run the following command

.. code-block:: bash

        curl 172.17.0.200:8000

You should see a ``Hello I am server_1``.

Running the same a second time should output ``Hello I am server_2``.

The playbook that accomplishes this setup can be found
`here <https://github.com/citrix/netscaler-ansible-modules/blob/master/samples/rolling_setup.yml>`_.

Upgrade process
~~~~~~~~~~~~~~~

The upgrade playbook utilizes the *pre_tasks* and *post_tasks* hooks to
bring the services down and back up during the update process.

The upgrade playbook is the following:

.. code-block:: yaml

        - hosts: webservers
          remote_user: root
          gather_facts: False
          serial: 1
          pre_tasks:
            - name: "Disable {{ servername }}"
              delegate_to: localhost
              netscaler_server:
                nsip: "{{ nsip }}"
                nitro_user: "{{ nitro_user }}"
                nitro_pass: "{{ nitro_pass }}"
                disabled: yes
                name: "{{ servername }}"
                ipaddress: "{{ hostip }}"
          post_tasks:
            - name: "Re enable {{ servername }}"
              delegate_to: localhost
              netscaler_server:
                nsip: "{{ nsip }}"
                nitro_user: "{{ nitro_user }}"
                nitro_pass: "{{ nitro_pass }}"
                name: "{{ servername }}"
                ipaddress: "{{ hostip }}"
          tasks:
            - name: "Update {{ servername }}"
              delegate_to: localhost
              docker_container:
                name: "{{ servername }}"
                image: myapp
                command: python /webapp/app.py "Hello I am {{ servername }} UPDATED"


The function of the pre_tasks and post_tasks hooks is documented by
`ansible <https://docs.ansible.com/ansible/playbooks_roles.html>`_.


Essentially what we do is that we disable the server entity in Netscaler
for each web service before the update process and after the update we
re enable the server entity.

The ``serial: 1`` option instructs ansible to operate on the webservers
one at a time. This is a deviation from the default behavior of Ansible
which is to operate on multiple nodes at once.

In our example the update process is just a simple restart of the
docker container along with some change in the response to verify
the update has taken effect.

To see how the update works you can run

.. code-block:: bash

        curl 172.17.0.200:8000

during the update process and see how the output changes.

Since the update itself is a relatively quick process  you may
not be able to see the `rolling` nature of the upgrade.

For that you may want to run the update script in step mode

.. code-block:: bash

        ansible-playbook -i inventory.txt rolling_update.yml --step

and watch the output of

.. code-block:: bash

        curl 172.17.0.200:8000

a number of times to actually see what happens.

What you should see is each server taken out of the load balancing
pool and then brought up without any service interruption.

Had we not used the pre_tasks and post_tasks hooks you could see
some requests being disrupted and possibly timing out.

Eventually the monitors attached to the Netscaler services would
take the disrupted service out of the load balancing pool
but depending on the traffic volume several requests would have
been affected by the non functioning service by that time.

Inventory file
~~~~~~~~~~~~~~

A sample inventory file is the following where we define
the variables referenced in the playbooks.


.. code-block:: ini

        [netscaler]

        netscaler_lb nsip=172.17.0.2 nitro_user=nsroot nitro_pass=nsroot validate_certs=no

        [webservers]

        172.17.0.3 nsip=172.17.0.2 nitro_user=nsroot nitro_pass=nsroot servername=server_1 hostip=172.17.0.3
        172.17.0.4 nsip=172.17.0.2 nitro_user=nsroot nitro_pass=nsroot servername=server_2 hostip=172.17.0.4

Note that the host running the docker containers must not have
other containers running at the same time so that the
ip addresses are mapped correctly.

References
~~~~~~~~~~

Netscaler ansible modules repository
++++++++++++++++++++++++++++++++++++

https://github.com/citrix/netscaler-ansible-modules

Ansible documentation
+++++++++++++++++++++

https://docs.ansible.com/ansible/index.html
