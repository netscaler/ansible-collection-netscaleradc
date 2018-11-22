from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adc_appfw_fieldtype'

def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []

    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')

    attributes = OrderedDict(
        [
            ('state',  'present'),

            ('name',  'integration_test_field_type'),
            ('regex',  'test_.*regex'),
            ('priority',  '"100"'),
            ('comment',  'some comment'),

            # FIXME nocharmaps does not work with 12.1
            #('nocharmaps',  True),


        ]
    )

    submodObj.add_operation('setup', copy.deepcopy(attributes))

    attributes['regex'] = 'other_test.*regex'

    submodObj.add_operation('update_regex', copy.deepcopy(attributes))

    attributes['comment'] = 'Some other comment'
    submodObj.add_operation('update_comment', copy.deepcopy(attributes))

    # Remove
    delete_dict = OrderedDict()
    for key in attributes:
        if key in ('state', 'name'):
            delete_dict[key] = attributes[key]
    delete_dict['state'] = 'absent'

    submodObj.add_operation('remove', delete_dict)


    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
