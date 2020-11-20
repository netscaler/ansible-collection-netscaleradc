:orphan:

.. _citrix_adm_rba_policy_module:

citrix_adm_rba_policy - Manage Citrix ADM rba policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADM rba policies.
- Note that due to limitations on the underlying NITRO API an update is always forced when I(state=present).
- Instead delete and recreate the rba_policy.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - description

        *(str)*
      -
      - Description of Policy.

        Minimum length = 1

        Maximum length = 1024
    * - id

        *(str)*
      -
      - Id is system generated key for all the system policys.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - name

        *(str)*
      -
      - Policy Name.

        Minimum length = 1

        Maximum length = 128
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout

        *(float)*
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - roles

        *(list)*
      -
      - Roles to which this policy attached.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - statement

        *(list)*
      -
      - RBA statement.
    * - tenant_id

        *(str)*
      -
      - Tenant Id of the RBA roles.

        Minimum length = 1

        Maximum length = 128
    * - ui

        *(list)*
      -
      - RBA for UI components.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup appfw policy
      delegate_to: localhost
      citrix_adm_rba_policy:
        mas_ip: 192.168.1.1
        nitro_auth_token: "{{ login_result.session_id }}"
    
        state: present
    
        name: test_policy
        description: some description
        tenant_id: "0ea1d85a-06b8-4225-9fc8-5a7065fdd590"
        statement:
          - access_type: true
            operation_name: add
            parent_name: rba_policy
            resource_type: ns_gslbservice
        ui:
          - access_type: true
            display_name: ""
            name: ContentSwitching
            parent_name: rba_policy


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
    * - rba_policy

        *(dict)*
      - success
      - Dictionary containing the attributes of the created rba_policy
