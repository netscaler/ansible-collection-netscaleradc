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
module: cacheparameter
short_description: Configuration for cache parameter resource.
description: Configuration for cache parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  enablebypass:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Evaluate the request-time policies before attempting hit selection. If set
        to C(NO), an incoming request for which a matching object is found in cache
        storage results in a response regardless of the policy configuration.
      - If the request matches a policy with a NOCACHE action, the request bypasses
        all cache processing.
      - This parameter does not affect processing of requests that match any invalidation
        policy.
  enablehaobjpersist:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - The HA object persisting parameter. When this value is set to C(YES), cache
        objects can be synced to Secondary in a HA deployment.  If set to C(NO), objects
        will never be synced to Secondary node.
  maxpostlen:
    type: float
    description:
      - Maximum number of POST body bytes to consider when evaluating parameters for
        a content group for which you have configured hit parameters and invalidation
        parameters.
  memlimit:
    type: float
    description:
      - Amount of memory available for storing the cache objects. In practice, the
        amount of memory available for caching can be less than half the total memory
        of the Citrix ADC.
  prefetchmaxpending:
    type: float
    description:
      - Maximum number of outstanding prefetches in the Integrated Cache.
  undefaction:
    type: str
    choices:
      - NOCACHE
      - RESET
    description:
      - Action to take when a policy cannot be evaluated.
  verifyusing:
    type: str
    choices:
      - HOSTNAME
      - HOSTNAME_AND_IP
      - DNS
    description:
      - 'Criteria for deciding whether a cached object can be served for an incoming
        HTTP request. Available settings function as follows:'
      - C(HOSTNAME) - The URL, host name, and host port values in the incoming HTTP
        request header must match the cache policy. The IP address and the TCP port
        of the destination host are not evaluated. Do not use the C(HOSTNAME) setting
        unless you are certain that no rogue client can access a rogue server through
        the cache.
      - C(HOSTNAME_AND_IP) - The URL, host name, host port in the incoming HTTP request
        header, and the IP address and TCP port of
      - the destination server, must match the cache policy.
      - C(DNS) - The URL, host name and host port in the incoming HTTP request, and
        the TCP port must match the cache policy. The host name is used for C(DNS)
        lookup of the destination server's IP address, and is compared with the set
        of addresses returned by the C(DNS) lookup.
  via:
    type: str
    description:
      - String to include in the Via header. A Via header is inserted into all responses
        served from a content group if its Insert Via flag is set.
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
