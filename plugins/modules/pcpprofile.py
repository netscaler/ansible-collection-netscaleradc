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
module: pcpprofile
short_description: Configuration for PCP Profile resource.
description: Configuration for PCP Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  announcemulticount:
    description:
      - Integer value that identify the number announce message to be send.
    type: int
    default: 10
  mapping:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This argument is for enabling/disabling the MAP opcode  of current PCP Profile
    type: str
    default: ENABLED
  maxmaplife:
    description:
      - Integer value that identify the maximum mapping lifetime (in seconds) for
        a pcp profile. default(86400s = 24Hours).
    type: int
  minmaplife:
    description:
      - Integer value that identify the minimum mapping lifetime (in seconds) for
        a pcp profile. default(120s)
    type: int
  name:
    description:
      - 'Name for the PCP Profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore CLI Users:
        If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my pcpProfile" or my pcpProfile).'
    type: str
  peer:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This argument is for enabling/disabling the PEER opcode of current PCP Profile
    type: str
    default: ENABLED
  thirdparty:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This argument is for enabling/disabling the THIRD PARTY opcode of current
        PCP Profile
    type: str
    default: DISABLED
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
