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
module: snmpoption
short_description: Configuration for SNMP option resource.
description: Configuration for SNMP option resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  partitionnameintrap:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send partition name as a varbind in traps. By default the partition names
        are not sent as a varbind.
  severityinfointrap:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - By default, the severity level info of the trap is not mentioned in the trap
        message. Enable this option to send severity level of trap as one of the varbind
        in the trap message.
  snmpset:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Accept SNMP SET requests sent to the Citrix ADC, and allow SNMP managers to
        write values to MIB objects that are configured for write access.
  snmptraplogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log any SNMP trap events (for SNMP alarms in which logging is enabled) even
        if no trap listeners are configured. With the default setting, SNMP trap events
        are logged if at least one trap listener is configured on the appliance.
  snmptraplogginglevel:
    type: str
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
    description:
      - Audit log level of SNMP trap logs. The default value is C(INFORMATIONAL).
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
