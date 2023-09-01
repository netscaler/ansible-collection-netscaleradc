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
module: nslicenseserver
short_description: Configuration for licenseserver resource.
description: Configuration for licenseserver resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  forceupdateip:
    description:
      - If this flag is used while adding the licenseserver, existing config will
        be overwritten. Use this flag only if you are sure that the new licenseserver
        has the required capacity.
    type: bool
  licensemode:
    choices:
      - Pooled
      - VCPU
      - CICO
      - SelfManagedPool
      - SelfManagedvCPU
    description:
      - This paramter indicates type of license customer interested while configuring
        add/set licenseserver
    type: str
  licenseserverip:
    description:
      - IP address of the License server.
    type: str
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: float
  port:
    description:
      - License server port.
    type: float
  servername:
    description:
      - Fully qualified domain name of the License server.
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
