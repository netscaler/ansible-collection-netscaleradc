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
module: cachepolicylabel_cachepolicy_binding
short_description: Binding Resource definition for describing association between
  cachepolicylabel and cachepolicy resources
description: Binding Resource definition for describing association between cachepolicylabel
  and cachepolicy resources
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
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - Invoke policies bound to a virtual server or a user-defined policy label.
        After the invoked policies are evaluated, the flow returns to the policy with
        the next-lower priority.
  invoke_labelname:
    type: str
    description:
      - Name of the policy label to invoke if the current policy rule evaluates to
        TRUE.
  labelname:
    type: str
    description:
      - Name of the cache policy label to which to bind the policy.
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - 'Type of policy label to invoke: an unnamed label associated with a virtual
        server, or user-defined policy label.'
  policyname:
    type: str
    description:
      - Name of the cache policy to bind to the policy label.
  priority:
    type: int
    description:
      - Specifies the priority of the policy.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample cachepolicylabel_cachepolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cachepolicylabel_cachepolicy_binding
      delegate_to: localhost
      netscaler.adc.cachepolicylabel_cachepolicy_binding:
        state: present
        labelname: _reqBuiltinDefaults
        policyname: SecureAccess_cache_policy
        priority: '10'
        gotopriorityexpression: END
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
