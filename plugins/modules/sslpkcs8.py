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
module: sslpkcs8
short_description: Configuration for pkcs8 resource.
description: Configuration for pkcs8 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
  keyfile:
    type: str
    description:
      - Name of and, optionally, path to the input key file to be converted from PEM
        or DER format to PKCS#8 format. /nsconfig/ssl/ is the default path.
  keyform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format in which the key file is stored on the appliance.
  password:
    type: str
    description:
      - Password to assign to the file if the key is encrypted. Applies only for PEM
        format files.
  pkcs8file:
    type: str
    description:
      - Name for and, optionally, path to, the output file where the PKCS#8 format
        key file is stored. /nsconfig/ssl/ is the default path.
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
