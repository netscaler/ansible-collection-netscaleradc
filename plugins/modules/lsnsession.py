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
module: lsnsession
short_description: Configuration for lsn session resource.
description: Configuration for lsn session resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - flushed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(flushed), the resource will be flushed on the NetScaler ADC node.
    type: str
  clientname:
    type: str
    description:
      - Name of the LSN Client entity.
  natip:
    type: str
    description:
      - Mapped NAT IP address used in LSN sessions.
  natport2:
    type: int
    description:
      - Mapped NAT port used in the LSN sessions.
  nattype:
    type: str
    choices:
      - NAT44
      - DS-Lite
      - NAT64
    description:
      - Type of sessions to be displayed.
  netmask:
    type: str
    description:
      - Subnet mask for the IP address specified by the network parameter.
  network:
    type: str
    description:
      - IP address or network address of subscriber(s).
  network6:
    type: str
    description:
      - IPv6 address of the LSN subscriber or B4 device.
  nodeid:
    type: int
    description:
      - Unique number that identifies the cluster node.
  td:
    type: int
    description:
      - Traffic domain ID of the LSN client entity.
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
