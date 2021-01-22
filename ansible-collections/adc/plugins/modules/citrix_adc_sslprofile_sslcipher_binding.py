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
module: citrix_adc_sslprofile_sslcipher_binding
short_description: Manage SSL profile and SSL cipher bindings
description:
    - Manage SSL profile and SSL cipher bindings
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.1.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    cipherpriority:
        description:
            - "cipher priority."
            - "Minimum value = C(1)"
        type: str

    name:
        description:
            - "Name of the SSL profile."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    ciphername:
        description:
            - "Name of the cipher."
            - "Minimum length =  1"
        type: str


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup binding
  delegate_to: localhost
  citrix_adc_sslprofile_sslcipher_binding:
    nsip: ""
    nitro_user: ""
    nitro_pass: ""

    validate_certs: no
    state: present

    name: test_ssl_profile
    ciphername: DTLS_FIPS
    cipherpriority: "5"

- name: Setup binding
  delegate_to: localhost
  citrix_adc_sslprofile_sslcipher_binding:
    nsip: ""
    nitro_user: ""
    nitro_pass: ""

    validate_certs: no
    state: present

    name: test_ssl_profile
    ciphername: TLS1.3-AES128-GCM-SHA256
    cipherpriority: "10"
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

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines,
    NitroAPIFetcher
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)
        self.main_nitro_class = 'servicegroup'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'sslprofile_sslcipher_binding': {
                'attributes_list': [
                    'cipherpriority',
                    'name',
                    'ciphername',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'name',
                    'ciphername',
                ],
                'non_updateable_attributes': [
                ],
            },
            }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_binding()

    def calculate_configured_binding(self):
        log('ModuleExecutor.calculate_configured_binding()')
        self.configured_binding = {}
        for attribute in self.attribute_config['sslprofile_sslcipher_binding']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['sslprofile_sslcipher_binding']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_binding[attribute] = value

        log('calculated configured sslprofile_sslcipher_binding %s' % self.configured_binding)

    def binding_exists(self):
        log('ModuleExecutor.binding_exists()')
        result = self.fetcher.get('sslprofile_sslcipher_binding', self.module.params['name'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 3248:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Sort though the bound ciphers for cipheraliasname match
        for binding in result['data'].get('sslprofile_sslcipher_binding', []):
            if binding['cipheraliasname'] == self.configured_binding['ciphername']:
                return True

        # Fallthrough
        return False

    def create_binding(self):
        log('ModuleExecutor.create_binding()')

        post_data = {
            'sslprofile_sslcipher_binding': self.configured_binding
        }

        result = self.fetcher.post(post_data=post_data, resource='sslprofile_sslcipher_binding')
        log('post data: %s' % post_data)
        log('result of post: %s' % result)
        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def update_binding(self):
        log('ModuleExecutor.update_binding()')

        self.delete_binding()
        self.create_binding()


    def binding_identical(self):
        log('ModuleExecutor.binding_identical()')
        result = self.fetcher.get('sslprofile_sslcipher_binding', self.module.params['name'])
        retrieved_bindings = result['data']['sslprofile_sslcipher_binding']

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        # Iterate over keys that already exist in the playbook
        for retrieved_object in retrieved_bindings:

            # Skip irrelevant ciphers
            if retrieved_object['cipheraliasname'] != self.configured_binding['ciphername']:
                continue

            for attribute in self.configured_binding.keys():

                # Need to add special case mapping from cipheraliasname to ciphername
                if attribute == 'ciphername':
                    retrieved_value = retrieved_object.get('cipheraliasname')
                else:
                    retrieved_value = retrieved_object.get(attribute)

                configured_value = self.configured_binding.get(attribute)
                if retrieved_value != configured_value:
                    str_tuple = (
                        attribute,
                        type(configured_value),
                        configured_value,
                        type(retrieved_value),
                        retrieved_value,
                    )
                    diff_list.append('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                    log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
            self.module_result['diff_list'] = diff_list

        if diff_list != []:
            return False
        else:
            return True

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.binding_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('binding does not exist. Will create.')
                self.create_binding()
        else:
            if not self.binding_identical():
                log('Existing binding does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_binding()
            else:
                log('Existing binding has identical values to configured.')


    def delete_binding(self):
        log('ModuleExecutor.delete_binding()')

        args = {
            'ciphername': self.configured_binding['ciphername']
        }
        result = self.fetcher.delete(
            resource='sslprofile_sslcipher_binding',
            id=self.module.params['name'],
            args=args
        )
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.binding_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_binding()

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
            elif self.module.params['state'] == 'absent':
                self.delete()

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        cipherpriority=dict(type='str'),
        name=dict(type='str'),
        ciphername=dict(type='str'),

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
