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
module: ipsecparameter
short_description: Configuration for IPSEC paramter resource.
description: Configuration for IPSEC paramter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
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
  perfectforwardsecrecy:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - Enable/Disable PFS.
  replaywindowsize:
    type: int
    description:
      - IPSec Replay window size for the data traffic
  retransmissiontime:
    type: int
    description:
      - The interval in seconds to retry sending the IKE messages to peer, three consecutive
        attempts are done with doubled interval after every failure,
      - increases for every retransmit till 6 retransmits.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ipsecparameter playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure ipsecparameter
      delegate_to: localhost
      netscaler.adc.ipsecparameter:
        state: present
        lifetime: '28800'
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
