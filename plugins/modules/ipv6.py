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
module: ipv6
short_description: Configuration for ip v6 resource.
description: Configuration for ip v6 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  dodad:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to do Duplicate Address
      - Detection (DAD) for all the Citrix ADC owned IPv6 addresses regardless of
        whether they are obtained through stateless auto configuration, DHCPv6, or
        manual configuration.
    type: str
    default: DISABLED
  natprefix:
    description:
      - Prefix used for translating packets from private IPv6 servers to IPv4 packets.
        This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed
        the destination IP address of the IPv4 servers or hosts in the last 32 bits
        of the destination IP address field of the IPv6 packets. The first 96 bits
        of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets
        addressed to this prefix have to be routed to the Citrix ADC to ensure that
        the IPv6-IPv4 translation is done by the appliance.
    type: str
  ndbasereachtime:
    description:
      - Base reachable time of the Neighbor Discovery (ND6) protocol. The time, in
        milliseconds, that the Citrix ADC assumes an adjacent device is reachable
        after receiving a reachability confirmation.
    type: float
    default: 30000
  ndretransmissiontime:
    description:
      - Retransmission time of the Neighbor Discovery (ND6) protocol. The time, in
        milliseconds, between retransmitted Neighbor Solicitation (NS) messages, to
        an adjacent device.
    type: float
    default: 1000
  ralearning:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to learn about various routes from Router Advertisement
        (RA) and Router Solicitation (RS) messages sent by the routers.
    type: str
    default: DISABLED
  routerredirection:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to do Router Redirection.
    type: str
    default: DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: float
  usipnatprefix:
    description:
      - IPV6 NATPREFIX used in NAT46 scenario when USIP is turned on
    type: str
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
