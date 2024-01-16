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
module: sslvserver_sslpolicy_binding
short_description: Binding Resource definition for describing association between
  sslvserver and sslpolicy resources
description: Binding Resource definition for describing association between sslvserver
  and sslpolicy resources
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
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - Invoke flag. This attribute is relevant only for ADVANCED policies
  labelname:
    type: str
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
  labeltype:
    type: str
    choices:
      - vserver
      - service
      - policylabel
    description:
      - Type of policy label invocation.
  policyname:
    type: str
    description:
      - The name of the SSL policy binding.
  priority:
    type: float
    description:
      - The priority of the policies bound to this SSL service
  type:
    type: str
    choices:
      - INTERCEPT_REQ
      - REQUEST
      - CLIENTHELLO_REQ
    description:
      - 'Bind point to which to bind the policy. Possible Values: C(REQUEST), C(INTERCEPT_REQ)
        and C(CLIENTHELLO_REQ). These bindpoints mean:'
      - '1. C(REQUEST): Policy evaluation will be done at appplication above SSL.
        This bindpoint is default and is used for actions based on clientauth and
        client cert.'
      - '2. C(INTERCEPT_REQ): Policy evaluation will be done during SSL handshake
        to decide whether to intercept or not. Actions allowed with this type are:
        INTERCEPT, BYPASS and RESET.'
      - '3. C(CLIENTHELLO_REQ): Policy evaluation will be done during handling of
        Client Hello Request. Action allowed with this type is: RESET, FORWARD and
        PICKCACERTGRP.'
  vservername:
    type: str
    description:
      - Name of the SSL virtual server.
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
