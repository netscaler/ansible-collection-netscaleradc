Speeding up execution
=====================

This document details how to speed up the execution time of a playbook
containing invocations of Netscaler ansible modules.

Ansible has some options to help with speeding up execution by making
forks of itself to execute playbooks in multiple target hosts.

Also in the context of a single playbook the use of the ``async`` keyword
may help with parallelizing the execution of the tasks therein but at
the cost of increased complexity.

Both of the above methods can be used to speed up the execution of
playbooks containing invocations of Netscaler modules.

Here we will detail a third option which is specific to the Netscaler
modules and the way the underlying API is used.

Saving configuration
--------------------

By default every Netscaler module after it performs any changes to the configuration
of the Netscaler node will also save the configuration.

While this is the safest option as far as robustness is concerned, it turns out that the save configuration operation
is quite costly time wise, taking up to 5 seconds.

When multiple tasks within a playbook make changes to Netscaler entities these
delays accumulate to a substantial amount.

The solution is to instruct the Netscaler modules not to save the configuration
individually but instead notify a handler which will save the configuration once
at the end of the playbook execution.

To do this we need to use the ``save_config`` option along with the ``netscaler_save_config``
module which will be invoked by the handler.

Sample playbook
---------------

The following playbook demonstrates this technique.


.. code-block:: yaml

        - hosts: netscaler

          vars:
            save_config: no
            state: present

          tasks:
            - name: Setup server 1

              delegate_to: localhost
              notify: Save netscaler configuration

              netscaler_server:
                nsip: 172.18.0.2
                nitro_user: nsroot
                nitro_pass: nsroot

                state: "{{ state }}"
                save_config: "{{ save_config }}"

                name: server-1
                ipaddress: 192.168.1.1
                comment: Our first server

            - name: Set server 2

              delegate_to: localhost
              notify: Save netscaler configuration

              netscaler_server:
                nsip: 172.18.0.2
                nitro_user: nsroot
                nitro_pass: nsroot

                state: "{{ state }}"
                save_config: "{{ save_config }}"

                name: server-2
                ipaddress: 192.168.1.2
                comment: Our second server

          handlers:
            - name: Save netscaler configuration
              delegate_to: localhost
              netscaler_save_config:
                nsip: 172.18.0.2
                nitro_user: nsroot
                nitro_pass: nsroot


Closing remarks
---------------

As you see in the example we need to explicitly set the ``save_config`` option
since by default it is set to ``yes``.

Also we call the ``netscaler_save_config`` module only once in the handlers section.

The number of times the configuration will be saved on the Netscaler module is
only one regardless of the number of changes, or none if there is no change recorded
in the result of any of the netscaler modules.

This is much better than the worst case with the default ``save_config`` option which would
save the configuration twice if both server modules made changes.

It is also just as fast as the best case with the default ``save_config`` option which would be
to save the configuration once in case only one of the tasks made any change.

Also note that the potential benefit increases, for each Netscaler module which utilizes the
save configuration handler. For example if we had ten Netscaler modules making changes we would
be saving the configuration ten times. Instead if these modules use the ``netscaler_save_config``
as a handler we will have only one call to the save operation.
