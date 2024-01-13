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
module: sslhsmkey
short_description: Configuration for HSM key resource.
description: Configuration for HSM key resource.
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
  hsmkeyname:
    type: str
    description:
      - '0'
  hsmtype:
    type: str
    choices:
      - THALES
      - SAFENET
      - KEYVAULT
    description:
      - Type of HSM.
  key:
    type: str
    description:
      - Name of the key. optionally, for Thales, path to the HSM key file; /var/opt/nfast/kmdata/local/
        is the default path. Applies when HSMTYPE is THALES or KEYVAULT.
  keystore:
    type: str
    description:
      - Name of keystore object representing HSM where key is stored. For example,
        name of keyvault object or azurekeyvault authentication object. Applies only
        to KEYVAULT type HSM.
  password:
    type: str
    description:
      - Password for a partition. Applies only to SafeNet HSM.
  serialnum:
    type: str
    description:
      - Serial number of the partition on which the key is present. Applies only to
        SafeNet HSM.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
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
