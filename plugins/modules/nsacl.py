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
module: nsacl
short_description: Configuration for ACL entry resource.
description: Configuration for ACL entry resource.
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
      - renamed
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
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  interface:
    type: str
    description:
      - ID of an interface. The Citrix ADC applies the ACL rule only to the incoming
        packets from the specified interface. If you do not specify any value, the
        appliance applies the ACL rule to the incoming packets of all interfaces.
  aclaction:
    type: str
    choices:
      - BRIDGE
      - DENY
      - ALLOW
    description:
      - Action to perform on incoming IPv4 packets that match the extended ACL rule.
      - 'Available settings function as follows:'
      - '* C(ALLOW) - The Citrix ADC processes the packet.'
      - '* C(BRIDGE) - The Citrix ADC bridges the packet to the destination without
        processing it.'
      - '* C(DENY) - The Citrix ADC drops the packet.'
  aclname:
    type: str
    description:
      - Name for the extended ACL rule. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  destip:
    type: bool
    description:
      - 'IP address or range of IP addresses to match against the destination IP address
        of an incoming IPv4 packet.  In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  destipdataset:
    type: str
    description:
      - Policy dataset which can have multiple IP ranges bound to it.
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
        of an incoming IPv4 packet.  In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  destport:
    type: bool
    description:
      - 'Port number or range of port numbers to match against the destination port
        number of an incoming IPv4 packet. In the command line interface, separate
        the range with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  destportdataset:
    type: str
    description:
      - Policy dataset which can have multiple port ranges bound to it.
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
        number of an incoming IPv4 packet. In the command line interface, separate
        the range with a hyphen. For example: 40-90.'
      - ''
      - 'Note: The destination port can be specified only for TCP and UDP protocols.'
  dfdhash:
    type: str
    choices:
      - SIP-SPORT-DIP-DPORT
      - SIP
      - DIP
      - SIP-DIP
      - SIP-SPORT
      - DIP-DPORT
    description:
      - Specifies the type hashmethod to be applied, to steer the packet to the FP
        of the packet.
  established:
    type: bool
    description:
      - Allow only incoming TCP packets that have the ACK or RST bit set, if the action
        set for the ACL rule is ALLOW and these packets match the other conditions
        in the ACL rule.
  icmpcode:
    type: float
    description:
      - Code of a particular ICMP message type to match against the ICMP code of an
        incoming ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE
        messages, specify 3 as the ICMP type and 1 as the ICMP code.
      - ''
      - If you set this parameter, you must set the ICMP Type parameter.
  icmptype:
    type: float
    description:
      - ICMP Message type to match against the message type of an incoming ICMP packet.
        For example, to block DESTINATION UNREACHABLE messages, you must specify 3
        as the ICMP type.
      - ''
      - 'Note: This parameter can be specified only for the ICMP protocol.'
  logstate:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable logging of events related to the extended ACL rule. The
        log messages are stored in the configured syslog or auditlog server.
  newname:
    type: str
    description:
      - New name for the extended ACL rule. Must begin with an ASCII alphabetic or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
  nodeid:
    type: float
    description:
      - Specifies the NodeId to steer the packet to the provided FP.
  priority:
    type: float
    description:
      - Priority for the extended ACL rule that determines the order in which it is
        evaluated relative to the other extended ACL rules. If you do not specify
        priorities while creating extended ACL rules, the ACL rules are evaluated
        in the order in which they are created.
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
      - Protocol to match against the protocol of an incoming IPv4 packet.
  protocolnumber:
    type: float
    description:
      - Protocol to match against the protocol of an incoming IPv4 packet.
  ratelimit:
    type: float
    description:
      - Maximum number of log messages to be generated per second. If you set this
        parameter, you must enable the Log State parameter.
  srcip:
    type: bool
    description:
      - 'IP address or range of IP addresses to match against the source IP address
        of an incoming IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 10.102.29.30-10.102.29.189.'
  srcipdataset:
    type: str
    description:
      - Policy dataset which can have multiple IP ranges bound to it.
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
      - IP address or range of IP addresses to match against the source IP address
        of an incoming IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example:10.102.29.30-10.102.29.189.
  srcmac:
    type: str
    description:
      - MAC address to match against the source MAC address of an incoming IPv4 packet.
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
        of an incoming IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 40-90.'
  srcportdataset:
    type: str
    description:
      - Policy dataset which can have multiple port ranges bound to it.
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
        of an incoming IPv4 packet. In the command line interface, separate the range
        with a hyphen. For example: 40-90.'
  stateful:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - If stateful option is enabled, transparent sessions are created for the traffic
        hitting this ACL and not hitting any other features like LB, INAT etc.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  ttl:
    type: float
    description:
      - Number of seconds, in multiples of four, after which the extended ACL rule
        expires. If you do not want the extended ACL rule to expire, do not specify
        a TTL value.
  type:
    type: str
    choices:
      - CLASSIC
      - DFD
    description:
      - Type of the acl ,default will be C(CLASSIC).
      - 'Available options as follows:'
      - '* C(CLASSIC) - specifies the regular extended acls.'
      - '* C(DFD) - cluster specific acls,specifies hashmethod for steering of the
        packet in cluster .'
  vlan:
    type: float
    description:
      - ID of the VLAN. The Citrix ADC applies the ACL rule only to the incoming packets
        of the specified VLAN. If you do not specify a VLAN ID, the appliance applies
        the ACL rule to the incoming packets on all VLANs.
  vxlan:
    type: float
    description:
      - ID of the VXLAN. The Citrix ADC applies the ACL rule only to the incoming
        packets of the specified VXLAN. If you do not specify a VXLAN ID, the appliance
        applies the ACL rule to the incoming packets on all VXLANs.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsacl playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nsacl
      delegate_to: localhost
      netscaler.adc.nsacl:
        state: present
        aclname: acl1
        aclaction: ALLOW
        srcip: true
        srcipval: 222.222.80.55
        destip: true
        destipval: 209.1.2.12
        protocol: TCP
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
