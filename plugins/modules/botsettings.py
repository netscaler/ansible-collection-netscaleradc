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
module: botsettings
short_description: Configuration for Bot engine settings resource.
description: Configuration for Bot engine settings resource.
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
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  defaultnonintrusiveprofile:
    type: str
    choices:
      - BOT_BYPASS
      - BOT_STATS
      - BOT_LOG
    description:
      - Profile to use when the feature is not enabled but feature is licensed. NonIntrusive
        checks will be disabled and IPRep cronjob(24 Hours) will be removed if this
        is set to C(BOT_BYPASS).
  defaultprofile:
    type: str
    description:
      - Profile to use when a connection does not match any policy. Default setting
        is " ", which sends unmatched connections back to the Citrix ADC without attempting
        to filter them further.
  dfprequestlimit:
    type: float
    description:
      - Number of requests to allow without bot session cookie if device fingerprint
        is enabled
  javascriptname:
    type: str
    description:
      - Name of the JavaScript that the Bot Management feature  uses in response.
      - Must begin with a letter or number, and can consist of from 1 to 31 letters,
        numbers, and the hyphen (-) and underscore (_) symbols.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cookie name" or 'my cookie name').
  proxypassword:
    type: str
    description:
      - Password with which user logs on.
  proxyport:
    type: int
    description:
      - Proxy Server Port to get updated signatures from AWS.
  proxyserver:
    type: str
    description:
      - Proxy Server IP to get updated signatures from AWS.
  proxyusername:
    type: str
    description:
      - Proxy Username
  sessioncookiename:
    type: str
    description:
      - Name of the SessionCookie that the Bot Management feature uses for tracking.
      - Must begin with a letter or number, and can consist of from 1 to 31 letters,
        numbers, and the hyphen (-) and underscore (_) symbols.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cookie name" or 'my cookie name').
  sessiontimeout:
    type: float
    description:
      - Timeout, in seconds, after which a user session is terminated.
  signatureautoupdate:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Flag used to enable/disable bot auto update signatures
  signatureurl:
    type: str
    description:
      - URL to download the bot signature mapping file from server
  trapurlautogenerate:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable/disable trap URL auto generation. When enabled, trap URL is updated
        within the configured interval.
  trapurlinterval:
    type: float
    description:
      - Time in seconds after which trap URL is updated.
  trapurllength:
    type: float
    description:
      - Length of the auto-generated trap URL.
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
