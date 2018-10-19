from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_policy'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    '''
    # PREREQUISITES
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_lb_vserver')
    lb_vserver_data = OrderedDict(
        [
            ('name', 'lb-vserver-1'),
            ('ipv46', '10.79.1.4'),
            ('port', 80),
            ('servicetype','ANY'),
        ]
    )
    
    testbed_data.append(testbedObj.add_testbed('setup', lb_vserver_data))
    '''
    return testbed_data

def sanitize_values(values_dict, skip_keys=[]):
    ret_val = copy.deepcopy(values_dict)
    del ret_val['state']
    for key in ret_val:
        if key in skip_keys:
            continue
        ret_val[key] = '"%s"' % ret_val[key]

    return ret_val


def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
    
            ('name',  'policy_integration_test'),
            ('rule', '\'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")\''),
            ('profilename',  'APPFW_BLOCK'),
            ('comment',  'policy test comment'),
            #('logaction', 'NONE'),
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    attributes['comment'] = 'Some other policy comment'
    
    submodObj.add_operation('update', copy.deepcopy(attributes))
    
    attributes['state'] = 'absent'
    
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
