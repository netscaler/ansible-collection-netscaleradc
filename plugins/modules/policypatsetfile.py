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
module: policypatsetfile
short_description: Configuration for patset file resource.
description: Configuration for patset file resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  charset:
    type: str
    choices:
      - ASCII
      - UTF_8
    description:
      - Character set associated with the characters in the string.
  comment:
    type: str
    description:
      - Any comments to preserve information about this patsetfile.
  delimiter:
    type: str
    description:
      - patset file patterns delimiter.
  imported:
    type: bool
    description:
      - When set, display only shows all imported patsetfiles.
  name:
    type: str
    description:
      - Name to assign to the imported patset file. Unique name of the pattern set.
        Not case sensitive. Must begin with an ASCII letter or underscore (_) character
        and must contain only alphanumeric and underscore characters.
  overwrite:
    type: bool
    description:
      - Overwrites the existing file
  src:
    type: str
    description:
      - URL in protocol, host, path, and file name format from where the patset file
        will be imported. If file is already present, then it can be imported using
        local keyword (import patsetfile local:filename patsetfile1)
      - '                      NOTE: The import fails if the object to be imported
        is on an HTTPS server that requires client certificate authentication for
        access'
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
