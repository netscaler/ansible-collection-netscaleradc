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
module: nd6ravariables
short_description: Configuration for nd6 Router Advertisment configuration variables
  resource.
description: Configuration for nd6 Router Advertisment configuration variables resource.
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
  ceaserouteradv:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Cease router advertisements on this vlan.
  currhoplimit:
    type: int
    description:
      - Current Hop limit.
  defaultlifetime:
    type: int
    description:
      - Default life time, in seconds.
  linkmtu:
    type: int
    description:
      - The Link MTU.
  managedaddrconfig:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Value to be placed in the Managed address configuration flag field.
  maxrtadvinterval:
    type: int
    description:
      - Maximum time allowed between unsolicited multicast RAs, in seconds.
  minrtadvinterval:
    type: int
    description:
      - Minimum time interval between RA messages, in seconds.
  onlyunicastrtadvresponse:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Send only Unicast Router Advertisements in respond to Router Solicitations.
  otheraddrconfig:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Value to be placed in the Other configuration flag field.
  reachabletime:
    type: int
    description:
      - Reachable time, in milliseconds.
  retranstime:
    type: int
    description:
      - Retransmission time, in milliseconds.
  sendrouteradv:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - whether the router sends periodic RAs and responds to Router Solicitations.
  srclinklayeraddroption:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Include source link layer address option in RA messages.
  vlan:
    type: int
    description:
      - The VLAN number.
  nd6ravariables_onlinkipv6prefix_binding:
    type: dict
    description: Bindings for nd6ravariables_onlinkipv6prefix_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nd6ravariables playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nd6ravariables
      delegate_to: localhost
      netscaler.adc.nd6ravariables:
        state: present
        vlan: '1'
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
