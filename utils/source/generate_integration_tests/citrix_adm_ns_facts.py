from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_ns_facts'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [

            ('name', 'integration_test_user'),
            ('ip_address', '192.168.1.1'),
            ('ipv4_address', '192.168.1.1'),
            ('ipv6_address', 'fe::23'),
            ('id', 'some_uuid')
        ]
    )
    
    submodObj.add_operation('get_all', copy.deepcopy(attributes), run_once=True)
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
