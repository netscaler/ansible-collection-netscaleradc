#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: route
short_description: Configuration for route resource.
description: Configuration for route resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
    type: raw
    choices:
      - DISABLED
      - ENABLED
    description:
      - Advertise this route.
  cost:
    type: float
    description:
      - Positive integer used by the routing algorithms to determine preference for
        using this route. The lower the cost, the higher the preference.
  cost1:
    type: raw
    description:
      - 'The cost of a route is used to compare routes of the same type. The route
        having the lowest cost is the most preferred route. Possible values: 0 through
        65535. Default: 0.'
  detail:
    type: bool
    description:
      - Display a detailed view.
  distance:
    type: raw
    description:
      - Administrative distance of this route, which determines the preference of
        this route over other routes, with same destination, from different routing
        protocols. A lower value is preferred.
  gateway:
    type: raw
    description:
      - IP address of the gateway for this route. Can be either the IP address of
        the gateway, or can be null to specify a null interface route.
  monitor:
    type: raw
    description:
      - Name of the monitor, of type ARP or PING, configured on the Citrix ADC to
        monitor this route.
  msr:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor this route using a monitor of type ARP or PING.
  netmask:
    type: raw
    description:
      - The subnet mask associated with the network address.
  network:
    type: raw
    description:
      - IPv4 network address for which to add a route entry in the routing table of
        the Citrix ADC.
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for this route. If owner node group is not
        specified then the route is treated as Striped route.
  protocol:
    type: raw
    choices:
      - OSPF
      - ISIS
      - RIP
      - BGP
    description:
      - Routing protocol used for advertising this route.
  routetype:
    type: str
    choices:
      - CONNECTED
      - STATIC
      - DYNAMIC
      - OSPF
      - ISIS
      - RIP
      - BGP
    description:
      - Protocol used by routes that you want to remove from the routing table of
        the Citrix ADC.
  td:
    type: raw
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  vlan:
    type: float
    description:
      - VLAN as the gateway for this route.
  weight:
    type: raw
    description:
      - Positive integer used by the routing algorithms to determine preference for
        this route over others of equal cost. The lower the weight, the higher the
        preference.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample Playbook
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Sample Task | route
      delegate_to: localhost
      netscaler.adc.route:
        state: present
        network: 172.31.0.0
        netmask: 255.255.0.0
        gateway: 172.31.0.1
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
