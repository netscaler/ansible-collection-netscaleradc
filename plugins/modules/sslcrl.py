#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: sslcrl
short_description: Configuration for Certificate Revocation List resource.
description: Configuration for Certificate Revocation List resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - created
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(created), the `create` operation will be applied on the resource.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  basedn:
    type: str
    description:
      - Base distinguished name (DN), which is used in an LDAP search to search for
        a CRL. Citrix recommends searching for the Base DN instead of the Issuer Name
        from the CA certificate, because the Issuer Name field might not exactly match
        the LDAP directory structure's DN.
  binary:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Set the LDAP-based CRL retrieval mode to binary.
  binddn:
    type: str
    description:
      - Bind distinguished name (DN) to be used to access the CRL object in the LDAP
        repository if access to the LDAP repository is restricted or anonymous access
        is not allowed.
  cacert:
    type: str
    description:
      - CA certificate that has issued the CRL. Required if CRL Auto Refresh is selected.
        Install the CA certificate on the appliance before adding the CRL.
  cacertfile:
    type: str
    description:
      - Name of and, optionally, path to the CA certificate file.
      - /nsconfig/ssl/ is the default path.
  cakeyfile:
    type: str
    description:
      - Name of and, optionally, path to the CA key file. /nsconfig/ssl/ is the default
        path
  crlname:
    type: str
    description:
      - Name for the Certificate Revocation List (CRL). Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the CRL is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my crl" or 'my crl').
  crlpath:
    type: str
    description:
      - Path to the CRL file. /var/netscaler/ssl/ is the default path.
  day:
    type: int
    description:
      - Day on which to refresh the CRL, or, if the Interval parameter is not set,
        the number of days after which to refresh the CRL. If Interval is set to MONTHLY,
        specify the date. If Interval is set to WEEKLY, specify the day of the week
        (for example, Sun=0 and Sat=6). This parameter is not applicable if the Interval
        is set to DAILY.
  gencrl:
    type: str
    description:
      - Name of and, optionally, path to the CRL file to be generated. The list of
        certificates that have been revoked is obtained from the index file. /nsconfig/ssl/
        is the default path.
  indexfile:
    type: str
    description:
      - Name of and, optionally, path to the file containing the serial numbers of
        all the certificates that are revoked. Revoked certificates are appended to
        the file. /nsconfig/ssl/ is the default path
  inform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - 'Input format of the CRL file. The two formats supported on the appliance
        are:'
      - C(PEM) - Privacy Enhanced Mail.
      - C(DER) - Distinguished Encoding Rule.
  interval:
    type: str
    choices:
      - MONTHLY
      - WEEKLY
      - DAILY
      - NOW
      - NONE
    description:
      - CRL refresh interval. Use the C(NONE) setting to unset this parameter.
  method:
    type: str
    choices:
      - HTTP
      - LDAP
    description:
      - Method for CRL refresh. If C(LDAP) is selected, specify the method, CA certificate,
        base DN, port, and C(LDAP) server name. If C(HTTP) is selected, specify the
        CA certificate, method, URL, and port. Cannot be changed after a CRL is added.
  password:
    type: str
    description:
      - Password to access the CRL in the LDAP repository if access to the LDAP repository
        is restricted or anonymous access is not allowed.
  port:
    type: int
    description:
      - Port for the LDAP server.
  refresh:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set CRL auto refresh.
  revoke:
    type: str
    description:
      - Name of and, optionally, path to the certificate to be revoked. /nsconfig/ssl/
        is the default path.
  scope:
    type: str
    choices:
      - Base
      - One
    description:
      - 'Extent of the search operation on the LDAP server. Available settings function
        as follows:'
      - C(One) - C(One) level below C(Base) DN.
      - C(Base) - Exactly the same level as C(Base) DN.
  server:
    type: str
    description:
      - IP address of the LDAP server from which to fetch the CRLs.
  time:
    type: str
    description:
      - Time, in hours (1-24) and minutes (1-60), at which to refresh the CRL.
  url:
    type: str
    description:
      - URL of the CRL distribution point.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslcrl playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslcrl
      delegate_to: localhost
      netscaler.adc.sslcrl:
        state: present
        crlname: crl_test_ldap1
        refresh: ENABLED
        cacert: ssl_cacert
        server: 2.2.2.10
        method: LDAP
        port: 389
        basedn: cn=ldap_new_crl_pem,ou=dsd,o=ns,c=in
        scope: Base
        day: '23'
        time: 00:01
        binddn: cn=Manager,dc=netscaler,dc=com
        password: free
        binary: 'YES'
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
