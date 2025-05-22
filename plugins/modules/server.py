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
module: server
short_description: Configuration for server resource.
description: Configuration for server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  internal:
    type: bool
    description:
      - Display names of the servers that have been created for internal use.
  comment:
    type: str
    description:
      - Any information about the server.
  delay:
    type: int
    description:
      - Time, in seconds, after which all the services configured on the server are
        disabled.
  domain:
    type: str
    description:
      - Domain name of the server. For a domain based configuration, you must create
        the server first.
  domainresolvenow:
    type: bool
    description:
      - Immediately send a DNS query to resolve the server's domain name.
  domainresolveretry:
    type: int
    description:
      - Time, in seconds, for which the NetScaler must wait, after DNS resolution
        fails, before sending the next DNS query to resolve the domain name.
  graceful:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Shut down gracefully, without accepting any new connections, and disabling
        each service when all of its connections are closed.
  ipaddress:
    type: str
    description:
      - 'IPv4 or IPv6 address of the server. If you create an IP address based server,
        you can specify the name of the server, instead of its IP address, when creating
        a service. Note: If you do not create a server entry, the server IP address
        that you enter when you create a service becomes the name of the server.'
  ipv6address:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Support IPv6 addressing mode. If you configure a server with the IPv6 addressing
        mode, you cannot use the server in the IPv4 addressing mode.
  name:
    type: str
    description:
      - Name for the server.
      - Must begin with an ASCII alphabetic or underscore (_) character, and must
        contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at (@), equals (=), and hyphen (-) characters.
      - Can be changed after the name is created.
  newname:
    type: str
    description:
      - New name for the server. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  querytype:
    type: str
    choices:
      - A
      - AAAA
      - SRV
    description:
      - Specify the type of DNS resolution to be done on the configured domain to
        get the backend services. Valid query types are C(A), C(AAAA) and C(SRV) with
        C(A) being the default querytype. The type of DNS resolution done on the domains
        in C(SRV) records is inherited from ipv6 argument.
  td:
    type: int
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  translationip:
    type: str
    description:
      - IP address used to transform the server's DNS-resolved IP address.
  translationmask:
    type: str
    description:
      - The netmask of the translation ip
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample server playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure server
      delegate_to: localhost
      netscaler.adc.server:
        state: present
        name: STA_SERVER
        domain: sta.devalab.com
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
