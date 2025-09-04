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
module: ospf6router
short_description: Manage OSPF router configuration on Citrix ADC (NetScaler) devices
description:
  - Manage OSPF router configuration on Citrix ADC (NetScaler) devices.
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
  afParams_addressFamily:
    type: str
    choices: ["ipv4", "ipv6"]
    description:
      - IPv4 or IPv6 Address Family.
  afParams_redistribute_metric:
    type: int
    description:
      - The metric of redistributed routes.
      - Minimum value is 0.
      - Maximum value is 16777214.
  afParams_redistribute_metricType:
    type: int
    description:
      - OSPFv3 metric type for default routes - OSPFv3 External Type 1 metrics or Type 2 metrics.
      - Minimum value is 1.
      - Maximum value is 2.
  afParams_redistribute_protocol:
    type: str
    choices: ["bgp", "connected", "isis", "kernel", "ospf", "rip", "static"]
    description:
      - The protocol from which routes need to be redistributed.
  afParams_redistribute_routeMap:
    type: str
    description:
      - Route map reference.
  tag:
    type: str
    description:
      - Set tag for routes redistributed into OSPFv3.
  passiveInterface:
    type: list
    description:
      - Suppress routing updates on an interface.
  routerId:
    type: str
    description:
      - Router-id for the OSPFv3 process.
  tagId:
    type: str
    description:
      - OSPFv3 Tag.
extends_documentation_fragment: netscaler.adc.netscaler_adc
"""
EXAMPLES = r""""""
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
