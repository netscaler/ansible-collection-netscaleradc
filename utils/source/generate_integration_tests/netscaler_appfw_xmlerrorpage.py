from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'netscaler_appfw_xmlerrorpage'

####### TESTBED DATA STARTS ###########

# PREREQUISITES/Testbed
def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []
    return testbed_data
    
####### TESTBED DATA ENDS ###########



####### ACTUAL MODULE INPUT DATA STARTS ###############

def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'netscaler_appfw_xmlerrorpage'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'netscaler_appfw_xmlerrorpage')
    import_data = OrderedDict(
        [
            ('name', 'integration_test'),
            ('src', 'local://error.xml'),
            ('comment', 'integration test comment'),
            ('overwrite', True),
        ]
    )
   
    remove_data = copy.deepcopy(import_data)
    remove_data['state'] = 'absent'    

    submodObj.add_operation('import', import_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    return input_data

####### ACTUAL MODULE INPUT DATA ENDS ###############
