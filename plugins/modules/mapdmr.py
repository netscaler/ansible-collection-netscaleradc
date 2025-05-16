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
module: mapdmr
short_description: Configuration for MAP-T Default Mapping rule resource.
description: Configuration for MAP-T Default Mapping rule resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  bripv6prefix:
    type: str
    description:
      - IPv6 prefix of Border Relay (Citrix ADC) device.MAP-T CE will send ipv6 packets
        to this ipv6 prefix.The DMR IPv6 prefix length SHOULD be 64 bits long by default
        and in any case MUST NOT exceed 96 bits
  name:
    type: str
    description:
      - 'Name for the Default Mapping Rule. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the MAP Default Mapping Rule is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "add network MapDmr map1 -BRIpv6Prefix 2003::/96").'
      - "\t\t\tDefault Mapping Rule (DMR) is defined in terms of the IPv6 prefix advertised\
        \ by one or more BRs, which provide external connectivity.  A typical MAP-T\
        \ CE will install an IPv4 default route using this rule.  A BR will use this\
        \ rule when translating all outside IPv4 source addresses to the IPv6 MAP\
        \ domain."
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample mapdmr playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure mapdmr
      delegate_to: localhost
      netscaler.adc.mapdmr:
        state: present
        name: dmr1
        bripv6prefix: 2001:db8::/64
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
