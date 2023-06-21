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
module: aaauser_authorizationpolicy_binding
short_description: Binding Resource definition for describing association between
  aaauser and authorizationpolicy resources
description: Binding Resource definition for describing association between aaauser
  and authorizationpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  policy:
    description:
      - The policy Name.
    type: str
  priority:
    description:
      - Integer specifying the priority of the policy.  A lower number indicates a
        higher priority. Policies are evaluated in the order of their priority numbers.
        Maximum value for default syntax policies is 2147483647 and for classic policies
        max priority is 64000.
    type: int
  type:
    description:
      - Bindpoint to which the policy is bound.
    type: str
    default: REQUEST
    choices:
      - REQUEST
      - UDP_REQUEST
      - DNS_REQUEST
      - ICMP_REQUEST
  username:
    description:
      - User account to which to bind the policy.
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
