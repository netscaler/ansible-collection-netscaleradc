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
module: aaatacacsparams
short_description: Configuration for tacacs parameters resource.
description: Configuration for tacacs parameters resource.
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
  accounting:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send accounting messages to the TACACS+ server.
  auditfailedcmds:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - The option for sending accounting messages to the TACACS+ server.
  authorization:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use streaming authorization on the TACACS+ server.
  authtimeout:
    type: float
    description:
      - Maximum number of seconds that the Citrix ADC waits for a response from the
        TACACS+ server.
  defaultauthenticationgroup:
    type: str
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  groupattrname:
    type: str
    description:
      - TACACS+ group attribute name.Used for group extraction on the TACACS+ server.
  serverip:
    type: str
    description:
      - IP address of your TACACS+ server.
  serverport:
    type: int
    description:
      - Port number on which the TACACS+ server listens for connections.
  tacacssecret:
    type: str
    description:
      - Key shared between the TACACS+ server and clients. Required for allowing the
        Citrix ADC to communicate with the TACACS+ server.
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
