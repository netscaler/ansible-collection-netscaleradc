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
module: sslvserver_sslpolicy_binding
short_description: Binding Resource definition for describing association between
  sslvserver and sslpolicy resources
description: Binding Resource definition for describing association between sslvserver
  and sslpolicy resources
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
      - Invoke flag. This attribute is relevant only for ADVANCED policies
    type: bool
  labelname:
    description:
      - Name of the label to invoke if the current policy rule evaluates to TRUE.
    type: str
  labeltype:
    description:
      - Type of policy label invocation.
    type: str
    choices:
      - vserver
      - service
      - policylabel
  policyname:
    description:
      - The name of the SSL policy binding.
    type: str
  priority:
    description:
      - The priority of the policies bound to this SSL service
    type: int
  type:
    description:
      - 'Bind point to which to bind the policy. Possible Values: REQUEST, INTERCEPT_REQ
        and CLIENTHELLO_REQ. These bindpoints mean:'
      - '1. REQUEST: Policy evaluation will be done at appplication above SSL. This
        bindpoint is default and is used for actions based on clientauth and client
        cert.'
      - '2. INTERCEPT_REQ: Policy evaluation will be done during SSL handshake to
        decide whether to intercept or not. Actions allowed with this type are: INTERCEPT,
        BYPASS and RESET.'
      - '3. CLIENTHELLO_REQ: Policy evaluation will be done during handling of Client
        Hello Request. Action allowed with this type is: RESET, FORWARD and PICKCACERTGRP.'
    type: str
    default: REQUEST
    choices:
      - INTERCEPT_REQ
      - REQUEST
      - CLIENTHELLO_REQ
  vservername:
    description:
      - Name of the SSL virtual server.
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
