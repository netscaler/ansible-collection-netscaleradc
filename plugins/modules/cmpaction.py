#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: cmpaction
short_description: Configuration for compression action resource.
description: Configuration for compression action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  addvaryheader:
    choices:
      - GLOBAL
      - DISABLED
      - ENABLED
    description:
      - Control insertion of the Vary header in HTTP responses compressed by Citrix
        ADC. Intermediate caches store different versions of the response for different
        values of the headers present in the Vary response header.
    type: str
    default: GLOBAL
  cmptype:
    choices:
      - compress
      - gzip
      - deflate
      - nocompress
    description:
      - 'Type of compression performed by this action. '
      - 'Available settings function as follows: '
      - '* COMPRESS - Apply GZIP or DEFLATE compression to the response, depending
        on the request header. Prefer GZIP.'
      - '* GZIP - Apply GZIP compression.'
      - '* DEFLATE - Apply DEFLATE compression.'
      - '* NOCOMPRESS - Do not C(compress) the response if the request matches a policy
        that uses this action.'
    type: str
  deltatype:
    choices:
      - PERURL
      - PERPOLICY
    description:
      - The type of delta action (if delta type compression action is defined).
    type: str
    default: PERURL
  name:
    description:
      - 'Name of the compression action. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the action is added. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp action" or 'my cmp action').
    type: str
  newname:
    description:
      - New name for the compression action. Must begin with an ASCII alphabetic or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at
      - '(@), equals (=), and hyphen (-) characters. '
      - 'Choose a name that can be correlated with the function that the action performs. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp action" or 'my cmp action').
    type: str
  varyheadervalue:
    description:
      - The value of the HTTP Vary header for compressed responses.
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
