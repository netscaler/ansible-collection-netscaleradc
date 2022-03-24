:orphan:

.. _citrix_adm_provision_vpx_module:

citrix_adm_provision_vpx - Provision a VPX.
+++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Provision a VPX through the ADM provisioning service.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - bearer_token

        *(str)*
      -
      - The Citrix Cloud bearer token.
    * - customer_id

        *(str)*
      -
      - The Citrix Cloud customer id.
    * - fail_on_stall

        *(bool)*
      - Default:

        *True*
      - Boolean flag. Set to true for the module to fail when a status of job stalled is reported.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - Boolean flag.

        Set to true when executing modules against the ADM service.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Netscaler instance.

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
    * - poll_interval

        *(int)*
      - Default:

        *10*
      - Time interval in seconds between job poll operation.
    * - provisioning_profile

        *(dict)*
      -
      - Provisioning profile

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - deployment_details

                *(dict)*
              -
              - Deployment details

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - nitro
              -
              - Payload to create ADC instance which is to be sent to SDX.
            * - target
              -
              - IP of managed SDX where Citrix ADC is going to be provisioned.

            * - instance_type
              -
              - Only NetScaler is supported as of now
            * - mas_registration_details

                *(dict)*
              -
              - MAS registration details

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - access_profile_id
              -
              - Reference to Instance/Device Access Profile to be set for instance being provisioned.
            * - mas_agent_id
              -
              - Reference to MAS Agent that has to be used in order to add and manage provisioned instance in MAS.

            * - name
              -
              - Name of the ProvisioningProfile.
            * - site_id
              -
              - Reference to MAS site which has location info where instance has to be provisioned.
            * - type
              -
              - Platform type

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
    
    - name: Provision vpx
      delegate_to: localhost
      citrix.adm.citrix_adm_provision_vpx:
        nitro_protocol: https
        nsip: railay.adm.cloud.com
        customer_id: "{{ customer_id }}"
        is_cloud: true
        bearer_token: "{{ login_result.access_token }}"
    
        state: present
    
        provisioning_profile:
            instance_type: "NetScaler"
            name: "{{ vpx_name }}"
            type: sdx
            site_id: "cfa47930-f3f6-475f-9780-da93699f01cf"
            mas_registration_details:
                mas_agent_id: "12ea1595-9161-4f56-b1c7-bc953ced6e9e"
            instance_capacity_details:
                config_job_templates:
                    - "c4a977d1-5633-03e6-961f-eb4e99a93f85"
            deployment_details:
                sdx:
                    target: 10.222.74.135
                    nitro:
                        name: "{{ vpx_name }}"
                        ip_address: "{{ ipaddress }}"
                        config_type: 0
                        ipv4_address: "{{ ipaddress }}"
                        netmask: 255.255.255.192
                        gateway: 10.222.74.129
                        nexthop: ""
                        image_name: NSVPX-XEN-13.1-17.42_nc_64.xva
                        profile_name: nsroot_Notnsroot250
                        sync_operation: "false"
                        throughput_allocation_mode: "0"
                        throughput: "1000"
                        max_burst_throughput: "0"
                        burst_priority: "0"
                        license: Standard
                        number_of_acu: 0
                        number_of_scu: "0"
                        vm_memory_total: "2048"
                        pps: "1000000"
                        number_of_cores: "0"
                        l2_enabled: "false"
                        if_0_1: "true"
                        vlan_id_0_1: ""
                        if_0_2: "true"
                        vlan_id_0_2: ""
                        network_interfaces:
                          - port_name: LA/1
                            mac_address: ""
                            mac_mode: default
                            device_channel_name: ""
                            receiveuntagged: "true"
                            vlan_whitelist_array:
                              - "110"
                        nsvlan_id: ""
                        vlan_type: 1
                        nsvlan_tagged: "false"
                        nsvlan_interfaces: []


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
    * - mps_datacenter

        *(dict)*
      - success
      - Facts about the named datacenter or empty if not exists.
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
