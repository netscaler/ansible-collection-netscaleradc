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
module: csvserver_rewritepolicy_binding
short_description: Binding Resource definition for describing association between
  csvserver and rewritepolicy resources
description: Binding Resource definition for describing association between csvserver
  and rewritepolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bindpoint:
    choices:
      - REQUEST
      - RESPONSE
      - ICA_REQUEST
      - OTHERTCP_REQUEST
      - MQTT_JUMBO_REQ
    description:
      - The bindpoint to which the policy is bound
    type: str
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - Invoke flag.
    type: bool
  labelname:
    description:
      - Name of the label invoked.
    type: str
  labeltype:
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - The invocation type.
    type: str
  name:
    description:
      - Name of the content switching virtual server to which the content switching
        policy applies.
    type: str
  policyname:
    description:
      - Policies bound to this vserver.
    type: str
  priority:
    description:
      - Priority for the policy.
    type: int
  targetlbvserver:
    description:
      - Name of the Load Balancing virtual server to which the content is switched,
        if policy rule is evaluated to be TRUE.
      - 'Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1'
      - 'Note: Use this parameter only in case of Content Switching policy bind operations
        to a CS vserver'
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
