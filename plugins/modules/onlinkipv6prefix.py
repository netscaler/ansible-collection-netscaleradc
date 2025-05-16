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
module: onlinkipv6prefix
short_description: Configuration for on-link IPv6 global prefixes for Router Advertisment
  resource.
description: Configuration for on-link IPv6 global prefixes for Router Advertisment
  resource.
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  autonomusprefix:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix Autonomus flag.
  decrementprefixlifetimes:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix Autonomus flag.
  depricateprefix:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Depricate the prefix.
  ipv6prefix:
    type: str
    description:
      - Onlink prefixes for RA messages.
  onlinkprefix:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix onlink flag.
  prefixpreferredlifetime:
    type: float
    description:
      - Preferred life time of the prefix, in seconds.
  prefixvalidelifetime:
    type: float
    description:
      - Valide life time of the prefix, in seconds.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample onlinkipv6prefix playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure onlinkipv6prefix
      delegate_to: localhost
      netscaler.adc.onlinkipv6prefix:
        state: present
        ipv6prefix: 2001::/64
        onlinkprefix: 'NO'
        autonomusprefix: 'NO'
        depricateprefix: 'YES'
        decrementprefixlifetimes: 'YES'
        prefixvalidelifetime: '30'
        prefixpreferredlifetime: '20'
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
