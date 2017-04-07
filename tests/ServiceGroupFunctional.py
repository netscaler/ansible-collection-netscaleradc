import unittest
from . import utils
import copy







class InitialServiceGroupValues(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.action= {}
        cls.action.update(utils.nitro_dict)
        cls.action.update({
            'operation': 'present',
            'module': 'netscaler_servicegroup',

            'servicegroupname': 'service-group-1',
            'servicetype': 'HTTP',
            'cachetype': 'TRANSPARENT',
            'comment': 'commenting server group',
            'weight': 100,
            #'cip': 'ENABLED',
            #'cipheader': 'cip_header',
            'servername': 'server1',
            'port': 80,
            'servicemembers': [
                {
                    'ip': '10.78.78.78',
                    'port': 80,
                    'weight': 60,
                },
                {
                    'ip': '10.79.79.79',
                    'port': 80,
                    'weight': 40,
                }
            ]
        })

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'test service group',
                    'local_action': cls.action,
                }
            ]
        }]

    def test_01_initial_setup(self):
        utils.run_ansible_play(self.minimal_playbook)

class ServiceGroupMonitorBindings(unittest.TestCase):
    
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
            'name': 'Setup service group',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_servicegroup',
                'servicegroupname': 'service-group-1',
                'servicetype': 'HTTP',
                'servicemembers': [
                    {
                      'ip': '10.78.78.78',
                      'port': 80,
                      'weight': 60,
                    },
                    {
                      'ip': '10.79.79.79',
                      'port': 80,
                      'weight': 40,
                    },
                ],
                'monitorbindings': [
                    {
                        'monitorname': 'monitor-1'
                    },
                ]
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_02_unset_monitorbindings(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service group',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_servicegroup',
                'servicegroupname': 'service-group-1',
                'servicetype': 'HTTP',
                'servicemembers': [
                    {
                      'ip': '10.78.78.78',
                      'port': 80,
                      'weight': 60,
                    },
                    {
                      'ip': '10.79.79.79',
                      'port': 80,
                      'weight': 40,
                    },
                ],
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_03_set_monitorbindings(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service group',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_servicegroup',
                'servicegroupname': 'service-group-1',
                'servicetype': 'HTTP',
                'servicemembers': [
                    {
                      'ip': '10.78.78.78',
                      'port': 80,
                      'weight': 60,
                    },
                    {
                      'ip': '10.79.79.79',
                      'port': 80,
                      'weight': 40,
                    },
                ],
                'monitorbindings': ['monitor-1'],
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_04_unset_monitorbindings(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup service group',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_servicegroup',
                'servicegroupname': 'service-group-1',
                'servicetype': 'HTTP',
                'servicemembers': [
                    {
                      'ip': '10.78.78.78',
                      'port': 80,
                      'weight': 60,
                    },
                    {
                      'ip': '10.79.79.79',
                      'port': 80,
                      'weight': 40,
                    },
                ],
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)


        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_servicegroup_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')
