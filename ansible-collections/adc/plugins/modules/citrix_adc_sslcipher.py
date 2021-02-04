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
module: citrix_adc_sslcipher
short_description: Manage custom SSL ciphers
description:
    - Manage custom SSL ciphers
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.1.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    ciphergroupname:
        description:
            - >-
                Name for the user-defined cipher group. Must begin with an ASCII alphanumeric or underscore (_)
                and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),
                (=), and hyphen (-) characters. Cannot be changed after the cipher group is created.
            - "The following requirement applies only to the Citrix ADC CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                "my ciphergroup" or 'my ciphergroup').
            - "Minimum length =  1"
        type: str


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup cipher
  delegate_to: localhost
  citrix_adc_sslcipher:
    nsip: 10.79.22.22
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    ciphergroupname: test_cipher
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
            'sslcipher': {
                'attributes_list': [
                    'ciphergroupname',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'ciphergroupname',
                ],
                'delete_id_attributes': [
                    'ciphergroupname',
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
        self.calculate_configured_cipher()

    def calculate_configured_cipher(self):
        log('ModuleExecutor.calculate_configured_cipher()')
        self.configured_cipher = {}
        for attribute in self.attribute_config['sslcipher']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['sslcipher']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_cipher[attribute] = value

        log('calculated configured sslcipher %s' % self.configured_cipher)

    def cipher_exists(self):
        log('ModuleExecutor.cipher_exists()')
        result = self.fetcher.get('sslcipher', self.module.params['ciphergroupname'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 258:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        # Fallthrough
        return True

    def create_cipher(self):
        log('ModuleExecutor.create_cipher()')

        post_data = {
            'sslcipher': self.configured_cipher
        }

        result = self.fetcher.post(post_data=post_data, resource='sslcipher')
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

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # sslcipher only valid attribute is its ciphergroupname
        # It either exists or not. ugdate is not sensible
        if not self.cipher_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('cipher does not exist. Will create.')
                self.create_cipher()
        else:
            self.module_result['changed'] = False

    def delete_cipher(self):
        log('ModuleExecutor.delete_cipher()')

        result = self.fetcher.delete(
            resource='sslcipher',
            id=self.module.params['ciphergroupname'],
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

        if self.cipher_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_cipher()

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
        ciphergroupname=dict(type='str'),

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
