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
module: sslpkcs12
short_description: Configuration for pkcs12 resource.
description: Configuration for pkcs12 resource.
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
  Import:
    type: bool
    description:
      - Convert the certificate and private-key from PKCS#12 format to PEM format.
  aes256:
    type: bool
    description:
      - Encrypt the private key by using the AES algorithm (256-bit key) during the
        import operation. On the command line, you are prompted to enter the pass
        phrase.
  certfile:
    type: str
    description:
      - Certificate file to be converted from PEM to PKCS#12 format.
  des:
    type: bool
    description:
      - Encrypt the private key by using the DES algorithm in CBC mode during the
        import operation. On the command line, you are prompted to enter the pass
        phrase.
  des3:
    type: bool
    description:
      - Encrypt the private key by using the Triple-DES algorithm in EDE CBC mode
        (168-bit key) during the import operation. On the command line, you are prompted
        to enter the pass phrase.
  export:
    type: bool
    description:
      - Convert the certificate and private key from PEM format to PKCS#12 format.
        On the command line, you are prompted to enter the pass phrase.
  keyfile:
    type: str
    description:
      - Name of the private key file to be converted from PEM to PKCS#12 format. If
        the key file is encrypted, you are prompted to enter the pass phrase used
        for encrypting the key.
  outfile:
    type: str
    description:
      - Name for and, optionally, path to, the output file that contains the certificate
        and the private key after converting from PKCS#12 to PEM format. /nsconfig/ssl/
        is the default path.
      - If importing, the certificate-key pair is stored in PEM format. If exporting,
        the certificate-key pair is stored in PKCS#12 format.
  password:
    type: str
    description:
      - '0'
  pempassphrase:
    type: str
    description:
      - '0'
  pkcs12file:
    type: str
    description:
      - Name for and, optionally, path to, the PKCS#12 file. If importing, specify
        the input file name that contains the certificate and the private key in PKCS#12
        format. If exporting, specify the output file name that contains the certificate
        and the private key after converting from PEM to
      - PKCS#12 format. /nsconfig/ssl/ is the default path.
      - During the import operation, if the key is encrypted, you are prompted to
        enter the pass phrase used for encrypting the key.
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
