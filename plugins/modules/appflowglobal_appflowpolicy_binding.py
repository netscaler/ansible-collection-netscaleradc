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
module: appflowglobal_appflowpolicy_binding
short_description: Binding Resource definition for describing association between
  appflowglobal and appflowpolicy resources
description: Binding Resource definition for describing association between appflowglobal
  and appflowpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  globalbindtype:
    type: str
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
      - TM_GLOBAL
    description:
      - '0'
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - Invoke policies bound to a virtual server or a user-defined policy label.
        After the invoked policies are evaluated, the flow returns to the policy with
        the next priority.
  labelname:
    type: str
    description:
      - Name of the label to invoke if the current policy evaluates to TRUE.
  labeltype:
    type: str
    choices:
      - vserver
      - policylabel
    description:
      - Type of policy label to invoke. Specify C(vserver) for a policy label associated
        with a virtual server, or C(policylabel) for a user-defined policy label.
  policyname:
    type: str
    description:
      - Name of the AppFlow policy.
  priority:
    type: float
    description:
      - Specifies the priority of the policy.
  type:
    type: str
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - OVERRIDE
      - DEFAULT
      - OTHERTCP_REQ_OVERRIDE
      - OTHERTCP_REQ_DEFAULT
      - MSSQL_REQ_OVERRIDE
      - MSSQL_REQ_DEFAULT
      - MYSQL_REQ_OVERRIDE
      - MYSQL_REQ_DEFAULT
      - ICA_REQ_OVERRIDE
      - ICA_REQ_DEFAULT
      - ORACLE_REQ_OVERRIDE
      - ORACLE_REQ_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
    description:
      - Global bind point for which to show detailed information about the policies
        bound to the bind point.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appflowglobal_appflowpolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appflowglobal_appflowpolicy_binding
      delegate_to: localhost
      netscaler.adc.appflowglobal_appflowpolicy_binding:
        state: present
        policyname: ia_appflowpol12
        priority: '42'
        gotopriorityexpression: end
        type: REQ_OVERRIDE
        invoke: true
        labeltype: vserver
        labelname: cs_invoke1
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
