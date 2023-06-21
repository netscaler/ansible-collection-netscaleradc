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
module: videooptimizationdetectionpolicylabel
short_description: Configuration for videooptimization detection policy label resource.
description: Configuration for videooptimization detection policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about this videooptimization detection
        policy label.
    type: str
  labelname:
    description:
      - Name for the Video optimization detection policy label. Must begin with a
        letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (-), period (
      - .) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        Cannot be changed after the videooptimization detection policy label is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my videooptimization detection policy label"
        or my videooptimization detection policy label').
    type: str
  newname:
    description:
      - New name for the videooptimization detection policy label. Must begin with
        a letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (
      - -), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters.
    type: str
  policylabeltype:
    description:
      - 'Type of responses sent by the policies bound to this policy label. Types
        are:'
      - '* HTTP - HTTP responses.'
      - '* OTHERTCP - NON-HTTP TCP responses.'
    type: str
    default: NS_PLTMAP_RSP_REQ
    choices:
      - videoopt_req
      - videoopt_res
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
