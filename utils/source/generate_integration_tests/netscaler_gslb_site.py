from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'netscaler_gslb_site'
input_data = OrderedDict()
testbed_data = []

# PREREQUISITES/Testbed
# testbedObj = BaseIntegrationModule('') #TODO: prerequisite module here
# testbed = OrderedDict(
    # [
        # ('', ''),
        # ('', ''),
    # ]
# )
# testbed_data.append(testbedObj.add_testbed('setup', testbed))

# For Submodule 'gslb_site'
submodObj = BaseIntegrationModule(ENTITY_NAME, 'gslb_site')
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

