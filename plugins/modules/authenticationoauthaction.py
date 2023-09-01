#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
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
  allowedalgorithms:
    choices:
      - HS256
      - RS256
      - RS512
    description:
      - Multivalued option to specify allowed token verification algorithms.
    type: list
    elements: str
    default: OAUTH_ALG_ALL
  attribute1:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute1
    type: str
  attribute10:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute10
    type: str
  attribute11:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute11
    type: str
  attribute12:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute12
    type: str
  attribute13:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute13
    type: str
  attribute14:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute14
    type: str
  attribute15:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute15
    type: str
  attribute16:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute16
    type: str
  attribute2:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute2
    type: str
  attribute3:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute3
    type: str
  attribute4:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute4
    type: str
  attribute5:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute5
    type: str
  attribute6:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute6
    type: str
  attribute7:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute7
    type: str
  attribute8:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute8
    type: str
  attribute9:
    description:
      - Name of the attribute to be extracted from OAuth Token and to be stored in
        the attribute9
    type: str
  attributes:
    description:
      - List of attribute names separated by ',' which needs to be extracted.
      - Note that preceding and trailing spaces will be removed.
      - Attribute name can be 127 bytes and total length of this string should not
        cross 1023 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
    type: str
  audience:
    description:
      - Audience for which token sent by Authorization server is applicable. This
        is typically entity name or url that represents the recipient
    type: str
  authentication:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If authentication is disabled, password is not sent in the request.
    type: str
    default: ENABLED
  authorizationendpoint:
    description:
      - Authorization endpoint/url to which unauthenticated user will be redirected.
        Citrix ADC redirects user to this endpoint by adding query parameters including
        clientid. If this parameter not specified then as default value we take Token
        Endpoint/URL value. Please note that Authorization Endpoint or Token Endpoint
        is mandatory for oauthAction
    type: str
  certendpoint:
    description:
      - URL of the endpoint that contains JWKs (Json Web Key) for JWT (Json Web Token)
        verification.
    type: str
  certfilepath:
    description:
      - Path to the file that contains JWKs (Json Web Key) for JWT (Json Web Token)
        verification.
    type: str
  clientid:
    description:
      - Unique identity of the client/user who is getting authenticated. Authorization
        server infers client configuration using this ID
    type: str
  clientsecret:
    description:
      - Secret string established by user and authorization server
    type: str
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  granttype:
    choices:
      - CODE
      - PASSWORD
    description:
      - Grant type support. value can be code or password
    type: str
    default: CODE
  graphendpoint:
    description:
      - URL of the Graph API service to learn Enterprise Mobility Services (EMS) endpoints.
    type: str
  idtokendecryptendpoint:
    description:
      - URL to which obtained idtoken will be posted to get a decrypted user identity.
        Encrypted idtoken will be obtained by posting OAuth token to token endpoint.
        In order to decrypt idtoken, Citrix ADC posts request to the URL configured
    type: str
  introspecturl:
    description:
      - URL to which access token would be posted for validation
    type: str
  issuer:
    description:
      - Identity of the server whose tokens are to be accepted.
    type: str
  metadataurl:
    description:
      - Well-known configuration endpoint of the Authorization Server. Citrix ADC
        fetches server details from this endpoint.
    type: str
  name:
    description:
      - 'Name for the OAuth Authentication action. '
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
  oauthtype:
    choices:
      - GENERIC
      - INTUNE
      - ATHENA
    description:
      - Type of the OAuth implementation. Default value is generic implementation
        that is applicable for most deployments.
    type: str
    default: GENERIC
  pkce:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to enable/disable PKCE flow during authentication.
    type: str
    default: ENABLED
  refreshinterval:
    description:
      - Interval at which services are monitored for necessary configuration.
    type: float
    default: 1440
  resourceuri:
    description:
      - Resource URL for Oauth configuration.
    type: str
  skewtime:
    description:
      - This option specifies the allowed clock skew in number of minutes that Citrix
        ADC allows on an incoming token. For example, if skewTime is 10, then token
        would be valid from (current time - 10) min to (current time + 10) min, ie
        20min in all.
    type: float
    default: 5
  tenantid:
    description:
      - TenantID of the application. This is usually specific to providers such as
        Microsoft and usually refers to the deployment identifier.
    type: str
  tokenendpoint:
    description:
      - URL to which OAuth token will be posted to verify its authenticity. User obtains
        this token from Authorization server upon successful authentication. Citrix
        ADC will validate presented token by posting it to the URL configured
    type: str
  tokenendpointauthmethod:
    choices:
      - client_secret_post
      - client_secret_jwt
      - private_key_jwt
      - client_secret_basic
    description:
      - Option to select the variant of token authentication method. This method is
        used while exchanging code with IdP.
    type: str
    default: client_secret_post
  userinfourl:
    description:
      - URL to which OAuth access token will be posted to obtain user information.
    type: str
  usernamefield:
    description:
      - Attribute in the token from which username should be extracted.
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
