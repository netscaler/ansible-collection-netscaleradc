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
---
module: nsmode
short_description: Configuration for ns mode resource.
description: Configuration for ns mode resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - enabled
      - disabled
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
    type: str
  mode:
    type: list
    choices:
      - FR
      - FastRamp
      - L2
      - L2mode
      - L3
      - L3mode
      - USIP
      - UseSourceIP
      - CKA
      - ClientKeepAlive
      - TCPB
      - TCPBuffering
      - MBF
      - MACbasedforwarding
      - Edge
      - USNIP
      - SRADV
      - DRADV
      - IRADV
      - SRADV6
      - DRADV6
      - PMTUD
      - RISE_APBR
      - RISE_RHI
      - BridgeBPDUs
      - SINGLE_IP
      - ULFD
    description:
      - Mode to be enabled. Multiple modes can be specified by providing a blank space
        between each mode.
    elements: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsmode playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nsmode
      delegate_to: localhost
      netscaler.adc.nsmode:
        state: present
        usnip: 'true'
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
