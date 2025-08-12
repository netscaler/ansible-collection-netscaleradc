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
module: bgpRouter
short_description: Manage BGP Router configuration on Citrix ADC (NetScaler) devices
description:
  - Manage BGP Router configurations on Citrix ADC (NetScaler) devices.
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

  afParams.addressFamily:
    type: str
    choices: ["ipv4", "ipv6"]
    description:
      - Address family for this BGP AF parameter.

  afParams.redistribute.protocol:
    type: str
    choices: ["kernel", "connected", "static", "rip", "ospf", "isis", "intranet"]
    description:
      - The protocol from which routes need to be redistributed.

  afParams.redistribute.routeMap:
    type: str
    description:
      - Route map reference.

  localAS:
    type: int
    description:
      - Local Autonomous System number.

  routerId:
    type: str
    description:
      - Router ID in IP address format.

  neighbor.ASOriginationInterval:
    type: int
    description:
      - Minimum interval between sending AS-origination routing updates.

  neighbor.address:
    type: str
    description:
      - Address of the neighboring router.

  neighbor.advertisementInterval:
    type: int
    description:
      - Minimum interval between sending BGP routing updates.

  neighbor.afParams.activate:
    type: bool
    description:
      - Enable the Address Family for the neighbor.

  neighbor.afParams.addressFamily:
    type: str
    choices: ["ipv4", "ipv6"]
    description:
      - Address family identifier.

  neighbor.afParams.routeMap.direction:
    type: str
    choices: ["in", "out"]
    description:
      - Apply the route-map to incoming or outgoing routes.

  neighbor.afParams.routeMap.name:
    type: str
    description:
      - Name of the route map.

  neighbor.connectTimer:
    type: int
    description:
      - Time interval (in seconds) for the ConnectRetry timer.

  neighbor.holdTimerConfig:
    type: int
    description:
      - Hold timer value for the neighbor in seconds.

  neighbor.keepaliveTimerConfig:
    type: int
    description:
      - Keepalive timer value for the neighbor in seconds.

  neighbor.md5Password:
    type: str
    description:
      - MD5 password used for neighbor authentication.
    no_log: true

  neighbor.multihopBfd:
    type: bool
    description:
      - Enable BFD for multihop BGP sessions.

  neighbor.remoteAS:
    type: int
    description:
      - Remote AS number for the neighbor.

  neighbor.singlehopBfd:
    type: bool
    description:
      - Enable BFD on this neighbor.

  neighbor.updateSource:
    type: str
    description:
      - Source of routing updates.
"""
EXAMPLES = r"""
---
- name: BGP routing
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure BGP routing
      delegate_to: localhost
      netscaler.adc.bgpRouter:
        state: present
        localAS: 10
        afParams.addressFamily: "ipv4"
        afParams.redistribute.protocol: "kernel"
        routerId: "10.102.201.219"
        neighbor.ASOriginationInterval: 15
        neighbor.address: "2.2.12.30"
        neighbor.advertisementInterval: 30
        neighbor.afParams.addressFamily: "ipv4"
        neighbor.holdTimerConfig: 90
        neighbor.keepaliveTimerConfig: 30
        neighbor.multihopBfd: "False"
        neighbor.remoteAS: 100
        neighbor.singlehopBfd: "False"
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
