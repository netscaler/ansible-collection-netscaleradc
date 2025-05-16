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
module: vlan_interface_binding
short_description: Binding Resource definition for describing association between
  vlan and interface resources
description: Binding Resource definition for describing association between vlan and
  interface resources
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  id:
    type: float
    description:
      - Specifies the virtual LAN ID.
  ifnum:
    type: str
    description:
      - The interface to be bound to the VLAN, specified in slot/port notation (for
        example, 1/3).
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for this vlan.
  tagged:
    type: bool
    description:
      - Make the interface an 802.1q tagged interface. Packets sent on this interface
        on this VLAN have an additional 4-byte 802.1q tag, which identifies the VLAN.
        To use 802.1q tagging, you must also configure the switch connected to the
        appliance's interfaces.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample vlan_interface_binding playbook
  hosts: demo_netscalers
  gather_facts: 'false'
  tasks:
    - name: Configure vlan_interface_binding
      delegate_to: localhost
      netscaler.adc.vlan_interface_binding:
        state: present
        id: '815'
        ifnum:
          - 10/2
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
