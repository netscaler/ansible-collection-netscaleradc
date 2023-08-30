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
module: authenticationldapaction
short_description: Configuration for LDAP action resource.
description: Configuration for LDAP action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  alternateemailattr:
    description:
      - The NetScaler appliance uses the alternateive email attribute to query the
        Active Directory for the alternative email id of a user
    type: str
  attribute1:
    description:
      - Expression that would be evaluated to extract attribute1 from the ldap response
    type: str
  attribute10:
    description:
      - Expression that would be evaluated to extract attribute10 from the ldap response
    type: str
  attribute11:
    description:
      - Expression that would be evaluated to extract attribute11 from the ldap response
    type: str
  attribute12:
    description:
      - Expression that would be evaluated to extract attribute12 from the ldap response
    type: str
  attribute13:
    description:
      - Expression that would be evaluated to extract attribute13 from the ldap response
    type: str
  attribute14:
    description:
      - Expression that would be evaluated to extract attribute14 from the ldap response
    type: str
  attribute15:
    description:
      - Expression that would be evaluated to extract attribute15 from the ldap response
    type: str
  attribute16:
    description:
      - Expression that would be evaluated to extract attribute16 from the ldap response
    type: str
  attribute2:
    description:
      - Expression that would be evaluated to extract attribute2 from the ldap response
    type: str
  attribute3:
    description:
      - Expression that would be evaluated to extract attribute3 from the ldap response
    type: str
  attribute4:
    description:
      - Expression that would be evaluated to extract attribute4 from the ldap response
    type: str
  attribute5:
    description:
      - Expression that would be evaluated to extract attribute5 from the ldap response
    type: str
  attribute6:
    description:
      - Expression that would be evaluated to extract attribute6 from the ldap response
    type: str
  attribute7:
    description:
      - Expression that would be evaluated to extract attribute7 from the ldap response
    type: str
  attribute8:
    description:
      - Expression that would be evaluated to extract attribute8 from the ldap response
    type: str
  attribute9:
    description:
      - Expression that would be evaluated to extract attribute9 from the ldap response
    type: str
  attributes:
    description:
      - 'List of attribute names separated by '','' which needs to be fetched from
        ldap server. '
      - 'Note that preceeding and trailing spaces will be removed. '
      - Attribute name can be 127 bytes and total length of this string should not
        cross 2047 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
    type: str
  authentication:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform LDAP authentication.
      - 'If authentication is disabled, any LDAP authentication attempt returns authentication
        success if the user is found. '
      - CAUTION! Authentication should be disabled only for authorization group extraction
        or where other (non-LDAP) authentication methods are in use and either bound
        to a primary list or flagged as secondary.
    type: str
    default: ENABLED
  authtimeout:
    description:
      - Number of seconds the Citrix ADC waits for a response from the RADIUS server.
    type: int
    default: 3
  cloudattributes:
    choices:
      - ENABLED
      - DISABLED
    description:
      - The Citrix ADC uses the cloud attributes to extract additional attributes
        from LDAP servers required for Citrix Cloud operations
    type: str
    default: DISABLED
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  email:
    description:
      - The Citrix ADC uses the email attribute to query the Active Directory for
        the email id of a user
    type: str
    default: mail
  followreferrals:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Setting this option to C(ON) enables following LDAP referrals received from
        the LDAP server.
    type: str
    default: 'OFF'
  groupattrname:
    description:
      - LDAP group attribute name.
      - Used for group extraction on the LDAP server.
    type: str
  groupnameidentifier:
    description:
      - Name that uniquely identifies a group in LDAP or Active Directory.
    type: str
  groupsearchattribute:
    description:
      - 'LDAP group search attribute. '
      - Used to determine to which groups a group belongs.
    type: str
  groupsearchfilter:
    description:
      - String to be combined with the default LDAP group search string to form the
        search value.  For example, the group search filter ""vpnallowed=true"" when
        combined with the group identifier ""samaccount"" and the group name ""g1""
        yields the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". If nestedGroupExtraction
        is ENABLED, the filter is applied on the first level group search as well,
        otherwise first level groups (of which user is a direct member of) will be
        fetched without applying this filter. (Be sure to enclose the search string
        in two sets of double quotation marks; both sets are needed.)
    type: str
  groupsearchsubattribute:
    description:
      - 'LDAP group search subattribute. '
      - Used to determine to which groups a group belongs.
    type: str
  kbattribute:
    description:
      - KnowledgeBasedAuthentication(KBA) attribute on AD. This attribute is used
        to store and retrieve preconfigured Question and Answer knowledge base used
        for KBA authentication.
    type: str
  ldapbase:
    description:
      - 'Base (node) from which to start LDAP searches. '
      - If the LDAP server is running locally, the default value of base is dc=netscaler,
        dc=com.
    type: str
  ldapbinddn:
    description:
      - 'Full distinguished name (DN) that is used to bind to the LDAP server. '
      - 'Default: cn=Manager,dc=netscaler,dc=com'
    type: str
  ldapbinddnpassword:
    description:
      - Password used to bind to the LDAP server.
    type: str
  ldaphostname:
    description:
      - Hostname for the LDAP server.  If -validateServerCert is ON then this must
        be the host name on the certificate from the LDAP server.
      - A hostname mismatch will cause a connection failure.
    type: str
  ldaploginname:
    description:
      - 'LDAP login name attribute. '
      - The Citrix ADC uses the LDAP login name to query external LDAP servers or
        Active Directories.
    type: str
  maxldapreferrals:
    description:
      - Specifies the maximum number of nested referrals to follow.
    type: int
    default: 1
  maxnestinglevel:
    description:
      - If nested group extraction is ON, specifies the number of levels up to which
        group extraction is performed.
    type: int
    default: 2
  mssrvrecordlocation:
    description:
      - MSSRV Specific parameter. Used to locate the DNS node to which the SRV record
        pertains in the domainname. The domainname is appended to it to form the srv
        record.
      - 'Example : For "dc._msdcs", the srv record formed is _ldap._tcp.dc._msdcs.<domainname>.'
    type: str
  name:
    description:
      - 'Name for the new LDAP action. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the LDAP action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
    type: str
  nestedgroupextraction:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow nested group extraction, in which the Citrix ADC queries external LDAP
        servers to determine whether a group is part of another group.
    type: str
    default: 'OFF'
  otpsecret:
    description:
      - OneTimePassword(OTP) Secret key attribute on AD. This attribute is used to
        store and retrieve secret key used for OTP check
    type: str
  passwdchange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow password change requests.
    type: str
    default: DISABLED
  pushservice:
    description:
      - Name of the service used to send push notifications
    type: str
  referraldnslookup:
    choices:
      - A-REC
      - SRV-REC
      - MSSRV-REC
    description:
      - Specifies the DNS Record lookup Type for the referrals
    type: str
    default: A-REC
  requireuser:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Require a successful user search for authentication.
      - CAUTION!  This field should be set to C(NO) only if usersearch not required
        [Both username validation as well as password validation skipped] and (non-LDAP)
        authentication methods are in use and either bound to a primary list or flagged
        as secondary.
    type: str
    default: 'YES'
  searchfilter:
    description:
      - String to be combined with the default LDAP user search string to form the
        search value. For example, if the search filter "vpnallowed=true" is combined
        with the LDAP login name "samaccount" and the user-supplied username is "bob",
        the result is the LDAP search string ""&(vpnallowed=true)(samaccount=bob)""
        (Be sure to enclose the search string in two sets of double quotation marks;
        both sets are needed.).
    type: str
  sectype:
    choices:
      - PLAINTEXT
      - TLS
      - SSL
    description:
      - Type of security used for communications between the Citrix ADC and the LDAP
        server. For the C(PLAINTEXT) setting, no encryption is required.
    type: str
    default: PLAINTEXT
  serverip:
    description:
      - IP address assigned to the LDAP server.
    type: str
  servername:
    description:
      - LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.
    type: str
  serverport:
    description:
      - Port on which the LDAP server accepts connections.
    type: int
    default: 389
  sshpublickey:
    description:
      - SSH PublicKey is attribute on AD. This attribute is used to retrieve ssh PublicKey
        for RBA authentication
    type: str
  ssonameattribute:
    description:
      - 'LDAP single signon (SSO) attribute. '
      - The Citrix ADC uses the SSO name attribute to query external LDAP servers
        or Active Directories for an alternate username.
    type: str
  subattributename:
    description:
      - 'LDAP group sub-attribute name. '
      - Used for group extraction from the LDAP server.
    type: str
  svrtype:
    choices:
      - AD
      - NDS
    description:
      - The type of LDAP server.
    type: str
    default: AAA_LDAP_SERVER_TYPE_DEFAULT
  validateservercert:
    choices:
      - 'YES'
      - 'NO'
    description:
      - When to validate LDAP server certs
    type: str
    default: 'NO'
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
