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
module: dbdbprofile
short_description: Configuration for DB profile resource.
description: Configuration for DB profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  conmultiplex:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use the same server-side connection for multiple client-side requests. Default
        is enabled.
    type: str
    default: ENABLED
  enablecachingconmuxoff:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable caching when connection multiplexing is OFF.
    type: str
    default: DISABLED
  interpretquery:
    choices:
      - 'YES'
      - 'NO'
    description:
      - If ENABLED, inspect the query and update the connection information, if required.
        If DISABLED, forward the query to the server.
    type: str
    default: 'YES'
  kcdaccount:
    description:
      - Name of the KCD account that is used for Windows authentication.
    type: str
  name:
    description:
      - Name for the database profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Cannot be changed after the profile is created.
      - "\t    CLI Users: If the name includes one or more spaces, enclose the name\
        \ in double or single quotation marks (for example, \"my profile\" or 'my\
        \ profile')."
    type: str
  stickiness:
    choices:
      - 'YES'
      - 'NO'
    description:
      - If the queries are related to each other, forward to the same backend server.
    type: str
    default: 'NO'
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
