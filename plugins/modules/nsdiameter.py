#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: nsdiameter
short_description: Configuration for Diameter Parameters resource.
description: Configuration for Diameter Parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  identity:
    description:
      - DiameterIdentity to be used by NS. DiameterIdentity is used to identify a
        Diameter node uniquely. Before setting up diameter configuration, Citrix ADC
        (as a Diameter node) MUST be assigned a unique DiameterIdentity.
      - example =>
      - set ns diameter -identity netscaler.com
      - Now whenever Citrix ADC needs to use identity in diameter messages. It will
        use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
    type: str
  ownernode:
    description:
      - ID of the cluster node for which the diameter id is set, can be configured
        only through CLIP
    type: float
    default: -1
  realm:
    description:
      - Diameter Realm to be used by NS.
      - example =>
      - set ns diameter -realm com
      - Now whenever Citrix ADC system needs to use realm in diameter messages. It
        will use 'com' as Origin-Realm AVP as defined in RFC3588
    type: str
  serverclosepropagation:
    choices:
      - 'YES'
      - 'NO'
    description:
      - when a Server connection goes down, whether to close the corresponding client
        connection if there were requests pending on the server.
    type: str
    default: 'NO'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | nsdiameter
      delegate_to: localhost
      netscaler.adc.nsdiameter:
        state: present
        identity: netscaler.com
        realm: com

"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
