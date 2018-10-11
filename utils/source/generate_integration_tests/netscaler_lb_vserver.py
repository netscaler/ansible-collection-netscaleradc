from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_lb_vserver'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_server')
    testbed = OrderedDict(
        [
            ('name', 'server-{{ item }}'),
            ('ipaddress', '192.168.1.{{ item }}'),
        ]
    )
    testbed_extra_vars = OrderedDict(
        [
            ('with_sequence','count=6'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', [testbed, testbed_extra_vars]))
    
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_service')
    testbed = OrderedDict(
        [
            ('name', 'service-http-{{ item }}'),
            ('servername', 'server-{{ item }}'),
            ('servicetype', 'HTTP'),
            ('port', 80),
        ]
    )
    testbed_extra_vars = OrderedDict(
        [
            ('with_sequence','count=2'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', [testbed, testbed_extra_vars]))
    
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_servicegroup')
    testbed = OrderedDict(
        [
            ('servicegroupname', 'service-group-1'),
            ('servicetype', 'HTTP'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('servername','server-3'),
                                            ('port', 80),
                                            ('weight', 50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servername','server-4'),
                                            ('port', 80),
                                            ('weight', 50),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_servicegroup')
    testbed = OrderedDict(
        [
            ('servicegroupname', 'service-group-2'),
            ('servicetype', 'HTTP'),
            ('servicemembers', [
                                    OrderedDict(
                                        [
                                            ('servername','server-5'),
                                            ('port', 80),
                                            ('weight', 50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servername','server-6'),
                                            ('port', 80),
                                            ('weight', 50),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_lb_vserver')
    testbed = OrderedDict(
        [
            ('name', 'lb-vserver-push'),
            ('port', 80),
            ('servicetype', 'PUSH'),
            ('ipv46', '192.1.1.1'),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    # Appfw policy prerequisite
    testbedObj = BaseIntegrationModule(test_type, 'netscaler_appfw_policy')
    
    testbed = OrderedDict([
            ('name',  'policy_lb_vserver_integration_helper'),
            ('rule', 'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")'),
            ('profilename', 'APPFW_BLOCK'),
    ])
    
    testbed_data.append(testbedObj.add_testbed('setup_appfw_policy', [testbed, {}]))
 
    return testbed_data
    

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'lb_vserver_any'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_any')
    setup_data = OrderedDict(
        [
            ('state', 'present'),
            ('name', 'lb-vserver-4'),
            ('ipv46', '10.79.1.4'),
            ('port', 80),
            ('servicetype', 'ANY'),
            ('connfailover', 'STATELESS'),
            ('skippersistency', 'None'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-4'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_dns'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_dns')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-8'),
            ('ipv46', '10.79.1.8'),
            ('port', 80),
            ('servicetype', 'DNS'),
            ('recursionavailable', 'no'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-8'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_flap_disabled'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME,  'lb_vserver_flap_disabled')
    setup_data1 = OrderedDict(
        [
            ('state',  'present'),
            ('name',  'lb-vserver-flap'),
            ('ipv46',  '10.79.1.2'),
            ('servicetype',  'HTTP'),
            ('port',  80),
            ('servicebindings', [
                                    OrderedDict(
                                        [
                                            ('servername','service-http-1'),
                                            ('weight', 50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servername','service-http-2'),
                                            ('weight', 50),
                                        ]
                                    ),
                                ]
            ),
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
            ('state',  'present'),
            ('name',  'lb-vserver-flap'),
            ('ipv46',  '10.79.1.2'),
            ('servicetype',  'HTTP'),
            ('port',  80),
            ('servicebindings', [
                                    OrderedDict(
                                        [
                                            ('servername','service-http-1'),
                                            ('weight', 50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servername','service-http-2'),
                                            ('weight', 50),
                                        ]
                                    ),
                                ]
            ),
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
            ('name',  'lb-vserver-flap'),
            ('state',  'absent'),
        ]
    )
    
    submodObj.add_operation('setup',  [[setup_data1, setup_data1_extra_vars], [setup_data2, setup_data2_extra_vars]], run_once=True)
    submodObj.add_operation('remove',  remove_data, run_once=True)
    
    
    # For Submodule 'lb_vserver_http'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_http')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name','lb-vserver-1'),
            ('ipv46','10.79.1.1'),
            ('port',80),
            ('range',2),
            ('servicetype','HTTP'),
            ('persistencetype','COOKIEINSERT'),
            ('timeout',100),
            ('persistencebackup','SOURCEIP'),
            ('backuppersistencetimeout',110),
            ('lbmethod','URLHASH'),
            ('cookiename','COOKIE'),
            ('listenpolicy','"CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24)"'),
            ('listenpriority',66),
            ('persistmask','255.255.0.0'),
            ('v6persistmasklen',64),
            ('m','IP'),
            ('tosid',6),
            ('sessionless','disabled'),
            ('redirurl','http://somewhere.com'),
            ('cacheable','no'),
            ('clttimeout',111),
            ('somethod','CONNECTION'),
            ('sopersistence','disabled'),
            ('sopersistencetimeout',222),
            ('sothreshold',4096),
            ('healththreshold',55),
            ('sobackupaction','DROP'),
            ('redirectportrewrite','disabled'),
            ('downstateflush','disabled'),
            ('disableprimaryondown','disabled'),
            ('insertvserveripport','VIPADDR'),
            ('vipheader','vip'),
            ('authenticationhost','authenticate.me'),
            ('authentication','off'),
            ('authn401','off'),
            ('authnvsname','somename'),
            ('push','disabled'),
            ('pushmulticlients','no'),
            ('comment','Vserver comment'),
            ('l2conn','"OFF"'),
            ('appflowlog','disabled'),
            ('icmpvsrresponse','PASSIVE'),
            ('rhistate','PASSIVE'),
            ('newservicerequest',11),
            ('newservicerequestunit','PER_SECOND'),
            ('newservicerequestincrementinterval',5),
            ('minautoscalemembers',8),
            ('maxautoscalemembers',10),
            ('macmoderetainvlan','disabled'),
            ('dns64','disabled'),
            ('bypassaaaa','no'),
            ('processlocal','disabled'),
            ('backuplbmethod','LEASTCONNECTION'),
            ('hashlength',100),
            ('servicebindings', [
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-1'),
                                            ('weight',50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-2'),
                                            ('weight',50),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    update_data = OrderedDict(
        [
            ('state','present'),
            ('name','lb-vserver-1'),
            ('ipv46','10.79.1.1'),
            ('port',80),
            ('range',2),
            ('servicetype','HTTP'),
            ('persistencetype','COOKIEINSERT'),
            ('timeout',100),
            ('persistencebackup','SOURCEIP'),
            ('backuppersistencetimeout',110),
            ('lbmethod','URLHASH'),
            ('cookiename','COOKIE'),
            ('listenpolicy','"CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24)"'),
            ('listenpriority',66),
            ('persistmask','255.255.0.0'),
            ('v6persistmasklen',64),
            ('m','IP'),
            ('tosid',6),
            ('sessionless','disabled'),
            ('redirurl','http://somewhere.com'),
            ('cacheable','no'),
            ('clttimeout',222),
            ('somethod','CONNECTION'),
            ('sopersistence','disabled'),
            ('sopersistencetimeout',222),
            ('sothreshold',4096),
            ('healththreshold',55),
            ('sobackupaction','DROP'),
            ('redirectportrewrite','disabled'),
            ('downstateflush','disabled'),
            ('disableprimaryondown','disabled'),
            ('insertvserveripport','VIPADDR'),
            ('vipheader','vip'),
            ('authenticationhost','authenticate.me'),
            ('authentication','off'),
            ('authn401','off'),
            ('authnvsname','somename'),
            ('push','disabled'),
            ('pushmulticlients','no'),
            ('comment','Vserver comment'),
            ('l2conn','"OFF"'),
            ('appflowlog','disabled'),
            ('icmpvsrresponse','PASSIVE'),
            ('rhistate','PASSIVE'),
            ('newservicerequest',11),
            ('newservicerequestunit','PER_SECOND'),
            ('newservicerequestincrementinterval',5),
            ('minautoscalemembers',8),
            ('maxautoscalemembers',10),
            ('macmoderetainvlan','disabled'),
            ('dns64','disabled'),
            ('bypassaaaa','no'),
            ('processlocal','disabled'),
            ('backuplbmethod','LEASTCONNECTION'),
            ('hashlength',100),
            ('servicebindings', [
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-1'),
                                            ('weight',60),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-2'),
                                            ('weight',40),
                                        ]
                                    ),
                                ]
            ),
        ]
    )
    
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-1'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_iphash'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_iphash')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-10'),
            ('port', 80),
            ('servicetype', 'HTTP'),
            ('lbmethod','DESTINATIONIPHASH'),
            ('netmask','255.255.255.0'),
            ('ippattern','10.68.0.0'),
            ('ipmask','255.255.0.0'),
            ('v6netmasklen',24),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-10'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_ippattern'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_ippattern')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-9'),
            ('port', 80),
            ('servicetype', 'HTTP'),
            ('ippattern','10.67.0.0'),
            ('ipmask','255.255.0.0'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-9'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_mssql'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_mssql')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-6'),
            ('ipv46','10.79.1.6'),
            ('port',80),
            ('servicetype','MSSQL'),
            ('mssqlserverversion',2000),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-6'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_mysql'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_mysql')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-7'),
            ('ipv46','10.79.1.7'),
            ('port',80),
            ('servicetype','MYSQL'),
            ('mysqlprotocolversion',2),
            ('mysqlserverversion',10),
            ('mysqlcharacterset',8),
            ('mysqlservercapabilities',244),
            ('dbslb','disabled'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-7'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_oracle'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_oracle')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-5'),
            ('ipv46','10.79.1.5'),
            ('port',80),
            ('servicetype','ORACLE'),
            ('oracleserverversion','10G'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-5'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_push'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_push')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-11'),
            ('port',80),
            ('servicetype','HTTP'),
            ('lbmethod','DESTINATIONIPHASH'),
            ('netmask','255.255.255.0'),
            ('ippattern','10.69.0.0'),
            ('ipmask','255.255.0.0'),
            ('v6netmasklen',24),
            ('pushvserver','lb-vserver-push'),
            ('pushlabel','none'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-11'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_tcp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_tcp')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-3'),
            ('ipv46', '10.79.1.3'),
            ('port',80),
            ('servicetype','TCP'),
            ('lbmethod','TOKEN'),
            ('datalength',20),
            ('dataoffset',5),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-3'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_servicegroup'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_servicegroup')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-20'),
            ('ipv46', '10.79.1.8'),
            ('port',80),
            ('servicetype','HTTP'),
            ('servicegroupbindings',[
                                    OrderedDict(
                                        [
                                            ('servicegroupname','service-group-1'),
                                        ]
                                    )
                                ]
            )
        ]
    )
    update_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-20'),
            ('ipv46', '10.79.1.8'),
            ('port',80),
            ('servicetype','HTTP'),
            ('servicegroupbindings',[
                                    OrderedDict(
                                        [
                                            ('servicegroupname','service-group-2'),
                                        ]
                                    )
                                ]
            )
        ]
    )
    update_service_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-20'),
            ('ipv46', '10.79.1.8'),
            ('port',80),
            ('servicetype','HTTP'),
            ('servicebindings',[
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-1'),
                                            ('weight',50),
                                        ]
                                    ),
                                    OrderedDict(
                                        [
                                            ('servicename','service-http-2'),
                                            ('weight',50),
                                        ]
                                    ),
                                ]
            )
        ]
    )
    
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-20'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('update_service', update_service_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_rtspnat'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_rtspnat')
    setup_data = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-2'),
            ('port',80),
            ('ipv46','10.79.1.2'),
            ('servicetype','RTSP'),
            ('rtspnat','on'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('name', 'lb-vserver-2'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_vserver_appfwpolicy'
    
   
    # Actual module
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_vserver_appfwpolicy_binding')
    attributes = OrderedDict(
        [
            ('state','present'),
            ('name', 'lb-vserver-appfw-policy'),
            ('port',80),
            ('ipv46','10.79.1.3'),
            ('servicetype','HTTP'),
            ('appfw_policybindings', [
                OrderedDict([
                    ('priority', '100'),
                    ('bindpoint', 'REQUEST'),
                    ('policyname', 'policy_lb_vserver_integration_helper'),
                    ('labelname', 'lb-vserver-appfw-policy'),
                    ('gotopriorityexpression', '101'),
                    ('invoke', True),
                    ('labeltype', 'reqvserver'),
                ])
            ])
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    attributes['appfw_policybindings'] = []
    submodObj.add_operation('remove_appfw_bindings', copy.deepcopy(attributes))
    
    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
