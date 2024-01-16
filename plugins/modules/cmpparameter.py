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
module: cmpparameter
short_description: Configuration for CMP parameter resource.
description: Configuration for CMP parameter resource.
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
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  addvaryheader:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Control insertion of the Vary header in HTTP responses compressed by Citrix
        ADC. Intermediate caches store different versions of the response for different
        values of the headers present in the Vary response header.
  cmpbypasspct:
    type: float
    description:
      - 'Citrix ADC CPU threshold after which compression is not performed. Range:
        0 - 100'
  cmplevel:
    type: str
    choices:
      - optimal
      - bestspeed
      - bestcompression
    description:
      - 'Specify a compression level. Available settings function as follows:'
      - ' * Optimal - Corresponds to a gzip GZIP level of 5-7.'
      - ' * Best speed - Corresponds to a gzip level of 1.'
      - ' * Best compression - Corresponds to a gzip level of 9.'
  cmponpush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Citrix ADC does not wait for the quantum to be filled before starting to compress
        data. Upon receipt of a packet with a PUSH flag, the appliance immediately
        begins compression of the accumulated packets.
  externalcache:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - 'Enable insertion of  Cache-Control: private response directive to indicate
        response message is intended for a single user and must not be cached by a
        shared or proxy cache.'
  heurexpiry:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Heuristic basefile expiry.
  heurexpiryhistwt:
    type: float
    description:
      - For heuristic basefile expiry, weightage to be given to historical delta compression
        ratio, specified as percentage.  For example, to give 25% weightage to historical
        ratio (and therefore 75% weightage to the ratio for current delta compression
        transaction), specify 25.
  heurexpirythres:
    type: float
    description:
      - Threshold compression ratio for heuristic basefile expiry, multiplied by 100.
        For example, to set the threshold ratio to 1.25, specify 125.
  minressize:
    type: float
    description:
      - Smallest response size, in bytes, to be compressed.
  policytype:
    type: str
    choices:
      - ADVANCED
    description:
      - Type of the policy. The only possible value is C(ADVANCED)
  quantumsize:
    type: float
    description:
      - Minimum quantum of data to be filled before compression begins.
  servercmp:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow the server to send compressed data to the Citrix ADC. With the default
        setting, the Citrix ADC appliance handles all compression.
  varyheadervalue:
    type: str
    description:
      - The value of the HTTP Vary header for compressed responses. If this argument
        is not specified, a default value of "Accept-Encoding" will be used.
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
