:orphan:

.. _citrix_adm_mpsuser_module:

citrix_adm_mpsuser - Manage Citrix ADM users.
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADM users.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - enable_session_timeout

        *(bool)*
      -
      - Enables session timeout for user.
    * - external_authentication

        *(bool)*
      -
      - Enable external authentication.
    * - groups

        *(list)*
      -
      - Groups to which user belongs.
    * - id

        *(str)*
      -
      - Id is system generated key for all the system users.
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
      - User Name.

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
    * - password

        *(str)*
      -
      - Password.

        Minimum length = 1

        Maximum length = 128
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - session_timeout

        *(str)*
      -
      - Session timeout for the user.
    * - session_timeout_unit

        *(str)*
      -
      - Session timeout unit for the user.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - tenant_id

        *(str)*
      -
      - Tenant Id of the system users.

        Minimum length = 1

        Maximum length = 128
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup mpsuser
      delegate_to: localhost
      citrix_adm_mpsuser:
        mas_ip: 192.168.1.1
        mas_user: nsroot
        mas_pass: nsroot
    
        state: present
    
        name: test_mpsuser
        password: 123456
    
        session_timeout: 10
        session_timeout_unit: Minutes
        external_authentication: false
        enable_session_timeout: true
        groups:
          - test_mpsgroup


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
    * - mpsuser

        *(dict)*
      - success
      - Dictionary containing the attributes of the created mpsuser
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
