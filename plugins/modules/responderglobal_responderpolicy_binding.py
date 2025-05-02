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
module: responderglobal_responderpolicy_binding
short_description: Binding Resource definition for describing association between
  responderglobal and responderpolicy resources
description: Binding Resource definition for describing association between responderglobal
  and responderpolicy resources
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
      - If the current policy evaluates to TRUE, terminate evaluation of policies
        bound to the current policy label, and then forward the request to the specified
        virtual server or evaluate the specified policy label.
  labelname:
    type: str
    description:
      - Name of the policy label to invoke. If the current policy evaluates to TRUE,
        the invoke parameter is set, and Label Type is policylabel.
  labeltype:
    type: str
    choices:
      - vserver
      - policylabel
    description:
      - 'Type of invocation, Available settings function as follows:'
      - '* C(vserver) - Forward the request to the specified virtual server.'
      - '* C(policylabel) - Invoke the specified policy label.'
  policyname:
    type: str
    description:
      - Name of the responder policy.
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
      - SIPUDP_REQ_OVERRIDE
      - SIPUDP_REQ_DEFAULT
      - SIPTCP_REQ_OVERRIDE
      - SIPTCP_REQ_DEFAULT
      - MSSQL_REQ_OVERRIDE
      - MSSQL_REQ_DEFAULT
      - MYSQL_REQ_OVERRIDE
      - MYSQL_REQ_DEFAULT
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
      - MQTT_JUMBO_REQ_OVERRIDE
      - MQTT_JUMBO_REQ_DEFAULT
      - QUIC_OVERRIDE
      - QUIC_DEFAULT
      - HTTPQUIC_REQ_OVERRIDE
      - HTTPQUIC_REQ_DEFAULT
    description:
      - 'Specifies the bind point whose policies you want to display. Available settings
        function as follows:'
      - '* C(REQ_OVERRIDE) - Request override. Binds the policy to the priority request
        queue.'
      - '* C(REQ_DEFAULT) - Binds the policy to the default request queue.'
      - '* C(OTHERTCP_REQ_OVERRIDE) - Binds the policy to the non-HTTP TCP priority
        request queue.'
      - '* C(OTHERTCP_REQ_DEFAULT) - Binds the policy to the non-HTTP TCP default
        request queue..'
      - '* C(SIPUDP_REQ_OVERRIDE) - Binds the policy to the SIP UDP priority response
        queue..'
      - '* C(SIPUDP_REQ_DEFAULT) - Binds the policy to the SIP UDP default response
        queue.'
      - '* C(RADIUS_REQ_OVERRIDE) - Binds the policy to the RADIUS priority response
        queue..'
      - '* C(RADIUS_REQ_DEFAULT) - Binds the policy to the RADIUS default response
        queue.'
      - '* C(MSSQL_REQ_OVERRIDE) - Binds the policy to the Microsoft SQL priority
        response queue..'
      - '* C(MSSQL_REQ_DEFAULT) - Binds the policy to the Microsoft SQL default response
        queue.'
      - '* C(MYSQL_REQ_OVERRIDE) - Binds the policy to the MySQL priority response
        queue.'
      - '* C(MYSQL_REQ_DEFAULT) - Binds the policy to the MySQL default response queue.'
      - '* C(HTTPQUIC_REQ_OVERRIDE) - Binds the policy to the HTTP_QUIC override response
        queue.'
      - '* C(HTTPQUIC_REQ_DEFAULT) - Binds the policy to the HTTP_QUIC default response
        queue.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample responderglobal_responderpolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure responderglobal_responderpolicy_binding
      delegate_to: localhost
      netscaler.adc.responderglobal_responderpolicy_binding:
        state: present
        policyname: policy_1
        priority: '10'
        gotopriorityexpression: END
        type: DNS_REQ_DEFAULT
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
