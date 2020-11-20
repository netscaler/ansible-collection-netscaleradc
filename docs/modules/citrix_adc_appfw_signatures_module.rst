:orphan:

.. _citrix_adc_appfw_signatures_module:

citrix_adc_appfw_signatures - Configuration for configured confidential form fields resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Configuration for configured confidential form fields resource.




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
      - Any comments to preserve information about the signatures object.

        Maximum length =  128
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
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - merge

        *(bool)*
      -
      - Merges the existing Signature with new signature rules.
    * - mergedefault

        *(bool)*
      -
      - Merges signature file with default signature file.
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
    * - overwrite

        *(bool)*
      -
      - Overwrite any existing signatures object of the same name.
    * - preservedefactions

        *(bool)*
      -
      - preserves def actions of signature rules.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - sha1

        *(str)*
      -
      - File path for sha1 file to validate signature file.

        Minimum length =  1

        Maximum length =  2047
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
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
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



Examples
--------

.. code-block:: yaml+jinja
    
    - hosts: citrix_adc
    
      gather_facts: False
      tasks:
        - name: Setup confidential field id
          delegate_to: localhost
          citrix_adc_appfw_signatures:
            nitro_user: nsroot
            nitro_pass: nsroot
            nsip: 192.168.1.2
            state: present
            fieldname: signatures_integration_test
            url: 'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")'
            isregex: REGEX
            comment: 'conf id field comment'


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
