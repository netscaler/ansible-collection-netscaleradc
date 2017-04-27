import unittest
import subprocess
import os.path
import os
import functools

from . import utils


def setUpModule():
    pass

def tearDownModule():
    pass


minimal_attrs = {
    'name': 'vserver1',
    'ipaddress': '192.168.1.1',
}

class ServerFullInitalValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_01(self):
        playbook = [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'Setup server',
                'local_action': {
                    'module': 'netscaler_server',
                    'operation': 'present',

                    'name': 'server1',
                    'ipaddress': '192.168.1.1',

                }
            }]
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        result = utils.run_ansible_play(playbook, testcase='server_test_01')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make second run
        result = utils.run_ansible_play(playbook, testcase='server_test_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')
