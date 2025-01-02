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
module: appfwprofile_xmldosurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and xmldosurl resources
description: Binding Resource definition for describing association between appfwprofile
  and xmldosurl resources
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
  xmlblockdtd:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML DTD is C(ON) or C(OFF). Protects against recursive Document Type
        Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have
        DTDs in messages.
  xmlblockexternalentities:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Block External Entities Check is C(ON) or C(OFF). Protects against
        XML External Entity (XXE) attacks that force applications to parse untrusted
        external entities (sources) in XML documents.
  xmlblockpi:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Block PI is C(ON) or C(OFF). Protects resources from denial of
        service attacks as SOAP messages cannot have processing instructions (PI)
        in messages.
  xmldosurl:
    type: str
    description:
      - XML DoS URL regular expression length.
  xmlmaxattributenamelength:
    type: float
    description:
      - Specify the longest name of any XML attribute. Protects against overflow attacks.
  xmlmaxattributenamelengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max attribute name length check is C(ON) or C(OFF).
  xmlmaxattributes:
    type: float
    description:
      - Specify maximum number of attributes per XML element. Protects against overflow
        attacks.
  xmlmaxattributescheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max attributes check is C(ON) or C(OFF).
  xmlmaxattributevaluelength:
    type: float
    description:
      - Specify the longest value of any XML attribute. Protects against overflow
        attacks.
  xmlmaxattributevaluelengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max atribute value length is C(ON) or C(OFF).
  xmlmaxchardatalength:
    type: float
    description:
      - Specify the maximum size of CDATA. Protects against overflow attacks and large
        quantities of unparsed data within XML messages.
  xmlmaxchardatalengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max CDATA length check is C(ON) or C(OFF).
  xmlmaxelementchildren:
    type: float
    description:
      - Specify the maximum number of children allowed per XML element. Protects against
        overflow attacks.
  xmlmaxelementchildrencheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element children check is C(ON) or C(OFF).
  xmlmaxelementdepth:
    type: float
    description:
      - Maximum nesting (depth) of XML elements. This check protects against documents
        that have excessive hierarchy depths.
  xmlmaxelementdepthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element depth check is C(ON) or C(OFF).
  xmlmaxelementnamelength:
    type: float
    description:
      - Specify the longest name of any element (including the expanded namespace)
        to protect against overflow attacks.
  xmlmaxelementnamelengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element name length check is C(ON) or C(OFF).
  xmlmaxelements:
    type: float
    description:
      - Specify the maximum number of XML elements allowed. Protects against overflow
        attacks.
  xmlmaxelementscheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max elements check is C(ON) or C(OFF).
  xmlmaxentityexpansiondepth:
    type: float
    description:
      - Specify maximum entity expansion depth. Protects aganist Entity Expansion
        Attack.
  xmlmaxentityexpansiondepthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max Entity Expansions Depth Check is C(ON) or C(OFF).
  xmlmaxentityexpansions:
    type: float
    description:
      - Specify maximum allowed number of entity expansions. Protects aganist Entity
        Expansion Attack.
  xmlmaxentityexpansionscheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max Entity Expansions Check is C(ON) or C(OFF).
  xmlmaxfilesize:
    type: float
    description:
      - Specify the maximum size of XML messages. Protects against overflow attacks.
  xmlmaxfilesizecheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max file size check is C(ON) or C(OFF).
  xmlmaxnamespaces:
    type: float
    description:
      - Specify maximum number of active namespaces. Protects against overflow attacks.
  xmlmaxnamespacescheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max namespaces check is C(ON) or C(OFF).
  xmlmaxnamespaceurilength:
    type: float
    description:
      - Specify the longest URI of any XML namespace. Protects against overflow attacks.
  xmlmaxnamespaceurilengthcheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max namespace URI length check is C(ON) or C(OFF).
  xmlmaxnodes:
    type: float
    description:
      - Specify the maximum number of XML nodes. Protects against overflow attacks.
  xmlmaxnodescheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max nodes check is C(ON) or C(OFF).
  xmlmaxsoaparrayrank:
    type: float
    description:
      - XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
  xmlmaxsoaparraysize:
    type: float
    description:
      - XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
  xmlminfilesize:
    type: float
    description:
      - Enforces minimum message size.
  xmlminfilesizecheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Min file size check is C(ON) or C(OFF).
  xmlsoaparraycheck:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML SOAP Array check is C(ON) or C(OFF).
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
