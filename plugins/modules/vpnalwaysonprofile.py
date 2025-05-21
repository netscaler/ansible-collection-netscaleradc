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
module: vpnalwaysonprofile
short_description: Configuration for AlwyasON profile resource.
description: Configuration for AlwyasON profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  clientcontrol:
    type: str
    choices:
      - ALLOW
      - DENY
    description:
      - Allow/Deny user to log off and connect to another Gateway
  locationbasedvpn:
    type: str
    choices:
      - Remote
      - Everywhere
    description:
      - Option to decide if tunnel should be established when in enterprise network.
        When locationBasedVPN is remote, client tries to detect if it is located in
        enterprise network or not and establishes the tunnel if not in enterprise
        network. Dns suffixes configured using -add dns suffix- are used to decide
        if the client is in the enterprise network or not. If the resolution of the
        DNS suffix results in private IP, client is said to be in enterprise network.
        When set to EveryWhere, the client skips the check to detect if it is on the
        enterprise network and tries to establish the tunnel
  name:
    type: str
    description:
      - name of AlwaysON profile
  networkaccessonvpnfailure:
    type: str
    choices:
      - onlyToGateway
      - fullAccess
    description:
      - Option to block network traffic when tunnel is not established(and the config
        requires that tunnel be established). When set to C(onlyToGateway), the network
        traffic to and from the client (except Gateway IP) is blocked. When set to
        C(fullAccess), the network traffic is not blocked
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample vpnalwaysonprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vpnalwaysonprofile
      delegate_to: localhost
      netscaler.adc.vpnalwaysonprofile:
        state: present
        name: aop1
        networkaccessonvpnfailure: fullAccess
        clientcontrol: DENY
        locationbasedvpn: Remote
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
