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
module: dnsmxrec
short_description: Configuration for MX record resource.
description: Configuration for MX record resource.
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
  domain:
    type: str
    description:
      - Domain name for which to add the MX record.
  ecssubnet:
    type: str
    description:
      - Subnet for which the cached MX record need to be removed.
  mx:
    type: str
    description:
      - Host name of the mail exchange server.
  nodeid:
    type: float
    description:
      - Unique number that identifies the cluster node.
  pref:
    type: float
    description:
      - Priority number to assign to the mail exchange server. A domain name can have
        multiple mail servers, with a priority number assigned to each server. The
        lower the priority number, the higher the mail server's priority. When other
        mail servers have to deliver mail to the specified domain, they begin with
        the mail server with the lowest priority number, and use other configured
        mail servers, in priority order, as backups.
  ttl:
    type: float
    description:
      - Time to Live (TTL), in seconds, for the record. TTL is the time for which
        the record must be cached by DNS proxies. The specified TTL is applied to
        all the resource records that are of the same record type and belong to the
        specified domain name. For example, if you add an address record, with a TTL
        of 36000, to the domain name example.com, the TTLs of all the address records
        of example.com are changed to 36000. If the TTL is not specified, the Citrix
        ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available
        on the appliance, the default value of 3600.
  type:
    type: str
    choices:
      - ALL
      - ADNS
      - PROXY
    description:
      - 'Type of records to display. Available settings function as follows:'
      - '* C(ADNS) - Display all authoritative address records.'
      - '* C(PROXY) - Display all proxy address records.'
      - '* C(ALL) - Display all address records.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnsmxrec playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnsmxrec
      delegate_to: localhost
      netscaler.adc.dnsmxrec:
        state: present
        domain: n2.com
        mx: mail.n1.com
        pref: '23'
        ttl: 3601
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
