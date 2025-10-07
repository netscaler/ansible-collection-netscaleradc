#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}
DOCUMENTATION = r"""
module: ospfinterface
short_description: Manage OSPF interface configuration on Citrix ADC (NetScaler) devices
description:
  - Manage OSPF interface configuration on Citrix ADC (NetScaler) devices.
version_added: 2.10.0
author:
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices: ["present", "absent"]
    default: present
    description:
      - The state of the resource on the NetScaler ADC node.
      - When C(present), the resource will be added or updated.
      - When C(absent), the resource will be deleted.
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  authKey:
    type: str
    description:
      - Authentication password (key).
  authType:
    type: str
    choices: ["null", "simple", "message-digest"]
    description:
      - Authentication type on the OSPF interface.
  bfd:
    type: bool
    description:
      - Enable BFD on interface.
  cost:
    type: int
    description:
      - Interface cost.
      - Minimum value is 1.
      - Maximum value is 65535.
  deadInterval:
    type: int
    description:
      - Interval after which a neighbor is declared dead.
      - Minimum value is 1.
      - Maximum value is 65535.
  helloInterval:
    type: int
    description:
      - Time between HELLO packets.
      - Minimum value is 1.
      - Maximum value is 65535.
  mtu:
    type: int
    description:
      - OSPF interface MTU.
      - Minimum value is 576.
      - Maximum value is 65535.
  name:
    type: str
    description:
      - Name of the interface.
  networkType:
    type: str
    choices: ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"]
    description:
      - Network type.
  priority:
    type: int
    description:
      - Router priority.
      - Minimum value is 0.
      - Maximum value is 255.
  retransmitInterval:
    type: int
    description:
      - Time between retransmitting lost link state advertisements.
      - Minimum value is 1.
      - Maximum value is 65535.
  transmitDelay:
    type: int
    description:
      - Link state transmit delay.
      - Minimum value is 1.
      - Maximum value is 65535.
extends_documentation_fragment: netscaler.adc.netscaler_adc
"""
EXAMPLES = r"""
---
- name: Ensure that OSPF interface is present
  hosts: netscaler
  gather_facts: false
  tasks:
    - name: Configure OSPF interface
      delegate_to: localhost
      netscaler.adc.ospfinterface:
        state: present
        name: eth0
        authKey: my_auth_key
        authType: message-digest
        bfd: true
        cost: 10
        deadInterval: 40
        helloInterval: 10
        mtu: 1500
        networkType: broadcast
        priority: 1
        retransmitInterval: 5
        transmitDelay: 1
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
