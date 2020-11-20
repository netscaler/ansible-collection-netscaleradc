Rolling upgrades (VPX)
######################


This document demonstrates how to to a rolling upgrade with zero
downtime for a simple load balanced service.

The methods showcased here are also applicable to more complex
networking setups.

Setup
~~~~~

The example utilizes Citrix ADC VPX and some virtualized
hosts to provide the back end web services.

The ansible playbooks along with other files needed to run
this example can be found at the following `github repository`_

The testbed required to run the examples is the following.

::


        +--------------------+
        | Citrix ADC VPX     |
        |                    | 192.168.10.2                  +----------+
        |               SNIP |<----------------------------->| server 1 |
        |                    |              |  192.168.10.10 +----------+
        | NSIP          VIP  |              |                          ^
        +--------------------+              |                          |10.78.60.204
          ^              ^                  |            +----------+  |
          |10.78.60.202  |10.78.60.203      +----------->| server 2 |  |
          |              |                 192.168.10.11 +----------+  |
          |              |                                       ^     |
          |              |                           10.78.60.205|     |
          |              |                                       |     |
          |              |                                       |     |
          |              |                                       |     |
          |              |                                       |     |
          |=NITRO        |=HTTP                                  |     |
          |              |                                       |     |
          |              |     +-----------+             SSH     |     |
          +--------------+-----| user host |---------------------+-----+
                               +-----------+


We need a virtual host to run Citrix ADC VPX and we also need two hosts to
run the back end web services. These can be any kind of hosts, as long as
it is possible for the Citrix ADC node and the web server nodes to communicate
via a specified subnet. Having the backend servers as virtual hosts on the same Xen Server
as the Citrix ADC VPX is recommended since it simplifies the networking setup needed.

In our example the back end servers and the Citrix ADC host communicate via the
``192.168.10.0/24`` subnet.

Also there is a user host which is the machine that will run the playbooks for this example.
This host needs to be able to communicate via SSH with the back end servers to be
able to setup and update the web services and also needs to be able to make
NITRO API calls to the Citrix ADC node on the configured NSIP.

Finally Citrix ADC needs to have a Virtual IP configured which will be the client facing
address of our load balanced service.

        *Note* that the playbooks and scripts do not configure any of these ip addresses
        on the Citrix ADC node or the server nodes.
        You need to set them up prior to running the playbooks in this example
        and modify the ``inventory.txt`` file to match your particular configuration.

More details for the requirements of each node are included in the README
file of the `github repository`_ containing this example's files.


.. _github repository: https://github.com/citrix/netscaler-rolling-updates-vpx-example



Initializing the testbed
~~~~~~~~~~~~~~~~~~~~~~~~

Having setup the testbed and modified the inventory.txt file to match
the configured ip addresses we need to initialize the Citrix ADC and the
back end server nodes.

This is done by running on the user host from a fresh checkout of the files
from the `github repository`_ by running the following command

.. code-block:: bash

        ansible-playbook -i inventory.txt rolling_init.yaml

Running this playbook will initialize the back end services and also
configure the Citrix ADC in order to serve them over the VIP of the
load balancer.

The logical configuration of the Citrix ADC node can be seen in the following
diagram.

::

                          +
                          |
                          |
                          |
                +---------V----------+
                | Load balancer      |
                | lb_vserver_1       |----------+
                | 10.78.60.203:80    |          |
                +--------------------+          |
                        |                       |
                        |                       |
                        |                       |
                +-------V-----+           +-----V-------+
                | Service 1   |           | Service 2   |
                | server_1    |           | server_2    |
                | port 80     |           | port 80     |
                +-------------+           +-------------+
                        |                       |
                        |                       |
                        |                       |
                +-------V-------+           +-----V---------+
                | server_1      |           | server_2      |
                | 192.168.10.10 |           | 192.168.10.11 |
                +---------------+           +---------------+


In this setup the load balancer virtual server is configured with the
ROUNDROBIN load balancing method and has 2 service members with 50%
weight each.

To check that the load balancer works correctly run the following command

.. code-block:: bash

        curl 10.78.60.203

You should see a ``Hello webserver1``.
Running the same command a second time should output ``Hello webserver2``.


Upgrade process
~~~~~~~~~~~~~~~

The upgrade playbook utilizes the ``pre_tasks`` and ``post_tasks`` hooks to
bring the services down and back up during the update process.

The upgrade playbook is the following:

.. code-block:: yaml

        - hosts: service_hosts
          vars:
            compose_yaml: /var/tmp/docker-compose.yaml

          remote_user: root
          gather_facts: False
          serial: 1

          pre_tasks:
            - name: "Disable {{ servername }}"
              delegate_to: localhost
              citrix_adc_server:
                nsip: "{{ nsip }}"
                nitro_user: "{{ nitro_user }}"
                nitro_pass: "{{ nitro_pass }}"

                disabled: yes

                name: "{{ servername }}"

          post_tasks:

            - name: "Re enable {{ servername }}"
              delegate_to: localhost
              citrix_adc_server:
                nsip: "{{ nsip }}"
                nitro_user: "{{ nitro_user }}"
                nitro_pass: "{{ nitro_pass }}"

                disabled: no
                name: "{{ servername }}"

          tasks:

            - name: "Update backend {{ servername }}"
              command: docker-compose -f "{{ compose_yaml }}" exec -d webserver bash -c "echo 'hello updated {{ servername }}' > /app/content.txt"

The function of the pre_tasks and post_tasks hooks is documented by
`ansible <https://docs.ansible.com/ansible/playbooks_roles.html>`_.


Essentially what we do is that we disable the server entity in Citrix ADC
for each web service before the update process and after the update
has taken place we re enable the server entity.

The ``serial: 1`` option instructs ansible to operate on the webservers
one at a time. This is a deviation from the default behavior of Ansible
which is to operate on multiple nodes at once.

In our example the update process is just a simple change of the
content file on the web service docker container to verify
the update has taken effect.

To see how the update works you can run

.. code-block:: bash

        curl 10.78.60.203

during the update process and see how the output changes.

Since the update itself is a relatively quick process  you may
not be able to see the `rolling` nature of the upgrade.

For that you may want to run the update script in step mode

.. code-block:: bash

        ansible-playbook -i inventory.txt rolling_update.yml --step

and watch the output of

.. code-block:: bash

        curl 10.78.60.203

a number of times to actually see what happens.

What you should see is each server taken out of the load balancing
pool and then brought up without any service interruption.

In our example the update of the web server is instantaneous
we do not have any actual down time.

In a real world situation the update would put the webserver in a
state that would be unable to respond to requests.

Had we not disabled the corresponding server, in this case, would
mean that a number of requests would be directed to the offline
server resulting in clients getting error responses.

Eventually the monitors attached to the Citrix ADC services would
take the disrupted service out of the load balancing pool
but depending on the traffic volume several requests would have
been affected by the non functioning service by that time.

Disabling the server before the update process guarantees that
Citrix ADC will not direct any traffic to it during that time,
ensuring continuous delivery of the content.

References
~~~~~~~~~~

Citrix ADC ansible modules repository
++++++++++++++++++++++++++++++++++++

https://github.com/citrix/citrix-adc-ansible-modules

Ansible documentation
+++++++++++++++++++++

https://docs.ansible.com/ansible/index.html
