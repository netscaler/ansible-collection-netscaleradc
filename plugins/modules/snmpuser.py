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
module: snmpuser
short_description: Configuration for SNMP user resource.
description: Configuration for SNMP user resource.
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
  authpasswd:
    type: str
    description:
      - Plain-text pass phrase to be used by the authentication algorithm specified
        by the authType (Authentication Type) parameter. Can consist of 1 to 31 characters
        that include uppercase and lowercase letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        (_) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the pass phrase includes one or more spaces, enclose it in double or single
        quotation marks (for example, "my phrase" or 'my phrase').
  authtype:
    type: str
    choices:
      - MD5
      - SHA
    description:
      - Authentication algorithm used by the Citrix ADC and the SNMPv3 user for authenticating
        the communication between them. You must specify the same authentication algorithm
        when you configure the SNMPv3 user in the SNMP manager.
  group:
    type: str
    description:
      - Name of the configured SNMPv3 group to which to bind this SNMPv3 user. The
        access rights (bound SNMPv3 views) and security level set for this group are
        assigned to this user.
  name:
    type: str
    description:
      - Name for the SNMPv3 user. Can consist of 1 to 31 characters that include uppercase
        and lowercase letters, numbers, and the hyphen (-), period (.) pound (#),
        space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my user" or 'my user').
  privpasswd:
    type: str
    description:
      - Encryption key to be used by the encryption algorithm specified by the privType
        (Encryption Type) parameter. Can consist of 1 to 31 characters that include
        uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound
        (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the key includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my key" or 'my key').
  privtype:
    type: str
    choices:
      - DES
      - AES
    description:
      - Encryption algorithm used by the Citrix ADC and the SNMPv3 user for encrypting
        the communication between them. You must specify the same encryption algorithm
        when you configure the SNMPv3 user in the SNMP manager.
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
