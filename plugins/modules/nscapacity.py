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
module: nscapacity
short_description: Configuration for capacity resource.
description: Configuration for capacity resource.
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
  bandwidth:
    type: int
    description:
      - System bandwidth limit.
  edition:
    type: str
    choices:
      - Standard
      - Enterprise
      - Platinum
    description:
      - Product edition.
  nodeid:
    type: int
    description:
      - Unique number that identifies the cluster node.
  password:
    type: str
    description:
      - Password to use when authenticating with ADM Agent for LAS licensing.
  platform:
    type: str
    choices:
      - VS10
      - VE10
      - VP10
      - VS25
      - VE25
      - VP25
      - VS50
      - VE50
      - VP50
      - VS200
      - VE200
      - VP200
      - VS1000
      - VE1000
      - VP1000
      - VS3000
      - VE3000
      - VP3000
      - VS5000
      - VE5000
      - VP5000
      - VS8000
      - VE8000
      - VP8000
      - VS10000
      - VE10000
      - VP10000
      - VS15000
      - VE15000
      - VP15000
      - VS25000
      - VE25000
      - VP25000
      - VS40000
      - VE40000
      - VP40000
      - VS100000
      - VE100000
      - VP100000
      - CP1000
    description:
      - appliance platform type.
  unit:
    type: str
    choices:
      - Gbps
      - Mbps
    description:
      - Bandwidth unit.
  username:
    type: str
    description:
      - Username to authenticate with ADM Agent for LAS licensing. Must begin with
        a letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals
        (=), colon (:), and underscore characters.
  vcpu:
    type: bool
    description:
      - licensed using vcpu pool.
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
