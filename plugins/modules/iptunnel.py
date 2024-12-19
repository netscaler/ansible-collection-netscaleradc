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
module: iptunnel
short_description: Configuration for ip Tunnel resource.
description: Configuration for ip Tunnel resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  destport:
    type: int
    description:
      - Specifies UDP destination port for Geneve packets. Default port is 6081.
  grepayload:
    type: str
    choices:
      - ETHERNETwithDOT1Q
      - ETHERNET
      - IP
    description:
      - The payload GRE will carry
  ipsecprofilename:
    type: str
    description:
      - Name of IPSec profile to be associated.
  local:
    type: str
    description:
      - Type of Citrix ADC owned public IPv4 address, configured on the local Citrix
        ADC and used to set up the tunnel.
  name:
    type: str
    description:
      - 'Name for the IP tunnel. Leading character must be a number or letter. Other
        characters allowed, after the first character, are @ _ - . (period) : (colon)
        # and space ( ).'
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for the iptunnel.
  protocol:
    type: str
    choices:
      - IPIP
      - GRE
      - IPSEC
      - UDP
      - GENEVE
    description:
      - Name of the protocol to be used on this tunnel.
  remote:
    type: str
    description:
      - Public IPv4 address, of the remote device, used to set up the tunnel. For
        this parameter, you can alternatively specify a network address.
  remotesubnetmask:
    type: str
    description:
      - Subnet mask of the remote IP address of the tunnel.
  tosinherit:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Default behavior is to copy the ToS field of the internal IP Packet (Payload)
        to the outer IP packet (Transport packet). But the user can configure a new
        ToS field using this option.
  vlan:
    type: float
    description:
      - The vlan for mulicast packets
  vlantagging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to select Vlan Tagging.
  vnid:
    type: float
    description:
      - Virtual network identifier (VNID) is the value that identifies a specific
        virtual network in the data plane.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample iptunnel playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure iptunnel
      delegate_to: localhost
      netscaler.adc.iptunnel:
        state: present
        name: t11
        remote: 1.1.1.14
        remotesubnetmask: 255.255.255.255
        local: 1.1.1.22
        protocol: VXLAN
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
