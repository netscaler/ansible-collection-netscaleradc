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
module: vpnnexthopserver
short_description: Configuration for Next Hop Server resource.
description: Configuration for Next Hop Server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - Name for the Citrix Gateway appliance in the first DMZ.
    type: str
  nexthopfqdn:
    description:
      - FQDN of the Citrix Gateway proxy in the second DMZ.
    type: str
  nexthopip:
    description:
      - IP address of the Citrix Gateway proxy in the second DMZ.
    type: str
  nexthopport:
    description:
      - Port number of the Citrix Gateway proxy in the second DMZ.
    type: int
  resaddresstype:
    description:
      - Address Type (IPV4/IPv6) of DNS name of nextHopServer FQDN.
    type: str
    choices:
      - IPV4
      - IPV6
  secure:
    description:
      - Use of a secure port, such as 443, for the double-hop configuration.
    type: str
    choices:
      - true
      - false
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
