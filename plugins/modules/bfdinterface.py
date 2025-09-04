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
---
module: bfd_interface
short_description: Configure BFD on an interface
description:
  - This module allows you to configure Bidirectional Forwarding Detection (BFD) on a network interface.
  - BFD is a network protocol used to detect faults between two forwarding engines.
options:
  state:
    description:
      - The desired state of the BFD configuration.
    type: str
    choices: ['present']
    default: 'present'
  interface:
    description:
      - The name of the interface to configure BFD on.
    type: str
    required: true
  interval:
    description:
      - The BFD detection interval in milliseconds.
    type: int
    default: 100
  min_rx:
    description:
      - The minimum BFD receive interval in milliseconds.
    type: int
    default: 100
  multiplier:
    description:
      - The BFD detection multiplier.
    type: int
    default: 3
  name:
    description:
      - The name of the BFD configuration.
    type: str
    required: true
  passive:
    description:
      - Whether to enable passive mode for BFD.
    type: bool
    default: false
"""

EXAMPLE = r"""
---
- name: Configure BFD interface
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure BFD
      delegate_to: localhost
      netscaler.adc.bfdinterface:
        state: present
        interval: 100
        min_rx: 100
        multiplier: 3
        name: "bfd1"
        passive: false
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
