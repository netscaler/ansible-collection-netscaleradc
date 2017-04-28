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

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'commiter',
}


DOCUMENTATION = '''
---
module: netscaler_cs_action
short_description: Manage content switching actions
description:
    - Manage content switching actions
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance

version_added: 2.2.3

options:

    name:
        description:
            - "Name for the content switching action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the content switching action is created."

    targetlbvserver:
        description:
            - Name of the load balancing virtual server to which the content is switched.
            - Create the load balancing vserver with netscaler_lb_vserver if it does not exist
            
    targetvserverexpr:
        description:
            - Information about this content switching action.

    comment:
        description:
            - Comments associated with this cs action.

extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
# lb_vserver_1 must have been already created with the netscaler_lb_vserver module

- name: Configure netscaler content switching action
    local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        ssl_cert_validation: no

        module: netscaler_cs_action
        operation: present

        name: action-1
        targetlbvserver: lb_vserver_1
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
    type: string
    sample: "Action does not exist"

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dictionary
    sample: { 'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2' }
'''

from ansible.module_utils.basic import AnsibleModule
import StringIO
import json


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled

    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csaction import csaction
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
        name=dict(type='str'),
        targetlbvserver=dict(type='str'),
        targetvserverexpr=dict(type='str'),
        comment=dict(type='str'),
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode = True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()



    # Instantiate Service Config object
    readwrite_attrs = [
        'name',
        'targetlbvserver',
        'targetvserverexpr',
        'comment',
    ]
    readonly_attrs = [
        'hits',
        'referencecount',
        'undefhits',
        'builtin',
    ]

    '''
    if 'targetvserverexpr' in module.params and module.params['targetvserverexpr'] is not None:
        module.params['targetvserverexpr'] = json.dumps(module.params['targetvserverexpr'])
    '''

    csaction_proxy = ConfigProxy(
        actual=csaction(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        json_encodes=['targetvserverexpr']
    )

    def action_exists():
        if csaction.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def action_identical():
        if len(diff_list()) == 0:
            return True
        else:
            return False

    def diff_list():
        action_list = csaction.get_filtered(client, 'name:%s' % module.params['name'])
        diff_list = csaction_proxy.diff_object(action_list[0])
        if False and 'targetvserverexpr' in diff_list:
            json_value = json.loads(action_list[0].targetvserverexpr)
            if json_value == module.params['targetvserverexpr']:
                del diff_list['targetvserverexpr']
        return diff_list


    try:

        ensure_feature_is_enabled(client, 'CS')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not action_exists():
                if not module.check_mode:
                    csaction_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not action_identical():
                if not module.check_mode:
                    csaction_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not action_exists():
                module.fail_json(msg='Content switching action does not exist', **module_result)
            if not action_identical():
                module.fail_json(msg='Content switching action differs from configured', diff=diff_list(), **module_result)

        elif module.params['operation'] == 'absent':
            if action_exists():
                if not module.check_mode:
                    csaction_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if action_exists():
                module.fail_json(msg='Service still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()
