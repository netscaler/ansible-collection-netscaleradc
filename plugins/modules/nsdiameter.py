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
module: nsdiameter
short_description: Configuration for Diameter Parameters resource.
description: Configuration for Diameter Parameters resource.
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
  identity:
    type: str
    description:
      - DiameterIdentity to be used by NS. DiameterIdentity is used to identify a
        Diameter node uniquely. Before setting up diameter configuration, Citrix ADC
        (as a Diameter node) MUST be assigned a unique DiameterIdentity.
      - example =>
      - set ns diameter -identity netscaler.com
      - Now whenever Citrix ADC needs to use identity in diameter messages. It will
        use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
  ownernode:
    type: float
    description:
      - ID of the cluster node for which the diameter id is set, can be configured
        only through CLIP
    default: -1
  realm:
    type: str
    description:
      - Diameter Realm to be used by NS.
      - example =>
      - set ns diameter -realm com
      - Now whenever Citrix ADC system needs to use realm in diameter messages. It
        will use 'com' as Origin-Realm AVP as defined in RFC3588
  serverclosepropagation:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - when a Server connection goes down, whether to close the corresponding client
        connection if there were requests pending on the server.
    default: 'NO'
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
