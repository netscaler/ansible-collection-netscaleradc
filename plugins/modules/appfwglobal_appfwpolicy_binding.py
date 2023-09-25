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
module: appfwglobal_appfwpolicy_binding
short_description: Binding Resource definition for describing association between
  appfwglobal and appfwpolicy resources
description: Binding Resource definition for describing association between appfwglobal
  and appfwpolicy resources
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
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
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
      - Type of policy label invocation.
    type: str
  policyname:
    description:
      - Name of the policy.
    type: str
  priority:
    description:
      - The priority of the policy.
    type: float
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
