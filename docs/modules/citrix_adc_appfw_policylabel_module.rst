:orphan:

.. _citrix_adc_appfw_policylabel_module:

citrix_adc_appfw_policylabel - Manage Citrix ADC Web Application Firewall policy labels.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADC Web Application Firewall policy labels.
- The module uses the NITRO API to make configuration changes to WAF policy labels on the target Citrix ADC.
- The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest




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

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - labelname

        *(str)*
      -
      - Name for the policy label. Must begin with a letter, number, or the underscore character (_), and contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals colon (:), and underscore characters. Can be changed after the policy label is created.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my policy label" or 'my policy label').
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
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
    * - policylabeltype

        *(str)*
      - Choices:

          - http_req
      - Type of transformations allowed by the policies bound to the label. Always http_req for application policy labels.
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
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup policy label
      delegate_to: localhost
      citrix_adc_appfw_policylabel:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: present
        labelname: test_label_name
        policylabeltype: http_req
    
    - name: Remove policy label
      delegate_to: localhost
      citrix_adc_appfw_policylabel:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: absent
        labelname: test_label_name
        policylabeltype: http_req
    


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
