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
module: nsextension
short_description: Configuration for Extension resource.
description: Configuration for Extension resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about the extension object.
    type: str
  detail:
    choices:
      - brief
      - all
    description:
      - Show detail for extension function.
    type: str
  name:
    description:
      - Name to assign to the extension object on the Citrix ADC.
    type: str
  overwrite:
    description:
      - Overwrites the existing file
    type: bool
  src:
    description:
      - Local path to and name of, or URL (protocol, host, path, and file name) for,
        the file in which to store the imported extension.
      - 'NOTE: The import fails if the object to be imported is on an HTTPS server
        that requires client certificate authentication for access.'
    type: str
  trace:
    choices:
      - false
      - calls
      - lines
      - all
    description:
      - 'Enables tracing to the NS log file of extension execution:'
      - '   off   - turns off tracing (equivalent to unset ns extension <extension-name>
        -trace)'
      - '   calls - traces extension function calls with arguments and function returns
        with the first return value'
      - '   lines - traces the above plus line numbers for executed extension lines'
      - '   all   - traces the above plus local variables changed by executed extension
        lines'
      - Note that the DEBUG log level must be enabled to see extension tracing.
      - This can be done by set audit syslogParams -loglevel ALL or -loglevel DEBUG.
    type: str
  tracefunctions:
    description:
      - Comma-separated list of extension functions to trace. By default, all extension
        functions are traced.
    type: str
  tracevariables:
    description:
      - Comma-separated list of variables (in traced extension functions) to trace.
        By default, all variables are traced.
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