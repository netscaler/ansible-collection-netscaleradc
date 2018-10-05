from collections import OrderedDict
import copy
import pprint
import json

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'netscaler_cs_vserver'
input_data = OrderedDict()
testbed_data = []

# PREREQUISITES/Testbed
testbedObj = BaseIntegrationModule('netscaler_lb_vserver')
testbed_1 = OrderedDict(
    [
        ('name', 'push_lb_vserver'),
        ('servicetype', 'PUSH'),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed_1))

testbedObj = BaseIntegrationModule('netscaler_lb_vserver')
testbed_1 = OrderedDict(
    [
        ('name', 'lb-vserver-1'),
        ('servicetype', 'HTTP'),
        ('ipv46', '10.60.60.60'),
        ('port', 80),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed_1))

testbedObj = BaseIntegrationModule('netscaler_lb_vserver')
testbed_1 = OrderedDict(
    [
        ('name', 'lb-vserver-2'),
        ('servicetype', 'HTTP'),
        ('ipv46', '10.60.60.62'),
        ('port', 80),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed_1))

testbedObj = BaseIntegrationModule('netscaler_cs_policy')
testbed_1 = OrderedDict(
    [
        ('policyname', 'policy-1'),
        ('url', '/example.com/basket'),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed_1))

testbedObj = BaseIntegrationModule('netscaler_cs_policy')
testbed_1 = OrderedDict(
    [
        ('policyname', 'policy-2'),
        ('url', '/example.com/basket2'),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed_1))


# For Submodule 'cs_vserver_default_lb'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'cs_vserver_default_lb')
default_1 = OrderedDict(
    [
        ('name', 'cs-vserver-3'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.3'),
        ('port', 80),
        ('lbvserver', 'lb-vserver-1'),
    ]
)

default_2 = OrderedDict(
    [
        ('name', 'cs-vserver-3'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.3'),
        ('port', 80),
        ('lbvserver', 'lb-vserver-2'),
    ]
)

default_none = OrderedDict(
    [
        ('name', 'cs-vserver-3'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.3'),
        ('port', 80),
    ]
)

nodefault = OrderedDict(
    [
        ('name', 'cs-vserver-3'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.3'),
        ('port', 80),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('servicetype',  'HTTP'),
        ('ipv46',  '192.168.1.3'),
        ('port',  80),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('nodefault',  nodefault)
submodObj.add_operation('default_1',  default_1)
submodObj.add_operation('default_2',  default_2)
submodObj.add_operation('nodefault',  nodefault)
# submodObj.add_operation('default_none',  default_none)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})


# For Submodule 'cs_vserver_dns'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_dns')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-6'),
        ('servicetype',  'DNS'),
        ('ipv46',  '192.168.1.6'),
        ('port',  80),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-6'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})



# For Submodule 'cs_vserver_flap_disabled'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_flap_disabled')
setup_data1 = OrderedDict(
    [
        ('name',  'cs-vserver-flap'),
        ('servicetype',  'HTTP'),
        ('ipv46',  '192.168.1.1'),
        ('port',  80),
        ('td',  0),
        ('disabled',  "{{ item|int % 2 }}"),
    ]
)
setup_data1_extra_vars = OrderedDict(
    [
        ('with_sequence', 'count=20'),
        ('delay', 1),
    ]
)

setup_data2 = OrderedDict(
    [
        ('name',  'cs-vserver-flap'),
        ('servicetype',  'HTTP'),
        ('ipv46',  '192.168.1.1'),
        ('port',  80),
        ('td',  0),
        ('disabled',  "{{ item|int % 2 }}"),
    ]
)
setup_data2_extra_vars = OrderedDict(
    [
        ('with_sequence', 'count=20'),
        ('delay', 5),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-flap'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  [[setup_data1, setup_data1_extra_vars], [setup_data2, setup_data2_extra_vars]])
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})


# For Submodule 'cs_vserver_http'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_http') 
setup_data = OrderedDict(
    [
        ('name', 'cs-vserver-1'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.1'),
        ('td', 0),
        ('port', 80),
        ('dnsrecordtype', 'A'),
        ('range', 2),
        ('stateupdate', 'disabled'),
        ('cacheable', 'no'),
        ('redirecturl', 'http://newurl.com'),
        ('clttimeout', 200),
        ('precedence', 'RULE'),
        ('casesensitive', 'on'),
        ('somethod', 'CONNECTION'),
        ('sopersistence', 'enabled'),
        ('sopersistencetimeout', 50),
        ('sothreshold', 200),
        ('sobackupaction', 'DROP'),
        ('redirectportrewrite', 'disabled'),
        ('downstateflush', 'disabled'),
        ('disableprimaryondown', 'disabled'),
        ('insertvserveripport', 'VIPADDR'),
        ('vipheader', 'someheader'),
        ('rtspnat', 'off'),
        ('authenticationhost', 'newauth.com'),
        ('authentication', 'on'),
        ('listenpolicy', '"NONE"'),
        ('authn401', 'off'),
        ('authnvsname', 'someserver'),
        ('push', 'disabled'),
        ('pushvserver', 'push_lb_vserver'),
        ('pushlabel', 'none'),
        ('pushmulticlients', 'no'),
        ('comment', 'some comment'),
        ('l2conn', 'off'),
        ('appflowlog', 'enabled'),
        ('icmpvsrresponse', 'PASSIVE'),
        ('rhistate', 'PASSIVE'),
    ]
)

update_data = OrderedDict(
    [
        ('name', 'cs-vserver-1'),
        ('servicetype', 'HTTP'),
        ('ipv46', '192.168.1.1'),
        ('td', 0),
        ('port', 80),
        ('dnsrecordtype', 'A'),
        ('range', 2),
        ('stateupdate', 'disabled'),
        ('cacheable', 'no'),
        ('redirecturl', 'http://url.com'),
        ('clttimeout', 200),
        ('precedence', 'RULE'),
        ('casesensitive', 'on'),
        ('somethod', 'CONNECTION'),
        ('sopersistence', 'enabled'),
        ('sopersistencetimeout', 50),
        ('sothreshold', 200),
        ('sobackupaction', 'DROP'),
        ('redirectportrewrite', 'disabled'),
        ('downstateflush', 'disabled'),
        ('disableprimaryondown', 'disabled'),
        ('insertvserveripport', 'VIPADDR'),
        ('vipheader', 'someheader'),
        ('rtspnat', 'off'),
        ('authenticationhost', 'auth.com'),
        ('authentication', 'on'),
        ('listenpolicy', '"NONE"'),
        ('authn401', 'off'),
        ('authnvsname', 'someserver'),
        ('push', 'disabled'),
        ('pushvserver', 'push_lb_vserver'),
        ('pushlabel', 'none'),
        ('pushmulticlients', 'no'),
        ('comment', 'some comment'),
        ('l2conn', 'off'),
        ('appflowlog', 'enabled'),
        ('icmpvsrresponse', 'PASSIVE'),
        ('rhistate', 'PASSIVE'),
    ]
)

remove_data = OrderedDict(
    [
        ('name', 'cs-vserver-1'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('update', update_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})


# For Submodule 'cs_vserver_ippattern'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_ippattern')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-2'),
        ('servicetype',  'HTTP'),
        ('port',  80),
        ('ippattern',  '10.78.10.0'),
        ('ipmask',  '255.255.255.0'),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-2'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})


# For Submodule 'cs_vserver_mssql'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_mssql')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-4'),
        ('servicetype',  'MSSQL'),
        ('port',  80),
        ('ipv46',  '192.168.1.4'),
        ('mssqlserverversion',  2000),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-4'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'cs_vserver_mysql'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_mysql')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-5'),
        ('servicetype',  'MYSQL'),
        ('port',  80),
        ('ipv46',  '192.168.1.5'),
        ('mysqlprotocolversion',  10),
        ('mysqlserverversion',  'Version 1'),
        ('mysqlcharacterset',  8),
        ('mysqlservercapabilities', 41613),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-5'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'cs_vserver_oracle'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_oracle')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('servicetype',  'ORACLE'),
        ('port',  80),
        ('ipv46',  '192.168.1.3'),
        ('td',  0),
        ('oracleserverversion',  '10G'),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('state',  'absent'),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove',  remove_data)

input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'cs_vserver_policies'
submodObj = BaseIntegrationModule(ENTITY_NAME,  'cs_vserver_policies')
setup_data = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('servicetype',  'HTTP'),
        ('port',  80),
        ('ipv46',  '192.168.1.3'),
        ('policybindings', [
                                OrderedDict(
                                    [
                                        ('policyname','policy-1'), 
                                        ('targetlbvserver','lb-vserver-1'),
                                    ]
                                ),
                                OrderedDict(
                                    [
                                        ('policyname','policy-2'), 
                                        ('targetlbvserver','lb-vserver-2'),
                                    ]
                                ),
                            ]
        ),
    ]
)

remove_data = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('state',  'absent'),
    ]
)

add_one_policy = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('servicetype',  'HTTP'),
        ('port',  80),
        ('ipv46',  '192.168.1.3'),
        ('policybindings', [
                                OrderedDict(
                                    [
                                        ('policyname','policy-1'), 
                                        ('targetlbvserver','lb-vserver-1'),
                                    ]
                                ),
                                OrderedDict(
                                    [
                                        ('policyname','policy-2'), 
                                        ('targetlbvserver','lb-vserver-2'),
                                    ]
                                ),
                            ]
        ),
    ]
)

remove_one_policy = OrderedDict(
    [
        ('name',  'cs-vserver-3'),
        ('servicetype',  'HTTP'),
        ('port',  80),
        ('ipv46',  '192.168.1.3'),
        ('policybindings', [
                                OrderedDict(
                                    [
                                        ('policyname','policy-1'), 
                                        ('targetlbvserver','lb-vserver-1'),
                                    ]
                                ),
                            ]
        ),
    ]
)

submodObj.add_operation('setup',  setup_data)
submodObj.add_operation('remove_one_policy',  remove_one_policy)
submodObj.add_operation('add_one_policy',  add_one_policy)
submodObj.add_operation('remove',  remove_data)


input_data.update({submodObj.get_sub_mod_name():  copy.deepcopy(submodObj.get_mod_attrib())})

# Appfw policy prerequisite
testbedObj = BaseIntegrationModule('netscaler_appfw_policy')

testbed = OrderedDict([
        ('name',  'policy_cs_vserver_integration_helper'),
        ('rule', 'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")'),
        ('profilename', 'APPFW_BLOCK'),
])

testbed_data.append(testbedObj.add_testbed('setup_appfw_policy', [testbed, {}]))

# LB vserver

# Actual module
submodObj = BaseIntegrationModule(ENTITY_NAME, 'cs_vserver_appfwpolicy_binding')
attributes = OrderedDict(
    [
        ('state','present'),
        ('name', 'cs-vserver-appfw-policy'),
        ('port',80),
        ('ipv46','10.79.1.3'),
        ('servicetype','HTTP'),
        ('appfw_policybindings', [
            OrderedDict([
                ('priority', '100'),
                ('bindpoint', 'REQUEST'),
                ('policyname', 'policy_cs_vserver_integration_helper'),
                ('labelname', 'cs-vserver-appfw-policy'),

                # FIXME investigate what kind of lb vserver is valid for this option value
                #('targetlbvserver', 'lb-vserver-1'),

                ('gotopriorityexpression', '101'),
                ('invoke', True),
                ('labeltype', 'reqvserver'),
                # FIXME cannot set attribute with python sdk
                # file bug for python sdk
                #('sc', 'off')
            ])
        ])
    ]
)

submodObj.add_operation('setup', copy.deepcopy(attributes))

attributes['appfw_policybindings'][0]['gotopriorityexpression'] = '102'
submodObj.add_operation('update_binding', copy.deepcopy(attributes))

attributes['appfw_policybindings'] = []
submodObj.add_operation('remove_appfw_bindings', copy.deepcopy(attributes))

attributes['state'] = 'absent'
submodObj.add_operation('remove', copy.deepcopy(attributes))

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
