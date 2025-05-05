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
module: rewriteaction
short_description: Configuration for rewrite action resource.
description: Configuration for rewrite action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  comment:
    type: str
    description:
      - Comment. Can be used to preserve information about this rewrite action.
  name:
    type: str
    description:
      - Name for the user-defined rewrite action. Must begin with a letter, number,
        or the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters. Can be changed after the rewrite policy is
        added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my rewrite action" or 'my rewrite action').
  newname:
    type: str
    description:
      - 'New name for the rewrite action. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed
        after the rewrite policy is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my rewrite action" or 'my rewrite action').
  refinesearch:
    type: str
    description:
      - 'Specify additional criteria to refine the results of the search. '
      - Always starts with the "extend(m,n)" operation, where 'm' specifies number
        of bytes to the left of selected data and 'n' specifies number of bytes to
        the right of selected data to extend the selected area.
      - You can use refineSearch only on body expressions, and for the INSERT_BEFORE_ALL,
        INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.
      - 'Example: -refineSearch ''EXTEND(10, 20).REGEX_SELECT(re~0x[0-9a-zA-Z]+~).'
  search:
    type: str
    description:
      - 'Search facility that is used to match multiple strings in the request or
        response. Used in the INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and
        DELETE_ALL action types. The following search types are supported:'
      - '* Text ("text(string)") - A literal string. Example: -search text("hello")'
      - '* Regular expression ("regex(re<delimiter>regular exp<delimiter>)") - Pattern
        that is used to match multiple strings in the request or response. The pattern
        may be a PCRE-format regular expression with a delimiter that consists of
        any printable ASCII non-alphanumeric character except for the underscore (_)
        and space ( ) that is not otherwise used in the expression. Example: -search
        regex(re~^hello*~) The preceding regular expression can use the tilde (~)
        as the delimiter because that character does not appear in the regular expression
        itself.'
      - '* XPath ("xpath(xp<delimiter>xpath expression<delimiter>)") - An XPath expression
        to search XML. The delimiter has the same rules as for regex. Example: -search
        xpath(xp%/a/b%)'
      - '* JSON ("xpath_json(xp<delimiter>xpath expression<delimiter>)") - An XPath
        expression to search JSON. The delimiter has the same rules as for regex.
        Example: -search xpath_json(xp%/a/b%)'
      - 'NOTE: JSON searches use the same syntax as XPath searches, but operate on
        JSON files instead of standard XML files.'
      - '* HTML ("xpath_html(xp<delimiter>xpath expression<delimiter>)") - An XPath
        expression to search HTML. The delimiter has the same rules as for regex.
        Example: -search xpath_html(xp%/html/body%)'
      - 'NOTE: HTML searches use the same syntax as XPath searches, but operate on
        HTML files instead of standard XML files; HTML 5 rules for the file syntax
        are used; HTML 4 and later are supported.'
      - '* Patset ("patset(patset)") - A predefined pattern set. Example: -search
        patset("patset1").'
      - '* Datset ("dataset(dataset)") - A predefined dataset. Example: -search dataset("dataset1").'
      - '* AVP ("avp(avp number)") - AVP number that is used to match multiple AVPs
        in a Diameter/Radius Message. Example: -search avp(999)'
      - ''
      - 'Note: for all these the TARGET prefix can be used in the replacement expression
        to specify the text that was selected by the -search parameter, optionally
        adjusted by the -refineSearch parameter.'
      - 'Example: TARGET.BEFORE_STR(",")'
  stringbuilderexpr:
    type: str
    description:
      - Expression that specifies the content to insert into the request or response
        at the specified location, or that replaces the specified string.
  target:
    type: str
    description:
      - Expression that specifies which part of the request or response to rewrite.
  type:
    type: str
    choices:
      - noop
      - delete
      - insert_http_header
      - delete_http_header
      - corrupt_http_header
      - insert_before
      - insert_after
      - replace
      - replace_http_res
      - delete_all
      - replace_all
      - insert_before_all
      - insert_after_all
      - clientless_vpn_encode
      - clientless_vpn_encode_all
      - clientless_vpn_decode
      - clientless_vpn_decode_all
      - insert_sip_header
      - delete_sip_header
      - corrupt_sip_header
      - replace_sip_res
      - replace_diameter_header_field
      - replace_dns_header_field
      - replace_dns_answer_section
      - replace_mqtt
      - delete_mqtt
      - insert_mqtt
      - insert_before_mqtt
      - insert_after_mqtt
    description:
      - 'Type of user-defined rewrite action. The information that you provide for,
        and the effect of, each type are as follows:: '
      - '* REPLACE <target> <string_builder_expr>. Replaces the string with the string-builder
        expression.'
      - '* REPLACE_ALL <target> <string_builder_expr> -search <search_expr>. In the
        request or response specified by <target>, replaces all occurrences of the
        string defined by <string_builder_expr> with the string defined by <search_expr>.'
      - '* REPLACE_HTTP_RES <string_builder_expr>. Replaces the complete HTTP response
        with the string defined by the string-builder expression.'
      - '* REPLACE_SIP_RES <target> - Replaces the complete SIP response with the
        string specified by <target>.'
      - '* INSERT_HTTP_HEADER <header_string_builder_expr> <contents_string_builder_expr>.
        Inserts the HTTP header specified by <header_string_builder_expr> and header
        contents specified by <contents_string_builder_expr>.'
      - '* DELETE_HTTP_HEADER <target>. Deletes the HTTP header specified by <target>.'
      - '* CORRUPT_HTTP_HEADER <target>. Replaces the header name of all occurrences
        of the HTTP header specified by <target> with a corrupted name, so that it
        will not be recognized by the receiver  Example: MY_HEADER is changed to MHEY_ADER.'
      - '* INSERT_BEFORE <target_expr> <string_builder_expr>. Finds the string specified
        in <target_expr> and inserts the string in <string_builder_expr> before it.'
      - '* INSERT_BEFORE_ALL <target> <string_builder_expr> -search <search_expr>.
        In the request or response specified by <target>, locates all occurrences
        of the string specified in <string_builder_expr> and inserts the string specified
        in <search_expr> before each.'
      - '* INSERT_AFTER <target_expr> <string_builder_expr>. Finds the string specified
        in <target_expr>, and inserts the string specified in <string_builder_expr>
        after it.'
      - '* INSERT_AFTER_ALL <target> <string_builder_expr> -search <search_expr>.
        In the request or response specified by <target>, locates all occurrences
        of the string specified by <string_builder_expr> and inserts the string specified
        by <search_expr> after each.'
      - '* DELETE <target>. Finds and deletes the specified target.'
      - '* DELETE_ALL <target> -search <string_builder_expr>. In the request or response
        specified by <target>, locates and deletes all occurrences of the string specified
        by <string_builder_expr>.'
      - '* REPLACE_DIAMETER_HEADER_FIELD <target> <field value>. In the request or
        response modify the header field specified by <target>. Use Diameter.req.flags.SET(<flag>)
        or Diameter.req.flags.UNSET<flag> as ''stringbuilderexpression'' to set or
        unset flags.'
      - '* REPLACE_DNS_HEADER_FIELD <target>. In the request or response modify the
        header field specified by <target>. '
      - '* REPLACE_DNS_ANSWER_SECTION <target>. Replace the DNS answer section in
        the response. This is currently applicable for A and AAAA records only. Use
        DNS.NEW_RRSET_A & DNS.NEW_RRSET_AAAA expressions to configure the new answer
        section.'
      - '* REPLACE_MQTT <target> <string_builder_expr> : Replace MQTT message fields
        specified in <target_expr> to the value specified in <string_builder_expr>'
      - '* INSERT_MQTT <string_builder_expr> : Insert the string_builder_expr to an
        appropriate packet field in the MQTT message.'
      - '* INSERT_AFTER_MQTT <target_expr> <string_builder_expr> : Insert a topic
        specified in <string_builder_expr> in the MQTT Subscribe or Unsubscribe message
        after the specified target_expr.'
      - '* INSERT_BEFORE_MQTT <target_expr> <string_builder_expr> : Insert a topic
        specified in <string_builder_expr> in the MQTT Subscribe or Unsubscribe message
        before the specified target_expr.'
      - '* DELETE_MQTT <target> : Deletes the specified target in the MQTT message.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample rewriteaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure rewriteaction
      delegate_to: localhost
      netscaler.adc.rewriteaction:
        state: present
        name: rw_act_insert_after_diameter_avp
        type: insert_after
        target: diameter.req.avp(345678)
        stringbuilderexpr: diameter.new_avp(3110, "Sayan Inserted AVP")
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
