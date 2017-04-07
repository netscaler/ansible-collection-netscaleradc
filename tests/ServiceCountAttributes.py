import unittest

from . import utils


class ServiceCountAttributes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()
        cls.action = {
            'operation': 'present',
            'module': 'netscaler_service',

            'name': 'service-1',
            'ipaddress': '192.168.1.1',
            'servicetype': 'SSL',
            'port': 80,
            'cleartextport': 88,
            
        }
        cls.action.update(utils.nitro_dict)
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

    def test_initial_setup(self):

        result = utils.run_ansible_play(self.minimal_playbook)
        self.assertListEqual(result['configured_service']['missing_rw_attributes'], [])
