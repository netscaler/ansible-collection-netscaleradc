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
module: server
short_description: Configuration for server resource.
description: Configuration for server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  Internal:
    description:
      - Display names of the servers that have been created for internal use.
    type: bool
  comment:
    description:
      - Any information about the server.
    type: str
  delay:
    description:
      - Time, in seconds, after which all the services configured on the server are
        disabled.
    type: int
  domain:
    description:
      - Domain name of the server. For a domain based configuration, you must create
        the server first.
    type: str
  domainresolvenow:
    description:
      - Immediately send a DNS query to resolve the server's domain name.
    type: bool
  domainresolveretry:
    description:
      - Time, in seconds, for which the Citrix ADC must wait, after DNS resolution
        fails, before sending the next DNS query to resolve the domain name.
    type: int
    default: 5
  graceful:
    choices:
      - true
      - false
    description:
      - Shut down gracefully, without accepting any new connections, and disabling
        each service when all of its connections are closed.
    type: str
  ipaddress:
    description:
      - 'IPv4 or IPv6 address of the server. If you create an IP address based server,
        you can specify the name of the server, instead of its IP address, when creating
        a service. Note: If you do not create a server entry, the server IP address
        that you enter when you create a service becomes the name of the server.'
    type: str
  ipv6address:
    choices:
      - true
      - false
    description:
      - Support IPv6 addressing mode. If you configure a server with the IPv6 addressing
        mode, you cannot use the server in the IPv4 addressing mode.
    type: str
  name:
    description:
      - 'Name for the server. '
      - Must begin with an ASCII alphabetic or underscore (_) character, and must
        contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at (@), equals (=), and hyphen (-) characters.
      - Can be changed after the name is created.
    type: str
  newname:
    description:
      - New name for the server. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
    type: str
  querytype:
    choices:
      - A
      - AAAA
      - SRV
    description:
      - Specify the type of DNS resolution to be done on the configured domain to
        get the backend services. Valid query types are C(A), C(AAAA) and C(SRV) with
        C(A) being the default querytype. The type of DNS resolution done on the domains
        in C(SRV) records is inherited from ipv6 argument.
    type: str
    default: A
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Initial state of the server.
    type: str
    default: ENABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  translationip:
    description:
      - IP address used to transform the server's DNS-resolved IP address.
    type: str
  translationmask:
    description:
      - The netmask of the translation ip
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
