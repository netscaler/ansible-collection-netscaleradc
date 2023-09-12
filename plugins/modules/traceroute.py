#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: traceroute
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  M:
    description:
      - Minimum TTL value used in outgoing probe packets.
    type: float
    default: 1
  P:
    description:
      - Send packets of specified IP protocol. The currently supported protocols are
        UDP and ICMP.
    type: str
  S:
    description:
      - Print a summary of how many probes were not answered for each hop.
    type: bool
  T:
    description:
      - Traffic Domain Id
    type: float
  host:
    description:
      - Destination host IP address or name.
    type: str
  m:
    description:
      - Maximum TTL value used in outgoing probe packets. For Nitro API, default value
        is taken as 10.
    type: int
    default: 64
  n:
    description:
      - Print hop addresses numerically instead of symbolically and numerically.
    type: bool
  p:
    description:
      - Base port number used in probes.
    type: int
    default: 33434
  packetlen:
    description:
      - Length (in bytes) of the query packets.
    type: int
    default: 44
  q:
    description:
      - Number of queries per hop. For Nitro API, defalut value is taken as 1.
    type: int
    default: 3
  r:
    description:
      - Bypass normal routing tables and send directly to a host on an attached network.
        If the host is not on a directly attached network, an error is returned.
    type: bool
  s:
    description:
      - Source IP address to use in the outgoing query packets. If the IP address
        does not belong to this appliance,  an error is returned and nothing is sent.
    type: str
  t:
    description:
      - Type-of-service in query packets.
    type: int
  v:
    description:
      - Verbose output. List received ICMP packets other than TIME_EXCEEDED and UNREACHABLE.
    type: bool
  w:
    description:
      - Time (in seconds) to wait for a response to a query. For Nitro API, defalut
        value is set to 3.
    type: int
    default: 5
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
