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
module: snmpmanager
short_description: Configuration for manager resource.
description: Configuration for manager resource.
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  domainresolveretry:
    type: int
    description:
      - Amount of time, in seconds, for which the Citrix ADC waits before sending
        another DNS query to resolve the host name of the SNMP manager if the last
        query failed. This parameter is valid for host-name based SNMP managers only.
        After a query succeeds, the TTL determines the wait time. The minimum and
        default value is 5.
  ipaddress:
    type: str
    description:
      - 'IP address of the SNMP manager. Can be an IPv4 or IPv6 address. You can instead
        specify an IPv4 network address or IPv6 network prefix if you want the Citrix
        ADC to respond to SNMP queries from any device on the specified network. Alternatively,
        instead of an IPv4 address, you can specify a host name that has been assigned
        to an SNMP manager. If you do so, you must add a DNS name server that resolves
        the host name of the SNMP manager to its IP address. '
      - 'Note: The Citrix ADC does not support host names for SNMP managers that have
        IPv6 addresses.'
  netmask:
    type: str
    description:
      - Subnet mask associated with an IPv4 network address. If the IP address specifies
        the address or host name of a specific host, accept the default value of 255.255.255.255.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample snmpmanager playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure snmpmanager
      delegate_to: localhost
      netscaler.adc.snmpmanager:
        state: present
        ipaddress:
          - citrix.com
        domainresolveretry: 6
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
