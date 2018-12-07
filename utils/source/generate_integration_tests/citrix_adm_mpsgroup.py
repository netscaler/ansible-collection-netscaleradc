from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_mpsgroup'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
            ('name', 'integration_test_mpsgroup'),
            ('permission', 'read-only'),
            ('allow_application_only', True),
            ('session_timeout',  10),
            ('session_timeout_unit', 'Minutes'),
            ('description', 'some description'),
            ('assign_all_apps', True),
            ('enable_session_timeout', True),
            ('assign_all_devices', False),
            ('role', 'admin'),
            ('roles', ['admin']),
            ('application_names_without_regex', []),
            ('application_names', []),
            ('application_names_with_regex', []),
            ('standalone_instances_id', []),
        ]
    )

    if ns_version == '12.0':
        del attributes['application_names_with_regex']
        del attributes['application_names_without_regex']
        del attributes['description']
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    attributes['session_timeout'] = 20
    submodObj.add_operation('update_timeout', copy.deepcopy(attributes))
    
    attributes['assign_all_devices'] = True
    submodObj.add_operation('update_assign_all_devices', copy.deepcopy(attributes))

    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
