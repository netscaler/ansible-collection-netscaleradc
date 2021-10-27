:orphan:

.. _citrix_adc_sslcipher_sslciphersuite_binding_module:

citrix_adc_sslcipher_sslciphersuite_binding - Manage SSL cipher and SSL ciphersuite bindings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.1.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage SSL cipher and SSL ciphersuite bindings
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance




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
    * - ciphergroupname

        *(str)*
      -
      - Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_) and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), (=), and hyphen (-) characters. Cannot be changed after the cipher group is created. The following applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in or single quotation marks (for example, "my ciphergroup" or 'my ciphergroup').

        Minimum length =  1
    * - ciphername

        *(str)*
      -
      - Cipher name.
    * - cipheroperation

        *(str)*
      - Choices:

          - ADD
          - REM
          - ORD
      - The operation that is performed when adding the cipher-suite. Possible cipher operations are: ADD - the given cipher-suite to the existing one configured for the virtual server. REM - Removes the given from the existing one configured for the virtual server. ORD - Overrides the current configured for the virtual server with the given cipher-suite.
    * - cipherpriority

        *(str)*
      -
      - This indicates priority assigned to the particular cipher.

        Minimum value = ``1``
    * - ciphgrpals

        *(str)*
      -
      - A cipher-suite can consist of an individual cipher name, the system predefined cipher-alias name, or defined cipher-group name.

        Minimum length =  1
    * - description

        *(str)*
      -
      - Cipher suite description.
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
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup cipher binding
      delegate_to: localhost
      citrix_adc_sslcipher_sslciphersuite_binding:
        nsip: ""
        nitro_user: ""
        nitro_pass: ""
    
        validate_certs: no
        state: absent
    
        ciphergroupname: test_cipher
        ciphername: TLS1.2-ECDHE-RSA-AES256-GCM-SHA384
        cipherpriority: "2"


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0'}
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
