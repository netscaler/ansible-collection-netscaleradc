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
module: authenticationoauthidpprofile
short_description: Configuration for OAuth Identity Provider (IdP) profile resource.
description: Configuration for OAuth Identity Provider (IdP) profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  attributes:
    type: str
    description:
      - Name-Value pairs of attributes to be inserted in idtoken. Configuration format
        is name=value_expr@@@name2=value2_expr@@@.
      - '''@@@'' is used as delimiter between Name-Value pairs. name is a literal
        string whose value is 127 characters and does not contain ''='' character.'
      - Value is advanced policy expression terminated by @@@ delimiter. Last value
        need not contain the delimiter.
  audience:
    type: str
    description:
      - Audience for which token is being sent by Citrix ADC IdP. This is typically
        entity name or url that represents the recipient
  clientid:
    type: str
    description:
      - Unique identity of the relying party requesting for authentication.
  clientsecret:
    type: str
    description:
      - Unique secret string to authorize relying party at authorization server.
  configservice:
    type: str
    description:
      - Name of the entity that is used to obtain configuration for the current authentication
        request. It is used only in Citrix Cloud.
  defaultauthenticationgroup:
    type: str
    description:
      - This group will be part of AAA session's internal group list. This will be
        helpful to admin in Nfactor flow to decide right AAA configuration for Relaying
        Party. In authentication policy AAA.USER.IS_MEMBER_OF("<default_auth_group>")  is
        way to use this feature.
  encrypttoken:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to encrypt token when Citrix ADC IDP sends one.
  issuer:
    type: str
    description:
      - "The name to be used in requests sent from\tCitrix ADC to IdP to uniquely\
        \ identify Citrix ADC."
  name:
    type: str
    description:
      - Name for the new OAuth Identity Provider (IdP) single sign-on profile. Must
        begin with an ASCII alphanumeric or underscore (_) character, and must contain
        only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:),
        at (@), equals (=), and hyphen (-) characters. Cannot be changed after an
        action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  redirecturl:
    type: str
    description:
      - URL endpoint on relying party to which the OAuth token is to be sent.
  refreshinterval:
    type: float
    description:
      - Interval at which Relying Party metadata is refreshed.
  relyingpartymetadataurl:
    type: str
    description:
      - This is the endpoint at which Citrix ADC IdP can get details about Relying
        Party (RP) being configured. Metadata response should include endpoints for
        jwks_uri for RP public key(s).
  sendpassword:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to send encrypted password in idtoken.
  signaturealg:
    type: str
    choices:
      - RS256
      - RS512
    description:
      - Algorithm to be used to sign OpenID tokens.
  signatureservice:
    type: str
    description:
      - Name of the service in cloud used to sign the data. This is applicable only
        if signature if offloaded to cloud.
  skewtime:
    type: float
    description:
      - This option specifies the duration for which the token sent by Citrix ADC
        IdP is valid. For example, if skewTime is 10, then token would be valid from
        (current time - 10) min to (current time + 10) min, ie 20min in all.
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
