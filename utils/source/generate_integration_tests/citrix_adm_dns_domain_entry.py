from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_dns_domain_entry'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
            ('name', 'integration.test.com'),
            ('description', 'some description'),

    
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    attributes['description'] = 'other description'
    submodObj.add_operation('update_description', copy.deepcopy(attributes))
    
    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
