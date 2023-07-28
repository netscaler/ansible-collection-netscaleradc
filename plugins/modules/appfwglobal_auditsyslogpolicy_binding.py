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
module: appfwglobal_auditsyslogpolicy_binding
short_description: Binding Resource definition for describing association between
  appfwglobal and auditsyslogpolicy resources
description: Binding Resource definition for describing association between appfwglobal
  and auditsyslogpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  gotopriorityexpression:
    description:
      - 'Expression or other value specifying the next policy to evaluate if the current
        policy evaluates to TRUE.  Specify one of the following values:'
      - '* NEXT - Evaluate the policy with the next higher priority number.'
      - '* END - End policy evaluation.'
      - '* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy
        label. If the final goto in the invoked policy label has a value of END, the
        evaluation stops. If the final goto is anything other than END, the current
        policy label performs a NEXT.'
      - '* An expression that evaluates to a number.'
      - 'If you specify an expression, the number to which it evaluates determines
        the next policy to evaluate, as follows:'
      - '* If the expression evaluates to a higher numbered priority, the policy with
        that priority is evaluated next.'
      - '* If the expression evaluates to the priority of the current policy, the
        policy with the next higher numbered priority is evaluated next.'
      - '* If the expression evaluates to a number that is larger than the largest
        numbered priority, policy evaluation ends.'
      - ''
      - 'An UNDEF event is triggered if:'
      - '* The expression is invalid.'
      - '* The expression evaluates to a priority number that is smaller than the
        current policy''s priority number.'
      - '* The expression evaluates to a priority number that is between the current
        policy''s priority number (say, 30) and the highest priority number (say,
        100), but does not match any configured priority number (for example, the
        expression evaluates to the number 85). This example assumes that the priority
        number increments by 10 for every successive policy, and therefore a priority
        number of 85 does not exist in the policy label.'
    type: str
  invoke:
    description:
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label, and then forward the request to the specified
        virtual server or evaluate the specified policy label.
    type: bool
  labelname:
    description:
      - Name of the policy label to invoke if the current policy evaluates to TRUE,
        the invoke parameter is set, and Label Type is set to Policy Label.
    type: str
  labeltype:
    choices:
      - reqvserver
      - policylabel
    description:
      - 'Type of policy label to invoke if the current policy evaluates to TRUE and
        the invoke parameter is set. Available settings function as follows:'
      - '* C(reqvserver). Invoke the unnamed policy label associated with the specified
        request virtual server.'
      - '* C(policylabel). Invoke the specified user-defined policy label.'
    type: str
  policyname:
    description:
      - Name of the policy.
    type: str
  priority:
    description:
      - The priority of the policy.
    type: int
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the binding to activate or deactivate the policy. This is
        applicable to classic policies only.
    type: str
  type:
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
      - NONE
    description:
      - Bind point to which to policy is bound.
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
