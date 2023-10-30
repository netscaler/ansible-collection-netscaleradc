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
module: l3param
short_description: Configuration for Layer 3 related parameter resource.
description: Configuration for Layer 3 related parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
    type: str
  acllogtime:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to tune acl logging time
  allowclasseipv4:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv4 Class E address clients
    default: DISABLED
  dropdfflag:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping the IP DF flag.
    default: DISABLED
  dropipfragments:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping of IP fragments.
    default: DISABLED
  dynamicrouting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable Dynamic routing on partition. This configuration is not applicable
        to default partition
    default: DISABLED
  externalloopback:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable external loopback.
    default: DISABLED
  forwardicmpfragments:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable forwarding of ICMP fragments.
    default: DISABLED
  icmpgenratethreshold:
    type: float
    description:
      - NS generated ICMP pkts per 10ms rate threshold
    default: 100
  implicitaclallow:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Do not apply ACLs for internal ports
    default: ENABLED
  ipv6dynamicrouting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv6 Dynamic routing
    default: DISABLED
  miproundrobin:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable round robin usage of mapped IPs.
    default: ENABLED
  overridernat:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - USNIP/USIP settings override RNAT settings for configured
      - '              service/virtual server traffic..'
    default: DISABLED
  srcnat:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform NAT if only the source is in the private network
    default: ENABLED
  tnlpmtuwoconn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable learning PMTU of IP tunnel when ICMP error does not contain
        connection information.
    default: ENABLED
  usipserverstraypkt:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable detection of stray server side pkts in USIP mode.
    default: DISABLED
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
