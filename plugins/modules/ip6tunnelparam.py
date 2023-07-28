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
module: ip6tunnelparam
short_description: Configuration for ip6 tunnel parameter resource.
description: Configuration for ip6 tunnel parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  dropfrag:
    choices:
      - true
      - false
    description:
      - Drop any packet that requires fragmentation.
    type: str
  dropfragcputhreshold:
    description:
      - Threshold value, as a percentage of CPU usage, at which to drop packets that
        require fragmentation. Applies only if dropFragparameter is set to NO.
    type: int
  srcip:
    description:
      - Common source IPv6 address for all IPv6 tunnels. Must be a SNIP6 or VIP6 address.
    type: str
  srciproundrobin:
    choices:
      - true
      - false
    description:
      - Use a different source IPv6 address for each new session through a particular
        IPv6 tunnel, as determined by round robin selection of one of the SNIP6 addresses.
        This setting is ignored if a common global source IPv6 address has been specified
        for all the IPv6 tunnels. This setting does not apply to a tunnel for which
        a source IPv6 address has been specified.
    type: str
  useclientsourceipv6:
    choices:
      - true
      - false
    description:
      - Use client source IPv6 address as source IPv6 address for outer tunnel IPv6
        header
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
