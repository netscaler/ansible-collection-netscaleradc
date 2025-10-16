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
module: routemap
short_description: Manage routemap configuration on Citrix ADC (NetScaler) devices
description:
  - Manage routemap configuration on Citrix ADC (NetScaler) devices.
version_added: 2.10.0
author:
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices: ["present", "absent", "unset", "get"]
    default: present
    description:
      - The state of the resource on the NetScaler ADC node.
      - When C(present), the resource will be added or updated.
      - When C(absent), the resource will be deleted.
      - When C(unset), the resource will be unset.
      - When C(get), retrieve the resource.
      - When C(delete), delete the resource.

  name:
    type: str
    description:
      - Route map tag.

  rules:
    type: list
    elements: dict
    description:
      - List of rule parameters for the route map entry.
    suboptions:
      action:
        type: str
        choices: ["permit", "deny"]
        description:
          - Specifies if the route-map denies or permits the operations.

      localPreference:
        type: int
        description:
          - Set the BGP local preference path attribute.

      matchAsPath:
        type: str
        description:
          - Match the BGP AS-path list.

      matchCommunity:
        type: str
        description:
          - Match BGP community list.

      matchIpAddress:
        type: str
        description:
          - Match IP address of route. IP access-list number in the range <1-99> or access-list name.

      matchIpNextHop:
        type: str
        description:
          - Match next-hop address of route. IP access-list number in the range <1-99> or access-list name.

      matchMetric:
        type: int
        description:
          - Match values from routing table. Match metric of route.

      matchRouteType:
        type: str
        choices: ["type-1", "type-2"]
        description:
          - Match OSPF external routes of type 1 or type 2 metrics.

      sequence:
        type: int
        description:
          - Sequence to insert to/delete from existing route-map entry.

      setAsPath:
        type: str
        description:
          - Set the prepend string for a BGP AS-path attribute.

      setCommunity:
        type: str
        description:
          - Set the BGP community attribute.

      setIpNextHop:
        type: str
        description:
          - Set next hop address of a route.

      setMetric:
        type: int
        description:
          - Set metric value for destination routing protocol.

      setMetricType:
        type: str
        choices: ["type-1", "type-2"]
        description:
          - Set type of metric for destination routing protocol. OSPF external type 1 metric or OSPF external type 2 metric.

      weight:
        type: int
        description:
          - Set BGP weight for routing table.

  remove_non_updatable_params:
    type: str
    choices: ["yes", "no"]
    default: "no"
    description:
      - Remove non-updatable parameters from the configuration.

extends_documentation_fragment: netscaler.adc.netscaler_adc
"""
EXAMPLES = r"""
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
