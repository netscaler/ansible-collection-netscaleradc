from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = '' #TODO: Module name here

####### TESTBED DATA STARTS ###########

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []

    testbedObj = BaseIntegrationModule(test_type, '')  #TODO: prerequisite module here
    testbed = OrderedDict(
        [
            ('name', 'sample testbed name'),
            ('', ''),
        ]
    )
    if '12.0' == ns_version:
        testbed['name'] = 'testbed name for 12.0'
    testbed_data.append(testbedObj.add_testbed('setup', testbed))
    
    # --------------

    testbedObj = BaseIntegrationModule(test_type, '')  #TODO: prerequisite module here
    testbed = OrderedDict(
        [
            ('', ''),
            ('', ''),
        ]
    )
    testbed_data.append(testbedObj.add_testbed('setup', testbed))

    return testbed_data
    
####### TESTBED DATA ENDS ###########




####### ACTUAL MODULE INPUT DATA STARTS ###############

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule '' #TODO: submodule name
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, '') #TODO: submodule name here
    setup_data = OrderedDict(
        [
            ('name', 'default name'),
            ('', ''),
            ('', ''),
        ]
    )
    if '12.0' == ns_version:
        setup_data['name'] = 'default name for 12.0'
    
    update_data = copy.deepcopy(setup_data)
    update_data['name'] = 'name updated'    

    remove_data = copy.deepcopy(update_data)
    remove_data['state'] = 'absent'    

    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # --------------

    # For Submodule '' #TODO: submodule name
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, '') #TODO: submodule name here
    setup_data = OrderedDict(
        [
            ('name', ''),
            ('', ''),
        ]
    )
    

    remove_data = copy.deepcopy(setup_data)
    remove_data['state'] = 'absent'    
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

    return input_data

####### ACTUAL MODULE INPUT DATA ENDS ###############
