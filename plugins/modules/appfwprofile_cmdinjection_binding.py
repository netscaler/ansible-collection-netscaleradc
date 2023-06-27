#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: appfwprofile_cmdinjection_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and cmdinjection resources
description: Binding Resource definition for describing association between appfwprofile
  and cmdinjection resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  alertonly:
    choices:
      - true
      - false
    description:
      - Send SNMP alert?
    type: str
  as_scan_location_cmd:
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
    description:
      - Location of command injection exception - form field, header or cookie.
    type: str
  as_value_expr_cmd:
    description:
      - The web form/header/cookie value expression.
    type: str
  as_value_type_cmd:
    choices:
      - Keyword
      - SpecialString
    description:
      - Type of the relaxed web form value
    type: str
  cmdinjection:
    description:
      - Name of the relaxed web form field/header/cookie
    type: str
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  formactionurl_cmd:
    description:
      - The web form action URL.
    type: str
  isautodeployed:
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
    description:
      - Is the rule auto deployed by dynamic profile ?
    type: str
  isregex_cmd:
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the relaxed web form field name/header/cookie a regular expression?
    type: str
  isvalueregex_cmd:
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is the web form field/header/cookie value a regular expression?
    type: str
  name:
    description:
      - Name of the profile to which to bind an exemption or rule.
    type: str
  resourceid:
    description:
      - A "id" that identifies the rule.
    type: str
  ruletype:
    choices:
      - ALLOW
      - DENY
    description:
      - Specifies rule type of binding
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enabled.
    type: str
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
