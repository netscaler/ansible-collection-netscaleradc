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
module: snmpview
short_description: Configuration for view resource.
description: Configuration for view resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - Name for the SNMPv3 view. Can consist of 1 to 31 characters that include uppercase
        and lowercase letters, numbers, and the hyphen (-), period (.) pound (#),
        space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
        You should choose a name that helps identify the SNMPv3 view.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my view" or 'my view').
    type: str
  subtree:
    description:
      - A particular branch (subtree) of the MIB tree that you want to associate with
        this SNMPv3 view. You must specify the subtree as an SNMP OID.
    type: str
  type:
    choices:
      - included
      - excluded
    description:
      - Include or exclude the subtree, specified by the subtree parameter, in or
        from this view. This setting can be useful when you have C(included) a subtree,
        such as A, in an SNMPv3 view and you want to exclude a specific subtree of
        A, such as B, from the SNMPv3 view.
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
