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
module: sslcipher_sslciphersuite_binding
short_description: Binding Resource definition for describing association between
  sslcipher and sslciphersuite resources
description: Binding Resource definition for describing association between sslcipher
  and sslciphersuite resources
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
  ciphergroupname:
    type: str
    description:
      - Name of the user-defined cipher group.
  ciphername:
    type: str
    description:
      - Cipher name.
  cipheroperation:
    type: str
    choices:
      - ADD
      - REM
      - ORD
    description:
      - The operation that is performed when adding the cipher-suite.
      - ''
      - 'Possible cipher operations are:'
      - "\tC(ADD) - Appends the given cipher-suite to the existing one configured\
        \ for the virtual server."
      - "\tC(REM) - Removes the given cipher-suite from the existing one configured\
        \ for the virtual server."
      - "\tC(ORD) - Overrides the current configured cipher-suite for the virtual\
        \ server with the given cipher-suite."
  cipherpriority:
    type: float
    description:
      - This indicates priority assigned to the particular cipher
  ciphgrpals:
    type: str
    description:
      - A cipher-suite can consist of an individual cipher name, the system predefined
        cipher-alias name, or user defined cipher-group name.
  description:
    type: str
    description:
      - Cipher suite description.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslcipher_sslciphersuite_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslcipher_sslciphersuite_binding
      delegate_to: localhost
      netscaler.adc.sslcipher_sslciphersuite_binding:

        state: present
        ciphergroupname: ssllabs-blackstone
        ciphername: TLS1.2-DHE-RSA-AES256-GCM-SHA384
        cipherpriority: '14'
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
