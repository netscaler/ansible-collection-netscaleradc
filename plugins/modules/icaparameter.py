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
module: icaparameter
short_description: Configuration for Config Parameters for NS ICA resource.
description: Configuration for Config Parameters for NS ICA resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  edtpmtuddf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable DF enforcement for EDT PMTUD Control Blocks
    default: ENABLED
  edtpmtuddftimeout:
    type: float
    description:
      - DF enforcement timeout for EDTPMTUDDF
    default: 100
  enablesronhafailover:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable/Disable Session Reliability on HA failover. The default value is No
    default: 'NO'
  hdxinsightnonnsap:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable/Disable HDXInsight for Non NSAP ICA Sessions. The default value is
        Yes
    default: 'YES'
  l7latencyfrequency:
    type: float
    description:
      - Specify the time interval/period for which L7 Client Latency value is to be
        calculated. By default, L7 Client Latency is calculated for every packet.
        The default value is 0
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
