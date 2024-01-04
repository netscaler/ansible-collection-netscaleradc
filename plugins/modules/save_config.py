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
module: save_config
short_description: Login to a NetScaler ADC node.
description: Configuration for logging in to a NetScaler ADC node.
version_added: 2.2.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
    type: str
  all:
    description:
      - Use this option to do saveconfig for all partitions
    type: bool
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample save config
  hosts: demo_netscalers

  gather_facts: false

  tasks:
    - name: V2 | Sample Task | Save config
      delegate_to: localhost
      netscaler.adc.save_config:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable
        all: false  # default is false. If true, save config for all partitions


    - name: V2 | Sample Task | Save config for all partitions
      delegate_to: localhost
      netscaler.adc.save_config:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable
        all: true
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module. `save_config` module always returns `true` unless it fails.
    returned: always
    type: bool
    sample: true
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
    executor.config_save()


if __name__ == "__main__":
    main()
