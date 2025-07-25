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
module: vpnvserver_feopolicy_binding
short_description: Binding Resource definition for describing association between
  vpnvserver and feopolicy resources
description: Binding Resource definition for describing association between vpnvserver
  and feopolicy resources
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
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
      - Bindpoint to which the policy is bound.
  gotopriorityexpression:
    type: str
    description:
      - Next priority expression.
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
      - Name of a policy to bind to the virtual server (for example, the name of an
        authentication, session, or endpoint analysis policy).
  priority:
    type: int
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
