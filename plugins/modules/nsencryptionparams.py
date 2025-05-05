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
---
module: nsencryptionparams
short_description: Configuration for default encryption parameters resource.
description: Configuration for default encryption parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  keyvalue:
    type: str
    description:
      - The base64-encoded key generation number, method, and key value.
      - 'Note:'
      - '* Do not include this argument if you are changing the encryption method.'
      - '* To generate a new key value for the current encryption method, specify
        an empty string \(""\) as the value of this parameter. The parameter is passed
        implicitly, with its automatically generated value, to the Citrix ADC packet
        engines even when it is not included in the command. Passing the parameter
        to the packet engines enables the appliance to save the key value to the configuration
        file and to propagate the key value to the secondary appliance in a high availability
        setup.'
  method:
    type: str
    choices:
      - NONE
      - RC4
      - DES3
      - AES128
      - AES192
      - AES256
      - DES
      - DES-CBC
      - DES-CFB
      - DES-OFB
      - DES-ECB
      - DES3-CBC
      - DES3-CFB
      - DES3-OFB
      - DES3-ECB
      - AES128-CBC
      - AES128-CFB
      - AES128-OFB
      - AES128-ECB
      - AES192-CBC
      - AES192-CFB
      - AES192-OFB
      - AES192-ECB
      - AES256-CBC
      - AES256-CFB
      - AES256-OFB
      - AES256-ECB
    description:
      - Cipher method (and key length) to be used to encrypt and decrypt content.
        The default value is C(AES256).
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsencryptionparams playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nsencryptionparams
      delegate_to: localhost
      netscaler.adc.nsencryptionparams:
        state: present
        method: AES256
        keyvalue: REQ_PASSWORD
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
