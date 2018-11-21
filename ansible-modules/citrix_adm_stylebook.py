#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2018 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



DOCUMENTATION = '''
---
module: citrix_adm_stylebook
short_description: Create or delete Citrix ADM stylebooks.
description: Create or delete Citrix ADM stylebooks.

version_added: "2.8.0"

options:

    source:
        description:
            - Source definition of the StyleBook.
            - Minimum length = 1
            - Maximum length = 32
        type: str

    namespace:
        description:
            - Namespace of the StyleBook.
            - Minimum length = 1
            - Maximum length = 32
        type: str

    version:
        description:
            - Version of the StyleBook.
            - Minimum length = 1
            - Maximum length = 32
        type: str

    name:
        description:
            - Name of the StyleBook.
        type: str

    display_name:
        description:
            - Display name of the StyleBook.
            - Minimum length = 1
            - Maximum length = 128
        type: str


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
vars:
stylebook_contents: "{{ lookup('file', 'stylebook_sample.yaml') }}"

- name: Setup stylebook
  delegate_to: localhost
  citrix_adm_stylebook:
    mas_ip: 192.168.1.1
    nitro_auth_token: "{{ login_result.session_id }}"

    state: present

    name: basic-lb-config
    namespace: com.example.stylebooks
    version: "0.1"

    source: "{{ stylebook_contents }}"
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"

stylebook:
    description: Dictionary containing the attributes of the created stylebook.
    returned: success
    type: dict
'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import NitroAPIFetcher, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):
    
    def __init__(self, module):
        self.module = module
        self.nitro_api_fetcher = NitroAPIFetcher(module, api_path='stylebook/nitro/v1/config')
        self.main_nitro_class = 'stylebook'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            
            'stylebook': {
                'attributes_list': [
                    
                    'source',
                    'namespace',
                    'version',
                    'name',
                    'display_name',
                ],
                'transforms': {
                    
                },
                'get_id_attributes': [
                    
                    'namespace',
                    'version',
                    'name',
                ],
                'delete_id_attributes': [
                    
                    'namespace',
                    'version',
                    'name',
                ],
            },
            

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def main_object_exists(self):
        filter = {}
        for attribute in self.attribute_config['stylebook']['get_id_attributes']:
            attr_val = self.module.params.get(attribute)
            if attr_val is not None:
                filter[attribute] = attr_val

        if filter == {}:
            self.module.fail_json(msg='Cannot get stylebook without any get attribute defined', **self.module_result)

        else:
            result = self.nitro_api_fetcher.get('stylebooks', filter=filter)
            log('result of get %s' % result)

            if result['http_response_data']['status'] != 200:
                message_tuple = (
                    result['http_response_data']['status'],
                    result['nitro_errorcode'],
                    result['nitro_message'],
                    result['nitro_severity'],
                )
                self.module.fail_json(msg='GET http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple, **self.module_result)
            stylebook_data = result['data']['stylebooks']
            if stylebook_data == []:
                return False
            elif len(stylebook_data) == 1:
                return True
            else:
                self.module.fail_json(msg='Got too many stylebooks %s' % len(stylebook_data))

    def create_stylebook(self):
        stylebook_data = {}
        for attribute in self.attribute_config['stylebook']['attributes_list']:
            attr_value = self.module.params.get(attribute)
            if attr_value is not None:
                stylebook_data[attribute] = attr_value

        post_data = {
            'stylebook': stylebook_data
        }
        result = self.nitro_api_fetcher.post(post_data=post_data, resource='stylebooks')
        log('result of stylebook creation %s' % result)

        if result['http_response_data']['status'] != 200:
            message_tuple = (
                result['http_response_data']['status'],
                result['nitro_errorcode'],
                result['nitro_message'],
                result['nitro_severity'],
            )
            self.module.fail_json(msg='POST http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple, **self.module_result)

        return result

    def get_stylebook(self):
        filter = {}
        for attribute in self.attribute_config['stylebook']['get_id_attributes']:
            attr_val = self.module.params.get(attribute)
            if attr_val is not None:
                filter[attribute] = attr_val
        result = self.nitro_api_fetcher.get(resource='stylebooks', filter=filter)

        if result['http_response_data']['status'] != 200:
            message_tuple = (
                result['http_response_data']['status'],
                result['nitro_errorcode'],
                result['nitro_message'],
                result['nitro_severity'],
            )
            self.module.fail_json(msg='GET http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple, **self.module_result)

        log('result of get  stylebooks %s' % result)
        stylebooks = result['data']['stylebooks']
        if not isinstance(stylebooks, list):
            msg = 'Unexpected stylebooks result type %s' % type(stylebooks)
            self.module.fail_json(msg=msg, **self.module_result)

        if stylebooks == []:
            self.module.fail_json('Failed to get the created stylebook', **self.module_result)
        elif len(stylebooks) > 1:
            self.module.fail_json('Multiple stylebooks were returned', **self.module_result)
        else:
            return stylebooks[0]




    def create(self):

        if not self.main_object_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.create_stylebook()

    def delete_stylebook(self):
        # Check if all attributes are present
        for attribute in self.attribute_config['stylebook']['delete_id_attributes']:
            attr_val = self.module.params.get(attribute)
            if attr_val is None:
                self.module.fail_json('Must define attribute %s for deletion' % attribute, **self.module_result)

        # Go on with the deletion
        resource_tuple = (
            self.module.params['namespace'],
            self.module.params['version'],
            self.module.params['name'],
        )
        resource = 'stylebooks/%s/%s/%s' % resource_tuple
        result = self.nitro_api_fetcher.delete(resource=resource)
        log('result of delete %s' % result)

        if result['http_response_data']['status'] != 200:
            message_tuple = (
                result['http_response_data']['status'],
                result['nitro_errorcode'],
                result['nitro_message'],
                result['nitro_severity'],
            )
            self.module.fail_json(msg='DELETE http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple, **self.module_result)


    def delete(self):

        if self.main_object_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_stylebook()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.create()
                created_stylebook = self.get_stylebook()
                self.module_result.update(dict(stylebook=created_stylebook))
            elif self.module.params['state'] == 'absent':
                self.delete()

            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)



def main():


    argument_spec = dict()

    module_specific_arguments = dict(
        
        source=dict(type='str',),

        
        namespace=dict(type='str',
        required=True,),

        
        version=dict(type='str',
        required=True,),

        
        name=dict(type='str',
        required=True,),

        
        display_name=dict(type='str',),

        
    )


    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)


    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()