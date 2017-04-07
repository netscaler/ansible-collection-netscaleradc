import unittest
import copy

from . import utils

class CSActionFullInitialValues(unittest.TestCase):
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
            'name': 'setup lb vserver 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_lb_vserver',

                'name': 'lb-vserver-1',
                'ipv46': '10.79.1.1',
                'port': 80,
                'servicetype': 'HTTP',
            }
        }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        result = utils.run_ansible_play(playbook, testcase='setup_lb_vserver_for_csaction')


    def test_01_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_action',
                'operation': 'present',

                'name': 'somename',
                #'targetlbvserver': 'lb-vserver-1',
                #'targetvserver': 'lb-vserver-1',
                'targetvserverexpr': r'\"mylb_\" + HTTP.REQ.URL.SUFFIX',
                'comment': 'some comment',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        # Make run
        result = utils.run_ansible_play(playbook, testcase='cs_action_initial_values_domain_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='cs_action_initial_values_domain_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')
