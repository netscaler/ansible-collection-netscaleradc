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
module: snmpmanager
short_description: Configuration for manager resource.
description: Configuration for manager resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  domainresolveretry:
    description:
      - Amount of time, in seconds, for which the Citrix ADC waits before sending
        another DNS query to resolve the host name of the SNMP manager if the last
        query failed. This parameter is valid for host-name based SNMP managers only.
        After a query succeeds, the TTL determines the wait time. The minimum and
        default value is 5.
    type: int
  ipaddress:
    description:
      - 'IP address of the SNMP manager. Can be an IPv4 or IPv6 address. You can instead
        specify an IPv4 network address or IPv6 network prefix if you want the Citrix
        ADC to respond to SNMP queries from any device on the specified network. Alternatively,
        instead of an IPv4 address, you can specify a host name that has been assigned
        to an SNMP manager. If you do so, you must add a DNS name server that resolves
        the host name of the SNMP manager to its IP address. '
      - 'Note: The Citrix ADC does not support host names for SNMP managers that have
        IPv6 addresses.'
    type: str
  netmask:
    description:
      - Subnet mask associated with an IPv4 network address. If the IP address specifies
        the address or host name of a specific host, accept the default value of 255.255.255.255.
    type: str
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
