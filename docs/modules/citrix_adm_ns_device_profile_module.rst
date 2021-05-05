:orphan:

.. _citrix_adm_ns_device_profile_module:

citrix_adm_ns_device_profile - Manage Citrix ADM ADC instances.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADM ADC instances.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - cb_profile_name

        *(str)*
      -
      - Profile Name, This is one of the already created Citrix SD-WAN profiles.
    * - host_password

        *(str)*
      -
      - Host Password for this profile.Used for BLX form factor of ADC.

         Minimum length =  1

         Maximum length =  127

        This attribute cannot be updated. Delete and recreate the profile instead.
    * - host_username

        *(str)*
      -
      - Host User Name for this profile.Used for BLX form factor of ADC.

         Minimum length =  1

         Maximum length =  127
    * - http_port

        *(str)*
      -
      - HTTP port to connect to the device.
    * - https_port

        *(str)*
      -
      - HTTPS port to connect to the device.
    * - id

        *(str)*
      -
      - Id is system generated key for all the device profiles.
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
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - max_wait_time_reboot

        *(str)*
      -
      - Max waiting time to reboot Citrix ADC.
    * - name

        *(str)*
      -
      - Profile Name.

         Minimum length =  1

         Maximum length =  128
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
    * - ns_profile_name

        *(str)*
      -
      - Profile Name, This is one of the already created Citrix ADC profiles.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - passphrase

        *(str)*
      -
      - Passphrase with which private key is encrypted.

        This attribute cannot be updated. Delete and recreate the profile instead.
    * - password

        *(str)*
      -
      - Instance credentials.Password for this profile.

         Minimum length =  1

         Maximum length =  127

        This attribute cannot be updated. Delete and recreate the profile instead.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - snmpauthpassword

        *(str)*
      -
      - SNMP v3 auth password for this profile.

         Minimum length =  8

         Maximum length =  31

        This attribute cannot be updated. Delete and recreate the profile instead.
    * - snmpauthprotocol

        *(str)*
      -
      - SNMP v3 auth protocol for this profile.
    * - snmpcommunity

        *(str)*
      -
      - SNMP community for this profile.

         Maximum length =  31
    * - snmpprivpassword

        *(str)*
      -
      - SNMP v3 priv password for this profile.

         Minimum length =  8

         Maximum length =  31

        This attribute cannot be updated. Delete and recreate the profile instead.
    * - snmpprivprotocol

        *(str)*
      -
      - SNMP v3 priv protocol for this profile.
    * - snmpsecuritylevel

        *(str)*
      -
      - SNMP v3 security level for this profile.
    * - snmpsecurityname

        *(str)*
      -
      - SNMP v3 security name for this profile.

         Maximum length =  31
    * - snmpversion

        *(str)*
      -
      - SNMP version for this profile.
    * - ssh_port

        *(str)*
      -
      - SSH port to connect to the device.
    * - ssl_cert

        *(str)*
      -
      - SSL Certificate for certificate based authentication.
    * - ssl_private_key

        *(str)*
      -
      - SSL Private Key for key based authentication.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - svm_ns_comm

        *(str)*
      -
      - Communication protocol (http or https) with Instances.

         Minimum length =  1

         Maximum length =  10
    * - type

        *(str)*
      -
      - Profile Type, This must be with in specified supported instance types:

         Minimum length =  1

         Maximum length =  128
    * - use_global_setting_for_communication_with_ns

        *(bool)*
      -
      - True, if the communication with Instance needs to be global and not device specific.
    * - username

        *(str)*
      -
      - Instance credentials.Username provided in the profile will be used to contact the instance.

         Minimum length =  1

         Maximum length =  127
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    citrix_adm_ns_device_profile:
      adm_ip: 10.222.74.111
      adm_user: nsroot
      adm_pass: nsroot
    
      state: present
    
      name: ansible_profile
      username: nsroot
      password: password1234
      host_password: otherpassword
      http_port: 9080


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
    * - ns_device_profile

        *(dict)*
      - success
      - Dictionary containing the attributes of the created profile
