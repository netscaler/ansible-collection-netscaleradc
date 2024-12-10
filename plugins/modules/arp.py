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
module: arp
short_description: Configuration for arp resource.
description: Configuration for arp resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  all:
    type: bool
    description:
      - Remove all ARP entries from the ARP table of the Citrix ADC.
  ifnum:
    type: str
    description:
      - Interface through which the network device is accessible. Specify the interface
        in (slot/port) notation. For example, 1/3.
  ipaddress:
    type: str
    description:
      - IP address of the network device that you want to add to the ARP table.
  mac:
    type: str
    description:
      - MAC address of the network device.
  nodeid:
    type: float
    description:
      - Unique number that identifies the cluster node.
  ownernode:
    type: float
    description:
      - The owner node for the Arp entry.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  vlan:
    type: float
    description:
      - The VLAN ID through which packets are to be sent after matching the ARP entry.
        This is a numeric value.
  vtep:
    type: str
    description:
      - IP address of the VXLAN tunnel endpoint (VTEP) through which the IP address
        of this ARP entry is reachable.
  vxlan:
    type: float
    description:
      - ID of the VXLAN on which the IP address of this ARP entry is reachable.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample arp playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure arp
      delegate_to: localhost
      netscaler.adc.arp:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        ipaddress: 177.0.0.31
        mac: 96:f1:a0:2b:98:1f
        ifnum: 1/2
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
