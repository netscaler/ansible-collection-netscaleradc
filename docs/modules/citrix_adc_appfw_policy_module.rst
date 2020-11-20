:orphan:

.. _citrix_adc_appfw_policy_module:

citrix_adc_appfw_policy - Manage Citrix ADC Web Application Firewall policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

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

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

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
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - name

        *(str)*
      -
      - Name for the policy.

        Must begin with a letter, number, or the underscore character (_), and must contain only letters, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore Can be changed after the policy is created.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my policy" or 'my policy').

        Minimum length =  1
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
    * - profilename

        *(str)*
      -
      - Name of the application firewall profile to use if the policy matches.

        Minimum length =  1
    * - rule

        *(str)*
      -
      - Name of the Citrix ADC named rule, or a Citrix ADC expression, that the policy uses to determine to filter the connection through the application firewall with the designated profile.
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
