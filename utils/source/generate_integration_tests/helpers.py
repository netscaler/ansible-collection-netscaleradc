from collections import OrderedDict
import copy
import pyaml
import codecs

SKELETON = [
    OrderedDict([
        ('name', 'Get object'),
        ('delegate_to', 'localhost'),
        ('register', 'get_result'),
        ('netscaler_nitro_request', 
            OrderedDict([
                ('nsip', '{{ instance_ip }}'),
                ('nitro_user', '{{ nitro_user }}'),
                ('nitro_pass', '{{ nitro_pass }}'),
                ('operation', 'get'),
                ('resource', ''),
                ('name', ''),

            ])
         ),
    ]),

    OrderedDict([
        ('name', 'Assert equality of NITRO attributes'),
        ('assert',
            OrderedDict([
                ('that', []),
            ]),
        ),
    ]),
]
def get_verification_playbook_dict(nitro_resource, nitro_resource_name, verification_dict):
    playbook = copy.deepcopy(SKELETON)
    get_dict = playbook[0]['netscaler_nitro_request']


    get_dict['resource'] = nitro_resource
    get_dict['name'] = nitro_resource_name

    assertion_dict =  playbook[1]['assert']

    for key, value in verification_dict.items():
        #value = codecs.decode(pyaml.dumps(value), 'utf-8')
        assertion = r'get_result.nitro_object[0].%s == %s' % (key, value)
        assertion_dict['that'].append(assertion)
    return playbook
