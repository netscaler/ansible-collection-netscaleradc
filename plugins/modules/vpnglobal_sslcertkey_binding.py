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
module: vpnglobal_sslcertkey_binding
short_description: Binding Resource definition for describing association between
  vpnglobal and sslcertkey resources
description: Binding Resource definition for describing association between vpnglobal
  and sslcertkey resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  cacert:
    type: str
    description:
      - The name of the CA certificate binding.
  certkeyname:
    type: str
    description:
      - SSL certkey to use in signing tokens. Only RSA cert key is allowed
  crlcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the CRL check parameter (C(Mandatory)/C(Optional)).
  gotopriorityexpression:
    type: str
    description:
      - Applicable only to advance vpn session policy. An expression or other value
        specifying the priority of the next policy which will get evaluated if the
        current policy rule evaluates to TRUE.
  ocspcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the OCSP check parameter (C(Mandatory)/C(Optional)).
  userdataencryptionkey:
    type: str
    description:
      - Certificate to be used for encrypting user data like KB Question and Answers,
        Alternate Email Address, etc.
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
