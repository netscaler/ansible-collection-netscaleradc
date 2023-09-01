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
module: snmptrap
short_description: Configuration for snmp trap resource.
description: Configuration for snmp trap resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  allpartitions:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send traps of all partitions to this destination.
    type: str
    default: DISABLED
  communityname:
    description:
      - 'Password (string) sent with the trap messages, so that the trap listener
        can authenticate them. Can include 1 to 31 uppercase or lowercase letters,
        numbers, and hyphen (-), period (.) pound (#), space ( ), at (@), equals (=),
        colon (:), and underscore (_) characters.  '
      - You must specify the same community string on the trap listener device. Otherwise,
        the trap listener drops the trap messages.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the string includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my string" or 'my string').
    type: str
  destport:
    description:
      - UDP port at which the trap listener listens for trap messages. This setting
        must match the setting on the trap listener. Otherwise, the listener drops
        the trap messages.
    type: int
    default: 162
  severity:
    choices:
      - Critical
      - Major
      - Minor
      - Warning
      - Informational
    description:
      - 'Severity level at or above which the Citrix ADC sends trap messages to this
        trap listener. The severity levels, in increasing order of severity, are C(Informational),
        C(Warning), C(Minor), C(Major), C(Critical). This parameter can be set for
        trap listeners of type SPECIFIC only. The default is to send all levels of
        trap messages. '
      - 'Important: Trap messages are not assigned severity levels unless you specify
        severity levels when configuring SNMP alarms.'
    type: str
    default: Unknown
  srcip:
    description:
      - IPv4 or IPv6 address that the Citrix ADC inserts as the source IP address
        in all SNMP trap messages that it sends to this trap listener. By default
        this is the appliance's NSIP or NSIP6 address, but you can specify an IPv4
        MIP or SNIP/SNIP6 address. In cluster setup, the default value is the individual
        node's NSIP, but it can be set to CLIP or Striped SNIP address. In non default
        partition, this parameter must be set to the SNIP/SNIP6 address.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: float
  trapclass:
    choices:
      - generic
      - specific
    description:
      - 'Type of trap messages that the Citrix ADC sends to the trap listener: Generic
        or the enterprise-C(specific) messages defined in the MIB file.'
    type: str
  trapdestination:
    description:
      - IPv4 or the IPv6 address of the trap listener to which the Citrix ADC is to
        send SNMP trap messages.
    type: str
  version:
    choices:
      - V1
      - V2
      - V3
    description:
      - 'SNMP version, which determines the format of trap messages sent to the trap
        listener. '
      - This setting must match the setting on the trap listener. Otherwise, the listener
        drops the trap messages.
    type: str
    default: V2
  snmptrap_snmpuser_binding:
    type: dict
    description: Bindings for snmptrap_snmpuser_binding resource
    suboptions:
      mode:
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
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | snmptrap
      delegate_to: localhost
      netscaler.adc.snmptrap:
        state: present
        trapclass: generic
        trapdestination: 10.10.10.10
        version: V3
        allpartitions: ENABLED

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
