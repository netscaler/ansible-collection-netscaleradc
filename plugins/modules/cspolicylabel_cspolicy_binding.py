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
module: cspolicylabel_cspolicy_binding
short_description: Binding Resource definition for describing association between
  cspolicylabel and cspolicy resources
description: Binding Resource definition for describing association between cspolicylabel
  and cspolicy resources
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
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - '0'
  invoke_labelname:
    type: str
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
  labelname:
    type: str
    description:
      - Name of the policy label to which to bind a content switching policy.
  labeltype:
    type: str
    choices:
      - policylabel
    description:
      - Type of policy label invocation.
  policyname:
    type: str
    description:
      - Name of the content switching policy.
  priority:
    type: float
    description:
      - Specifies the priority of the policy.
  targetvserver:
    type: str
    description:
      - Name of the virtual server to which to forward requests that match the policy.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample cspolicylabel_cspolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cspolicylabel_cspolicy_binding
      delegate_to: localhost
      netscaler.adc.cspolicylabel_cspolicy_binding:
        state: present
        labelname: CSW_polabl5
        policyname: CSW_pol4
        priority: '2300'
        gotopriorityexpression: END
        invoke: true
        labeltype: policylabel
        invoke_labelname: CSW_invoke_labelname
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
