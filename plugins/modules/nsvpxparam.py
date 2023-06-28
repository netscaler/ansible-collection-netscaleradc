#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: nsvpxparam
short_description: Configuration for "VPX" resource.
description: Configuration for "VPX" resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  cpuyield:
    choices:
      - DEFAULT
      - true
      - false
    description:
      - This setting applicable in virtual appliances, is to affect the cpu yield(relinquishing
        the cpu resources) in any hypervised environment.
      - ''
      - '* There are 3 options for the behavior:'
      - 1. YES - Allow the Virtual Appliance to yield its vCPUs periodically, if there
        is no data traffic.
      - 2. NO - Virtual Appliance will not yield the vCPU.
      - 3. DEFAULT - Restores the default behaviour, according to the license.
      - ''
      - '* Its behavior in different scenarios:'
      - 1. As this setting is node specific only, it will not be propagated to other
        nodes, when executed on Cluster(CLIP) and HA(Primary).
      - 2. In cluster setup, use '-ownerNode' to specify ID of the cluster node.
      - 3. This setting is a system wide implementation and not granular to vCPUs.
      - 4. No effect on the management PE.
    type: str
    default: DEFAULT
  masterclockcpu1:
    choices:
      - true
      - false
    description:
      - This argument is deprecated.
    type: str
  ownernode:
    description:
      - ID of the cluster node for which you are setting the cpuyield. It can be configured
        only through the cluster IP address.
    type: int
    default: 255
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
