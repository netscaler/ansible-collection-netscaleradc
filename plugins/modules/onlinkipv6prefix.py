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
module: onlinkipv6prefix
short_description: Configuration for on-link IPv6 global prefixes for Router Advertisment
  resource.
description: Configuration for on-link IPv6 global prefixes for Router Advertisment
  resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  autonomusprefix:
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix Autonomus flag.
    type: str
    default: 'YES'
  decrementprefixlifetimes:
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix Autonomus flag.
    type: str
    default: 'NO'
  depricateprefix:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Depricate the prefix.
    type: str
    default: 'NO'
  ipv6prefix:
    description:
      - Onlink prefixes for RA messages.
    type: str
  onlinkprefix:
    choices:
      - 'YES'
      - 'NO'
    description:
      - RA Prefix onlink flag.
    type: str
    default: 'YES'
  prefixpreferredlifetime:
    description:
      - Preferred life time of the prefix, in seconds.
    type: float
    default: 604800
  prefixvalidelifetime:
    description:
      - Valide life time of the prefix, in seconds.
    type: float
    default: 2592000
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
