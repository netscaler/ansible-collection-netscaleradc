#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_cs_vserver
short_description: Manage cs vserver
description:
    - Manage service group configuration in Netscaler

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True

    name:
        
        description:
            
            - Name for the content switching action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the content switching action is created.
            
            - The following requirement applies only to the NetScaler CLI:
            
            - If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, ?my action? or ?my action?).
            

    targetlbvserver:
        
        description:
            
            - Name of the load balancing virtual server to which the content is switched.
            

    targetvserver:
        
        description:
            
            - Name of the VPN virtual server to which the content is switched.
            

    targetvserverexpr:
        
        description:
            
            - Information about this content switching action.
            

    comment:
        
        description:
            
            - Comments associated with this cs action.
            

    newname:
        
        description:
            
            - New name for the content switching action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters.
            
            - The following requirement applies only to the NetScaler CLI:
            
            - If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my name or my name).
            
            - Minimum length = 1
            

    hits:
        
        description:
            
            - The number of times the action has been taken.
            

    referencecount:
        
        description:
            
            - The number of references to the action.
            

    undefhits:
        
        description:
            
            - The number of times the action resulted in UNDEF.
            

    builtin:
        choices: ['MODIFIABLE', 'DELETABLE', 'IMMUTABLE', 'PARTITION_ALL']
        description:
            
            - .
            
            - Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL
            

'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Connect to netscaler appliance
    netscaler_service_group:
        nsip: "172.17.0.2"
'''

# TODO: Update as module progresses
RETURN = '''
config_updated:
    description: determine if a change in the netscaler configuration happened
    returned: always
    type: boolean
    sample: False
'''

from ansible.module_utils.basic import AnsibleModule
import StringIO
import json


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csaction import csaction
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
        name=dict(type='str'),
        targetlbvserver=dict(type='str'),
        targetvserver=dict(type='str'),
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
        'targetvserver',
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
                module.fail_json(msg='Service does not exist')
            if not action_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())

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
                module.fail_json(msg='Service still exists')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()
