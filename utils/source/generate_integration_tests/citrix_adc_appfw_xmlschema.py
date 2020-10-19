from collections import OrderedDict
import copy
import codecs
import base64

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_appfw_xmlschema'
schema_data='''\
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:element name="shiporder">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="orderperson" type="xs:string"/>
      <xs:element name="shipto">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="name" type="xs:string"/>
            <xs:element name="address" type="xs:string"/>
            <xs:element name="city" type="xs:string"/>
            <xs:element name="country" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="item" maxOccurs="unbounded">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="title" type="xs:string"/>
            <xs:element name="note" type="xs:string" minOccurs="0"/>
            <xs:element name="quantity" type="xs:positiveInteger"/>
            <xs:element name="price" type="xs:decimal"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="orderid" type="xs:string" use="required"/>
  </xs:complexType>
</xs:element>

</xs:schema> 
'''

####### TESTBED DATA STARTS ###########

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    return testbed_data
    
####### TESTBED DATA ENDS ###########



####### ACTUAL MODULE INPUT DATA STARTS ###############

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'citrix_adc_appfw_xmlschema'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_appfw_xmlschema')

    # Create xml schema file
    create_xsd = [OrderedDict([
        ('name', 'create xsd file'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),
            ('validate_certs', 'no'),

            ('operation', 'add'),

            ('resource', 'systemfile'),
            ('attributes', OrderedDict([
                ('filename', 'error.xsd'),
                ('filecontent', codecs.decode(base64.b64encode(codecs.encode(schema_data))) ),
                ('filelocation',  '/var/tmp')
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Create xsd file', copy.deepcopy(create_xsd), run_once=True)

    import_data = OrderedDict(
        [
            ('name', 'integration_test'),
            ('src', 'local://error.xsd'),
            ('comment', 'integration test comment'),
            ('overwrite', True),
        ]
    )
   
    remove_data = copy.deepcopy(import_data)
    remove_data['state'] = 'absent'    

    submodObj.add_operation('import', import_data)
    submodObj.add_operation('remove', remove_data)

    # Delete xsd file
    delete_xsd = [OrderedDict([
        ('name', 'delete xsd'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),
            ('validate_certs', 'no'),

            ('operation', 'delete_by_args'),

            ('resource', 'systemfile/error.xsd'),
            ('args', OrderedDict([
                ('filelocation',  '\'%2Fvar%2Ftmp\'')
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Delete xsd file', copy.deepcopy(delete_xsd), run_once=True)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    return input_data

####### ACTUAL MODULE INPUT DATA ENDS ###############
