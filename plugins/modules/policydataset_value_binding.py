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
module: policydataset_value_binding
short_description: Binding Resource definition for describing association between
  policydataset and value resources
description: Binding Resource definition for describing association between policydataset
  and value resources
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about this dataset or a data bound to
        this dataset.
  endrange:
    type: str
    description:
      - The dataset entry is a range from <value> through <end_range>, inclusive.
        endRange cannot be used if value is an ipv4 or ipv6 subnet and endRange cannot
        itself be a subnet.
  index:
    type: float
    description:
      - The index of the value (ipv4, ipv6, number) associated with the set.
  name:
    type: str
    description:
      - Name of the dataset to which to bind the value.
  value:
    type: str
    description:
      - Value of the specified type that is associated with the dataset. For ipv4
        and ipv6, value can be a subnet using the slash notation address/n, where
        address is the beginning of the subnet and n is the number of left-most bits
        set in the subnet mask, defining the end of the subnet. The start address
        will be masked by the subnet mask if necessary, for example for 192.128.128.0/10,
        the start address will be 192.128.0.0.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample policydataset_value_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure policydataset_value_binding
      delegate_to: localhost
      netscaler.adc.policydataset_value_binding:
        state: present
        name: SF_LBVIP
        value: 10.76.126.10
        index: '2'
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
