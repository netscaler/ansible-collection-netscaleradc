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
module: authenticationwebauthaction
short_description: Configuration for Web authentication action resource.
description: Configuration for Web authentication action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  attribute1:
    description:
      - Expression that would be evaluated to extract attribute1 from the webauth
        response
    type: str
  attribute10:
    description:
      - Expression that would be evaluated to extract attribute10 from the webauth
        response
    type: str
  attribute11:
    description:
      - Expression that would be evaluated to extract attribute11 from the webauth
        response
    type: str
  attribute12:
    description:
      - Expression that would be evaluated to extract attribute12 from the webauth
        response
    type: str
  attribute13:
    description:
      - Expression that would be evaluated to extract attribute13 from the webauth
        response
    type: str
  attribute14:
    description:
      - Expression that would be evaluated to extract attribute14 from the webauth
        response
    type: str
  attribute15:
    description:
      - Expression that would be evaluated to extract attribute15 from the webauth
        response
    type: str
  attribute16:
    description:
      - Expression that would be evaluated to extract attribute16 from the webauth
        response
    type: str
  attribute2:
    description:
      - Expression that would be evaluated to extract attribute2 from the webauth
        response
    type: str
  attribute3:
    description:
      - Expression that would be evaluated to extract attribute3 from the webauth
        response
    type: str
  attribute4:
    description:
      - Expression that would be evaluated to extract attribute4 from the webauth
        response
    type: str
  attribute5:
    description:
      - Expression that would be evaluated to extract attribute5 from the webauth
        response
    type: str
  attribute6:
    description:
      - Expression that would be evaluated to extract attribute6 from the webauth
        response
    type: str
  attribute7:
    description:
      - Expression that would be evaluated to extract attribute7 from the webauth
        response
    type: str
  attribute8:
    description:
      - Expression that would be evaluated to extract attribute8 from the webauth
        response
    type: str
  attribute9:
    description:
      - Expression that would be evaluated to extract attribute9 from the webauth
        response
    type: str
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  fullreqexpr:
    description:
      - Exact HTTP request, in the form of an expression, which the Citrix ADC sends
        to the authentication server.
      - The Citrix ADC does not check the validity of this request. One must manually
        validate the request.
    type: str
  name:
    description:
      - 'Name for the Web Authentication action. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
    type: str
  scheme:
    description:
      - Type of scheme for the web server.
    type: str
    choices:
      - http
      - https
  serverip:
    description:
      - IP address of the web server to be used for authentication.
    type: str
  serverport:
    description:
      - Port on which the web server accepts connections.
    type: int
  successrule:
    description:
      - Expression, that checks to see if authentication is successful.
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
