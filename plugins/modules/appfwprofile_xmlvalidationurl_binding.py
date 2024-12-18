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
---
module: appfwprofile_xmlvalidationurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and xmlvalidationurl resources
description: Binding Resource definition for describing association between appfwprofile
  and xmlvalidationurl resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  alertonly:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send SNMP alert?
  comment:
    type: str
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
  isautodeployed:
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
    description:
      - Is the rule auto deployed by dynamic profile ?
  name:
    type: str
    description:
      - Name of the profile to which to bind an exemption or rule.
  resourceid:
    type: str
    description:
      - A "id" that identifies the rule.
  ruletype:
    type: str
    choices:
      - ALLOW
      - DENY
    description:
      - Specifies rule type of binding
  xmladditionalsoapheaders:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow addtional soap headers.
  xmlendpointcheck:
    type: str
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
  xmlrequestschema:
    type: str
    description:
      - XML Schema object for request validation .
  xmlresponseschema:
    type: str
    description:
      - XML Schema object for response validation.
  xmlvalidateresponse:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Validate response message.
  xmlvalidatesoapenvelope:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Validate SOAP Evelope only.
  xmlvalidationurl:
    type: str
    description:
      - XML Validation URL regular expression.
  xmlwsdl:
    type: str
    description:
      - WSDL object for soap request validation.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appfwprofile_xmlvalidationurl_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwprofile_xmlvalidationurl_binding
      delegate_to: localhost
      netscaler.adc.appfwprofile_xmlvalidationurl_binding:
        state: present
        name: XMLSchema_2
        xmlvalidationurl: .*
        xmlrequestschema: Xml_Schema_2
        xmlresponseschema: Xml_Schema_2
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
