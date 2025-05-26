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
module: ssldhparam
short_description: Configuration for dh Parameter resource.
description: Configuration for dh Parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - created
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(created), the `create` operation will be applied on the resource.
    type: str
  bits:
    type: float
    description:
      - Size, in bits, of the DH key being generated.
  dhfile:
    type: str
    description:
      - Name of and, optionally, path to the DH key file. /nsconfig/ssl/ is the default
        path.
  gen:
    type: str
    choices:
      - '2'
      - '5'
    description:
      - Random number required for generating the DH key. Required as part of the
        DH key generation algorithm.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ssldhparam playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure ssldhparam
      delegate_to: localhost
      netscaler.adc.ssldhparam:
        state: present
        dhfile: dfile
        bits: '512'
        gen: '2'
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
