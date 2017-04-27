import unittest
import subprocess
import os.path
import os
import functools
import copy
import json
import yaml
import sys

from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from . import utils


def setUpModule():
    pass

def tearDownModule():
    pass


class SSLCertkeyFullInitialValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()
        utils.copy_sslcertificate_to_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        cls.attributes_to_check = [
            'certkey',
            'cert',
            'key',
            'password',
            'fipskey',
            'hsmkey',
            'inform',
            'passplain',
            'expirymonitor',
            'notificationperiod',
            'bundle',
            'linkcertkeyname',
            'nodomaincheck'
        ]


    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)


    @classmethod
    def tearDownClass(cls):
        #utils.ensure_teardown_cpx('test_crucible')
        pass

    def test_99_no_attribute_unchecked(self):
        missing = [
            'fipskey', 
            'hsmkey', 
            'bundle', 
            'linkcertkeyname', 
            'nodomaincheck'
        ]
        self.assertListEqual(self.attributes_to_check,missing)

    def test_01_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_ssl_certkey',
                
                'certkey': 'certirificate_1',
                'cert': 'server.crt',
                'key': 'server.key',
                'expirymonitor': 'ENABLED',
                'notificationperiod': 30,
                'inform': 'PEM',

                # missing from other
                #'nodomaincheck': False,

                # missing from other
                #'bundle': '"NO"',

                # missing from other
                #'linkcertkeyname': 'google.com',
                'password': False,
                'passplain': 'somesecret',
            }
        }]
        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Sslcertkey_initial_values_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Sslcertkey_initial_values_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_02_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_ssl_certkey',
                
                'certkey': 'certirificate_2',
                'cert': 'server2.crt',
                #"msg": "nitro exception errorcode=1670,message=No such HSM key."
                #'hsmkey': 'somekey',
                #"msg": "nitro exception errorcode=1576,message=Operation not permitted - no FIPS card present in the system"
                #'fipskey': 'somekey',
            }
        }]
        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Sslcertkey_initial_values_02_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Sslcertkey_initial_values_02_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

class ServiceMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('utils/source/scrap/basic_service.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_service
        yaml_data = yaml.load(netscaler_service.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'newname', 
            'monconnectionclose',
        ]
        self.assertListEqual(list(json_attributes - doc_attributes),missing_from_documentation)


class SSLCertkeyDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_create_and_delete_entity(self):
        service_name = 'service-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                    'name': 'setup monitor',
                    'local_action': {
                        'operation': 'present',
                        'module': 'netscaler_service',
                        'name': service_name,
                        'ipaddress': '192.168.1.1',
                        'servicetype': 'HTTP',
                        'port': 80
                    
                    },
            }]
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_service_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = service.count_filtered(utils.get_nitro_client(), 'name:%s' % service_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % service_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_service_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = service.count_filtered(utils.get_nitro_client(), 'name:%s' % service_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % service_name)
