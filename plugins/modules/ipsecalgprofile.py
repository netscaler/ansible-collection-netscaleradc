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
module: ipsecalgprofile
short_description: Configuration for IPSEC ALG profile resource.
description: Configuration for IPSEC ALG profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  connfailover:
    description:
      - Mode in which the connection failover feature must operate for the IPSec Alg.
        After a failover, established UDP connections and ESP packet flows are kept
        active and resumed on the secondary appliance. Recomended setting is ENABLED.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  espgatetimeout:
    description:
      - Timeout ESP in seconds as no ESP packets are seen after IKE negotiation
    type: int
    default: 30
  espsessiontimeout:
    description:
      - ESP session timeout in minutes.
    type: int
    default: 60
  ikesessiontimeout:
    description:
      - IKE session timeout in minutes
    type: int
    default: 60
  name:
    description:
      - The name of the ipsec alg profile
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