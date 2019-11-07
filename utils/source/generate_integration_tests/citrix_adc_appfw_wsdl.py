from collections import OrderedDict
import copy
import codecs
import base64

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_appfw_wsdl'

####### TESTBED DATA STARTS ###########

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    return testbed_data

wsdl_data='''\
<definitions name = "HelloService"
   targetNamespace = "http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns = "http://schemas.xmlsoap.org/wsdl/"
   xmlns:soap = "http://schemas.xmlsoap.org/wsdl/soap/"
   xmlns:tns = "http://www.examples.com/wsdl/HelloService.wsdl"
   xmlns:xsd = "http://www.w3.org/2001/XMLSchema">
 
   <message name = "SayHelloRequest">
      <part name = "firstName" type = "xsd:string"/>
   </message>
	
   <message name = "SayHelloResponse">
      <part name = "greeting" type = "xsd:string"/>
   </message>

   <portType name = "Hello_PortType">
      <operation name = "sayHello">
         <input message = "tns:SayHelloRequest"/>
         <output message = "tns:SayHelloResponse"/>
      </operation>
   </portType>

   <binding name = "Hello_Binding" type = "tns:Hello_PortType">
      <soap:binding style = "rpc"
         transport = "http://schemas.xmlsoap.org/soap/http"/>
      <operation name = "sayHello">
         <soap:operation soapAction = "sayHello"/>
         <input>
            <soap:body
               encodingStyle = "http://schemas.xmlsoap.org/soap/encoding/"
               namespace = "urn:examples:helloservice"
               use = "encoded"/>
         </input>
		
         <output>
            <soap:body
               encodingStyle = "http://schemas.xmlsoap.org/soap/encoding/"
               namespace = "urn:examples:helloservice"
               use = "encoded"/>
         </output>
      </operation>
   </binding>

   <service name = "Hello_Service">
      <documentation>WSDL File for HelloService</documentation>
      <port binding = "tns:Hello_Binding" name = "Hello_Port">
         <soap:address
            location = "http://www.examples.com/SayHello/" />
      </port>
   </service>
</definitions>
'''
    
####### TESTBED DATA ENDS ###########



####### ACTUAL MODULE INPUT DATA STARTS ###############

def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'citrix_adc_appfw_wsdl'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'citrix_adc_appfw_wsdl')

    # Create wsdl sample
    create_wsdl = [OrderedDict([
        ('name', 'setup auditnslogpolicy'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),

            ('operation', 'add'),

            ('resource', 'systemfile'),
            ('attributes', OrderedDict([
                ('filename', 'sample.wsdl'),
                ('filecontent', codecs.decode(base64.b64encode(codecs.encode(wsdl_data))) ),
                ('filelocation',  '/var/tmp')
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Create wsdl file', copy.deepcopy(create_wsdl), run_once=True)

    import_data = OrderedDict(
        [
            ('name', 'integration_test'),
            ('src', 'local://sample.wsdl'),
            ('comment', 'integration test comment'),
            ('overwrite', True),
        ]
    )
   
    remove_data = copy.deepcopy(import_data)
    remove_data['state'] = 'absent'    

    submodObj.add_operation('import', import_data)
    submodObj.add_operation('remove', remove_data)

    # Delete wsdl sample
    delete_wsdl = [OrderedDict([
        ('name', 'setup auditnslogpolicy'),
        ('delegate_to', 'localhost'),
        ('citrix_adc_nitro_request', OrderedDict([
            ('nitro_user', '{{ nitro_user }}'),
            ('nitro_pass', '{{ nitro_pass }}'),
            ('nsip', '{{ nsip }}'),

            ('operation', 'delete_by_args'),

            ('resource', 'systemfile/sample.wsdl'),
            ('args', OrderedDict([
                ('filelocation',  '\'%2Fvar%2Ftmp\'')
            ])),
        ])),
    ])]
    submodObj.add_raw_operation('Delete wsdl file', copy.deepcopy(delete_wsdl), run_once=True)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    return input_data

####### ACTUAL MODULE INPUT DATA ENDS ###############
