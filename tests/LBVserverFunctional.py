import unittest
import copy

from . import utils





class FullInitialValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()

        # Create service
        service_action = {
            'operation': 'present',
            'module': 'netscaler_service',
            'name': 'service-http-1',
            'ipaddress': '192.168.1.1',
            'servicetype': 'HTTP',
            'port': 80,
        }
        service_action.update(utils.nitro_dict)

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'service-1',
                    'local_action': service_action,
                },
            ]
        }]


        result = utils.run_ansible_play(cls.minimal_playbook, testcase='Setup_service-1')

        cls.action= {
            'operation': 'present',
            'module': 'netscaler_lb_vserver',

            'name': 'lb-vserver-1',
            'ipv46': '10.79.1.1',
            'port': 80,
            'servicetype': 'HTTP',
            'persistencetype': 'COOKIEINSERT',
            'timeout': 100,
            'persistencebackup': 'SOURCEIP',
            'backuppersistencetimeout': 110,
            'lbmethod': 'URLHASH',
            'cookiename': 'COOKIE',
            #'rule': 'nothing',
            'listenpolicy': 'CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24)',
            'listenpriority': 66,

            # 'resrule': 'someexpression',
            # "msg": "lb vserver lb-vserver-1 is not configured correctly"

            'persistmask': '255.255.0.0',
            'v6persistmasklen': 64,
            'pq': '"ON"',
            'sc': '"ON"',

            #'rtspnat': '"ON"',
            # "msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [rtspNat, serviceType==RTSP]"

            'm': 'IP',
            'tosid': 6,

            #'datalength': 20,
            #'dataoffset': 5,
            # "msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [dataLength, lbMethod==TOKEN]"
            'sessionless': 'DISABLED',

            #'state': 'DISABLED',
            #"msg": "lb vserver lb-vserver-1 is not configured correctly"

            #'connfailover': 'STATELESS',
            #"msg": "nitro exception errorcode=1290,message=Connection failover can only be enabled on a virtual server of service type ANY"

            'redirurl': 'http://somewhere.com',
            'cacheable': '"NO"',
            'clttimeout': 111,
            'somethod': 'CONNECTION',
            'sopersistence': 'DISABLED',
            'sopersistencetimeout': 222,
            'sothreshold': 4096,
            'healththreshold': 55,

            'sobackupaction': 'DROP',
            'redirectportrewrite': 'DISABLED',
            'downstateflush': 'DISABLED',
            'disableprimaryondown': 'DISABLED',
            'insertvserveripport': 'VIPADDR',
            'vipheader': 'vip',
            'authenticationhost': 'authenticate.me',
            'authentication': '"OFF"',
            'authn401': '"OFF"',
            'authnvsname': 'somename',
            'push': 'DISABLED',

            #'pushvserver': 'somepushserver',
            #"msg": "nitro exception errorcode=258,message=No such resource [pushVserver, somepushserver]"

            #'pushlabel': 'somelabel',
            #"msg": "nitro exception errorcode=3081,message=Expression syntax error [^somelabel, Offset 0]"

            'pushmulticlients': '"NO"',

            #'tcpprofilename': 'someprofile',
            #"msg": "nitro exception errorcode=3248,message=Profile does not exist"

            #'httpprofilename': 'someprofile',
            #"msg": "nitro exception errorcode=3248,message=Profile does not exist"

            #'dbprofilename': 'someprofile',
            #"msg": "nitro exception errorcode=1092,message=Arguments cannot both be specified [dbProfileName, serviceType==HTTP]"

            'comment': 'Vserver comment',
            'l2conn': '"OFF"',

            #'oracleserverversion': '10G',
            #"msg": "lb vserver lb-vserver-1 is not configured correctly"
            #"oracleserverversion": "missing from other"

            #'mssqlserverversion': '2000',
            #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [mssqlServerVersion, serviceType==MSSQL]"

            #'mysqlprotocolversion': '2',
            #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [mysqlProtocolVersion, serviceType==MYSQL]"

            #'mysqlserverversion': 'version',
            #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [mysqlServerVersion, serviceType==MYSQL]"

            #'mysqlcharacterset'
            #'mysqlservercapabilities'
            #"msg": "nitro exception errorcode=1093,message=Argument pre-requisite missing [mysqlServerVersion, serviceType==MYSQL]"

            'appflowlog': 'DISABLED',

            #'netprofile': 'someprofile',
            #"msg": "nitro exception errorcode=3956,message=Netprofile does not exist"

            'icmpvsrresponse': 'PASSIVE',
            'rhistate': 'PASSIVE',
            'newservicerequest': 11,
            'newservicerequestunit': 'PER_SECOND',
            'newservicerequestincrementinterval': 5,
            'minautoscalemembers': 8,
            'maxautoscalemembers': 10,

            #'persistavpno': [3,2,1],
            #"msg": "lb vserver lb-vserver-1 is not configured correctly"
            #"persistavpno": "missing from other"

            #'skippersistency': 'Bypass',
            #"msg": "nitro exception errorcode=1401,message=Skip persistency is supported only for ANY and UDP service types"

            #'td': 10,
            #"msg": "nitro exception errorcode=946,message=The specified traffic domain is not configured."

            #'authnprofile': 'someprofile',
            #"msg": "nitro exception errorcode=2744,message=Profile does not exist or does not have Host configured"

            'macmoderetainvlan': 'DISABLED',

            #'dbslb': 'DISABLED',
            #"msg": "nitro exception errorcode=1092,message=Arguments cannot both be specified [dbsLb, serviceType==HTTP]"

            'dns64': 'DISABLED',
            'bypassaaaa': '"NO"',

            #'recursionavailable': '"NO"',
            #"msg": "nitro exception errorcode=1092,message=Arguments cannot both be specified [RecursionAvailable, serviceType==HTTP]"

            'processlocal': 'DISABLED',

            #'dnsprofilename': 'someprofile',
            #"msg": "nitro exception errorcode=2043,message=DNS profile cannot be set to this service type"


            #'redirectfromport': 100,
            #"msg": "nitro exception errorcode=2043,message=DNS profile cannot be set to this service type"

            #'httpsredirecturl': 'http://redir.com',
            #"msg": "unsupported parameter for module: httpsredirecturl"

            #'weight': 50,
            #'servicename': '10.2.2.2',
            #"msg": "nitro exception errorcode=344,message=No Service"

            #'redirurlflags': False,
            #"msg": "lb vserver lb-vserver-1 is not configured correctly"
            #"redirurlflags": "missing from other"

            #'newname': 'hello',
            #"msg": "unsupported parameter for module: newname"

            'backuplbmethod': 'LEASTCONNECTION',
            'hashlength': 100,
            'servicebindings': [
                {
                    'servicename': 'service-http-1',
                    'weight': 100
                },
            ]


        }
        cls.action.update(utils.nitro_dict)


    def test_01_initial_values_set(self):


        minimal_playbook = copy.deepcopy(self.minimal_playbook)
        minimal_playbook[0]['tasks'] = [
            {
                'name': 'test vserver 1',
                'local_action': self.action,
            }
        ]

        result = utils.run_ansible_play(minimal_playbook, testcase='Full_lb_vserver_initial_run')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Second run
        result = utils.run_ansible_play(minimal_playbook, testcase='Full_lb_vserver_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook second run returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was incorrectly set for second run')

    def no_test_02_initial_values_set_datalength(self):
        action = copy.deepcopy(self.action)
        del action['redirurl']
        del action['authenticationhost']
        del action['authentication']
        del action['authn401']
        del action['authnvsname']
        action['name'] = 'lb-vserver-2'
        action['servicetype'] = 'MSSQL'
        action['mssqlserverversion'] = '2000'

        minimal_playbook = copy.deepcopy(self.minimal_playbook)
        minimal_playbook[0]['tasks'] = [
            {
                'name': 'test vserver with rtsp',
                'local_action': action,
            },
        ]

        result = utils.run_ansible_play(minimal_playbook, testcase='Full_lb_vserver_rtsp')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')


class MinimalInitialSetValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()
        cls.action= {
            'operation': 'present',
            'module': 'netscaler_lb_vserver',

            'name': 'lb-vserver-1',
            'ipv46': '10.79.1.1',
            'port': 80,
            'servicetype': 'HTTP',

        }
        cls.action.update(utils.nitro_dict)

        service_action = {
            'operation': 'present',
            'module': 'netscaler_service',
            'name': 'service-http-1',
            'ipaddress': '192.168.1.1',
            'servicetype': 'HTTP',
            'port': 80,
        }
        service_action.update(utils.nitro_dict)

        cls.minimal_playbook =  [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'service-1',
                    'local_action': service_action,
                },
                {
                    'name': 'test vserver 1',
                    'local_action': cls.action,
                }
            ]
        }]
        result = utils.run_ansible_play(cls.minimal_playbook)


    def test_01_add_more_attributes(self):
        action = copy.deepcopy(self.action)
        action.update({
            'dns64': 'DISABLED',
            'servicetype': 'HTTP',
            'redirurl': 'http://somewhere.com',
            'sopersistence': 'ENABLED',
            'comment': 'Vserver comment',
            'vipheader': 'vip',
            'insertvserveripport': 'VIPADDR',
            'servicebindings': [
                {
                    'servicename': 'service-http-1',
                    'weight': 100
                },
            ]
        })
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
