#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


DOCUMENTATION = '''
---
module: citrix_adc_rewriteaction
short_description: Manage rewrite action configuration
description:
    - _

version_added: "2.4.0"

author: George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - >-
                Name for the user-defined rewrite action. Must begin with a letter, number, or the underscore
                character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
                ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the rewrite
                policy is added.

    type:
        choices:
            - 'noop'
            - 'delete'
            - 'insert_http_header'
            - 'delete_http_header'
            - 'corrupt_http_header'
            - 'insert_before'
            - 'insert_after'
            - 'replace'
            - 'replace_http_res'
            - 'delete_all'
            - 'replace_all'
            - 'insert_before_all'
            - 'insert_after_all'
            - 'clientless_vpn_encode'
            - 'clientless_vpn_encode_all'
            - 'clientless_vpn_decode'
            - 'clientless_vpn_decode_all'
            - 'insert_sip_header'
            - 'delete_sip_header'
            - 'corrupt_sip_header'
            - 'replace_sip_res'
            - 'replace_diameter_header_field'
            - 'replace_dns_header_field'
            - 'replace_dns_answer_section
        description:
            - >-
                Type of user-defined rewrite action. The information that you provide for, and the effect of, each
                type are as follows::

    target:
        description:
            - "Default syntax expression that specifies which part of the request or response to rewrite."

    stringbuilderexpr:
        description:
            - >-
                Default syntax expression that specifies the content to insert into the request or response at the
                specified location, or that replaces the specified string.

    pattern:
        description:
            - >-
                DEPRECATED in favor of -search: Pattern that is used to match multiple strings in the request or
                response. The pattern may be a string literal (without quotes) or a PCRE-format regular expression
                with a delimiter that consists of any printable ASCII non-alphanumeric character except for the
                underscore (_) and space ( ) that is not otherwise used in the expression. Example:
                re~https?://|HTTPS?://~ The preceding regular expression can use the tilde (~) as the delimiter
                because that character does not appear in the regular expression itself. Used in the
                INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types.

    search:
        description:
            - >-
                Search facility that is used to match multiple strings in the request or response. Used in the
                INSERT_BEFORE_ALL, INSERT_AFTER_ALL, REPLACE_ALL, and DELETE_ALL action types. The following search
                types are supported: text(), regex(), xpath(), xpath_json(), xpath_html(), patset(), dataset(), avp()

    bypasssafetycheck:
        description:
            - >-
                Bypass the safety check and allow unsafe expressions. An unsafe expression is one that contains
                references to message elements that might not be present in all messages. If an expression refers to
                a missing request element, an empty string is used instead.

    refinesearch:
        description:
            - "Specify additional criteria to refine the results of the search."

    comment:
        description:
            - "Comment. Can be used to preserve information about this rewrite action."

    newname:
        description:
            - "New name for the rewrite action."

    hits:
        description:
            - "The number of times the action has been taken."

    undefhits:
        description:
            - "The number of times the action resulted in UNDEF."

    referencecount:
        description:
            - "The number of references to the action."

    description:
        description:
            - "Description of the action."

    isdefault:
        description:
            - "A value of true is returned if it is a default rewriteaction."

    builtin:
        description:
            - "Flag to determine whether rewrite action is built-in or not."


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
# Create or update a rewrite action with citrix_adc_rewrite_action ansible module

- name: Setup basic rewrite action
  delegate_to: localhost
  register: result
  check_mode: "{{ check_mode }}"
  citrix_adc_rewrite_action:
    nitro_user: "{{nitro_user}}"
    nitro_pass: "{{nitro_pass}}"
    nsip: "{{nsip}}"

    state: present

    name: test-rewriteaction-1
    type: insert_http_header
    target: "client-IP"
    stringbuilderexpr: CLIENT.IP.SRC

# Delete an existing rewrite action

- name: Remove basic rewrite action
  delegate_to: localhost
  register: result
  check_mode: "{{ check_mode }}"
  citrix_adc_rewrite_action:
    nitro_user: "{{nitro_user}}"
    nitro_pass: "{{nitro_pass}}"
    nsip: "{{nsip}}"

    state: absent

    name: test-rewriteaction-1

'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
'''

import json

try:
    from nssrc.com.citrix.netscaler.nitro.resource.config.rewrite.rewriteaction import rewriteaction
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.citrix_adc.citrix_adc import (
    ConfigProxy,
    get_nitro_client,
    netscaler_common_arguments,
    log, loglines,
    ensure_feature_is_enabled,
    get_immutables_intersection
)


def rewriteaction_exists(client, module):
    if rewriteaction.count_filtered(client, 'name:%s' % module.params['name']) > 0:
        return True
    else:
        return False


def rewriteaction_identical(client, module, rewriteaction_proxy):
    if len(diff_list(client, module, rewriteaction_proxy)) == 0:
        return True
    else:
        return False


def diff_list(client, module, rewriteaction_proxy):
    action_list = rewriteaction.get_filtered(client, 'name:%s' % module.params['name'])
    diff_list = rewriteaction_proxy.diff_object(action_list[0])
    return diff_list

def main():

    module_specific_arguments = dict(
        name=dict(type='str'),
        type=dict(
            type='str',
            choices=[
                'noop',
                'delete',
                'insert_http_header',
                'delete_http_header',
                'corrupt_http_header',
                'insert_before',
                'insert_after',
                'replace',
                'replace_http_res',
                'delete_all',
                'replace_all',
                'insert_before_all',
                'insert_after_all',
                'clientless_vpn_encode',
                'clientless_vpn_encode_all',
                'clientless_vpn_decode',
                'clientless_vpn_decode_all',
                'insert_sip_header',
                'delete_sip_header',
                'corrupt_sip_header',
                'replace_sip_res',
                'replace_diameter_header_field',
                'replace_dns_header_field',
                'replace_dns_answer_section'
            ]
        ),
        target=dict(type='str'),
        stringbuilderexpr=dict(type='str'),
        pattern=dict(type='str'),
        search=dict(type='str'),
        bypasssafetycheck=dict(type='str'),
        refinesearch=dict(type='str'),
        comment=dict(type='str'),
        newname=dict(type='str'),
        hits=dict(type='float'),
        undefhits=dict(type='float'),
        referencecount=dict(type='float'),
        description=dict(type='str'),
        isdefault=dict(type='bool'),
        builtin=dict(type='list'),
    )

    hand_inserted_arguments = dict(
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not PYTHON_SDK_IMPORTED:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)

    try:
        client.login()
    except nitro_exception as e:
        msg = "nitro exception during login. errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg)
    except Exception as e:
        if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
            module.fail_json(msg='Connection error %s' % str(e))
        elif str(type(e)) == "<class 'requests.exceptions.SSLError'>":
            module.fail_json(msg='SSL Error %s' % str(e))
        else:
            module.fail_json(msg='Unexpected error during login %s' % str(e))

    readwrite_attrs = [
        'name',
        'type',
        'target',
        'stringbuilderexpr',
        'pattern',
        'search',
        'bypasssafetycheck',
        'refinesearch',
        'comment',
        'newname'
    ]

    readonly_attrs = [
        'hits',
        'undefhits',
        'referencecount',
        'description',
        'isdefault',
        'builtin',
        '__count'
    ]

    immutable_attrs = [
        'name',
        'type'
    ]

    transforms = {
    }

    # Instantiate config proxy
    rewriteaction_proxy = ConfigProxy(
        actual=rewriteaction(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
        transforms=transforms,
    )

    try:
        ensure_feature_is_enabled(client, 'rewrite')
        # Apply appropriate state
        if module.params['state'] == 'present':
            if not rewriteaction_exists(client, module):
                if not module.check_mode:
                    rewriteaction_proxy.add()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            elif not rewriteaction_identical(client, module, rewriteaction_proxy):

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(rewriteaction_proxy, diff_list(client, module, rewriteaction_proxy).keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff_list(client, module, rewriteaction_proxy), **module_result)

                if not module.check_mode:
                    rewriteaction_proxy.update()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if not rewriteaction_exists(client, module):
                    module.fail_json(msg='Rewrite action does not exist', **module_result)
                if not rewriteaction_identical(client, module, rewriteaction_proxy):
                    module.fail_json(msg='Rewrite action differs from configured', diff=diff_list(client, module, rewriteaction_proxy), **module_result)

        elif module.params['state'] == 'absent':
            if rewriteaction_exists(client, module):
                if not module.check_mode:
                    rewriteaction_proxy.delete()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if rewriteaction_exists(client, module):
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
