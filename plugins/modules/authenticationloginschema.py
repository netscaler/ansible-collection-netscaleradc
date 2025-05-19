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
module: authenticationloginschema
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
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
  authenticationschema:
    type: str
    description:
      - Name of the file for reading authentication schema to be sent for Login Page
        UI. This file should contain xml definition of elements as per Citrix Forms
        Authentication Protocol to be able to render login form. If administrator
        does not want to prompt users for additional credentials but continue with
        previously obtained credentials, then "noschema" can be given as argument.
        Please note that this applies only to loginSchemas that are used with user-defined
        factors, and not the vserver factor.
  authenticationstrength:
    type: int
    description:
      - Weight of the current authentication
  name:
    type: str
    description:
      - Name for the new login schema. Login schema defines the way login form is
        rendered. It provides a way to customize the fields that are shown to the
        user. Must begin with an ASCII alphanumeric or underscore (_) character, and
        must contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed
        after an action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  passwdexpression:
    type: str
    description:
      - Expression for password extraction during login. This can be any relevant
        advanced policy expression.
  passwordcredentialindex:
    type: int
    description:
      - The index at which user entered password should be stored in session.
  ssocredentials:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option indicates whether current factor credentials are the default SSO
        (SingleSignOn) credentials.
  usercredentialindex:
    type: int
    description:
      - The index at which user entered username should be stored in session.
  userexpression:
    type: str
    description:
      - Expression for username extraction during login. This can be any relevant
        advanced policy expression.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample authenticationloginschema playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure authenticationloginschema
      delegate_to: localhost
      netscaler.adc.authenticationloginschema:
        state: present
        name: single_auth
        authenticationschema: /nsconfig/loginschema/LoginSchema/SingleAuth.xml
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
