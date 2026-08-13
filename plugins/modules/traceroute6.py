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
module: traceroute6
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
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
  I:
    type: bool
    description:
      - Use ICMP ECHO for probes.
  T:
    type: int
    description:
      - Traffic Domain Id
  host:
    type: str
    description:
      - Destination host IP address or name.
  m:
    type: int
    description:
      - Maximum hop value for outgoing probe packets. For Nitro API, default value
        is taken as 10.
  n:
    type: bool
    description:
      - Print hop addresses numerically rather than symbolically and numerically.
  p:
    type: int
    description:
      - Base port number used in probes.
  packetlen:
    type: int
    description:
      - Length (in bytes) of the query packets.
  q:
    type: int
    description:
      - Number of probes per hop. For Nitro API, default value is taken as 1.
  r:
    type: bool
    description:
      - Bypass normal routing tables and send directly to a host on an attached network.
        If the host is not on a directly attached network, an error is returned.
  s:
    type: str
    description:
      - Source IP address to use in the outgoing query packets. If the IP address
        does not belong to this appliance,  an error is returned and nothing is sent.
  v:
    type: bool
    description:
      - Verbose output. List received ICMP packets other than TIME_EXCEEDED and UNREACHABLE.
  w:
    type: int
    description:
      - Time (in seconds) to wait for a response to a query. For Nitro API, defalut
        value is set to 3.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample traceroute6 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Traceroute to an IPv6 host from the NetScaler ADC
      delegate_to: localhost
      register: traceroute6_result
      netscaler.adc.traceroute6:
        state: present
        host: "::1"
        m: 10                # maximum hop value
        q: 1                 # probes per hop

    - name: Show the traceroute6 command output
      delegate_to: localhost
      ansible.builtin.debug:
        var: traceroute6_result.traceroute6
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
traceroute6:
  description: Result of the traceroute6 command. The command output is in the C(response) field.
  returned: on success (not in check mode)
  type: dict
  sample: {'response': 'traceroute6 to ::1 (::1) from ::1, 10 hops max, 12 byte packets\n
      1  ::1 (::1)  0.512 ms  0.498 ms  0.489 ms'}
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
