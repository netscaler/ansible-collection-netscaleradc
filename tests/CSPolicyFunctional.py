import unittest
import copy

from . import utils

class CSPolicyFullInitialValues(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]


    def test_01_full_initial_values_domain(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_policy',
                'operation': 'present',

                'policyname': 'somepolicy',
                #'url': 'http://example.com',
                #'rule': 'rule1',
                'domain': 'example.com',
                #'action': 'lb-vserver-1',
                #'logaction': 'action',
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        # Make run
        result = utils.run_ansible_play(playbook, testcase='cs_policy_initial_values_domain_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='cs_policy_initial_values_domain_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

    def test_02_full_initial_values_rule(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_policy',
                'operation': 'present',

                'policyname': 'somepolicy_rule',
                #'url': 'http://example.com',
                'rule': 'CLIENT.IP.SRC.SUBNET(24).EQ(10.217.84.0)',
                #'domain': 'example.com',
                #'action': 'lb-vserver-1',
                #'logaction': 'action',
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        # Make run
        result = utils.run_ansible_play(playbook, testcase='cs_policy_initial_values_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='cs_policy_initial_values_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

