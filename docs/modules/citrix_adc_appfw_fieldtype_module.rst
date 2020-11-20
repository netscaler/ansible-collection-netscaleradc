:orphan:

.. _citrix_adc_appfw_fieldtype_module:

citrix_adc_appfw_fieldtype - Configuration for application firewall form field type resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Configuration for application firewall form field type resource.




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
      - Comment describing the type of field that this field type is intended to match.
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``true`` the server state will be set to ``disabled``.

        When set to ``false`` the server state will be set to ``enabled``.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
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
      - Name for the field type.

        Must begin with a letter, number, or the underscore character (_), and must contain only letters, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore Cannot be changed after the field type is added.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my field type" or 'my field type').

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
    * - nocharmaps

        *(bool)*
      -
      - will not show internal field types added as part of FieldFormat learn rules deployment.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - priority

        *(str)*
      -
      - Positive integer specifying the priority of the field type. A lower number specifies a higher Field types are checked in the order of their priority numbers.

        Minimum value = ``0``

        Maximum value = ``64000``
    * - regex

        *(str)*
      -
      - PCRE - format regular expression defining the characters and length allowed for this field type.

        Minimum length =  1
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
    
    - hosts: citrix_adc
    
      gather_facts: False
      tasks:
        - name: Setup an AppFW fieldtype
          delegate_to: localhost
          citrix_adc_appfw_fieldtype:
            nitro_user: nsroot
            nitro_pass: nsroot
            nsip: 192.168.1.2
            state: present
            name: test_field_type
            regex: test_.*regex
            priority: "100"
            comment: 'some comment'


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
