#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adm_stylebook
short_description: Create or delete Citrix ADM stylebooks.
description:
    - Create or delete Citrix ADM stylebooks.
    - Note that due to API limitations this module does not work with basic authentication.
    - Instead use the I(nitro_auth_token) option.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    source:
        description:
            - "Source definition of the StyleBook."
            - " Minimum length =  1"
            - " Maximum length =  32"
        type: str

    namespace:
        description:
            - "Namespace of the StyleBook."
            - " Minimum length =  1"
            - " Maximum length =  32"
        type: str
        required: true

    version:
        description:
            - "Version of the StyleBook."
            - " Minimum length =  1"
            - " Maximum length =  32"
        type: str
        required: true

    name:
        description:
            - "Name of the StyleBook."
        type: str
        required: true

    display_name:
        description:
            - "Display name of the StyleBook."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''

- name: Setup stylebook
  delegate_to: localhost
  citrix_adm_stylebook:
    adm_ip: 192.168.1.1
    nitro_auth_token: "{{ login_result.session_id }}"

    state: present

    name: basic-lb-config
    namespace: com.example.stylebooks
    version: "0.1"

    source: "{{ lookup('file', 'stylebook_sample.yaml') }}"

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
import codecs
import base64

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adm.plugins.module_utils.citrix_adm import (
    NitroAPIFetcher,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines
)


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
        self.calculate_configured_stylebook()
        self.fetch_stylebook()

    def calculate_configured_stylebook(self):
        log('ModuleExecutor.calculate_configured_stylebook()')
        self.configured_stylebook = {}
        for attribute in self.attribute_config['stylebook']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['stylebook']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_stylebook[attribute] = value

        log('calculated configured stylebook %s' % self.configured_stylebook)

    def fetch_stylebook(self):
        log('ModuleExecutor.fetch_stylebook()')
        resource_tuple = (
            self.configured_stylebook['namespace'],
            self.configured_stylebook['version'],
            self.configured_stylebook['name'],
        )
        resource = 'stylebooks/%s/%s/%s' % resource_tuple
        result = self.nitro_api_fetcher.get(resource=resource)
        log('get result %s' % result)

        if result['http_response_data']['status'] == 200:
            self.fetched_stylebook = result['data'].get('stylebook', {})
        elif result['http_response_data']['status'] in [400, 404]:
            unexpected_error = True
            if 'data' in result:
                if 'errorcode' in result['data']:
                    if result['data']['errorcode'] in [555, 530]:
                        unexpected_error = False
                        self.fetched_stylebook = {}
                elif 'error_code' in result['data']:
                    if result['data']['error_code'] in [555, 530]:
                        unexpected_error = False
                        self.fetched_stylebook = {}
            if unexpected_error:
                self.module.fail_json(
                    msg='Unexpected error during fetch',
                    **self.module_result
                )
        else:
            self.module.fail_json(
                msg='Unexpected error during fetch',
                **self.module_result
            )


    def stylebook_exists(self):
        if self.fetched_stylebook != {}:
            return True
        else:
            return False

    def stylebook_identical(self):
        log('ModuleExecutor.stylebook_identical()')
        identical = True
        for attribute in self.configured_stylebook:
            if attribute == 'source':
                continue
            configured_value = self.configured_stylebook[attribute]
            fetched_value = self.fetched_stylebook.get(attribute)
            if configured_value != fetched_value:
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(fetched_value),
                    fetched_value
                )
                log('Attribute %s differs. configured: (%s) %s  fetched: (%s) %s' % str_tuple)
                identical = False

        if 'source' in self.configured_stylebook:
            configured_value = self.configured_stylebook['source']
            fetched_value = self.fetched_stylebook.get('source')
            if fetched_value is not None:
                fetched_value = codecs.decode(base64.b64decode(fetched_value))
                str_tuple = (
                    'source',
                    type(configured_value),
                    configured_value,
                    type(fetched_value),
                    fetched_value
                )
            if configured_value != fetched_value:
                log('Attribute %s differs. configured: (%s) %s  fetched: (%s) %s' % str_tuple)
                identical = False

        return identical


    def create_stylebook(self):
        log('ModuleExecutor.create_stylebook()')

        post_data = {
            'stylebook': self.configured_stylebook
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
        resource_tuple = (
            self.module.params['namespace'],
            self.module.params['version'],
            self.module.params['name'],
        )
        resource = 'stylebooks/%s/%s/%s' % resource_tuple
        result = self.nitro_api_fetcher.get(resource=resource)

        if result['http_response_data']['status'] != 200:
            message_tuple = (
                result['http_response_data']['status'],
                result['nitro_errorcode'],
                result['nitro_message'],
                result['nitro_severity'],
            )
            msg = 'GET http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

        log('result of get  stylebooks %s' % result)
        stylebooks = result['data']['stylebooks']
        if not isinstance(stylebooks, list):
            msg = 'Unexpected stylebooks result type %s' % type(stylebooks)
            self.module.fail_json(msg=msg, **self.module_result)

        if stylebooks == []:
            self.module.fail_json(msg='Failed to get the created stylebook', **self.module_result)
        elif len(stylebooks) > 1:
            self.module.fail_json(msg='Multiple stylebooks were returned', **self.module_result)
        else:
            return stylebooks[0]

    def update_stylebook(self):
        log('ModuleExecutor.update_stylebook()')
        self.delete_stylebook()
        self.create_stylebook()

    def delete_stylebook(self):
        # Go on with the deletion
        resource_tuple = (
            self.configured_stylebook['namespace'],
            self.configured_stylebook['version'],
            self.configured_stylebook['name'],
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
            msg = 'DELETE http status %s. nitro_errorcode=%s, nitro_message=%s, nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                if not self.stylebook_exists():
                    self.module_result['changed'] = True
                    if not self.module.check_mode:
                        self.create_stylebook()
                else:
                    if not self.stylebook_identical():
                        self.module_result['changed'] = True
                        if not self.module.check_mode:
                            self.update_stylebook()

            elif self.module.params['state'] == 'absent':
                if self.stylebook_exists():
                    self.module_result['changed'] = True
                    if not self.module.check_mode:
                        self.delete_stylebook()

            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        source=dict(
            type='str'
        ),
        namespace=dict(
            type='str',
            required=True,
        ),
        version=dict(
            type='str',
            required=True,
        ),
        name=dict(
            type='str',
            required=True,
        ),
        display_name=dict(
            type='str'
        ),
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
