#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: ipsecprofile
short_description: Configuration for IPSEC profile resource.
description: Configuration for IPSEC profile resource.
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  encalgo:
    type: list
    choices:
      - AES
      - AES192
      - AES256
    description:
      - 'Type of encryption algorithm (Note: Selection of C(AES) enables AES128)'
    elements: str
  hashalgo:
    type: list
    choices:
      - HMAC_SHA1
      - HMAC_SHA256
      - HMAC_SHA384
      - HMAC_SHA512
      - HMAC_MD5
    description:
      - Type of hashing algorithm
    elements: str
  ikeretryinterval:
    type: int
    description:
      - IKE retry interval for bringing up the connection
  ikeversion:
    type: str
    choices:
      - V1
      - V2
    description:
      - IKE Protocol Version
  lifetime:
    type: int
    description:
      - Lifetime of IKE SA in seconds. Lifetime of IPSec SA will be (lifetime of IKE
        SA/8)
  livenesscheckinterval:
    type: int
    description:
      - Number of seconds after which a notify payload is sent to check the liveliness
        of the peer. Additional retries are done as per retransmit interval setting.
        Zero value disables liveliness checks.
  name:
    type: str
    description:
      - The name of the ipsec profile
  peerpublickey:
    type: str
    description:
      - Peer public key file path
  perfectforwardsecrecy:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - Enable/Disable PFS.
  privatekey:
    type: str
    description:
      - Private key file path
  psk:
    type: str
    description:
      - Pre shared key value
  publickey:
    type: str
    description:
      - Public key file path
  replaywindowsize:
    type: int
    description:
      - IPSec Replay window size for the data traffic
  retransmissiontime:
    type: int
    description:
      - The interval in seconds to retry sending the IKE messages to peer, three consecutive
        attempts are done with doubled interval after every failure.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ipsecprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure ipsecprofile
      delegate_to: localhost
      netscaler.adc.ipsecprofile:
        state: present
        name: ia_ipsecpro10
        publickey: sample
        privatekey: sample
        peerpublickey: sample
        livenesscheckinterval: '23'
        replaywindowsize: '23'
        ikeretryinterval: '60'
        retransmissiontime: '23'
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
