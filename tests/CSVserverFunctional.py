import unittest
import copy
import json
import yaml
import sys

from . import utils

class CSVserverFullInitialValues(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        playbook = copy.deepcopy(cls.minimal_playbook)
        playbook[0]['tasks'] = [{
            'name': 'Setup push lb vserver',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_lb_vserver',

                'name': 'push_lb_vserver',
                'ipv46': '11.11.11.11',
                'port': 80,
                'servicetype': 'PUSH'

            }
        }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        utils.run_ansible_play(playbook)

        utils.make_tcpprofile('tcp-profile-1')
        utils.make_netprofile('net-profile-1')
        utils.make_httpprofile('http-profile-1')
        utils.make_dnsprofile('dns-profile-1')
        utils.make_dbprofile('db-profile-1')
        utils.make_authnprofile(
            'auth-profile-1', 
            'vs1',
            'vs1.example.com',
            'example.com',
            1,
        )

        cls.attributes_to_check = [
            'name',
            'td', 
            'servicetype',
            'ipv46',
            'targettype',
            'dnsrecordtype',
            'persistenceid',
            'ippattern',
            'ipmask',
            'range',
            'port',
            'state',
            'stateupdate',
            'cacheable',
            'redirecturl',
            'clttimeout',
            'precedence',
            'casesensitive',
            'somethod',
            'sopersistence',
            'sopersistencetimeout',
            'sothreshold',
            'sobackupaction',
            'redirectportrewrite',
            'downstateflush',
            'backupvserver',
            'disableprimaryondown',
            'insertvserveripport',
            'vipheader',
            'rtspnat',
            'authenticationhost',
            'authentication',
            'listenpolicy',
            'listenpriority',
            'authn401',
            'authnvsname',
            'push',
            'pushvserver',
            'pushlabel',
            'pushmulticlients',
            'tcpprofilename',
            'httpprofilename',
            'dbprofilename',
            'oracleserverversion',
            'comment',
            'mssqlserverversion',
            'l2conn',
            'mysqlprotocolversion',
            'mysqlserverversion',
            'mysqlcharacterset',
            'mysqlservercapabilities',
            'appflowlog',
            'netprofile',
            'icmpvsrresponse',
            'rhistate',
            'authnprofile',
            'dnsprofilename',
            'domainname',
            'ttl',
            'backupip',
            'cookiedomain',
            'cookietimeout',
            'sitedomainttl',
        ]

    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        missing = [
            'targettype',
            'persistenceid',
            'state',
            'backupvserver',
            'listenpriority',
            'domainname',
            'ttl',
            'backupip',
            'cookiedomain',
            'cookietimeout',
            'sitedomainttl'
        ]
        self.assertListEqual(self.attributes_to_check, missing)

    def test_01_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-1',
                'servicetype': 'HTTP',
                'ipv46': '192.168.1.1',
                'td': 0,

                'port': 80,
                'dnsrecordtype': 'A',
                'range': 2,
                'stateupdate': 'DISABLED',
                'cacheable': '"NO"',
                'redirecturl': 'http://url.com',
                'clttimeout': 200,
                'precedence': 'RULE',
                'casesensitive': '"ON"',
                'somethod': 'CONNECTION',
                'sopersistence': '"ENABLED"',
                'sopersistencetimeout': 50,
                'sothreshold': 200,
                'sobackupaction': 'DROP',
                'redirectportrewrite': '"DISABLED"',
                'downstateflush': '"DISABLED"',
                'disableprimaryondown': '"DISABLED"',
                'insertvserveripport': '"VIPADDR"',
                'vipheader': 'someheader',
                'rtspnat': '"OFF"',
                'authenticationhost': 'auth.com',
                'authentication': '"ON"',
                'listenpolicy': '"NONE"',
                'authn401': '"OFF"',
                'authnvsname': 'someserver',
                'push': '"DISABLED"',
                'pushvserver': 'push_lb_vserver',
                'pushlabel': 'none',
                'pushmulticlients': '"NO"',
                'comment': 'some comment',
                'l2conn': '"OFF"',
                'appflowlog': 'ENABLED',
                'icmpvsrresponse': 'PASSIVE',
                'rhistate': 'PASSIVE',
                'tcpprofilename': 'tcp-profile-1',
                'netprofile': 'net-profile-1',
                'httpprofilename': 'http-profile-1',
                'authnprofile': 'auth-profile-1',

                #"sitedomainttl": "difference. ours: (<type 'float'>) 100.0 other: (<type 'int'>) 0"
                #'sitedomainttl': 100

                #"cookietimeout": "difference. ours: (<type 'float'>) 100.0 other: (<type 'int'>) 0"
                #'cookietimeout': 100,

                #"cookiedomain": "missing from other"
                #'cookiedomain': 'some.domain',

                #"backupip": "missing from other"
                #'backupip': '192.169.1.1',

                #"ttl": "difference. ours: (<type 'float'>) 200.0 other: (<type 'int'>) 0"
                #'ttl': 200,
                
                #"msg": "nitro exception errorcode=3248,message=Profile does not exist"
                #'authnprofile': 'someprofile',

                #"msg": "nitro exception errorcode=1354,message=Error in binding listen priority to normal vserver"
                #'listenpriority': 50,

                #"msg": "nitro exception errorcode=258,message=No such resource [backupVServer, backup-server]"
                #'backupvserver': 'backup-server',

                #"state": "missing from other"
                #'state': 'ENABLED',

                #"persistenceid": "missing from other", 
                #"targettype": "missing from other"
                #'targettype': 'GSLB',
                #'persistenceid': 256,

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_02_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-2',
                'servicetype': 'HTTP',
                'port': 80,
                'ippattern': '10.78.10.0',
                'ipmask': '255.255.255.0',

                
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_02_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_02_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_03_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-3',
                'servicetype': 'ORACLE',
                'ipv46': '192.168.1.3',
                'port': 80,
                'td': 0,
                'oracleserverversion': '10G',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])
        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_03_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_03_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_04_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-4',
                'servicetype': 'MSSQL',
                'ipv46': '192.168.1.4',
                'port': 80,
                #'td': 0,
                'mssqlserverversion': '2000',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])
        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_04_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_04_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_05_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-5',
                'servicetype': 'MYSQL',
                'ipv46': '192.168.1.5',
                'port': 80,
                #'td': 0,
                'mysqlprotocolversion': 10,
                'mysqlserverversion': 'Version 1',
                'mysqlcharacterset': 8,
                'mysqlservercapabilities': 41613,

                'dbprofilename': 'db-profile-1',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])
        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_05_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_05_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_06_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_vserver',
                'operation': 'present',

                'name': 'cs-vserver-6',
                'servicetype': 'DNS',
                'ipv46': '192.168.1.6',
                'port': 80,
                'dnsprofilename': 'dns-profile-1',

                #"domainname": "missing from other"
                #'domainname': 'some.domain',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])
        # Make run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_06_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='CSVserverFullInitialValues_test_06_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

class CSVserverMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/content-switching_csvserver.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_cs_vserver
        yaml_data = yaml.load(netscaler_cs_vserver.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = ['newname']
        self.assertListEqual(list(json_attributes - doc_attributes),missing_from_documentation)

class CSVserverDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

    def test_create_and_delete_entity(self):
        vserver_name = 'cs-vserver-1'
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

        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
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
