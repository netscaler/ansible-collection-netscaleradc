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
module: gslbvserver_spilloverpolicy_binding
short_description: Binding Resource definition for describing association between
  gslbvserver and spilloverpolicy resources
description: Binding Resource definition for describing association between gslbvserver
  and spilloverpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
      - "\to\tIf gotoPriorityExpression is not present or if it is equal to END then\
        \ the policy bank evaluation ends here"
      - "\to\tElse if the gotoPriorityExpression is equal to NEXT then the next policy\
        \ in the priority order is evaluated."
      - "\to\tElse gotoPriorityExpression is evaluated. The result of gotoPriorityExpression\
        \ (which has to be a number) is processed as follows:"
      - "\t\t-\tAn UNDEF event is triggered if"
      - "\t\t\t.\tgotoPriorityExpression cannot be evaluated"
      - "\t\t\t.\tgotoPriorityExpression evaluates to number which is smaller than\
        \ the maximum priority in the policy bank but is not same as any policy's\
        \ priority"
      - "\t\t\t.\tgotoPriorityExpression evaluates to a priority that is smaller than\
        \ the current policy's priority"
      - "\t\t-\tIf the gotoPriorityExpression evaluates to the priority of the current\
        \ policy then the next policy in the priority order is evaluated."
      - "\t\t-\tIf the gotoPriorityExpression evaluates to the priority of a policy\
        \ further ahead in the list then that policy will be evaluated next."
      - "\t\tThis field is applicable only to rewrite and responder policies."
    type: str
  name:
    description:
      - Name of the virtual server on which to perform the binding operation.
    type: str
  order:
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
    type: float
  policyname:
    description:
      - Name of the policy bound to the GSLB vserver.
    type: str
  priority:
    description:
      - Priority.
    type: float
  type:
    choices:
      - REQUEST
      - RESPONSE
      - MQTT_JUMBO_REQ
    description:
      - The bindpoint to which the policy is bound
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
