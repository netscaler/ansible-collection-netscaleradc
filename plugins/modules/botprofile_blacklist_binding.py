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
---
module: botprofile_blacklist_binding
short_description: Binding Resource definition for describing association between
  botprofile and blacklist resources
description: Binding Resource definition for describing association between botprofile
  and blacklist resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  bot_bind_comment:
    type: str
    description:
      - Any comments about this binding.
  bot_blacklist:
    type: bool
    description:
      - Blacklist binding. Maximum 32 bindings can be configured per profile for Blacklist
        detection.
  bot_blacklist_action:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - RESET
      - REDIRECT
    description:
      - One or more actions to be taken if  bot is detected based on this Blacklist
        binding. Only C(LOG) action can be combined with C(DROP) or C(RESET) action.
    elements: str
  bot_blacklist_enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enabled or disbaled black-list binding.
  bot_blacklist_type:
    type: str
    choices:
      - IPv4
      - SUBNET
      - IPv6
      - IPv6_SUBNET
      - EXPRESSION
    description:
      - Type of the black-list entry.
  bot_blacklist_value:
    type: str
    description:
      - Value of the bot black-list entry.
  logmessage:
    type: str
    description:
      - Message to be logged for this binding.
  name:
    type: str
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
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
