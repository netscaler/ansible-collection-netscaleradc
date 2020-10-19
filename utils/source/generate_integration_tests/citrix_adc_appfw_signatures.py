from collections import OrderedDict
import copy
import codecs
import base64

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_appfw_signatures'

####### TESTBED DATA STARTS ###########

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    return testbed_data

sample_xml='''\
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013-2019 Citrix Systems, Inc. All rights reserved. -->
<SignaturesFile schema_version="6" version="34">
<Signatures>
  <SignatureRule actions="block,log" category="web-misc" enabled="OFF" id="509" source="Snort" sourceid="509" type="" version="15">
    <LogString>WEB-MISC PCCS mysql database admin tool access</LogString>
    <PatternList>
      <RequestPatterns>
        <Pattern type="fastmatch">
          <Location area="HTTP_URL"/>
          <Match type="LITERAL">pccsmysqladm/incs/dbconnect.inc</Match>
        </Pattern>
      </RequestPatterns>
    </PatternList>
    <Reference>bugtraq,1557</Reference>
    <Reference>cve,2000-0707</Reference>
    <Reference>nessus,10783</Reference>
  </SignatureRule>
</Signatures>
</SignaturesFile>
'''
    
####### TESTBED DATA ENDS ###########



####### ACTUAL MODULE INPUT DATA STARTS ###############

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'citrix_adc_appfw_signatures'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_appfw_signatures')

    # Create sample_sign.xml
    create_sample_xml = [OrderedDict([
        ('name', 'setup sample xml file'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),
            ('validate_certs', 'no'),

            ('operation', 'add'),

            ('resource', 'systemfile'),
            ('attributes', OrderedDict([
                ('filename', 'sample_sign.xml'),
                ('filecontent', codecs.decode(base64.b64encode(codecs.encode(sample_xml))) ),
                ('filelocation',  '/var/tmp'),
            ])),
        ])),
    ])]

    submodObj.add_raw_operation('Create sample xml', copy.deepcopy(create_sample_xml), run_once=True)

    # Main steps
    import_data = OrderedDict(
        [
            ('name', 'integration_test'),
            ('src', 'local://sample_sign.xml'),
            ('comment', 'integration test comment'),
            ('overwrite', True),
        ]
    )
   
    remove_data = copy.deepcopy(import_data)
    remove_data['state'] = 'absent'    

    submodObj.add_operation('import', import_data)
    submodObj.add_operation('remove', remove_data)

    # Delete sample_sign.xml
    # Delete error.html
    delete_sample_xml = [OrderedDict([
        ('name', 'delete sample xml'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),
            ('validate_certs', 'no'),

            ('operation', 'delete_by_args'),

            ('resource', 'systemfile/sample_sign.xml'),
            ('args', OrderedDict([
                ('filelocation',  '\'%2Fvar%2Ftmp\'')
            ])),
        ])),
    ])]

    submodObj.add_raw_operation('Delete sample xml', copy.deepcopy(delete_sample_xml), run_once=True)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    return input_data

####### ACTUAL MODULE INPUT DATA ENDS ###############
