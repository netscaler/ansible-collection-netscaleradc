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
module: lbvserver_cmppolicy_binding
short_description: Binding Resource definition for describing association between
  lbvserver and cmppolicy resources
description: Binding Resource definition for describing association between lbvserver
  and cmppolicy resources
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
  bindpoint:
    type: str
    choices:
      - REQUEST
      - RESPONSE
      - MQTT_JUMBO_REQ
    description:
      - The bindpoint to which the policy is bound
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  invoke:
    type: bool
    description:
      - Invoke policies bound to a virtual server or policy label.
  labelname:
    type: str
    description:
      - Name of the label invoked.
  labeltype:
    type: str
    choices:
      - reqvserver
      - resvserver
      - policylabel
    description:
      - The invocation type.
  name:
    type: str
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
  order:
    type: int
    description:
      - Integer specifying the order of the service. A larger number specifies a lower
        order. Defines the order of the service relative to the other services in
        the load balancing vserver's bindings. Determines the priority given to the
        service among all the services bound.
  policyname:
    type: str
    description:
      - Name of the policy bound to the LB vserver.
  priority:
    type: int
    description:
      - Priority.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lbvserver_cmppolicy_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lbvserver_cmppolicy_binding
      delegate_to: localhost
      netscaler.adc.lbvserver_cmppolicy_binding:
        state: present
        name: Base_v-cmp
        policyname: Base_cmp_mypolicy
        priority: '1'
        gotopriorityexpression: next
        bindpoint: RESPONSE
        invoke: true
        labeltype: policylabel
        labelname: Base_cmp_pol_label
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
