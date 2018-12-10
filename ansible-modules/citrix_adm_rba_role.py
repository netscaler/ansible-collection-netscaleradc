#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2018 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



DOCUMENTATION = '''
---
module: citrix_adm_rba_role
short_description: Manage Citrix ADM rba roles.
description: Manage Citrix ADM rba roles.

version_added: "2.8.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    tenant_id:
        description:
            - "Tenant Id of the RBA roles."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    name:
        description:
            - "Role Name."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    id:
        description:
            - "Id is system generated key for all the RBA roles."
        type: str

    description:
        description:
            - "Description of Role."
            - "Minimum length = 1"
            - "Maximum length = 1024"
        type: str

    resourcegroups:
        description:
            - "Resourcegroups attached to this role.."
        type: list

    groups:
        description:
            - "Groups to which this role is assigned."
        type: list

    policies:
        description:
            - "Policies attached to this role.."
        type: list


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- name: Setup rba role
  delegate_to: localhost
  citrix_adm_rba_role:
    mas_ip: 192.168.1.1
    mas_user: nsroot
    mas_pass: nsroot

    state: present

    name: test_role
    description: some description
    tenant_id: 0ea1d85a-06b8-4225-9fc8-5a7065fdd590
    policies: 
      - test_policy
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

rba_role:
    description: Dictionary contatining the attributes of the created rba_role.
    returned: success
    type: dict
'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import MASResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):
    
    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'rba_role'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            
            'rba_role': {
                'attributes_list': [
                    
                    'tenant_id',
                    'name',
                    'id',
                    'description',
                    'resourcegroups',
                    'groups',
                    'policies',
                ],
                'transforms': {
                    
                },
                'get_id_attributes': [
                    
                    'name',
                    'id',
                ],
                'delete_id_attributes': [
                    
                    'name',
                    'id',
                ],
            },
            

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def main_object_exists(self, config):
        try:
            main_object_exists = config.exists(
                get_id_attributes=self.attribute_config[self.main_nitro_class]['get_id_attributes'],
                use_filter=True,
            )
        except NitroException as e:
                raise

        return main_object_exists

    def get_main_config(self):
        config = MASResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attribute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attribute_config[self.main_nitro_class]['transforms'],
            api_path='nitro/v2/config',
        )

        return config


    def update_or_create(self):
        # Check if main object exists
        config = self.get_main_config()

        if not self.main_object_exists(config):
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.create()
        else:
            if not config.values_subset_of_actual():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    config.update(id_attribute='id')

        # Return the actual object
        config.get_actual_instance(
            get_id_attributes=self.attribute_config[self.main_nitro_class]['get_id_attributes'],
            success_codes=[None, 0],
            use_filter=True
        )
        self.module_result.update(dict(rba_role=config.actual_dict))


    def delete(self):
        # Check if main object exists
        config = self.get_main_config()

        if self.main_object_exists(config):
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.delete(delete_id_attributes=self.attribute_config[self.main_nitro_class]['delete_id_attributes'])

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
            elif self.module.params['state'] == 'absent':
                self.delete()

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)



def main():


    argument_spec = dict()

    module_specific_arguments = dict(
        
        tenant_id=dict(type='str',),

        
        name=dict(type='str',),

        
        id=dict(type='str',),

        
        description=dict(type='str',),

        
        resourcegroups=dict(type='list',),

        
        groups=dict(type='list',),

        
        policies=dict(type='list',),

        
    )


    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)


    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
