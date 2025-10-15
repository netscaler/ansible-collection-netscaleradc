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
module: ospfinterface
short_description: Configuration for OSPF Interface resource.
description: Configuration for OSPF Interface resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler ADC node.
      - When C(present), the resource will be added/updated configured according to the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
  remove_non_updatable_params:
    type: str
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.

  authKey:
    type: str
    description:
      - Authentication password (key) for the OSPF interface.
  authType:
    type: str
    choices:
      - null
      - simple
      - message-digest
    description:
      - Authentication type on the OSPF interface.
  bfd:
    type: bool
    description:
      - Enable or disable Bidirectional Forwarding Detection (BFD) on the interface.
  cost:
    type: int
    description:
      - Cost metric of the OSPF interface.
  deadInterval:
    type: int
    description:
      - Time interval (in seconds) after which a router is declared down if no Hello packets are received.
  helloInterval:
    type: int
    description:
      - Time interval (in seconds) between sending Hello packets on the interface.
  mtu:
    type: int
    description:
      - Maximum Transmission Unit size on the interface.
  name:
    type: str
    description:
      - Name of the OSPF interface.
  networkType:
    type: str
    description:
      - Type of the OSPF network.
  priority:
    type: int
    description:
      - Router priority used in the designated router election process.
  retransmitInterval:
    type: int
    description:
      - Time interval (in seconds) between retransmissions of Link State Advertisements (LSAs).
  transmitDelay:
    type: int
    description:
      - Delay in seconds on the interface before transmitting LSAs.

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
