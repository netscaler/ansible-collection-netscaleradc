import unittest
from . import utils
import copy
import json
import yaml
import sys







class ServiceGrouptFullInitialValues(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        cls.attributes_to_check = [
            'servicegroupname',
            'servicetype',
            'cachetype',
            'td',
            'maxclient',
            'maxreq',
            'cacheable',
            'cip',
            'cipheader',
            'usip',
            'pathmonitor',
            'pathmonitorindv',
            'useproxyport',
            'healthmonitor',
            'sc',
            'sp',
            'rtspsessionidremap',
            'clttimeout',
            'svrtimeout',
            'cka',
            'tcpb',
            'cmp',
            'maxbandwidth',
            'monthreshold',
            'state',
            'downstateflush',
            'tcpprofilename',
            'httpprofilename',
            'comment',
            'appflowlog',
            'netprofile',
            'autoscale',
            'memberport',
            'servername',
            'port',
            'weight',
            'customserverid',
            'serverid',
            'hashid',
            'monitor_name_svc',
            'dup_weight',
            'riseapbrstatsmsgcode',
            'delay',
            'graceful',
            'includemembers'
        ]
        utils.make_tcpprofile('tcp-profile-1')
        utils.make_httpprofile('http-profile-1')
        utils.make_netprofile('netprofile-1')

    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        missing = [
            'td',
            'servername',
            'port',
            'weight',
            'customserverid',
            'serverid',
            'hashid',
            'monitor_name_svc',
            'dup_weight',
            'riseapbrstatsmsgcode',
            'delay',
            'includemembers'
        ]
        self.assertListEqual(self.attributes_to_check,missing)


    def test_01_servicegroup(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_servicegroup',

                'servicegroupname': 'group-1',
                'servicetype': 'HTTP',
                'cachetype': 'TRANSPARENT',
                'maxclient': 100,
                'maxreq': 100,
                'cacheable': '"NO"',
                'cip': 'ENABLED',
                'cipheader': 'cip-header',
                'usip': '"NO"',
                'pathmonitor': '"NO"',
                'pathmonitorindv': '"NO"',
                'useproxyport': '"NO"',
                'healthmonitor': '"NO"',
                'sc': '"OFF"',
                'sp': '"OFF"',
                'rtspsessionidremap': '"OFF"',
                'clttimeout': 2000,
                'svrtimeout': 2000,
                'cka': '"YES"',
                'tcpb': '"YES"',
                'cmp': '"NO"',
                'maxbandwidth': 5000,
                'monthreshold': 100,
                'state': 'ENABLED',
                'downstateflush': 'DISABLED',
                'comment': 'some comment',
                'appflowlog': 'ENABLED',
                'autoscale': 'POLICY',
                'memberport': 80,
                'graceful': '"NO"',
                'tcpprofilename': 'tcp-profile-1',
                'httpprofilename': 'http-profile-1',
                'netprofile': 'netprofile-1',

                # Fails to set value
                #'riseapbrstatsmsgcode': 10,
                #'delay': 1000,
                #'includemembers': True,

                #"msg": "nitro exception errorcode=278,message=Invalid argument [dupweight]"
                #'dup_weight': 100,

                #"msg": "nitro exception errorcode=278,message=Invalid argument [monitornamesvc]"
                #'monitor_name_svc': 'name',

                #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [CustomServerID, serverName]"
                #'weight': 100,
                #'customserverid': 211,
                #'serverid': 200,
                #'hashid': 100,

                #"msg": "nitro exception errorcode=3956,message=Netprofile does not exist"
                #'netprofile': 'someprofile',

                #"msg": "nitro exception errorcode=3248,message=Profile does not exist"
                #'tcpprofilename': 'someprofile',
                #'httpprofilename': 'someprofile',


                #"msg": "nitro exception errorcode=946,message=The specified traffic domain is not configured."
                #'td': 1,

                'servicemembers': [
                    {
                      'ip': '10.78.78.78',
                      'port': 80,
                      'weight': 100,
                    },
                ],
            }
        }]

        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Servicegroup_initial_values_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Servicegroup_initial_values_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

class ServiceGroupMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/basic_servicegroup.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_servicegroup
        yaml_data = yaml.load(netscaler_servicegroup.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'td',
            'servername',
            'port',
            'weight',
            'customserverid',
            'serverid',
            'hashid',
            'monitor_name_svc',
            'dup_weight',
            'riseapbrstatsmsgcode',
            'delay',
            'includemembers',
            'monconnectionclose',
            'newname',
        ]
        self.assertListEqual(
                sorted(list(json_attributes - doc_attributes)),
                sorted(missing_from_documentation))

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
        result = utils.run_ansible_play(playbook, testcase='setup_service_monitor_bindings')
        if result['failed']:
            raise Exception('Could not setup monitor')


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
                'cachetype': 'TRANSPARENT',
                'maxclient': 100,
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
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_bydict_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_bydict_to_servicegroup_second_run')
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
        result = utils.run_ansible_play(playbook, testcase='Unsetting_monitor_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Unsetting_monitor_to_servicegroup_second_run')
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
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_byname_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_byname_to_servicegroup_second_run')
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
        result = utils.run_ansible_play(playbook, testcase='Unsetting_monitor_byname_to_servicegroup')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Unsetting_monitor_byname_to_servicegroup_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

class ServiceGroupDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_create_and_delete_entity(self):
        servicegroup_name = 'servicegroup-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                    'name': 'setup monitor',
                    'local_action': {
                        'operation': 'present',
                        'module': 'netscaler_servicegroup',

                        'servicegroupname': servicegroup_name,
                        'servicetype': 'HTTP',
                        'cachetype': 'TRANSPARENT',
                        'maxclient': 100,
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
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_servicegroup_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = servicegroup.count_filtered(utils.get_nitro_client(), 'name:%s' % servicegroup_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % servicegroup_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_servicegroup_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = servicegroup.count_filtered(utils.get_nitro_client(), 'name:%s' % servicegroup_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % servicegroup_name)
