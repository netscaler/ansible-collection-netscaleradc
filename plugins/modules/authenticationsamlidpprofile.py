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
module: authenticationsamlidpprofile
short_description: Configuration for AAA Saml IdentityProvider (IdP) profile resource.
description: Configuration for AAA Saml IdentityProvider (IdP) profile resource.
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
  acsurlrule:
    type: str
    description:
      - Expression that will be evaluated to allow Assertion Consumer Service URI
        coming in the SAML Request
  assertionconsumerserviceurl:
    type: str
    description:
      - URL to which the assertion is to be sent.
  attribute1:
    type: str
    description:
      - Name of attribute1 that needs to be sent in SAML Assertion
  attribute10:
    type: str
    description:
      - Name of attribute10 that needs to be sent in SAML Assertion
  attribute10expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute10's value to be sent
        in Assertion
  attribute10format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute10 to be sent in Assertion.
  attribute10friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute10 that needs to be sent in SAML Assertion
  attribute11:
    type: str
    description:
      - Name of attribute11 that needs to be sent in SAML Assertion
  attribute11expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute11's value to be sent
        in Assertion
  attribute11format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute11 to be sent in Assertion.
  attribute11friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute11 that needs to be sent in SAML Assertion
  attribute12:
    type: str
    description:
      - Name of attribute12 that needs to be sent in SAML Assertion
  attribute12expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute12's value to be sent
        in Assertion
  attribute12format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute12 to be sent in Assertion.
  attribute12friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute12 that needs to be sent in SAML Assertion
  attribute13:
    type: str
    description:
      - Name of attribute13 that needs to be sent in SAML Assertion
  attribute13expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute13's value to be sent
        in Assertion
  attribute13format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute13 to be sent in Assertion.
  attribute13friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute13 that needs to be sent in SAML Assertion
  attribute14:
    type: str
    description:
      - Name of attribute14 that needs to be sent in SAML Assertion
  attribute14expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute14's value to be sent
        in Assertion
  attribute14format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute14 to be sent in Assertion.
  attribute14friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute14 that needs to be sent in SAML Assertion
  attribute15:
    type: str
    description:
      - Name of attribute15 that needs to be sent in SAML Assertion
  attribute15expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute15's value to be sent
        in Assertion
  attribute15format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute15 to be sent in Assertion.
  attribute15friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute15 that needs to be sent in SAML Assertion
  attribute16:
    type: str
    description:
      - Name of attribute16 that needs to be sent in SAML Assertion
  attribute16expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute16's value to be sent
        in Assertion
  attribute16format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute16 to be sent in Assertion.
  attribute16friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute16 that needs to be sent in SAML Assertion
  attribute1expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute1's value to be sent
        in Assertion
  attribute1format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute1 to be sent in Assertion.
  attribute1friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute1 that needs to be sent in SAML Assertion
  attribute2:
    type: str
    description:
      - Name of attribute2 that needs to be sent in SAML Assertion
  attribute2expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute2's value to be sent
        in Assertion
  attribute2format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute2 to be sent in Assertion.
  attribute2friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute2 that needs to be sent in SAML Assertion
  attribute3:
    type: str
    description:
      - Name of attribute3 that needs to be sent in SAML Assertion
  attribute3expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute3's value to be sent
        in Assertion
  attribute3format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute3 to be sent in Assertion.
  attribute3friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute3 that needs to be sent in SAML Assertion
  attribute4:
    type: str
    description:
      - Name of attribute4 that needs to be sent in SAML Assertion
  attribute4expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute4's value to be sent
        in Assertion
  attribute4format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute4 to be sent in Assertion.
  attribute4friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute4 that needs to be sent in SAML Assertion
  attribute5:
    type: str
    description:
      - Name of attribute5 that needs to be sent in SAML Assertion
  attribute5expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute5's value to be sent
        in Assertion
  attribute5format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute5 to be sent in Assertion.
  attribute5friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute5 that needs to be sent in SAML Assertion
  attribute6:
    type: str
    description:
      - Name of attribute6 that needs to be sent in SAML Assertion
  attribute6expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute6's value to be sent
        in Assertion
  attribute6format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute6 to be sent in Assertion.
  attribute6friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute6 that needs to be sent in SAML Assertion
  attribute7:
    type: str
    description:
      - Name of attribute7 that needs to be sent in SAML Assertion
  attribute7expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute7's value to be sent
        in Assertion
  attribute7format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute7 to be sent in Assertion.
  attribute7friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute7 that needs to be sent in SAML Assertion
  attribute8:
    type: str
    description:
      - Name of attribute8 that needs to be sent in SAML Assertion
  attribute8expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute8's value to be sent
        in Assertion
  attribute8format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute8 to be sent in Assertion.
  attribute8friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute8 that needs to be sent in SAML Assertion
  attribute9:
    type: str
    description:
      - Name of attribute9 that needs to be sent in SAML Assertion
  attribute9expr:
    type: str
    description:
      - Expression that will be evaluated to obtain attribute9's value to be sent
        in Assertion
  attribute9format:
    type: str
    choices:
      - URI
      - Basic
    description:
      - Format of Attribute9 to be sent in Assertion.
  attribute9friendlyname:
    type: str
    description:
      - User-Friendly Name of attribute9 that needs to be sent in SAML Assertion
  audience:
    type: str
    description:
      - Audience for which assertion sent by IdP is applicable. This is typically
        entity name or url that represents ServiceProvider
  defaultauthenticationgroup:
    type: str
    description:
      - This group will be part of AAA session's internal group list. This will be
        helpful to admin in Nfactor flow to decide right AAA configuration for Relaying
        Party. In authentication policy AAA.USER.IS_MEMBER_OF("<default_auth_group>")  is
        way to use this feature.
  digestmethod:
    type: str
    choices:
      - SHA1
      - SHA256
    description:
      - Algorithm to be used to compute/verify digest for SAML transactions
  encryptassertion:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to encrypt assertion when Citrix ADC IDP sends one.
  encryptionalgorithm:
    type: str
    choices:
      - DES3
      - AES128
      - AES192
      - AES256
    description:
      - Algorithm to be used to encrypt SAML assertion
  keytransportalg:
    type: str
    choices:
      - RSA-V1_5
      - RSA_OAEP
    description:
      - Key transport algorithm to be used in encryption of SAML assertion
  logoutbinding:
    type: str
    choices:
      - REDIRECT
      - POST
    description:
      - This element specifies the transport mechanism of saml logout messages.
  metadatarefreshinterval:
    type: int
    description:
      - Interval in minute for fetching metadata from specified metadata URL
  metadataurl:
    type: str
    description:
      - This URL is used for obtaining samlidp metadata
  name:
    type: str
    description:
      - Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after an action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  nameidexpr:
    type: str
    description:
      - Expression that will be evaluated to obtain NameIdentifier to be sent in assertion
  nameidformat:
    type: str
    choices:
      - Unspecified
      - emailAddress
      - X509SubjectName
      - WindowsDomainQualifiedName
      - kerberos
      - entity
      - persistent
      - transient
    description:
      - Format of Name Identifier sent in Assertion.
  rejectunsignedrequests:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to Reject unsigned SAML Requests. C(ON) option denies any authentication
        requests that arrive without signature.
  samlbinding:
    type: str
    choices:
      - REDIRECT
      - POST
      - ARTIFACT
    description:
      - This element specifies the transport mechanism of saml messages.
  samlidpcertname:
    type: str
    description:
      - Name of the certificate used to sign the SAMLResposne that is sent to Relying
        Party or Service Provider after successful authentication
  samlissuername:
    type: str
    description:
      - "The name to be used in requests sent from\tCitrix ADC to IdP to uniquely\
        \ identify Citrix ADC."
  samlsigningcertversion:
    type: str
    description:
      - version of the certificate in signature service used to sign the SAMLResposne
        that is sent to Relying Party or Service Provider after successful authentication
  samlspcertname:
    type: str
    description:
      - Name of the SSL certificate of SAML Relying Party. This certificate is used
        to verify signature of the incoming AuthnRequest from a Relying Party or Service
        Provider
  samlspcertversion:
    type: str
    description:
      - version of the certificate in signature service used to verify the signature
        of the incoming AuthnRequest from a Relying Party or Service Provider
  sendpassword:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to send password in assertion.
  serviceproviderid:
    type: str
    description:
      - Unique identifier of the Service Provider that sends SAML Request. Citrix
        ADC will ensure that the Issuer of the SAML Request matches this URI. In case
        of SP initiated sign-in scenarios, this value must be same as samlIssuerName
        configured in samlAction.
  signassertion:
    type: str
    choices:
      - NONE
      - ASSERTION
      - RESPONSE
      - BOTH
    description:
      - Option to sign portions of assertion when Citrix ADC IDP sends one. Based
        on the user selection, either Assertion or Response or Both or none can be
        signed
  signaturealg:
    type: str
    choices:
      - RSA-SHA1
      - RSA-SHA256
    description:
      - Algorithm to be used to sign/verify SAML transactions
  signatureservice:
    type: str
    description:
      - Name of the service in cloud used to sign the data
  skewtime:
    type: int
    description:
      - This option specifies the number of minutes on either side of current time
        that the assertion would be valid. For example, if skewTime is 10, then assertion
        would be valid from (current time - 10) min to (current time + 10) min, ie
        20min in all.
  splogouturl:
    type: str
    description:
      - Endpoint on the ServiceProvider (SP) to which logout messages are to be sent
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample authenticationsamlidpprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure authenticationsamlidpprofile
      delegate_to: localhost
      netscaler.adc.authenticationsamlidpprofile:
        state: present
        name: samlidp_red1
        samlbinding: REDIRECT
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
