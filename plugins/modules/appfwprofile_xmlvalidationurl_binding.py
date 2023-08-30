#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: appfwprofile_xmlvalidationurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and xmlvalidationurl resources
description: Binding Resource definition for describing association between appfwprofile
  and xmlvalidationurl resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  alertonly:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send SNMP alert?
    type: str
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  isautodeployed:
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
    description:
      - Is the rule auto deployed by dynamic profile ?
    type: str
  name:
    description:
      - Name of the profile to which to bind an exemption or rule.
    type: str
  resourceid:
    description:
      - A "id" that identifies the rule.
    type: str
  ruletype:
    choices:
      - ALLOW
      - DENY
    description:
      - Specifies rule type of binding
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enabled.
    type: str
  xmladditionalsoapheaders:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow addtional soap headers.
    type: str
  xmlendpointcheck:
    choices:
      - ABSOLUTE
      - RELATIVE
    description:
      - Modifies the behaviour of the Request URL validation w.r.t. the Service URL.
      - "\tIf set to C(ABSOLUTE), the entire request URL is validated with the entire\
        \ URL mentioned in Service of the associated WSDL."
      - "\t\teg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService\
        \ would FAIL the validation."
      - "\tIf set to RELAIVE, only the non-hostname part of the request URL is validated\
        \ against the non-hostname part of the Service URL."
      - "\t\teg: Service URL: http://example.org/ExampleService, Request URL: http//example.com/ExampleService\
        \ would PASS the validation."
    type: str
  xmlrequestschema:
    description:
      - XML Schema object for request validation .
    type: str
  xmlresponseschema:
    description:
      - XML Schema object for response validation.
    type: str
  xmlvalidateresponse:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Validate response message.
    type: str
  xmlvalidatesoapenvelope:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Validate SOAP Evelope only.
    type: str
  xmlvalidationurl:
    description:
      - XML Validation URL regular expression.
    type: str
  xmlwsdl:
    description:
      - WSDL object for soap request validation.
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
