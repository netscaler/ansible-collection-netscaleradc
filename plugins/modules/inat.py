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
module: inat
short_description: Configuration for inbound nat resource.
description: Configuration for inbound nat resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  connfailover:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Synchronize connection information with the secondary appliance in a high
        availability (HA) pair. That is, synchronize all connection-related information
        for the INAT session
    type: str
    default: DISABLED
  ftp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the FTP protocol on the server for transferring files between the client
        and the server.
    type: str
    default: DISABLED
  mode:
    choices:
      - STATELESS
    description:
      - Stateless translation.
    type: str
  name:
    description:
      - 'Name for the Inbound NAT (INAT) entry. Leading character must be a number
        or letter. Other characters allowed, after the first character, are @ _ -
        . (period) : (colon) # and space ( ).'
    type: str
  privateip:
    description:
      - IP address of the server to which the packet is sent by the Citrix ADC. Can
        be an IPv4 or IPv6 address.
    type: str
  proxyip:
    description:
      - Unique IP address used as the source IP address in packets sent to the server.
        Must be a MIP or SNIP address.
    type: str
  publicip:
    description:
      - Public IP address of packets received on the Citrix ADC. Can be aNetScaler-owned
        VIP or VIP6 address.
    type: str
  tcpproxy:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable TCP proxy, which enables the Citrix ADC to optimize the RNAT TCP traffic
        by using Layer 4 features.
    type: str
    default: DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  tftp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - To enable/disable TFTP (Default C(DISABLED)).
    type: str
    default: DISABLED
  useproxyport:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable the Citrix ADC to proxy the source port of packets before sending the
        packets to the server.
    type: str
    default: ENABLED
  usip:
    choices:
      - true
      - false
    description:
      - Enable the Citrix ADC to retain the source IP address of packets before sending
        the packets to the server.
    type: str
  usnip:
    choices:
      - true
      - false
    description:
      - Enable the Citrix ADC to use a SNIP address as the source IP address of packets
        before sending the packets to the server.
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
