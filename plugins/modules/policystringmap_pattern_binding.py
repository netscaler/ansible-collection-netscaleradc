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
module: policystringmap_pattern_binding
short_description: Binding Resource definition for describing association between
  policystringmap and pattern resources
description: Binding Resource definition for describing association between policystringmap
  and pattern resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Comments associated with the string map or key-value pair bound to this string
        map.
    type: str
  key:
    description:
      - Character string constituting the key to be bound to the string map. The key
        is matched against the data processed by the operation that uses the string
        map. The default character set is ASCII. UTF-8 characters can be included
        if the character set is UTF-8.  UTF-8 characters can be entered directly (if
        the UI supports it) or can be encoded as a sequence of hexadecimal bytes '\xNN'.
        For example, the UTF-8 character '' can be encoded as '\xC3\xBC'.
    type: str
  name:
    description:
      - Name of the string map to which to bind the key-value pair.
    type: str
  value:
    description:
      - Character string constituting the value associated with the key. This value
        is returned when processed data matches the associated key. Refer to the key
        parameter for details of the value character set.
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
