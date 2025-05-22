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
module: rewriteglobal_rewritepolicy_binding
short_description: Binding Resource definition for describing association between
  rewriteglobal and rewritepolicy resources
description: Binding Resource definition for describing association between rewriteglobal
  and rewritepolicy resources
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
      - Terminate evaluation of policies bound to the current policy label, and then
        forward the request to the specified virtual server or evaluate the specified
        policy label.
  labelname:
    type: str
    description:
      - '* If labelType is policylabel, name of the policy label to invoke. '
      - '* If labelType is reqvserver or resvserver, name of the virtual server to
        which to forward the request of response.'
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - 'Type of invocation. Available settings function as follows:'
      - '* C(reqvserver) - Forward the request to the specified request virtual server.'
      - '* C(resvserver) - Forward the response to the specified response virtual
        server.'
      - '* C(policylabel) - Invoke the specified policy label.'
  policyname:
    type: str
    description:
      - Name of the rewrite policy.
  priority:
    type: int
    description:
      - Specifies the priority of the policy.
  type:
    type: str
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - RES_OVERRIDE
      - RES_DEFAULT
      - OTHERTCP_REQ_OVERRIDE
      - OTHERTCP_REQ_DEFAULT
      - OTHERTCP_RES_OVERRIDE
      - OTHERTCP_RES_DEFAULT
      - SIPUDP_REQ_OVERRIDE
      - SIPUDP_REQ_DEFAULT
      - SIPUDP_RES_OVERRIDE
      - SIPUDP_RES_DEFAULT
      - SIPTCP_REQ_OVERRIDE
      - SIPTCP_REQ_DEFAULT
      - SIPTCP_RES_OVERRIDE
      - SIPTCP_RES_DEFAULT
      - DIAMETER_REQ_OVERRIDE
      - DIAMETER_REQ_DEFAULT
      - DIAMETER_RES_OVERRIDE
      - DIAMETER_RES_DEFAULT
      - RADIUS_REQ_OVERRIDE
      - RADIUS_REQ_DEFAULT
      - RADIUS_RES_OVERRIDE
      - RADIUS_RES_DEFAULT
      - DNS_REQ_OVERRIDE
      - DNS_REQ_DEFAULT
      - DNS_RES_OVERRIDE
      - DNS_RES_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
      - HTTPQUIC_RES_OVERRIDE
      - HTTPQUIC_RES_DEFAULT
      - MQTT_REQ_OVERRIDE
      - MQTT_REQ_DEFAULT
      - MQTT_RES_OVERRIDE
      - MQTT_RES_DEFAULT
    description:
      - The bindpoint to which to policy is bound.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample rewriteglobal_rewritepolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure rewriteglobal_rewritepolicy_binding
      delegate_to: localhost
      netscaler.adc.rewriteglobal_rewritepolicy_binding:
        state: present
        policyname: new_policy_2
        priority: '11'
        gotopriorityexpression: END
        type: DNS_RES_DEFAULT
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
