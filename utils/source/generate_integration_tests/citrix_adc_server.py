from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adc_server'

def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    #TODO:test bed data here
    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'citrix_adc_server'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_server')
    setup_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipaddress', '10.10.10.10'),
            ('comment', 'comment for server'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipaddress', '11.11.11.11'),
        ]
    )
    
    disable_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipaddress', '11.11.11.11'),
            ('disabled', 'yes'),
            ('graceful', 'yes'),
            ('delay', '20'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('ipaddress', '10.10.10.10'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('disable', disable_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    
    # For Submodule 'citrix_adc_server_domain'
    submodObj = None
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_server_domain')
    setup_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipv6address', 'no'),
            ('domain', 'example.com'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('domain', 'example.com'),
            ('translationip', '192.168.1.1'),
            ('translationmask', '255.255.255.0'),
            ('domainresolveretry', 10),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    
    
    # For Submodule 'citrix_adc_server_ipv6'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_server_ipv6')
    setup_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipaddress', 'ff::fa:0'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'present'),
            ('ipaddress', 'ff::fb:0'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'test-server-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
