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
module: dnsnameserver
short_description: Configuration for name server resource.
description: Configuration for name server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  dnsprofilename:
    type: str
    description:
      - Name of the DNS profile to be associated with the name server
  dnsvservername:
    type: str
    description:
      - Name of a DNS virtual server. Overrides any IP address-based name servers
        configured on the Citrix ADC.
  ip:
    type: str
    description:
      - IP address of an external name server or, if the Local parameter is set, IP
        address of a local DNS server (LDNS).
  local:
    type: bool
    description:
      - Mark the IP address as one that belongs to a local recursive DNS server on
        the Citrix ADC. The appliance recursively resolves queries received on an
        IP address that is marked as being local. For recursive resolution to work,
        the global DNS parameter, Recursion, must also be set.
      - ''
      - If no name server is marked as being local, the appliance functions as a stub
        resolver and load balances the name servers.
  type:
    type: str
    choices:
      - UDP
      - TCP
      - UDP_TCP
    description:
      - Protocol used by the name server. C(UDP_TCP) is not valid if the name server
        is a DNS virtual server configured on the appliance.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnsnameserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnsnameserver
      delegate_to: localhost
      netscaler.adc.dnsnameserver:
        state: present
        dnsvservername: LB_dnsv1
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
