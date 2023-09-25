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
  accounting:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure the RADIUS server state to accept or refuse accounting messages.
    type: str
  authentication:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure the RADIUS server state to accept or refuse authentication messages.
    type: str
    default: 'ON'
  authservretry:
    description:
      - Number of retry by the Citrix ADC before getting response from the RADIUS
        server.
    type: float
    default: 3
  authtimeout:
    description:
      - Maximum number of seconds that the Citrix ADC waits for a response from the
        RADIUS server.
    type: float
    default: 3
  callingstationid:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Calling-Station-ID of the client to the RADIUS server. IP Address of
        the client is sent as its Calling-Station-ID.
    type: str
    default: DISABLED
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  ipattributetype:
    description:
      - IP attribute type in the RADIUS response.
    type: float
  ipvendorid:
    description:
      - 'Vendor ID attribute in the RADIUS response. '
      - If the attribute is not vendor-encoded, it is set to 0.
    type: float
  passencoding:
    choices:
      - pap
      - chap
      - mschapv1
      - mschapv2
    description:
      - Enable password encoding in RADIUS packets that the Citrix ADC sends to the
        RADIUS server.
    type: str
    default: mschapv2
  pwdattributetype:
    description:
      - Attribute type of the Vendor ID in the RADIUS response.
    type: float
  pwdvendorid:
    description:
      - Vendor ID of the password in the RADIUS response. Used to extract the user
        password.
    type: float
  radattributetype:
    description:
      - Attribute type for RADIUS group extraction.
    type: float
  radgroupseparator:
    description:
      - Group separator string that delimits group names within a RADIUS attribute
        for RADIUS group extraction.
    type: str
  radgroupsprefix:
    description:
      - Prefix string that precedes group names within a RADIUS attribute for RADIUS
        group extraction.
    type: str
  radkey:
    description:
      - 'The key shared between the RADIUS server and clients. '
      - Required for allowing the Citrix ADC to communicate with the RADIUS server.
    type: str
  radnasid:
    description:
      - Send the Network Access Server ID (NASID) for your Citrix ADC to the RADIUS
        server as the nasid part of the Radius protocol.
    type: str
  radnasip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send the Citrix ADC IP (NSIP) address to the RADIUS server as the Network
        Access Server IP (NASIP) part of the Radius protocol.
    type: str
  radvendorid:
    description:
      - Vendor ID for RADIUS group extraction.
    type: float
  serverip:
    description:
      - IP address of your RADIUS server.
    type: str
  serverport:
    description:
      - Port number on which the RADIUS server listens for connections.
    type: int
    default: 1812
  tunnelendpointclientip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Tunnel Endpoint Client IP address to the RADIUS server.
    type: str
    default: DISABLED
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
