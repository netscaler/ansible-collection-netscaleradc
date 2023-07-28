#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: nsip6
short_description: Configuration for ip6 resource.
description: Configuration for ip6 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  advertiseondefaultpartition:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Advertise VIPs from Shared VLAN on Default Partition
    type: str
    default: DISABLED
  decrementhoplimit:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Decrement Hop Limit by 1 when C(ENABLED).This setting is applicable only for
        UDP traffic.
    type: str
    default: DISABLED
  dynamicrouting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow dynamic routing on this IP address. Specific to Subnet IPv6 (SNIP6)
        address.
    type: str
    default: DISABLED
  ftp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow File Transfer Protocol (FTP) access to this IP address.
    type: str
    default: ENABLED
  gui:
    choices:
      - ENABLED
      - SECUREONLY
      - DISABLED
    description:
      - Allow graphical user interface (GUI) access to this IP address.
    type: str
    default: ENABLED
  hostroute:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to push the VIP6 to ZebOS routing table for Kernel route redistribution
        through dynamic routing protocols.
    type: str
  icmp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Respond to ICMP requests for this IP address.
    type: str
    default: ENABLED
  ip6hostrtgw:
    description:
      - 'IPv6 address of the gateway for the route. If Gateway is not set, VIP uses
        :: as the gateway.'
    type: str
  ipv6address:
    description:
      - IPv6 address to create on the Citrix ADC.
    type: str
  map:
    description:
      - Mapped IPV4 address for the IPV6 address.
    type: str
  metric:
    description:
      - Integer value to add to or subtract from the cost of the route advertised
        for the VIP6 address.
    type: int
  mgmtaccess:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow access to management applications on this IP address.
    type: str
    default: DISABLED
  mptcpadvertise:
    choices:
      - true
      - false
    description:
      - If enabled, this IP will be advertised by Citrix ADC to MPTCP enabled clients
        as part of ADD_ADDR option.
    type: str
  nd:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Respond to Neighbor Discovery (ND) requests for this IP address.
    type: str
    default: ENABLED
  ndowner:
    description:
      - NdOwner in Cluster for VIPS and Striped SNIPS
    type: int
    default: 255
  networkroute:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to push the SNIP6 subnet to ZebOS routing table for Kernel route redistribution
        through dynamic routing protocol.
    type: str
  ospf6lsatype:
    choices:
      - INTRA_AREA
      - EXTERNAL
    description:
      - Type of LSAs to be used by the IPv6 OSPF protocol, running on the Citrix ADC,
        for advertising the route for the VIP6 address.
    type: str
    default: EXTERNAL
  ospfarea:
    description:
      - ID of the area in which the Intra-Area-Prefix LSAs are to be advertised for
        the VIP6 address by the IPv6 OSPF protocol running on the Citrix ADC. When
        ospfArea is not set, VIP6 is advertised on all areas.
    type: int
    default: -1
  ownerdownresponse:
    choices:
      - true
      - false
    description:
      - in cluster system, if the owner node is down, whether should it respond to
        icmp/arp
    type: str
    default: true
  ownernode:
    description:
      - ID of the cluster node for which you are adding the IP address. Must be used
        if you want the IP address to be active only on the specific node. Can be
        configured only through the cluster IP address. Cannot be changed after the
        IP address is created.
    type: int
    default: 255
  restrictaccess:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Block access to nonmanagement applications on this IP address. This option
        is applicable forMIP6s, SNIP6s, and NSIP6s, and is disabled by default. Nonmanagement
        applications can run on the underlying Citrix ADC Free BSD operating system.
    type: str
    default: DISABLED
  scope:
    choices:
      - global
      - link-local
    description:
      - Scope of the IPv6 address to be created. Cannot be changed after the IP address
        is created.
    type: str
    default: global
  snmp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow Simple Network Management Protocol (SNMP) access to this IP address.
    type: str
    default: ENABLED
  ssh:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow secure Shell (SSH) access to this IP address.
    type: str
    default: ENABLED
  state:
    choices:
      - DISABLED
      - ENABLED
    description:
      - Enable or disable the IP address.
    type: str
    default: ENABLED
  tag:
    description:
      - Tag value for the network/host route associated with this IP.
    type: int
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  telnet:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow Telnet access to this IP address.
    type: str
    default: ENABLED
  type:
    choices:
      - NSIP
      - VIP
      - SNIP
      - GSLBsiteIP
      - ADNSsvcIP
      - RADIUSListenersvcIP
      - CLIP
    description:
      - Type of IP address to be created on the Citrix ADC. Cannot be changed after
        the IP address is created.
    type: str
    default: SNIP
  vlan:
    description:
      - The VLAN number.
    type: int
  vrid6:
    description:
      - A positive integer that uniquely identifies a VMAC address for binding to
        this VIP address. This binding is used to set up Citrix ADCs in an active-active
        configuration using VRRP.
    type: int
  vserver:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the state of all the virtual servers associated with this
        VIP6 address.
    type: str
    default: ENABLED
  vserverrhilevel:
    choices:
      - ONE_VSERVER
      - ALL_VSERVERS
      - NONE
      - VSVR_CNTRLD
    description:
      - Advertise or do not advertise the route for the Virtual IP (VIP6) address
        on the basis of the state of the virtual servers associated with that VIP6.
      - '* C(NONE) - Advertise the route for the VIP6 address, irrespective of the
        state of the virtual servers associated with the address.'
      - '* ONE VSERVER - Advertise the route for the VIP6 address if at least one
        of the associated virtual servers is in UP state.'
      - '* ALL VSERVER - Advertise the route for the VIP6 address if all of the associated
        virtual servers are in UP state.'
      - '* C(VSVR_CNTRLD).   Advertise the route for the VIP address according to
        the  RHIstate (RHI STATE) parameter setting on all the associated virtual
        servers of the VIP address along with their states.'
      - ''
      - 'When Vserver RHI Level (RHI) parameter is set to C(VSVR_CNTRLD), the following
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
