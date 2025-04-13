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
module: servicegroup_servicegroupmember_binding
short_description: Binding Resource definition for describing association between
  servicegroup and servicegroupmember resources
description: Binding Resource definition for describing association between servicegroup
  and servicegroupmember resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be updated and enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be updated and disabled on the NetScaler ADC node.
    type: str
  customserverid:
    type: str
    description:
      - The identifier for this IP:Port pair. Used when the persistency type is set
        to Custom Server ID.
  dbsttl:
    type: float
    description:
      - Specify the TTL for DNS record for domain based service.The default value
        of ttl is 0 which indicates to use the TTL received in DNS response for monitors
  hashid:
    type: float
    description:
      - The hash identifier for the service. This must be unique for each service.
        This parameter is used by hash based load balancing methods.
  ip:
    type: str
    description:
      - IP Address.
  nameserver:
    type: str
    description:
      - Specify the nameserver to which the query for bound domain needs to be sent.
        If not specified, use the global nameserver
  order:
    type: float
    description:
      - Order number to be assigned to the servicegroup member
  port:
    type: int
    description:
      - Server port number.
  serverid:
    type: float
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
  servername:
    type: str
    description:
      - Name of the server to which to bind the service group.
  servicegroupname:
    type: str
    description:
      - Name of the service group.
  weight:
    type: float
    description:
      - Weight to assign to the servers in the service group. Specifies the capacity
        of the servers relative to the other servers in the load balancing configuration.
        The higher the weight, the higher the percentage of requests sent to the service.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample servicegroup_servicegroupmember_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure servicegroup_servicegroupmember_binding
      delegate_to: localhost
      netscaler.adc.servicegroup_servicegroupmember_binding:
        state: present
        servicegroupname: CR_SVG
        ip: 172.168.1.20
        port: 80
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
