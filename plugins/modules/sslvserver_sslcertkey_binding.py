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
module: sslvserver_sslcertkey_binding
short_description: Binding Resource definition for describing association between
  sslvserver and sslcertkey resources
description: Binding Resource definition for describing association between sslvserver
  and sslcertkey resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ca:
    description:
      - CA certificate.
    type: bool
  certkeyname:
    description:
      - The name of the certificate key pair binding.
    type: str
  crlcheck:
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the CRL check parameter. (C(Mandatory)/C(Optional))
    type: str
  ocspcheck:
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the OCSP check parameter. (C(Mandatory)/C(Optional))
    type: str
  skipcaname:
    description:
      - The flag is used to indicate whether this particular CA certificate's CA_Name
        needs to be sent to the SSL client while requesting for client certificate
        in a SSL handshake
    type: bool
  snicert:
    description:
      - The name of the CertKey. Use this option to bind Certkey(s) which will be
        used in SNI processing.
    type: bool
  vservername:
    description:
      - Name of the SSL virtual server.
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
