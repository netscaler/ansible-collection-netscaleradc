from collections import OrderedDict
import copy
import re
import json
import yaml
import pyaml
import codecs


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adm_application'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    # FIXME create stylebook for use with application on the fly instead of using hardcoded one
    testbed_data = []

    return testbed_data

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()

    # 12.0 does not have the application feature as it is implemented in 12.1
    if ns_version == '12.0':
        return input_data

    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')

    # FIXME don't hardcode instance id
    application_name = 'integration_test_application'
    stylebook_params = {
        "name": "basic-lb-config",
        "namespace": "com.example.stylebooks",
        "version": "0.1",
        "configpack_payload": {
            "parameters": {
                "name": application_name,
                "ip": "192.199.19.1",
                "lb-alg": "ROUNDROBIN",
                "svc-servers": [
                    "192.199.19.3",
                ],
                "svc-port": "80",
            },
            "targets": [
                { "id": "6a28b48b-e7c0-4770-b499-3ddb85b47561"},
            ]
        }
    }

    attributes = OrderedDict(
        [
            ('state',  'present'),
            ('name', application_name),

            ('check_create', True),
            ('check_create_delay', 10),

            ('poll_after_delete', True),
            ('poll_delay', 10),

            ('stylebook_params', json.dumps(stylebook_params)),

        ]
    )

    submodObj.add_operation('setup', copy.deepcopy(attributes), run_once=True)

    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes), run_once=True)


    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
