from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_policy'
input_data = OrderedDict()
testbed_data = []

'''
# PREREQUISITES
testbedObj = BaseIntegrationModule('netscaler_lb_vserver')
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

def sanitize_values(values_dict, skip_keys=[]):
    ret_val = copy.deepcopy(values_dict)
    del ret_val['state']
    for key in ret_val:
        if key in skip_keys:
            continue
        ret_val[key] = '"%s"' % ret_val[key]

    return ret_val


submodObj = BaseIntegrationModule(ENTITY_NAME, 'basic')

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

# Verify previous step
verification_dict = sanitize_values(attributes, skip_keys=['rule'])
verification_dict['rule'] = r'"HTTP.REQ.HOSTNAME.DOMAIN.EQ(\"blog.example.com\")"'

data = helpers.get_verification_playbook_dict(
    nitro_resource='appfwpolicy',
    nitro_resource_name=attributes['name'],
    verification_dict=verification_dict,
)
submodObj.add_raw_operation('setup_verify', data, run_once=True)



attributes['comment'] = 'Some other policy comment'

submodObj.add_operation('update', copy.deepcopy(attributes))

# Verify previous step
verification_dict = sanitize_values(attributes, skip_keys=['rule'])
verification_dict['rule'] = r'"HTTP.REQ.HOSTNAME.DOMAIN.EQ(\"blog.example.com\")"'

data = helpers.get_verification_playbook_dict(
    nitro_resource='appfwpolicy',
    nitro_resource_name=attributes['name'],
    verification_dict=verification_dict,
)
submodObj.add_raw_operation('update_verify', data, run_once=True)


attributes['state'] = 'absent'

submodObj.add_operation('remove', copy.deepcopy(attributes))


input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
