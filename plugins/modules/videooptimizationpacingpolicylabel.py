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
module: videooptimizationpacingpolicylabel
short_description: Configuration for videooptimization pacing policy label resource.
description: Configuration for videooptimization pacing policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about this videooptimization pacing policy
        label.
    type: str
  labelname:
    description:
      - Name for the Video optimization pacing policy label. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (
      - .) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        Cannot be changed after the videooptimization pacing policy label is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my videooptimization pacing policy label" or
        my videooptimization pacing policy label').
    type: str
  newname:
    description:
      - New name for the videooptimization pacing policy label. Must begin with a
        letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (
      - -), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters.
    type: str
  policylabeltype:
    choices:
      - videoopt_req
      - videoopt_res
    description:
      - 'Type of responses sent by the policies bound to this policy label. Types
        are:'
      - '* HTTP - HTTP responses.'
      - '* OTHERTCP - NON-HTTP TCP responses.'
    type: str
    default: NS_PLTMAP_RSP_REQ
  videooptimizationpacingpolicylabel_videooptimizationpacingpolicy_binding:
    type: dict
    description: Bindings for videooptimizationpacingpolicylabel_videooptimizationpacingpolicy_binding
      resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
