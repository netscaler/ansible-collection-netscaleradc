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
module: aaaradiusparams
short_description: Configuration for RADIUS parameter resource.
description: Configuration for RADIUS parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  accounting:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure the RADIUS server state to accept or refuse accounting messages.
  authentication:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure the RADIUS server state to accept or refuse authentication messages.
  authservretry:
    type: raw
    description:
      - Number of retry by the Citrix ADC before getting response from the RADIUS
        server.
  authtimeout:
    type: raw
    description:
      - Maximum number of seconds that the Citrix ADC waits for a response from the
        RADIUS server.
  callingstationid:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Calling-Station-ID of the client to the RADIUS server. IP Address of
        the client is sent as its Calling-Station-ID.
  defaultauthenticationgroup:
    type: raw
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  ipattributetype:
    type: raw
    description:
      - IP attribute type in the RADIUS response.
  ipvendorid:
    type: raw
    description:
      - Vendor ID attribute in the RADIUS response.
      - If the attribute is not vendor-encoded, it is set to 0.
  passencoding:
    type: raw
    choices:
      - pap
      - chap
      - mschapv1
      - mschapv2
    description:
      - Enable password encoding in RADIUS packets that the Citrix ADC sends to the
        RADIUS server.
  pwdattributetype:
    type: raw
    description:
      - Attribute type of the Vendor ID in the RADIUS response.
  pwdvendorid:
    type: raw
    description:
      - Vendor ID of the password in the RADIUS response. Used to extract the user
        password.
  radattributetype:
    type: raw
    description:
      - Attribute type for RADIUS group extraction.
  radgroupseparator:
    type: raw
    description:
      - Group separator string that delimits group names within a RADIUS attribute
        for RADIUS group extraction.
  radgroupsprefix:
    type: raw
    description:
      - Prefix string that precedes group names within a RADIUS attribute for RADIUS
        group extraction.
  radkey:
    type: str
    description:
      - The key shared between the RADIUS server and clients.
      - Required for allowing the Citrix ADC to communicate with the RADIUS server.
  radnasid:
    type: raw
    description:
      - Send the Network Access Server ID (NASID) for your Citrix ADC to the RADIUS
        server as the nasid part of the Radius protocol.
  radnasip:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send the Citrix ADC IP (NSIP) address to the RADIUS server as the Network
        Access Server IP (NASIP) part of the Radius protocol.
  radvendorid:
    type: raw
    description:
      - Vendor ID for RADIUS group extraction.
  serverip:
    type: raw
    description:
      - IP address of your RADIUS server.
  serverport:
    type: raw
    description:
      - Port number on which the RADIUS server listens for connections.
  tunnelendpointclientip:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Tunnel Endpoint Client IP address to the RADIUS server.
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
