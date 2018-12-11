Understanding citrix_adm_application delays
===========================================

`citrix_adm_application` introduces two delays that
are configurable during execution.

One delay relates to the creation and retrieval of a new application.

The other relates to when to poll the managed instances so that Citrix ADM
updates the list of applications in case some were deleted.


Creation of an application
--------------------------


Let's take the following sample task.

.. code-block:: yaml

    - name: Setup application
      delegate_to: localhost
      citrix_adm_application:
        mas_ip: "{{ mas_ip }}"
        nitro_auth_token: "{{ login_result.session_id }}"

        state: present

        poll_after_delete: true
        poll_delay: 10

        check_create: true
        check_create_delay: 10

        app_category: test_category
        name: test_application_19
        stylebook_params: "{{ stylebook_facts | to_json }}"

In this task we have defined the `check_create`
and `check_create_delay` options.

These options will cause the playbook to pause execution of the module
for 10 seconds in order to give the Citrix ADM time to create and register
the new application.

This delay is needed since in the result values of the playbook execution
there is the `application` key which contains all the data returned by
Citrix ADM that are relevant to the newly created application.


Deletion of an application
---------------------------

.. code-block:: yaml

    - name: Setup application
      delegate_to: localhost
      citrix_adm_application:
        mas_ip: "{{ mas_ip }}"
        nitro_auth_token: "{{ login_result.session_id }}"

        state: absent

        poll_after_delete: true
        poll_delay: 10

        app_category: test_category
        name: test_application_19
        stylebook_params: "{{ stylebook_facts | to_json }}"

In the task presented above we see that we are deleting and application
from the target Citrix ADM.

The `poll_after_delete` and `poll_delay` options will cause the module
to pause execution for the specified time period and then issue a poll
instances command to the target Citrix ADM.

This command will update the list of applications which should now have
the deleted application removed.

The poll command is issued by the Citrix ADM in 30 minute intervals so
if there is no need for an immediate update of the available applications
the user can set this option to `false`.


Polling instances on demand
---------------------------

There is an Ansible module that can issue the poll instances command on
demand on a target Citrix ADM.

This module is useful in case a user wants to delete many applications and
also wishes to have the application list updated but does not want to
have to wait after every single application deletion for the `poll_delay`
time period.

For this purpose the `citrix_adm_application` tasks can run with the `poll_after_delete`
option set to `false` and then call the `citrix_adm_poll_instances` module as shown below.

.. code-block:: yaml

    - name: poll instances
      delegate_to: localhost
      citrix_adm_poll_instances:
        mas_ip: "{{ mas_ip }}"
        nitro_auth_token: "{{ login_result.session_id }}"


In this manner the poll instances command is issued only once,
saving execution time.
