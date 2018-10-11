from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'netscaler_servicegroup'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'monitor-1'),
            ('type', 'HTTP'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'monitor-2'),
            ('type', 'HTTP'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    return testbed_data
    

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'flap_disabled'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME,  'flap_disabled')
    setup_data1 = OrderedDict(
        [
            ('state','present'),
            ('servicegroupname','service-group-1'),
            ('servicetype','HTTP'),
            ('servicemembers',[
                                OrderedDict(
                                    [
                                        ('ip','10.78.78.78'),
                                        ('port', 80),
                                        ('weight', 100),
                                    ]
                                ),
                              ]
            ),
            ('disabled','{{ item|int % 2 }}'),
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
            ('state','present'),
            ('servicegroupname','service-group-1'),
            ('servicetype','HTTP'),
            ('servicemembers',[
                                OrderedDict(
                                    [
                                        ('ip','10.78.78.78'),
                                        ('port', 80),
                                        ('weight', 100),
                                    ]
                                ),
                              ]
            ),
            ('disabled','{{ item|int % 2 }}'),
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
            ('servicegroupname',  'service-group-1'),
            ('state',  'absent'),
            ('servicetype',  'HTTP'),
        ]
    )
    
    submodObj.add_operation('setup',  [[setup_data1, setup_data1_extra_vars], [setup_data2, setup_data2_extra_vars]], run_once=True)
    submodObj.add_operation('remove',  remove_data, run_once=True)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    
    
    # For Submodule 'servicegroup'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'servicegroup')
    setup_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('cachetype', 'TRANSPARENT'),
            ('maxclient', 100),
            ('maxreq', 100),
            ('cacheable', 'no'),
            ('cip', 'enabled'),
            ('cipheader', 'cip-header'),
            ('usip', 'no'),
            ('pathmonitor', 'no'),
            ('pathmonitorindv', 'no'),
            ('useproxyport', 'no'),
            ('healthmonitor', 'no'),
            ('sp', 'off'),
            ('rtspsessionidremap', 'off'),
            ('clttimeout', 2000),
            ('svrtimeout', 2000),
            ('cka', 'yes'),
            ('tcpb', 'yes'),
            ('cmp', 'no'),
            ('maxbandwidth', 5000),
            ('monthreshold', 100),
            ('downstateflush', 'disabled'),
            ('comment', 'some comment'),
            ('appflowlog', 'enabled'),
            # ('autoscale', 'POLICY'),
            # ('memberport', 80),
            ('graceful', 'no'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    
    update_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('cachetype', 'TRANSPARENT'),
            ('maxclient', 100),
            ('maxreq', 100),
            ('cacheable', 'no'),
            ('cip', 'enabled'),
            ('cipheader', 'cip-header'),
            ('usip', 'no'),
            ('pathmonitor', 'no'),
            ('pathmonitorindv', 'no'),
            ('useproxyport', 'no'),
            ('healthmonitor', 'no'),
            ('sp', 'off'),
            ('rtspsessionidremap', 'off'),
            ('clttimeout', 1000),
            ('svrtimeout', 1000),
            ('cka', 'yes'),
            ('tcpb', 'yes'),
            ('cmp', 'no'),
            ('maxbandwidth', 5000),
            ('monthreshold', 100),
            ('downstateflush', 'disabled'),
            ('comment', 'some comment'),
            ('appflowlog', 'enabled'),
            # ('autoscale', 'POLICY'),
            # ('memberport', 80),
            ('graceful', 'no'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('ip','10.79.79.79'),
                                            ('port',80),
                                            ('weight',50),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('state', 'absent'),
            ('servicetype', 'HTTP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'servicegroup_monitors'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'servicegroup_monitors')
    setup_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    ),
                                ]
            ),
            ('monitorbindings', [
                                    OrderedDict(
                                        [
                                            ('monitorname','monitor-1'),
                                            ('weight',50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('monitorname','monitor-2'),
                                            ('weight',50),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    update_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    ),
                                ]
            ),
            ('monitorbindings', [
                                    OrderedDict(
                                        [
                                            ('monitorname','monitor-1'),
                                            ('weight',80),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('monitorname','monitor-2'),
                                            ('weight',20),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    default_only_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    
    
    remove_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update',update_data)
    submodObj.add_operation('default_only', default_only_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
