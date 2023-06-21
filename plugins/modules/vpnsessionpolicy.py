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
module: vpnsessionpolicy
short_description: Configuration for VPN session policy resource.
description: Configuration for VPN session policy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  action:
    description:
      - Action to be applied by the new session policy if the rule criteria are met.
    type: str
  name:
    description:
      - Name for the new session policy that is applied after the user logs on to
        Citrix Gateway.
    type: str
  rule:
    description:
      - Expression, or name of a named expression, specifying the traffic that matches
        the policy.
      - ''
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character. '
      - '* Alternatively, you can use single quotation marks to enclose the rule,
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
