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
module: authenticationcertaction
short_description: Configuration for CERT action resource.
description: Configuration for CERT action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  groupnamefield:
    description:
      - Client-cert field from which the group is extracted.  Must be set to either
        ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
      - 'Format: <field>:<subfield>'
    type: str
  name:
    description:
      - 'Name for the client cert authentication server profile (action). '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after certifcate action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
    type: str
  twofactor:
    description:
      - 'Enables or disables two-factor authentication. '
      - Two factor authentication is client cert authentication followed by password
        authentication.
    type: str
    choices:
      - true
      - false
  usernamefield:
    description:
      - Client-cert field from which the username is extracted. Must be set to either
        ""Subject"" and ""Issuer"" (include both sets of double quotation marks).
      - 'Format: <field>:<subfield>.'
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
