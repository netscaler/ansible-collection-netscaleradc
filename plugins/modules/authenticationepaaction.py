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
module: authenticationepaaction
short_description: Configuration for epa action resource.
description: Configuration for epa action resource.
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
  csecexpr:
    type: str
    description:
      - it holds the ClientSecurityExpression to be sent to the client
  defaultepagroup:
    type: str
    description:
      - This is the default group that is chosen when the EPA check succeeds.
  deletefiles:
    type: str
    description:
      - String specifying the path(s) and name(s) of the files to be deleted by the
        endpoint analysis (EPA) tool. Multiple files to be delimited by comma
  deviceposture:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to enable/disable device posture service scan
  killprocess:
    type: str
    description:
      - String specifying the name of a process to be terminated by the endpoint analysis
        (EPA) tool. Multiple processes to be delimited by comma
  name:
    type: str
    description:
      - Name for the epa action. Must begin with a
      - "\t    letter, number, or the underscore character (_), and must consist"
      - "\t    only of letters, numbers, and the hyphen (-), period (.) pound"
      - "\t    (#), space ( ), at (@), equals (=), colon (:), and underscore"
      - "\t\t    characters. Cannot be changed after epa action is created.The following\
        \ requirement applies only to the Citrix ADC CLI:If the name includes one\
        \ or more spaces, enclose the name in double or single quotation marks (for\
        \ example, \"my aaa action\" or 'my aaa action')."
  quarantinegroup:
    type: str
    description:
      - This is the quarantine group that is chosen when the EPA check fails
      - if configured.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample authenticationepaaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure authenticationepaaction
      delegate_to: localhost
      netscaler.adc.authenticationepaaction:
        state: present
        name: EPA_ACT2
        csecexpr: sys.client_expr("proc_0_perl")
        killprocess: process2
        deletefiles: file2
        defaultepagroup: DG2
        quarantinegroup: QG2
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
