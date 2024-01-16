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
module: nshmackey
short_description: Configuration for HMAC key resource.
description: Configuration for HMAC key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Comments associated with this encryption key.
  digest:
    type: str
    choices:
      - MD2
      - MD4
      - MD5
      - SHA1
      - SHA224
      - SHA256
      - SHA384
      - SHA512
    description:
      - Digest (hash) function to be used in the HMAC computation.
  keyvalue:
    type: str
    description:
      - 'The hex-encoded key to be used in the HMAC computation. The key can be any
        length (up to a Citrix ADC-imposed maximum of 255 bytes). If the length is
        less than the digest block size, it will be zero padded up to the block size.
        If it is greater than the block size, it will be hashed using the digest function
        to the block size. The block size for each digest is:'
      - '   MD2    - 16 bytes'
      - '   MD4    - 16 bytes'
      - '   MD5    - 16 bytes'
      - '   SHA1   - 20 bytes'
      - '   SHA224 - 28 bytes'
      - '   SHA256 - 32 bytes'
      - '   SHA384 - 48 bytes'
      - '   SHA512 - 64 bytes'
      - Note that the key will be encrypted when it it is saved
      - ''
      - There is a special key value AUTO which generates a new random key for the
        specified digest. This kind of key is
      - intended for use cases where the NetScaler both generates and verifies an
        HMAC on  the same data.
  name:
    type: str
    description:
      - 'Key name.  This follows the same syntax rules as other expression entity
        names:'
      - '   It must begin with an alpha character (A-Z or a-z) or an underscore (_).'
      - '   The rest of the characters must be alpha, numeric (0-9) or underscores.'
      - '   It cannot be re or xp (reserved for regular and XPath expressions).'
      - '   It cannot be an expression reserved word (e.g. SYS or HTTP).'
      - '   It cannot be used for an existing expression object (HTTP callout, patset,
        dataset, stringmap, or named expression).'
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
