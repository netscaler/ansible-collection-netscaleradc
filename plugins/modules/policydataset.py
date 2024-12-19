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
module: policydataset
short_description: Configuration for TYPE set resource.
description: Configuration for TYPE set resource.
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
  comment:
    type: str
    description:
      - Any comments to preserve information about this dataset or a data bound to
        this dataset.
  dynamic:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - This is used to populate internal dataset information so that the dataset
        can also be used dynamically in an expression. Here dynamically means the
        dataset name can also be derived using an expression. For example for a given
        dataset name "allow_test" it can be used dynamically as client.ip.src.equals_any("allow_"
        + http.req.url.path.get(1)). This cannot be used with default datasets.
  dynamiconly:
    type: bool
    description:
      - Shows only dynamic datasets when set true.
  name:
    type: str
    description:
      - Name of the dataset. Must not exceed 127 characters.
  patsetfile:
    type: str
    description:
      - File which contains list of patterns that needs to be bound to the dataset.
        A patsetfile cannot be associated with multiple datasets.
  type:
    type: str
    choices:
      - ipv4
      - number
      - ipv6
      - ulong
      - double
      - mac
    description:
      - Type of value to bind to the dataset.
  policydataset_value_binding:
    type: dict
    description: Bindings for policydataset_value_binding resource
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
- name: Sample policydataset playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure policydataset
      delegate_to: localhost
      netscaler.adc.policydataset:
        state: present
        name: SF_LBVIP
        type: ipv4
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
