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
module: dnsptrrec
short_description: Configuration for PTR record resource.
description: Configuration for PTR record resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  domain:
    description:
      - Domain name for which to configure reverse mapping.
    type: str
  ecssubnet:
    description:
      - Subnet for which the cached PTR record need to be removed.
    type: str
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: int
  reversedomain:
    description:
      - Reversed domain name representation of the IPv4 or IPv6 address for which
        to create the PTR record. Use the "in-addr.arpa." suffix for IPv4 addresses
        and the "ip6.arpa." suffix for IPv6 addresses.
    type: str
  ttl:
    description:
      - Time to Live (TTL), in seconds, for the record. TTL is the time for which
        the record must be cached by DNS proxies. The specified TTL is applied to
        all the resource records that are of the same record type and belong to the
        specified domain name. For example, if you add an address record, with a TTL
        of 36000, to the domain name example.com, the TTLs of all the address records
        of example.com are changed to 36000. If the TTL is not specified, the Citrix
        ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available
        on the appliance, the default value of 3600.
    type: int
    default: 3600
  type:
    description:
      - 'Type of records to display. Available settings function as follows:'
      - '* ADNS - Display all authoritative address records.'
      - '* PROXY - Display all proxy address records.'
      - '* ALL - Display all address records.'
    type: str
    choices:
      - ALL
      - ADNS
      - PROXY
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
