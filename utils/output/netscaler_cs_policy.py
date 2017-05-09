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


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


DOCUMENTATION = '''
---
module: _
short_description: _
description:
    - _

version_added: 2.3.1

options:

    policyname:
        description:
            - >-
                Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore (_)
                character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon
                (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after a policy is
                created.
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, my policy or my policy).
            - "Minimum length = 1"

    url:
        description:
            - >-
                URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the
                string value in the following format: [[prefix] [*]] [.suffix].
            - "Minimum length = 1"
            - "Maximum length = 208"

    rule:
        description:
            - >-
                Expression, or name of a named expression, against which traffic is evaluated. Written in the classic
                or default syntax.
            - "Note:"
            - >-
                Maximum length of a string literal in the expression is 255 characters. A longer string can be split
                into smaller strings of up to 255 characters each, and the smaller strings concatenated with the +
                operator. For example, you can create a 500-character string as follows: '"<string of 255
                characters>" + "<string of 245 characters>"'
            - "The following requirements apply only to the NetScaler CLI:"
            - >-
                * If the expression includes one or more spaces, enclose the entire expression in double quotation
                marks.
            - >-
                * If the expression itself includes double quotation marks, escape the quotations by using the
                character.
            - >-
                * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not
                have to escape the double quotation marks.

    domain:
        description:
            - "The domain name. The string value can range to 63 characters."
            - "Minimum length = 1"

    action:
        description:
            - >-
                Content switching action that names the target load balancing virtual server to which the traffic is
                switched.

    logaction:
        description:
            - "The log action associated with the content switching policy."

    newname:
        description:
            - "The new name of the content switching policy."
            - "Minimum length = 1"


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled
    try:
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        policyname=dict(type='str'),
        url=dict(type='str'),
        rule=dict(type='str'),
        domain=dict(type='str'),
        action=dict(type='str'),
        logaction=dict(type='str'),
        newname=dict(type='str'),
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
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    readwrite_attrs = [
        'policyname',
        'url',
        'rule',
        'domain',
        'action',
        'logaction',
        'newname',
    ]

    readonly_attrs = [
        'vstype',
        'hits',
        'bindhits',
        'labelname',
        'labeltype',
        'priority',
        'activepolicy',
        'cspolicytype',
        '__count',
    ]

    immutable_attrs = [
        'policyname',
        'newname',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
    )

    def _exists():
        if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def _identical():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = _proxy.diff_object(_list[0])
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        return _proxy.diff_object(_list[0])

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not _exists():
                if not module.check_mode:
                    _proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not _identical():

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(gslb_site_proxy, diff().keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='_ differs from configured', diff=diff(), **module_result)

        elif module.params['operation'] == 'absent':
            if _exists():
                if not module.check_mode:
                    _proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if _exists():
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
