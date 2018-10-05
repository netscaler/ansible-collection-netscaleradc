from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'netscaler_service'
input_data = OrderedDict()
testbed_data = []

# PREREQUISITES/Testbed
# testbedObj = BaseIntegrationModule('') #TODO: prerequisite module here
# testbed_data = OrderedDict(
    # [
        # ('', ''),
        # ('', ''),
    # ]
# )
# testbed_data.append(testbedObj.add_testbed('setup', testbed_data))

# For Submodule 'adns_service'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'adns_service')
setup_data = OrderedDict(
    [
        ('state', 'present'),
        ('name', 'service-adns'),
        ('ipaddress', '192.168.1.3'),
        ('port', 80),
        ('servicetype', 'ADNS'),
    ]
)

remove_data = OrderedDict(
    [
        ('name', 'service-adns'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'flap_disabled'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'flap_disabled')
setup_data1 = OrderedDict(
    [
        ('name', 'service-http'),
        ('ip', '192.168.1.1'),
        ('ipaddress', '192.168.1.1'),
        ('port', 80),
        ('servicetype', 'HTTP'),
        ('disabled', '{{ item|int % 2 }}'),
    ]
)
setup_data1_extra_vars = OrderedDict(
    [
        ('with_sequence','count=20'),
        ('delay', 1),
    ]
) 

setup_data2 = OrderedDict(
    [
        ('name', 'service-http'),
        ('ip', '192.168.1.1'),
        ('ipaddress', '192.168.1.1'),
        ('port', 80),
        ('servicetype', 'HTTP'),
        ('disabled', '{{ item|int % 2 }}'),
    ]
)
setup_data2_extra_vars = OrderedDict(
    [
        ('with_sequence','count=20'),
        ('delay', 5),
    ]
) 

remove_data = OrderedDict(
    [
        ('name', 'service-http'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', [[setup_data1, setup_data1_extra_vars],[setup_data2, setup_data2_extra_vars]])
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule 'http_service'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'http_service')
setup_data = OrderedDict(
    [
        ('state', 'present'),
        ('name', 'service-http'),
        ('ip', '192.168.1.1'),
        ('ipaddress', '192.168.1.1'),
        ('port', 80),
        ('servicetype', 'HTTP'),
        ('cachetype', 'TRANSPARENT'),
        ('maxclient', 100),
        ('healthmonitor', 'no'),
        ('maxreq', 200),
        ('cacheable', 'no'),
        ('cip', 'enabled'),
        ('cipheader', 'client-ip'),
        ('usip', 'yes'),
        ('useproxyport', 'yes'),
        ('sp', 'off'),
        ('rtspsessionidremap', 'off'),
        ('clttimeout', 100),
        ('svrtimeout', 100),
        ('customserverid', 476),
        ('cka', 'yes'),
        ('tcpb', 'yes'),
        ('cmp', 'no'),
        ('maxbandwidth', 10000),
        ('accessdown', '"NO"'),
        ('monthreshold', 100),
        ('downstateflush', 'enabled'),
        ('hashid', 10),
        ('comment', 'some comment'),
        ('appflowlog', 'enabled'),
        ('processlocal', 'enabled'),
        ('graceful', 'no'),
        ('monitor_bindings',[
                                OrderedDict(
                                    [
                                        ('monitorname','ping'),
                                        ('weight',50),
                                    ]
                                ),
                                OrderedDict(
                                    [
                                        ('monitorname','http'),
                                        ('weight',50),
                                    ]
                                ),
                            ]
        )
    ]
)
update_data = OrderedDict(
    [
        ('state', 'present'),
        ('name', 'service-http'),
        ('ip', '192.168.1.1'),
        ('ipaddress', '192.168.1.1'),
        ('port', 80),
        ('servicetype', 'HTTP'),
        ('cachetype', 'TRANSPARENT'),
        ('maxclient', 100),
        ('healthmonitor', 'no'),
        ('maxreq', 200),
        ('cacheable', 'no'),
        ('cip', 'enabled'),
        ('cipheader', 'client-ip'),
        ('usip', 'yes'),
        ('useproxyport', 'yes'),
        ('sp', 'off'),
        ('rtspsessionidremap', 'off'),
        ('clttimeout', 100),
        ('svrtimeout', 100),
        ('customserverid', 476),
        ('cka', 'yes'),
        ('tcpb', 'yes'),
        ('cmp', 'no'),
        ('maxbandwidth', 20000),
        ('accessdown', '"NO"'),
        ('monthreshold', 100),
        ('downstateflush', 'enabled'),
        ('hashid', 10),
        ('comment', 'some comment'),
        ('appflowlog', 'enabled'),
        ('processlocal', 'enabled'),
        ('monitor_bindings',[
                                OrderedDict(
                                    [
                                        ('monitorname','http'),
                                        ('weight',100),
                                    ]
                                ),
                            ]
        )
    ]
)

remove_data = OrderedDict(
    [
        ('name', 'service-http'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('update', update_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
# For Submodule 'ssl_service'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'ssl_service')
setup_data = OrderedDict(
    [
        ('state', 'present'),
        ('name', 'service-ssl'),
        ('ipaddress', '192.168.1.2'),
        ('port', 80),
        ('servicetype', 'SSL'),
        ('cleartextport', 80),
    ]
)

remove_data = OrderedDict(
    [
        ('name', 'service-ssl'),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

