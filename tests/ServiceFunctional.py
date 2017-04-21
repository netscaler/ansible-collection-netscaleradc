import unittest
import subprocess
import os.path
import os
import functools
import copy
import json
import yaml
import sys

from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from . import utils


def setUpModule():
    pass

def tearDownModule():
    pass


class ServiceFullInitialValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': []
        }]

        cls.attributes_to_check = [
            'name',
            'ip',
            'servername',
            'servicetype',
            'port',
            'cleartextport',
            'cachetype',
            'maxclient',
            'healthmonitor',
            'maxreq',
            'cacheable',
            'cip',
            'cipheader',
            'usip',
            'pathmonitor',
            'pathmonitorindv',
            'useproxyport',
            'sc',
            'sp',
            'rtspsessionidremap',
            'clttimeout',
            'svrtimeout',
            'customserverid',
            'serverid',
            'cka',
            'tcpb',
            'cmp',
            'maxbandwidth',
            'accessdown',
            'monthreshold',
            'state',
            'downstateflush',
            'tcpprofilename',
            'httpprofilename',
            'hashid',
            'comment',
            'appflowlog',
            'netprofile',
            'td',
            'processlocal',
            'dnsprofilename',
            'ipaddress',
            'weight',
            'monitor_name_svc',
            'riseapbrstatsmsgcode',
            'delay',
            'graceful',
            'all',
            'Internal'
        ]
        utils.make_tcpprofile('tcp-profile-1')
        utils.make_httpprofile('http-profile-1')
        utils.make_netprofile('netprofile-1')
        utils.make_dnsprofile('dns-profile-1')
        utils.make_server('server-1', '10.10.10.10')


    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)


    @classmethod
    def tearDownClass(cls):
        #utils.ensure_teardown_cpx('test_crucible')
        pass

    def test_99_no_attribute_unchecked(self):
        missing = [
            'servername',
            'pathmonitor',
            'pathmonitorindv',
            'serverid',
            'state',
            'td',
            'weight',
            'monitor_name_svc',
            'riseapbrstatsmsgcode',
            'delay',
            'all',
            'Internal'
        ]
        self.assertListEqual(self.attributes_to_check,missing)

    def test_01_http_service(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-http',
                'ip': '192.168.1.1',
                'ipaddress': '192.168.1.1',
                'port': 80,
                'servicetype': 'HTTP',
                'cachetype': 'TRANSPARENT',
                'maxclient': 100,
                'healthmonitor': '"NO"',
                'maxreq': 200,
                'cacheable': '"NO"',
                'cip': 'ENABLED',
                'cipheader': 'client-ip',
                'usip': '"YES"',
                'useproxyport': '"YES"',
                'sc': '"OFF"',
                'sp': '"OFF"',
                'rtspsessionidremap': '"OFF"',
                'clttimeout': 100,
                'svrtimeout': 100,
                'customserverid': '476',
                'cka': '"YES"',
                'tcpb': '"YES"',
                'cmp': '"NO"',
                'maxbandwidth': 10000,
                'accessdown': '"NO"',
                'monthreshold': 100,
                'downstateflush': 'ENABLED',
                'hashid': 10,
                'comment': 'some comment',
                'appflowlog': 'ENABLED',
                'processlocal': 'ENABLED',
                'graceful': '"NO"',

                'tcpprofilename': 'tcp-profile-1',
                'httpprofilename': 'http-profile-1',
                'netprofile': 'netprofile-1',

                #"Internal": "missing from other"
                #'Internal': True,

                #"all": "missing from other"
                #'all': True,

                #"delay": "difference. ours: (<type 'float'>) 200.0 other: (<type 'int'>) 0"
                #'delay': 200,

                #"riseapbrstatsmsgcode": "difference. ours: (<type 'int'>) 10 other: (<type 'int'>) 0"
                #'riseapbrstatsmsgcode': 10,

                #"monitor_name_svc": "missing from other"
                #'monitor_name_svc': 'somemonitor',

                #"weight": "missing from other"
                #'weight': 100,

                #"msg": "unsupported parameter for module: monconnectionclose"
                #'monconnectionclose': 'RESET',

                #"msg": "nitro exception errorcode=946,message=The specified traffic domain is not configured."
                #'td': 10,

                # profile must exist net.netprofile
                #'netprofile': 'someprofile',

                # profile must exist ns.nstcpprofile  ns.nshttpprofile
                #'tcpprofilename': 'someprofile',
                #'httpprofilename': 'somehttpprofile',

                #'state': 'ENABLED',
                #"state": "missing from other"

                # the value of this is actually returned in customserverid
                #'serverid': 476,

                #"msg": "nitro exception errorcode=2008,message=The option is only supported for clustering systems."
                #'pathmonitor': '"YES"',
                #'pathmonitorindv': '"YES"',
            }

        }]
        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_02_service_ssl(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-ssl',
                'ipaddress': '192.168.1.2',
                'port': 80,
                'servicetype': 'SSL',
                'cleartextport': 88,
            }

        }]
        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_01_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_03_service_adns(self):
        playbook = copy.deepcopy(self.minimal_playbook)

        tasks = [{
            'name': 'setup service attributes 1',
            'local_action': {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': 'service-adns',
                'ipaddress': '192.168.1.3',
                'port': 80,
                'servicetype': 'ADNS',

                'dnsprofilename': 'dns-profile-1',
            }

        }]
        tasks[0]['local_action'].update(utils.nitro_dict)

        self.sub_attributes(tasks[0]['local_action'])

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'] = tasks

        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_03_first_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Service_initial_values_03_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')


class ServiceMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/basic_service.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_service
        yaml_data = yaml.load(netscaler_service.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'newname', 
            'monconnectionclose',
        ]
        self.assertListEqual(list(json_attributes - doc_attributes),missing_from_documentation)


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
            {
                'name': 'Setup monitor 2',
                'local_action': {
                    'operation': 'present',
                    'module': 'netscaler_lb_monitor',
                    'monitorname': 'monitor-2',
                    'type': 'PING',
                }
            },
        ]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        playbook[0]['tasks'][1]['local_action'].update(utils.nitro_dict)
        utils.run_ansible_play(playbook, testcase='setup_service_monitor_bindings')

    def test_01_set_single_monitorbinding(self):
        playbook = copy.deepcopy(self.minimal_playbook)
        service_name = 'service-1'
        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': service_name,
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

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonbindings_service_binding import lbmonbindings_service_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        client = utils.get_nitro_client()

        # Check monitor bindings are initially null
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, [])

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

        # Check we have the required bindings
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['monitor-1'])

        # Unset monitor bindings

        del playbook[0]['tasks'][0]['local_action']['monitorbindings']

        # Make delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Check monitor bindings deleted
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['tcp-default'])

    def test_02_set_singlemonitorbinding_name_only(self):
        playbook = copy.deepcopy(self.minimal_playbook)
        service_name = 'service-2'

        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': service_name,
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.2',
                'port': 80,
                'monitorbindings': [ 'monitor-1']
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        client = utils.get_nitro_client()

        # Check monitor bindings are initially null
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, [])


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

        # Check we have the required bindings
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['monitor-1'])

        # Unset monitor bindings

        del playbook[0]['tasks'][0]['local_action']['monitorbindings']

        # Make delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Check monitor bindings deleted
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['tcp-default'])

    def test_03_set_multiple_monitorbinding(self):
        playbook = copy.deepcopy(self.minimal_playbook)
        service_name = 'service-3'
        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': service_name,
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.3',
                'port': 80,
                'monitorbindings': [
                    {
                        'monitorname': 'monitor-1'
                    },
                    {
                        'monitorname': 'monitor-2'
                    },
                ]
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonbindings_service_binding import lbmonbindings_service_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        client = utils.get_nitro_client()

        # Check monitor bindings are initially null
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, [])

        # Make run
        result = utils.run_ansible_play(playbook, testcase='Adding_multiple_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second run
        result = utils.run_ansible_play(playbook, testcase='Adding_multiple_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Check we have the required bindings
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['monitor-1', 'monitor-2'])

        # Unset monitor bindings

        del playbook[0]['tasks'][0]['local_action']['monitorbindings']

        # Make delete run
        result = utils.run_ansible_play(playbook, testcase='Deleting_multiple_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second delete run
        result = utils.run_ansible_play(playbook, testcase='Deleting_multiple_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Check monitor bindings deleted
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['tcp-default'])

    def test_04_set_multiple_monitorbinding(self):
        playbook = copy.deepcopy(self.minimal_playbook)
        service_name = 'service-4'
        playbook[0]['tasks'] = [{
            'name': 'Setup service',
            'local_action':
            {
                'operation': 'present',
                'module': 'netscaler_service',
                'name': service_name,
                'servicetype': 'HTTP',
                'ipaddress': '192.168.1.4',
                'port': 80,
                'monitorbindings': [
                    'monitor-1',
                    'monitor-2',
                ]
            },
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonbindings_service_binding import lbmonbindings_service_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        client = utils.get_nitro_client()

        # Check monitor bindings are initially null
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, [])

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

        # Check we have the required bindings
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['monitor-1', 'monitor-2'])

        # Unset monitor bindings

        del playbook[0]['tasks'][0]['local_action']['monitorbindings']

        # Make delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


        # Make second delete run
        result = utils.run_ansible_play(playbook, testcase='Adding_monitor_to_service_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')

        # Check monitor bindings deleted
        bindings = utils.get_service_monitor_bindings_list(client, service_name)
        self.assertListEqual(bindings, ['tcp-default'])

class ServiceDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_create_and_delete_entity(self):
        service_name = 'service-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                    'name': 'setup monitor',
                    'local_action': {
                        'operation': 'present',
                        'module': 'netscaler_service',
                        'name': service_name,
                        'ipaddress': '192.168.1.1',
                        'servicetype': 'HTTP',
                        'port': 80
                    
                    },
            }]
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_service_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = service.count_filtered(utils.get_nitro_client(), 'name:%s' % service_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % service_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_service_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = service.count_filtered(utils.get_nitro_client(), 'name:%s' % service_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % service_name)
