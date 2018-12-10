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
module: citrix_adc_appfw_global_bindings
short_description: Define global bindings for AppFW
description: 
    - Define global bindings for AppFW
    - Note that due to limitations in the NITRO API this module will always report a changed status.

version_added: "2.8.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)
    - Sumanth Lingappa (@sumanth-lingappa)

options:



    appfwpolicy_bindings:
        description: appfwpolicy bindings
        suboptions:
            mode:
                description:
                    - If mode is C(bind):
                    - Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - If mode is C(unbind):
                    - Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.
                    - Existing bindings that are not on the attributes list remain unaffected.
                choices:
                    - bind
                    - unbind
            attributes:
                description: 
                    - List of the attributes dictionaries for the bindings.
                    - Valid attribute keys:
                    - policyname
                    - priority
                    - gotopriorityexpression
                    - invoke
                    - state
                    - labeltype
                    - labelname
                    - type
                    - globalbindtype
                    

    auditnslogpolicy_bindings:
        description: auditnslogpolicy bindings
        suboptions:
            mode:
                description:
                    - If mode is C(bind):
                    - Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - If mode is C(unbind):
                    - Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.
                    - Existing bindings that are not on the attributes list remain unaffected.
                choices:
                    - bind
                    - unbind
            attributes:
                description: 
                    - List of the attributes dictionaries for the bindings.
                    - Valid attribute keys:
                    - policyname
                    - priority
                    - state
                    - type
                    - gotopriorityexpression
                    - invoke
                    - labeltype
                    - labelname
                    

    auditsyslogpolicy_bindings:
        description: auditsyslogpolicy bindings
        suboptions:
            mode:
                description:
                    - If mode is C(bind):
                    - Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - If mode is C(unbind):
                    - Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.
                    - Existing bindings that are not on the attributes list remain unaffected.
                choices:
                    - bind
                    - unbind
            attributes:
                description: 
                    - List of the attributes dictionaries for the bindings.
                    - Valid attribute keys:
                    - policyname
                    - priority
                    - state
                    - type
                    - gotopriorityexpression
                    - invoke
                    - labeltype
                    - labelname
                    


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
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
'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import NitroResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):
    
    def __init__(self, module):
        self.module = module
        self.main_nitro_class = ''

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            
            'appfwpolicy_bindings': {
                'attributes_list': [
                    
                    'policyname',
                    'priority',
                    'gotopriorityexpression',
                    'invoke',
                    'state',
                    'labeltype',
                    'labelname',
                    'type',
                    'globalbindtype',
                ],
                'transforms': {
                    
                    'state': lambda v: v.upper(),
                },
                'get_id_attributes': [
                    
                    'type',
                ],
                'delete_id_attributes': [
                    
                    'policyname',
                    'priority',
                    'type',
                ],
            },
            
            'auditnslogpolicy_bindings': {
                'attributes_list': [
                    
                    'policyname',
                    'priority',
                    'state',
                    'type',
                    'gotopriorityexpression',
                    'invoke',
                    'labeltype',
                    'labelname',
                ],
                'transforms': {
                    
                    'state': lambda v: v.upper(),
                },
                'get_id_attributes': [
                    
                    'type',
                ],
                'delete_id_attributes': [
                    
                    'policyname',
                    'priority',
                    'type',
                ],
            },
            
            'auditsyslogpolicy_bindings': {
                'attributes_list': [
                    
                    'policyname',
                    'priority',
                    'state',
                    'type',
                    'gotopriorityexpression',
                    'invoke',
                    'labeltype',
                    'labelname',
                ],
                'transforms': {
                    
                    'state': lambda v: v.upper(),
                },
                'get_id_attributes': [
                    
                    'type',
                ],
                'delete_id_attributes': [
                    
                    'policyname',
                    'priority',
                    'type',
                ],
            },
            

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )


    def sync_binding_with_data(self, data):

        binding_key = data['binding_key']
        binding_object = data['binding_object']

        if self.module.params.get(binding_key) is None:
            return

        log('ModuleExecutor syncing binding %s' % binding_key)

        mode = self.module.params[binding_key]['mode']

        # Make a list of config objects for configured bindings
        configured_bindings = []
        for bind_values in self.module.params[binding_key]['attributes']:
            all_bind_values = copy.deepcopy(bind_values)
            configured_binding = NitroResourceConfig(
                module=self.module,
                resource=binding_object,
                attribute_values_dict=all_bind_values,
                attributes_list=self.attribute_config[binding_key]['attributes_list'],
                transforms=self.attribute_config[binding_key]['transforms'],
            )

            configured_bindings.append(configured_binding)


        if mode == 'bind':
            for configured_binding in configured_bindings:
                self.module_result['changed'] = True
                try:
                    configured_binding.create()
                except NitroException as e:
                    if e.errorcode != 273:
                        raise

        elif mode == 'unbind':
            for configured_binding in configured_bindings:
                self.module_result['changed'] = True
                try:
                    configured_binding.delete(delete_id_attributes=self.attribute_config[binding_key]['delete_id_attributes'])
                except NitroException as e:
                    # Handle exceptions when trying to unbind objects that are not bound
                    # Every binding has its own errorcode
                    if binding_object == 'appfwglobal_appfwpolicy_binding':
                        if e.errorcode == 3093:
                            log('Ignoring nitro_errocode 3093 for appfwglobal_appfwpolicy_binding')
                        else:
                            raise

    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        
        self.sync_appfwpolicy_bindings()
        
        self.sync_auditnslogpolicy_bindings()
        
        self.sync_auditsyslogpolicy_bindings()
        


        
        
    def sync_appfwpolicy_bindings(self):
        self.sync_binding_with_data({'binding_key': 'appfwpolicy_bindings', 'attributes_config_list': {'get_id_attributes': ['type'], 'delete_id_attributes': ['policyname', 'priority', 'type'], 'transforms': {'state': 'lambda v: v.upper()'}, 'resource_name': 'appfwpolicy_bindings', 'attributes': ['policyname', 'priority', 'gotopriorityexpression', 'invoke', 'state', 'labeltype', 'labelname', 'type', 'globalbindtype']}, 'doc_list': ['policyname', 'priority', 'gotopriorityexpression', 'invoke', 'state', 'labeltype', 'labelname', 'type', 'globalbindtype'], 'description': 'appfwpolicy bindings', 'binding_object': 'appfwglobal_appfwpolicy_binding'})
        
        
    def sync_auditnslogpolicy_bindings(self):
        self.sync_binding_with_data({'binding_key': 'auditnslogpolicy_bindings', 'attributes_config_list': {'get_id_attributes': ['type'], 'delete_id_attributes': ['policyname', 'priority', 'type'], 'transforms': {'state': 'lambda v: v.upper()'}, 'resource_name': 'auditnslogpolicy_bindings', 'attributes': ['policyname', 'priority', 'state', 'type', 'gotopriorityexpression', 'invoke', 'labeltype', 'labelname']}, 'doc_list': ['policyname', 'priority', 'state', 'type', 'gotopriorityexpression', 'invoke', 'labeltype', 'labelname'], 'description': 'auditnslogpolicy bindings', 'binding_object': 'appfwglobal_auditnslogpolicy_binding'})
        
        
    def sync_auditsyslogpolicy_bindings(self):
        self.sync_binding_with_data({'binding_key': 'auditsyslogpolicy_bindings', 'attributes_config_list': {'get_id_attributes': ['type'], 'delete_id_attributes': ['policyname', 'priority', 'type'], 'transforms': {'state': 'lambda v: v.upper()'}, 'resource_name': 'auditsyslogpolicy_bindings', 'attributes': ['policyname', 'priority', 'state', 'type', 'gotopriorityexpression', 'invoke', 'labeltype', 'labelname']}, 'doc_list': ['policyname', 'priority', 'state', 'type', 'gotopriorityexpression', 'invoke', 'labeltype', 'labelname'], 'description': 'auditsyslogpolicy bindings', 'binding_object': 'appfwglobal_auditsyslogpolicy_binding'})
        

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.sync_bindings()
            elif self.module.params['state'] == 'absent':
                log('state "absent" is a noop for this module')

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
        
        
        appfwpolicy_bindings=dict(type='dict'),
        auditnslogpolicy_bindings=dict(type='dict'),
        auditsyslogpolicy_bindings=dict(type='dict'),

    )


    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)


    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
