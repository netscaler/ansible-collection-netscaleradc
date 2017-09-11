Direct NITRO API calls
######################

One method of configuring Netscaler consists of making
direct NITRO API calls using Ansbile's `uri module`_.

This method tends to be quite verbose since setting up even
basic functions requires multiple NITRO calls.

Another consideration is failure robustness.
NITRO API call failures result in the uri module task failing
immediately and stopping the execution of the rest of the playbook.

This may be desired behavior in general since in some cases we need
to examine the failure response to actually determine if the operation
was indeed a failure or expected.

An example of that would be trying to add a resource while it exists.
This is will result in failure since the HTTP POST request will not
create the resource but this does not mean the configuration of Netscaler
is necessarily invalid.

Using Ansible's conditional constructs we can work around this problem
in most cases but this adds to the verbosity and complexity of the playbooks.


Workflow
~~~~~~~~

In the following example we use direct NITRO API calls to create or update
a basic server.

The play would be quite short but we have added some control logic to
detect whether the resource already exists and then apply the appropriate
operation.

We first try to get the details of the configuration resource. We examine
the outcome of this operation and if it was successful we proceed to update
the resource. If it failed we examine the exact errorcode and if it signifies
that the error was due to the resource missing we proceed to create it.

On any other outcome, an error that was not what was expected, the play fails.

The final task is to save the running configuration to ensure that a reboot
of Netscaler will not undo the changes we have made.


Playbook
~~~~~~~~

.. code-block:: yaml

        - hosts: netscaler
          gather_facts: no
          vars:
            resource: server
            request_payload:
              server:
                name: test-server-1
                ipaddress: 192.168.1.6

          tasks:
            - name: Get resource
              delegate_to: localhost
              ignore_errors: true
              register: result
              uri:
                url: "http://{{ nsip }}/nitro/v1/config/{{ resource }}/{{ request_payload.server.name }}"
                method: GET
                status_code: 200
                return_content: yes
                headers:
                  X-NITRO-USER: "{{ nitro_user }}"
                  X-NITRO-PASS: "{{ nitro_pass }}"

            - name: Check success or expected failure
              assert:
                that: result|succeeded or ( result|failed and result.json.errorcode == 258 )

            - name: Add resource when not existing
              delegate_to: localhost
              when: result|failed
              uri:
                url: "http://{{ nsip }}/nitro/v1/config/{{ resource }}"
                method: POST
                status_code: 201
                return_content: yes
                headers:
                  X-NITRO-USER: "{{ nitro_user }}"
                  X-NITRO-PASS: "{{ nitro_pass }}"
                body_format: json
                body: "{{ request_payload }}"

            - name: Update resource if existing
              delegate_to: localhost
              when: result|succeeded
              uri:
                url: "http://{{ nsip }}/nitro/v1/config/{{ resource }}"
                method: PUT
                status_code: 200
                return_content: yes
                headers:
                  X-NITRO-USER: "{{ nitro_user }}"
                  X-NITRO-PASS: "{{ nitro_pass }}"
                body_format: json
                body: "{{ request_payload }}"

            - name: Save running configuration
              delegate_to: localhost
              uri:
                url: "http://{{ nsip }}/nitro/v1/config/nsconfig?action=save"
                method: POST
                status_code: 200
                headers:
                  X-NITRO-USER: "{{ nitro_user }}"
                  X-NITRO-PASS: "{{ nitro_pass }}"
                body_format: json
                body:
                  nsconfig: {}

For the first task which detects if the resource already exists we have set
``ignore_errors: true``. This has the effect that an error will not stop the
execution of the playbook. We also register the result under the variable ``result``
to be available for examination in the following tasks.

The next task leverages Ansible's `assert module`_ to distinguish between an
expected failure and an unexpected one. In the case of an unexpected failure
this task fails and prevents any further execution.

Next there are two tasks, one creating the resource and one updating the existing
resource. Which one executes depends on the condition defined in each task's
``when:`` option.

References
~~~~~~~~~~

Ansible NITRO API calls repository
==================================

https://github.com/citrix/ansible-nitro-api-calls

Ansible uri module documentation
================================

http://docs.ansible.com/ansible/latest/uri_module.html

Ansible assert module documentation
===================================

http://docs.ansible.com/ansible/latest/assert_module.html


.. _uri module: http://docs.ansible.com/ansible/latest/uri_module.html
.. _assert module: http://docs.ansible.com/ansible/latest/assert_module.html
