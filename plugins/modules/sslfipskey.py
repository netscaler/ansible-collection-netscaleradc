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
module: sslfipskey
short_description: Configuration for FIPS key resource.
description: Configuration for FIPS key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - absent
      - created
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(created), the `create` operation will be applied on the resource.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  curve:
    type: str
    choices:
      - P_256
      - P_384
    description:
      - Only p_256 (prime256v1) and C(P_384) (secp384r1) are supported.
  exponent:
    type: str
    choices:
      - '3'
      - F4
    description:
      - 'Exponent value for the FIPS key to be created. Available values function
        as follows:'
      - ' 3=3 (hexadecimal)'
      - F4=10001 (hexadecimal)
  fipskeyname:
    type: str
    description:
      - Name for the FIPS key. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the FIPS key is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my fipskey" or 'my fipskey').
  inform:
    type: str
    choices:
      - SIM
      - DER
      - PEM
    description:
      - 'Input format of the key file. Available formats are:'
      - C(SIM) - Secure Information Management; select when importing a FIPS key.
        If the external FIPS key is encrypted, first decrypt it, and then import it.
      - C(PEM) - Privacy Enhanced Mail; select when importing a non-FIPS key.
  iv:
    type: str
    description:
      - Initialization Vector (IV) to use for importing the key. Required for importing
        a non-FIPS key.
  key:
    type: str
    description:
      - Name of and, optionally, path to the key file to be imported.
      - ' /nsconfig/ssl/ is the default path.'
  keytype:
    type: str
    choices:
      - RSA
      - ECDSA
    description:
      - Only C(RSA) key and C(ECDSA) Key are supported.
  modulus:
    type: float
    description:
      - Modulus, in multiples of 64, of the FIPS key to be created.
  wrapkeyname:
    type: str
    description:
      - Name of the wrap key to use for importing the key. Required for importing
        a non-FIPS key.
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
