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
module: cmpaction
short_description: Configuration for compression action resource.
description: Configuration for compression action resource.
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
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  addvaryheader:
    type: str
    choices:
      - GLOBAL
      - DISABLED
      - ENABLED
    description:
      - Control insertion of the Vary header in HTTP responses compressed by Citrix
        ADC. Intermediate caches store different versions of the response for different
        values of the headers present in the Vary response header.
  cmptype:
    type: str
    choices:
      - compress
      - gzip
      - deflate
      - nocompress
    description:
      - Type of compression performed by this action.
      - 'Available settings function as follows:'
      - '* COMPRESS - Apply GZIP or DEFLATE compression to the response, depending
        on the request header. Prefer GZIP.'
      - '* GZIP - Apply GZIP compression.'
      - '* DEFLATE - Apply DEFLATE compression.'
      - '* NOCOMPRESS - Do not C(compress) the response if the request matches a policy
        that uses this action.'
  deltatype:
    type: str
    choices:
      - PERURL
      - PERPOLICY
    description:
      - The type of delta action (if delta type compression action is defined).
  name:
    type: str
    description:
      - Name of the compression action. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp action" or 'my cmp action').
  newname:
    type: str
    description:
      - New name for the compression action. Must begin with an ASCII alphabetic or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at
      - (@), equals (=), and hyphen (-) characters.
      - Choose a name that can be correlated with the function that the action performs.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp action" or 'my cmp action').
  varyheadervalue:
    type: str
    description:
      - The value of the HTTP Vary header for compressed responses.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample cmpaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cmpaction
      delegate_to: localhost
      netscaler.adc.cmpaction:
        state: present
        name: Base_cmp_act1
        cmptype: compress
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
