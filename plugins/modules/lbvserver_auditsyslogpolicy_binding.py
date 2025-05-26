#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: lbvserver_auditsyslogpolicy_binding
short_description: Binding Resource definition for describing association between
  lbvserver and auditsyslogpolicy resources
description: Binding Resource definition for describing association between lbvserver
  and auditsyslogpolicy resources
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
  bindpoint:
    type: str
    choices:
      - REQUEST
      - RESPONSE
      - MQTT_JUMBO_REQ
    description:
      - Bind point to which to bind the policy.
  gotopriorityexpression:
    type: str
    description:
      - 'Expression or other value specifying the next policy to be evaluated if the
        current policy evaluates to TRUE.  Specify one of the following values:'
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
  invoke:
    type: bool
    description:
      - Invoke policies bound to a virtual server or policy label.
  labelname:
    type: str
    description:
      - Name of the virtual server or user-defined policy label to invoke if the policy
        evaluates to TRUE.
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - 'Type of policy label to invoke. Applicable only to rewrite, videooptimization
        and cache policies. Available settings function as follows:'
      - '* C(reqvserver) - Evaluate the request against the request-based policies
        bound to the specified virtual server.'
      - '* C(resvserver) - Evaluate the response against the response-based policies
        bound to the specified virtual server.'
      - '* C(policylabel) - invoke the request or response against the specified user-defined
        policy label.'
  name:
    type: str
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
  order:
    type: float
    description:
      - Integer specifying the order of the service. A larger number specifies a lower
        order. Defines the order of the service relative to the other services in
        the load balancing vserver's bindings. Determines the priority given to the
        service among all the services bound.
  policyname:
    type: str
    description:
      - Name of the policy bound to the LB vserver.
  priority:
    type: float
    description:
      - Priority.
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
