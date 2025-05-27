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
module: appfwprofile_xmlwsiurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and xmlwsiurl resources
description: Binding Resource definition for describing association between appfwprofile
  and xmlwsiurl resources
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
  comment:
    type: str
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
  isautodeployed:
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
    description:
      - Is the rule auto deployed by dynamic profile ?
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
  xmlwsichecks:
    type: str
    description:
      - Specify a comma separated list of relevant WS-I rule IDs. (R1140, R1141)
  xmlwsiurl:
    type: str
    description:
      - XML WS-I URL regular expression length.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appfwprofile_xmlwsiurl_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwprofile_xmlwsiurl_binding
      delegate_to: localhost
      netscaler.adc.appfwprofile_xmlwsiurl_binding:
        state: present
        name: webgoat_prof
        xmlwsiurl: .*
        xmlwsichecks: BP1201, R1000, R1001, R1003, R1004, R1005, R1006, R1007, R1011,
          R1012, R1013, R1014, R1015, R1031, R1032, R1033, R1109, R1111, R1126, R1132,
          R1140, R1141, R2113, R2211, R2714, R2729, R2735, R2738, R2740, R2744
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
