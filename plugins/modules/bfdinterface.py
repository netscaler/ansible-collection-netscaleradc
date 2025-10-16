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
module: bfdinterface
short_description: Manage bfdinterface configuration on Citrix ADC (NetScaler) devices
description:
  - Manage bfdInterface configuration on Citrix ADC (NetScaler) devices.
version_added: 2.10.0
author:
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices: ["present"]
    default: present
    description:
      - The state of the resource on the NetScaler ADC node.
      - When C(present), the resource will be added or updated.
  interval:
    type: int
    description:
      - Transmit interval for BFD packets.
      - Minimum value is 100.
      - Maximum value is 30000.

  minrx:
    type: int
    description:
      - Minimum receive interval for BFD packets.
      - Minimum value is 100.
      - Maximum value is 30000.

  multiplier:
    type: int
    description:
      - Multiplier for BFD packets.
      - Minimum value is 1.
      - Maximum value is 20.

  name:
    type: str
    description:
      - Name of the interface.

  passive:
    type: bool
    description:
      - Make BFD session passive.
      - Read-write.

  remove_non_updatable_params:
    type: str
    choices: ["yes", "no"]
    default: "no"
    description:
      - Remove non-updatable parameters from the configuration.

extends_documentation_fragment: netscaler.adc.netscaler_adc
"""

EXAMPLES = r"""
---
- name: Configure bfdinterface
  hosts: localhost
  tasks:
    - name: Create bfdinterface
      delegate_to: localhost
      netscaler.adc.bfdinterface:
        state: present
        name: vlan0
        passive: true
        interval: 752
        minrx: 501
        multiplier: 3
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
