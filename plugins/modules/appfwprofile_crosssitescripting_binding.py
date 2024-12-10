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
module: appfwprofile_crosssitescripting_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and crosssitescripting resources
description: Binding Resource definition for describing association between appfwprofile
  and crosssitescripting resources
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
  alertonly:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send SNMP alert?
  as_scan_location_xss:
    type: str
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
      - URL
    description:
      - Location of cross-site scripting exception - form field, header, cookie or
        C(URL).
  as_value_expr_xss:
    type: str
    description:
      - The web form value expression.
  as_value_type_xss:
    type: str
    choices:
      - Tag
      - Attribute
      - Pattern
    description:
      - The web form value type.
  comment:
    type: str
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
  crosssitescripting:
    type: str
    description:
      - The web form field name.
  formactionurl_xss:
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
  isregex_xss:
    type: str
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the web form field name a regular expression?
  isvalueregex_xss:
    type: str
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the web form field value a regular expression?
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
---
- name: Sample appfwprofile_crosssitescripting_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwprofile_crosssitescripting_binding
      delegate_to: localhost
      netscaler.adc.appfwprofile_crosssitescripting_binding:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: Test_profile
        crosssitescripting: text_area
        formactionurl_xss: ^http://test.net/forms/login.php$
        as_scan_location_xss: FORMFIELD
        as_value_type_xss: Pattern
        as_value_expr_xss: onblur
        isvalueregex_xss: NOTREGEX
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
