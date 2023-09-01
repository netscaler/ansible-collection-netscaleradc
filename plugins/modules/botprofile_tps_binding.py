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
module: botprofile_tps_binding
short_description: Binding Resource definition for describing association between
  botprofile and tps resources
description: Binding Resource definition for describing association between botprofile
  and tps resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bot_bind_comment:
    description:
      - Any comments about this binding.
    type: str
  bot_tps:
    description:
      - TPS binding. For each type only binding can be configured. To  update the
        values of an existing binding, user has to first unbind that binding, and
        then needs to bind again with new values.
    type: bool
  bot_tps_action:
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
    type: list
    elements: str
    default: NONE
  bot_tps_enabled:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enabled or disabled TPS binding.
    type: str
    default: 'ON'
  bot_tps_type:
    choices:
      - SOURCE_IP
      - GEOLOCATION
      - REQUEST_URL
      - Host
    description:
      - Type of TPS binding.
    type: str
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
  percentage:
    description:
      - Maximum percentage increase in the requests from (or to) a IP, Geolocation,
        URL or Host in 30 minutes interval.
    type: float
  threshold:
    description:
      - Maximum number of requests that are allowed from (or to) a IP, Geolocation,
        URL or Host in 1 second time interval.
    type: float
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
