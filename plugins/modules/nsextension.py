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
module: nsextension
short_description: Configuration for Extension resource.
description: Configuration for Extension resource.
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
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about the extension object.
  detail:
    type: str
    choices:
      - brief
      - all
    description:
      - Show detail for extension function.
  name:
    type: str
    description:
      - Name to assign to the extension object on the Citrix ADC.
  overwrite:
    type: bool
    description:
      - Overwrites the existing file
  src:
    type: str
    description:
      - Local path to and name of, or URL (protocol, host, path, and file name) for,
        the file in which to store the imported extension.
      - 'NOTE: The import fails if the object to be imported is on an HTTPS server
        that requires client certificate authentication for access.'
  trace:
    type: str
    choices:
      - 'off'
      - calls
      - lines
      - all
    description:
      - 'Enables tracing to the NS log file of extension execution:'
      - '   C(off)   - turns C(off) tracing (equivalent to unset ns extension <extension-name>
        -trace)'
      - '   C(calls) - traces extension function C(calls) with arguments and function
        returns with the first return value'
      - '   C(lines) - traces the above plus line numbers for executed extension C(lines)'
      - '   C(all)   - traces the above plus local variables changed by executed extension
        C(lines)'
      - Note that the DEBUG log level must be enabled to see extension tracing.
      - This can be done by set audit syslogParams -loglevel ALL or -loglevel DEBUG.
  tracefunctions:
    type: str
    description:
      - Comma-separated list of extension functions to trace. By default, all extension
        functions are traced.
  tracevariables:
    type: str
    description:
      - Comma-separated list of variables (in traced extension functions) to trace.
        By default, all variables are traced.
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
