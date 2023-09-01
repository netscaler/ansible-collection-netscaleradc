#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
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
  advertise:
    choices:
      - DISABLED
      - ENABLED
    description:
      - Advertise this route.
    type: str
  cost:
    description:
      - Positive integer used by the routing algorithms to determine preference for
        using this route. The lower the cost, the higher the preference.
    type: float
  cost1:
    description:
      - 'The cost of a route is used to compare routes of the same type. The route
        having the lowest cost is the most preferred route. Possible values: 0 through
        65535. Default: 0.'
    type: float
  detail:
    description:
      - Display a detailed view.
    type: bool
  distance:
    description:
      - Administrative distance of this route, which determines the preference of
        this route over other routes, with same destination, from different routing
        protocols. A lower value is preferred.
    type: float
    default: 1
  gateway:
    description:
      - IP address of the gateway for this route. Can be either the IP address of
        the gateway, or can be null to specify a null interface route.
    type: str
  monitor:
    description:
      - Name of the monitor, of type ARP or PING, configured on the Citrix ADC to
        monitor this route.
    type: str
  msr:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor this route using a monitor of type ARP or PING.
    type: str
    default: DISABLED
  netmask:
    description:
      - The subnet mask associated with the network address.
    type: str
  network:
    description:
      - IPv4 network address for which to add a route entry in the routing table of
        the Citrix ADC.
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for this route. If owner node group is not
        specified then the route is treated as Striped route.
    type: str
    default: DEFAULT_NG
  protocol:
    choices:
      - OSPF
      - ISIS
      - RIP
      - BGP
    description:
      - Routing protocol used for advertising this route.
    type: list
    elements: str
    default: ADV_ROUTE_FLAGS
  routetype:
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
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: float
  vlan:
    description:
      - VLAN as the gateway for this route.
    type: float
  weight:
    description:
      - Positive integer used by the routing algorithms to determine preference for
        this route over others of equal cost. The lower the weight, the higher the
        preference.
    type: float
    default: 1
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
