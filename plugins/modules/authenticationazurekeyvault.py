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
  authentication:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If authentication is disabled, otp checks are not performed after azure vault
        keys are obtained. This is useful to distinguish whether user has registered
        devices.
    type: str
    default: ENABLED
  clientid:
    description:
      - Unique identity of the relying party requesting for authentication.
    type: str
  clientsecret:
    description:
      - Unique secret string to authorize relying party at authorization server.
    type: str
  defaultauthenticationgroup:
    description:
      - This is the group that is added to user sessions that match current IdP policy.
        It can be used in policies to identify relying party trust.
    type: str
  name:
    description:
      - Name for the new Azure Key Vault profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after an action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
    type: str
  pushservice:
    description:
      - Name of the service used to send push notifications
    type: str
  refreshinterval:
    description:
      - Interval at which access token in obtained.
    type: float
    default: 50
  servicekeyname:
    description:
      - Friendly name of the Key to be used to compute signature.
    type: str
  signaturealg:
    choices:
      - RS256
    description:
      - Algorithm to be used to sign/verify transactions
    type: str
    default: RS256
  tenantid:
    description:
      - TenantID of the application. This is usually specific to providers such as
        Microsoft and usually refers to the deployment identifier.
    type: str
  tokenendpoint:
    description:
      - URL endpoint on relying party to which the OAuth token is to be sent.
    type: str
  vaultname:
    description:
      - Name of the Azure vault account as configured in azure portal.
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
