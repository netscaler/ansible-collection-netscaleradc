:orphan:

.. _citrix_adc_nsip_module:

citrix_adc_nsip - Manage Citrix ADC nsip address
++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.2.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADC nsip address




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - advertiseondefaultpartition

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Advertise VIPs from Shared VLAN on Default Partition.
    * - api_path

        *(str)*
      -
      - Base NITRO API path.

        Define only in case of an ADM service proxy call
    * - arp

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Respond to ARP requests for this IP address.
    * - arpowner

        *(str)*
      -
      - The arp owner in a Cluster for this IP address. It can vary from 0 to 31.
    * - arpresponse

        *(str)*
      - Choices:

          - NONE
          - ONE_VSERVER
          - ALL_VSERVERS
      - Respond to ARP requests for a Virtual IP (VIP) address on the basis of the states of the virtual associated with that VIP. Available settings function as follows:

        * NONE - The Citrix ADC responds to any ARP request for the VIP address, irrespective of the states the virtual servers associated with the address.

        * ONE VSERVER - The Citrix ADC responds to any ARP request for the VIP address if at least one of the virtual servers is in UP state.

        * ALL VSERVER - The Citrix ADC responds to any ARP request for the VIP address if all of the virtual servers are in UP state.
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - bgp

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Use this option to enable or disable BGP on this IP address for the entity.
    * - decrementttl

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Decrement TTL by 1 when ENABLED.This setting is applicable only for UDP traffic.
    * - disabled

        *(bool)*
      -
      - When set to ``true`` the nsip state will be set to ``disabled``.

        When set to ``false`` the nsip state will be set to ``enabled``.
    * - dynamicrouting

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow dynamic routing on this IP address. Specific to Subnet IP (SNIP) address.
    * - ftp

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow File Transfer Protocol (FTP) access to this IP address.
    * - gui

        *(str)*
      - Choices:

          - ENABLED
          - SECUREONLY
          - DISABLED
      - Allow graphical user interface (GUI) access to this IP address.
    * - hostroute

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Option to push the VIP to ZebOS routing table for Kernel route redistribution through dynamic routing
    * - hostrtgw

        *(str)*
      -
      - IP address of the gateway of the route for this VIP address.
    * - icmp

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Respond to ICMP requests for this IP address.
    * - icmpresponse

        *(str)*
      - Choices:

          - NONE
          - ONE_VSERVER
          - ALL_VSERVERS
          - VSVR_CNTRLD
      - Respond to ICMP requests for a Virtual IP (VIP) address on the basis of the states of the virtual associated with that VIP. Available settings function as follows:

        * NONE - The Citrix ADC responds to any ICMP request for the VIP address, irrespective of the states the virtual servers associated with the address.

        * ONE VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if at least one of associated virtual servers is in UP state.

        * ALL VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if all of the virtual servers are in UP state.

        * VSVR_CNTRLD - The behavior depends on the ICMP VSERVER RESPONSE setting on all the associated servers.

        The following settings can be made for the ICMP VSERVER RESPONSE parameter on a virtual server:

        * If you set ICMP VSERVER RESPONSE to PASSIVE on all virtual servers, Citrix ADC always responds.

        * If you set ICMP VSERVER RESPONSE to ACTIVE on all virtual servers, Citrix ADC responds if even one server is UP.

        * When you set ICMP VSERVER RESPONSE to ACTIVE on some and PASSIVE on others, Citrix ADC responds if one virtual server set to ACTIVE is UP.
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - ipaddress

        *(str)*
      -
      - IPv4 address to create on the Citrix ADC. Cannot be changed after the IP address is created.

        Minimum length =  1
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``

        When true and adm service is the api proxy the following option must also be defined: ``bearer_token``

        When true you must define a target ADC by defining any of the following parameters

        I(instance_ip)

        I(instance_id)

        I(instance_name)
    * - metric

        *(int)*
      -
      - Integer value to add to or subtract from the cost of the route advertised for the VIP address.

        Minimum value = ``-16777215``
    * - mgmtaccess

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow access to management applications on this IP address.
    * - netmask

        *(str)*
      -
      - Subnet mask associated with the IP address.
    * - networkroute

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Option to push the SNIP subnet to ZebOS routing table for Kernel route redistribution through dynamic protocol.
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
    * - ospf

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Use this option to enable or disable OSPF on this IP address for the entity.
    * - ospfarea

        *(str)*
      -
      - ID of the area in which the type1 link-state advertisements (LSAs) are to be advertised for this IP (VIP) address by the OSPF protocol running on the Citrix ADC. When this parameter is not set, the is advertised on all areas.

        Minimum value = ``0``

        Maximum value = ``4294967294``
    * - ospflsatype

        *(str)*
      - Choices:

          - TYPE1
          - TYPE5
      - Type of LSAs to be used by the OSPF protocol, running on the Citrix ADC, for advertising the route this VIP address.
    * - ownerdownresponse

        *(bool)*
      -
      - in cluster system, if the owner node is down, whether should it respond to icmp/arp.
    * - ownernode

        *(str)*
      -
      - The owner node in a Cluster for this IP address. Owner node can vary from 0 to 31. If ownernode is specified then the IP is treated as Striped IP.
    * - restrictaccess

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Block access to nonmanagement applications on this IP. This option is applicable for MIPs, SNIPs, and and is disabled by default. Nonmanagement applications can run on the underlying Citrix ADC Free BSD system.
    * - rip

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Use this option to enable or disable RIP on this IP address for the entity.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - snmp

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow Simple Network Management Protocol (SNMP) access to this IP address.
    * - ssh

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow secure shell (SSH) access to this IP address.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - tag

        *(str)*
      -
      - Tag value for the network/host route associated with this IP.
    * - td

        *(str)*
      -
      - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of TD id 4095 is used reserved for LSN use .

        Minimum value = ``0``

        Maximum value = ``4095``
    * - telnet

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Allow Telnet access to this IP address.
    * - type

        *(str)*
      - Choices:

          - SNIP
          - VIP
          - NSIP
          - GSLBsiteIP
          - CLIP
      - Type of the IP address to create on the Citrix ADC. Cannot be changed after the IP address is The following are the different types of Citrix ADC owned IP addresses:

        * A Subnet IP (SNIP) address is used by the Citrix ADC to communicate with the servers. The Citrix also uses the subnet IP address when generating its own packets, such as packets related to dynamic protocols, or to send monitor probes to check the health of the servers.

        * A Virtual IP (VIP) address is the IP address associated with a virtual server. It is the IP address which clients connect. An appliance managing a wide range of traffic may have many VIPs configured. of the attributes of the VIP address are customized to meet the requirements of the virtual server.

        * A GSLB site IP (GSLBIP) address is associated with a GSLB site. It is not mandatory to specify a address when you initially configure the Citrix ADC. A GSLBIP address is used only when you create a site.

        * A Cluster IP (CLIP) address is the management address of the cluster. All cluster configurations be performed by accessing the cluster through this IP address.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - vrid

        *(str)*
      -
      - A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This is used to set up Citrix ADCs in an active-active configuration using VRRP.

        Minimum value = ``1``

        Maximum value = ``255``
    * - vserver

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Use this option to set (enable or disable) the virtual server attribute for this IP address.
    * - vserverrhilevel

        *(str)*
      - Choices:

          - ONE_VSERVER
          - ALL_VSERVERS
          - NONE
          - VSVR_CNTRLD
      - Advertise the route for the Virtual IP (VIP) address on the basis of the state of the virtual servers with that VIP.

        * NONE - Advertise the route for the VIP address, regardless of the state of the virtual servers with the address.

        * ONE VSERVER - Advertise the route for the VIP address if at least one of the associated virtual is in UP state.

        * ALL VSERVER - Advertise the route for the VIP address if all of the associated virtual servers are UP state.

        * VSVR_CNTRLD - Advertise the route for the VIP address according to the RHIstate (RHI STATE) setting on all the associated virtual servers of the VIP address along with their states.

        When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated the VIP address:

        * If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route the VIP address.

        * If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the address if at least one of the associated virtual servers is in UP state.

        *If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is UP state.
    * - vserverrhimode

        *(str)*
      - Choices:

          - DYNAMIC_ROUTING
          - RISE
      - Advertise the route for the Virtual IP (VIP) address using dynamic routing protocols or using RISE

        * DYNMAIC_ROUTING - Advertise the route for the VIP address using dynamic routing protocols (default)

        * RISE - Advertise the route for the VIP address using RISE.



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
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0'}
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
