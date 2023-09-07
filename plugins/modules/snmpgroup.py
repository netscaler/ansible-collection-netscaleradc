#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: snmpgroup
short_description: Configuration for SNMP group resource.
description: Configuration for SNMP group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - 'Name for the SNMPv3 group. Can consist of 1 to 31 characters that include
        uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound
        (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You
        should choose a name that helps identify the SNMPv3 group. '
      - '            '
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my name" or 'my name').
    type: str
  readviewname:
    description:
      - Name of the configured SNMPv3 view that you want to bind to this SNMPv3 group.
        An SNMPv3 user bound to this group can access the subtrees that are bound
        to this SNMPv3 view as type INCLUDED, but cannot access the ones that are
        type EXCLUDED. If the Citrix ADC has multiple SNMPv3 view entries with the
        same name, all such entries are associated with the SNMPv3 group.
    type: str
  securitylevel:
    choices:
      - noAuthNoPriv
      - authNoPriv
      - authPriv
    description:
      - 'Security level required for communication between the Citrix ADC and the
        SNMPv3 users who belong to the group. Specify one of the following options:'
      - C(noAuthNoPriv). Require neither authentication nor encryption.
      - C(authNoPriv). Require authentication but no encryption.
      - C(authPriv). Require authentication and encryption.
      - 'Note: If you specify authentication, you must specify an encryption algorithm
        when you assign an SNMPv3 user to the group. If you also specify encryption,
        you must assign both an authentication and an encryption algorithm for each
        group member.'
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | snmpgroup
      delegate_to: localhost
      netscaler.adc.snmpgroup:
        state: present
        name: v3_grp
        securitylevel: noAuthNoPriv
        readviewname: v3_grp_view

"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
