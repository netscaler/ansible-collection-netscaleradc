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
module: lbaction
short_description: Configuration for lb action resource.
description: Configuration for lb action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Comment. Any type of information about this LB action.
    type: str
  name:
    description:
      - 'Name for the LB action. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my lb action" or 'my lb action').
    type: str
  newname:
    description:
      - New name for the LB action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my lb action" or my lb action').
    type: str
  type:
    description:
      - 'Type of an LB action. Available settings function as follows:'
      - '* NOLBACTION - Does not consider LB action in making LB decision.'
      - '* SELECTIONORDER - services bound to vserver with order specified in value
        parameter is considerd for lb/gslb decision.'
    type: str
    choices:
      - NOLBACTION
      - SELECTIONORDER
  value:
    description:
      - 'The selection order list used during lb/gslb decision. Preference of services
        during lb/gslb decision is as follows - services corresponding to first order
        specified in the sequence is considered first, services corresponding to second
        order specified in the sequence is considered next and so on. For example,
        if -value 2 1 3 is specified here and service-1 bound to a vserver with order
        1, service-2 bound to a vserver with order 2 and  service-3 bound to a vserver
        with order 3. Then preference of selecting services in LB decision is as follows:
        service-2, service-1, service-3.'
    type: list
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