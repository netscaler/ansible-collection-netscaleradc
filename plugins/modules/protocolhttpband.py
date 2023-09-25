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
module: protocolhttpband
short_description: Configuration for HTTP request/response band resource.
description: Configuration for HTTP request/response band resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: float
  reqbandsize:
    description:
      - 'Band size, in bytes, for HTTP request band statistics. For example, if you
        specify a band size of 100 bytes, statistics will be maintained and displayed
        for the following size ranges:'
      - 0 - 99 bytes
      - 100 - 199 bytes
      - 200 - 299 bytes and so on.
    type: int
    default: 100
  respbandsize:
    description:
      - 'Band size, in bytes, for HTTP response band statistics. For example, if you
        specify a band size of 100 bytes, statistics will be maintained and displayed
        for the following size ranges:'
      - 0 - 99 bytes
      - 100 - 199 bytes
      - 200 - 299 bytes and so on.
    type: int
    default: 1024
  type:
    choices:
      - REQUEST
      - RESPONSE
      - MQTT_JUMBO_REQ
    description:
      - Type of statistics to display.
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
