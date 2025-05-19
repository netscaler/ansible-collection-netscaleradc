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
module: ping6
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
  I:
    type: str
    description:
      - Network interface on which to ping, if you have multiple interfaces.
  S:
    type: str
    description:
      - Source IP address to be used in the outgoing query packets.
  T:
    type: int
    description:
      - Traffic Domain Id
  V:
    type: int
    description:
      - VLAN ID for link local address.
  b:
    type: int
    description:
      - Set socket buffer size. If used, should be used with roughly +100 then the
        datalen (-s option). The default value is 8192.
  c:
    type: int
    description:
      - Number of packets to send. The default value is infinite. For Nitro API, defalut
        value is taken as 5.
  hostName:
    type: str
    description:
      - Address of host to ping.
  i:
    type: int
    description:
      - Waiting time, in seconds. The default value is 1 second.
  m:
    type: bool
    description:
      - By default, ping6 asks the kernel to fragment packets to fit into the minimum
        IPv6 MTU.The -m option will suppress the behavior for unicast packets.
  n:
    type: bool
    description:
      - Numeric output only. No name resolution.
  p:
    type: str
    description:
      - Pattern to fill in packets. Can be up to 16 bytes, useful for diagnosing data-dependent
        problems.
  q:
    type: bool
    description:
      - Quiet output. Only summary is printed. For Nitro API, this flag is set by
        default
  s:
    type: int
    description:
      - Data size, in bytes. The default value is 32.
  t:
    type: int
    description:
      - Timeout in seconds before ping6 exits
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
