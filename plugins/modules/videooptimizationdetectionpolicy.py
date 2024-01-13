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
module: videooptimizationdetectionpolicy
short_description: Configuration for videooptimization detectionpolicy resource.
description: Configuration for videooptimization detectionpolicy resource.
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
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  action:
    type: str
    description:
      - 'Name of the videooptimization detection action to perform if the request
        matches this videooptimization detection policy. Built-in actions should be
        used. These are:'
      - '* DETECT_CLEARTEXT_PD - Cleartext PD is detected and increment related counters.'
      - '* DETECT_CLEARTEXT_ABR - Cleartext ABR is detected and increment related
        counters.'
      - '* DETECT_ENCRYPTED_ABR - Encrypted ABR is detected and increment related
        counters.'
      - '* TRIGGER_ENC_ABR_DETECTION - This is potentially encrypted ABR. Internal
        traffic heuristics algorithms will further process traffic to confirm detection.'
      - '* TRIGGER_CT_ABR_BODY_DETECTION -  This is potentially cleartext ABR. Internal
        traffic heuristics algorithms will further process traffic to confirm detection.'
      - '* RESET - Reset the client connection by closing it.'
      - '* DROP - Drop the connection without sending a response.'
  comment:
    type: str
    description:
      - Any type of information about this videooptimization detection policy.
  logaction:
    type: str
    description:
      - Name of the messagelog action to use for requests that match this policy.
  name:
    type: str
    description:
      - Name for the videooptimization detection policy. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.Can be modified, removed or renamed.
  newname:
    type: str
    description:
      - New name for the videooptimization detection policy. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
  rule:
    type: str
    description:
      - Expression that determines which request or response match the video optimization
        detection policy.
      - ''
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
  undefaction:
    type: str
    description:
      - Action to perform if the result of policy evaluation is undefined (UNDEF).
        An UNDEF event indicates an internal error condition. Only the above built-in
        actions can be used.
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
