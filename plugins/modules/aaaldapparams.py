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
  authtimeout:
    type: float
    description:
      - Maximum number of seconds that the Citrix ADC waits for a response from the
        LDAP server.
  defaultauthenticationgroup:
    type: str
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  groupattrname:
    type: str
    description:
      - Attribute name used for group extraction from the LDAP server.
  groupnameidentifier:
    type: str
    description:
      - LDAP-group attribute that uniquely identifies the group. No two groups on
        one LDAP server can have the same group name identifier.
  groupsearchattribute:
    type: str
    description:
      - LDAP-group attribute that designates the parent group of the specified group.
        Use this attribute to search for a group's parent group.
  groupsearchfilter:
    type: str
    description:
      - Search-expression that can be specified for sending group-search requests
        to the LDAP server.
  groupsearchsubattribute:
    type: str
    description:
      - LDAP-group subattribute that designates the parent group of the specified
        group. Use this attribute to search for a group's parent group.
  ldapbase:
    type: str
    description:
      - Base (the server and location) from which LDAP search commands should start.
      - If the LDAP server is running locally, the default value of base is dc=netscaler,
        dc=com.
  ldapbinddn:
    type: str
    description:
      - Complete distinguished name (DN) string used for binding to the LDAP server.
  ldapbinddnpassword:
    type: str
    description:
      - Password for binding to the LDAP server.
  ldaploginname:
    type: str
    description:
      - Name attribute that the Citrix ADC uses to query the external LDAP server
        or an Active Directory.
  maxnestinglevel:
    type: float
    description:
      - Number of levels up to which the system can query nested LDAP groups.
  nestedgroupextraction:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Queries the external LDAP server to determine whether the specified group
        belongs to another group.
  passwdchange:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Accept password change requests.
  searchfilter:
    type: str
    description:
      - String to be combined with the default LDAP user search string to form the
        value to use when executing an LDAP search.
      - 'For example, the following values:'
      - vpnallowed=true,
      - ldaploginame=""samaccount""
      - 'when combined with the user-supplied username ""bob"", yield the following
        LDAP search string:'
      - '""(&(vpnallowed=true)(samaccount=bob)""'
  sectype:
    type: str
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
      - IP address of your LDAP server.
  serverport:
    type: int
    description:
      - Port number on which the LDAP server listens for connections.
  ssonameattribute:
    type: str
    description:
      - Attribute used by the Citrix ADC to query an external LDAP server or Active
        Directory for an alternative username.
      - This alternative username is then used for single sign-on (SSO).
  subattributename:
    type: str
    description:
      - Subattribute name used for group extraction from the LDAP server.
  svrtype:
    type: str
    choices:
      - AD
      - NDS
    description:
      - The type of LDAP server.
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
