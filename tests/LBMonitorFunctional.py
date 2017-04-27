import unittest
import copy
import json
import sys
import yaml

from . import utils

class LBMonitorFullInitialValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'service-1',
                    'local_action': {},
                },
            ]
        }]
        cls.attributes_to_check = [
            'monitorname', 
            'type', 
            'action', 
            'respcode', 
            'httprequest', 
            'rtsprequest', 
            'customheaders', 
            'maxforwards', 
            'sipmethod', 
            'sipuri', 
            'sipreguri', 
            'send', 
            'recv', 
            'query', 
            'querytype', 
            'scriptname', 
            'scriptargs', 
            'dispatcherip', 
            'dispatcherport', 
            'username', 
            'password', 
            'secondarypassword', 
            'logonpointname', 
            'lasversion', 
            'radkey', 
            'radnasid', 
            'radnasip', 
            'radaccounttype', 
            'radframedip', 
            'radapn', 
            'radmsisdn', 
            'radaccountsession', 
            'lrtm', 
            'deviation', 
            'units1', 
            'interval', 
            'units3', 
            'resptimeout', 
            'units4', 
            'resptimeoutthresh', 
            'retries', 
            'failureretries', 
            'alertretries', 
            'successretries', 
            'downtime', 
            'units2', 
            'destip', 
            'destport', 
            'state', 
            'reverse', 
            'transparent', 
            'iptunnel', 
            'tos', 
            'tosid', 
            'secure', 
            'validatecred', 
            'domain', 
            'ipaddress', 
            'group', 
            'filename', 
            'basedn', 
            'binddn', 
            'filter', 
            'attribute', 
            'database', 
            'oraclesid', 
            'sqlquery', 
            'evalrule', 
            'mssqlprotocolversion', 
            'Snmpoid', 
            'snmpcommunity', 
            'snmpthreshold', 
            'snmpversion', 
            'metrictable', 
            'application', 
            'sitepath', 
            'storename', 
            'storefrontacctservice', 
            'hostname', 
            'netprofile', 
            'originhost', 
            'originrealm', 
            'hostipaddress', 
            'vendorid', 
            'productname', 
            'firmwarerevision', 
            'authapplicationid', 
            'acctapplicationid', 
            'inbandsecurityid', 
            'supportedvendorids', 
            'vendorspecificvendorid', 
            'vendorspecificauthapplicationids', 
            'vendorspecificacctapplicationids', 
            'kcdaccount', 
            'storedb', 
            'storefrontcheckbackendservices', 
            'trofscode', 
            'trofsstring', 
            'sslprofile', 
            'metric', 
            'metricthreshold', 
            'metricweight', 
            'servicename', 
            'servicegroupname'
        ]

        utils.make_dbuser('dbuser1', 'password1')
        utils.make_metrictable('metrictable1')
        utils.make_netprofile('netprofile-1')

    def sub_attributes(self, attribute_list):
        for attribute in attribute_list:
            #print('examining %s' % attribute)
            if attribute in self.attributes_to_check:
                #print('removing %s' % attribute)
                self.attributes_to_check.remove(attribute)

    def test_99_no_attribute_unchecked(self):
        missing = [
            'metrictable',
            'hostname',
            'kcdaccount',
            'sslprofile',
            'metric',
            'metricthreshold',
            'metricweight',
            'servicename',
            'servicegroupname'
        ]
        self.assertListEqual(self.attributes_to_check,missing)

    def test_01_full_initial_values(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-1',
            'type': 'HTTP-INLINE',
            'action': 'DOWN',
            'respcode': [ '"200"', '"203"'],
            'httprequest': 'HEAD /file.html',


            'customheaders': 'HEADER_CUSTOM: NONE\r\n',

        }
        self.sub_attributes(action.keys())

        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup http monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_02_full_initial_values_sip(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-2',
            'type': 'SIP-UDP',
            #'action': 'DOWN',
            #'respcode': [ '"200"', '"203"'],
            #'httprequest': 'HEAD /file.html',

            #'rtsprequest': 'OPTIONS',
            #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [rtspRequest, type==RTSP]"

            'customheaders': 'HEADER_CUSTOM: NONE\r\n',

            'maxforwards': 5,
            'sipmethod': 'REGISTER',
            'sipuri': 'sip:sip.test',
            'sipreguri': 'sip:sip.register',

            'lrtm': 'DISABLED',


        }
        self.sub_attributes(action.keys())

        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup sip monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_sip_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_sip_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_03_full_initial_values_rtsp(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-rtsp',
            'type': 'RTSP',

            'rtsprequest': 'OPTIONS',

            'deviation': 100,
            'units1': 'MSEC',
            'interval': 5,
            'units3': 'SEC',
            'resptimeout': 10,
            'units4': 'MSEC',
            'resptimeoutthresh': 10,
            'retries': 5,
            'failureretries': 3,
            'alertretries': 2,
            'successretries': 4,
            'downtime': 60,
            'units2': 'MSEC',
            'destip': '10.10.10.10',
            'destport': '1111',
            'state': 'ENABLED',
            'reverse': '"YES"',
            'transparent': '"YES"',
            'iptunnel': '"NO"',
            'tos': '"YES"',
            'tosid': 20,
            'secure': '"NO"',

        }

        self.sub_attributes(action.keys())

        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup rtsp monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_rtsp_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_rtsp_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_04_full_initial_values_tcp_ecv(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-tcp-ecv',
            'type': 'TCP-ECV',

            'send': 'sendstring',
            'recv': 'recvstring',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup tcp-ecv monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_tcp_ecv_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_tcp_ecv_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_05_full_initial_values_dns_tcp(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-dns-tcp',
            'type': 'DNS-TCP',

            'query': 'example.com',
            'querytype': 'Address',
            'ipaddress': ['192.168.1.1', '192.168.1.2']


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup tcp-ecv monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_dns_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_dns_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_06_full_initial_values_user(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-user',
            'type': 'USER',

            'scriptname': 'myscript.sh',
            'scriptargs': 'argument1 argument2',
            'dispatcherip': '10.10.10.10',
            'dispatcherport': 22,


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup user monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_user_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_user_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_07_full_initial_values_citrix_ag(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-citrix-ag',
            'type': 'CITRIX-AG',


            'username': 'user1',
            'password': 'password1',
            'secondarypassword': 'password2',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix ag monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_ag_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_ag_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_08_full_initial_values_citrix_aac_las(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-citrix-aac',
            'type': 'CITRIX-AAC-LAS',

            'lasversion': '7.1',
            'logonpointname': 'user',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix aac las monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_aac_las_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_aac_las_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_09_full_initial_values_citrix_radius(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-radius',
            'type': 'RADIUS',

            'username': 'someuser',
            'password': 'somepass',
            'radkey': 'somekey',
            'radnasid': 'someid',
            'radnasip': '192.168.1.1',
        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix radius monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_radius_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_radius_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_10_full_initial_values_citrix_radius_accounting(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-radius-accounting',
            'type': 'RADIUS_ACCOUNTING',

            'username': 'someuser',
            'password': 'somepass',
            'radkey': 'somekey',

            'radaccounttype': 10,
            'radframedip': '192.168.1.1',
            'radapn': 'someapn',
            'radmsisdn': 'someisdn',
            'radaccountsession': 'sessionid',
        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix radius accounting monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_radius_accounting_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_radius_accounting_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_11_full_initial_values_citrix_xd_ddc(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-citrix-xd-ddc',
            'type': 'CITRIX-XD-DDC',

            'validatecred': '"NO"',
            'domain': 'somedomain.com',
        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix radius accounting monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_xd_ddc_accounting_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_xd_ddc_accounting_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_12_full_initial_values_nntp(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-nntp',
            'type': 'NNTP',

            'group': 'somegroup.nntp',
        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix nntp monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_nntp_accounting_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_nntp_accounting_lb_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_13_full_initial_values_ftp(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-ftp',
            'type': 'FTP-EXTENDED',
            'filename': 'somefile.txt',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix nntp monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_ftp_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_ftp_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_14_full_initial_values_ldap(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-ldap',
            'type': 'LDAP',

            'basedn': 'example.com',
            'binddn': 'example.com',
            'filter': 'somefilter',
            'attribute': 'cn',
        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix ldap monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_ldap_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_ldap_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_15_full_initial_values_snmp(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-oracle',
            'type': 'SNMP',

            'Snmpoid': 'some.id',
            'snmpcommunity': 'some.community',
            'snmpthreshold': 'threshold',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup snmp monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_snmp_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_snmp_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_16_full_initial_values_load(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-load',
            'type': 'LOAD',

            'snmpversion': 'V1',

            #'metric': 'iso',
            #'metricthreshold': 5,

            #'metrictable': 'metrictable1',
            # "msg": "nitro exception errorcode=2174,message=Metric table does not exist"

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup load monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_load_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_load_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_17_full_initial_values_citrix_xml_service(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-citrix-xml-service',
            'type': 'CITRIX-XML-SERVICE',

            'application': 'app',

            # 'metrictable': 'table',
            # "msg": "nitro exception errorcode=2174,message=Metric table does not exist"

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix xml service monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_xml_service_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_xml_service_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_18_full_initial_values_citrix_web_interface(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-citrix-web-interface',
            'type': 'CITRIX-WEB-INTERFACE',
            
            'sitepath': 'hello/',


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup citrix site path monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_citrix_web_interface_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_citrix_web_interface_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_19_full_initial_values_storefront(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-storefront',
            'type': 'STOREFRONT',
            
            'storename': 'store',
            'storefrontacctservice': '"YES"',
            'storefrontcheckbackendservices': '"YES"',

            #'hostname': 'example.com',
            #"msg": "Monitor is not configured according to parameters given"


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup storefront monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_storefront_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_storefront_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_20_full_initial_values_diameter(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-diameter',
            'type': 'DIAMETER',

            'netprofile': 'netprofile-1',
            # "msg": "nitro exception errorcode=3956,message=Netprofile does not exist"
            'originhost': 'origin.host',
            'originrealm': 'some.realm',
            'hostipaddress': '192.168.1.1',
            'vendorid': 20,
            'productname': 'someproduct',
            'firmwarerevision': 10,
            'authapplicationid': ['"100"', '"200"'],
            'inbandsecurityid': 'NO_INBAND_SECURITY',
            'supportedvendorids': ['"10"','"20"'],
            'vendorspecificvendorid': 10,
            'vendorspecificauthapplicationids': ['"11"', '"22"'],
            'vendorspecificacctapplicationids': ['"12"', '"23"'],
            'acctapplicationid': ['"1"','"2"'],
            


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup diameter monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_diameter_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_diameter_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_21_full_initial_values_http(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-http',
            'type': 'HTTP',

            
            'trofscode': 500,


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup http monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_http_lb_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_http_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_22_full_initial_values_http_ecv(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-http-ecv',
            'type': 'HTTP-ECV',

            
            'trofsstring': 'somestring',
            #'servicename': 'service-1',
            #'sslprofile': 'someprofile',
            #"msg": "unsupported parameter for module: sslprofile"


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup http ecv monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')


    def test_23_full_initial_values_mssql(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-mssql-ecv',
            'type': 'MSSQL-ECV',

            'username': 'dbuser1',
            'evalrule': "True",
            'database': 'somedb',
            'sqlquery': 'select * from table',
            'mssqlprotocolversion': '2000',
            'storedb': 'ENABLED',

        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup http ecv monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def test_24_full_initial_values_oracle(self):
        action = {
            'operation': 'present',
            'module': 'netscaler_lb_monitor',

            'monitorname': 'lb-monitor-oracle-ecv',
            'type': 'ORACLE-ECV',

            'username': 'dbuser1',
            'oraclesid': 'idstring',
            'evalrule': 'True',
            


        }
        self.sub_attributes(action.keys())
        action.update(utils.nitro_dict)

        playbook = copy.deepcopy(self.minimal_playbook)
        playbook[0]['tasks'][0]['name'] = 'setup http ecv monitor'
        playbook[0]['tasks'][0]['local_action'] = action

        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(playbook, testcase='Full_http_ecv_monitor_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

class LBMonitorMissingArguments(unittest.TestCase):

    def test_arguments(self):
        with open('source/scrap/load-balancing_lbmonitor.json', 'r') as fh:
            json_data = json.load(fh)

        sys.path.append('./ansible-modules')
        import netscaler_lb_monitor
        yaml_data = yaml.load(netscaler_lb_monitor.DOCUMENTATION)

        json_attributes = set([ item['name'] for item in json_data if item['readonly'] == False])
        doc_attributes = set( yaml_data['options'].keys())
        missing_from_documentation = [
            'metric',
            'metrictable',
            'metricthreshold',
            'metricweight',
            'hostname',
            'kcdaccount',
            'sslprofile',
            'servicename',
            'servicegroupname',
        ]
        self.assertListEqual(
                sorted(list(json_attributes - doc_attributes)),
                sorted(missing_from_documentation))


class LBMonitorDeleteEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_create_and_delete_entity(self):
        monitor_name = 'lb-monitor-1'
        playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                    'name': 'setup monitor',
                    'local_action': {
                        'operation': 'present',
                        'module': 'netscaler_lb_monitor',

                        'monitorname': monitor_name,
                        'type': 'HTTP-INLINE',
                        'action': 'DOWN',
                        #'respcode': [ '"200"', '"203"'],
                        #'httprequest': 'HEAD /file.html',
                    
                    },
            }]
        }]

        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        # Create entity
        result = utils.run_ansible_play(playbook, testcase='Create_lb_monitor_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry exists only once
        count = lbmonitor.count_filtered(utils.get_nitro_client(), 'monitorname:%s' % monitor_name)
        self.assertEqual(count,1, msg='%s was not deleted properly' % monitor_name)

        # Delete entity
        playbook[0]['tasks'][0]['local_action']['operation'] = 'absent'
        result = utils.run_ansible_play(playbook, testcase='Delete_lb_monitor_entity')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make sure the named entiry does not exist
        count = lbmonitor.count_filtered(utils.get_nitro_client(), 'monitorname:%s' % monitor_name)
        self.assertEqual(count,0, msg='%s was not deleted properly' % monitor_name)

class LBMonitorServiceBindings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()
