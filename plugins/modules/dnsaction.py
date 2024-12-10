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
module: dnsaction
short_description: Configuration for DNS action resource.
description: Configuration for DNS action resource.
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
  actionname:
    type: str
    description:
      - Name of the dns action.
  actiontype:
    type: str
    choices:
      - ViewName
      - GslbPrefLoc
      - noop
      - Drop
      - Cache_Bypass
      - Rewrite_Response
    description:
      - The type of DNS action that is being configured.
  dnsprofilename:
    type: str
    description:
      - Name of the DNS profile to be associated with the transaction for which the
        action is chosen
  ipaddress:
    type: list
    description:
      - List of IP address to be returned in case of rewrite_response actiontype.
        They can be of IPV4 or IPV6 type.
      - '        In case of set command We will remove all the IP address previously
        present in the action and will add new once given in set dns action command.'
    elements: str
  preferredloclist:
    type: list
    description:
      - The location list in priority order used for the given action.
    elements: str
  ttl:
    type: float
    description:
      - Time to live, in seconds.
  viewname:
    type: str
    description:
      - The view name that must be used for the given action.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnsaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnsaction
      delegate_to: localhost
      netscaler.adc.dnsaction:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        actionname: ia_dnsact8
        actiontype: Rewrite_Response
        ipaddress:
          - 1.1.1.102
        ttl: 3601
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
