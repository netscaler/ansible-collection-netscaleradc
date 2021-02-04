:orphan:

.. _citrix_adc_nitro_info_module:

citrix_adc_nitro_info - Retrieve information from various NITRO API endpoints
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.1.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Retrieve information from various NITRO API endpoints.
- The nitro information is returned at the C(nitro_info) key of the result variable.
- You must register the result to a variable to access the nitro information.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - args

        *(dict)*
      -
      - A dictionary which defines the args query parameter.
    * - attrs

        *(dict)*
      -
      - A dictionary which defines the attrs query parameter.
    * - endpoint

        *(str)*
      -
      - The endpoint for which we retrieve information.
    * - filter

        *(dict)*
      -
      - A dictionary which defines the filter query parameter.
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*
      -
      - The IP address of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
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
    * - nitro_empty_errorcodes

        *(list)*
      -
      - A list of errorcodes which signify that no data exist for this endpoint.

        The NITRO error will not cause the module execution to fail.
    * - nitro_info_key

        *(str)*
      -
      - The key which contains the requested info.

        If not set it will default to the value of the ``endpoint`` option.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Citrix ADC node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the Nitro API objects.
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The IP address of the Citrix ADC or Citrix ADM instance where the Nitro API calls will be made.

        The port can be specified with the colon ``:``. E.g. ``192.168.1.1:555``.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Get sslparameters
      delegate_to: localhost
      citrix_adc_nitro_info:
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        nsip: '{{ nsip }}'
        validate_certs: no
        endpoint: sslparameter
    
    - name: Get a resource with args
      delegate_to: localhost
      citrix_adc_nitro_info:
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        nsip: '{{ nsip }}'
        validate_certs: no
        endpoint: interface
        args:
          id: LO/1
        nitro_info_key: Interface
    
    - name: Get an empty errorcode
      delegate_to: localhost
      citrix_adc_nitro_info:
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        nsip: '{{ nsip }}'
        validate_certs: no
        endpoint: dnsnsrec/nosuchdomain.com
        nitro_empty_errorcodes:
          - 258
        nitro_info_key: dnsnsrec


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
    * - nitro_info

        *(list)*
      - success
      - ['The result of the nitro request.', 'If no data were found an empty list will be returned.', 'Depending on the endpoint this will either be a list of dictionaries or a standalone dictionary.']
