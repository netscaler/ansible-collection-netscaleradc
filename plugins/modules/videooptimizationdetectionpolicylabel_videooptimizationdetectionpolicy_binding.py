#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: videooptimizationdetectionpolicylabel_videooptimizationdetectionpolicy_binding
short_description: Binding Resource definition for describing association between
  videooptimizationdetectionpolicylabel and videooptimizationdetectionpolicy resources
description: Binding Resource definition for describing association between videooptimizationdetectionpolicylabel
  and videooptimizationdetectionpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label and evaluate the specified policy label.
    type: bool
  invoke_labelname:
    description:
      - '* If labelType is policylabel, name of the policy label to invoke.'
      - '* If labelType is reqvserver or resvserver, name of the virtual server.'
    type: str
  labelname:
    description:
      - Name of the videooptimization detection policy label to which to bind the
        policy.
    type: str
  labeltype:
    description:
      - 'Type of policy label to invoke. Available settings function as follows:'
      - '* vserver - Invoke an unnamed policy label associated with a virtual server.'
      - '* policylabel - Invoke a user-defined policy label.'
    type: str
    choices:
      - vserver
      - policylabel
  policyname:
    description:
      - Name of the videooptimization policy.
    type: str
  priority:
    description:
      - Specifies the priority of the policy.
    type: int
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
