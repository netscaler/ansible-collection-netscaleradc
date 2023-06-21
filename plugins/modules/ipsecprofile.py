#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: ipsecprofile
short_description: Configuration for IPSEC profile resource.
description: Configuration for IPSEC profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  encalgo:
    description:
      - 'Type of encryption algorithm (Note: Selection of AES enables AES128)'
    type: list
    elements: str
    choices:
      - AES
      - AES192
      - AES256
  hashalgo:
    description:
      - Type of hashing algorithm
    type: list
    elements: str
    choices:
      - HMAC_SHA1
      - HMAC_SHA256
      - HMAC_SHA384
      - HMAC_SHA512
      - HMAC_MD5
  ikeretryinterval:
    description:
      - IKE retry interval for bringing up the connection
    type: int
  ikeversion:
    description:
      - IKE Protocol Version
    type: str
    choices:
      - V1
      - V2
  lifetime:
    description:
      - Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE
        SA/8)
    type: int
  livenesscheckinterval:
    description:
      - Number of seconds after which a notify payload is sent to check the liveliness
        of the peer. Additional retries are done as per retransmit interval setting.
        Zero value disables liveliness checks.
    type: int
  name:
    description:
      - The name of the ipsec profile
    type: str
  peerpublickey:
    description:
      - Peer public key file path
    type: str
  perfectforwardsecrecy:
    description:
      - Enable/Disable PFS.
    type: str
    choices:
      - ENABLE
      - DISABLE
  privatekey:
    description:
      - Private key file path
    type: str
  psk:
    description:
      - Pre shared key value
    type: str
  publickey:
    description:
      - Public key file path
    type: str
  replaywindowsize:
    description:
      - IPSec Replay window size for the data traffic
    type: int
  retransmissiontime:
    description:
      - The interval in seconds to retry sending the IKE messages to peer, three consecutive
        attempts are done with doubled interval after every failure.
    type: int
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
