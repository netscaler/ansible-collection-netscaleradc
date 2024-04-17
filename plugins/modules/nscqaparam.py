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
module: nscqaparam
short_description: Configuration for cqaparam resource.
description: Configuration for cqaparam resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  harqretxdelay:
    type: raw
    description:
      - HARQ retransmission delay (in ms).
  lr1coeflist:
    type: raw
    description:
      - coefficients values for Label1.
  lr1probthresh:
    type: raw
    description:
      - Probability threshold values for LR model to differentiate between NET1 and
        reset(NET2 and NET3).
  lr2coeflist:
    type: str
    description:
      - coefficients values for Label 2.
  lr2probthresh:
    type: float
    description:
      - Probability threshold values for LR model to differentiate between NET2 and
        NET3.
  minrttnet1:
    type: raw
    description:
      - MIN RTT (in ms) for the first network.
  minrttnet2:
    type: raw
    description:
      - MIN RTT (in ms) for the second network.
  minrttnet3:
    type: raw
    description:
      - MIN RTT (in ms) for the third network.
  net1cclscale:
    type: raw
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
  net1csqscale:
    type: raw
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
  net1label:
    type: raw
    description:
      - Name of the network label.
  net1logcoef:
    type: raw
    description:
      - Connection quality ranking Log coefficients of network 1.
  net2cclscale:
    type: raw
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
  net2csqscale:
    type: raw
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
  net2label:
    type: raw
    description:
      - Name of the network label 2.
  net2logcoef:
    type: raw
    description:
      - Connnection quality ranking Log coefficients of network 2.
  net3cclscale:
    type: raw
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
  net3csqscale:
    type: raw
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
  net3label:
    type: raw
    description:
      - Name of the network label 3.
  net3logcoef:
    type: raw
    description:
      - Connection quality ranking Log coefficients of network 3.
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
