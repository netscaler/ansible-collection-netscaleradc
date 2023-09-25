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
  as_scan_location_sql:
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
    description:
      - Location of sql injection exception - form field, header or cookie.
    type: str
  as_scan_location_xss:
    choices:
      - FORMFIELD
      - HEADER
      - COOKIE
      - URL
    description:
      - Location of cross-site scripting exception - form field, header, cookie or
        url.
    type: str
  as_value_expr_sql:
    description:
      - SQL value expressions consistituting expressions for Keyword, SpecialString
        or Wildchar.
    type: str
  as_value_expr_xss:
    description:
      - XSS value expressions consistituting expressions for Tag, Attribute or Pattern.
    type: str
  as_value_type_sql:
    choices:
      - Keyword
      - SpecialString
      - Wildchar
    description:
      - SQL value type. C(Keyword), C(SpecialString) or C(Wildchar)
    type: str
  as_value_type_xss:
    choices:
      - Tag
      - Attribute
      - Pattern
    description:
      - XSS value type. (C(Tag) | C(Attribute) | C(Pattern))
    type: str
  contenttype:
    description:
      - Content Type Name.
    type: str
  cookieconsistency:
    description:
      - Cookie Name.
    type: str
  creditcardnumber:
    description:
      - The object expression that is to be excluded from safe commerce check.
    type: str
  creditcardnumberurl:
    description:
      - The url for which the list of credit card numbers are needed to be bypassed
        from inspection
    type: str
  crosssitescripting:
    description:
      - Cross-site scripting.
    type: str
  csrfformoriginurl:
    description:
      - CSRF Form Origin URL.
    type: str
  csrftag:
    description:
      - CSRF Form Action URL
    type: str
  fieldconsistency:
    description:
      - Form field name.
    type: str
  fieldformat:
    description:
      - Field format name.
    type: str
  formactionurl_ff:
    description:
      - Form action URL.
    type: str
  formactionurl_ffc:
    description:
      - Form action URL.
    type: str
  formactionurl_sql:
    description:
      - Form action URL.
    type: str
  formactionurl_xss:
    description:
      - Form action URL.
    type: str
  profilename:
    description:
      - Name of the profile.
    type: str
  securitycheck:
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
    type: str
  sqlinjection:
    description:
      - Form field name.
    type: str
  starturl:
    description:
      - Start URL configuration.
    type: str
  target:
    description:
      - Target filename for data to be exported.
    type: str
  totalxmlrequests:
    description:
      - Total XML requests.
    type: bool
  xmlattachmentcheck:
    description:
      - XML Attachment Content-Type.
    type: str
  xmldoscheck:
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
    type: str
  xmlwsicheck:
    description:
      - Web Services Interoperability Rule ID.
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
