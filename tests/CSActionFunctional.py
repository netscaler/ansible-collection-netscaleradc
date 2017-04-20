import unittest
import copy
import json
import sys
import pyaml
import yaml

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
            },
        }]

        cls.attributes_to_check  = [
            'name',
            'targetlbvserver',
            'targetvserver',
            'targetvserverexpr',
            'comment',
        ]

        # targetvserver requires sslvpn feature which is unavailable in CPX

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        result = utils.run_ansible_play(playbook, testcase='setup_lb_vserver_for_csaction')


    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        missing = ['targetvserver']
        self.assertListEqual(self.attributes_to_check, missing)


    def test_01_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_action',
                'operation': 'present',

                'name': 'action-1',
                'targetlbvserver': 'lb-vserver-1',
                'comment': 'some comment',

            }
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

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

    def test_02_full_initial_values(self):
        playbook = copy.deepcopy(self.minimal_playbook)
        import json

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_action',
                'operation': 'present',

                'name': 'action-2',
                'targetvserverexpr': '"mylb_" + HTTP.REQ.URL.SUFFIX',

            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

        # Make run
        result = utils.run_ansible_play(playbook, testcase='cs_action_initial_values_02_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make second run
        result = utils.run_ansible_play(playbook, testcase='cs_action_initial_values_02_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')


class CSActionMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/content-switching_csaction.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_cs_action
        yaml_data = yaml.load(netscaler_cs_action.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'newname',
            'targetvserver',
        ]
        self.assertListEqual(list(json_attributes - doc_attributes),missing_from_documentation)

