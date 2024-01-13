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
module: iptunnelparam
short_description: Configuration for ip tunnel parameter resource.
description: Configuration for ip tunnel parameter resource.
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
  dropfrag:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Drop any IP packet that requires fragmentation before it is sent through the
        tunnel.
  dropfragcputhreshold:
    type: float
    description:
      - Threshold value, as a percentage of CPU usage, at which to drop packets that
        require fragmentation to use the IP tunnel. Applies only if dropFragparameter
        is set to NO. The default value, 0, specifies that this parameter is not set.
  enablestrictrx:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Strict PBR check for IPSec packets received through tunnel
  enablestricttx:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Strict PBR check for packets to be sent IPSec protected
  mac:
    type: str
    description:
      - The shared MAC used for shared IP between cluster nodes/HA peers
  srcip:
    type: str
    description:
      - Common source-IP address for all tunnels. For a specific tunnel, this global
        setting is overridden if you have specified another source IP address. Must
        be a MIP or SNIP address.
  srciproundrobin:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use a different source IP address for each new session through a particular
        IP tunnel, as determined by round robin selection of one of the SNIP addresses.
        This setting is ignored if a common global source IP address has been specified
        for all the IP tunnels. This setting does not apply to a tunnel for which
        a source IP address has been specified.
  useclientsourceip:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use client source IP as source IP for outer tunnel IP header
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
