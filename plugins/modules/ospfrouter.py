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
module: ospfrouter
short_description: Configuration for OSPF Router resource.
description: Configuration for OSPF Router resource.
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
  routerId:
    description:
      - Router ID for the OSPF process
    type: str
  processId:
    description:
      - OSPF process ID
    type: int
  networks:
    description:
      - Network configurations for OSPF
    type: list
    elements: dict
    suboptions:
      ipaddress:
        description:
          - IP address of the network
        type: str
      netmask:
        description:
          - Network mask
        type: int
      area:
        description:
          - OSPF area ID
        type: int
  passiveInterface:
    description:
      - List of passive interfaces
    type: list
    elements: str
  redistribute:
    description:
      - Route redistribution configuration
    type: list
    elements: dict
    suboptions:
      protocol:
        description:
          - Protocol to redistribute
        type: str
        choices: ['bgp', 'connected', 'intranet', 'isis', 'kernel', 'ospf', 'rip', 'static']
      metric:
        description:
          - Metric for redistributed routes
        type: int
      metricType:
        description:
          - Metric type for redistributed routes
        type: int
      routeMap:
        description:
          - Route map for redistribution
        type: str
      tag:
        description:
          - Tag for redistributed routes
        type: int
      ospfProcessId:
        description:
          - OSPF process ID for redistribution
        type: int
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ospfrouter playbook
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure ospfrouter
      delegate_to: localhost
      netscaler.adc.ospfrouter:
        state: present
        processId: 1
        routerId: "1.1.1.1"
        passiveInterface:
          - vlan22
        redistribute:
          - protocol: connected
        networks:
          - ipaddress: "33.1.2.5"
            netmask: 25
            area: 1
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
