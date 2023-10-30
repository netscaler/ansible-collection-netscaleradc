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
module: callhome
short_description: Configuration for callhome resource.
description: Configuration for callhome resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
    type: str
  emailaddress:
    type: str
    description:
      - Email address of the contact administrator.
  hbcustominterval:
    type: float
    description:
      - Interval (in days) between CallHome heartbeats
    default: 7
  ipaddress:
    type: str
    description:
      - IP address of the proxy server.
  mode:
    type: str
    choices:
      - Default
      - CSP
    description:
      - CallHome mode of operation
    default: Default
  nodeid:
    type: float
    description:
      - Unique number that identifies the cluster node.
  port:
    type: int
    description:
      - HTTP port on the Proxy server. This is a mandatory parameter for both IP address
        and service name based configuration.
  proxyauthservice:
    type: str
    description:
      - Name of the service that represents the proxy server.
  proxymode:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enables or disables the proxy mode. The proxy server can be set by either
        specifying the IP address of the server or the name of the service representing
        the proxy server.
    default: 'NO'
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
