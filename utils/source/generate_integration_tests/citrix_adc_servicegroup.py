from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_servicegroup'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'monitor-http'),
            ('type', 'HTTP'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'monitor-http-inline'),
            ('type', 'HTTP-INLINE'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_lb_monitor')
    testbed = OrderedDict(
        [
            ('monitorname', 'monitor-tcp'),
            ('type', 'TCP'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', '10.78.78.78'),
            ('ipaddress', '10.78.78.78'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', '10.79.79.79'),
            ('ipaddress', '10.79.79.79'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', 'server_by_name_1'),
            ('ipaddress', '10.80.80.80'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_server')
    testbed = OrderedDict(
        [
            ('name', 'server_by_name_2'),
            ('ipaddress', '10.90.90.90'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    return testbed_data

def bind_unbind_servicemembers(input_data):
    test_type='citrix_adc_direct_calls'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'servicegroup_bind_unbind')
    member_by_ip = OrderedDict([
                                ('ip','10.78.78.78'),
                                ('port',80),
                                ('weight',100),
                            ])
    member_by_name = OrderedDict([
                        ('servername', 'server_by_name_1'),
                        ('port', 80),
                        ('weight', 100),
                    ])
    data = OrderedDict(
        [
            ('servicegroupname', 'service-group-bind-unbind'),
            ('servicetype', 'HTTP'),
            ('state', 'present'),
            ('servicemembers', OrderedDict([
                                    ('mode', 'bind'),
                                    ('attributes', [ member_by_ip ]),
                                ]),
            ),
        ]
    )
    submodObj.add_operation('setup', copy.deepcopy(data))

    # Add a member
    data['servicemembers']['attributes'].append(member_by_name)

    submodObj.add_operation('bind_additional_servicemember', copy.deepcopy(data))

    # Unbind members
    data['servicemembers']['mode'] = 'unbind'
    data['servicemembers']['attributes'] = [member_by_name]
    submodObj.add_operation('unbind_servicemember_by_name', copy.deepcopy(data))


    data['servicemembers']['attributes'] = [ member_by_name, member_by_ip]
    submodObj.add_operation('unbind_servicemember_by_ip', copy.deepcopy(data))

    data['state'] = 'absent'

    submodObj.add_operation('remove', copy.deepcopy(data))

    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})


def dsapi_test(input_data):
    test_type='citrix_adc_direct_calls'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'servicegroup_dsapi')

    member_1 = OrderedDict([
                ('ip','10.78.78.78'),
                ('port',80),
                ('weight',100),
            ])

    member_2 = OrderedDict([
                ('ip','10.79.79.79'),
                ('port',80),
                ('weight',100),
            ])

    data = OrderedDict(
        [
            ('servicegroupname', 'service-group-dsapi'),
            ('servicetype', 'HTTP'),
            ('state', 'present'),
            ('autoscale', 'API'),
            ('servicemembers', OrderedDict([
                                    ('mode', 'dsapi'),
                                    ('attributes', [ member_1, member_2 ]),
                                ]),
            ),
        ]
    )
    submodObj.add_operation('setup', copy.deepcopy(data), run_once=True)

    altered_member_1 = copy.deepcopy(member_1)
    altered_member_1['weight'] = 50
    data['servicemembers']['attributes'] = [altered_member_1, member_2]
    submodObj.add_operation('update_alter_member', copy.deepcopy(data), run_once=True)

    data['servicemembers']['attributes'] = [member_2]
    submodObj.add_operation('update_remove_member', copy.deepcopy(data), run_once=True)

    data['servicemembers']['attributes'] = [member_2, member_1]
    submodObj.add_operation('update_readd_member', copy.deepcopy(data), run_once=True)

    data['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(data), run_once=True)

    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'flap_disabled'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME,  'flap_disabled')
    setup_data1 = OrderedDict(
        [
            ('state','present'),
            ('servicegroupname','service-group-1'),
            ('servicetype','HTTP'),
            ('servicemembers', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes',  [OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port', 80),
                                            ('weight', 100),
                                        ]
                                      )]),
                                ])
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
            ('servicemembers', OrderedDict([
                                ('mode', 'exact'),
                                ('attributes', [OrderedDict(
                                    [
                                        ('ip','10.78.78.78'),
                                        ('port', 80),
                                        ('weight', 100),
                                    ]
                                )]),
                              ])
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
            ('servicemembers', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [OrderedDict(
                                        [
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]
                                    )]),
                                ])
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
            ('servicemembers', OrderedDict([
                                        ('mode', 'exact'),
                                        ('attributes', [
                                            OrderedDict([
                                                ('ip','10.78.78.78'),
                                                ('port',80),
                                                ('weight', 100),
                                            ]),
                                            OrderedDict([
                                                ('ip','10.79.79.79'),
                                                ('port',80),
                                                ('weight', 50),
                                            ]),
                                        ])
                                    ]),
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
            ('servicemembers', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [
                                        OrderedDict(
                                            [
                                                ('ip','10.78.78.78'),
                                                ('port',80),
                                                ('weight', 100),
                                            ]
                                        ),
                                    ])
                                ]),
            ),
            ('monitor_bindings', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [
                                         OrderedDict(
                                            [
                                                ('monitor_name','monitor-http'),
                                                ('weight',50),
                                            ]
                                        ),
                                        OrderedDict(
                                            [
                                                ('monitor_name','monitor-tcp'),
                                                ('weight',50),
                                            ]
                                        ),
                                    ]),
                                ])
            ),
    ])
    update_data = OrderedDict([
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [
                                        OrderedDict([
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight', 100),
                                        ])
                                    ]),
                                ])
            ),
            ('monitor_bindings', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [
                                        OrderedDict([
                                            ('monitor_name','monitor-http'),
                                            ('weight',80),
                                        ]),
                                        OrderedDict([
                                            ('monitor_name','monitor-tcp'),
                                            ('weight',20),
                                        ]),
                                    ])
                                ]),
            )
        ])
    default_only_data = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [
                                        OrderedDict([
                                            ('ip','10.78.78.78'),
                                            ('port',80),
                                            ('weight',100),
                                        ]),
                                    ])
                                ])
            ),
            ('monitor_bindings', OrderedDict([
                                    ('mode', 'exact'),
                                    ('attributes', [])
                                ]),
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

    # Do the bind unbind tests
    bind_unbind_servicemembers(input_data)

    # Do the dsapi tests
    dsapi_test(input_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
