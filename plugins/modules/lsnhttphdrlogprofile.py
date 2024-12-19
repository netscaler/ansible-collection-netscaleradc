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
module: lsnhttphdrlogprofile
short_description: Configuration for LSN HTTP header logging Profile resource.
description: Configuration for LSN HTTP header logging Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  httphdrlogprofilename:
    type: str
    description:
      - The name of the HTTP header logging Profile.
  loghost:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Host information is logged if option is enabled.
  logmethod:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - HTTP method information is logged if option is enabled.
  logurl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - URL information is logged if option is enabled.
  logversion:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Version information is logged if option is enabled.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lsnhttphdrlogprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lsnhttphdrlogprofile
      delegate_to: localhost
      netscaler.adc.lsnhttphdrlogprofile:
        state: present
        httphdrlogprofilename: httplog
        logurl: ENABLED
        logmethod: ENABLED
        logversion: ENABLED
        loghost: ENABLED
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
