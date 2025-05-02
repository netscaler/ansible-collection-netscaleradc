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
module: dnsproxyrecords
short_description: Configuration for proxy record resource.
description: Configuration for proxy record resource.
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  negrectype:
    type: str
    choices:
      - NXDOMAIN
      - NODATA
    description:
      - Filter the Negative DNS records i.e C(NXDOMAIN) and C(NODATA) entries to be
        flushed. e.g flush dns proxyRecords C(NXDOMAIN) will flush only the C(NXDOMAIN)
        entries from the cache
  type:
    type: str
    choices:
      - A
      - NS
      - CNAME
      - SOA
      - MX
      - AAAA
      - SRV
      - RRSIG
      - NSEC
      - DNSKEY
      - PTR
      - TXT
      - NAPTR
      - CAA
    description:
      - Filter the DNS records to be flushed.e.g flush dns proxyRecords -type C(A)   will
        flush only the C(A) records from the cache.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample Playbook for netscaler.adc.dnsproxyrecords
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Flush DNS Proxy records
      delegate_to: localhost
      netscaler.adc.dnsproxyrecords:
        state: flushed
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
