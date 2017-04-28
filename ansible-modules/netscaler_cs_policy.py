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
                    'supported_by': 'commiter',
                    'version': '1.0'}


DOCUMENTATION = '''
---
module: netscaler_cs_policy
short_description: Manage content switching policy
description:
    - Manage content switching policy.
    - "This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance."

version_added: 2.2.3

options:

    policyname:
        description:
            - >-
                Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore (_) character,
                and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:),
                at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after a policy is created.

            - Minimum length = 1

    url:
        description:
            - >-
                URL string that is matched with the URL of a request.
                Can contain a wildcard character.
                Specify the string value in the following format: [[prefix] [*]] [.suffix].
            - Minimum length = 1
            - Maximum length = 208

    rule:
        description:
            - Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.
            - Note
            - >-
                Maximum length of a string literal in the expression is 255 characters.
                A longer string can be split into smaller strings of up to 255 characters each,
                and the smaller strings concatenated with the + operator.
                For example, you can create a 500-character string as follows '"<string of 255 characters>" + "<string of 245 characters>"'
            - The following requirements apply only to the NetScaler CLI
            - If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
            - If the expression itself includes double quotation marks, escape the quotations by using the character.
            - lternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.

    domain:
        description:
            - The domain name. The string value can range to 63 characters.
            - Minimum length = 1

    action:
        description:
            - Content switching action that names the target load balancing virtual server to which the traffic is switched.

extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Create url cs policy
    local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        ssl_cert_validation: no

        module: netscaler_cs_policy
        operation: present

        policyname: policy_1
        url: /example/
'''

# TODO: Update as module progresses
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
    sample: "Could not load nitro python sdk"

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'url': 'difference. ours: (str) example1 other: (str) /example1' }
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
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
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

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

    # Instantiate Service Config object
    readwrite_attrs = [
        'policyname',
        'url',
        'rule',
        'domain',
        'action',
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
    ]

    cspolicy_proxy = ConfigProxy(
        actual=cspolicy(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def policy_exists():
        if cspolicy.count_filtered(client, 'policyname:%s' % module.params['policyname']) > 0:
            return True
        else:
            return False

    def policy_identical():
        if cspolicy.count_filtered(client, 'policyname:%s' % module.params['policyname']) == 0:
            return False
        policy_list = cspolicy.get_filtered(client, 'policyname:%s' % module.params['policyname'])
        diff_dict = cspolicy_proxy.diff_object(policy_list[0])
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff_list():
        policy_list = cspolicy.get_filtered(client, 'policyname:%s' % module.params['policyname'])
        return cspolicy_proxy.diff_object(policy_list[0])

    try:
        ensure_feature_is_enabled(client, 'CS')

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not policy_exists():
                if not module.check_mode:
                    cspolicy_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not policy_identical():
                if not module.check_mode:
                    cspolicy_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not policy_exists():
                module.fail_json(msg='Service does not exist', **module_result)
            if not policy_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list(), **module_result)

        elif module.params['operation'] == 'absent':
            if policy_exists():
                if not module.check_mode:
                    cspolicy_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if policy_exists():
                module.fail_json(msg='Service still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
