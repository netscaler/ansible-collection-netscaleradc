#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: appflowglobal_appflowpolicy_binding
short_description: Binding Resource definition for describing association between
  appflowglobal and appflowpolicy resources
description: Binding Resource definition for describing association between appflowglobal
  and appflowpolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  globalbindtype:
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
    description:
      - '0'
    type: str
    default: SYSTEM_GLOBAL
  gotopriorityexpression:
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
    type: str
  invoke:
    description:
      - Invoke policies bound to a virtual server or a user-defined policy label.
        After the invoked policies are evaluated, the flow returns to the policy with
        the next priority.
    type: bool
  labelname:
    description:
      - Name of the label to invoke if the current policy evaluates to TRUE.
    type: str
  labeltype:
    choices:
      - vserver
      - policylabel
    description:
      - Type of policy label to invoke. Specify C(vserver) for a policy label associated
        with a virtual server, or C(policylabel) for a user-defined policy label.
    type: str
  policyname:
    description:
      - Name of the AppFlow policy.
    type: str
  priority:
    description:
      - Specifies the priority of the policy.
    type: int
  type:
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
