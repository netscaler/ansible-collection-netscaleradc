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
module: vpnvserver_responderpolicy_binding
short_description: Binding Resource definition for describing association between
  vpnvserver and responderpolicy resources
description: Binding Resource definition for describing association between vpnvserver
  and responderpolicy resources
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
      - Bindpoint to which the policy is bound.
    type: str
  gotopriorityexpression:
    description:
      - Next priority expression.
    type: str
  groupextraction:
    description:
      - Binds the authentication policy to a tertiary chain which will be used only
        for group extraction.  The user will not authenticate against this server,
        and this will only be called if primary and/or secondary authentication has
        succeeded.
    type: bool
  name:
    description:
      - Name of the virtual server.
    type: str
  policy:
    description:
      - The name of the policy, if any, bound to the VPN virtual server.
    type: str
  priority:
    description:
      - Integer specifying the policy's priority. The lower the number, the higher
        the priority. Policies are evaluated in the order of their priority numbers.
        Maximum value for default syntax policies is 2147483647 and for classic policies
        is 64000.
    type: int
  secondary:
    description:
      - Binds the authentication policy as the secondary policy to use in a two-factor
        configuration. A user must then authenticate not only via a primary authentication
        method but also via a secondary authentication method. User groups are aggregated
        across both. The user name must be exactly the same for both authentication
        methods, but they can require different passwords.
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
