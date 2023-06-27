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
module: authenticationvserver_authenticationldappolicy_binding
short_description: Binding Resource definition for describing association between
  authenticationvserver and authenticationldappolicy resources
description: Binding Resource definition for describing association between authenticationvserver
  and authenticationldappolicy resources
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
      - 'Applicable only to advance authentication policy. Expression or other value
        specifying the next policy to be evaluated if the current policy evaluates
        to TRUE.  Specify one of the following values:'
      - '* NEXT - Evaluate the policy with the next higher priority number.'
      - '* END - End policy evaluation.'
      - '* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy
        label. If the final goto in the invoked policy label has a value of END, the
        evaluation stops. If the final goto is anything other than END, the current
        policy label performs a NEXT.'
      - '* An expression that evaluates to a number.'
      - 'If you specify an expression, the number to which it evaluates determines
        the next policy to evaluate, as follows:'
      - '* If the expression evaluates to a higher numbered priority, the policy with
        that priority is evaluated next.'
      - '* If the expression evaluates to the priority of the current policy, the
        policy with the next higher numbered priority is evaluated next.'
      - '* If the expression evaluates to a priority number that is numerically higher
        than the highest numbered priority, policy evaluation ends.'
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
    type: str
  groupextraction:
    description:
      - Bind the Authentication policy to a tertiary chain which will be used only
        for group extraction.  The user will not authenticate against this server,
        and this will only be called if primary and/or secondary authentication has
        succeeded.
    type: bool
  name:
    description:
      - Name of the authentication virtual server to which to bind the policy.
    type: str
  nextfactor:
    description:
      - Applicable only while binding advance authentication policy as classic authentication
        policy does not support nFactor
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
      - Bind the authentication policy to the secondary chain.
      - Provides for multifactor authentication in which a user must authenticate
        via both a primary authentication method and, afterward, via a secondary authentication
        method.
      - Because user groups are aggregated across authentication systems, usernames
        must be the same on all authentication servers. Passwords can be different.
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
