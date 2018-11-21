from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_rba_role'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
    
            ('name',  'integration_test_rba_policy'),
            ('description',  'some description'),
            ('resourcegroups', []),
            ('groups', []),
            ('policies', ['appReadOnlyPolicy']),
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    attributes['description'] = 'Some other description'
    
    submodObj.add_operation('update', copy.deepcopy(attributes))
    
    attributes['state'] = 'absent'
    
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
