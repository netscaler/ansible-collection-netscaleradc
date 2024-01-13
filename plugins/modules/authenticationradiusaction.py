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
module: authenticationradiusaction
short_description: Configuration for RADIUS action resource.
description: Configuration for RADIUS action resource.
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
  accounting:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Whether the RADIUS server is currently accepting accounting messages.
  authentication:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure the RADIUS server state to accept or refuse authentication messages.
  authservretry:
    type: float
    description:
      - Number of retry by the Citrix ADC before getting response from the RADIUS
        server.
  authtimeout:
    type: float
    description:
      - Number of seconds the Citrix ADC waits for a response from the RADIUS server.
  callingstationid:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Calling-Station-ID of the client to the RADIUS server. IP Address of
        the client is sent as its Calling-Station-ID.
  defaultauthenticationgroup:
    type: str
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  ipattributetype:
    type: float
    description:
      - Remote IP address attribute type in a RADIUS response.
  ipvendorid:
    type: float
    description:
      - Vendor ID of the intranet IP attribute in the RADIUS response.
      - 'NOTE: A value of 0 indicates that the attribute is not vendor encoded.'
  name:
    type: str
    description:
      - Name for the RADIUS action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the RADIUS action is added.
  passencoding:
    type: str
    choices:
      - pap
      - chap
      - mschapv1
      - mschapv2
    description:
      - Encoding type for passwords in RADIUS packets that the Citrix ADC sends to
        the RADIUS server.
  pwdattributetype:
    type: float
    description:
      - Vendor-specific password attribute type in a RADIUS response.
  pwdvendorid:
    type: float
    description:
      - Vendor ID of the attribute, in the RADIUS response, used to extract the user
        password.
  radattributetype:
    type: float
    description:
      - RADIUS attribute type, used for RADIUS group extraction.
  radgroupseparator:
    type: str
    description:
      - RADIUS group separator string
      - The group separator delimits group names within a RADIUS attribute for RADIUS
        group extraction.
  radgroupsprefix:
    type: str
    description:
      - RADIUS groups prefix string.
      - This groups prefix precedes the group names within a RADIUS attribute for
        RADIUS group extraction.
  radkey:
    type: str
    description:
      - Key shared between the RADIUS server and the Citrix ADC.
      - Required to allow the Citrix ADC to communicate with the RADIUS server.
  radnasid:
    type: str
    description:
      - If configured, this string is sent to the RADIUS server as the Network Access
        Server ID (NASID).
  radnasip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, the Citrix ADC IP address (NSIP) is sent to the RADIUS server
        as the  Network Access Server IP (NASIP) address.
      - The RADIUS protocol defines the meaning and use of the NASIP address.
  radvendorid:
    type: float
    description:
      - RADIUS vendor ID attribute, used for RADIUS group extraction.
  serverip:
    type: str
    description:
      - IP address assigned to the RADIUS server.
  servername:
    type: str
    description:
      - RADIUS server name as a FQDN.  Mutually exclusive with RADIUS IP address.
  serverport:
    type: int
    description:
      - Port number on which the RADIUS server listens for connections.
  targetlbvserver:
    type: str
    description:
      - If transport mode is TLS, specify the name of LB vserver to associate. The
        LB vserver needs to be of type TCP and service associated needs to be SSL_TCP
  transport:
    type: str
    choices:
      - UDP
      - TCP
      - TLS
    description:
      - Transport mode to RADIUS server.
  tunnelendpointclientip:
    type: str
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
