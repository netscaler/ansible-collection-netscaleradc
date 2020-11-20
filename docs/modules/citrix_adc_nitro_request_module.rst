:orphan:

.. _citrix_adc_nitro_request_module:

citrix_adc_nitro_request - Issue Nitro API requests to a Netscaler instance.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Issue Nitro API requests to a Netscaler instance.
- This is intended to be a short hand for using the uri Ansible module to issue the raw HTTP requests directly.
- It provides consistent return values and has no other dependencies apart from the base Ansible runtime environment.
- This module is intended to run either on the Ansible control node or a bastion (jumpserver) with access to the actual Netscaler instance
- Note. This module does not check the target Citrix ADC if a configuration change has actually taken place. It will instead always report a I(changed=yes) status.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - action

        *(str)*
      -
      - The action to perform when the ``operation`` value is set to ``action``.

        Some common values for this parameter are ``enable``, ``disable``, ``rename``.
    * - args

        *(dict)*
      -
      - A dictionary which defines the key arguments by which we will select the Nitro object to operate on.

        It is required for the following ``operation`` values: ``get_by_args``, ``'delete_by_args'``.
    * - attributes

        *(dict)*
      -
      - The attributes of the Nitro object we are operating on.

        It is required for the following ``operation`` values: ``add``, ``update``, ``action``.
    * - expected_nitro_errorcode

        *(list)*
      - Default:

        *[0]*
      - A list of numeric values that signify that the operation was successful.
    * - filter

        *(dict)*
      -
      - A dictionary which defines the filter with which to refine the Nitro objects returned by the ``get_filtered`` ``operation``.
    * - idempotent

        *(bool)*
      - Default:

        *False*
      - Add the idempotent flag for ``operation=add`` and ``operation=update`` requests.
    * - instance_id

        *(str)*
      -
      - The id of the target Netscaler instance when issuing a Nitro request through a MAS proxy.
    * - instance_ip

        *(str)*
      -
      - The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy.
    * - instance_name

        *(str)*
      -
      - The name of the target Netscaler instance when issuing a Nitro request through a MAS proxy.
    * - name

        *(str)*
      -
      - The name of the resource we are operating on.

        It is required for the following ``operation`` values: ``update``, ``get``, ``delete``.
    * - nitro_auth_token

        *(str)*
      -
      - The authentication token provided by the ``mas_login`` operation. It is required when issuing Nitro API calls through a MAS proxy.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Netscaler node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the Nitro API objects.
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Netscaler node.
    * - nsip

        *(str)*
      -
      - The IP address of the Netscaler or MAS instance where the Nitro API calls will be made.

        The port can be specified with the colon ``:``. E.g. ``192.168.1.1:555``.
    * - operation

        *(str)*
      - Choices:

          - add
          - update
          - get
          - get_by_args
          - get_filtered
          - get_all
          - delete
          - delete_by_args
          - count
          - mas_login
          - save_config
          - action
      - Define the Nitro operation that we want to perform.
    * - resource

        *(str)*
      -
      - The type of resource we are operating on.

        It is required for all ``operation`` values except ``mas_login`` and ``save_config``.
    * - timeout

        *(int)*
      - Default:

        *45*
      - Timeout for the NITRO HTTP request.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Add a server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: add
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.1
    
    - name: Update server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: update
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.2
    
    - name: Get server
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get
        resource: server
        name: test-server-1
    
    - name: Delete server
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: delete
        resource: server
        name: test-server-1
    
    - name: Rename server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: action
        action: rename
        resource: server
        attributes:
          name: test-server-1
          newname: test-server-2
    
    - name: Get server by args
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get_by_args
        resource: server
        args:
          name: test-server-1
    
    - name: Get server by filter
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get_filtered
        resource: server
        filter:
          ipaddress: 192.168.1.2
    
    # Doing a NITRO request through MAS.
    # Requires to have an authentication token from the mas_login and used as the nitro_auth_token parameter
    # Also nsip is the MAS address and the target Netscaler IP must be defined with instance_ip
    # The rest of the task arguments remain the same as when issuing the NITRO request directly to a Netscaler instance.
    
    - name: Do mas login
      delegate_to: localhost
      register: login_result
      citrix_adc_nitro_request:
        nsip: "{{ mas_ip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: mas_login
    
    - name: Add resource through MAS proxy
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ mas_ip }}"
        nitro_auth_token: "{{ login_result.nitro_auth_token }}"
        instance_ip: "{{ nsip }}"
        operation: add
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.7


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - http_response_body

        *(str)*
      - always
      - A string with the actual HTTP response body content if existent. If there is no HTTP response body it is an empty string.

        **Sample:**

        { errorcode: 0, message: Done, severity: NONE }
    * - http_response_data

        *(dict)*
      - always
      - A dictionary that contains all the HTTP response's data.

        **Sample:**

        status: 200
    * - nitro_auth_token

        *(str)*
      - when applicable
      - The token returned by the C(mas_login) operation when succesful.

        **Sample:**

        ##E8D7D74DDBD907EE579E8BB8FF4529655F22227C1C82A34BFC93C9539D66
    * - nitro_errorcode

        *(int)*
      - always
      - A numeric value containing the return code of the NITRO operation. When 0 the operation is succesful. Any non zero value indicates an error.

        **Sample:**

        0
    * - nitro_message

        *(str)*
      - always
      - A string containing a human readable explanation for the NITRO operation result.

        **Sample:**

        Success
    * - nitro_object

        *(list)*
      - when applicable
      - The object returned from the NITRO operation. This is applicable to the various get operations which return an object.

        **Sample:**

        [{'ipaddress': '192.168.1.8', 'ipv6address': 'NO', 'maxbandwidth': '0', 'name': 'test-server-1', 'port': 0, 'sp': 'OFF', 'state': 'ENABLED'}]
    * - nitro_severity

        *(str)*
      - always
      - A string describing the severity of the NITRO operation error or NONE.

        **Sample:**

        NONE
