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
module: botprofile_captcha_binding
short_description: Binding Resource definition for describing association between
  botprofile and captcha resources
description: Binding Resource definition for describing association between botprofile
  and captcha resources
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
  bot_bind_comment:
    type: str
    description:
      - Any comments about this binding.
  bot_captcha_action:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - One or more actions to be taken when client fails captcha challenge. Only,
        log action can be configured with C(DROP), C(REDIRECT) or C(RESET) action.
    elements: str
  bot_captcha_enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable the captcha binding.
  bot_captcha_url:
    type: str
    description:
      - URL for which the Captcha action, if configured under IP reputation, TPS or
        device fingerprint, need to be applied.
  captcharesource:
    type: bool
    description:
      - Captcha action binding. For each URL, only one binding is allowed. To update
        the values of an existing URL binding, user has to first unbind that binding,
        and then needs to bind the URL again with new values. Maximum 30 bindings
        can be configured per profile.
  graceperiod:
    type: int
    description:
      - Time (in seconds) duration for which no new captcha challenge is sent after
        current captcha challenge has been answered successfully.
  logmessage:
    type: str
    description:
      - Message to be logged for this binding.
  muteperiod:
    type: int
    description:
      - Time (in seconds) duration for which client which failed captcha need to wait
        until allowed to try again. The requests from this client are silently dropped
        during the mute period.
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
  requestsizelimit:
    type: int
    description:
      - Length of body request (in Bytes) up to (equal or less than) which captcha
        challenge will be provided to client. Above this length threshold the request
        will be dropped. This is to avoid DOS and DDOS attacks.
  retryattempts:
    type: int
    description:
      - Number of times client can retry solving the captcha.
  waittime:
    type: int
    description:
      - Wait time in seconds for which ADC needs to wait for the Captcha response.
        This is to avoid DOS attacks.
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
