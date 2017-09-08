Templating the configuration file
#################################

One method of configuring Netscaler consists of editing
the ns.conf file directly and then rebooting Netscaler for
the configuration changes to take effect.

After the reboot the saved configuration becomes the running
configuration which is what we want to change.

Workflow
~~~~~~~~

With this method we leverage Ansible's `template module`_ to produce
a ns.conf file from a Jinja2 template.

The Jinja2 template is populated from configuration variables which can
be defined with various methods, inside the playbook, in an inventory file
or loaded from inventory files.

We then upload the resulting ns.conf to the Netscaler node which alters the
saved configuration.

For the saved configuration to become running configuration we need to reboot
Netscaler. Doing a warm reboot is recommended since it is sufficient to reload
the configuration and also avoid the greater downtime a cold reboot would induce.

After the reboot the user can check the running configuration either through the GUI or the
command line interface and make sure the changes have been succesfully applied.

There is an assortment of playbooks on this `github repository`_ which contains
sample playbooks that perform fundamental NITRO operations. The tasks within
each playbook can be combined into a larger playbook which accomplishes a full
Netscaler configuration.

In fact this is how the following example was constructed.

Playbook
~~~~~~~~

In the following example we showcase how we can setup a load balancer which
balances two backend services. The full content of the referenced files can
be found `here`_.

Processing the template
=======================

First we have a Jinja template file to produce the desired ns.conf.
It is recommended to use an actual ns.conf file from the target Netscaler node
as a starting point for the template.

The full file is quite long but the interesting parts are shown below.


.. code-block:: yaml

    ...

    # Start of Jinja inserted servers
    {% for server in configuration.servers %}
    add server {{ server.name }} {{ server.ipaddress }}
    {% endfor %}
    # End of Jinja inserted servers

    ...

    # Start of Jinja inserted services
    {% for service in configuration.services %}
    add service {{ service.name }} {{ service.ipaddress }} {{ service.type }} {{ service.port }} -gslb NONE -maxClient 0 -maxReq 0 -cip DISABLED -usip NO -useproxyport YES -sp OFF -cltTimeout 180 -svrTimeout 360 -CKA NO -TCPB NO -CMP NO
    {% endfor %}
    # End of Jinja inserted services


    ...

    # Start of Jinja inserted lb vservers
    {% for vserver in configuration.lbvservers %}
    add lb vserver {{ vserver.name }} {{ vserver.type }} {{ vserver.ipaddress }} {{ vserver.port }} -persistenceType NONE -cltTimeout 180
    {% endfor %}
    # End of Jinja inserted lb vservers

    ...

    # Start of Jinja inserted lb vservers binds
    {% for bind in configuration.lbvserver_binds %}
    bind lb vserver {{ bind.server }} {{ bind.service }} -weight {{ bind.weight }}
    {% endfor %}
    # End of Jinja inserted lb vservers binds


Essentially we iterate over items in the configuration dictionary.
This dictionary is populated from the playbook variables.


Defining the configuration variables
====================================

The playbook variables are shown below.

.. code-block:: yaml

  vars:
    filename: "ns.conf"
    filelocation: "/nsconfig"
    localfile: "/var/tmp/ns.conf"

    warm_reboot: yes

    configuration:
      servers:
        - name: 192.168.1.1
          ipaddress: 192.168.1.1
        - name: 192.168.1.2
          ipaddress: 192.168.1.2

      services:
        - name: service-test-1
          ipaddress: 192.168.1.1
          port: 80
          type: HTTP

        - name: service-test-2
          ipaddress: 192.168.1.2
          port: 80
          type: HTTP

      lbvservers:
        - name: server-test
          ipaddress: 10.78.60.203
          port: 80
          type: HTTP

      lbvserver_binds:
        - server: server-test
          service: service-test-1
          weight: 50
        - server: server-test
          service: service-test-2
          weight: 50

The configuration dictionary is defined inside the playbook.
This is done for maintaining simplicity in the context of the example.

A more sophisticated setup could have defined the configuration dictionary
in a separate variables file, in the inventory file or use any other method
Ansible allows to define variables.

We also see the variables that configure the paths of the source and target files.
These could also be defined in the different ways the configuration dictionary is
defined.

Upload the new ns.conf
======================

Having produced the ns.conf file we need to upload it to Netscaler.

Following are the tasks that accomplish this.

.. code-block:: yaml

    - name: Delete old ns.conf
      delegate_to: localhost
      uri:
        url: "http://{{ nsip }}/nitro/v1/config/systemfile?args=filename:{{ filename }},filelocation:{{ filelocation | replace('/','%2F') }}"
        method: DELETE
        status_code: 200
        return_content: yes
        headers:
          X-NITRO-USER: "{{ nitro_user }}"
          X-NITRO-PASS: "{{ nitro_pass }}"

    - name: Upload new ns.conf
      delegate_to: localhost
      uri:
        url: "http://{{ nsip }}/nitro/v1/config/systemfile"
        method: POST
        status_code: 201
        return_content: yes
        headers:
          X-NITRO-USER: "{{ nitro_user }}"
          X-NITRO-PASS: "{{ nitro_pass }}"
        body_format: json
        body:
          systemfile:
            filename: "{{ filename }}"
            filecontent: "{{ lookup('file', localfile) | b64encode }}"
            filelocation: "{{ filelocation }}"

Notice that we need to delete the existing file before copying the new one.
Trying to upload a file to an existing file path will result in a NITRO error.

Rebooting Netscaler
===================

The last step is to warm reboot the Netscaler node. Replacing the ns.conf file
overwrites the saved configuration. The running configuration of Netscaler remains
unaffected. To force Netscaler to apply the saved configuration we need to reboot
it. We have the option do a warm reboot which results in less downtime than a full
reboot.

The task that accomplishes this is shown below.

.. code-block:: yaml

    - name: Reboot Netscaler
      delegate_to: localhost
      uri:
        url: "http://{{ nsip }}/nitro/v1/config/reboot"
        method: POST
        status_code: 201
        headers:
          X-NITRO-USER: "{{ nitro_user }}"
          X-NITRO-PASS: "{{ nitro_pass }}"
        body_format: json
        body:
          reboot:
            warm: "{{ warm_reboot }}"

Final points
============

The user needs for this example to set
the variables needed for authentication and communication with Netscaler. Namely
``nsip``, ``nitro_user``, ``nitro_pass``. These variables retain the meaning they
have in the Netscaler specific Ansible modules.

All tasks are run with the ``delegate_to: localhost`` option set.
This is needed since we are making NITRO API calls to the Netscaler node. We do not
want to connect directly with SSH to it.

In some deployments the delegated host may need to be the bastion node that has
actual NITRO access to the Netscaler node.

References
~~~~~~~~~~

Ansible NITRO API calls repository
==================================

https://github.com/citrix/ansible-nitro-api-calls

Ansible template module documentation
=====================================

http://docs.ansible.com/ansible/latest/template_module.html



.. _template module: http://docs.ansible.com/ansible/latest/template_module.html
.. _github repository: https://github.com/citrix/ansible-nitro-api-calls
.. _here: https://github.com/citrix/netscaler-rolling-updates-example
