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
module: systemcmdpolicy
short_description: Configuration for command policy resource.
description: Configuration for command policy resource.
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
  action:
    type: str
    choices:
      - ALLOW
      - DENY
    description:
      - Action to perform when a request matches the policy.
  cmdspec:
    type: str
    description:
      - Regular expression specifying the data that matches the policy.
  policyname:
    type: str
    description:
      - Name for a command policy. Must begin with a letter, number, or the underscore
        (_) character, and must contain only alphanumeric, hyphen (-), period (.),
        hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters.
        Cannot be changed after the policy is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my policy" or ''my policy'').'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample systemcmdpolicy playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure systemcmdpolicy
      delegate_to: localhost
      netscaler.adc.systemcmdpolicy:
        state: present
        policyname: read-only
        action: ALLOW
        cmdspec: (^man.*)|(^show\s+(\?!system)(\?!configstatus)(\?!ns ns\.conf)(\?!ns
          savedconfig)(\?!ns runningConfig)(\?!gslb runningConfig)(\?!audit messages)(\?!techsupport).*)|(^stat.*)
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
