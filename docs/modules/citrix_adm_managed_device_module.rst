:orphan:

.. _citrix_adm_managed_device_module:

citrix_adm_managed_device - Manage Citrix ADM ADC instances.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
    * - agent_id

        *(str)*
      -
      - Agent Id.
    * - autoprovisioned

        *(bool)*
      -
      - Device is auto-provisioned or not.
    * - bearer_token

        *(str)*
      -
      - The Citrix Cloud bearer token.
    * - config_type

        *(int)*
      -
      - Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both.

         Maximum value =  
    * - customer_id

        *(str)*
      -
      - The Citrix Cloud customer id.
    * - datacenter_id

        *(str)*
      -
      - Datacenter Id is system generated key for data center.
    * - description

        *(str)*
      -
      - Description of managed device.

         Minimum length =  1

         Maximum length =  512
    * - device_family

        *(str)*
      -
      - Device Family.

         Minimum length =  1

         Maximum length =  64
    * - device_finger_print

        *(str)*
      -
      - Fingerprint/thumb-print from UMS public certificate for SSL communication.
    * - device_host_ip

        *(str)*
      -
      - Device Host IP Address for instance of type BLX ADC..

         Minimum length =  1

         Maximum length =  64
    * - discovery_time

        *(str)*
      -
      - discovery time.
    * - display_name

        *(str)*
      -
      - Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP.

         Minimum length =  1

         Maximum length =  128
    * - ent_bw_available

        *(int)*
      -
      - Enterprise Bandwidth configured.
    * - ent_bw_config

        *(int)*
      -
      - Enterprise Bandwidth configured.
    * - ent_bw_total

        *(int)*
      -
      - Enterprise Bandwidth Total.
    * - entity_tag

        *(list)*
      -
      - Array of tag_name and tag_value pair assocaited with an entity.
    * - file_location_path

        *(str)*
      -
      - File Location on Client for upload/download.

         Minimum length =  1
    * - file_name

        *(str)*
      -
      - File name which contains comma separated instances to be  discovered.

         Minimum length =  1

         Maximum length =  128
    * - gateway

        *(str)*
      -
      - Default Gateway of managed device.

         Minimum length =  1

         Maximum length =  64
    * - gateway_deployment

        *(bool)*
      -
      - Is this device acting as Gateway..
    * - gateway_ipv6

        *(str)*
      -
      - Gateway IPv6 Address.
    * - geo_support

        *(bool)*
      -
      - Is this device configured to support GEO location..
    * - hostname

        *(str)*
      -
      - Assign hostname to managed device, if this is not provided, name will be set as host name .

         Minimum length =  1

         Maximum length =  256
    * - httpxforwardedfor

        *(str)*
      -
      - HTTP x-Forwardedfor header flag..

         Minimum length =  1

         Maximum length =  10
    * - id

        *(str)*
      -
      - Id is system generated key for all the managed devices.
    * - instance_available

        *(int)*
      -
      - Instance license available.
    * - instance_classifier

        *(int)*
      -
      - Value based on which certain features may be enabled/disabled in ADM for the instance.
    * - instance_config

        *(int)*
      -
      - Instance license running.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_mode

        *(str)*
      -
      - Denotes state- primary,secondary,clip,clusternode.
    * - instance_total

        *(int)*
      -
      - Instance license.
    * - internal_annotation

        *(str)*
      -
      - Internal annotation used by ADM.Example, if a device is marked for delete.
    * - ip_address

        *(str)*
      -
      - IP Address for this managed device.

         Minimum length =  1

         Maximum length =  64
    * - ipv4_address

        *(str)*
      -
      - IPv4 Address.

         Minimum length =  1

         Maximum length =  64
    * - ipv6_address

        *(str)*
      -
      - IPv6 Address.
    * - is_autoscale_group

        *(bool)*
      -
      - Does this device belong to an Autoscale Group..
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - Boolean flag.

        Set to true when executing modules against the ADM service.
    * - is_ha_configured

        *(bool)*
      -
      - Is HA configured.
    * - is_managed

        *(bool)*
      -
      - Is Managed.
    * - isolation_policy

        *(str)*
      -
      - Isolation Policy of the Device.
    * - last_updated_time

        *(str)*
      -
      - Last Updated Time.
    * - license_edition

        *(str)*
      -
      - Edition of instance.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - mastools_version

        *(str)*
      -
      - Mastools version if the device is embedded agent.
    * - mgmt_ip_address

        *(str)*
      -
      - Management IP Address for this Managed Device.

         Minimum length =  1

         Maximum length =  64
    * - name

        *(str)*
      -
      - Name of managed device.

         Minimum length =  1

         Maximum length =  128
    * - netmask

        *(str)*
      -
      - Netmask of managed device.

         Minimum length =  1

         Maximum length =  64
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
    * - node_id

        *(str)*
      -
      - Node identification of a device.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - partition_id

        *(str)*
      -
      - ID of admin partition.
    * - partition_name

        *(str)*
      -
      - Citrix ADC Admin Partition Name.

         Maximum length =  512
    * - peer_device_ip

        *(str)*
      -
      - Peer Device IP address for instance of type BLX ADC..

         Minimum length =  1

         Maximum length =  64
    * - peer_host_device_ip

        *(str)*
      -
      - Peer Host Device IP Address for instance of type BLX ADC..

         Minimum length =  1

         Maximum length =  64
    * - plt_bw_available

        *(int)*
      -
      - Platinum Bandwidth Available.
    * - plt_bw_config

        *(int)*
      -
      - Platinum Bandwidth configured.
    * - plt_bw_total

        *(int)*
      -
      - Total Platinum Bandwidth.
    * - profile_name

        *(str)*
      -
      - Device Profile Name that is attached with this managed device.

         Minimum length =  1

         Maximum length =  128
    * - profile_password

        *(str)*
      -
      - Password specified by the user for this Citrix ADC Instance..

         Minimum length =  1

         Maximum length =  128
    * - profile_username

        *(str)*
      -
      - User Name specified by the user for this Citrix ADC Instance..

         Minimum length =  1

         Maximum length =  128
    * - provision_request_id

        *(str)*
      -
      - Value is set only if the instance was provisioned from Citrix ADM.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - servicepackage

        *(str)*
      -
      - Service Package Name of the device.
    * - sslvpn_config

        *(int)*
      -
      - sslvpn license maximum.
    * - sslvpn_total

        *(int)*
      -
      - sslvpn license.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - std_bw_available

        *(int)*
      -
      - Standard Bandwidth Available.
    * - std_bw_config

        *(int)*
      -
      - Standard Bandwidth running.
    * - std_bw_total

        *(int)*
      -
      - Standard Bandwidth.
    * - sysservices

        *(str)*
      -
      - System Services.
    * - template_interval

        *(int)*
      -
      - Template refresh interval.
    * - tr_task_id

        *(str)*
      -
      - Task Id used by Triton to identify NS.
    * - trust_id

        *(str)*
      -
      - Device ID obtained from trust service.
    * - type

        *(str)*
      -
      - Type of device, (Xen | NS).

         Minimum length =  1

         Maximum length =  64
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - vcpu_config

        *(int)*
      -
      - Number of vCPU allocated for the device.



Examples
--------

.. code-block:: yaml+jinja
    


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
    * - managed_device

        *(dict)*
      - success
      - Dictionary containing the attributes of the created ADC instance
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
