from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_global_bindings'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    testbedObj = BaseIntegrationModule(test_type, 'netscaler_appfw_policy')
    appfw_policy = OrderedDict(
        [
            ('name', 'integration_test_policy'),
            ('rule','HTTP.REQ.BODY.EQ("hello content")'),
            ('profilename','APPFW_BYPASS'),
        ]
    )
    
    testbed_data.append(testbedObj.add_testbed('setup', appfw_policy))

    return testbed_data


def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'appfwpolicy_bindings')

    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('appfwpolicy_bindings', OrderedDict([
                ('mode', 'bind'),
                ('attributes', [OrderedDict([
                    ('globalbindtype',  'SYSTEM_GLOBAL'),
                    ('policyname',  'integration_test_policy'),
                    ('state',  'ENABLED'),
                    ('priority', '"111"'),
                    ('gotopriorityexpression',  'end'),
                    ('type',  'REQ_OVERRIDE'),

                    # FIXME add a testcase to test these commented values as well
                    #('labelname',  'integration_test_policy'),
                    #('invoke', True),
                    #('labeltype',  'policylabel'),
                ])]),
            ])),
        ]
    )

    submodObj.add_operation('bind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('bind_twice', copy.deepcopy(attributes), run_once=True)

    attributes['appfwpolicy_bindings']['mode'] = 'unbind'

    submodObj.add_operation('unbind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('unbind_twice', copy.deepcopy(attributes), run_once=True)

    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

    # auditnslogpolicy
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'appfwauditnslog_bindings')

    
    auditnslog_policy = [OrderedDict([
        ('name', 'setup auditnslogpolicy'),
        ('delegate_to', 'localhost'),
        ('netscaler_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),

            ('operation', 'add'),

            ('resource', 'auditnslogpolicy'),
            ('attributes', OrderedDict([
                ('name', 'integration_test_auditnslogpolicy'),
                ('rule', 'ns_true'),
                ('action', 'SETASLEARNNSLOG_ACT'),
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Create audit nslogpolicy', copy.deepcopy(auditnslog_policy), run_once=True)

    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('auditnslogpolicy_bindings', OrderedDict([
                ('mode', 'bind'),
                ('attributes', [OrderedDict([
                    ('policyname',  'integration_test_auditnslogpolicy'),
                    ('priority',  '"100"'),
                    ('state',  'enabled'),
                    ('gotopriorityexpression',  'end'),
                    ('type', 'NONE'),

                    # FIXME add a testcase to test these commented values as well
                    #('labelname',  'integration_test_policy'),
                    #('invoke', True),
                    #('labeltype',  'policylabel'),
                ])]),
            ])),
        ]
    )

    submodObj.add_operation('bind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('bind_twice', copy.deepcopy(attributes), run_once=True)

    attributes['auditnslogpolicy_bindings']['mode'] = 'unbind'
    submodObj.add_operation('unbind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('unbind_twice', copy.deepcopy(attributes), run_once=True)

    auditnslog_policy[0]['netscaler_nitro_request']['operation'] = 'delete'
    auditnslog_policy[0]['netscaler_nitro_request']['name'] = auditnslog_policy[0]['netscaler_nitro_request']['attributes']['name']
    submodObj.add_raw_operation('Remove audit nslogpolicy', copy.deepcopy(auditnslog_policy), run_once=True)

    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})


    # auditsyslogpolicy
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'appfwauditsyslog_bindings')

    auditnslog_policy = [OrderedDict([
        ('name', 'setup auditsyslogpolicy'),
        ('delegate_to', 'localhost'),
        ('netscaler_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),

            ('operation', 'add'),

            ('resource', 'auditsyslogpolicy'),
            ('attributes', OrderedDict([
                ('name', 'integration_test_auditsyslogpolicy'),
                ('rule', 'ns_true'),

                # FIXME try to create test_audit_server automatically
                ('action', 'test_audit_server'),
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Create audit nslogpolicy', copy.deepcopy(auditnslog_policy), run_once=True)


    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('auditsyslogpolicy_bindings', OrderedDict([
                ('mode', 'bind'),
                ('attributes', [OrderedDict([
                    ('policyname',  'integration_test_auditsyslogpolicy'),
                    ('priority', '"101"'),
                    ('state', 'enabled'),
                    ('gotopriorityexpression',  'end'),
                    ('type', 'NONE'),

                    # FIXME add a testcase to test these commented values as well
                    #('labelname',  'integration_test_policy'),
                    #('invoke', True),
                    #('labeltype',  'policylabel'),
                ])]),
            ])),
        ]
    )

    submodObj.add_operation('bind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('bind_twice', copy.deepcopy(attributes), run_once=True)

    attributes['auditsyslogpolicy_bindings']['mode'] = 'unbind'

    submodObj.add_operation('unbind_once', copy.deepcopy(attributes), run_once=True)
    submodObj.add_operation('unbind_twice', copy.deepcopy(attributes), run_once=True)


    auditnslog_policy[0]['netscaler_nitro_request']['operation'] = 'delete'
    auditnslog_policy[0]['netscaler_nitro_request']['name'] = auditnslog_policy[0]['netscaler_nitro_request']['attributes']['name']
    submodObj.add_raw_operation('Remove audit nslogpolicy', copy.deepcopy(auditnslog_policy), run_once=True)

    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})


    return input_data
