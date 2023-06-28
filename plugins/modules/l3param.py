#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

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
  acllogtime:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to tune acl logging time
    type: int
    default: 5000
  allowclasseipv4:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv4 Class E address clients
    type: str
    default: DISABLED
  dropdfflag:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping the IP DF flag.
    type: str
    default: DISABLED
  dropipfragments:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dropping of IP fragments.
    type: str
    default: DISABLED
  dynamicrouting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable Dynamic routing on partition. This configuration is not applicable
        to default partition
    type: str
    default: DISABLED
  externalloopback:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable external loopback.
    type: str
    default: DISABLED
  forwardicmpfragments:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable forwarding of ICMP fragments.
    type: str
    default: DISABLED
  icmpgenratethreshold:
    description:
      - NS generated ICMP pkts per 10ms rate threshold
    type: int
    default: 100
  implicitaclallow:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Do not apply ACLs for internal ports
    type: str
    default: ENABLED
  ipv6dynamicrouting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable IPv6 Dynamic routing
    type: str
    default: DISABLED
  miproundrobin:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable round robin usage of mapped IPs.
    type: str
    default: ENABLED
  overridernat:
    choices:
      - ENABLED
      - DISABLED
    description:
      - USNIP/USIP settings override RNAT settings for configured
      - '              service/virtual server traffic..'
    type: str
    default: DISABLED
  srcnat:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform NAT if only the source is in the private network
    type: str
    default: ENABLED
  tnlpmtuwoconn:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable learning PMTU of IP tunnel when ICMP error does not contain
        connection information.
    type: str
    default: ENABLED
  usipserverstraypkt:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable detection of stray server side pkts in USIP mode.
    type: str
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
