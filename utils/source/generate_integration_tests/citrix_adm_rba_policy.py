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
            ('name', 'integration_test_policy'),
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

    attributes['description'] = 'Other description'
    submodObj.add_operation('change_description', copy.deepcopy(attributes), run_once=True)

    attributes['statement'].append({
                    "access_type": True,
                    "parent_name": "rba_policy",
                    "operation_name": "add",
                    "resource_type": "DeviceAPIProxy"
                })
    submodObj.add_operation('add_statement_item', copy.deepcopy(attributes), run_once=True)

    attributes['statement'].pop()
    submodObj.add_operation('remove_statement_item', copy.deepcopy(attributes), run_once=True)

    attributes['ui'].append({
                    "name": "ApplicationsDashboard",
                    "access_type": True,
                    "parent_name": "rba_policy",
                    "display_name": ""
                })
    submodObj.add_operation('add_ui_item', copy.deepcopy(attributes), run_once=True)


    attributes['ui'].pop()
    submodObj.add_operation('remove_ui_item', copy.deepcopy(attributes), run_once=True)
    
    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
