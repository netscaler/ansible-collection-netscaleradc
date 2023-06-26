#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: lbmonitor_sslcertkey_binding
short_description: Binding Resource definition for describing association between
  lbmonitor and sslcertkey resources
description: Binding Resource definition for describing association between lbmonitor
  and sslcertkey resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ca:
    description:
      - The rule for use of CRL corresponding to this CA certificate during client
        authentication. If crlCheck is set to Mandatory, the system will deny all
        SSL clients if the CRL is missing, expired - NextUpdate date is in the past,
        or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional,
        the system will allow SSL clients in the above error cases.However, in any
        case if the client certificate is revoked in the CRL, the SSL client will
        be denied access.
    type: bool
  certkeyname:
    description:
      - The name of the certificate bound to the monitor.
    type: str
  crlcheck:
    description:
      - The state of the CRL check parameter. (Mandatory/Optional)
    type: str
    choices:
      - Mandatory
      - Optional
  monitorname:
    description:
      - Name of the monitor.
    type: str
  ocspcheck:
    description:
      - The state of the OCSP check parameter. (Mandatory/Optional)
    type: str
    choices:
      - Mandatory
      - Optional
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