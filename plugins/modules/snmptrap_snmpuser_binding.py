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
module: snmptrap_snmpuser_binding
short_description: Binding Resource definition for describing association between
  snmptrap and snmpuser resources
description: Binding Resource definition for describing association between snmptrap
  and snmpuser resources
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
  securitylevel:
    type: str
    choices:
      - noAuthNoPriv
      - authNoPriv
      - authPriv
    description:
      - Security level of the SNMPv3 trap.
  td:
    type: int
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  trapclass:
    type: str
    choices:
      - generic
      - specific
    description:
      - 'Type of trap messages that the Citrix ADC sends to the trap listener: Generic
        or the enterprise-C(specific) messages defined in the MIB file.'
  trapdestination:
    type: str
    description:
      - IPv4 or the IPv6 address of the trap listener to which the Citrix ADC is to
        send SNMP trap messages.
  username:
    type: str
    description:
      - Name of the SNMP user that will send the SNMPv3 traps.
  version:
    type: str
    choices:
      - V1
      - V2
      - V3
    description:
      - 'SNMP version, which determines the format of trap messages sent to the trap
        listener. '
      - This setting must match the setting on the trap listener. Otherwise, the listener
        drops the trap messages.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
