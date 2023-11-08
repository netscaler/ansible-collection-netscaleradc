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
module: authenticationwebauthaction
short_description: Configuration for Web authentication action resource.
description: Configuration for Web authentication action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  attribute1:
    type: str
    description:
      - Expression that would be evaluated to extract attribute1 from the webauth
        response
  attribute10:
    type: str
    description:
      - Expression that would be evaluated to extract attribute10 from the webauth
        response
  attribute11:
    type: str
    description:
      - Expression that would be evaluated to extract attribute11 from the webauth
        response
  attribute12:
    type: str
    description:
      - Expression that would be evaluated to extract attribute12 from the webauth
        response
  attribute13:
    type: str
    description:
      - Expression that would be evaluated to extract attribute13 from the webauth
        response
  attribute14:
    type: str
    description:
      - Expression that would be evaluated to extract attribute14 from the webauth
        response
  attribute15:
    type: str
    description:
      - Expression that would be evaluated to extract attribute15 from the webauth
        response
  attribute16:
    type: str
    description:
      - Expression that would be evaluated to extract attribute16 from the webauth
        response
  attribute2:
    type: str
    description:
      - Expression that would be evaluated to extract attribute2 from the webauth
        response
  attribute3:
    type: str
    description:
      - Expression that would be evaluated to extract attribute3 from the webauth
        response
  attribute4:
    type: str
    description:
      - Expression that would be evaluated to extract attribute4 from the webauth
        response
  attribute5:
    type: str
    description:
      - Expression that would be evaluated to extract attribute5 from the webauth
        response
  attribute6:
    type: str
    description:
      - Expression that would be evaluated to extract attribute6 from the webauth
        response
  attribute7:
    type: str
    description:
      - Expression that would be evaluated to extract attribute7 from the webauth
        response
  attribute8:
    type: str
    description:
      - Expression that would be evaluated to extract attribute8 from the webauth
        response
  attribute9:
    type: str
    description:
      - Expression that would be evaluated to extract attribute9 from the webauth
        response
  defaultauthenticationgroup:
    type: str
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  fullreqexpr:
    type: str
    description:
      - Exact HTTP request, in the form of an expression, which the Citrix ADC sends
        to the authentication server.
      - The Citrix ADC does not check the validity of this request. One must manually
        validate the request.
  name:
    type: str
    description:
      - Name for the Web Authentication action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
  scheme:
    type: str
    choices:
      - http
      - https
    description:
      - Type of scheme for the web server.
  serverip:
    type: str
    description:
      - IP address of the web server to be used for authentication.
  serverport:
    type: int
    description:
      - Port on which the web server accepts connections.
  successrule:
    type: str
    description:
      - Expression, that checks to see if authentication is successful.
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
