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
module: nsencryptionkey
short_description: Configuration for encryption key resource.
description: Configuration for encryption key resource.
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
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Comments associated with this encryption key.
  iv:
    type: str
    description:
      - 'The initalization voector (IV) for a block cipher, one block of data used
        to initialize the encryption. The best practice is to not specify an IV, in
        which case a new random IV will be generated for each encryption. The format
        must be iv_data or keyid_iv_data to include the generated IV in the encrypted
        data. The IV should only be specified if it cannot be included in the encrypted
        data. The IV length is the cipher block size:'
      - '   RC4    - not used (error if IV is specified)'
      - '   DES    -  8 bytes (all modes)'
      - '   DES3   -  8 bytes (all modes)'
      - '   AES128 - 16 bytes (all modes)'
      - '   AES192 - 16 bytes (all modes)'
      - '   AES256 - 16 bytes (all modes)'
  keyvalue:
    type: str
    description:
      - 'The hex-encoded key value. The length is determined by the cipher method:'
      - '   RC4    - 16 bytes'
      - '   DES    -  8 bytes (all modes)'
      - '   DES3   - 24 bytes (all modes)'
      - '   AES128 - 16 bytes (all modes)'
      - '   AES192 - 24 bytes (all modes)'
      - '   AES256 - 32 bytes (all modes)'
      - Note that the keyValue will be encrypted when it it is saved.
      - ''
      - There is a special key value AUTO which generates a new random key for the
        specified method. This kind of key is
      - intended for use cases where the NetScaler both encrypts and decrypts the
        same data, such an HTTP header.
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
      - Cipher method to be used to encrypt and decrypt content.
      - '   C(NONE) - no encryption or decryption is performed The output of ENCRYPT()
        and DECRYPT() is the same as the input.'
      - '   C(RC4)  - the C(RC4) stream cipher with a 128 bit (16 byte) key; C(RC4)
        is now considered insecure and should only be used if required by existing
        applciations.'
      - '   C(DES)[-<mode>] - the Data Encryption Standard (C(DES)) block cipher with
        a 64-bit (8 byte) key, with 56 data bits and 8 parity bits. C(DES) is considered
        less secure than C(DES3) or AES so it should only be used if required by an
        existing applicastion. The optional mode is described below; C(DES) without
        a mode is equivalent to C(DES)-CBC.'
      - '   C(DES3)[-<mode>] - the Triple Data Encryption Standard (C(DES)) block
        cipher with a 192-bit (24 byte) key. The optional mode is described below;
        C(DES3) without a mode is equivalent to C(DES3)-CBC.'
      - '   AES<keysize>[-<mode>] - the Advanced Encryption Standard block cipher,
        available with 128 bit (16 byte), 192 bit (24 byte), and 256 bit (32 byte)
        keys. The optional mode is described below; AES<keysize> without a mode is
        equivalent to AES<keysize>-CBC.'
      - ''
      - For a block cipher, the <mode> specifies how multiple blocks of plaintext
        are encrypted and how the Initialization Vector (IV) is used. Choices are
      - '   CBC (Cipher Block Chaining) - Each block of plaintext is XORed with the
        previous ciphertext block, or IV for the first block, before being encrypted.
        Padding is required if the plaintext is not a multiple of the cipher block
        size.'
      - '   CFB (Cipher Feedback) - The previous ciphertext block, or the IV for the
        first block, is encrypted and the output is XORed with the current plaintext
        block to create the current ciphertext block. The 128-bit version of CFB is
        provided. Padding is not required.'
      - '   OFB (Output Feedback) - A keystream is generated by applying the cipher
        successfully to the IV and XORing the keystream blocks with the plaintext.
        Padding is not required.'
      - '   ECB (Electronic Codebook) - Each block of plaintext is independently encrypted.
        An IV is not used. Padding is required. This mode is considered less secure
        than the other modes because the same plaintext always produces the same encrypted
        text and should only be used if required by an existing application.'
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
  padding:
    type: str
    choices:
      - 'OFF'
      - 'ON'
    description:
      - 'Enables or disables the padding of plaintext to meet the block size requirements
        of block ciphers:'
      - '   C(ON) - For encryption, PKCS5/7 padding is used, which appends n bytes
        of value n on the end of the plaintext to bring it to the cipher block lnegth.
        If the plaintext length is alraady a multiple of the block length, an additional
        block with bytes of value block_length will be added. For decryption, ISO
        10126 padding is accepted, which expects the last byte of the block to be
        the number of added pad bytes. Note that this accepts PKCS5/7 padding, as
        well as ANSI_X923 padding. Padding C(ON) is the default for the ECB and CBD
        modes.'
      - '   C(OFF) - No padding. An Undef error will occur with the ECB or CBC modes
        if the plaintext length is not a multitple of the cipher block size. This
        can be used with the CFB and OFB modes, and with the ECB and CBC modes if
        the plaintext will always be an integral number of blocks, or if custom padding
        is implemented using a policy extension function. Padding OFf is the default
        for CFB and OFB modes.'
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
