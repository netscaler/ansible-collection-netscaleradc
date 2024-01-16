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
module: lbsipparameters
short_description: Configuration for SIP parameters resource.
description: Configuration for SIP parameters resource.
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
  addrportvip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Add the rport parameter to the VIA headers of SIP requests that virtual servers
        receive from clients or servers.
  retrydur:
    type: int
    description:
      - Time, in seconds, for which a client must wait before initiating a connection
        after receiving a 503 Service Unavailable response from the SIP server. The
        time value is sent in the "Retry-After" header in the 503 response.
  rnatdstport:
    type: int
    description:
      - Port number with which to match the destination port in server-initiated SIP
        traffic. The rport parameter is added, without a value, to SIP packets that
        have a matching destination port number, and CALL-ID based persistence is
        implemented for the responses received by the virtual server.
  rnatsecuredstport:
    type: int
    description:
      - Port number with which to match the destination port in server-initiated SIP
        over SSL traffic. The rport parameter is added, without a value, to SIP packets
        that have a matching destination port number, and CALL-ID based persistence
        is implemented for the responses received by the virtual server.
  rnatsecuresrcport:
    type: int
    description:
      - Port number with which to match the source port in server-initiated SIP over
        SSL traffic. The rport parameter is added, without a value, to SIP packets
        that have a matching source port number, and CALL-ID based persistence is
        implemented for the responses received by the virtual server.
  rnatsrcport:
    type: int
    description:
      - Port number with which to match the source port in server-initiated SIP traffic.
        The rport parameter is added, without a value, to SIP packets that have a
        matching source port number, and CALL-ID based persistence is implemented
        for the responses received by the virtual server.
  sip503ratethreshold:
    type: float
    description:
      - Maximum number of 503 Service Unavailable responses to generate, once every
        10 milliseconds, when a SIP virtual server becomes unavailable.
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
