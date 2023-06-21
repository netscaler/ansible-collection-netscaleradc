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
module: nspartition
short_description: Configuration for admin partition resource.
description: Configuration for admin partition resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  force:
    description:
      - Switches to new admin partition without prompt for saving configuration. Configuration
        will not be saved
    type: bool
  maxbandwidth:
    description:
      - Maximum bandwidth, in Kbps, that the partition can consume. A zero value indicates
        the bandwidth is unrestricted on the partition and it can consume up to the
        system limits.
    type: int
    default: 10240
  maxconn:
    description:
      - Maximum number of concurrent connections that can be open in the partition.
        A zero value indicates no limit on number of open connections.
    type: int
    default: 1024
  maxmemlimit:
    description:
      - Maximum memory, in megabytes, allocated to the partition.  A zero value indicates
        the memory is unlimited on the partition and it can consume up to the system
        limits.
    type: int
    default: 10
  minbandwidth:
    description:
      - Minimum bandwidth, in Kbps, that the partition can consume. A zero value indicates
        the bandwidth is unrestricted on the partition and it can consume up to the
        system limits
    type: int
    default: 10240
  partitionmac:
    description:
      - Special MAC address for the partition which is used for communication over
        shared vlans in this partition. If not specified, the MAC address is auto-generated.
    type: str
  partitionname:
    description:
      - Name of the Partition. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
    type: str
  save:
    description:
      - Switches to new admin partition without prompt for saving configuration. Configuration
        will be saved
    type: bool
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
