:orphan:

.. _citrix_adm_stylebook_module:

citrix_adm_stylebook - Create or delete Citrix ADM stylebooks.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.8.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Create or delete Citrix ADM stylebooks.
- Note that due to API limitations this module does not work with basic authentication.
- Instead use the I(nitro_auth_token) option.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - display_name

        *(str)*
      -
      - Display name of the StyleBook.

        Minimum length = 1

        Maximum length = 128
    * - instance_ip

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
    * - name

        *(str)*
      -
      - Name of the StyleBook.
    * - namespace

        *(str)*
      -
      - Namespace of the StyleBook.

        Minimum length = 1

        Maximum length = 32
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
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - source

        *(str)*
      -
      - Source definition of the StyleBook.

        Minimum length = 1

        Maximum length = 32
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
    * - version

        *(str)*
      -
      - Version of the StyleBook.

        Minimum length = 1

        Maximum length = 32



Examples
--------

.. code-block:: yaml+jinja
    
    vars:
    stylebook_contents: "{{ lookup('file', 'stylebook_sample.yaml') }}"
    
    - name: Setup stylebook
      delegate_to: localhost
      citrix_adm_stylebook:
        mas_ip: 192.168.1.1
        nitro_auth_token: "{{ login_result.session_id }}"
    
        state: present
    
        name: basic-lb-config
        namespace: com.example.stylebooks
        version: "0.1"
    
        source: "{{ stylebook_contents }}"


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
    * - stylebook

        *(dict)*
      - success
      - Dictionary containing the attributes of the created stylebook.
