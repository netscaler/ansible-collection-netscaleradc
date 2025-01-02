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
module: vrid6
short_description: Configuration for Virtual Router ID for IPv6 resource.
description: Configuration for Virtual Router ID for IPv6 resource.
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
  all:
    type: bool
    description:
      - Remove all configured VMAC6 addresses from the Citrix ADC.
  id:
    type: float
    description:
      - Integer value that uniquely identifies a VMAC6 address.
  ownernode:
    type: float
    description:
      - In a cluster setup, assign a cluster node as the owner of this VMAC address
        for IP based VRRP configuration. If no owner is configured, ow ner node is
        displayed as ALL and one node is dynamically elected as the owner.
  preemption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - In an active-active mode configuration, make a backup VIP address the master
        if its priority becomes higher than that of a master VIP address bound to
        this VMAC address.
      - '             If you disable pre-emption while a backup VIP address is the
        master, the backup VIP address remains master until the original master VIP''s
        priority becomes higher than that of the current master.'
  preemptiondelaytimer:
    type: float
    description:
      - Preemption delay time in seconds, in an active-active configuration. If any
        high priority node will come in network, it will wait for these many seconds
        before becoming master.
  priority:
    type: float
    description:
      - Base priority (BP), in an active-active mode configuration, which ordinarily
        determines the master VIP address.
  sharing:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - In an active-active mode configuration, enable the backup VIP address to process
        any traffic instead of dropping it.
  trackifnumpriority:
    type: float
    description:
      - Priority by which the Effective priority will be reduced if any of the tracked
        interfaces goes down in an active-active configuration.
  tracking:
    type: str
    choices:
      - NONE
      - ONE
      - ALL
      - PROGRESSIVE
    description:
      - The effective priority (EP) value, relative to the base priority (BP) value
        in an active-active mode configuration. When EP is set to a value other than
        None, it is EP, not BP, which determines the master VIP address.
      - 'Available settings function as follows:'
      - '* C(NONE) - No tracking. EP = BP'
      - '* C(ALL) -  If the status of all virtual servers is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* C(ONE) - If the status of at least one virtual server is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* C(PROGRESSIVE) - If the status of all virtual servers is UP, EP = BP. If
        the status of all virtual servers is DOWN, EP = 0. Otherwise EP = BP (1 -
        K/N), where N is the total number of virtual servers associated with the VIP
        address and K is the number of virtual servers for which the status is DOWN.'
      - 'Default: C(NONE).'
  vrid6_channel_binding:
    type: dict
    description: Bindings for vrid6_channel_binding resource
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
  vrid6_interface_binding:
    type: dict
    description: Bindings for vrid6_interface_binding resource
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
  vrid6_trackinterface_binding:
    type: dict
    description: Bindings for vrid6_trackinterface_binding resource
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
- name: Sample vrid6 playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vrid6
      delegate_to: localhost
      netscaler.adc.vrid6:
        state: present
        id: '13'
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
