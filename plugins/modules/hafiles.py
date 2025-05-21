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
module: hafiles
short_description: Configuration for files resource.
description: Configuration for files resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
  mode:
    type: list
    choices:
      - all
      - bookmarks
      - ssl
      - imports
      - misc
      - dns
      - krb
      - AAA
      - app_catalog
      - all_plus_misc
      - all_minus_misc
    description:
      - Specify one of the following modes of synchronization.
      - '* C(all) - Synchronize files related to system configuration, Access Gateway
        C(bookmarks), SSL certificates, SSL CRL lists,  and Application Firewall XML
        objects.'
      - '* C(bookmarks) - Synchronize C(all) Access Gateway C(bookmarks).'
      - '* C(ssl) - Synchronize C(all) certificates, keys, and CRLs for the SSL feature.'
      - '* C(imports). Synchronize C(all) XML objects (for example, WSDLs, schemas,
        error pages) configured for the application firewall.'
      - '* C(misc) - Synchronize C(all) license files and the rc.conf file.'
      - '* C(all_plus_misc) - Synchronize files related to system configuration, Access
        Gateway C(bookmarks), SSL certificates, SSL CRL lists, application firewall
        XML objects, licenses, and the rc.conf file.'
    elements: str
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
