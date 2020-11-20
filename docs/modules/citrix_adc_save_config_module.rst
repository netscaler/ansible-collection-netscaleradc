:orphan:

.. _citrix_adc_save_config_module:

citrix_adc_save_config - Save Citrix ADC configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- This module uncoditionally saves the configuration on the target Citrix ADC node.
- This module does not support check mode.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - instance_ip

        *(str)*
      -
      - The IP address of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - mas_proxy_call

        *(bool)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - nitro_auth_token

        *(str)*
      -
      - The authentication token provided by the ``mas_login`` operation. It is required when issuing Nitro API calls through a Citrix ADM proxy.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Citrix ADC node.
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
      - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC.
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. ``192.168.1.1:555``.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    ---
    - name: Save Citrix ADC configuration
      delegate_to: localhost
      citrix_adc_save_config:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
    - name: Setup server without saving  configuration
      delegate_to: localhost
      notify: Save configuration
      citrix_adc_server:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        save_config: no
    
        name: server-1
        ipaddress: 192.168.1.1
    
    # Under playbook's handlers
    
    - name: Save configuration
      delegate_to: localhost
      citrix_adc_save_config:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot


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
