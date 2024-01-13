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
module: l2param
short_description: Configuration for Layer 2 related parameter resource.
description: Configuration for Layer 2 related parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  bdggrpproxyarp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set/reset proxy ARP in bridge group deployment
  bdgsetting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Bridging settings for C2C behavior. If enabled, each PE will learn MAC entries
        independently. Otherwise, when L2 mode is ON, learned MAC entries on a PE
        will be broadcasted to all other PEs.
  bridgeagetimeout:
    type: float
    description:
      - Time-out value for the bridge table entries, in seconds. The new value applies
        only to the entries that are dynamically learned after the new value is set.
        Previously existing bridge table entries expire after the previously configured
        time-out value.
  garponvridintf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send GARP messagess on VRID-configured interfaces upon failover
  garpreply:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set/reset REPLY form of GARP
  macmodefwdmypkt:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allows MAC mode vserver to pick and forward the packets even if it is destined
        to Citrix ADC owned VIP.
  maxbridgecollision:
    type: float
    description:
      - Maximum bridge collision for loop detection
  mbfinstlearning:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable instant learning of MAC changes in MBF mode.
  mbfpeermacupdate:
    type: float
    description:
      - When mbf_instant_learning is enabled, learn any changes in peer's MAC after
        this time interval, which is in 10ms ticks.
  proxyarp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Proxies the ARP as Citrix ADC MAC for FreeBSD.
  returntoethernetsender:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Return to ethernet sender.
  rstintfonhafo:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the reset interface upon HA failover.
  skipproxyingbsdtraffic:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Control source parameters (IP and Port) for FreeBSD initiated traffic. If
        Enabled, source parameters are retained. Else proxy the source parameters
        based on next hop.
  stopmacmoveupdate:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Stop Update of server mac change to NAT sessions.
  usemymac:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use Citrix ADC MAC for all outgoing packets.
  usenetprofilebsdtraffic:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Control source parameters (IP and Port) for FreeBSD initiated traffic. If
        enabled proxy the source parameters based on netprofile source ip. If netprofile
        does not have ip configured, then it will continue to use NSIP as earlier.
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
