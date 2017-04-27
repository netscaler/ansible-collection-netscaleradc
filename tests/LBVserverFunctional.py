import unittest
import copy
import json
import sys
import yaml

from . import utils





class LBVserverFullInitialValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        playbook = copy.deepcopy(cls.minimal_playbook)
        playbook[0]['tasks'] = [
            {
                'name': 'Setup http service',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_service',
                    'name': 'service-http-1',
                    'ipaddress': '192.168.1.1',
                    'servicetype': 'HTTP',
                    'port': 80,
                },
            },
            {
                'name': 'Setup http service',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_service',
                    'name': 'service-http-2',
                    'ipaddress': '192.168.1.2',
                    'servicetype': 'HTTP',
                    'port': 80,
                }
            }
        ]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        playbook[0]['tasks'][1]['local_action'].update(utils.nitro_dict)
        result = utils.run_ansible_play(playbook, testcase='setup_lbvserverfullinitialvalues')

        utils.make_dbprofile('dbprofile1')
        utils.make_tcpprofile('tcp-profile-1')
        utils.make_netprofile('net-profile-1')
        utils.make_httpprofile('http-profile-1')
        utils.make_dnsprofile('dns-profile-1')
        utils.make_authnprofile(
            'auth-profile-1', 
            'vs1',
            'vs1.example.com',
            'example.com',
            1,
        )



        cls.attributes_to_check = [
            'name', 
            'servicetype', 
            'ipv46', 
            'ippattern', 
            'ipmask', 
            'port', 
            'range', 
            'persistencetype', 
            'timeout', 
            'persistencebackup', 
            'backuppersistencetimeout', 
            'lbmethod', 
            'hashlength', 
            'netmask', 
            'v6netmasklen', 
            'backuplbmethod', 
            'cookiename', 
            'rule', 
            'listenpolicy', 
            'listenpriority', 
            'resrule', 
            'persistmask', 
            'v6persistmasklen', 
            'pq', 
            'sc', 
            'rtspnat', 
            'm', 
            'tosid', 
            'datalength', 
            'dataoffset', 
            'sessionless', 
            'state', 
            'connfailover', 
            'redirurl', 
            'cacheable', 
            'clttimeout', 
            'somethod', 
            'sopersistence', 
            'sopersistencetimeout', 
            'healththreshold', 
            'sothreshold', 
            'sobackupaction', 
            'redirectportrewrite', 
            'downstateflush', 
            'backupvserver', 
            'disableprimaryondown', 
            'insertvserveripport', 
            'vipheader', 
            'authenticationhost', 
            'authentication', 
            'authn401', 
            'authnvsname', 
            'push', 
            'pushvserver', 
            'pushlabel', 
            'pushmulticlients', 
            'tcpprofilename', 
            'httpprofilename', 
            'dbprofilename', 
            'comment', 
            'l2conn', 
            'oracleserverversion', 
            'mssqlserverversion', 
            'mysqlprotocolversion', 
            'mysqlserverversion', 
            'mysqlcharacterset', 
            'mysqlservercapabilities', 
            'appflowlog', 
            'netprofile', 
            'icmpvsrresponse', 
            'rhistate', 
            'newservicerequest', 
            'newservicerequestunit', 
            'newservicerequestincrementinterval', 
            'minautoscalemembers', 
            'maxautoscalemembers', 
            'persistavpno', 
            'skippersistency', 
            'td', 
            'authnprofile', 
            'macmoderetainvlan', 
            'dbslb', 
            'dns64', 
            'bypassaaaa', 
            'recursionavailable', 
            'processlocal', 
            'dnsprofilename', 
            'lbprofilename', 
            'redirectfromport', 
            'httpsredirecturl', 
            'weight', 
            'servicename', 
            'redirurlflags'
        ]

    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        documented_omissions = [
            'rule',
            'resrule',
            'state',
            'backupvserver',
            'persistavpno',
            'td',
            'lbprofilename',
            'redirectfromport',
            'httpsredirecturl',
            'weight',
            'servicename',
            'redirurlflags'
        ]
        self.assertListEqual(self.attributes_to_check,documented_omissions)


    def test_01_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_1',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-1',
                    'ipv46': '10.79.1.1',
                    'port': 80,
                    'range': 2,
                    'servicetype': 'HTTP',
                    'persistencetype': 'COOKIEINSERT',
                    'timeout': 100,
                    'persistencebackup': 'SOURCEIP',
                    'backuppersistencetimeout': 110,
                    'lbmethod': 'URLHASH',
                    'cookiename': 'COOKIE',
                    'listenpolicy': 'CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24)',
                    'listenpriority': 66,

                    'persistmask': '255.255.0.0',
                    'v6persistmasklen': 64,
                    'pq': '"ON"',
                    'sc': '"ON"',
                    'm': 'IP',
                    'tosid': 6,
                    'sessionless': 'DISABLED',

                    #"rule": "missing from other"
                    #'rule': 'nothing',

                    #"resrule": "missing from other"
                    # 'resrule': 'someexpression',


                    #"state": "missing from other"
                    #'state': 'ENABLED',

                    'redirurl': 'http://somewhere.com',
                    'cacheable': '"NO"',
                    'clttimeout': 111,
                    'somethod': 'CONNECTION',
                    'sopersistence': 'DISABLED',
                    'sopersistencetimeout': 222,
                    'sothreshold': 4096,
                    'healththreshold': 55,

                    'sobackupaction': 'DROP',
                    'redirectportrewrite': 'DISABLED',
                    'downstateflush': 'DISABLED',
                    'disableprimaryondown': 'DISABLED',
                    'insertvserveripport': 'VIPADDR',
                    'vipheader': 'vip',
                    'authenticationhost': 'authenticate.me',
                    'authentication': '"OFF"',
                    'authn401': '"OFF"',
                    'authnvsname': 'somename',
                    'push': 'DISABLED',

                    #'pushvserver': 'somepushserver',
                    #"msg": "nitro exception errorcode=258,message=No such resource [pushVserver, somepushserver]"

                    #'pushlabel': 'somelabel',
                    #"msg": "nitro exception errorcode=3081,message=Expression syntax error [^somelabel, Offset 0]"

                    'pushmulticlients': '"NO"',

                    'tcpprofilename': 'tcp-profile-1',
                    'httpprofilename': 'http-profile-1',

                    #'dbprofilename': 'someprofile',
                    #"msg": "nitro exception errorcode=1092,message=Arguments cannot both be specified [dbProfileName, serviceType==HTTP]"

                    'comment': 'Vserver comment',
                    'l2conn': '"OFF"',



                    'appflowlog': 'DISABLED',

                    'netprofile': 'net-profile-1',

                    'icmpvsrresponse': 'PASSIVE',
                    'rhistate': 'PASSIVE',
                    'newservicerequest': 11,
                    'newservicerequestunit': 'PER_SECOND',
                    'newservicerequestincrementinterval': 5,
                    'minautoscalemembers': 8,
                    'maxautoscalemembers': 10,

                    #'persistavpno': [3,2,1],
                    #"persistavpno": "missing from other"


                    #'td': 10,
                    #"msg": "nitro exception errorcode=946,message=The specified traffic domain is not configured."

                    'authnprofile': 'auth-profile-1',

                    'macmoderetainvlan': 'DISABLED',

                    'dns64': 'DISABLED',
                    'bypassaaaa': '"NO"',


                    'processlocal': 'DISABLED',


                    #"msg": "unsupported parameter for module: redirectfromport"
                    #'redirectfromport': 100,

                    #"msg": "unsupported parameter for module: httpsredirecturl"
                    #'httpsredirecturl': 'http://redir.com',

                    #"msg": "nitro exception errorcode=344,message=No Service"
                    #"msg": "nitro exception errorcode=305,message=Can't assign requested address"
                    #'weight': 50,
                    #'servicename': 'service-http-2',

                    #"msg": "lb vserver lb-vserver-1 is not configured correctly"
                    #"redirurlflags": "missing from other"
                    #'redirurlflags': False,

                    'backuplbmethod': 'LEASTCONNECTION',
                    'hashlength': 100,
                    'servicebindings': [
                        {
                            'servicename': 'service-http-1',
                            'weight': 100
                        },
                    ]
                }
            }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        # First run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_02_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_1',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-2',
                    'ipv46': '10.79.1.2',
                    'port': 80,
                    'servicetype': 'RTSP',
                    'rtspnat': '"ON"',
                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_02_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_02_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_03_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_3',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-3',
                    'ipv46': '10.79.1.3',
                    'port': 80,
                    'servicetype': 'TCP',

                    'lbmethod': 'TOKEN',
                    'datalength': 20,
                    'dataoffset': 5,
                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_03_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_03_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_04_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_4',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-4',
                    'ipv46': '10.79.1.4',
                    'port': 80,
                    'servicetype': 'ANY',
                    'connfailover': 'STATELESS',
                    'skippersistency': 'None',

                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_04_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_04_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_05_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_5',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-5',
                    'ipv46': '10.79.1.5',
                    'port': 80,
                    'servicetype': 'ORACLE',
                    'oracleserverversion': '10G',

                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_05_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_05_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_06_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_6',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-6',
                    'ipv46': '10.79.1.6',
                    'port': 80,
                    'servicetype': 'MSSQL',
                    'mssqlserverversion': '2000',
                    'dbprofilename': 'dbprofile1',

                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_06_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_06_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_07_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_7',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-7',
                    'ipv46': '10.79.1.7',
                    'port': 80,
                    'servicetype': 'MYSQL',

                    'mysqlprotocolversion': '2',
                    'mysqlserverversion': '10',
                    'mysqlcharacterset': 8,
                    'mysqlservercapabilities': 244,

                    'dbslb': 'DISABLED',

                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_07_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_07_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_08_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_8',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-8',
                    'ipv46': '10.79.1.8',
                    'port': 80,
                    'servicetype': 'DNS',

                    'dnsprofilename': 'dns-profile-1',
                    'recursionavailable': '"NO"',


                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_08_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_08_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_09_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_9',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-9',
                    'port': 80,
                    'servicetype': 'HTTP',
                    'ippattern': '10.67.0.0',
                    'ipmask': '255.255.0.0',
                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_09_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_09_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_10_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [{
                'name': 'test_lbvserver_10',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-10',
                    'port': 80,
                    'servicetype': 'HTTP',
                    'lbmethod': 'DESTINATIONIPHASH',
                    'netmask': '255.255.255.0',
                    'ippattern': '10.68.0.0',
                    'ipmask': '255.255.0.0',
                    'v6netmasklen': 24,
                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_10_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_10_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_11_full_initial_values(self):

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = [

                {
                    'name': 'pushvserver',
                    'local_action': {
                        'operation': 'present',
                        'module': 'netscaler_lb_vserver',
                        'name': 'lb-vserver-push',
                        'port': 80,
                        'servicetype': 'PUSH',
                        'ipv46': '193.1.1.1',

                    }
                },
                    {
                'name': 'test_lbvserver_11',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': 'lb-vserver-11',
                    'port': 80,
                    'servicetype': 'HTTP',
                    'lbmethod': 'DESTINATIONIPHASH',
                    'netmask': '255.255.255.0',
                    'ippattern': '10.68.0.0',
                    'ipmask': '255.255.0.0',
                    'v6netmasklen': 24,
                    'pushvserver': 'lb-vserver-push',
                    'pushlabel': 'none',
                }
            }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        playbook[0]['tasks'][1]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][1]['local_action'])

        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_10_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='FullInitialValuesLBVserver_test_10_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

class LBVserverMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/load-balancing_lbvserver.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_lb_vserver
        yaml_data = yaml.load(netscaler_lb_vserver.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'rule',
            'resrule',
            'state',
            'backupvserver',
            'persistavpno',
            'td',
            'lbprofilename',
            'redirectfromport', 
            'httpsredirecturl', 
            'weight',
            'servicename',
            'redirurlflags',
            'newname', 
        ]
        self.assertListEqual(
                sorted(list(json_attributes - doc_attributes)),
                sorted(missing_from_documentation))

class LBVserverDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

    def test_create_and_delete_entity(self):
        vserver_name = 'lb-vserver-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'setup monitor',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': vserver_name,
                    'servicetype': 'HTTP',
                    'ipv46': '192.168.1.1',
                    'port': 80,
                },
            }]
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_lb_vserver_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = lbvserver.count_filtered(utils.get_nitro_client(), 'name:%s' % vserver_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % vserver_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_lb_vserver_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = lbvserver.count_filtered(utils.get_nitro_client(), 'name:%s' % vserver_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % vserver_name)

class LBVserverSSLCertkeyBindings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()
        utils.copy_sslcertificate_to_cpx()
        cls.certkeyname = 'certificate_1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'setup monitor',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_ssl_certkey',

                    'certkey': cls.certkeyname,
                    'cert': 'server.crt',
                    'key': 'server.key',
                },
            }]
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        utils.run_ansible_play(playbook, testcase='Setup_sslcertkey_for_lbvserver')

    def test_certificate(self):
        vserver_name = 'lb-vserver-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'setup monitor',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_vserver',

                    'name': vserver_name,
                    'servicetype': 'SSL',
                    'ipv46': '192.168.1.1',
                    'port': 80,
                    'ssl_certkey': self.certkeyname
                },
            }]
        }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
        client = utils.get_nitro_client()
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_lb_vserver_with_ssl_certificate')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the bindings are ok
        bindings = sslvserver_sslcertkey_binding.get(client, vserver_name)
        self.assertListEqual([ item.certkeyname for item in bindings ], [ self.certkeyname ], msg='ssl cert bindings differ')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Create_lb_vserver_with_ssl_certificate_second_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Make sure the bindings are ok
        bindings = sslvserver_sslcertkey_binding.get(client, vserver_name)
        self.assertListEqual([ item.certkeyname for item in bindings ], [ self.certkeyname ], msg='ssl cert bindings differ')

        # Delete entity
        del playbook[0]['tasks'][0]['local_action']['ssl_certkey']
        result = utils.run_ansible_play(playbook, testcase='Delete_lb_vserver_ssl_cert_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure no bindings exist
        count = sslvserver_sslcertkey_binding.count(client, vserver_name)
        self.assertEqual(count, 0, msg='ssl certkey bindings did not get deleted')

        # Delete second run
        result = utils.run_ansible_play(playbook, testcase='Delete_lb_vserver_ssl_cert_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Make sure no bindings exist
        count = sslvserver_sslcertkey_binding.count(client, vserver_name)
        self.assertEqual(count, 0, msg='ssl certkey bindings did not get deleted')
