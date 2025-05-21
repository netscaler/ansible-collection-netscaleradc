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
module: dnsaction64
short_description: Configuration for dns64 action resource.
description: Configuration for dns64 action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  actionname:
    type: str
    description:
      - Name of the dns64 action.
  excluderule:
    type: str
    description:
      - The expression to select the criteria for eliminating the corresponding ipv6
        addresses from the response.
  mappedrule:
    type: str
    description:
      - The expression to select the criteria for ipv4 addresses to be used for synthesis.
      - '                      Only if the mappedrule is evaluated to true the corresponding
        ipv4 address is used for synthesis using respective prefix,'
      - '                      otherwise the A RR is discarded'
  prefix:
    type: str
    description:
      - The dns64 prefix to be used if the after evaluating the rules
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnsaction64 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnsaction64
      delegate_to: localhost
      netscaler.adc.dnsaction64:
        state: present
        actionname: dns64_act2
        prefix: 64:ff9b::/96
        mappedrule: DNS.RR.TYPE.EQ(A) && !(DNS.RR.RDATA.IP.IN_SUBNET(0.0.0.0/8) ||
          DNS.RR.RDATA.IP.IN_SUBNET(10.0.0.0/8))
        excluderule: DNS.RR.TYPE.EQ(AAAA) && DNS.RR.RDATA.IPV6.IN_SUBNET(::ffff:0:0/96)
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
