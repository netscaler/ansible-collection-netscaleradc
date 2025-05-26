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
module: lsnparameter
short_description: Configuration for LSN parameter resource.
description: Configuration for LSN parameter resource.
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
  memlimit:
    type: float
    description:
      - Amount of Citrix ADC memory to reserve for the LSN feature, in multiples of
        2MB.
      - ''
      - 'Note: If you later reduce the value of this parameter, the amount of active
        memory is not reduced. Changing the configured memory limit can only increase
        the amount of active memory.'
      - This command is deprecated, use 'set extendedmemoryparam -memlimit' instead.
  sessionsync:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Synchronize all LSN sessions with the secondary node in a high availability
        (HA) deployment (global synchronization). After a failover, established TCP
        connections and UDP packet flows are kept active and resumed on the secondary
        node (new primary).
      - ''
      - The global session synchronization parameter and session synchronization parameters
        (group level) of all LSN groups are enabled by default.
      - ''
      - For a group, when both the global level and the group level LSN session synchronization
        parameters are enabled, the primary node synchronizes information of all LSN
        sessions related to this LSN group with the secondary node.
  subscrsessionremoval:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - LSN global setting for controlling subscriber aware session removal, when
        this is enabled, when ever the subscriber info is deleted from subscriber
        database, sessions corresponding to that subscriber will be removed. if this
        setting is disabled, subscriber sessions will be timed out as per the idle
        time out settings.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lsnparameter playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lsnparameter
      delegate_to: localhost
      netscaler.adc.lsnparameter:
        state: present
        subscrsessionremoval: ENABLED
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
