#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

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
    description:
      - Send SNMP alert?
    type: str
    choices:
      - true
      - false
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  isautodeployed:
    description:
      - Is the rule auto deployed by dynamic profile ?
    type: str
    choices:
      - AUTODEPLOYED
      - NOTAUTODEPLOYED
  name:
    description:
      - Name of the profile to which to bind an exemption or rule.
    type: str
  resourceid:
    description:
      - A "id" that identifies the rule.
    type: str
  ruletype:
    description:
      - Specifies rule type of binding
    type: str
    choices:
      - ALLOW
      - DENY
  state:
    description:
      - Enabled.
    type: str
    choices:
      - ENABLED
      - DISABLED
  xmlblockdtd:
    description:
      - State if XML DTD is ON or OFF. Protects against recursive Document Type Declaration
        (DTD) entity expansion attacks. Also, SOAP messages cannot have DTDs in messages.
    type: str
    choices:
      - true
      - false
  xmlblockexternalentities:
    description:
      - State if XML Block External Entities Check is ON or OFF. Protects against
        XML External Entity (XXE) attacks that force applications to parse untrusted
        external entities (sources) in XML documents.
    type: str
    choices:
      - true
      - false
  xmlblockpi:
    description:
      - State if XML Block PI is ON or OFF. Protects resources from denial of service
        attacks as SOAP messages cannot have processing instructions (PI) in messages.
    type: str
    choices:
      - true
      - false
  xmldosurl:
    description:
      - XML DoS URL regular expression length.
    type: str
  xmlmaxattributenamelength:
    description:
      - Specify the longest name of any XML attribute. Protects against overflow attacks.
    type: int
  xmlmaxattributenamelengthcheck:
    description:
      - State if XML Max attribute name length check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxattributes:
    description:
      - Specify maximum number of attributes per XML element. Protects against overflow
        attacks.
    type: int
  xmlmaxattributescheck:
    description:
      - State if XML Max attributes check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxattributevaluelength:
    description:
      - Specify the longest value of any XML attribute. Protects against overflow
        attacks.
    type: int
  xmlmaxattributevaluelengthcheck:
    description:
      - State if XML Max atribute value length is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxchardatalength:
    description:
      - Specify the maximum size of CDATA. Protects against overflow attacks and large
        quantities of unparsed data within XML messages.
    type: int
  xmlmaxchardatalengthcheck:
    description:
      - State if XML Max CDATA length check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxelementchildren:
    description:
      - Specify the maximum number of children allowed per XML element. Protects against
        overflow attacks.
    type: int
  xmlmaxelementchildrencheck:
    description:
      - State if XML Max element children check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxelementdepth:
    description:
      - Maximum nesting (depth) of XML elements. This check protects against documents
        that have excessive hierarchy depths.
    type: int
  xmlmaxelementdepthcheck:
    description:
      - State if XML Max element depth check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxelementnamelength:
    description:
      - Specify the longest name of any element (including the expanded namespace)
        to protect against overflow attacks.
    type: int
  xmlmaxelementnamelengthcheck:
    description:
      - State if XML Max element name length check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxelements:
    description:
      - Specify the maximum number of XML elements allowed. Protects against overflow
        attacks.
    type: int
  xmlmaxelementscheck:
    description:
      - State if XML Max elements check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxentityexpansiondepth:
    description:
      - Specify maximum entity expansion depth. Protects aganist Entity Expansion
        Attack.
    type: int
  xmlmaxentityexpansiondepthcheck:
    description:
      - State if XML Max Entity Expansions Depth Check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxentityexpansions:
    description:
      - Specify maximum allowed number of entity expansions. Protects aganist Entity
        Expansion Attack.
    type: int
  xmlmaxentityexpansionscheck:
    description:
      - State if XML Max Entity Expansions Check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxfilesize:
    description:
      - Specify the maximum size of XML messages. Protects against overflow attacks.
    type: int
  xmlmaxfilesizecheck:
    description:
      - State if XML Max file size check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxnamespaces:
    description:
      - Specify maximum number of active namespaces. Protects against overflow attacks.
    type: int
  xmlmaxnamespacescheck:
    description:
      - State if XML Max namespaces check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxnamespaceurilength:
    description:
      - Specify the longest URI of any XML namespace. Protects against overflow attacks.
    type: int
  xmlmaxnamespaceurilengthcheck:
    description:
      - State if XML Max namespace URI length check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxnodes:
    description:
      - Specify the maximum number of XML nodes. Protects against overflow attacks.
    type: int
  xmlmaxnodescheck:
    description:
      - State if XML Max nodes check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlmaxsoaparrayrank:
    description:
      - XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
    type: int
  xmlmaxsoaparraysize:
    description:
      - XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
    type: int
  xmlminfilesize:
    description:
      - Enforces minimum message size.
    type: int
  xmlminfilesizecheck:
    description:
      - State if XML Min file size check is ON or OFF.
    type: str
    choices:
      - true
      - false
  xmlsoaparraycheck:
    description:
      - State if XML SOAP Array check is ON or OFF.
    type: str
    choices:
      - true
      - false
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
