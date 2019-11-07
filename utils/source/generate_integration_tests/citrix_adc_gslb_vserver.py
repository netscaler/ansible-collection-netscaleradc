from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_gslb_vserver'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', '10.10.10.11'),
            ('ipaddress', '10.10.10.11'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_gslb_site')
    testbed = OrderedDict(
        [
            ('sitename', 'gslb-site-1'),
            ('siteipaddress', '192.168.1.1'),
            ('sitetype', 'LOCAL'),
            ('publicip', '192.168.1.1'),
            ('metricexchange', 'enabled'),
            ('nwmetricexchange', 'enabled'),
            ('sessionexchange', 'enabled'),
            ('triggermonitor', 'ALWAYS'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_gslb_service')
    testbed = OrderedDict(
        [
            ('servicename', 'gslb-service-1'),
            ('servicetype', 'HTTP'),
            ('sitename', 'gslb-site-1'),
            ('ipaddress', '10.10.10.11'),
            ('port', 80),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    return testbed_data
    


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'flap_disabled'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME,  'flap_disabled')
    setup_data1 = OrderedDict(
        [
            ('name',  'gslb-vserver-2'),
            ('servicetype',  'HTTP'),
            ('lbmethod', 'SOURCEIPHASH'),
            ('netmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
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
            ('name',  'gslb-vserver-2'),
            ('servicetype',  'HTTP'),
            ('lbmethod', 'SOURCEIPHASH'),
            ('netmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
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
            ('name',  'gslb-vserver-2'),
            ('state',  'absent'),
        ]
    )
    
    submodObj.add_operation('setup',  [[setup_data1, setup_data1_extra_vars], [setup_data2, setup_data2_extra_vars]], run_once=True)
    submodObj.add_operation('remove',  remove_data, run_once=True)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'http'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'http')
    setup_data = OrderedDict(
        [
            ('name', 'gslb-vserver-1'),
            ('servicetype', 'HTTP'),
            ('dnsrecordtype', 'A'),
            ('lbmethod', 'ROUNDROBIN'),
            ('backuplbmethod', 'RTT'),
            ('tolerance', 50),
            ('persistencetype', 'NONE'),
            ('persistenceid', 500),
            ('persistmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
            ('timeout', 1000),
            ('mir', 'disabled'),
            ('disableprimaryondown', 'disabled'),
            ('dynamicweight', 'DISABLED'),
            ('considereffectivestate', 'NONE'),
            ('comment', 'some comment'),
            ('somethod', 'CONNECTION'),
            ('sopersistence', 'disabled'),
            ('sopersistencetimeout', 100),
            ('sothreshold', 5000),
            ('sobackupaction', 'DROP'),
            ('appflowlog', 'disabled'),
            ('domain_bindings',[
                                    OrderedDict(
                                        [
                                            ('domainname','example.com'),
                                            ('cookietimeout',100),
                                            ('backupip','10.10.10.10'),
                                            ('ttl',100),
                                            ('sitedomainttl',200),
                                        ]
                                    ),
                                ]
            ),
            ('service_bindings',[
                                    OrderedDict(
                                        [
                                            ('weight',100),
                                            ('servicename','gslb-service-1'),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    
    update_data = OrderedDict(
        [
            ('name', 'gslb-vserver-1'),
            ('servicetype', 'HTTP'),
            ('dnsrecordtype', 'A'),
            ('lbmethod', 'ROUNDROBIN'),
            ('backuplbmethod', 'RTT'),
            ('tolerance', 50),
            ('persistencetype', 'NONE'),
            ('persistenceid', 500),
            ('persistmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
            ('timeout', 500),
            ('mir', 'disabled'),
            ('disableprimaryondown', 'disabled'),
            ('dynamicweight', 'DISABLED'),
            ('considereffectivestate', 'NONE'),
            ('comment', 'some comment'),
            ('somethod', 'CONNECTION'),
            ('sopersistence', 'disabled'),
            ('sopersistencetimeout', 100),
            ('sothreshold', 5000),
            ('sobackupaction', 'DROP'),
            ('appflowlog', 'disabled'),
            ('domain_bindings',[
                                    OrderedDict(
                                        [
                                            ('domainname','example.com'),
                                            ('cookietimeout',100),
                                            ('backupip','10.10.10.10'),
                                            ('ttl',100),
                                            ('sitedomainttl',200),
                                        ]
                                    ),
                                ]
            ),
            ('service_bindings',[
                                    OrderedDict(
                                        [
                                            ('weight',100),
                                            ('servicename','gslb-service-1'),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    update_domainbinding_data = OrderedDict(
        [
            ('name', 'gslb-vserver-1'),
            ('servicetype', 'HTTP'),
            ('dnsrecordtype', 'A'),
            ('lbmethod', 'ROUNDROBIN'),
            ('backuplbmethod', 'RTT'),
            ('tolerance', 50),
            ('persistencetype', 'NONE'),
            ('persistenceid', 500),
            ('persistmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
            ('timeout', 500),
            ('mir', 'disabled'),
            ('disableprimaryondown', 'disabled'),
            ('dynamicweight', 'DISABLED'),
            ('considereffectivestate', 'NONE'),
            ('comment', 'some comment'),
            ('somethod', 'CONNECTION'),
            ('sopersistence', 'disabled'),
            ('sopersistencetimeout', 100),
            ('sothreshold', 5000),
            ('sobackupaction', 'DROP'),
            ('appflowlog', 'disabled'),
            ('domain_bindings',[
                                    OrderedDict(
                                        [
                                            ('domainname','anotherexample.com'),
                                            ('cookietimeout',100),
                                            ('backupip','10.10.10.10'),
                                            ('ttl',100),
                                            ('sitedomainttl',200),
                                        ]
                                    ),
                                ]
            ),
            ('service_bindings',[
                                    OrderedDict(
                                        [
                                            ('weight',100),
                                            ('servicename','gslb-service-1'),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    update_gslbservice_binding_data = OrderedDict(
        [
            ('name', 'gslb-vserver-1'),
            ('servicetype', 'HTTP'),
            ('dnsrecordtype', 'A'),
            ('lbmethod', 'ROUNDROBIN'),
            ('backuplbmethod', 'RTT'),
            ('tolerance', 50),
            ('persistencetype', 'NONE'),
            ('persistenceid', 500),
            ('persistmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
            ('timeout', 500),
            ('mir', 'disabled'),
            ('disableprimaryondown', 'disabled'),
            ('dynamicweight', 'DISABLED'),
            ('considereffectivestate', 'NONE'),
            ('comment', 'some comment'),
            ('somethod', 'CONNECTION'),
            ('sopersistence', 'disabled'),
            ('sopersistencetimeout', 100),
            ('sothreshold', 5000),
            ('sobackupaction', 'DROP'),
            ('appflowlog', 'disabled'),
            ('domain_bindings',[
                                    OrderedDict(
                                        [
                                            ('domainname','example.com'),
                                            ('cookietimeout',100),
                                            ('backupip','10.10.10.10'),
                                            ('ttl',200),
                                            ('sitedomainttl',200),
                                        ]
                                    ),
                                ]
            ),
            ('service_bindings',[
                                    OrderedDict(
                                        [
                                            ('weight',50),
                                            ('servicename','gslb-service-1'),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    
    
    
    remove_data = OrderedDict(
        [
            ('name', 'gslb-vserver-1'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('update_domainbinding', update_domainbinding_data)
    submodObj.add_operation('update_gslbservice_binding', update_gslbservice_binding_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'sourceiphash'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'sourceiphash')
    setup_data = OrderedDict(
        [
            ('name', 'gslb-vserver-2'),
            ('servicetype', 'HTTP'),
            ('lbmethod', 'SOURCEIPHASH'),
            ('netmask', '255.255.255.0'),
            ('v6persistmasklen', 128),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'gslb-vserver-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
