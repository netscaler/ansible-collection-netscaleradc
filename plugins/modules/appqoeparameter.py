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
module: appqoeparameter
short_description: Configuration for QOS parameter resource.
description: Configuration for QOS parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  avgwaitingclient:
    description:
      - average number of client connections, that can sit in service waiting queue
    type: int
    default: 1000000
  dosattackthresh:
    description:
      - average number of client connection that can queue up on vserver level without
        triggering DoS mitigation module
    type: int
    default: 2000
  maxaltrespbandwidth:
    description:
      - maximum bandwidth which will determine whether to send alternate content response
    type: int
    default: 100
  sessionlife:
    description:
      - Time, in seconds, between the first time and the next time the AppQoE alternative
        content window is displayed. The alternative content window is displayed only
        once during a session for the same browser accessing a configured URL, so
        this parameter determines the length of a session.
    type: int
    default: 300
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
