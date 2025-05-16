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
---
module: channel_interface_binding
short_description: Binding Resource definition for describing association between
  channel and interface resources
description: Binding Resource definition for describing association between channel
  and interface resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  id:
    type: str
    description:
      - ID of the LA channel or the cluster LA channel to which you want to bind interfaces.
        Specify an LA channel in LA/x notation, where x can range from 1 to 8 or a
        cluster LA channel in CLA/x notation or  Link redundant channel in LR/x notation
        , where x can range from 1 to 4.
  ifnum:
    type: list
    description:
      - Interfaces to be bound to the LA channel of a Citrix ADC or to the LA channel
        of a cluster configuration.
      - For an LA channel of a Citrix ADC, specify an interface in C/U notation (for
        example, 1/3).
      - For an LA channel of a cluster configuration, specify an interface in N/C/U
        notation (for example, 2/1/3).
      - 'where C can take one of the following values:'
      - '* 0 - Indicates a management interface.'
      - '* 1 - Indicates a 1 Gbps port.'
      - '* 10 - Indicates a 10 Gbps port.'
      - U is a unique integer for representing an interface in a particular port group.
      - N is the ID of the node to which an interface belongs in a cluster configuration.
      - Use spaces to separate multiple entries.
    elements: str
  svmcmd:
    type: float
    description:
      - New attribute added to identify the source of cmd, when SVM fires the nitro
        cmd, it will set the value of SVMCMD to be 1.
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
