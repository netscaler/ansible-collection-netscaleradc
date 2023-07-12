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
module: videooptimizationdetectionaction
short_description: Configuration for videooptimization detectionaction resource.
description: Configuration for videooptimization detectionaction resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Comment. Any type of information about this video optimization detection action.
    type: str
  name:
    description:
      - Name for the video optimization detection action. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
    type: str
  newname:
    description:
      - New name for the videooptimization detection action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
    type: str
  type:
    choices:
      - clear_text_pd
      - clear_text_abr
      - encrypted_abr
      - trigger_enc_abr
      - trigger_body_detection
    description:
      - 'Type of video optimization action. Available settings function as follows:'
      - '* C(clear_text_pd) - Cleartext PD type is detected.'
      - '* C(clear_text_abr) - Cleartext ABR is detected.'
      - '* C(encrypted_abr) - Encrypted ABR is detected.'
      - '* C(trigger_enc_abr) - Possible encrypted ABR is detected.'
      - '* C(trigger_body_detection) - Possible cleartext ABR is detected. Triggers
        body content detection.'
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