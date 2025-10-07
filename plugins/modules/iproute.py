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
module: iproute
short_description: Manage iproute configuration on Citrix ADC (NetScaler) devices
description:
  - Manage iproute configuration on Citrix ADC (NetScaler) devices.
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
  addressFamily:
    type: str
    choices: ["ipv4", "ipv6"]
    description:
      - The address family of the route.
  distance:
    type: int
    description:
      - Distance value for this route.
      - Minimum value is 1.
      - Maximum value is 255.
  interface:
    type: str
    description:
      - IP gateway interface name or pseudo interface Null.
  isBest:
    type: str
    description:
      - Indicates if this is the best route for the prefix.
  metric:
    type: int
    description:
      - IP route metric value.
  nextHop:
    type: str
    description:
      - IP gateway address.
  prefix:
    type: str
    description:
      - IP destination prefix.
  prefixLength:
    type: int
    description:
      - IP destination prefix length.
      - Minimum value is 0.
      - Maximum value is 128.
  type:
    type: str
    description:
      - IP route protocol type.
extends_documentation_fragment: netscaler.adc.netscaler_adc
"""
EXAMPLES = r"""
---
- name: Configure iproute
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure iproute
      delegate_to: localhost
      netscaler.adc.iproute:
        state: present
        addressFamily: ipv4
        distance: 1
        interface: eth0
        nextHop: 192.168.1.1
        prefix: 192.168.1.0
        prefixLength: 24
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
