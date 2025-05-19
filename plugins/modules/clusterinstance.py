#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: clusterinstance
short_description: Configuration for cluster instance resource.
description: Configuration for cluster instance resource.
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
    type: str
  backplanebasedview:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - View based on heartbeat only on bkplane interface
  clid:
    type: int
    description:
      - Unique number that identifies the cluster.
  clusterproxyarp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This field controls the proxy arp feature in cluster. By default the flag
        is enabled.
  deadinterval:
    type: int
    description:
      - Amount of time, in seconds, after which nodes that do not respond to the heartbeats
        are assumed to be down.If the value is less than 3 sec, set the helloInterval
        parameter to 200 msec
  dfdretainl2params:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - flag to add ext l2 header during steering. By default the flag is disabled.
  hellointerval:
    type: int
    description:
      - Interval, in milliseconds, at which heartbeats are sent to each cluster node
        to check the health status.Set the value to 200 msec, if the deadInterval
        parameter is less than 3 sec
  inc:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option is required if the cluster nodes reside on different networks.
  nodegroup:
    type: str
    description:
      - The node group in a Cluster system used for transition from L2 to L3.
  preemption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Preempt a cluster node that is configured as a SPARE if an ACTIVE node becomes
        available.
  processlocal:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option packets destined to a service in a cluster will
        not under go any steering.
  quorumtype:
    type: str
    choices:
      - MAJORITY
      - NONE
    description:
      - Quorum Configuration Choices  - "Majority" (recommended) requires majority
        of nodes to be online for the cluster to be UP. "None" relaxes this requirement.
  retainconnectionsoncluster:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option enables you to retain existing connections on a node joining a
        Cluster system or when a node is being configured for passive timeout. By
        default, this option is disabled.
  secureheartbeats:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option cluster heartbeats will have security enabled.
  syncstatusstrictmode:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - strict mode for sync status of cluster. Depending on the the mode if there
        are any errors while applying config, sync status is displayed accordingly.
        By default the flag is disabled.
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
