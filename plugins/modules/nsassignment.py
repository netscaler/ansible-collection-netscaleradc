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
module: nsassignment
short_description: Configuration for assignment resource.
description: Configuration for assignment resource.
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
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  add:
    type: str
    description:
      - Right hand side of the assignment. The expression is evaluated and added to
        the left hand variable.
  append:
    type: str
    description:
      - Right hand side of the assignment. The expression is evaluated and appended
        to the left hand variable.
  clear:
    type: bool
    description:
      - Clear the variable value. Deallocates a text value, and for a map, the text
        key.
  comment:
    type: str
    description:
      - Comment. Can be used to preserve information about this rewrite action.
  name:
    type: str
    description:
      - Name for the assignment. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters. Can be changed after the assignment is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my assignment" or my assignment).
  newname:
    type: str
    description:
      - New name for the assignment.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed
        after the rewrite policy is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my assignment" or my assignment).
  set:
    type: str
    description:
      - Right hand side of the assignment. The expression is evaluated and assigned
        to the left hand variable.
  sub:
    type: str
    description:
      - Right hand side of the assignment. The expression is evaluated and subtracted
        from the left hand variable.
  variable:
    type: str
    description:
      - Left hand side of the assigment, of the form $variable-name (for a singleton
        variabled) or $variable-name[key-expression], where key-expression is an expression
        that evaluates to a text string and provides the key to select a map entry
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
