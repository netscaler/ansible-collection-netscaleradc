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
module: contentinspectionaction
short_description: Configuration for Content Inspection action resource.
description: Configuration for Content Inspection action resource.
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
  icapprofilename:
    type: str
    description:
      - Name of the ICAP profile to be attached to the contentInspection action.
  ifserverdown:
    type: str
    choices:
      - CONTINUE
      - DROP
      - RESET
    description:
      - 'Name of the action to perform if the Vserver representing the remote service
        is not UP. This is not supported for NOINSPECTION Type. The Supported actions
        are:'
      - '* C(RESET) - Reset the client connection by closing it. The client program,
        such as a browser, will handle this and may inform the user. The client may
        then resend the request if desired.'
      - '* C(DROP) - Drop the request without sending a response to the user.'
      - '* C(CONTINUE) - It bypasses the ContentIsnpection and Continues/resumes the
        Traffic-Flow to Client/Server.'
  name:
    type: str
    description:
      - Name of the remote service action. Must begin with an ASCII alphabetic or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
  serverip:
    type: str
    description:
      - IP address of remoteService
  servername:
    type: str
    description:
      - Name of the LB vserver or service
  serverport:
    type: float
    description:
      - Port of remoteService
  type:
    type: str
    choices:
      - ICAP
      - INLINEINSPECTION
      - MIRROR
      - NOINSPECTION
    description:
      - 'Type of operation this action is going to perform. following actions are
        available to configure:'
      - '* C(ICAP) - forward the incoming request or response to an C(ICAP) server
        for modification.'
      - '* C(INLINEINSPECTION) - forward the incoming or outgoing packets to IPS server
        for Intrusion Prevention.'
      - '* C(MIRROR) - Forwards cloned packets for Intrusion Detection.'
      - '* C(NOINSPECTION) - This does not forward incoming and outgoing packets to
        the Inspection device.'
      - '* NSTRACE - capture current and further incoming packets on this transaction.'
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
