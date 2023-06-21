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
module: systemgroup
short_description: Configuration for system group resource.
description: Configuration for system group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  allowedmanagementinterface:
    description:
      - Allowed Management interfaces of the system users in the group. By default
        allowed from both API and CLI interfaces. If management interface for a group
        is set to API, then all users under this group will not allowed to access
        NS through CLI. GUI interface will come under API interface
    type: list
    elements: str
    default: NS_INTERFACE_ALL
    choices:
      - CLI
      - API
  groupname:
    description:
      - Name for the group. Must begin with a letter, number, hash(#) or the underscore
        (_) character, and must contain only alphanumeric, hyphen (-), period (.),
        hash (#), space ( ), at (@), equal (=), colon (:), and underscore characters.
        Cannot be changed after the group is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my group" or ''my group'').'
    type: str
  promptstring:
    description:
      - 'String to display at the command-line prompt. Can consist of letters, numbers,
        hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:),
        underscore (_), and the following variables: '
      - '* %u - Will be replaced by the user name.'
      - '* %h - Will be replaced by the hostname of the Citrix ADC.'
      - '* %t - Will be replaced by the current time in 12-hour format.'
      - '* %T - Will be replaced by the current time in 24-hour format.'
      - '* %d - Will be replaced by the current date.'
      - '* %s - Will be replaced by the state of the Citrix ADC.'
      - ''
      - 'Note: The 63-character limit for the length of the string does not apply
        to the characters that replace the variables.'
    type: str
  timeout:
    description:
      - CLI session inactivity timeout, in seconds. If Restrictedtimeout argument
        of system parameter is enabled, Timeout can have values in the range [300-86400]
        seconds.If Restrictedtimeout argument of system parameter is disabled, Timeout
        can have values in the range [0, 10-100000000] seconds. Default value is 900
        seconds.
    type: int
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
