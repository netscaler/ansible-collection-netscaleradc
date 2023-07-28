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
module: appfwprofile_jsondosurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and jsondosurl resources
description: Binding Resource definition for describing association between appfwprofile
  and jsondosurl resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  alertonly:
    choices:
      - true
      - false
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
  jsondosurl:
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
    type: str
  jsonmaxarraylength:
    description:
      - Maximum array length in the any of JSON object. This check protects against
        arrays having large lengths.
    type: int
    default: 10000
  jsonmaxarraylengthcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max array value count check is ON or OFF.
    type: str
  jsonmaxcontainerdepth:
    description:
      - Maximum allowed nesting depth  of JSON document. JSON allows one to nest the
        containers (object and array) in any order to any depth. This check protects
        against documents that have excessive depth of hierarchy.
    type: int
    default: 5
  jsonmaxcontainerdepthcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max depth check is ON or OFF.
    type: str
  jsonmaxdocumentlength:
    description:
      - Maximum document length of JSON document, in bytes.
    type: int
    default: 20000000
  jsonmaxdocumentlengthcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max document length check is ON or OFF.
    type: str
  jsonmaxobjectkeycount:
    description:
      - Maximum key count in the any of JSON object. This check protects against objects
        that have large number of keys.
    type: int
    default: 10000
  jsonmaxobjectkeycountcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max object key count check is ON or OFF.
    type: str
  jsonmaxobjectkeylength:
    description:
      - Maximum key length in the any of JSON object. This check protects against
        objects that have large keys.
    type: int
    default: 128
  jsonmaxobjectkeylengthcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max object key length check is ON or OFF.
    type: str
  jsonmaxstringlength:
    description:
      - Maximum string length in the JSON. This check protects against strings that
        have large length.
    type: int
    default: 1000000
  jsonmaxstringlengthcheck:
    choices:
      - true
      - false
    description:
      - State if JSON Max string value count check is ON or OFF.
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
