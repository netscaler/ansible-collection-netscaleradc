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
module: nsrpcnode
short_description: Configuration for rpc node resource.
description: Configuration for rpc node resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  ipaddress:
    type: str
    description:
      - IP address of the node. This has to be in the same subnet as the NSIP address.
  password:
    type: str
    description:
      - Password to be used in authentication with the peer system node.
  secure:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - State of the channel when talking to the node.
  srcip:
    type: str
    description:
      - Source IP address to be used to communicate with the peer system node. The
        default value is 0, which means that the appliance uses the NSIP address as
        the source IP address.
  validatecert:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - validate the server certificate for secure SSL connections
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nsrpcnode playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nsrpcnode
      delegate_to: localhost
      netscaler.adc.nsrpcnode:
        state: present
        ipaddress: 10.76.126.5
        password: REQ_PASSWORD
        srcip: '*'
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
