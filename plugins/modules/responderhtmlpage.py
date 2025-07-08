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
module: responderhtmlpage
short_description: Configuration for Responder HTML page resource.
description: Configuration for Responder HTML page resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - absent
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
    type: str
  cacertfile:
    type: str
    description:
      - CA certificate file name which will be used to verify the peer's certificate.
        The certificate should be imported using "import ssl certfile" CLI command
        or equivalent in API or GUI. If certificate name is not configured, then default
        root CA certificates are used for peer's certificate verification.
  comment:
    type: str
    description:
      - Any comments to preserve information about the HTML page object.
  name:
    type: str
    description:
      - Name to assign to the HTML page object on the Citrix ADC.
  overwrite:
    type: bool
    description:
      - Overwrites the existing file
  src:
    type: str
    description:
      - Local path or URL (protocol, host, path, and file name) for the file from
        which to retrieve the imported HTML page.
      - 'NOTE: The import fails if the object to be imported is on an HTTPS server
        that requires client certificate authentication for access.'
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
