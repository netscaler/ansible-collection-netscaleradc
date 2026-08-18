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
module: dnszone
short_description: Configuration for DNS zone resource.
description: Configuration for DNS zone resource.
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
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  dnssecoffload:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable dnssec offload for this zone.
  keyname:
    type: list
    description:
      - Name of the public/private DNS key pair with which to sign the zone. You can
        sign a zone with up to four keys.
    elements: str
  nsec:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable nsec generation for dnssec offload.
  proxymode:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - 'Deploy the zone in proxy mode. Enable in the following scenarios:'
      - '* The load balanced DNS servers are authoritative for the zone and all resource
        records that are part of the zone.'
      - '* The load balanced DNS servers are authoritative for the zone, but the Citrix
        ADC owns a subset of the resource records that belong to the zone (partial
        zone ownership configuration). Typically seen in global server load balancing
        (GSLB) configurations, in which the appliance responds authoritatively to
        queries for GSLB domain names but forwards queries for other domain names
        in the zone to the load balanced servers.'
      - In either scenario, do not create the zone's Start of Authority (SOA) and
        name server (NS) resource records on the appliance.
      - Disable if the appliance is authoritative for the zone, but make sure that
        you have created the SOA and NS records on the appliance before you create
        the zone.
  type:
    type: str
    choices:
      - ALL
      - ADNS
      - PROXY
    description:
      - 'Type of zone to display. Mutually exclusive with the DNS Zone (zoneName)
        parameter. Available settings function as follows:'
      - '* C(ADNS) - Display all the zones for which the Citrix ADC is authoritative.'
      - '* C(PROXY) - Display all the zones for which the Citrix ADC is functioning
        as a proxy server.'
      - '* C(ALL) - Display all the zones configured on the appliance.'
  zonename:
    type: str
    description:
      - Name of the zone to create.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnszone playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnszone
      delegate_to: localhost
      netscaler.adc.dnszone:
        state: present
        zonename: com
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
