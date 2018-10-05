from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_cs_policy'
input_data = OrderedDict()
testbed_data = []


# PREREQUISITES
testbedObj = BaseIntegrationModule('netscaler_cs_action')
lb_vserver_data = OrderedDict(
    [
        ('name', 'action-1'),
        ('targetvserverexpr','"mylb_" + HTTP.REQ.URL.SUFFIX'),
    ]
)

testbed_data.append(testbedObj.add_testbed('setup', lb_vserver_data))

# For Submodule 'policy_domain'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'policy_domain')
setup_data = OrderedDict(
    [
        ('policyname', 'somepolicy'),
        ('domain', 'example.com'),
    ]
)

update_data = OrderedDict(
    [
        ('policyname', 'somepolicy'),
        ('domain', 'example2.com'),
    ]
)

remove_data = OrderedDict(
    [
        ('policyname', 'somepolicy'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('update', update_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'policy_rule'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'policy_rule')
setup_data = OrderedDict(
    [
        ('policyname', 'somepolicy_rule'),
        ('rule', 'CLIENT.IP.SRC.SUBNET(24).EQ(10.217.84.0)'),
        ('action', 'action-1'),
    ]
)

remove_data = OrderedDict(
    [
        ('policyname', 'somepolicy_rule'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'policy_url'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'policy_url')
setup_data = OrderedDict(
    [
        ('policyname', 'somepolicy'),
        ('url', '/example.com/basket'),
    ]
)

remove_data = OrderedDict(
    [
        ('policyname', 'somepolicy'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
