from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adc_cs_action'


# PREREQUISITES
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_lb_vserver')
    lb_vserver_data = OrderedDict(
        [
            ('name', 'lb-vserver-1'),
            ('ipv46', '10.79.1.4'),
            ('port', 80),
            ('servicetype','ANY'),
        ]
    )
    
    testbed_data.append(testbedObj.add_testbed('setup', lb_vserver_data))
    return testbed_data

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'target_lb_vserver'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'target_lb_vserver')
    setup_data = OrderedDict(
        [
            ('name', 'action-1'),
            ('targetlbvserver', 'lb-vserver-1'),
            ('comment', 'some comment'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('name', 'action-1'),
            ('targetlbvserver', 'lb-vserver-1'),
            ('comment', 'some other comment'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'action-1'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'target_expression'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'target_expression')
    setup_data = OrderedDict(
        [
            ('name', 'action-2'),
            ('targetvserverexpr', '"mylb_" + HTTP.REQ.URL.SUFFIX'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'action-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
