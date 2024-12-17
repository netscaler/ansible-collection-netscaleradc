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
module: appfwhtmlerrorpage
short_description: Configuration for HTML error page resource.
description: Configuration for HTML error page resource.
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
  comment:
    type: str
    description:
      - Any comments to preserve information about the HTML error object.
  name:
    type: str
    description:
      - Name of the XML error object to remove.
  overwrite:
    type: bool
    description:
      - Overwrite any existing HTML error object of the same name.
  src:
    type: str
    description:
      - URL (protocol, host, path, and name) for the location at which to store the
        imported HTML error object.
      - 'NOTE: The import fails if the object to be imported is on an HTTPS server
        that requires client certificate authentication for access.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appfwhtmlerrorpage playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwhtmlerrorpage
      delegate_to: localhost
      netscaler.adc.appfwhtmlerrorpage:

        state: present
        src: http://10.217.30.16/testsite/Signatures/44_38_1_36/credit_card.html
        name: Html_ Error_2
        nitro_operation: import
        '#nitro_operation': import
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
