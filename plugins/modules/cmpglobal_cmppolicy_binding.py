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
module: cmpglobal_cmppolicy_binding
short_description: Binding Resource definition for describing association between
  cmpglobal and cmppolicy resources
description: Binding Resource definition for describing association between cmpglobal
  and cmppolicy resources
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
  globalbindtype:
    type: str
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
      - TM_GLOBAL
    description:
      - '0'
  gotopriorityexpression:
    type: str
    description:
      - 'Expression or other value specifying the priority of the next policy, within
        the policy label, to evaluate if the current policy evaluates to TRUE.  Specify
        one of the following values:'
      - '* NEXT - Evaluate the policy with the next higher numbered priority.'
      - '* END - Stop evaluation.'
      - '* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy
        label. If the final goto in the invoked policy label has a value of END, the
        evaluation stops. If the final goto is anything other than END, the current
        policy label performs a NEXT.'
      - '* An expression that evaluates to a number.'
      - 'If you specify an expression, it''s evaluation result determines the next
        policy to evaluate, as follows:'
      - '* If the expression evaluates to a higher numbered priority, that policy
        is evaluated next.'
      - '* If the expression evaluates to the priority of the current policy, the
        policy with the next higher priority number is evaluated next.'
      - '* If the expression evaluates to a priority number that is numerically higher
        than the highest priority number, policy evaluation ends.'
      - 'An UNDEF event is triggered if:'
      - '* The expression is invalid.'
      - '* The expression evaluates to a priority number that is numerically lower
        than the current policy''s priority.'
      - '* The expression evaluates to a priority number that is between the current
        policy''s priority number (say, 30) and the highest priority number (say,
        100), but does not match any configured priority number (for example, the
        expression evaluates to the number 85). This example assumes that the priority
        number increments by 10 for every successive policy, and therefore a priority
        number of 85 does not exist in the policy label.'
  invoke:
    type: bool
    description:
      - Invoke policies bound to a virtual server or a policy label. After the invoked
        policies are evaluated, the flow returns to the policy with the next priority.
  labelname:
    type: str
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - Type of policy label invocation.
  policyname:
    type: str
    description:
      - The name of the globally bound HTTP compression policy.
  priority:
    type: float
    description:
      - Positive integer specifying the priority of the policy. The lower the number,
        the higher the priority. By default, polices within a label are evaluated
        in the order of their priority numbers.
      - In the configuration utility, you can click the Priority field and edit the
        priority level or drag the entry to a new position in the list. If you drag
        the entry to a new position, the priority level is updated automatically.
  type:
    type: str
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - RES_OVERRIDE
      - RES_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
      - HTTPQUIC_RES_OVERRIDE
      - HTTPQUIC_RES_DEFAULT
      - NONE
    description:
      - Bind point to which the policy is bound.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample cmpglobal_cmppolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cmpglobal_cmppolicy_binding
      delegate_to: localhost
      netscaler.adc.cmpglobal_cmppolicy_binding:
        state: present
        policyname: ns_adv_cmp_content_type
        priority: '10000'
        gotopriorityexpression: END
        type: RES_DEFAULT
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
