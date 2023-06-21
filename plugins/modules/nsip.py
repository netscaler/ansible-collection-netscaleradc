#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: nsip
short_description: Configuration for ip resource.
description: Configuration for ip resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  advertiseondefaultpartition:
    description:
      - Advertise VIPs from Shared VLAN on Default Partition.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  arp:
    description:
      - Respond to ARP requests for this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  arpowner:
    description:
      - The arp owner in a Cluster for this IP address. It can vary from 0 to 31.
    type: int
    default: 255
  arpresponse:
    description:
      - 'Respond to ARP requests for a Virtual IP (VIP) address on the basis of the
        states of the virtual servers associated with that VIP. Available settings
        function as follows:'
      - ''
      - '* NONE - The Citrix ADC responds to any ARP request for the VIP address,
        irrespective of the states of the virtual servers associated with the address.'
      - '* ONE VSERVER - The Citrix ADC responds to any ARP request for the VIP address
        if at least one of the associated virtual servers is in UP state.'
      - '* ALL VSERVER - The Citrix ADC responds to any ARP request for the VIP address
        if all of the associated virtual servers are in UP state.'
    type: str
    default: 5
    choices:
      - NONE
      - ONE_VSERVER
      - ALL_VSERVERS
  bgp:
    description:
      - Use this option to enable or disable BGP on this IP address for the entity.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  decrementttl:
    description:
      - Decrement TTL by 1 when ENABLED.This setting is applicable only for UDP traffic.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dynamicrouting:
    description:
      - Allow dynamic routing on this IP address. Specific to Subnet IP (SNIP) address.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ftp:
    description:
      - Allow File Transfer Protocol (FTP) access to this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  gui:
    description:
      - Allow graphical user interface (GUI) access to this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - SECUREONLY
      - DISABLED
  hostroute:
    description:
      - Option to push the VIP to ZebOS routing table for Kernel route redistribution
        through dynamic routing protocols
    type: str
    choices:
      - ENABLED
      - DISABLED
  hostrtgw:
    description:
      - IP address of the gateway of the route for this VIP address.
    type: str
    default: -1
  icmp:
    description:
      - Respond to ICMP requests for this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  icmpresponse:
    description:
      - 'Respond to ICMP requests for a Virtual IP (VIP) address on the basis of the
        states of the virtual servers associated with that VIP. Available settings
        function as follows:'
      - '* NONE - The Citrix ADC responds to any ICMP request for the VIP address,
        irrespective of the states of the virtual servers associated with the address.'
      - '* ONE VSERVER - The Citrix ADC responds to any ICMP request for the VIP address
        if at least one of the associated virtual servers is in UP state.'
      - '* ALL VSERVER - The Citrix ADC responds to any ICMP request for the VIP address
        if all of the associated virtual servers are in UP state.'
      - '* VSVR_CNTRLD - The behavior depends on the ICMP VSERVER RESPONSE setting
        on all the associated virtual servers.'
      - ''
      - 'The following settings can be made for the ICMP VSERVER RESPONSE parameter
        on a virtual server:'
      - '* If you set ICMP VSERVER RESPONSE to PASSIVE on all virtual servers, Citrix
        ADC always responds.'
      - '* If you set ICMP VSERVER RESPONSE to ACTIVE on all virtual servers, Citrix
        ADC responds if even one virtual server is UP.'
      - '* When you set ICMP VSERVER RESPONSE to ACTIVE on some and PASSIVE on others,
        Citrix ADC responds if even one virtual server set to ACTIVE is UP.'
    type: str
    default: 5
    choices:
      - NONE
      - ONE_VSERVER
      - ALL_VSERVERS
      - VSVR_CNTRLD
  ipaddress:
    description:
      - IPv4 address to create on the Citrix ADC. Cannot be changed after the IP address
        is created.
    type: str
  metric:
    description:
      - Integer value to add to or subtract from the cost of the route advertised
        for the VIP address.
    type: int
  mgmtaccess:
    description:
      - Allow access to management applications on this IP address.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  mptcpadvertise:
    description:
      - If enabled, this IP will be advertised by Citrix ADC to MPTCP enabled clients
        as part of ADD_ADDR option.
    type: str
    choices:
      - true
      - false
  netmask:
    description:
      - Subnet mask associated with the IP address.
    type: str
  networkroute:
    description:
      - Option to push the SNIP subnet to ZebOS routing table for Kernel route redistribution
        through dynamic routing protocol.
    type: str
    choices:
      - ENABLED
      - DISABLED
  ospf:
    description:
      - Use this option to enable or disable OSPF on this IP address for the entity.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ospfarea:
    description:
      - ID of the area in which the type1 link-state advertisements (LSAs) are to
        be advertised for this virtual IP (VIP)  address by the OSPF protocol running
        on the Citrix ADC.  When this parameter is not set, the VIP is advertised
        on all areas.
    type: int
    default: -1
  ospflsatype:
    description:
      - Type of LSAs to be used by the OSPF protocol, running on the Citrix ADC, for
        advertising the route for this VIP address.
    type: str
    default: TYPE5
    choices:
      - TYPE1
      - TYPE5
  ownerdownresponse:
    description:
      - in cluster system, if the owner node is down, whether should it respond to
        icmp/arp
    type: str
    default: true
    choices:
      - true
      - false
  ownernode:
    description:
      - The owner node in a Cluster for this IP address. Owner node can vary from
        0 to 31. If ownernode is not specified then the IP is treated as Striped IP.
    type: int
    default: 255
  restrictaccess:
    description:
      - Block access to nonmanagement applications on this IP. This option is applicable
        for MIPs, SNIPs, and NSIP, and is disabled by default. Nonmanagement applications
        can run on the underlying Citrix ADC Free BSD operating system.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  rip:
    description:
      - Use this option to enable or disable RIP on this IP address for the entity.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  snmp:
    description:
      - Allow Simple Network Management Protocol (SNMP) access to this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  ssh:
    description:
      - Allow secure shell (SSH) access to this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  state:
    description:
      - Enable or disable the IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tag:
    description:
      - Tag value for the network/host route associated with this IP.
    type: int
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0. TD id 4095 is used reserved
        for  LSN use
    type: int
  telnet:
    description:
      - Allow Telnet access to this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  type:
    description:
      - 'Type of the IP address to create on the Citrix ADC. Cannot be changed after
        the IP address is created. The following are the different types of Citrix
        ADC owned IP addresses:'
      - '* A Subnet IP (SNIP) address is used by the Citrix ADC to communicate with
        the servers. The Citrix ADC also uses the subnet IP address when generating
        its own packets, such as packets related to dynamic routing protocols, or
        to send monitor probes to check the health of the servers.'
      - '* A Virtual IP (VIP) address is the IP address associated with a virtual
        server. It is the IP address to which clients connect. An appliance managing
        a wide range of traffic may have many VIPs configured. Some of the attributes
        of the VIP address are customized to meet the requirements of the virtual
        server.'
      - '* A GSLB site IP (GSLBIP) address is associated with a GSLB site. It is not
        mandatory to specify a GSLBIP address when you initially configure the Citrix
        ADC. A GSLBIP address is used only when you create a GSLB site.'
      - '* A Cluster IP (CLIP) address is the management address of the cluster. All
        cluster configurations must be performed by accessing the cluster through
        this IP address.'
    type: str
    default: SNIP
    choices:
      - SNIP
      - VIP
      - NSIP
      - HostIP
      - GSLBsiteIP
      - CLIP
  vrid:
    description:
      - A positive integer that uniquely identifies a VMAC address for binding to
        this VIP address. This binding is used to set up Citrix ADCs in an active-active
        configuration using VRRP.
    type: int
  vserver:
    description:
      - Use this option to set (enable or disable) the virtual server attribute for
        this IP address.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  vserverrhilevel:
    description:
      - Advertise the route for the Virtual IP (VIP) address on the basis of the state
        of the virtual servers associated with that VIP.
      - '* NONE - Advertise the route for the VIP address, regardless of the state
        of the virtual servers associated with the address.'
      - '* ONE VSERVER - Advertise the route for the VIP address if at least one of
        the associated virtual servers is in UP state.'
      - '* ALL VSERVER - Advertise the route for the VIP address if all of the associated
        virtual servers are in UP state.'
      - '* VSVR_CNTRLD - Advertise the route for the VIP address according to the  RHIstate
        (RHI STATE) parameter setting on all the associated virtual servers of the
        VIP address along with their states.'
      - ''
      - 'When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following
        are different RHI behaviors for the VIP address on the basis of RHIstate (RHI
        STATE) settings on the virtual servers associated with the VIP address:'
      - ' * If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC
        always advertises the route for the VIP address.'
      - ' * If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC
        advertises the route for the VIP address if at least one of the associated
        virtual servers is in UP state.'
      - ' *If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix
        ADC advertises the route for the VIP address if at least one of the associated
        virtual servers, whose RHI STATE set to ACTIVE, is in UP state.'
    type: str
    default: ONE_VSERVER
    choices:
      - ONE_VSERVER
      - ALL_VSERVERS
      - NONE
      - VSVR_CNTRLD
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
failed:
    description: Indicates if the module failed or not
    returned: always
    type: bool
    sample: false
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
