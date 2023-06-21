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
module: appfwconfidfield
short_description: Configuration for configured confidential form fields resource.
description: Configuration for configured confidential form fields resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about the form field designation.
    type: str
  fieldname:
    description:
      - Name of the form field to designate as confidential.
    type: str
  isregex:
    description:
      - 'Method of specifying the form field name. Available settings function as
        follows:'
      - '* REGEX. Form field is a regular expression.'
      - '* NOTREGEX. Form field is a literal string.'
    type: str
    default: NOTREGEX
    choices:
      - REGEX
      - NOTREGEX
  state:
    description:
      - Enable or disable the confidential field designation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  url:
    description:
      - URL of the web page that contains the web form.
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
