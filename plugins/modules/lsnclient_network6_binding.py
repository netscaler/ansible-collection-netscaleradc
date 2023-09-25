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
module: lsnclient_network6_binding
short_description: Binding Resource definition for describing association between
  lsnclient and network6 resources
description: Binding Resource definition for describing association between lsnclient
  and network6 resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  clientname:
    description:
      - 'Name for the LSN client entity. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the LSN client is created. The following
        requirement applies only to the Citrix ADC CLI: If the name includes one or
        more spaces, enclose the name in double or single quotation marks (for example,
        "lsn client1" or ''lsn client1'').'
    type: str
  netmask:
    description:
      - Subnet mask for the IPv4 address specified in the Network parameter.
    type: str
  network:
    description:
      - IPv4 address(es) of the LSN subscriber(s) or subscriber network(s) on whose
        traffic you want the Citrix ADC to perform Large Scale NAT.
    type: str
  network6:
    description:
      - IPv6 address(es) of the LSN subscriber(s) or subscriber network(s) on whose
        traffic you want the Citrix ADC to perform Large Scale NAT.
    type: str
  td:
    description:
      - 'ID of the traffic domain on which this subscriber or the subscriber network
        (as specified by the network parameter) belongs. '
      - If you do not specify an ID, the subscriber or the subscriber network becomes
        part of the default traffic domain.
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
