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
module: appfwprofile_cmdinjection_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and cmdinjection resources
description: Binding Resource definition for describing association between appfwprofile
  and cmdinjection resources
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  alertonly:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send SNMP alert?
  as_scan_location_cmd:
    type: str
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
    description:
      - Location of command injection exception - form field, header or cookie.
  as_value_expr_cmd:
    type: str
    description:
      - The web form/header/cookie value expression.
  as_value_type_cmd:
    type: str
    choices:
      - Keyword
      - SpecialString
    description:
      - Type of the relaxed web form value
  cmdinjection:
    type: str
    description:
      - Name of the relaxed web form field/header/cookie
  comment:
    type: str
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
  formactionurl_cmd:
    type: str
    description:
      - The web form action URL.
  isautodeployed:
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
    description:
      - Is the rule auto deployed by dynamic profile ?
  isregex_cmd:
    type: str
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the relaxed web form field name/header/cookie a regular expression?
  isvalueregex_cmd:
    type: str
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the web form field/header/cookie value a regular expression?
  name:
    type: str
    description:
      - Name of the profile to which to bind an exemption or rule.
  resourceid:
    type: str
    description:
      - A "id" that identifies the rule.
  ruletype:
    type: str
    choices:
      - ALLOW
      - DENY
    description:
      - Specifies rule type of binding
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
