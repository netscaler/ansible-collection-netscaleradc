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
module: vxlan
short_description: Configuration for "VXLAN" resource.
description: Configuration for "VXLAN" resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  dynamicrouting:
    description:
      - Enable dynamic routing on this VXLAN.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  id:
    description:
      - A positive integer, which is also called VXLAN Network Identifier (VNI), that
        uniquely identifies a VXLAN.
    type: int
  innervlantagging:
    description:
      - Specifies whether Citrix ADC should generate VXLAN packets with inner VLAN
        tag.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ipv6dynamicrouting:
    description:
      - 'Enable all IPv6 dynamic routing protocols on this VXLAN. Note: For the ENABLED
        setting to work, you must configure IPv6 dynamic routing protocols from the
        VTYSH command line.'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  port:
    description:
      - Specifies UDP destination port for VXLAN packets.
    type: int
    default: 4789
  protocol:
    description:
      - VXLAN-GPE next protocol. RESERVED, IPv4, IPv6, ETHERNET, NSH
    type: str
    default: ETHERNET
    choices:
      - IPv4
      - IPv6
      - ETHERNET
      - NSH
  type:
    description:
      - VXLAN encapsulation type. VXLAN, VXLANGPE
    type: str
    default: VXLAN
    choices:
      - VXLAN
      - VXLANGPE
  vlan:
    description:
      - ID of VLANs whose traffic is allowed over this VXLAN. If you do not specify
        any VLAN IDs, the Citrix ADC allows traffic of all VLANs that are not part
        of any other VXLANs.
    type: int
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
