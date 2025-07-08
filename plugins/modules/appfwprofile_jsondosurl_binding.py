#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: appfwprofile_jsondosurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and jsondosurl resources
description: Binding Resource definition for describing association between appfwprofile
  and jsondosurl resources
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
  jsondosurl:
    type: str
    description:
      - The URL on which we need to enforce the specified JSON denial-of-service (JSONDoS)
        attack protections.
      - 'An JSON DoS configuration consists of the following items:'
      - '* URL. PCRE-format regular expression for the URL.'
      - '* Maximum-document-length-check toggle.  ON to enable this check, OFF to
        disable it.'
      - '* Maximum document length. Positive integer representing the maximum length
        of the JSON document.'
      - '* Maximum-container-depth-check toggle. ON to enable, OFF to disable.'
      - ' * Maximum container depth. Positive integer representing the maximum container
        depth of the JSON document.'
      - '* Maximum-object-key-count-check toggle. ON to enable, OFF to disable.'
      - '* Maximum object key count. Positive integer representing the maximum allowed
        number of keys in any of the  JSON object.'
      - '* Maximum-object-key-length-check toggle. ON to enable, OFF to disable.'
      - '* Maximum object key length. Positive integer representing the maximum allowed
        length of key in any of the  JSON object.'
      - '* Maximum-array-value-count-check toggle. ON to enable, OFF to disable.'
      - '* Maximum array value count. Positive integer representing the maximum allowed
        number of values in any of the JSON array.'
      - '* Maximum-string-length-check toggle. ON to enable, OFF to disable.'
      - '* Maximum string length. Positive integer representing the maximum length
        of string in JSON.'
  jsonmaxarraylength:
    type: int
    description:
      - Maximum array length in the any of JSON object. This check protects against
        arrays having large lengths.
  jsonmaxarraylengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max array value count check is C(ON) or C(OFF).
  jsonmaxcontainerdepth:
    type: int
    description:
      - Maximum allowed nesting depth  of JSON document. JSON allows one to nest the
        containers (object and array) in any order to any depth. This check protects
        against documents that have excessive depth of hierarchy.
  jsonmaxcontainerdepthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max depth check is C(ON) or C(OFF).
  jsonmaxdocumentlength:
    type: int
    description:
      - Maximum document length of JSON document, in bytes.
  jsonmaxdocumentlengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max document length check is C(ON) or C(OFF).
  jsonmaxobjectkeycount:
    type: int
    description:
      - Maximum key count in the any of JSON object. This check protects against objects
        that have large number of keys.
  jsonmaxobjectkeycountcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max object key count check is C(ON) or C(OFF).
  jsonmaxobjectkeylength:
    type: int
    description:
      - Maximum key length in the any of JSON object. This check protects against
        objects that have large keys.
  jsonmaxobjectkeylengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max object key length check is C(ON) or C(OFF).
  jsonmaxstringlength:
    type: int
    description:
      - Maximum string length in the JSON. This check protects against strings that
        have large length.
  jsonmaxstringlengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if JSON Max string value count check is C(ON) or C(OFF).
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
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample appfwprofile_jsondosurl_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure appfwprofile_jsondosurl_binding
      delegate_to: localhost
      netscaler.adc.appfwprofile_jsondosurl_binding:
        state: present
        name: webgoat_prof
        jsondosurl: .*
        jsonmaxcontainerdepthcheck: 'ON'
        jsonmaxdocumentlengthcheck: 'ON'
        jsonmaxobjectkeycountcheck: 'ON'
        jsonmaxobjectkeylengthcheck: 'ON'
        jsonmaxarraylengthcheck: 'ON'
        jsonmaxstringlengthcheck: 'ON'
        resourceid: 585e356d88315f169cda718947d7052f6425c6d6997648506b8036f04d1b880b
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
