from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_rba_policy'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
            ('name', 'playbook_test_policy'),
            ('description', 'some description'),
            ('statement', [{
                'access_type': True,
                'operation_name': 'add',
                'parent_name': 'rba_policy',
                'resource_type': 'ns_gslbservice',
                }]
            ),
            ('ui', [{
                'access_type': True,
                'display_name': "",
                'name': 'ContentSwitching',
                'parent_name': 'rba_policy',
                }]
            ),
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes), run_once=True)
    
    attributes['state'] = 'absent'
    
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
