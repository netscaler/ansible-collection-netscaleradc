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
module: routemap
short_description: Manage route map configuration on Citrix ADC (NetScaler) devices
description:
  - Manage route map configuration on Citrix ADC (NetScaler) devices.
version_added: 2.10.0
author:
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices: ["present", "absent"]
    default: present
    description:
      - The state of the resource on the NetScaler ADC node.
      - When C(present), the resource will be added or updated.
      - When C(absent), the resource will be deleted.
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
  name:
    type: str
    description:
      - Route map tag.
  rules_action:
    type: str
    choices: ["permit", "deny"]
    description:
      - Specifies if the route-map denies or permits the operations.
  rules_localPreference:
    type: int
    description:
      - Set the BGP local preference path attribute.
      - Minimum value is 0.
      - Maximum value is 4294967295.
  rules_matchAsPath:
    type: str
    description:
      - Match the BGP AS-path list.
  rules_matchCommunity:
    type: str
    description:
      - Match BGP community list.
  rules_matchIpAddress:
    type: str
    description:
      - Match IP address of route. IP access-list number in the range <1-99> or access-list name.
  rules_matchIpNextHop:
    type: str
    description:
      - Match next-hop address of route. IP access-list number in the range <1-99> or access-list name.
  rules_matchMetric:
    type: int
    description:
      - Match values from routing table. Match metric of route.
      - Minimum value is 0.
      - Maximum value is 4294967295.
  rules_matchRouteType:
    type: str
    choices: ["type-1", "type-2"]
    description:
      - Match OSPF external routes of type 1 or type 2 metrics.
  rules_sequence:
    type: int
    description:
      - Sequence to insert to/delete from existing route-map entry.
      - Minimum value is 1.
      - Maximum value is 65535.
  rules_setAsPath:
    type: str
    description:
      - Set the prepend string for a BGP AS-path attribute.
  rules_setCommunity:
    type: str
    description:
      - Set the BGP community attribute.
  rules_setIpNextHop:
    type: str
    description:
      - Set next hop address of a route.
  rules_setMetric:
    type: int
    description:
      - Set metric value for destination routing protocol.
      - Minimum value is 0.
      - Maximum value is 4294967295.
  rules_setMetricType:
    type: str
    choices: ["type-1", "type-2"]
    description:
      - Set type of metric for destination routing protocol. OSPF external type 1 metric or OSPF external type 2 metric.
  rules_weight:
    type: int
    description:
      - Set BGP weight for routing table.
      - Minimum value is 0.
      - Maximum value is 4294967295.
extends_documentation_fragment: netscaler.adc.netscaler_adc
"""

EXAMPLES = r"""
---
- name: Configure route map
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure route map
      delegate_to: localhost
      netscaler.adc.routemap:
        state: present
        name: "routeMap1"
        rules_action: "permit"
        rules_sequence: 10
        rules_matchIpAddress: "accessList1"
        rules_setMetric: 20
        rules_setMetricType: "type-1"
        rules_setCommunity: "commList1"
        rules_setAsPath: "asPathList1"
        rules_localPreference: 100
        rules_weight: 200
        rules_matchMetric: 10
        rules_matchRouteType: "type-1"
        rules_matchIpNextHop: "accessList2"
        rules_matchCommunity: "commList2"
        rules_matchAsPath: "asPathList2"
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
