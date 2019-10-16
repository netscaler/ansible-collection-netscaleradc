from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_gslb_service'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
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
    
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'lb-monitor-for-gslb-service'),
            ('type', 'TCP-ECV'),
            ('send', 'sendstring'),
            ('recv', 'recvstring'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', '10.10.10.10'),
            ('ipaddress', '10.10.10.10'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    return testbed_data

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'cname'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'cname')
    setup_data = OrderedDict(
        [
            ('servicename', 'gslb-service-2'),
            ('cnameentry', 'example.com'),
            ('sitename', 'gslb-site-1'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('servicename', 'gslb-service-2'),
            ('cnameentry', 'example.com'),
            ('sitename', 'gslb-site-1'),
            ('comment', 'addded comment'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('servicename', 'gslb-service-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'http'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'http')
    setup_data = OrderedDict(
        [
            ('servicename','gslb-service-1'),
            ('servicetype','HTTP'),
            ('sitename','gslb-site-1'),
            ('ipaddress','10.10.10.11'),
            ('port', 80),
            ('publicip','10.10.10.11'),
            ('publicport', 80),
            ('maxclient', 100),
            ('healthmonitor','"NO"'),
            ('cip','enabled'),
            ('cipheader','hello'),
            ('sitepersistence','NONE'),
            ('siteprefix','prefix'),
            ('clttimeout','100'),
            ('maxbandwidth','100'),
            ('downstateflush','enabled'),
            ('maxaaausers','100'),
            ('monthreshold','500'),
            ('hashid','10'),
            ('comment','cool gslb service!'),
            ('appflowlog','enabled'),
            ('monitor_bindings',[
                                    OrderedDict(
                                        [
                                            ('monitor_name','lb-monitor-for-gslb-service'),
                                            ('weight',100),
                                        ]
                                    ),
                                ]
            )
    
        ]
    )
    
    update_data = OrderedDict(
        [
            ('servicename','gslb-service-1'),
            ('servicetype','HTTP'),
            ('sitename','gslb-site-1'),
            ('ipaddress','10.10.10.11'),
            ('port', 80),
            ('publicip','10.10.10.11'),
            ('publicport', 80),
            ('maxclient', 100),
            ('healthmonitor','"NO"'),
            ('cip','enabled'),
            ('cipheader','hello'),
            ('sitepersistence','NONE'),
            ('siteprefix','prefix'),
            ('clttimeout','100'),
            ('maxbandwidth','100'),
            ('downstateflush','enabled'),
            ('maxaaausers','100'),
            ('monthreshold','500'),
            ('hashid','10'),
            ('comment','some other comment'),
            ('appflowlog','enabled'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('servicename', 'gslb-service-1'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'servername'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'servername')
    setup_data = OrderedDict(
        [
            ('servicename','gslb-service-3'),
            ('servername','10.10.10.10'),
            ('servicetype','HTTP'),
            ('port', 80),
            ('sitename','gslb-site-1'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('servicename','gslb-service-3'),
            ('servername','10.10.10.10'),
            ('servicetype','HTTP'),
            ('port', 80),
            ('sitename','gslb-site-1'),
            ('comment','added comment'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('servicename', 'gslb-service-3'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
