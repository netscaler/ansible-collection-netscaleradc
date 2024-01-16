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
module: csvserver_feopolicy_binding
short_description: Binding Resource definition for describing association between
  csvserver and feopolicy resources
description: Binding Resource definition for describing association between csvserver
  and feopolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  bindpoint:
    type: str
    choices:
      - REQUEST
      - RESPONSE
      - ICA_REQUEST
      - OTHERTCP_REQUEST
      - MQTT_JUMBO_REQ
    description:
      - The bindpoint to which the policy is bound
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - Invoke a policy label if this policy's rule evaluates to TRUE.
  labelname:
    type: str
    description:
      - Name of the label to be invoked.
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - Type of label to be invoked.
  name:
    type: str
    description:
      - Name of the content switching virtual server to which the content switching
        policy applies.
  policyname:
    type: str
    description:
      - Policies bound to this vserver.
  priority:
    type: float
    description:
      - Priority for the policy.
  targetlbvserver:
    type: str
    description:
      - Name of the Load Balancing virtual server to which the content is switched,
        if policy rule is evaluated to be TRUE.
      - 'Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1'
      - 'Note: Use this parameter only in case of Content Switching policy bind operations
        to a CS vserver'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
