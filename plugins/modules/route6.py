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
module: route6
short_description: Configuration for route 6 resource.
description: Configuration for route 6 resource.
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
        this route. The lower the cost, the higher the preference.
    type: float
    default: 1
  detail:
    description:
      - To get a detailed view.
    type: bool
  distance:
    description:
      - Administrative distance of this route from the appliance.
    type: float
    default: 1
  gateway:
    description:
      - The gateway for this route. The value for this parameter is either an IPv6
        address or null.
    type: str
  monitor:
    description:
      - Name of the monitor, of type ND6 or PING, configured on the Citrix ADC to
        monitor this route.
    type: str
  msr:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor this route with a monitor of type ND6 or PING.
    type: str
    default: DISABLED
  network:
    description:
      - IPv6 network address for which to add a route entry to the routing table of
        the Citrix ADC.
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for this route6. If owner node group is
        not specified then the route is treated as Striped route.
    type: str
    default: DEFAULT_NG
  routetype:
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
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: float
  vlan:
    description:
      - Integer value that uniquely identifies a VLAN through which the Citrix ADC
        forwards the packets for this route.
    type: float
  vxlan:
    description:
      - Integer value that uniquely identifies a VXLAN through which the Citrix ADC
        forwards the packets for this route.
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
