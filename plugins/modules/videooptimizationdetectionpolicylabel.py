#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: videooptimizationdetectionpolicylabel
short_description: Configuration for videooptimization detection policy label resource.
description: Configuration for videooptimization detection policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about this videooptimization detection
        policy label.
  labelname:
    type: str
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
  newname:
    type: str
    description:
      - New name for the videooptimization detection policy label. Must begin with
        a letter, number, or the underscore character (_), and must contain only letters,
        numbers, and the hyphen (
      - -), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters.
  policylabeltype:
    type: str
    choices:
      - videoopt_req
      - videoopt_res
    description:
      - 'Type of responses sent by the policies bound to this policy label. Types
        are:'
      - '* HTTP - HTTP responses.'
      - '* OTHERTCP - NON-HTTP TCP responses.'
  videooptimizationdetectionpolicylabel_videooptimizationdetectionpolicy_binding:
    type: dict
    description: Bindings for videooptimizationdetectionpolicylabel_videooptimizationdetectionpolicy_binding
      resource
    suboptions:
      mode:
        type: str
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
