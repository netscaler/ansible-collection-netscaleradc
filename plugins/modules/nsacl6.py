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
module: nsacl6
short_description: Configuration for ACL6 entry resource.
description: Configuration for ACL6 entry resource.
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
      - ID of an interface. The Citrix ADC applies the ACL6 rule only to the incoming
        packets from the specified interface. If you do not specify any value, the
        appliance applies the ACL6 rule to the incoming packets from all interfaces.
  acl6action:
    type: str
    choices:
      - BRIDGE
      - DENY
      - ALLOW
    description:
      - Action to perform on the incoming IPv6 packets that match the ACL6 rule.
      - 'Available settings function as follows:'
      - '* C(ALLOW) - The Citrix ADC processes the packet.'
      - '* C(BRIDGE) - The Citrix ADC bridges the packet to the destination without
        processing it.'
      - '* C(DENY) - The Citrix ADC drops the packet.'
  acl6name:
    type: str
    description:
      - Name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  aclaction:
    type: str
    choices:
      - BRIDGE
      - DENY
      - ALLOW
    description:
      - Action associated with the ACL6.
  destipop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  destipv6:
    type: bool
    description:
      - IP address or range of IP addresses to match against the destination IP address
        of an incoming IPv6 packet.  In the command line interface, separate the range
        with a hyphen.
  destipv6val:
    type: str
    description:
      - Destination IPv6 address (range).
  destport:
    type: bool
    description:
      - 'Port number or range of port numbers to match against the destination port
        number of an incoming IPv6 packet. In the command line interface, separate
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
      - Destination port (range).
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
      - Specifies the type of hashmethod to be applied, to steer the packet to the
        FP of the packet.
  dfdprefix:
    type: float
    description:
      - hashprefix to be applied to SIP/DIP to generate rsshash FP.eg 128 => hash
        calculated on the complete IP
  established:
    type: bool
    description:
      - Allow only incoming TCP packets that have the ACK or RST bit set if the action
        set for the ACL6 rule is ALLOW and these packets match the other conditions
        in the ACL6 rule.
  icmpcode:
    type: float
    description:
      - Code of a particular ICMP message type to match against the ICMP code of an
        incoming IPv6 ICMP packet.  For example, to block DESTINATION HOST UNREACHABLE
        messages, specify 3 as the ICMP type and 1 as the ICMP code.
      - ''
      - If you set this parameter, you must set the ICMP Type parameter.
  icmptype:
    type: float
    description:
      - ICMP Message type to match against the message type of an incoming IPv6 ICMP
        packet. For example, to block DESTINATION UNREACHABLE messages, you must specify
        3 as the ICMP type.
      - ''
      - 'Note: This parameter can be specified only for the ICMP protocol.'
  logstate:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable logging of events related to the ACL6 rule. The log messages
        are stored in the configured syslog or auditlog server.
  newname:
    type: str
    description:
      - New name for the ACL6 rule. Must begin with an ASCII alphabetic or underscore
        \(_\) character, and must contain only ASCII alphanumeric, underscore, hash
        \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen
        \(-\) characters.
  priority:
    type: float
    description:
      - Priority for the ACL6 rule, which determines the order in which it is evaluated
        relative to the other ACL6 rules. If you do not specify priorities while creating
        ACL6 rules, the ACL6 rules are evaluated in the order in which they are created.
  protocol:
    type: str
    choices:
      - ICMPV6
      - TCP
      - UDP
      - ICMP
      - IGMP
      - EGP
      - IGP
      - ARGUS
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
        incoming C(IPv6) packet.
  protocolnumber:
    type: float
    description:
      - Protocol, identified by protocol number, to match against the protocol of
        an incoming IPv6 packet.
  ratelimit:
    type: float
    description:
      - Maximum number of log messages to be generated per second. If you set this
        parameter, you must enable the Log State parameter.
  srcipop:
    type: str
    choices:
      - '='
      - '!='
      - EQ
      - NEQ
    description:
      - Either the equals (=) or does not equal (!=) logical operator.
  srcipv6:
    type: bool
    description:
      - IP address or range of IP addresses to match against the source IP address
        of an incoming IPv6 packet. In the command line interface, separate the range
        with a hyphen.
  srcipv6val:
    type: str
    description:
      - Source IPv6 address (range).
  srcmac:
    type: str
    description:
      - MAC address to match against the source MAC address of an incoming IPv6 packet.
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
        of an incoming IPv6 packet. In the command line interface, separate the range
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
      - Source port (range).
  stateful:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - If stateful option is enabled, transparent sessions are created for the traffic
        hitting this ACL6 and not hitting any other features like LB, INAT etc.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  ttl:
    type: float
    description:
      - Time to expire this ACL6 (in seconds).
  type:
    type: str
    choices:
      - CLASSIC
      - DFD
    description:
      - Type of the acl6 ,default will be C(CLASSIC).
      - 'Available options as follows:'
      - '* C(CLASSIC) - specifies the regular extended acls.'
      - '* C(DFD) - cluster specific acls,specifies hashmethod for steering of the
        packet in cluster .'
  vlan:
    type: float
    description:
      - ID of the VLAN. The Citrix ADC applies the ACL6 rule only to the incoming
        packets on the specified VLAN. If you do not specify a VLAN ID, the appliance
        applies the ACL6 rule to the incoming packets on all VLANs.
  vxlan:
    type: float
    description:
      - ID of the VXLAN. The Citrix ADC applies the ACL6 rule only to the incoming
        packets on the specified VXLAN. If you do not specify a VXLAN ID, the appliance
        applies the ACL6 rule to the incoming packets on all VXLANs.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsacl6 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nsacl6
      delegate_to: localhost
      netscaler.adc.nsacl6:

        state: present
        acl6name: net_acl6
        acl6action: ALLOW
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
