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
module: policyexpression
short_description: Configuration for expression resource.
description: Configuration for expression resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  clientsecuritymessage:
    type: str
    description:
      - Message to display if the expression fails. Allowed for classic end-point
        check expressions only.
  comment:
    type: str
    description:
      - Any comments associated with the expression. Displayed upon viewing the policy
        expression.
  name:
    type: str
    description:
      - Unique name for the expression. Not case sensitive. Must begin with an ASCII
        letter or underscore (_) character, and must consist only of ASCII alphanumeric
        or underscore characters. Must not begin with 're' or 'xp' or be a word reserved
        for use as an expression qualifier prefix (such as HTTP) or enumeration value
        (such as ASCII). Must not be the name of an existing named expression, pattern
        set, dataset, stringmap, or HTTP callout.
  type:
    type: str
    choices:
      - CLASSIC
      - ADVANCED
    description:
      - Type of expression. Can be a classic or default syntax (advanced) expression.
  value:
    type: str
    description:
      - 'Expression string. For example: http.req.body(100).contains("this").'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample policyexpression playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure policyexpression
      delegate_to: localhost
      netscaler.adc.policyexpression:
        state: present
        name: Sub_1471612160_23
        value: CLIENT.IP.SRC.IN_SUBNET(147.161.216.0/23)
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
