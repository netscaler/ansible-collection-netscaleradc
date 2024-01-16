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
module: dnspolicy64
short_description: Configuration for dns64 policy resource.
description: Configuration for dns64 policy resource.
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
  action:
    type: str
    description:
      - 'Name of the DNS64 action to perform when the rule evaluates to TRUE. The
        built in actions function as follows:'
      - '* A default dns64 action with prefix <default prefix> and mapped and exclude
        are any'
      - You can create custom actions by using the add dns action command in the CLI
        or the DNS64 > Actions > Create DNS64 Action dialog box in the Citrix ADC
        configuration utility.
  name:
    type: str
    description:
      - Name for the DNS64 policy.
  rule:
    type: str
    description:
      - Expression against which DNS traffic is evaluated.
      - 'Note:'
      - '* On the command line interface, if the expression includes blank spaces,
        the entire expression must be enclosed in double quotation marks.'
      - '* If the expression itself includes double quotation marks, you must escape
        the quotations by using the  character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
      - 'Example: CLIENT.IP.SRC.IN_SUBENT(23.34.0.0/16)'
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
