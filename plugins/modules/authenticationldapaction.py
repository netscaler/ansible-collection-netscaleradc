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
module: authenticationldapaction
short_description: Configuration for LDAP action resource.
description: Configuration for LDAP action resource.
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
  alternateemailattr:
    type: raw
    description:
      - The NetScaler appliance uses the alternateive email attribute to query the
        Active Directory for the alternative email id of a user
  attribute1:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute1 from the ldap response
  attribute10:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute10 from the ldap response
  attribute11:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute11 from the ldap response
  attribute12:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute12 from the ldap response
  attribute13:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute13 from the ldap response
  attribute14:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute14 from the ldap response
  attribute15:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute15 from the ldap response
  attribute16:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute16 from the ldap response
  attribute2:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute2 from the ldap response
  attribute3:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute3 from the ldap response
  attribute4:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute4 from the ldap response
  attribute5:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute5 from the ldap response
  attribute6:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute6 from the ldap response
  attribute7:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute7 from the ldap response
  attribute8:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute8 from the ldap response
  attribute9:
    type: raw
    description:
      - Expression that would be evaluated to extract attribute9 from the ldap response
  attributes:
    type: raw
    description:
      - List of attribute names separated by ',' which needs to be fetched from ldap
        server.
      - Note that preceeding and trailing spaces will be removed.
      - Attribute name can be 127 bytes and total length of this string should not
        cross 2047 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
  authentication:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform LDAP authentication.
      - If authentication is disabled, any LDAP authentication attempt returns authentication
        success if the user is found.
      - CAUTION! Authentication should be disabled only for authorization group extraction
        or where other (non-LDAP) authentication methods are in use and either bound
        to a primary list or flagged as secondary.
  authtimeout:
    type: raw
    description:
      - Number of seconds the Citrix ADC waits for a response from the RADIUS server.
  cloudattributes:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - The Citrix ADC uses the cloud attributes to extract additional attributes
        from LDAP servers required for Citrix Cloud operations
  defaultauthenticationgroup:
    type: raw
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  email:
    type: raw
    description:
      - The Citrix ADC uses the email attribute to query the Active Directory for
        the email id of a user
  followreferrals:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Setting this option to C(ON) enables following LDAP referrals received from
        the LDAP server.
  groupattrname:
    type: raw
    description:
      - LDAP group attribute name.
      - Used for group extraction on the LDAP server.
  groupnameidentifier:
    type: raw
    description:
      - Name that uniquely identifies a group in LDAP or Active Directory.
  groupsearchattribute:
    type: raw
    description:
      - LDAP group search attribute.
      - Used to determine to which groups a group belongs.
  groupsearchfilter:
    type: raw
    description:
      - String to be combined with the default LDAP group search string to form the
        search value.  For example, the group search filter ""vpnallowed=true"" when
        combined with the group identifier ""samaccount"" and the group name ""g1""
        yields the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". If nestedGroupExtraction
        is ENABLED, the filter is applied on the first level group search as well,
        otherwise first level groups (of which user is a direct member of) will be
        fetched without applying this filter. (Be sure to enclose the search string
        in two sets of double quotation marks; both sets are needed.)
  groupsearchsubattribute:
    type: raw
    description:
      - LDAP group search subattribute.
      - Used to determine to which groups a group belongs.
  kbattribute:
    type: raw
    description:
      - KnowledgeBasedAuthentication(KBA) attribute on AD. This attribute is used
        to store and retrieve preconfigured Question and Answer knowledge base used
        for KBA authentication.
  ldapbase:
    type: raw
    description:
      - Base (node) from which to start LDAP searches.
      - If the LDAP server is running locally, the default value of base is dc=netscaler,
        dc=com.
  ldapbinddn:
    type: raw
    description:
      - Full distinguished name (DN) that is used to bind to the LDAP server.
      - 'Default: cn=Manager,dc=netscaler,dc=com'
  ldapbinddnpassword:
    type: raw
    description:
      - Password used to bind to the LDAP server.
  ldaphostname:
    type: raw
    description:
      - Hostname for the LDAP server.  If -validateServerCert is ON then this must
        be the host name on the certificate from the LDAP server.
      - A hostname mismatch will cause a connection failure.
  ldaploginname:
    type: raw
    description:
      - LDAP login name attribute.
      - The Citrix ADC uses the LDAP login name to query external LDAP servers or
        Active Directories.
  maxldapreferrals:
    type: raw
    description:
      - Specifies the maximum number of nested referrals to follow.
  maxnestinglevel:
    type: raw
    description:
      - If nested group extraction is ON, specifies the number of levels up to which
        group extraction is performed.
  mssrvrecordlocation:
    type: raw
    description:
      - MSSRV Specific parameter. Used to locate the DNS node to which the SRV record
        pertains in the domainname. The domainname is appended to it to form the srv
        record.
      - 'Example : For "dc._msdcs", the srv record formed is _ldap._tcp.dc._msdcs.<domainname>.'
  name:
    type: raw
    description:
      - Name for the new LDAP action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the LDAP action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'my authentication
        action').
  nestedgroupextraction:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow nested group extraction, in which the Citrix ADC queries external LDAP
        servers to determine whether a group is part of another group.
  otpsecret:
    type: raw
    description:
      - OneTimePassword(OTP) Secret key attribute on AD. This attribute is used to
        store and retrieve secret key used for OTP check
  passwdchange:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow password change requests.
  pushservice:
    type: raw
    description:
      - Name of the service used to send push notifications
  referraldnslookup:
    type: raw
    choices:
      - A-REC
      - SRV-REC
      - MSSRV-REC
    description:
      - Specifies the DNS Record lookup Type for the referrals
  requireuser:
    type: raw
    choices:
      - 'YES'
      - 'NO'
    description:
      - Require a successful user search for authentication.
      - CAUTION!  This field should be set to C(NO) only if usersearch not required
        [Both username validation as well as password validation skipped] and (non-LDAP)
        authentication methods are in use and either bound to a primary list or flagged
        as secondary.
  searchfilter:
    type: raw
    description:
      - String to be combined with the default LDAP user search string to form the
        search value. For example, if the search filter "vpnallowed=true" is combined
        with the LDAP login name "samaccount" and the user-supplied username is "bob",
        the result is the LDAP search string ""&(vpnallowed=true)(samaccount=bob)""
        (Be sure to enclose the search string in two sets of double quotation marks;
        both sets are needed.).
  sectype:
    type: raw
    choices:
      - PLAINTEXT
      - TLS
      - SSL
    description:
      - Type of security used for communications between the Citrix ADC and the LDAP
        server. For the C(PLAINTEXT) setting, no encryption is required.
  serverip:
    type: str
    description:
      - IP address assigned to the LDAP server.
  servername:
    type: str
    description:
      - LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.
  serverport:
    type: raw
    description:
      - Port on which the LDAP server accepts connections.
  sshpublickey:
    type: str
    description:
      - SSH PublicKey is attribute on AD. This attribute is used to retrieve ssh PublicKey
        for RBA authentication
  ssonameattribute:
    type: raw
    description:
      - LDAP single signon (SSO) attribute.
      - The Citrix ADC uses the SSO name attribute to query external LDAP servers
        or Active Directories for an alternate username.
  subattributename:
    type: raw
    description:
      - LDAP group sub-attribute name.
      - Used for group extraction from the LDAP server.
  svrtype:
    type: raw
    choices:
      - AD
      - NDS
    description:
      - The type of LDAP server.
  validateservercert:
    type: raw
    choices:
      - 'YES'
      - 'NO'
    description:
      - When to validate LDAP server certs
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
