from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_confidfield'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data


def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')

    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('fieldname',  'confidfield_integration_test'),
            ('url', '\'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")\''),
            ('isregex',  'REGEX'),
            ('comment',  'conf id field comment'),
        ]
    )

    submodObj.add_operation('setup', copy.deepcopy(attributes))

    attributes['comment'] = 'some other comment'

    submodObj.add_operation('update', copy.deepcopy(attributes))

    # Delete entity
    attributes['state'] = 'absent'

    # Make sure delete works with the minimum number of attributes
    del attributes['isregex']
    del attributes['comment']

    submodObj.add_operation('delete', copy.deepcopy(attributes))



    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
