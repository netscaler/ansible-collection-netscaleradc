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
module: vpnurl
short_description: Configuration for VPN URL resource.
description: Configuration for VPN URL resource.
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
  actualurl:
    type: str
    description:
      - Web address for the bookmark link.
  appjson:
    type: str
    description:
      - To store the template details in the json format.
  applicationtype:
    type: str
    choices:
      - CVPN
      - VPN
      - SaaS
    description:
      - The type of application this C(VPN) URL represents. Possible values are C(CVPN)/C(SaaS)/C(VPN)
  clientlessaccess:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - If clientless access to the resource hosting the link is allowed, also use
        clientless access for the bookmarked web address in the Secure Client Access
        based session. Allows single sign-on and other HTTP processing on Citrix Gateway
        for HTTPS resources.
  comment:
    type: str
    description:
      - Any comments associated with the bookmark link.
  iconurl:
    type: str
    description:
      - URL to fetch icon file for displaying this resource.
  linkname:
    type: str
    description:
      - Description of the bookmark link. The description appears in the Access Interface.
  samlssoprofile:
    type: str
    description:
      - Profile to be used for doing SAML SSO
  ssotype:
    type: str
    choices:
      - unifiedgateway
      - selfauth
      - samlauth
    description:
      - Single sign on type for unified gateway
  urlname:
    type: str
    description:
      - Name of the bookmark link.
  vservername:
    type: str
    description:
      - Name of the associated LB/CS vserver
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample vpnurl playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vpnurl
      delegate_to: localhost
      netscaler.adc.vpnurl:
        state: present
        urlname: url3
        linkname: url3
        actualurl: https://a.c.com/
        ssotype: samlauth
        samlssoprofile: new
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
