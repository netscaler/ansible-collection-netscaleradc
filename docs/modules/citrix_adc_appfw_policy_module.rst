:orphan:

.. _citrix_adc_appfw_policy_module:

citrix_adc_appfw_policy - Manage Citrix ADC Web Application Firewall policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.8.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADC Web Application Firewall policies.
- The module uses the NITRO API to make configuration changes to WAF policies on a target Citrix ADC.
- The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - comment

        *(str)*
      -
      - Any comments to preserve information about the policy for later reference.
    * - instance_ip

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - logaction

        *(str)*
      -
      - Where to log information for connections that match this policy.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - name

        *(str)*
      -
      - Name for the policy. 

        Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and characters. Can be changed after the policy is created.

        

        The following requirement applies only to the NetScaler CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks \(for "my policy" or 'my policy'\).
    * - nitro_auth_token

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol
      - Choices:

          - http (*default*)
          - https
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - profilename

        *(str)*
      -
      - Name of the application firewall profile to use if the policy matches.
    * - rule

        *(str)*
      -
      - Name of the NetScaler named rule, or a NetScaler default syntax expression, that the policy uses to whether to filter the connection through the application firewall with the designated profile.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - state
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - validate_certs
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup appfw policy
      delegate_to: localhost
      citrix_adc_appfw_policy:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: present
        name: policy_integration_test
        rule: 'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")'
        profilename: APPFW_BLOCK
        comment: 'policy test comment'
    
    - name: Remove appfw policy
      delegate_to: localhost
      citrix_adc_appfw_policy:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: absent
        name: policy_integration_test


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
