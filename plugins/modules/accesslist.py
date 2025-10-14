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
module: accesslist
short_description: Manage accesslist configuration on Citrix ADC (NetScaler) devices
description:
  - Manage Accesslist configuration on Citrix ADC (NetScaler) devices.
version_added: 2.10.0
author:
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices: ["absent", "present", "unset"]
    default: present
    description:
      - The state of the resource on the NetScaler ADC node.
      - When C(present), the resource will be added or updated.
      - When C(absent), the resource will be deleted.
      - When C(unset), the resource will be unset.
  id:
    type: str
    description:
      - Standard access list number in the range <0-99> or a ZebOS access-list name.

  remark:
    type: str
    description:
      - Access list entry comment.

  rules:
    type: list
    elements: dict
    description:
      - List of rule parameters for the access list entry.
    suboptions:
      action:
        type: str
        description:
          - Allow or deny if traffic matches the rule.
      address:
        type: str
        description:
          - Address to match.
      wildcard:
        type: str
        description:
          - Wildcard mask to apply to the address.

  remove_non_updatable_params:
    type: str
    choices: ["yes", "no"]
    default: "no"
    description:
      - Remove non-updatable parameters from the configuration.

extends_documentation_fragment: netscaler.adc.netscaler_adc
"""

EXAMPLES = r"""
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
