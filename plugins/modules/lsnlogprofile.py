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
module: lsnlogprofile
short_description: Configuration for LSN logging Profile resource.
description: Configuration for LSN logging Profile resource.
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
  analyticsprofile:
    type: str
    description:
      - Name of the Analytics Profile attached to this lsn profile.
  logcompact:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Logs in Compact Logging format if option is enabled.
  logipfix:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Logs in IPFIX  format if option is enabled.
  logprofilename:
    type: str
    description:
      - The name of the logging Profile.
  logsessdeletion:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - LSN Session deletion will not be logged if disabled.
  logsubscrinfo:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Subscriber ID information is logged if option is enabled.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lsnlogprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lsnlogprofile
      delegate_to: localhost
      netscaler.adc.lsnlogprofile:
        state: present
        logprofilename: msd
        logsubscrinfo: ENABLED
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
