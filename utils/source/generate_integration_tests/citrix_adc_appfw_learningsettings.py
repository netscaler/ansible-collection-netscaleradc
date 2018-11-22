from collections import OrderedDict
import copy
import re


import helpers


from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'citrix_adc_appfw_learningsettings'

def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []

    testbedObj = BaseIntegrationModule(test_type, 'citrix_adc_appfw_profile')
    lb_vserver_data = OrderedDict(
        [
            ('name', 'integration_test_profile'),
            ('defaults', 'basic'),
        ]
    )
    
    testbed_data.append(testbedObj.add_testbed('setup', lb_vserver_data))
    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
            ('profilename', 'integration_test_profile'),
            ('starturlminthreshold', '10'),
            ('starturlpercentthreshold', '10'),
            ('cookieconsistencyminthreshold', '10'),
            ('cookieconsistencypercentthreshold', '10'),
            ('csrftagminthreshold', '10'),
            ('csrftagpercentthreshold', '10'),
            ('fieldconsistencyminthreshold', '10'),
            ('fieldconsistencypercentthreshold', '10'),
            ('crosssitescriptingminthreshold', '10'),
            ('crosssitescriptingpercentthreshold', '10'),
            ('sqlinjectionminthreshold', '10'),
            ('sqlinjectionpercentthreshold', '10'),
            ('fieldformatminthreshold', '10'),
            ('fieldformatpercentthreshold', '10'),
            ('creditcardnumberminthreshold', '10'),
            ('creditcardnumberpercentthreshold', '10'),
            ('contenttypeminthreshold', '10'),
            ('contenttypepercentthreshold', '10'),
            ('xmlwsiminthreshold', '10'),
            ('xmlwsipercentthreshold', '10'),
            ('xmlattachmentminthreshold', '10'),
            ('xmlattachmentpercentthreshold', '10'),
        ]
    )
    
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    for key in attributes:
        if key in ('state', 'profilename'):
            continue
        attributes[key] = '20'
    
        submodObj.add_operation('update_%s' % key, copy.deepcopy(attributes))
    
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
