#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: ping
short_description: Configuration for 0 resource.
description: Configuration for 0 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices: []
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
  interface:
    type: str
    description:
      - Network interface on which to ping, if you have multiple interfaces.
      - 'Deprecated alias: C(I).'
  source_ip:
    type: str
    description:
      - Source IP address to be used in the outgoing query packets. If the IP addrESS
        does not belongs to this appliance, an error is returned and nothing is sent.
      - 'Deprecated alias: C(S).'
  traffic_domain:
    type: int
    description:
      - Traffic Domain Id
      - 'Deprecated alias: C(T).'
  c:
    type: int
    description:
      - Number of packets to send. The default value is infinite. For Nitro API, defalut
        value is taken as 5.
  hostName:
    type: str
    description:
      - Address of host to ping.
  interval:
    type: int
    description:
      - Waiting time, in seconds. The default value is 1 second.
      - 'Deprecated alias: C(i).'
  n:
    type: bool
    description:
      - Numeric output only. No name resolution.
  p:
    type: str
    description:
      - Pattern to fill in packets.  Can be up to 16 bytes, useful for diagnosing
        data-dependent problems.
  q:
    type: bool
    description:
      - Quiet output. Only the summary is printed. For Nitro API, this flag is set
        by default.
  packet_size:
    type: int
    description:
      - Data size, in bytes. The default value is 56.
      - 'Deprecated alias: C(s).'
  timeout:
    type: int
    description:
      - Time-out, in seconds, before ping exits.
      - 'Deprecated alias: C(t).'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample ping playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Ping a host from the NetScaler ADC
      delegate_to: localhost
      register: ping_result
      netscaler.adc.ping:
        state: present
        hostName: 127.0.0.1
        c: 4                # number of packets to send
        packet_size: 56     # data size in bytes (deprecated alias: s)
        interval: 1         # seconds between packets (deprecated alias: i)
        timeout: 5          # seconds before ping exits (deprecated alias: t)

    - name: Show the ping command output
      delegate_to: localhost
      ansible.builtin.debug:
        msg: "{{ ping_result.ping.response }}"
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
ping:
  description: Result of the ping command. The command output is in the C(response) field.
  returned: on success (not in check mode)
  type: dict
  sample: {'response': 'PING 127.0.0.1 (127.0.0.1): 56 data bytes\n64 bytes from 127.0.0.1:
      icmp_seq=0 ttl=64 time=0.045 ms\n\n--- 127.0.0.1 ping statistics ---\n3 packets
      transmitted, 3 packets received, 0.0% packet loss'}
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
