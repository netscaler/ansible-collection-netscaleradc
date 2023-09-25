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
module: botprofile_whitelist_binding
short_description: Binding Resource definition for describing association between
  botprofile and whitelist resources
description: Binding Resource definition for describing association between botprofile
  and whitelist resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bot_bind_comment:
    description:
      - Any comments about this binding.
    type: str
  bot_whitelist:
    description:
      - Whitelist binding. Maximum 32 bindings can be configured per profile for Whitelist
        detection.
    type: bool
  bot_whitelist_enabled:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enabled or disabled white-list binding.
    type: str
    default: 'OFF'
  bot_whitelist_type:
    choices:
      - IPv4
      - SUBNET
      - IPv6
      - IPv6_SUBNET
      - EXPRESSION
    description:
      - Type of the white-list entry.
    type: str
  bot_whitelist_value:
    description:
      - Value of bot white-list entry.
    type: str
  log:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable logging for Whitelist binding.
    type: str
    default: 'OFF'
  logmessage:
    description:
      - Message to be logged for this binding.
    type: str
  name:
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
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
