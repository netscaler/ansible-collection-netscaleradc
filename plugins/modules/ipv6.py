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
module: ipv6
short_description: Configuration for ip v6 resource.
description: Configuration for ip v6 resource.
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
  dodad:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to do Duplicate Address
      - Detection (DAD) for all the Citrix ADC owned IPv6 addresses regardless of
        whether they are obtained through stateless auto configuration, DHCPv6, or
        manual configuration.
  natprefix:
    type: str
    description:
      - Prefix used for translating packets from private IPv6 servers to IPv4 packets.
        This prefix has a length of 96 bits (128-32 = 96). The IPv6 servers embed
        the destination IP address of the IPv4 servers or hosts in the last 32 bits
        of the destination IP address field of the IPv6 packets. The first 96 bits
        of the destination IP address field are set as the IPv6 NAT prefix. IPv6 packets
        addressed to this prefix have to be routed to the Citrix ADC to ensure that
        the IPv6-IPv4 translation is done by the appliance.
  ndbasereachtime:
    type: int
    description:
      - Base reachable time of the Neighbor Discovery (ND6) protocol. The time, in
        milliseconds, that the Citrix ADC assumes an adjacent device is reachable
        after receiving a reachability confirmation.
  ndretransmissiontime:
    type: int
    description:
      - Retransmission time of the Neighbor Discovery (ND6) protocol. The time, in
        milliseconds, between retransmitted Neighbor Solicitation (NS) messages, to
        an adjacent device.
  ralearning:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to learn about various routes from Router Advertisement
        (RA) and Router Solicitation (RS) messages sent by the routers.
  routerredirection:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to do Router Redirection.
  td:
    type: int
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  usipnatprefix:
    type: str
    description:
      - IPV6 NATPREFIX used in NAT46 scenario when USIP is turned on
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ipv6 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure ipv6
      delegate_to: localhost
      netscaler.adc.ipv6:
        state: present
        routerredirection: ENABLED
        ndbasereachtime: '20000'
        ndretransmissiontime: '2000'
        natprefix: 2001::/96
        dodad: ENABLED
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
