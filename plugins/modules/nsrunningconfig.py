#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: nsrunningconfig
short_description: Configuration for running configuration resource.
description: Configuration for running configuration resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
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
  withdefaults:
    type: bool
    description:
      - Include default values of parameters that have not been explicitly configured.
        If this argument is disabled, such parameters are not included.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsrunningconfig playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Get nsrunningconfig information
      delegate_to: localhost
      register: result
      netscaler.adc.nsrunningconfig:

    - name: Display nsrunningconfig
      ansible.builtin.debug:
        var: result

    - name: Get nsrunningconfig with defaults
      delegate_to: localhost
      register: result_with_defaults
      netscaler.adc.nsrunningconfig:
        withdefaults: true

    - name: Display nsrunningconfig with defaults
      ansible.builtin.debug:
        var: result_with_defaults
"""

RETURN = r"""
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
