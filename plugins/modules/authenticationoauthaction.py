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
module: authenticationoauthaction
short_description: Configuration for OAuth authentication action resource.
description: Configuration for OAuth authentication action resource.
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
  allowedalgorithms:
    type: list
    choices:
      - HS256
      - RS256
      - RS512
    description:
      - Multivalued option to specify allowed token verification algorithms.
    elements: str
  attribute1:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute1
  attribute10:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute10
  attribute11:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute11
  attribute12:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute12
  attribute13:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute13
  attribute14:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute14
  attribute15:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute15
  attribute16:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute16
  attribute2:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute2
  attribute3:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute3
  attribute4:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute4
  attribute5:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute5
  attribute6:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute6
  attribute7:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute7
  attribute8:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute8
  attribute9:
    type: str
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute9
  attributes:
    type: str
    description:
      - List of attribute names separated by ',' which needs to be extracted.
      - Note that preceding and trailing spaces will be removed.
      - Attribute name can be 127 bytes and total length of this string should not
        cross 1023 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
  audience:
    type: str
    description:
      - Audience for which token sent by Authorization server is applicable. This
        is typically entity name or url that represents the recipient
  authentication:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If authentication is disabled, password is not sent in the request.
  authorizationendpoint:
    type: str
    description:
      - Authorization endpoint/url to which unauthenticated user will be redirected.
        Citrix ADC redirects user to this endpoint by adding query parameters including
        clientid. If this parameter not specified then as default value we take Token
        Endpoint/URL value. Please note that Authorization Endpoint or Token Endpoint
        is mandatory for oauthAction
  certendpoint:
    type: str
    description:
      - URL of the endpoint that contains JWKs (Json Web Key) for JWT (Json Web Token)
        verification.
  certfilepath:
    type: str
    description:
      - Path to the file that contains JWKs (Json Web Key) for JWT (Json Web Token)
        verification.
  clientid:
    type: str
    description:
      - Unique identity of the client/user who is getting authenticated. Authorization
        server infers client configuration using this ID
  clientsecret:
    type: str
    description:
      - Secret string established by user and authorization server
  defaultauthenticationgroup:
    type: str
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  granttype:
    type: str
    choices:
      - CODE
      - PASSWORD
    description:
      - Grant type support. value can be code or password
  graphendpoint:
    type: str
    description:
      - URL of the Graph API service to learn Enterprise Mobility Services (EMS) endpoints.
  idtokendecryptendpoint:
    type: str
    description:
      - URL to which obtained idtoken will be posted to get a decrypted user identity.
        Encrypted idtoken will be obtained by posting OAuth token to token endpoint.
        In order to decrypt idtoken, Citrix ADC posts request to the URL configured
  introspecturl:
    type: str
    description:
      - URL to which access token would be posted for validation
  issuer:
    type: str
    description:
      - Identity of the server whose tokens are to be accepted.
  metadataurl:
    type: str
    description:
      - Well-known configuration endpoint of the Authorization Server. Citrix ADC
        fetches server details from this endpoint.
  name:
    type: str
    description:
      - Name for the OAuth Authentication action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
  oauthtype:
    type: str
    choices:
      - GENERIC
      - INTUNE
      - ATHENA
    description:
      - Type of the OAuth implementation. Default value is generic implementation
        that is applicable for most deployments.
  pkce:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to enable/disable PKCE flow during authentication.
  refreshinterval:
    type: float
    description:
      - Interval at which services are monitored for necessary configuration.
  resourceuri:
    type: str
    description:
      - Resource URL for Oauth configuration.
  skewtime:
    type: float
    description:
      - This option specifies the allowed clock skew in number of minutes that Citrix
        ADC allows on an incoming token. For example, if skewTime is 10, then token
        would be valid from (current time - 10) min to (current time + 10) min, ie
        20min in all.
  tenantid:
    type: str
    description:
      - TenantID of the application. This is usually specific to providers such as
        Microsoft and usually refers to the deployment identifier.
  tokenendpoint:
    type: str
    description:
      - URL to which OAuth token will be posted to verify its authenticity. User obtains
        this token from Authorization server upon successful authentication. Citrix
        ADC will validate presented token by posting it to the URL configured
  tokenendpointauthmethod:
    type: str
    choices:
      - client_secret_post
      - client_secret_jwt
      - private_key_jwt
      - client_secret_basic
    description:
      - Option to select the variant of token authentication method. This method is
        used while exchanging code with IdP.
  userinfourl:
    type: str
    description:
      - URL to which OAuth access token will be posted to obtain user information.
  usernamefield:
    type: str
    description:
      - Attribute in the token from which username should be extracted.
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
