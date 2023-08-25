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
module: authenticationsamlaction
short_description: Configuration for AAA Saml action resource.
description: Configuration for AAA Saml action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  artifactresolutionserviceurl:
    description:
      - URL of the Artifact Resolution Service on IdP to which Citrix ADC will post
        artifact to get actual SAML token.
    type: str
  attribute1:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute1. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute10:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute10. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute11:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute11. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute12:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute12. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute13:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute13. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute14:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute14. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute15:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute15. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute16:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute16. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute2:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute2. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute3:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute3. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute4:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute4. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute5:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute5. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute6:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute6. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute7:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute7. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute8:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute8. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attribute9:
    description:
      - Name of the attribute in SAML Assertion whose value needs to be extracted
        and stored as attribute9. Maximum length of the extracted attribute is 239
        bytes.
    type: str
  attributeconsumingserviceindex:
    description:
      - Index/ID of the attribute specification at Identity Provider (IdP). IdP will
        locate attributes requested by SP using this index and send those attributes
        in Assertion
    type: int
    default: 255
  attributes:
    description:
      - 'List of attribute names separated by '','' which needs to be extracted. '
      - 'Note that preceeding and trailing spaces will be removed. '
      - Attribute name can be 127 bytes and total length of this string should not
        cross 2047 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
    type: str
  audience:
    description:
      - Audience for which assertion sent by IdP is applicable. This is typically
        entity name or url that represents ServiceProvider
    type: str
  authnctxclassref:
    choices:
      - InternetProtocol
      - InternetProtocolPassword
      - Kerberos
      - MobileOneFactorUnregistered
      - MobileTwoFactorUnregistered
      - MobileOneFactorContract
      - MobileTwoFactorContract
      - Password
      - PasswordProtectedTransport
      - PreviousSession
      - X509
      - PGP
      - SPKI
      - XMLDSig
      - Smartcard
      - SmartcardPKI
      - SoftwarePKI
      - Telephony
      - NomadTelephony
      - PersonalTelephony
      - AuthenticatedTelephony
      - SecureRemotePassword
      - TLSClient
      - TimeSyncToken
      - Unspecified
      - Windows
    description:
      - This element specifies the authentication class types that are requested from
        IdP (IdentityProvider).
      - 'C(InternetProtocol): This is applicable when a principal is authenticated
        through the use of a provided IP address.'
      - 'C(InternetProtocolPassword): This is applicable when a principal is authenticated
        through the use of a provided IP address, in addition to a username/password.'
      - 'C(Kerberos): This is applicable when the principal has authenticated using
        a password to a local authentication authority, in order to acquire a C(Kerberos)
        ticket.'
      - 'C(MobileOneFactorUnregistered): This indicates authentication of the mobile
        device without requiring explicit end-user interaction.'
      - 'C(MobileTwoFactorUnregistered): This indicates two-factor based authentication
        during mobile customer registration process, such as secure device and user
        PIN.'
      - 'C(MobileOneFactorContract): Reflects mobile contract customer registration
        procedures and a single factor authentication.'
      - 'C(MobileTwoFactorContract): Reflects mobile contract customer registration
        procedures and a two-factor based authentication.'
      - 'C(Password): This class is applicable when a principal authenticates using
        password over unprotected http session.'
      - 'C(PasswordProtectedTransport): This class is applicable when a principal
        authenticates to an authentication authority through the presentation of a
        password over a protected session.'
      - 'C(PreviousSession): This class is applicable when a principal had authenticated
        to an authentication authority at some point in the past using any authentication
        context.'
      - 'C(X509): This indicates that the principal authenticated by means of a digital
        signature where the key was validated as part of an X.509 Public Key Infrastructure.'
      - 'C(PGP): This indicates that the principal authenticated by means of a digital
        signature where the key was validated as part of a C(PGP) Public Key Infrastructure.'
      - 'C(SPKI): This indicates that the principal authenticated by means of a digital
        signature where the key was validated via an C(SPKI) Infrastructure.'
      - 'C(XMLDSig): This indicates that the principal authenticated by means of a
        digital signature according to the processing rules specified in the XML Digital
        Signature specification.'
      - 'C(Smartcard): This indicates that the principal has authenticated using smartcard.'
      - 'C(SmartcardPKI): This class is applicable when a principal authenticates
        to an authentication authority through a two-factor authentication mechanism
        using a smartcard with enclosed private key and a PIN.'
      - 'C(SoftwarePKI): This class is applicable when a principal uses an X.509 certificate
        stored in software to authenticate to the authentication authority.'
      - 'C(Telephony): This class is used to indicate that the principal authenticated
        via the provision of a fixed-line telephone number, transported via a telephony
        protocol such as ADSL.'
      - 'C(NomadTelephony): Indicates that the principal is "roaming" and authenticates
        via the means of the line number, a user suffix, and a password element.'
      - 'C(PersonalTelephony): This class is used to indicate that the principal authenticated
        via the provision of a fixed-line telephone.'
      - 'C(AuthenticatedTelephony): Indicates that the principal authenticated via
        the means of the line number, a user suffix, and a password element.'
      - 'C(SecureRemotePassword): This class is applicable when the authentication
        was performed by means of Secure Remote C(Password).'
      - 'C(TLSClient): This class indicates that the principal authenticated by means
        of a client certificate, secured with the SSL/TLS transport.'
      - 'C(TimeSyncToken): This is applicable when a principal authenticates through
        a time synchronization token.'
      - 'C(Unspecified): This indicates that the authentication was performed by unspecified
        means.'
      - 'C(Windows): This indicates that C(Windows) integrated authentication is utilized
        for authentication.'
    type: list
    elements: str
  customauthnctxclassref:
    description:
      - This element specifies the custom authentication class reference to be sent
        as a part of the Authentication Request that is sent by the SP to SAML IDP.
        The input string must be the body of the authentication class being requested.
      - 'Input format: Alphanumeric string or URL specifying the body of the Request.If
        more than one string has to be provided, then the same can be done by specifying
        the classes as a string of comma separated values.'
      - 'Example input: set authentication samlaction samlact1 -customAuthnCtxClassRef
        http://www.class1.com/LoA1,http://www.class2.com/LoA2'
    type: str
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  digestmethod:
    choices:
      - SHA1
      - SHA256
    description:
      - Algorithm to be used to compute/verify digest for SAML transactions
    type: str
    default: SHA256
  enforceusername:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to choose whether the username that is extracted from SAML assertion
        can be edited in login page while doing second factor
    type: str
    default: 'ON'
  forceauthn:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option that forces authentication at the Identity Provider (IdP) that receives
        Citrix ADC's request
    type: str
    default: 'OFF'
  groupnamefield:
    description:
      - Name of the tag in assertion that contains user groups.
    type: str
  logoutbinding:
    choices:
      - REDIRECT
      - POST
    description:
      - This element specifies the transport mechanism of saml logout messages.
    type: str
    default: POST
  logouturl:
    description:
      - SingleLogout URL on IdP to which logoutRequest will be sent on Citrix ADC
        session cleanup.
    type: str
  metadatarefreshinterval:
    description:
      - Interval in minutes for fetching metadata from specified metadata URL
    type: int
    default: 3600
  metadataurl:
    description:
      - This URL is used for obtaining saml metadata. Note that it fills samlIdPCertName
        and samlredirectUrl fields so those fields should not be updated when metadataUrl
        present
    type: str
  name:
    description:
      - 'Name for the SAML server profile (action). '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after SAML profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
    type: str
  relaystaterule:
    description:
      - Boolean expression that will be evaluated to validate the SAML Response.
      - 'Examples: '
      - set authentication samlaction <actionname> -relaystateRule 'AAA.LOGIN.RELAYSTATE.EQ("https://fqdn.com/")'
      - set authentication samlaction <actionname> -relaystateRule 'AAA.LOGIN.RELAYSTATE.CONTAINS("https://fqdn.com/")'
      - set authentication samlaction <actionname> -relaystateRule 'AAA.LOGIN.RELAYSTATE.CONTAINS_ANY("patset_name")'
      - set authentication samlAction samlsp -relaystateRule 'AAA.LOGIN.RELAYSTATE.REGEX_MATCH(re#http://<regex>.com/#)'.
    type: str
  requestedauthncontext:
    choices:
      - exact
      - minimum
      - maximum
      - better
    description:
      - This element specifies the authentication context requirements of authentication
        statements returned in the response.
    type: str
    default: exact
  samlacsindex:
    description:
      - Index/ID of the metadata entry corresponding to this configuration.
    type: int
    default: 255
  samlbinding:
    choices:
      - REDIRECT
      - POST
      - ARTIFACT
    description:
      - This element specifies the transport mechanism of saml messages.
    type: str
    default: POST
  samlidpcertname:
    description:
      - Name of the SSL certificate used to verify responses from SAML Identity Provider
        (IdP). Note that if metadateURL is present then this filed should be empty.
    type: str
  samlissuername:
    description:
      - "The name to be used in requests sent from\tCitrix ADC to IdP to uniquely\
        \ identify Citrix ADC."
    type: str
  samlredirecturl:
    description:
      - URL to which users are redirected for authentication. Note that if metadateURL
        is present then this filed should be empty
    type: str
  samlrejectunsignedassertion:
    choices:
      - 'ON'
      - 'OFF'
      - STRICT
    description:
      - Reject unsigned SAML assertions. C(ON) option results in rejection of Assertion
        that is received without signature. C(STRICT) option ensures that both Response
        and Assertion are signed. C(OFF) allows unsigned Assertions.
    type: str
    default: 'ON'
  samlsigningcertname:
    description:
      - Name of the SSL certificate to sign requests from ServiceProvider (SP) to
        Identity Provider (IdP).
    type: str
  samltwofactor:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to enable second factor after SAML
    type: str
    default: 'OFF'
  samluserfield:
    description:
      - SAML user ID, as given in the SAML assertion.
    type: str
  sendthumbprint:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to send thumbprint instead of x509 certificate in SAML request
    type: str
    default: 'OFF'
  signaturealg:
    choices:
      - RSA-SHA1
      - RSA-SHA256
    description:
      - Algorithm to be used to sign/verify SAML transactions
    type: str
    default: RSA-SHA256
  skewtime:
    description:
      - This option specifies the allowed clock skew in number of minutes that Citrix
        ADC ServiceProvider allows on an incoming assertion. For example, if skewTime
        is 10, then assertion would be valid from (current time - 10) min to (current
        time + 10) min, ie 20min in all.
    type: int
    default: 5
  statechecks:
    description:
      - Boolean expression that will be evaluated to validate HTTP requests on SAML
        endpoints.
      - 'Examples: '
      - set authentication samlaction <actionname> -stateChecks 'HTTP.REQ.HOSTNAME.EQ("https://fqdn.com/")'
    type: str
  storesamlresponse:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to store entire SAML Response through the life of user session.
    type: str
    default: 'OFF'
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
