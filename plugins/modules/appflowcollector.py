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
module: appflowcollector
short_description: Configuration for AppFlow collector resource.
description: Configuration for AppFlow collector resource.
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
  ipaddress:
    type: str
    description:
      - IPv4 address of the collector.
  name:
    type: str
    description:
      - Name for the collector. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at
      - (@), equals (=), and hyphen (-) characters.
      - ' Only four collectors can be configured.'
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow collector" or 'my appflow collector').
  netprofile:
    type: str
    description:
      - Netprofile to associate with the collector. The IP address defined in the
        profile is used as the source IP address for AppFlow traffic for this collector.  If
        you do not set this parameter, the Citrix ADC IP (NSIP) address is used as
        the source IP address.
  newname:
    type: str
    description:
      - New name for the collector. Must begin with an ASCII alphabetic or underscore
        (_) character, and must
      - contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at(@), equals (=), and hyphen (-) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow coll" or 'my appflow coll').
  port:
    type: int
    description:
      - Port on which the collector listens.
  transport:
    type: str
    choices:
      - ipfix
      - logstream
      - rest
    description:
      - 'Type of collector: either C(logstream) or C(ipfix) or C(rest).'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appflowcollector playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appflowcollector
      delegate_to: localhost
      netscaler.adc.appflowcollector:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: af_collector_logstream_10.189.64.10
        ipaddress: 10.189.64.10
        port: 5557
        transport: logstream
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
