from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_settings'
input_data = OrderedDict()
testbed_data = []

submodObj = BaseIntegrationModule(ENTITY_NAME, 'basic')

attributes = OrderedDict(
    [
        ('state',  'present'),
        ('defaultprofile',  'APPFW_BYPASS'),
        ('undefaction',  'APPFW_BLOCK'),
        ('sessiontimeout',  '"1000"'),
        ('learnratelimit',  '"500"'),
        ('sessionlifetime',  '"2000"'),
        ('sessioncookiename',  'cookie_name'),
        ('clientiploggingheader',  'header_name'),
        ('importsizelimit',  '"134217000"'),
        ('signatureautoupdate',  'on'),
        ('signatureurl',  'http://signature.url'),
        ('cookiepostencryptprefix',  'prepend'),
        ('logmalformedreq',  'on'),
        ('geolocationlogging',  'on'),
        ('ceflogging',  'on'),
        ('entitydecoding',  'on'),
        ('useconfigurablesecretkey',  'on'),
        ('sessionlimit',  '"10000"'),

    ]
)

submodObj.add_operation('setup', copy.deepcopy(attributes), run_once=True)


attributes['ceflogging'] = 'off'

submodObj.add_operation('update_ceflogging', copy.deepcopy(attributes), run_once=True)

attributes['importsizelimit'] = '"134217727"'

submodObj.add_operation('update_importsizelimit', copy.deepcopy(attributes), run_once=True)

input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
