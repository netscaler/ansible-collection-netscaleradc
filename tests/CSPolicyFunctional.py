import unittest
import copy
import json
import yaml
import sys

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

        playbook = copy.deepcopy(cls.minimal_playbook)
        playbook[0]['tasks'] = [{
            'name': 'Setup action',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_cs_action',

                'name': 'action-1',
                'targetvserverexpr': '"mylb_" + HTTP.REQ.URL.SUFFIX',

            }
        }]

        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        utils.run_ansible_play(playbook)

        utils.make_logaction('logaction1', '192.2.2.2')

        cls.attributes_to_check = [
            'policyname',
            'url',
            'rule',
            'domain',
            'action',
            'logaction'
        ]

    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        missing = ['logaction']
        self.assertListEqual(self.attributes_to_check, missing)

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
                #'logaction': 'logaction1',
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

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
                'action': 'action-1',
                #'domain': 'example.com',
                #'action': 'lb-vserver-1',
                #'logaction': 'action',
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

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


    def test_03_full_initial_values_rule(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        playbook[0]['tasks'] = [{
            'name': 'Setup policy',
            'local_action': {
                'module': 'netscaler_cs_policy',
                'operation': 'present',

                'policyname': 'somepolicy',
                'url': '/example.com/basket',
                #"msg": "nitro exception errorcode=278,message=Invalid argument"
                #'logaction': 'logaction1',
            }

        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        self.sub_attributes(playbook[0]['tasks'][0]['local_action'])

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

class CSPolicyMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('utils/source/scrap/content-switching_cspolicy.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_cs_policy
        yaml_data = yaml.load(netscaler_cs_policy.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = ['newname', 'logaction']
        self.assertListEqual(list(json_attributes - doc_attributes),missing_from_documentation)


class CSPolicyDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

    def test_create_and_delete_entity(self):
        policy_name = 'policy-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'setup monitor',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_cs_policy',

                    'policyname': policy_name,
                    'url': '/example.com',
                },
            }]
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_cs_policy_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = cspolicy.count_filtered(utils.get_nitro_client(), 'name:%s' % policy_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % policy_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_cs_policy_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = cspolicy.count_filtered(utils.get_nitro_client(), 'name:%s' % policy_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % policy_name)
