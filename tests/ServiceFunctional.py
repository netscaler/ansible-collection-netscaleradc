import unittest
import subprocess
import os.path
import os
import functools
import copy

from . import utils


def setUpModule():
    pass

def tearDownModule():
    pass








class InitialServiceValuesSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.action= {}
        cls.action.update(utils.nitro_dict)
        cls.action.update({
            'module': 'netscaler_service',
            'name': 'vserver1',
            'ipaddress': '192.168.1.1',
            'port': 80,
            'servicetype': 'HTTP',
        })
        cls.action['operation'] = 'present'

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'test vserver 1',
                    'local_action': cls.action,
                }
            ]
        }]

    @classmethod
    def tearDownClass(cls):
        #utils.ensure_teardown_cpx('test_crucible')
        pass

    def test_001_initial_setup(self):

        result = utils.run_ansible_play(self.minimal_playbook)
        self.assertIsNotNone(result)
        self.assertFalse(result['failed'])
        self.assertTrue(result['changed'])

    def test_002_more_attributes(self):
        action = copy.deepcopy(self.action)
        # Add some more attributes
        action.update({
            'clttimeout': 100,
            'comment': 'This is comment',
            'appflowlog': 'DISABLED',
            'hashid': 10,
            'Internal': True,
            'state': 'ENABLED',
        })
        #print('action is %s' % action)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook)
        self.assertIsNotNone(result)
        self.assertFalse(result['failed'])
        self.assertTrue(result['changed'])

class ServiceMonitorBindings(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        # Create service action
        playbook = copy.deepcopy(cls.minimal_playbook)
        playbook[0]['tasks'] = [
            {
                'name': 'Setup monitor 1',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_monitor',
                    'monitorname': 'monitor-1',
                    'type': 'HTTP',
                    'trofscode': 500,
                }
            },
        ]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        utils.run_ansible_play(playbook, testcase='setup_service_monitor_bindings')


    def test_01_set_monitorbindings(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-1',
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.1',
                'port': 80,
                'monitorbindings': [
                    {
                        'monitorname': 'monitor-1'
                    },
                ]
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_02_unset_monitorbindings(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-1',
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.1',
                'port': 80,
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Removing_monitor_from_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Removing_monitor_from_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_03_set_monitorbindings_name_only(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-1',
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.1',
                'port': 80,
                'monitorbindings': [ 'monitor-1']
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_by_name_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_by_name_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

