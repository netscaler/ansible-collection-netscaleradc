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
module: authenticationvserver_authenticationsamlidppolicy_binding
short_description: Binding Resource definition for describing association between
  authenticationvserver and authenticationsamlidppolicy resources
description: Binding Resource definition for describing association between authenticationvserver
  and authenticationsamlidppolicy resources
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
      - AAA_REQUEST
      - AAA_RESPONSE
    description:
      - Bind point to which to bind the policy. Applies only to rewrite and cache
        policies. If you do not set this parameter, the policy is bound to REQ_DEFAULT
        or RES_DEFAULT, depending on whether the policy rule is a response-time or
        a request-time expression.
    type: str
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  groupextraction:
    description:
      - Applicable only while bindind classic authentication policy as advance authentication
        policy use nFactor
    type: bool
  name:
    description:
      - Name of the authentication virtual server to which to bind the policy.
    type: str
  nextfactor:
    description:
      - On success invoke label.
    type: str
  policy:
    description:
      - The name of the policy, if any, bound to the authentication vserver.
    type: str
  priority:
    description:
      - The priority, if any, of the vpn vserver policy.
    type: int
  secondary:
    description:
      - Applicable only while bindind classic authentication policy as advance authentication
        policy use nFactor
    type: bool
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
