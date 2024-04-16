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
module: snmpmib
short_description: Configuration for SNMP mib resource.
description: Configuration for SNMP mib resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  contact:
    type: raw
    description:
      - Name of the administrator for this Citrix ADC. Along with the name, you can
        include information on how to contact this person, such as a phone number
        or an email address. Can consist of 1 to 127 characters that include uppercase
        and  lowercase letters, numbers, and the hyphen (-), period (.) pound (#),
        space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the information includes one or more spaces, enclose it in double or single
        quotation marks (for example, "my contact" or 'my contact').
  customid:
    type: raw
    description:
      - Custom identification number for the Citrix ADC. Can consist of 1 to 127 characters
        that include uppercase and lowercase letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        (_) characters. You should choose a custom identification that helps identify
        the Citrix ADC appliance.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the ID includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my ID" or 'my ID').
  location:
    type: raw
    description:
      - Physical location of the Citrix ADC. For example, you can specify building
        name, lab number, and rack number. Can consist of 1 to 127 characters that
        include uppercase and lowercase letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        (_) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the location includes one or more spaces, enclose it in double or single
        quotation marks (for example, "my location" or 'my location').
  name:
    type: raw
    description:
      - Name for this Citrix ADC. Can consist of 1 to 127 characters that include
        uppercase and lowercase letters, numbers, and the hyphen (-), period (.) pound
        (#), space ( ), at sign (@), equals (=), colon (:), and underscore (_) characters.  You
        should choose a name that helps identify the Citrix ADC appliance.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose it in double or single quotation
        marks (for example, "my name" or 'my name').
  ownernode:
    type: raw
    description:
      - ID of the cluster node for which we are setting the mib. This is a mandatory
        argument to set snmp mib on CLIP.
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
