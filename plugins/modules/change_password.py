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
module: change_password
short_description: Change password of a user on a NetScaler ADC node.
description: Configuration for changing password of a user on a NetScaler ADC node.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  username:
    description:
      - Username of the user whose password to be changed
    type: str
    required: true
  password:
    description:
      - Current password of the user on the NetScaler ADC node.
    type: str
    required: true
  new_password:
    description:
      - New desired password of the user on the NetScaler ADC node.
    type: str
    required: true
  first_boot:
    description:
      - 'true' if the NetScaler ADC node is booting for the first time after installation.
      - 'false' if the NetScaler ADC node is already configured and running.
    type: bool
    required: true
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample change_password
  hosts: demo_netscalers

  gather_facts: false

  tasks:
    # Change password of previously logged in user on a NetScaler ADC node
    - name: V2 | Sample Task | change_password
      delegate_to: localhost
      netscaler.adc.change_password:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        username: nsroot
        password: strongpassword
        new_password: newverystrongpassword
        first_boot: false

    # Change password of first time login (first_boot) user on a NetScaler ADC node
    - name: V2 | Sample Task | change_password
      delegate_to: localhost
      netscaler.adc.change_password:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        username: nsroot
        password: strongpassword
        new_password: newverystrongpassword
        first_boot: true
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module. `change_password` module always returns `true` unless it fails.
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
    executor.change_password()


if __name__ == "__main__":
    main()
