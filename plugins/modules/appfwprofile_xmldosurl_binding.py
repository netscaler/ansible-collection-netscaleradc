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
module: appfwprofile_xmldosurl_binding
short_description: Binding Resource definition for describing association between
  appfwprofile and xmldosurl resources
description: Binding Resource definition for describing association between appfwprofile
  and xmldosurl resources
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
  xmlblockdtd:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML DTD is C(ON) or C(OFF). Protects against recursive Document Type
        Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have
        DTDs in messages.
    type: str
  xmlblockexternalentities:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Block External Entities Check is C(ON) or C(OFF). Protects against
        XML External Entity (XXE) attacks that force applications to parse untrusted
        external entities (sources) in XML documents.
    type: str
  xmlblockpi:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Block PI is C(ON) or C(OFF). Protects resources from denial of
        service attacks as SOAP messages cannot have processing instructions (PI)
        in messages.
    type: str
  xmldosurl:
    description:
      - XML DoS URL regular expression length.
    type: str
  xmlmaxattributenamelength:
    description:
      - Specify the longest name of any XML attribute. Protects against overflow attacks.
    type: float
  xmlmaxattributenamelengthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max attribute name length check is C(ON) or C(OFF).
    type: str
  xmlmaxattributes:
    description:
      - Specify maximum number of attributes per XML element. Protects against overflow
        attacks.
    type: float
  xmlmaxattributescheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max attributes check is C(ON) or C(OFF).
    type: str
  xmlmaxattributevaluelength:
    description:
      - Specify the longest value of any XML attribute. Protects against overflow
        attacks.
    type: float
  xmlmaxattributevaluelengthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max atribute value length is C(ON) or C(OFF).
    type: str
  xmlmaxchardatalength:
    description:
      - Specify the maximum size of CDATA. Protects against overflow attacks and large
        quantities of unparsed data within XML messages.
    type: float
  xmlmaxchardatalengthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max CDATA length check is C(ON) or C(OFF).
    type: str
  xmlmaxelementchildren:
    description:
      - Specify the maximum number of children allowed per XML element. Protects against
        overflow attacks.
    type: float
  xmlmaxelementchildrencheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element children check is C(ON) or C(OFF).
    type: str
  xmlmaxelementdepth:
    description:
      - Maximum nesting (depth) of XML elements. This check protects against documents
        that have excessive hierarchy depths.
    type: float
  xmlmaxelementdepthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element depth check is C(ON) or C(OFF).
    type: str
  xmlmaxelementnamelength:
    description:
      - Specify the longest name of any element (including the expanded namespace)
        to protect against overflow attacks.
    type: float
  xmlmaxelementnamelengthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max element name length check is C(ON) or C(OFF).
    type: str
  xmlmaxelements:
    description:
      - Specify the maximum number of XML elements allowed. Protects against overflow
        attacks.
    type: float
  xmlmaxelementscheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max elements check is C(ON) or C(OFF).
    type: str
  xmlmaxentityexpansiondepth:
    description:
      - Specify maximum entity expansion depth. Protects aganist Entity Expansion
        Attack.
    type: float
  xmlmaxentityexpansiondepthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max Entity Expansions Depth Check is C(ON) or C(OFF).
    type: str
  xmlmaxentityexpansions:
    description:
      - Specify maximum allowed number of entity expansions. Protects aganist Entity
        Expansion Attack.
    type: float
  xmlmaxentityexpansionscheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max Entity Expansions Check is C(ON) or C(OFF).
    type: str
  xmlmaxfilesize:
    description:
      - Specify the maximum size of XML messages. Protects against overflow attacks.
    type: float
  xmlmaxfilesizecheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max file size check is C(ON) or C(OFF).
    type: str
  xmlmaxnamespaces:
    description:
      - Specify maximum number of active namespaces. Protects against overflow attacks.
    type: float
  xmlmaxnamespacescheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max namespaces check is C(ON) or C(OFF).
    type: str
  xmlmaxnamespaceurilength:
    description:
      - Specify the longest URI of any XML namespace. Protects against overflow attacks.
    type: float
  xmlmaxnamespaceurilengthcheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max namespace URI length check is C(ON) or C(OFF).
    type: str
  xmlmaxnodes:
    description:
      - Specify the maximum number of XML nodes. Protects against overflow attacks.
    type: float
  xmlmaxnodescheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Max nodes check is C(ON) or C(OFF).
    type: str
  xmlmaxsoaparrayrank:
    description:
      - XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
    type: float
  xmlmaxsoaparraysize:
    description:
      - XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
    type: float
  xmlminfilesize:
    description:
      - Enforces minimum message size.
    type: float
  xmlminfilesizecheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML Min file size check is C(ON) or C(OFF).
    type: str
  xmlsoaparraycheck:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - State if XML SOAP Array check is C(ON) or C(OFF).
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
