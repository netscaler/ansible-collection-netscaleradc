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
module: vserver
short_description: Configuration for virtual server resource.
description: Configuration for virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  backupvserver:
    description:
      - The name of the backup virtual server for this virtual server.
    type: str
  cacheable:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use this option to specify whether a virtual server (used for load balancing
        or content switching) routes requests to the cache redirection virtual server
        before sending it to the configured servers.
    type: str
  clttimeout:
    description:
      - The timeout value in seconds for idle client connection
    type: float
  name:
    description:
      - The name of the virtual server to be removed.
    type: str
  pushvserver:
    description:
      - The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received
        on the client facing non-push lb vserver.
    type: str
  redirecturl:
    description:
      - The URL where traffic is redirected if the virtual server in the system becomes
        unavailable.
    type: str
  somethod:
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
    description:
      - The spillover factor. The system will use this value to determine if it should
        send traffic to the backupvserver when the main virtual server reaches the
        spillover threshold.
    type: str
  sopersistence:
    choices:
      - ENABLED
      - DISABLED
    description:
      - The state of the spillover persistence.
    type: str
    default: DISABLED
  sopersistencetimeout:
    description:
      - The spillover persistence entry timeout.
    type: float
    default: 2
  sothreshold:
    description:
      - The spillver threshold value.
    type: float
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
