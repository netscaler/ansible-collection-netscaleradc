#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: login
short_description: Login to a NetScaler ADC node.
description: Configuration for logging in to a NetScaler ADC node.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  username:
    description:
      - Username for logging into the NetScaler ADC node.
    type: str
    required: true
  password:
    description:
      - Password for logging into the NetScaler ADC node.
    type: str
    required: true
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample login  and logout playbook
  hosts: demo_netscalers

  gather_facts: false

  tasks:
    - name: V2 | Sample Task | login
      delegate_to: localhost
      register: login_result
      netscaler.adc.login:
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        username: nsroot
        password: verysecretpassword

    - name: Print login sessionid
      ansible.builtin.debug:
        var: login_result.sessionid

    - name: V2 | Sample Task | nsip
      delegate_to: localhost
      netscaler.adc.nsip:
        nitro_auth_token: "{{ login_result.sessionid }}" # This can also be given via NETSCALER_NITRO_AUTH_TOKEN environment variable
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        state: present

        ipaddress: 4.4.4.4
        netmask: 255.255.255.192
        type: VIP

    - name: V2 | Sample Task | logout
      delegate_to: localhost
      netscaler.adc.logout:
        nitro_auth_token: "{{ login_result.sessionid }}" # This can also be given via NETSCALER_NITRO_AUTH_TOKEN environment variable
        # nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        # nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        # validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable
        # save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module. `login` module always returns `true` unless it fails.
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
sessionid:
    description: Session ID of the logged in user
    returned: always
    type: str
    sample: '1234567890'
"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.login()


if __name__ == "__main__":
    main()
