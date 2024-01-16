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
module: cacheobject
short_description: Configuration for cache object resource.
description: Configuration for cache object resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - flushed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(flushed), the resource will be flushed on the NetScaler ADC node.
    type: str
  group:
    type: str
    description:
      - Name of the content group whose objects should be listed.
  groupname:
    type: str
    description:
      - Name of the content group to which the object belongs. It will display only
        the objects belonging to the specified content group. You must also set the
        Host parameter.
  host:
    type: str
    description:
      - Host name of the object. Parameter "url" must be specified.
  httpmethod:
    type: str
    choices:
      - GET
      - POST
    description:
      - HTTP request method that caused the object to be stored.
  httpstatus:
    type: float
    description:
      - HTTP status of the object.
  ignoremarkerobjects:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Ignore marker objects. Marker objects are created when a response exceeds
        the maximum or minimum response size for the content group or has not yet
        received the minimum number of hits for the content group.
  includenotreadyobjects:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Include responses that have not yet reached a minimum number of hits before
        being cached.
  locator:
    type: float
    description:
      - ID of the cached object.
  nodeid:
    type: float
    description:
      - Unique number that identifies the cluster node.
  port:
    type: int
    description:
      - Host port of the object. You must also set the Host parameter.
  tosecondary:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Object will be saved onto Secondary.
  url:
    type: str
    description:
      - URL of the particular object whose details is required. Parameter "host" must
        be specified along with the URL.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
