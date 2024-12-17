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
module: icalatencyprofile
short_description: Configuration for Profile for Latency monitoring resource.
description: Configuration for Profile for Latency monitoring resource.
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
  l7latencymaxnotifycount:
    type: float
    description:
      - L7 Latency Max notify Count. This is the upper limit on the number of notifications
        sent to the Insight Center within an interval where the Latency is above the
        threshold.
  l7latencymonitoring:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable L7 Latency monitoring for L7 latency notifications
  l7latencynotifyinterval:
    type: float
    description:
      - L7 Latency Notify Interval. This is the interval at which the Citrix ADC sends
        out notifications to the Insight Center after the wait time has passed.
  l7latencythresholdfactor:
    type: float
    description:
      - L7 Latency threshold factor. This is the factor by which the active latency
        should be greater than the minimum observed value to determine that the latency
        is high and may need to be reported
  l7latencywaittime:
    type: float
    description:
      - L7 Latency Wait time. This is the time for which the Citrix ADC waits after
        the threshold is exceeded before it sends out a Notification to the Insight
        Center.
  name:
    type: str
    description:
      - Name for the ICA latencyprofile. Must begin with a letter, number, or the
        underscore character (_), and must contain only letters, numbers, and
      - the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters. Cannot be changed after the ICA latency profile
        is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my ica l7latencyprofile" or 'my ica l7latencyprofile').
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample icalatencyprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure icalatencyprofile
      delegate_to: localhost
      netscaler.adc.icalatencyprofile:

        state: present
        name: l6
        l7latencywaittime: '5'
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
