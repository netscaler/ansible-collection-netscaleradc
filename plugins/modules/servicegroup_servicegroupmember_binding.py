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
module: servicegroup_servicegroupmember_binding
short_description: Binding Resource definition for describing association between
  servicegroup and servicegroupmember resources
description: Binding Resource definition for describing association between servicegroup
  and servicegroupmember resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  customserverid:
    description:
      - The identifier for this IP:Port pair. Used when the persistency type is set
        to Custom Server ID.
    type: str
    default: '"None"'
  dbsttl:
    description:
      - Specify the TTL for DNS record for domain based service.The default value
        of ttl is 0 which indicates to use the TTL received in DNS response for monitors
    type: int
  hashid:
    description:
      - The hash identifier for the service. This must be unique for each service.
        This parameter is used by hash based load balancing methods.
    type: int
  ip:
    description:
      - IP Address.
    type: str
  nameserver:
    description:
      - Specify the nameserver to which the query for bound domain needs to be sent.
        If not specified, use the global nameserver
    type: str
  order:
    description:
      - Order number to be assigned to the servicegroup member
    type: int
  port:
    description:
      - Server port number.
    type: int
  serverid:
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
    type: int
  servername:
    description:
      - Name of the server to which to bind the service group.
    type: str
  servicegroupname:
    description:
      - Name of the service group.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Initial state of the service group.
    type: str
    default: ENABLED
  weight:
    description:
      - Weight to assign to the servers in the service group. Specifies the capacity
        of the servers relative to the other servers in the load balancing configuration.
        The higher the weight, the higher the percentage of requests sent to the service.
    type: int
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
