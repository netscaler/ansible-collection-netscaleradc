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
module: appfwsignatures
short_description: Configuration for application firewall signatures XML configuration
  resource.
description: Configuration for application firewall signatures XML configuration resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - absent
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  action:
    type: list
    choices:
      - none
      - block
      - log
      - stats
    description:
      - Signature action
    elements: str
  autoenablenewsignatures:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Flag used to enable/disable auto enable new signatures
    default: 'OFF'
  category:
    type: str
    description:
      - Signature category to be Enabled/Disabled
  comment:
    type: str
    description:
      - Any comments to preserve information about the signatures object.
  enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Flag used to enable/disable enable signature rule IDs/Signature Category
    default: 'ON'
  merge:
    type: bool
    description:
      - Merges the existing Signature with new signature rules
  mergedefault:
    type: bool
    description:
      - Merges signature file with default signature file.
  name:
    type: str
    description:
      - Name of the signature object.
  overwrite:
    type: bool
    description:
      - Overwrite any existing signatures object of the same name.
  preservedefactions:
    type: bool
    description:
      - preserves def actions of signature rules
  ruleid:
    type: list
    description:
      - Signature rule IDs to be Enabled/Disabled
    elements: int
  sha1:
    type: str
    description:
      - File path for sha1 file to validate signature file
  src:
    type: str
    description:
      - URL (protocol, host, path, and file name) for the location at which to store
        the imported signatures object.
      - 'NOTE: The import fails if the object to be imported is on an HTTPS server
        that requires client certificate authentication for access.'
  vendortype:
    type: str
    choices:
      - Snort
    description:
      - Third party vendor type for which WAF signatures has to be generated.
  xslt:
    type: str
    description:
      - XSLT file source.
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
