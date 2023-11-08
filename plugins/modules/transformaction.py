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
module: transformaction
short_description: Configuration for transform action resource.
description: Configuration for transform action resource.
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
  comment:
    type: str
    description:
      - Any comments to preserve information about this URL Transformation action.
  cookiedomainfrom:
    type: str
    description:
      - Pattern that matches the domain to be transformed in Set-Cookie headers.
  cookiedomaininto:
    type: str
    description:
      - 'PCRE-format regular expression that describes the transformation to be performed
        on cookie domains that match the cookieDomainFrom pattern. '
      - 'NOTE: The cookie domain to be transformed is extracted from the request.'
  name:
    type: str
    description:
      - Name for the URL transformation action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after the URL Transformation action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, my transform action or my transform action).
  priority:
    type: float
    description:
      - Positive integer specifying the priority of the action within the profile.
        A lower number specifies a higher priority. Must be unique within the list
        of actions bound to the profile. Policies are evaluated in the order of their
        priority numbers, and the first policy that matches is applied.
  profilename:
    type: str
    description:
      - Name of the URL Transformation profile with which to associate this action.
  requrlfrom:
    type: str
    description:
      - PCRE-format regular expression that describes the request URL pattern to be
        transformed.
  requrlinto:
    type: str
    description:
      - PCRE-format regular expression that describes the transformation to be performed
        on URLs that match the reqUrlFrom pattern.
  resurlfrom:
    type: str
    description:
      - PCRE-format regular expression that describes the response URL pattern to
        be transformed.
  resurlinto:
    type: str
    description:
      - PCRE-format regular expression that describes the transformation to be performed
        on URLs that match the resUrlFrom pattern.
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
