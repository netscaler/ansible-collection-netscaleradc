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
module: sslcipher_sslciphersuite_binding
short_description: Binding Resource definition for describing association between
  sslcipher and sslciphersuite resources
description: Binding Resource definition for describing association between sslcipher
  and sslciphersuite resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ciphergroupname:
    description:
      - Name for the user-defined cipher group. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the cipher group is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my ciphergroup" or 'my ciphergroup').
    type: str
  ciphername:
    description:
      - Cipher name.
    type: str
  cipheroperation:
    choices:
      - ADD
      - REM
      - ORD
    description:
      - The operation that is performed when adding the cipher-suite.
      - ''
      - 'Possible cipher operations are:'
      - "\tC(ADD) - Appends the given cipher-suite to the existing one configured\
        \ for the virtual server."
      - "\tC(REM) - Removes the given cipher-suite from the existing one configured\
        \ for the virtual server."
      - "\tC(ORD) - Overrides the current configured cipher-suite for the virtual\
        \ server with the given cipher-suite."
    type: str
  cipherpriority:
    description:
      - This indicates priority assigned to the particular cipher
    type: float
  ciphgrpals:
    description:
      - A cipher-suite can consist of an individual cipher name, the system predefined
        cipher-alias name, or user defined cipher-group name.
    type: str
  description:
    description:
      - Cipher suite description.
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
