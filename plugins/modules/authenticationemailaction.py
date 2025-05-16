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
module: authenticationemailaction
short_description: Configuration for Email entity resource.
description: Configuration for Email entity resource.
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  content:
    type: str
    description:
      - Content to be delivered to the user. "$code" string within the content will
        be replaced with the actual one-time-code to be sent.
  defaultauthenticationgroup:
    type: str
    description:
      - This is the group that is added to user sessions that match current IdP policy.
        It can be used in policies to identify relying party trust.
  emailaddress:
    type: str
    description:
      - An optional expression that yields user's email. When not configured, user's
        default mail address would be used. When configured, result of this expression
        is used as destination email address.
  name:
    type: str
    description:
      - Name for the new email action. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after an action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  password:
    type: str
    description:
      - Password/Clientsecret to use when authenticating to the server.
  serverurl:
    type: str
    description:
      - Address of the server that delivers the message. It is fully qualified fqdn
        such as http(s):// or smtp(s):// for http and smtp protocols respectively.
        For SMTP, the port number is mandatory like smtps://smtp.example.com:25.
  timeout:
    type: float
    description:
      - Time after which the code expires.
  type:
    type: str
    choices:
      - SMTP
      - ATHENA
    description:
      - Type of the email action. Default type is C(SMTP).
  username:
    type: str
    description:
      - Username/Clientid/EmailID to be used to authenticate to the server.
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
