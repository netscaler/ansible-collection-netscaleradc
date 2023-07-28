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
module: callhome
short_description: Configuration for callhome resource.
description: Configuration for callhome resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  emailaddress:
    description:
      - Email address of the contact administrator.
    type: str
  hbcustominterval:
    description:
      - Interval (in days) between CallHome heartbeats
    type: int
    default: 7
  ipaddress:
    description:
      - IP address of the proxy server.
    type: str
  mode:
    choices:
      - Default
      - CSP
    description:
      - CallHome mode of operation
    type: str
    default: Default
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: int
  port:
    description:
      - HTTP port on the Proxy server. This is a mandatory parameter for both IP address
        and service name based configuration.
    type: int
  proxyauthservice:
    description:
      - Name of the service that represents the proxy server.
    type: str
  proxymode:
    choices:
      - true
      - false
    description:
      - Enables or disables the proxy mode. The proxy server can be set by either
        specifying the IP address of the server or the name of the service representing
        the proxy server.
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
