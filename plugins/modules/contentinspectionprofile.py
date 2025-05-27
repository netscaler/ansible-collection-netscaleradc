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
module: contentinspectionprofile
short_description: Configuration for ContentInspection profile resource.
description: Configuration for ContentInspection profile resource.
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
  egressinterface:
    type: str
    description:
      - Egress interface for CI profile.It is a mandatory argument while creating
        an ContentInspection profile of type INLINEINSPECTION or MIRROR.
  egressvlan:
    type: int
    description:
      - Egress Vlan for CI
  ingressinterface:
    type: str
    description:
      - Ingress interface for CI profile.It is a mandatory argument while creating
        an ContentInspection profile of IPS type.
  ingressvlan:
    type: int
    description:
      - Ingress Vlan for CI
  iptunnel:
    type: str
    description:
      - IP Tunnel for CI profile. It is used while creating a ContentInspection profile
        of type MIRROR when the IDS device is in a different network
  name:
    type: str
    description:
      - Name of a ContentInspection profile. Must begin with a letter, number, or
        the underscore \(_\) character. Other characters allowed, after the first
        character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at
        \(@\), colon \(:\), and equal \(=\) characters. The name of a IPS profile
        cannot be changed after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my ips profile" or ''my ips profile''\).'
  type:
    type: str
    choices:
      - InlineInspection
      - Mirror
    description:
      - 'Type of ContentInspection profile. Following types are available to configure:'
      - '           INLINEINSPECTION : To inspect the packets/requests using IPS.'
      - "\t   MIRROR : To forward cloned packets."
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
