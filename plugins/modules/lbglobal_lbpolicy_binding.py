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
module: lbglobal_lbpolicy_binding
short_description: Binding Resource definition for describing association between
  lbglobal and lbpolicy resources
description: Binding Resource definition for describing association between lbglobal
  and lbpolicy resources
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
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
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label, and then forward the request to the specified
        virtual server or evaluate the specified policy label.
  labelname:
    type: str
    description:
      - Name of the virtual server or user-defined policy label to invoke if the policy
        evaluates to TRUE.
  labeltype:
    type: str
    choices:
      - reqvserver
      - policylabel
    description:
      - 'Type of invocation, Available settings function as follows:'
      - '* vserver - Invokes the unnamed policy label associated with the specified
        virtual server.'
      - '* C(policylabel) - Invoke the specified policy label.'
  policyname:
    type: str
    description:
      - Name of the LB policy.
  priority:
    type: int
    description:
      - Specifies the priority of the policy.
  type:
    type: str
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - OTHERTCP_REQ_OVERRIDE
      - OTHERTCP_REQ_DEFAULT
      - SIPUDP_REQ_OVERRIDE
      - SIPUDP_REQ_DEFAULT
      - SIPTCP_REQ_OVERRIDE
      - SIPTCP_REQ_DEFAULT
      - MSSQL_REQ_OVERRIDE
      - MSSQL_REQ_DEFAULT
      - MYSQL_REQ_OVERRIDE
      - MYSQL_REQ_DEFAULT
      - ORACLE_REQ_OVERRIDE
      - ORACLE_REQ_DEFAULT
      - NAT_REQ_OVERRIDE
      - NAT_REQ_DEFAULT
      - DIAMETER_REQ_OVERRIDE
      - DIAMETER_REQ_DEFAULT
      - RADIUS_REQ_OVERRIDE
      - RADIUS_REQ_DEFAULT
      - DNS_REQ_OVERRIDE
      - DNS_REQ_DEFAULT
      - MQTT_REQ_OVERRIDE
      - MQTT_REQ_DEFAULT
      - QUIC_OVERRIDE
      - QUIC_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
      - GSLB_REQ_OVERRIDE
      - GSLB_REQ_DEFAULT
    description:
      - '0'
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
