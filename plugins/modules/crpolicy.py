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
module: crpolicy
short_description: Configuration for cache redirection policy resource.
description: Configuration for cache redirection policy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  action:
    description:
      - 'Name of the built-in cache redirection action: CACHE/ORIGIN.'
    type: str
  logaction:
    description:
      - The log action associated with the cache redirection policy
    type: str
  newname:
    description:
      - The new name of the content switching policy.
    type: str
  policyname:
    description:
      - Name for the cache redirection policy. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Cannot be changed after the policy is created.
      - 'The following requirement applies only to the Citrix ADC CLI: '
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policy" or 'my policy').
    type: str
  rule:
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '*  If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '*  If the expression itself includes double quotation marks, escape the quotations
        by using the \ character. '
      - '*  Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
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
