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
module: route6
short_description: Configuration for route 6 resource.
description: Configuration for route 6 resource.
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
  advertise:
    type: str
    choices:
      - DISABLED
      - ENABLED
    description:
      - Advertise this route.
  cost:
    type: int
    description:
      - Positive integer used by the routing algorithms to determine preference for
        this route. The lower the cost, the higher the preference.
  detail:
    type: bool
    description:
      - To get a detailed view.
  distance:
    type: int
    description:
      - Administrative distance of this route from the appliance.
  gateway:
    type: str
    description:
      - The gateway for this route. The value for this parameter is either an IPv6
        address or null.
  mgmt:
    type: bool
    description:
      - Route in management plane.
  monitor:
    type: str
    description:
      - Name of the monitor, of type ND6 or PING, configured on the Citrix ADC to
        monitor this route.
  msr:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor this route with a monitor of type ND6 or PING.
  network:
    type: str
    description:
      - IPv6 network address for which to add a route entry to the routing table of
        the Citrix ADC.
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for this route6. If owner node group is
        not specified then the route is treated as Striped route.
  routetype:
    type: str
    choices:
      - CONNECTED
      - STATIC
      - DYNAMIC
      - OSPF
      - ISIS
      - BGP
      - RIP
      - ND-RA-ROUTE
      - FIB6
    description:
      - Type of IPv6 routes to remove from the routing table of the Citrix ADC.
  td:
    type: int
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  vlan:
    type: int
    description:
      - Integer value that uniquely identifies a VLAN through which the Citrix ADC
        forwards the packets for this route.
  vxlan:
    type: int
    description:
      - Integer value that uniquely identifies a VXLAN through which the Citrix ADC
        forwards the packets for this route.
  weight:
    type: int
    description:
      - Positive integer used by the routing algorithms to determine preference for
        this route over others of equal cost. The lower the weight, the higher the
        preference.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample route6 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure route6
      delegate_to: localhost
      netscaler.adc.route6:
        state: present
        network: 202::/64
        gateway: fe80::1234
        vlan: '23'
        weight: '10'
        distance: '10'
        cost: '10'
        advertise: ENABLED
        msr: ENABLED
        monitor: ia_mon1
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
