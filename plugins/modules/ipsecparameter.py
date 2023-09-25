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
module: ipsecparameter
short_description: Configuration for IPSEC paramter resource.
description: Configuration for IPSEC paramter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  encalgo:
    choices:
      - AES
      - AES192
      - AES256
    description:
      - 'Type of encryption algorithm (Note: Selection of C(AES) enables AES128)'
    type: list
    elements: str
    default: AES
  hashalgo:
    choices:
      - HMAC_SHA1
      - HMAC_SHA256
      - HMAC_SHA384
      - HMAC_SHA512
      - HMAC_MD5
    description:
      - Type of hashing algorithm
    type: list
    elements: str
    default: HMAC_SHA256
  ikeretryinterval:
    description:
      - IKE retry interval for bringing up the connection
    type: float
  ikeversion:
    choices:
      - V1
      - V2
    description:
      - IKE Protocol Version
    type: str
    default: V2
  lifetime:
    description:
      - Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE
        SA/8)
    type: float
  livenesscheckinterval:
    description:
      - Number of seconds after which a notify payload is sent to check the liveliness
        of the peer. Additional retries are done as per retransmit interval setting.
        Zero value disables liveliness checks.
    type: float
  perfectforwardsecrecy:
    choices:
      - ENABLE
      - DISABLE
    description:
      - Enable/Disable PFS.
    type: str
    default: DISABLE
  replaywindowsize:
    description:
      - IPSec Replay window size for the data traffic
    type: float
  retransmissiontime:
    description:
      - The interval in seconds to retry sending the IKE messages to peer, three consecutive
        attempts are done with doubled interval after every failure,
      - increases for every retransmit till 6 retransmits.
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
