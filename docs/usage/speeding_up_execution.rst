Speeding up execution
=====================

This document details how to speed up the execution time of a playbook
containing invocations of Citrix ADC ansible modules.

Ansible has some options to help with speeding up execution by making
forks of itself to execute playbooks in multiple target hosts.

Also in the context of a single playbook the use of the ``async`` keyword
may help with parallelizing the execution of the tasks therein but at
the cost of increased complexity.

Both of the above methods can be used to speed up the execution of
playbooks containing invocations of Citrix ADC modules.

Here we will detail a third option which is specific to the Citrix ADC
modules and the way the underlying API is used.

Saving configuration
--------------------

By default every Citrix ADC module after it performs any changes to the configuration
of the Citrix ADC node will also save the configuration.

While this is the safest option as far as robustness is concerned, it turns out that the save configuration operation
is quite costly time wise, taking up to 5 seconds.

When multiple tasks within a playbook make changes to Citrix ADC entities these
delays accumulate to a substantial amount.

The solution is to instruct the Citrix ADC modules not to save the configuration
individually but instead notify a handler which will save the configuration once
at the end of the playbook execution.

To do this we need to use the ``save_config`` option along with the ``citrix_adc_save_config``
module which will be invoked by the handler.

Sample playbook
---------------

The following playbook demonstrates this technique.


.. code-block:: yaml

        - hosts: citrix_adc

          vars:
            save_config: no
            state: present

          tasks:
            - name: Setup server 1

              delegate_to: localhost
              notify: Save Citrix ADC configuration

              citrix_adc_server:
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
              notify: Save Citrix ADC configuration

              citrix_adc_server:
                nsip: 172.18.0.2
                nitro_user: nsroot
                nitro_pass: nsroot

                state: "{{ state }}"
                save_config: "{{ save_config }}"

                name: server-2
                ipaddress: 192.168.1.2
                comment: Our second server

          handlers:
            - name: Save Citrix ADC configuration
              delegate_to: localhost
              citrix_adc_save_config:
                nsip: 172.18.0.2
                nitro_user: nsroot
                nitro_pass: nsroot


Closing remarks
---------------

As you see in the example we need to explicitly set the ``save_config`` option
since by default it is set to ``yes``.

Also we call the ``citrix_adc_save_config`` module only once in the handlers section.

The number of times the configuration will be saved on the Citrix ADC module is
only one regardless of the number of changes, or none if there is no change recorded
in the result of any of the Citrix ADC modules.

This is much better than the worst case with the default ``save_config`` option which would
save the configuration twice if both server modules made changes.

It is also just as fast as the best case with the default ``save_config`` option which would be
to save the configuration once in case only one of the tasks made any change.

Also note that the potential benefit increases, for each Citrix ADC module which utilizes the
save configuration handler. For example if we had ten Citrix ADC modules making changes we would
be saving the configuration ten times. Instead if these modules use the ``citrix_adc_save_config``
as a handler we will have only one call to the save operation.
