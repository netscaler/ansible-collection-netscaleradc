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
module: bgprouter
short_description: Configuration for BGP Router resource.
description: Configuration for BGP Router resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    type: str
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler ADC node.
      - When C(present), the resource will be added/updated configured according to the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
  remove_non_updatable_params:
    type: str
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
  localAS:
    type: int
    description:
      - Autonomous system number for the BGP router.
  routerId:
    type: str
    description:
      - Router identifier for the BGP routing instance.
  afParams:
    type: list
    elements: dict
    description:
      - Address family parameters for the BGP router.
    suboptions:
      addressFamily:
        type: str
        description:
          - Address family of the routes.
        choices:
          - ipv4
          - ipv6
      redistribute:
        type: list
        elements: dict
        description:
          - Redistribution settings per protocol.
        suboptions:
          protocol:
            type: str
            description:
              - The protocol from which routes need to be redistributed.
            choices:
              - kernel
              - connected
              - static
              - rip
              - ospf
              - isis
              - intranet
          routeMap:
            type: str
            description:
              - Route map reference for redistribution.
  neighbor:
    type: dict
    description:
      - Neighbor router configuration.
    suboptions:
      ASOriginationInterval:
        type: int
        description:
          - Minimum interval between sending AS-origination routing updates.
      address:
        type: str
        description:
          - The IPv4 or IPv6 address of the neighboring router.
      advertisementInterval:
        type: int
        description:
          - Minimum interval between sending BGP routing updates.
      afParams:
        type: list
        elements: dict
        description:
          - Address family parameters for the neighbor.
        suboptions:
          activate:
            type: bool
            description:
              - Enable the address family for the neighbor.
          addressFamily:
            type: str
            description:
              - Address family identifier.
            choices:
              - ipv4
              - ipv6
          routeMap:
            type: list
            elements: dict
            description:
              - Route maps applied to neighbor routes.
            suboptions:
              direction:
                type: str
                description:
                  - Apply the route-map to incoming or outgoing routes.
                choices:
                  - in
                  - out
              name:
                type: str
                description:
                  - Name of the route-map.
      connectTimer:
        type: int
        description:
          - Time interval (in seconds) for the ConnectRetry timer.
      holdTimerConfig:
        type: int
        description:
          - Configured hold time for the neighbor.
      keepaliveTimerConfig:
        type: int
        description:
          - Configured keepalive time for the neighbor.
      md5Password:
        type: str
        description:
          - MD5 password for the neighbor.
      multihopBfd:
        type: bool
        description:
          - Enable BFD for multihop sessions.
      remoteAS:
        type: int
        description:
          - AS number of the neighbor.
      singlehopBfd:
        type: bool
        description:
          - Enable BFD on this neighbor.
      updateSource:
        type: str
        description:
          - Source of routing updates.

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
