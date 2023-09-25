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
module: ping
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  I:
    description:
      - Network interface on which to ping, if you have multiple interfaces.
    type: str
  S:
    description:
      - Source IP address to be used in the outgoing query packets. If the IP addrESS
        does not belongs to this appliance, an error is returned and nothing is sent.
    type: str
  T:
    description:
      - Traffic Domain Id
    type: float
  c:
    description:
      - Number of packets to send. The default value is infinite. For Nitro API, defalut
        value is taken as 5.
    type: float
  hostName:
    description:
      - Address of host to ping.
    type: str
  i:
    description:
      - Waiting time, in seconds. The default value is 1 second.
    type: float
  n:
    description:
      - Numeric output only. No name resolution.
    type: bool
  p:
    description:
      - Pattern to fill in packets.  Can be up to 16 bytes, useful for diagnosing
        data-dependent problems.
    type: str
  q:
    description:
      - Quiet output. Only the summary is printed. For Nitro API, this flag is set
        by default.
    type: bool
  s:
    description:
      - Data size, in bytes. The default value is 56.
    type: float
  t:
    description:
      - Time-out, in seconds, before ping exits.
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
