from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = '' #TODO: Module name here
input_data = OrderedDict()
testbed_data = []

# PREREQUISITES/Testbed
testbedObj = BaseIntegrationModule('') #TODO: prerequisite module here
testbed = OrderedDict(
    [
        ('', ''),
        ('', ''),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed))

testbed = OrderedDict(
    [
        ('', ''),
        ('', ''),
    ]
)
testbed_data.append(testbedObj.add_testbed('setup', testbed))



# For Submodule '' #TODO: submodule name
submodObj = BaseIntegrationModule(ENTITY_NAME, '') #TODO: submodule name here
setup_data = OrderedDict(
    [
        ('', ''),
        ('', ''),
        ('', ''),
    ]
)

update_data = OrderedDict(
    [
        ('', ''),
        ('', ''),
        ('', ''),
    ]
)

remove_data = OrderedDict(
    [
        ('name', ''),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('update', update_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})

# For Submodule '' #TODO: submodule name
submodObj = BaseIntegrationModule(ENTITY_NAME, '') #TODO: submodule name here
setup_data = OrderedDict(
    [
        ('name', ''),
        ('', ''),
    ]
)

remove_data = OrderedDict(
    [
        ('name', ''),
        ('state', 'absent'),
    ]
)

submodObj.add_operation('setup', setup_data)
submodObj.add_operation('remove', remove_data)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
