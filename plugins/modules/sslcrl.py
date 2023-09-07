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
module: sslcrl
short_description: Configuration for Certificate Revocation List resource.
description: Configuration for Certificate Revocation List resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  basedn:
    description:
      - Base distinguished name (DN), which is used in an LDAP search to search for
        a CRL. Citrix recommends searching for the Base DN instead of the Issuer Name
        from the CA certificate, because the Issuer Name field might not exactly match
        the LDAP directory structure's DN.
    type: str
  binary:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Set the LDAP-based CRL retrieval mode to binary.
    type: str
    default: 'NO'
  binddn:
    description:
      - Bind distinguished name (DN) to be used to access the CRL object in the LDAP
        repository if access to the LDAP repository is restricted or anonymous access
        is not allowed.
    type: str
  cacert:
    description:
      - CA certificate that has issued the CRL. Required if CRL Auto Refresh is selected.
        Install the CA certificate on the appliance before adding the CRL.
    type: str
  cacertfile:
    description:
      - Name of and, optionally, path to the CA certificate file.
      - /nsconfig/ssl/ is the default path.
    type: str
  cakeyfile:
    description:
      - Name of and, optionally, path to the CA key file. /nsconfig/ssl/ is the default
        path
    type: str
  crlname:
    description:
      - Name for the Certificate Revocation List (CRL). Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the CRL is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my crl" or 'my crl').
    type: str
  crlpath:
    description:
      - Path to the CRL file. /var/netscaler/ssl/ is the default path.
    type: str
  day:
    description:
      - Day on which to refresh the CRL, or, if the Interval parameter is not set,
        the number of days after which to refresh the CRL. If Interval is set to MONTHLY,
        specify the date. If Interval is set to WEEKLY, specify the day of the week
        (for example, Sun=0 and Sat=6). This parameter is not applicable if the Interval
        is set to DAILY.
    type: float
  gencrl:
    description:
      - Name of and, optionally, path to the CRL file to be generated. The list of
        certificates that have been revoked is obtained from the index file. /nsconfig/ssl/
        is the default path.
    type: str
  indexfile:
    description:
      - Name of and, optionally, path to the file containing the serial numbers of
        all the certificates that are revoked. Revoked certificates are appended to
        the file. /nsconfig/ssl/ is the default path
    type: str
  inform:
    choices:
      - DER
      - PEM
    description:
      - 'Input format of the CRL file. The two formats supported on the appliance
        are:'
      - C(PEM) - Privacy Enhanced Mail.
      - C(DER) - Distinguished Encoding Rule.
    type: str
    default: PEM
  interval:
    choices:
      - MONTHLY
      - WEEKLY
      - DAILY
      - NOW
      - NONE
    description:
      - CRL refresh interval. Use the C(NONE) setting to unset this parameter.
    type: str
  method:
    choices:
      - HTTP
      - LDAP
    description:
      - Method for CRL refresh. If C(LDAP) is selected, specify the method, CA certificate,
        base DN, port, and C(LDAP) server name. If C(HTTP) is selected, specify the
        CA certificate, method, URL, and port. Cannot be changed after a CRL is added.
    type: str
  password:
    description:
      - Password to access the CRL in the LDAP repository if access to the LDAP repository
        is restricted or anonymous access is not allowed.
    type: str
  port:
    description:
      - Port for the LDAP server.
    type: int
  refresh:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set CRL auto refresh.
    type: str
  revoke:
    description:
      - Name of and, optionally, path to the certificate to be revoked. /nsconfig/ssl/
        is the default path.
    type: str
  scope:
    choices:
      - Base
      - One
    description:
      - 'Extent of the search operation on the LDAP server. Available settings function
        as follows:'
      - C(One) - C(One) level below C(Base) DN.
      - C(Base) - Exactly the same level as C(Base) DN.
    type: str
    default: One
  server:
    description:
      - IP address of the LDAP server from which to fetch the CRLs.
    type: str
  time:
    description:
      - Time, in hours (1-24) and minutes (1-60), at which to refresh the CRL.
    type: str
  url:
    description:
      - URL of the CRL distribution point.
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
