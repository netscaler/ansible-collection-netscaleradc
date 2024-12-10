#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: nspbr
short_description: Configuration for Policy Based Routing(PBR) entry resource.
description: Configuration for Policy Based Routing(PBR) entry resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  interface:
    type: str
    description:
      - ID of an interface. The Citrix ADC compares the PBR only to the outgoing packets
        on the specified interface. If you do not specify any value, the appliance
        compares the PBR to the outgoing packets on all interfaces.
  action:
    type: str
    choices:
      - ALLOW
      - DENY
    description:
      - Action to perform on the outgoing IPv4 packets that match the PBR.
      - ''
      - 'Available settings function as follows:'
      - '* C(ALLOW) - The Citrix ADC sends the packet to the designated next-hop router.'
      - '* C(DENY) - The Citrix ADC applies the routing table for normal destination-based
        routing.'
  destip:
    type: bool
    description:
      - 'IP address or range of IP addresses to match against the destination IP address
        of an outgoing IPv4 packet.  In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  destipop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  destipval:
    type: str
    description:
      - 'IP address or range of IP addresses to match against the destination IP address
        of an outgoing IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  destport:
    type: bool
    description:
      - 'Port number or range of port numbers to match against the destination port
        number of an outgoing IPv4 packet. In the command line interface, separate
        the range with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  destportop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  destportval:
    type: str
    description:
      - 'Port number or range of port numbers to match against the destination port
        number of an outgoing IPv4 packet. In the command line interface, separate
        the range with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  detail:
    type: bool
    description:
      - To get a detailed view.
  iptunnel:
    type: bool
    description:
      - The Tunnel name.
  iptunnelname:
    type: str
    description:
      - The iptunnel name where packets need to be forwarded upon.
  monitor:
    type: str
    description:
      - The name of the monitor.(Can be only of type ping or ARP )
  msr:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor the route specified byte Next Hop parameter. This parameter is not
        applicable if you specify a link load balancing (LLB) virtual server name
        with the Next Hop parameter.
  name:
    type: str
    description:
      - Name for the PBR. Must begin with an ASCII alphabetic or underscore \(_\)
        character, and must contain only ASCII alphanumeric, underscore, hash \(\#\),
        period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\)
        characters. Cannot be changed after the PBR is created.
  nexthop:
    type: bool
    description:
      - IP address of the next hop router or the name of the link load balancing virtual
        server to which to send matching packets if action is set to ALLOW.
      - If you specify a link load balancing (LLB) virtual server, which can provide
        a backup if a next hop link fails, first make sure that the next hops bound
        to the LLB virtual server are actually next hops that are directly connected
        to the Citrix ADC. Otherwise, the Citrix ADC throws an error when you attempt
        to create the PBR. The next hop can be null to represent null routes
  nexthopval:
    type: str
    description:
      - The Next Hop IP address or gateway name.
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for this pbr rule. If ownernode is not specified
        then the pbr rule is treated as Striped pbr rule.
  priority:
    type: float
    description:
      - Priority of the PBR, which determines the order in which it is evaluated relative
        to the other PBRs. If you do not specify priorities while creating PBRs, the
        PBRs are evaluated in the order in which they are created.
  protocol:
    type: str
    choices:
      - ICMP
      - IGMP
      - TCP
      - EGP
      - IGP
      - ARGUS
      - UDP
      - RDP
      - RSVP
      - EIGRP
      - L2TP
      - ISIS
      - GGP
      - IPoverIP
      - ST
      - CBT
      - BBN-RCC-M
      - NVP-II
      - PUP
      - EMCON
      - XNET
      - CHAOS
      - MUX
      - DCN-MEAS
      - HMP
      - PRM
      - XNS-IDP
      - TRUNK-1
      - TRUNK-2
      - LEAF-1
      - LEAF-2
      - IRTP
      - ISO-TP4
      - NETBLT
      - MFE-NSP
      - MERIT-INP
      - SEP
      - 3PC
      - IDPR
      - XTP
      - DDP
      - IDPR-CMTP
      - TP++
      - IL
      - IPv6
      - SDRP
      - IPv6-Route
      - IPv6-Frag
      - IDRP
      - GRE
      - MHRP
      - BNA
      - ESP
      - AH
      - I-NLSP
      - SWIPE
      - NARP
      - MOBILE
      - TLSP
      - SKIP
      - ICMPV6
      - IPv6-NoNx
      - IPv6-Opts
      - Any-Host-Internal-Protocol
      - CFTP
      - Any-Local-Network
      - SAT-EXPAK
      - KRYPTOLAN
      - RVD
      - IPPC
      - Any-Distributed-File-System
      - TFTP
      - VISA
      - IPCV
      - CPNX
      - CPHB
      - WSN
      - PVP
      - BR-SAT-MO
      - SUN-ND
      - WB-MON
      - WB-EXPAK
      - ISO-IP
      - VMTP
      - SECURE-VM
      - VINES
      - TTP
      - NSFNET-IG
      - DGP
      - TCF
      - OSPFIGP
      - Sprite-RP
      - LARP
      - MTP
      - AX.25
      - IPIP
      - MICP
      - SCC-SP
      - ETHERIP
      - Any-Private-Encryption-Scheme
      - GMTP
      - IFMP
      - PNNI
      - PIM
      - ARIS
      - SCPS
      - QNX
      - A/N
      - IPComp
      - SNP
      - Compaq-Pe
      - IPX-in-IP
      - VRRP
      - PGM
      - Any-0-Hop-Protocol
      - ENCAP
      - DDX
      - IATP
      - STP
      - SRP
      - UTI
      - SMP
      - SM
      - PTP
      - FIRE
      - CRTP
      - CRUDP
      - SSCOPMCE
      - IPLT
      - SPS
      - PIPE
      - SCTP
      - FC
      - RSVP-E2E-IGNORE
      - Mobility-Header
      - UDPLite
    description:
      - Protocol, identified by protocol name, to match against the protocol of an
        outgoing IPv4 packet.
  protocolnumber:
    type: float
    description:
      - Protocol, identified by protocol number, to match against the protocol of
        an outgoing IPv4 packet.
  srcip:
    type: bool
    description:
      - 'IP address or range of IP addresses to match against the source IP address
        of an outgoing IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  srcipop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  srcipval:
    type: str
    description:
      - 'IP address or range of IP addresses to match against the source IP address
        of an outgoing IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  srcmac:
    type: str
    description:
      - MAC address to match against the source MAC address of an outgoing IPv4 packet.
  srcmacmask:
    type: str
    description:
      - Used to define range of Source MAC address. It takes string of 0 and 1, 0s
        are for exact match and 1s for wildcard. For matching first 3 bytes of MAC
        address, srcMacMask value "000000111111".
  srcport:
    type: bool
    description:
      - 'Port number or range of port numbers to match against the source port number
        of an outgoing IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  srcportop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  srcportval:
    type: str
    description:
      - 'Port number or range of port numbers to match against the source port number
        of an outgoing IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  vlan:
    type: float
    description:
      - ID of the VLAN. The Citrix ADC compares the PBR only to the outgoing packets
        on the specified VLAN. If you do not specify any interface ID, the appliance
        compares the PBR to the outgoing packets on all VLANs.
  vxlan:
    type: float
    description:
      - ID of the VXLAN. The Citrix ADC compares the PBR only to the outgoing packets
        on the specified VXLAN. If you do not specify any interface ID, the appliance
        compares the PBR to the outgoing packets on all VXLANs.
  vxlanvlanmap:
    type: str
    description:
      - The vlan to vxlan mapping to be applied for incoming packets over this pbr
        tunnel
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nspbr playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nspbr
      delegate_to: localhost
      netscaler.adc.nspbr:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: mgmt_pbr
        action: ALLOW
        srcip: true
        srcipop: '='
        srcipval: 10.189.64.50
        destip: true
        destipop: '!='
        destipval: 10.189.64.1-10.189.64.254
        nexthop: true
        nexthopval: 10.189.64.1
        priority: '10'
        kernelstate: SFAPPLIED61
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
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
