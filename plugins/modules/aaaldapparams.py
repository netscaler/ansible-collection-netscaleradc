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
module: aaaldapparams
short_description: Configuration for LDAP parameter resource.
description: Configuration for LDAP parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  authtimeout:
    description:
      - Maximum number of seconds that the Citrix ADC waits for a response from the
        LDAP server.
    type: float
    default: 3
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  groupattrname:
    description:
      - Attribute name used for group extraction from the LDAP server.
    type: str
  groupnameidentifier:
    description:
      - LDAP-group attribute that uniquely identifies the group. No two groups on
        one LDAP server can have the same group name identifier.
    type: str
  groupsearchattribute:
    description:
      - LDAP-group attribute that designates the parent group of the specified group.
        Use this attribute to search for a group's parent group.
    type: str
  groupsearchfilter:
    description:
      - Search-expression that can be specified for sending group-search requests
        to the LDAP server.
    type: str
  groupsearchsubattribute:
    description:
      - LDAP-group subattribute that designates the parent group of the specified
        group. Use this attribute to search for a group's parent group.
    type: str
  ldapbase:
    description:
      - 'Base (the server and location) from which LDAP search commands should start. '
      - If the LDAP server is running locally, the default value of base is dc=netscaler,
        dc=com.
    type: str
  ldapbinddn:
    description:
      - Complete distinguished name (DN) string used for binding to the LDAP server.
    type: str
  ldapbinddnpassword:
    description:
      - Password for binding to the LDAP server.
    type: str
  ldaploginname:
    description:
      - Name attribute that the Citrix ADC uses to query the external LDAP server
        or an Active Directory.
    type: str
  maxnestinglevel:
    description:
      - Number of levels up to which the system can query nested LDAP groups.
    type: float
    default: 2
  nestedgroupextraction:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Queries the external LDAP server to determine whether the specified group
        belongs to another group.
    type: str
    default: 'OFF'
  passwdchange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Accept password change requests.
    type: str
    default: DISABLED
  searchfilter:
    description:
      - 'String to be combined with the default LDAP user search string to form the
        value to use when executing an LDAP search. '
      - 'For example, the following values:'
      - vpnallowed=true,
      - ldaploginame=""samaccount""
      - 'when combined with the user-supplied username ""bob"", yield the following
        LDAP search string:'
      - '""(&(vpnallowed=true)(samaccount=bob)""'
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
    default: TLS
  serverip:
    description:
      - IP address of your LDAP server.
    type: str
  serverport:
    description:
      - Port number on which the LDAP server listens for connections.
    type: int
    default: 389
  ssonameattribute:
    description:
      - 'Attribute used by the Citrix ADC to query an external LDAP server or Active
        Directory for an alternative username. '
      - This alternative username is then used for single sign-on (SSO).
    type: str
  subattributename:
    description:
      - Subattribute name used for group extraction from the LDAP server.
    type: str
  svrtype:
    choices:
      - AD
      - NDS
    description:
      - The type of LDAP server.
    type: str
    default: AAA_LDAP_SERVER_TYPE_DEFAULT
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
