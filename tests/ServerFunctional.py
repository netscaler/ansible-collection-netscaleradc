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

class InitialServerValuesSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    @classmethod
    def tearDownClass(cls):
        #utils.ensure_teardown_cpx('test_crucible')
        pass

    def test_setup_00(self):
        action= {}
        action.update(utils.nitro_dict)
        action.update({
            'name': 'vserver1',
            'ipaddress': '192.168.1.1',
        })
        action['operation'] = 'present'

        minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'test vserver 1',
                    'local_action': action,
                }
            ]
        }]


        result = utils.run_ansible_play(minimal_playbook)
        self.assertIsNotNone(result)
        self.assertFalse(result['failed'])
        self.assertTrue(result['changed'])

    def test_setup_01(self):
        action= {}
        action.update(utils.nitro_dict)
        action.update({
            'name': 'vserver1',
            'ipaddress': '192.168.1.1',
        })
        action['operation'] = 'present'

        minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'test vserver 1',
                    'local_action': action,
                }
            ]
        }]


        result = utils.run_ansible_play(minimal_playbook)
        self.assertIsNotNone(result)
        self.assertFalse(result['failed'])
        self.assertFalse(result['changed'])

    def test_setup_02(self):
        action= {}
        action.update(utils.nitro_dict)
        action.update({
            'name': 'vserver1',
            'ipaddress': '192.168.1.2',
        })
        action['operation'] = 'present'

        minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'test vserver 1',
                    'local_action': action,
                }
            ]
        }]


        result = utils.run_ansible_play(minimal_playbook)
        self.assertIsNotNone(result)
        self.assertFalse(result['failed'])
        self.assertTrue(result['changed'])
