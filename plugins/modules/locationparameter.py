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
module: locationparameter
short_description: Configuration for location parameter resource.
description: Configuration for location parameter resource.
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
  context:
    type: raw
    choices:
      - geographic
      - custom
    description:
      - 'Context for describing locations. In C(geographic) context, qualifier labels
        are assigned by default in the following sequence: Continent.Country.Region.City.ISP.Organization.
        In C(custom) context, the qualifiers labels can have any meaning that you
        designate.'
  matchwildcardtoany:
    type: raw
    choices:
      - 'YES'
      - 'NO'
      - Expression
    description:
      - Indicates whether wildcard qualifiers should match any other
      - qualifier including non-wildcard while evaluating
      - location based expressions.
      - 'Possible values: Yes, No, C(Expression).'
      - '    Yes - Wildcard qualifiers match any other qualifiers.'
      - '    No  - Wildcard qualifiers do not match non-wildcard'
      - '          qualifiers, but match other wildcard qualifiers.'
      - '    C(Expression) - Wildcard qualifiers in an expression'
      - '          match any qualifier in an LDNS location,'
      - '          wildcard qualifiers in the LDNS location do not match'
      - '          non-wildcard qualifiers in an expression'
  q1label:
    type: raw
    description:
      - Label specifying the meaning of the first qualifier. Can be specified for
        custom context only.
  q2label:
    type: raw
    description:
      - Label specifying the meaning of the second qualifier. Can be specified for
        custom context only.
  q3label:
    type: raw
    description:
      - Label specifying the meaning of the third qualifier. Can be specified for
        custom context only.
  q4label:
    type: raw
    description:
      - Label specifying the meaning of the fourth qualifier. Can be specified for
        custom context only.
  q5label:
    type: raw
    description:
      - Label specifying the meaning of the fifth qualifier. Can be specified for
        custom context only.
  q6label:
    type: raw
    description:
      - Label specifying the meaning of the sixth qualifier. Can be specified for
        custom context only.
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
