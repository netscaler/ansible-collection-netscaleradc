:orphan:

.. _citrix_adc_appfw_signatures_custom_import_module:

citrix_adc_appfw_signatures_custom_import - Import custom Application Firewall signatures
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.2.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Import custom Application Firewall signatures.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - api_path

        *(str)*
      -
      - Base NITRO API path.

        Define only in case of an ADM service proxy call
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - block_all

        *(bool)*
      -
      - Disable all rules in signature file
    * - enable_all

        *(bool)*
      -
      - Enable all rules in signature file
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - log_all

        *(bool)*
      -
      - Enable log for all rules in signature file
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``

        When true and adm service is the api proxy the following option must also be defined: ``bearer_token``

        When true you must define a target ADC by defining any of the following parameters

        I(instance_ip)

        I(instance_id)

        I(instance_name)
    * - name

        *(str)*
      -
      - Name of the signature object.

        Minimum length =  1

        Maximum length =  31
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
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
      - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - src

        *(str)*
      -
      - URL (protocol, host, path, and file name) for the location at which to store the imported signatures

        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client authentication for access.

        Minimum length =  1

        Maximum length =  2047
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - stats_all

        *(bool)*
      -
      - Enable stats for all rules in signature file
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - xslt

        *(str)*
      -
      - XSLT file source.

        Maximum length =  2047
    * - xslt_builtin

        *(str)*
      -
      - Built-in XSLT file source.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: setup appfw custom signatures 
      delegate_to: localhost
      register: result
      citrix_adc_appfw_signatures_custom_import:
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        nsip: '{{ nsip }}'
        validate_certs: '{{ validate_certs }}'
    
        state: present 
    
        name: "custom_signatures"
        src: "local:Scan_Report_ctrx8pb_20200109.xml"
        xslt: "local:scan_Qualys_cloud_2_42_3.xsl"
    
        enable_all: true
        block_all: true
        log_all: true
        stats_all: false


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
