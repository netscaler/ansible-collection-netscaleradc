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
module: nscqaparam
short_description: Configuration for cqaparam resource.
description: Configuration for cqaparam resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  harqretxdelay:
    description:
      - HARQ retransmission delay (in ms).
    type: int
  lr1coeflist:
    description:
      - coefficients values for Label1.
    type: str
  lr1probthresh:
    description:
      - Probability threshold values for LR model to differentiate between NET1 and
        reset(NET2 and NET3).
    type: int
  lr2coeflist:
    description:
      - coefficients values for Label 2.
    type: str
  lr2probthresh:
    description:
      - Probability threshold values for LR model to differentiate between NET2 and
        NET3.
    type: int
  minrttnet1:
    description:
      - MIN RTT (in ms) for the first network.
    type: int
  minrttnet2:
    description:
      - MIN RTT (in ms) for the second network.
    type: int
  minrttnet3:
    description:
      - MIN RTT (in ms) for the third network.
    type: int
  net1cclscale:
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
    type: str
  net1csqscale:
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
    type: str
  net1label:
    description:
      - Name of the network label.
    type: str
  net1logcoef:
    description:
      - Connection quality ranking Log coefficients of network 1.
    type: str
  net2cclscale:
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
    type: str
  net2csqscale:
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
    type: str
  net2label:
    description:
      - Name of the network label 2.
    type: str
  net2logcoef:
    description:
      - Connnection quality ranking Log coefficients of network 2.
    type: str
  net3cclscale:
    description:
      - Three congestion level scores limits corresponding to None, Low, Medium.
    type: str
  net3csqscale:
    description:
      - Three signal quality level scores limits corresponding to Excellent, Good,
        Fair.
    type: str
  net3label:
    description:
      - Name of the network label 3.
    type: str
  net3logcoef:
    description:
      - Connection quality ranking Log coefficients of network 3.
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
