#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: cmpglobal_cmppolicy_binding
short_description: Binding Resource definition for describing association between
  cmpglobal and cmppolicy resources
description: Binding Resource definition for describing association between cmpglobal
  and cmppolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  globalbindtype:
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
    description:
      - '0'
    type: str
    default: SYSTEM_GLOBAL
  gotopriorityexpression:
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
        policy to evaluate, as follows: '
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
    type: str
  invoke:
    description:
      - Invoke policies bound to a virtual server or a policy label. After the invoked
        policies are evaluated, the flow returns to the policy with the next priority.
    type: bool
  labelname:
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
    type: str
  labeltype:
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - Type of policy label invocation.
    type: str
  policyname:
    description:
      - The name of the globally bound HTTP compression policy.
    type: str
  priority:
    description:
      - Positive integer specifying the priority of the policy. The lower the number,
        the higher the priority. By default, polices within a label are evaluated
        in the order of their priority numbers.
      - In the configuration utility, you can click the Priority field and edit the
        priority level or drag the entry to a new position in the list. If you drag
        the entry to a new position, the priority level is updated automatically.
    type: int
  type:
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
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
