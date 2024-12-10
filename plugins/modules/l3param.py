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
module: l3param
short_description: Configuration for Layer 3 related parameter resource.
description: Configuration for Layer 3 related parameter resource.
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
  acllogtime:
    type: str
    description:
      - Parameter to tune acl logging time
  allowclasseipv4:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv4 Class E address clients
  dropdfflag:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping the IP DF flag.
  dropipfragments:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping of IP fragments.
  dynamicrouting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable Dynamic routing on partition. This configuration is not applicable
        to default partition
  externalloopback:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable external loopback.
  forwardicmpfragments:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable forwarding of ICMP fragments.
  icmpgenratethreshold:
    type: float
    description:
      - NS generated ICMP pkts per 10ms rate threshold
  implicitaclallow:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Do not apply ACLs for internal ports
  implicitpbr:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable Policy Based Routing for control packets
  ipv6dynamicrouting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv6 Dynamic routing
  miproundrobin:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable round robin usage of mapped IPs.
  overridernat:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - USNIP/USIP settings override RNAT settings for configured
      - '              service/virtual server traffic..'
  srcnat:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform NAT if only the source is in the private network
  tnlpmtuwoconn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable learning PMTU of IP tunnel when ICMP error does not contain
        connection information.
  usipserverstraypkt:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable detection of stray server side pkts in USIP mode.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample l3param playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure l3param
      delegate_to: localhost
      netscaler.adc.l3param:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        icmperrgenerate: DISABLED
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
