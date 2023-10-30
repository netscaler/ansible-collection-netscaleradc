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
module: botprofile_tps_binding
short_description: Binding Resource definition for describing association between
  botprofile and tps resources
description: Binding Resource definition for describing association between botprofile
  and tps resources
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
  bot_bind_comment:
    type: str
    description:
      - Any comments about this binding.
  bot_tps:
    type: bool
    description:
      - TPS binding. For each type only binding can be configured. To  update the
        values of an existing binding, user has to first unbind that binding, and
        then needs to bind again with new values.
  bot_tps_action:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - MITIGATION
    description:
      - One to more actions to be taken if bot is detected based on this TPS binding.
        Only C(LOG) action can be combined with C(DROP), C(RESET), C(REDIRECT), or
        MITIGIATION action.
    elements: str
    default: NONE
  bot_tps_enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enabled or disabled TPS binding.
    default: 'ON'
  bot_tps_type:
    type: str
    choices:
      - SOURCE_IP
      - GEOLOCATION
      - REQUEST_URL
      - Host
    description:
      - Type of TPS binding.
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
  percentage:
    type: float
    description:
      - Maximum percentage increase in the requests from (or to) a IP, Geolocation,
        URL or Host in 30 minutes interval.
  threshold:
    type: float
    description:
      - Maximum number of requests that are allowed from (or to) a IP, Geolocation,
        URL or Host in 1 second time interval.
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
