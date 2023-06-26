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
module: icaparameter
short_description: Configuration for Config Parameters for NS ICA resource.
description: Configuration for Config Parameters for NS ICA resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  edtpmtuddf:
    description:
      - Enable/Disable DF enforcement for EDT PMTUD Control Blocks
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  edtpmtuddftimeout:
    description:
      - DF enforcement timeout for EDTPMTUDDF
    type: int
    default: 100
  enablesronhafailover:
    description:
      - Enable/Disable Session Reliability on HA failover. The default value is No
    type: str
    choices:
      - true
      - false
  hdxinsightnonnsap:
    description:
      - Enable/Disable HDXInsight for Non NSAP ICA Sessions. The default value is
        Yes
    type: str
    default: true
    choices:
      - true
      - false
  l7latencyfrequency:
    description:
      - Specify the time interval/period for which L7 Client Latency value is to be
        calculated. By default, L7 Client Latency is calculated for every packet.
        The default value is 0
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