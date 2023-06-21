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
module: clusternodegroup
short_description: Configuration for Node group object type resource.
description: Configuration for Node group object type resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - Name of the nodegroup. The name uniquely identifies the nodegroup on the cluster.
    type: str
  priority:
    description:
      - Priority of Nodegroup. This priority is used for all the nodes bound to the
        nodegroup for Nodegroup selection
    type: int
  state:
    description:
      - State of the nodegroup. All the nodes binding to this nodegroup must have
        the same state. ACTIVE/SPARE/PASSIVE
    type: str
    choices:
      - ACTIVE
      - SPARE
      - PASSIVE
  sticky:
    description:
      - Only one node can be bound to nodegroup with this option enabled. It specifies
        whether to prempt the traffic for the entities bound to nodegroup when owner
        node goes down and rejoins the cluster.
      - '  * Enabled - When owner node goes down, backup node will become the owner
        node and takes the traffic for the entities bound to the nodegroup. When bound
        node rejoins the cluster, traffic for the entities bound to nodegroup will
        not be steered back to this bound node. Current owner will have the ownership
        till it goes down.'
      - '  * Disabled - When one of the nodes goes down, a non-nodegroup cluster node
        is picked up and acts as part of the nodegroup. When the original node of
        the nodegroup comes up, the backup node will be replaced.'
    type: str
    choices:
      - true
      - false
  strict:
    description:
      - Specifies whether cluster nodes, that are not part of the nodegroup, will
        be used as backup for the nodegroup.
      - '  * Enabled - When one of the nodes goes down, no other cluster node is picked
        up to replace it. When the node comes up, it will continue being part of the
        nodegroup.'
      - '  * Disabled - When one of the nodes goes down, a non-nodegroup cluster node
        is picked up and acts as part of the nodegroup. When the original node of
        the nodegroup comes up, the backup node will be replaced.'
    type: str
    choices:
      - true
      - false
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
