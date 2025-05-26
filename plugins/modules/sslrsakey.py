#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: sslrsakey
short_description: Configuration for RSA key resource.
description: Configuration for RSA key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - created
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(created), the `create` operation will be applied on the resource.
    type: str
  aes256:
    type: bool
    description:
      - Encrypt the generated RSA key by using the AES algorithm.
  bits:
    type: float
    description:
      - Size, in bits, of the RSA key.
  des:
    type: bool
    description:
      - Encrypt the generated RSA key by using the DES algorithm. On the command line,
        you are prompted to enter the pass phrase (password) that is used to encrypt
        the key.
  des3:
    type: bool
    description:
      - Encrypt the generated RSA key by using the Triple-DES algorithm. On the command
        line, you are prompted to enter the pass phrase (password) that is used to
        encrypt the key.
  exponent:
    type: str
    choices:
      - '3'
      - F4
    description:
      - Public exponent for the RSA key. The exponent is part of the cipher algorithm
        and is required for creating the RSA key.
  keyfile:
    type: str
    description:
      - Name for and, optionally, path to the RSA key file. /nsconfig/ssl/ is the
        default path.
  keyform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format in which the RSA key file is stored on the appliance.
  password:
    type: str
    description:
      - Pass phrase to use for encryption if DES or DES3 option is selected.
  pkcs8:
    type: bool
    description:
      - Create the private key in PKCS#8 format.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslrsakey playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslrsakey
      delegate_to: localhost
      netscaler.adc.sslrsakey:
        state: present
        keyfile: ssl_rsa_der_key
        bits: '2048'
        exponent: '3'
        keyform: DER
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
