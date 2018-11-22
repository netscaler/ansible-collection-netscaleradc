from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_gslb_site'


def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    #TODO: testbed data here
    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'gslb_site'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'gslb_site')
    setup_data = OrderedDict(
        [
            ('sitename', 'gslb-site-1'),
            ('siteipaddress', '192.168.1.1'),
            ('sitetype', 'LOCAL'),
            ('publicip', '192.168.1.1'),
            ('metricexchange', 'enabled'),
            ('nwmetricexchange', 'enabled'),
            ('sessionexchange', 'enabled'),
            ('triggermonitor', 'ALWAYS'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('sitename', 'gslb-site-1'),
            ('siteipaddress', '192.168.1.1'),
            ('sitetype', 'LOCAL'),
            ('publicip', '192.168.1.1'),
            ('metricexchange', 'disabled'),
            ('nwmetricexchange', 'enabled'),
            ('sessionexchange', 'enabled'),
            ('triggermonitor', 'ALWAYS'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('sitename', 'gslb-site-1'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
    
