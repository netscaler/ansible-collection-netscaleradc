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
module: sslecdsakey
short_description: Configuration for ecdsa key resource.
description: Configuration for ecdsa key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aes256:
    description:
      - Encrypt the generated ECDSA key by using the AES algorithm.
    type: bool
  curve:
    choices:
      - P_256
      - P_384
    description:
      - Curve id to generate ECDSA key. Only C(P_256) and C(P_384) are supported
    type: str
    default: FIPSEXP_F4
  des:
    description:
      - Encrypt the generated ECDSA key by using the DES algorithm. On the command
        line, you are prompted to enter the pass phrase (password) that is used to
        encrypt the key.
    type: bool
  des3:
    description:
      - Encrypt the generated ECDSA key by using the Triple-DES algorithm. On the
        command line, you are prompted to enter the pass phrase (password) that is
        used to encrypt the key.
    type: bool
  keyfile:
    description:
      - Name for and, optionally, path to the ECDSA key file. /nsconfig/ssl/ is the
        default path.
    type: str
  keyform:
    choices:
      - DER
      - PEM
    description:
      - Format in which the ECDSA key file is stored on the appliance.
    type: str
    default: PEM
  password:
    description:
      - Pass phrase to use for encryption if DES or DES3 option is selected.
    type: str
  pkcs8:
    description:
      - Create the private key in PKCS#8 format.
    type: bool
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
