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
module: appfwlearningdata
short_description: Configuration for learning data resource.
description: Configuration for learning data resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  as_scan_location_sql:
    type: str
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
    description:
      - Location of sql injection exception - form field, header or cookie.
  as_scan_location_xss:
    type: str
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
      - URL
    description:
      - Location of cross-site scripting exception - form field, header, cookie or
        url.
  as_value_expr_sql:
    type: str
    description:
      - SQL value expressions consistituting expressions for Keyword, SpecialString
        or Wildchar.
  as_value_expr_xss:
    type: str
    description:
      - XSS value expressions consistituting expressions for Tag, Attribute or Pattern.
  as_value_type_sql:
    type: str
    choices:
      - Keyword
      - SpecialString
      - Wildchar
    description:
      - SQL value type. C(Keyword), C(SpecialString) or C(Wildchar)
  as_value_type_xss:
    type: str
    choices:
      - Tag
      - Attribute
      - Pattern
    description:
      - XSS value type. (C(Tag) | C(Attribute) | C(Pattern))
  contenttype:
    type: str
    description:
      - Content Type Name.
  cookieconsistency:
    type: str
    description:
      - Cookie Name.
  creditcardnumber:
    type: str
    description:
      - The object expression that is to be excluded from safe commerce check.
  creditcardnumberurl:
    type: str
    description:
      - The url for which the list of credit card numbers are needed to be bypassed
        from inspection
  crosssitescripting:
    type: str
    description:
      - Cross-site scripting.
  csrfformoriginurl:
    type: str
    description:
      - CSRF Form Origin URL.
  csrftag:
    type: str
    description:
      - CSRF Form Action URL
  fieldconsistency:
    type: str
    description:
      - Form field name.
  fieldformat:
    type: str
    description:
      - Field format name.
  formactionurl_ff:
    type: str
    description:
      - Form action URL.
  formactionurl_ffc:
    type: str
    description:
      - Form action URL.
  formactionurl_sql:
    type: str
    description:
      - Form action URL.
  formactionurl_xss:
    type: str
    description:
      - Form action URL.
  profilename:
    type: str
    description:
      - Name of the profile.
  securitycheck:
    type: str
    choices:
      - startURL
      - cookieConsistency
      - fieldConsistency
      - crossSiteScripting
      - SQLInjection
      - fieldFormat
      - CSRFtag
      - XMLDoSCheck
      - XMLWSICheck
      - XMLAttachmentCheck
      - TotalXMLRequests
      - creditCardNumber
      - ContentType
    description:
      - Name of the security check.
  sqlinjection:
    type: str
    description:
      - Form field name.
  starturl:
    type: str
    description:
      - Start URL configuration.
  target:
    type: str
    description:
      - Target filename for data to be exported.
  totalxmlrequests:
    type: bool
    description:
      - Total XML requests.
  xmlattachmentcheck:
    type: str
    description:
      - XML Attachment Content-Type.
  xmldoscheck:
    type: str
    description:
      - XML Denial of Service check, one of
      - "\tMaxAttributes"
      - "\tMaxAttributeNameLength"
      - "\tMaxAttributeValueLength"
      - "\tMaxElementNameLength"
      - "\tMaxFileSize"
      - "\tMinFileSize"
      - "\tMaxCDATALength"
      - "\tMaxElements"
      - "\tMaxElementDepth"
      - "\tMaxElementChildren"
      - "\tNumDTDs"
      - "\tNumProcessingInstructions"
      - "\tNumExternalEntities"
      - "\tMaxEntityExpansions"
      - "\tMaxEntityExpansionDepth"
      - "\tMaxNamespaces"
      - "\tMaxNamespaceUriLength"
      - "\tMaxSOAPArraySize"
      - "\tMaxSOAPArrayRank"
  xmlwsicheck:
    type: str
    description:
      - Web Services Interoperability Rule ID.
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
