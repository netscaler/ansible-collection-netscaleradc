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
module: dnsprofile
short_description: Configuration for DNS profile resource.
description: Configuration for DNS profile resource.
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
  cacheecsresponses:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Cache DNS responses with EDNS Client Subnet(ECS) option in the DNS cache.
        When disabled, the appliance stops caching responses with ECS option. This
        is relevant to proxy configuration. Enabling/disabling support of ECS option
        when Citrix ADC is authoritative for a GSLB domain is supported using a knob
        in GSLB vserver. In all other modes, ECS option is ignored.
  cachenegativeresponses:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Cache negative responses in the DNS cache. When disabled, the appliance stops
        caching negative responses except referral records. This applies to all configurations
        - proxy, end resolver, and forwarder. However, cached responses are not flushed.
        The appliance does not serve negative responses from the cache until this
        parameter is enabled again.
  cacherecords:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Cache resource records in the DNS cache. Applies to resource records obtained
        through proxy configurations only. End resolver and forwarder configurations
        always cache records in the DNS cache, and you cannot disable this behavior.
        When you disable record caching, the appliance stops caching server responses.
        However, cached records are not flushed. The appliance does not serve requests
        from the cache until record caching is enabled again.
  dnsanswerseclogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - DNS answer section; if enabled, answer section in the response will be logged.
  dnserrorlogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - DNS error logging; if enabled, whenever error is encountered in DNS module
        reason for the error will be logged.
  dnsextendedlogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - DNS extended logging; if enabled, authority and additional section in the
        response will be logged.
  dnsprofilename:
    type: str
    description:
      - Name of the DNS profile
  dnsquerylogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - DNS query logging; if enabled, DNS query information such as DNS query id,
        DNS query flags , DNS domain name and DNS query type will be logged
  dropmultiqueryrequest:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop the DNS requests containing multiple queries. When enabled, DNS requests
        containing multiple queries will be dropped. In case of proxy configuration
        by default the DNS request containing multiple queries is forwarded to the
        backend and in case of ADNS and Resolver configuration NOCODE error response
        will be sent to the client.
  insertecs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert ECS Option on DNS query
  maxcacheableecsprefixlength:
    type: float
    description:
      - The maximum ecs prefix length that will be cached
  maxcacheableecsprefixlength6:
    type: float
    description:
      - The maximum ecs prefix length that will be cached for IPv6 subnets
  replaceecs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Replace ECS Option on DNS query
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample dnsprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure dnsprofile
      delegate_to: localhost
      netscaler.adc.dnsprofile:
        state: present
        dnsprofilename: p1
        cacherecords: ENABLED
        cachenegativeresponses: ENABLED
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
