from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adc_appfw_xmlcontenttype'

def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')

    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('xmlcontenttypevalue',  'integraton.*test'),
            ('isregex',  'REGEX'),


        ]
    )

    submodObj.add_operation('setup', copy.deepcopy(attributes))

    attributes['isregex'] = 'NOTREGEX'

    submodObj.add_operation('update', copy.deepcopy(attributes))

    # Remove
    delete_dict = OrderedDict()
    for key in attributes:
        if key in ('state', 'xmlcontenttypevalue'):
            delete_dict[key] = attributes[key]
    delete_dict['state'] = 'absent'

    submodObj.add_operation('remove', delete_dict)


    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
