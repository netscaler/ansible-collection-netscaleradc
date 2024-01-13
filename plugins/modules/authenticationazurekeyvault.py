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
module: authenticationazurekeyvault
short_description: Configuration for Azure Key Vault entity resource.
description: Configuration for Azure Key Vault entity resource.
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
  authentication:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If authentication is disabled, otp checks are not performed after azure vault
        keys are obtained. This is useful to distinguish whether user has registered
        devices.
  clientid:
    type: str
    description:
      - Unique identity of the relying party requesting for authentication.
  clientsecret:
    type: str
    description:
      - Unique secret string to authorize relying party at authorization server.
  defaultauthenticationgroup:
    type: str
    description:
      - This is the group that is added to user sessions that match current IdP policy.
        It can be used in policies to identify relying party trust.
  name:
    type: str
    description:
      - Name for the new Azure Key Vault profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after an action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  pushservice:
    type: str
    description:
      - Name of the service used to send push notifications
  refreshinterval:
    type: float
    description:
      - Interval at which access token in obtained.
  servicekeyname:
    type: str
    description:
      - Friendly name of the Key to be used to compute signature.
  signaturealg:
    type: str
    choices:
      - RS256
    description:
      - Algorithm to be used to sign/verify transactions
  tenantid:
    type: str
    description:
      - TenantID of the application. This is usually specific to providers such as
        Microsoft and usually refers to the deployment identifier.
  tokenendpoint:
    type: str
    description:
      - URL endpoint on relying party to which the OAuth token is to be sent.
  vaultname:
    type: str
    description:
      - Name of the Azure vault account as configured in azure portal.
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
