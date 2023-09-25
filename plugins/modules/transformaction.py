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
  comment:
    description:
      - Any comments to preserve information about this URL Transformation action.
    type: str
  cookiedomainfrom:
    description:
      - Pattern that matches the domain to be transformed in Set-Cookie headers.
    type: str
  cookiedomaininto:
    description:
      - 'PCRE-format regular expression that describes the transformation to be performed
        on cookie domains that match the cookieDomainFrom pattern. '
      - 'NOTE: The cookie domain to be transformed is extracted from the request.'
    type: str
  name:
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
    type: str
  priority:
    description:
      - Positive integer specifying the priority of the action within the profile.
        A lower number specifies a higher priority. Must be unique within the list
        of actions bound to the profile. Policies are evaluated in the order of their
        priority numbers, and the first policy that matches is applied.
    type: float
  profilename:
    description:
      - Name of the URL Transformation profile with which to associate this action.
    type: str
  requrlfrom:
    description:
      - PCRE-format regular expression that describes the request URL pattern to be
        transformed.
    type: str
  requrlinto:
    description:
      - PCRE-format regular expression that describes the transformation to be performed
        on URLs that match the reqUrlFrom pattern.
    type: str
  resurlfrom:
    description:
      - PCRE-format regular expression that describes the response URL pattern to
        be transformed.
    type: str
  resurlinto:
    description:
      - PCRE-format regular expression that describes the transformation to be performed
        on URLs that match the resUrlFrom pattern.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable this action.
    type: str
    default: ENABLED
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
