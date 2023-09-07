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
module: iptunnel
short_description: Configuration for ip Tunnel resource.
description: Configuration for ip Tunnel resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  destport:
    description:
      - Specifies UDP destination port for Geneve packets. Default port is 6081.
    type: int
    default: 6081
  grepayload:
    choices:
      - ETHERNETwithDOT1Q
      - ETHERNET
      - IP
    description:
      - The payload GRE will carry
    type: str
    default: ETHERNETwithDOT1Q
  ipsecprofilename:
    description:
      - Name of IPSec profile to be associated.
    type: str
    default: '"ns_ipsec_default_profile"'
  local:
    description:
      - Type of Citrix ADC owned public IPv4 address, configured on the local Citrix
        ADC and used to set up the tunnel.
    type: str
  name:
    description:
      - 'Name for the IP tunnel. Leading character must be a number or letter. Other
        characters allowed, after the first character, are @ _ - . (period) : (colon)
        # and space ( ).'
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for the iptunnel.
    type: str
    default: DEFAULT_NG
  protocol:
    choices:
      - IPIP
      - GRE
      - IPSEC
      - UDP
      - GENEVE
    description:
      - Name of the protocol to be used on this tunnel.
    type: str
    default: IPIP
  remote:
    description:
      - Public IPv4 address, of the remote device, used to set up the tunnel. For
        this parameter, you can alternatively specify a network address.
    type: str
  remotesubnetmask:
    description:
      - Subnet mask of the remote IP address of the tunnel.
    type: str
  tosinherit:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Default behavior is to copy the ToS field of the internal IP Packet (Payload)
        to the outer IP packet (Transport packet). But the user can configure a new
        ToS field using this option.
    type: str
    default: ENABLED
  vlan:
    description:
      - The vlan for mulicast packets
    type: float
  vlantagging:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to select Vlan Tagging.
    type: str
    default: DISABLED
  vnid:
    description:
      - Virtual network identifier (VNID) is the value that identifies a specific
        virtual network in the data plane.
    type: float
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
