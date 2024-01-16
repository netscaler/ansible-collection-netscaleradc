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
module: vpnvserver_authenticationnegotiatepolicy_binding
short_description: Binding Resource definition for describing association between
  vpnvserver and authenticationnegotiatepolicy resources
description: Binding Resource definition for describing association between vpnvserver
  and authenticationnegotiatepolicy resources
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
      - AAA_REQUEST
      - AAA_RESPONSE
    description:
      - Bind point to which to bind the policy. Applies only to rewrite and cache
        policies. If you do not set this parameter, the policy is bound to REQ_DEFAULT
        or RES_DEFAULT, depending on whether the policy rule is a response-time or
        a request-time expression.
  gotopriorityexpression:
    type: str
    description:
      - 'Applicable only to advance vpn session policy. Expression or other value
        specifying the next policy to evaluate if the current policy evaluates to
        TRUE.  Specify one of the following values:'
      - '* NEXT - Evaluate the policy with the next higher priority number.'
      - '* END - End policy evaluation.'
      - '* An expression that evaluates to a number.'
      - 'If you specify an expression, the number to which it evaluates determines
        the next policy to evaluate, as follows:'
      - '*  If the expression evaluates to a higher numbered priority, the policy
        with that priority is evaluated next.'
      - '* If the expression evaluates to the priority of the current policy, the
        policy with the next higher numbered priority is evaluated next.'
      - '* If the expression evaluates to a number that is larger than the largest
        numbered priority, policy evaluation ends.'
      - 'An UNDEF event is triggered if:'
      - '* The expression is invalid.'
      - '* The expression evaluates to a priority number that is numerically lower
        than the current policy''s priority.'
      - '* The expression evaluates to a priority number that is between the current
        policy''s priority number (say, 30) and the highest priority number (say,
        100), but does not match any configured priority number (for example, the
        expression evaluates to the number 85). This example assumes that the priority
        number increments by 10 for every successive policy, and therefore a priority
        number of 85 does not exist in the policy label.'
  groupextraction:
    type: bool
    description:
      - Binds the authentication policy to a tertiary chain which will be used only
        for group extraction.  The user will not authenticate against this server,
        and this will only be called if primary and/or secondary authentication has
        succeeded.
  name:
    type: str
    description:
      - Name of the virtual server.
  policy:
    type: str
    description:
      - The name of the policy, if any, bound to the VPN virtual server.
  priority:
    type: float
    description:
      - Integer specifying the policy's priority. The lower the number, the higher
        the priority. Policies are evaluated in the order of their priority numbers.
        Maximum value for default syntax policies is 2147483647 and for classic policies
        is 64000.
  secondary:
    type: bool
    description:
      - Binds the authentication policy as the secondary policy to use in a two-factor
        configuration. A user must then authenticate not only via a primary authentication
        method but also via a secondary authentication method. User groups are aggregated
        across both. The user name must be exactly the same for both authentication
        methods, but they can require different passwords.
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
