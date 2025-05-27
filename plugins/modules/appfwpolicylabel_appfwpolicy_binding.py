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
module: appfwpolicylabel_appfwpolicy_binding
short_description: Binding Resource definition for describing association between
  appfwpolicylabel and appfwpolicy resources
description: Binding Resource definition for describing association between appfwpolicylabel
  and appfwpolicy resources
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
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label, and then forward the request to the specified
        virtual server or evaluate the specified policy label.
  invoke_labelname:
    type: str
    description:
      - Name of the policy label to invoke if the current policy evaluates to TRUE,
        the invoke parameter is set, and Label Type is set to Policy Label.
  labelname:
    type: str
    description:
      - Name of the application firewall policy label.
  labeltype:
    type: str
    choices:
      - reqvserver
      - policylabel
    description:
      - 'Type of policy label to invoke if the current policy evaluates to TRUE and
        the invoke parameter is set. Available settings function as follows:'
      - '* C(reqvserver). Invoke the unnamed policy label associated with the specified
        request virtual server.'
      - '* C(policylabel). Invoke the specified user-defined policy label.'
  policyname:
    type: str
    description:
      - Name of the application firewall policy to bind to the policy label.
  priority:
    type: int
    description:
      - Positive integer specifying the priority of the policy. A lower number specifies
        a higher priority. Must be unique within a group of policies that are bound
        to the same bind point or label. Policies are evaluated in the order of their
        priority numbers.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appfwpolicylabel_appfwpolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwpolicylabel_appfwpolicy_binding
      delegate_to: localhost
      netscaler.adc.appfwpolicylabel_appfwpolicy_binding:
        state: present
        labelname: appfw_label_01
        policyname: ia_appfwpol1
        priority: '1'
        invoke: true
        labeltype: policylabel
        invoke_labelname: appfw_label_02
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
