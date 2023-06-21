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
module: cmppolicylabel
short_description: Configuration for compression policy label resource.
description: Configuration for compression policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  labelname:
    description:
      - 'Name of the HTTP compression policy label. Must begin with a letter, number,
        or the underscore character (_). Additional characters allowed, after the
        first character, are the hyphen (-), period (.) pound sign (#), space ( ),
        at sign (@), equals (=), and colon (:). The name must be unique within the
        list of policy labels for compression policies. Can be renamed after the policy
        label is created. '
      - '            '
      - '            The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp policylabel" or 'my cmp policylabel').
    type: str
  newname:
    description:
      - New name for the compression policy label. Must begin with an ASCII alphabetic
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
      - '                        '
      - '                        The following requirement applies only to the Citrix
        ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cmp policylabel" or 'my cmp policylabel').
    type: str
  type:
    description:
      - Type of packets (request packets or response) against which to match the policies
        bound to this policy label.
    type: str
    choices:
      - REQ
      - RES
      - HTTPQUIC_REQ
      - HTTPQUIC_RES
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
