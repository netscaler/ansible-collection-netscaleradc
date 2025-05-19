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
module: forwardingsession
short_description: Configuration for session forward resource.
description: Configuration for session forward resource.
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
  acl6name:
    type: str
    description:
      - Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is
        used as a forwarding session rule.
  aclname:
    type: str
    description:
      - Name of any configured ACL whose action is ALLOW. The rule of the ACL is used
        as a forwarding session rule.
  connfailover:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Synchronize connection information with the secondary appliance in a high
        availability (HA) pair. That is, synchronize all connection-related information
        for the forwarding session.
  name:
    type: str
    description:
      - Name for the forwarding session rule. Can begin with a letter, number, or
        the underscore character (_), and can consist of letters, numbers, and the
        hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:),
        and underscore characters. Cannot be changed after the rule is created.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my rule" or 'my rule').
  netmask:
    type: str
    description:
      - Subnet mask associated with the network.
  network:
    type: str
    description:
      - An IPv4 network address or IPv6 prefix of a network from which the forwarded
        traffic originates or to which it is destined.
  processlocal:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enabling this option on forwarding session will not steer the packet to flow
        processor. Instead, packet will be routed.
  sourceroutecache:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Cache the source ip address and mac address of the DA servers.
  td:
    type: int
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample forwardingsession playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure forwardingsession
      delegate_to: localhost
      netscaler.adc.forwardingsession:
        state: present
        name: ia_forsess5
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
