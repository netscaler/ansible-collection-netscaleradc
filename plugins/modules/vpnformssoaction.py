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
module: vpnformssoaction
short_description: Configuration for Form sso action resource.
description: Configuration for Form sso action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  actionurl:
    description:
      - Root-relative URL to which the completed form is submitted.
    type: str
  name:
    description:
      - Name for the form based single sign-on profile.
    type: str
  namevaluepair:
    description:
      - Other name-value pair attributes to send to the server, in addition to sending
        the user name and password. Value names are separated by an ampersand (&),
        such as in name1=value1&name2=value2.
    type: str
  nvtype:
    choices:
      - STATIC
      - DYNAMIC
    description:
      - 'How to process the name-value pair. Available settings function as follows:'
      - '* C(STATIC) - The administrator-configured values are used.'
      - '* C(DYNAMIC) - The response is parsed, the form is extracted, and then submitted.'
    type: str
    default: DYNAMIC
  passwdfield:
    description:
      - Name of the form field in which the user types in the password.
    type: str
  responsesize:
    description:
      - Maximum number of bytes to allow in the response size. Specifies the number
        of bytes in the response to be parsed for extracting the forms.
    type: int
    default: 8096
  ssosuccessrule:
    description:
      - Expression that defines the criteria for SSO success. Expression such as checking
        for cookie in the response is a common example.
    type: str
  submitmethod:
    choices:
      - GET
      - POST
    description:
      - HTTP method (C(GET) or C(POST)) used by the single sign-on form to send the
        logon credentials to the logon server.
    type: str
    default: GET
  userfield:
    description:
      - Name of the form field in which the user types in the user ID.
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
