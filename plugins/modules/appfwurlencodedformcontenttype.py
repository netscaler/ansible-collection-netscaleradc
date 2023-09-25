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
module: appfwurlencodedformcontenttype
short_description: Configuration for Urlencoded form content type resource.
description: Configuration for Urlencoded form content type resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  isregex:
    choices:
      - REGEX
      - NOTREGEX
    description:
      - Is urlencoded form content type a regular expression?
    type: str
    default: NOTREGEX
  urlencodedformcontenttypevalue:
    description:
      - Content type to be classified as urlencoded form
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | appfwurlEncodedFormContentType
      delegate_to: localhost
      netscaler.adc.appfwurlencodedformcontenttype:
        state: present
        urlencodedformcontenttypevalue: application/x-www-form-urlencoded
    - name: Sample Task | appfwurlEncodedFormContentType | 2
      delegate_to: localhost
      netscaler.adc.appfwurlencodedformcontenttype:
        state: present
        urlencodedformcontenttypevalue: application/x-www-form-urlencoded.*
        isregex: REGEX

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
