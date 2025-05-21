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
---
module: vpnglobal_authenticationldappolicy_binding
short_description: Binding Resource definition for describing association between
  vpnglobal and authenticationldappolicy resources
description: Binding Resource definition for describing association between vpnglobal
  and authenticationldappolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
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
      - Applicable only to advance vpn session policy. An expression or other value
        specifying the priority of the next policy which will get evaluated if the
        current policy rule evaluates to TRUE.
  groupextraction:
    type: bool
    description:
      - Bind the Authentication policy to a tertiary chain which will be used only
        for group extraction.  The user will not authenticate against this server,
        and this will only be called it primary and/or secondary authentication has
        succeeded.
  policyname:
    type: str
    description:
      - The name of the policy.
  priority:
    type: int
    description:
      - Integer specifying the policy's priority. The lower the priority number, the
        higher the policy's priority. Maximum value for default syntax policies is
        2147483647 and for classic policies is 64000.
  secondary:
    type: bool
    description:
      - Bind the authentication policy as the secondary policy to use in a two-factor
        configuration. A user must then authenticate not only to a primary authentication
        server but also to a secondary authentication server. User groups are aggregated
        across both authentication servers. The user name must be exactly the same
        on both authentication servers, but the authentication servers can require
        different passwords.
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
