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
module: citrix_adc_system_file
short_description: Upload systemfile to ADC
description:
    - Upload systemfile to ADC

version_added: "1.1.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    filename:
        description:
            - "Name of the file. It should not include filepath."
            - "Maximum length =  63"
        type: str

    filecontent:
        description:
            - "file content in Base64 format."
        type: str

    filelocation:
        description:
            - "location of the file on Citrix ADC."
            - "Maximum length =  127"
        type: str

    fileencoding:
        description:
            - "encoding type of the file content."
        type: str


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup file
  delegate_to: localhost
  citrix.adc.citrix_adc_system_file:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 10.78.33.22

    state: present

    filelocation: /var/tmp
    filename: testfile.txt
    filecontent: "Some file content"
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

import base64
import codecs
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

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'systemfile': {
                'attributes_list': [
                    'filename',
                    'filecontent',
                    'filelocation',
                    'fileencoding',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                ],
                'delete_id_attributes': [
                    'filename',
                    'filelocation',
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
        self.calculate_configured_systemfile()

    def calculate_configured_systemfile(self):
        log('ModuleExecutor.calculate_configured_systemfile()')
        self.configured_systemfile = {}
        for attribute in self.attribute_config['systemfile']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['systemfile']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_systemfile[attribute] = value

        log('calculated configured systemfile %s' % self.configured_systemfile)

    def systemfile_exists(self):
        log('ModuleExecutor.systemfile_exists()')
        args = {}
        args['filename'] = self.module.params['filename']
        args['filelocation'] = self.module.params['filelocation']
        result = self.fetcher.get('systemfile', args=args)

        log('get result %s' % result)

        # File does not exist
        if result['nitro_errorcode'] == 3441:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Fallthrough

        # Save retrieved file contents for systemfile_identical()
        self.retrieved_systemfile = result['data']['systemfile'][0]

        return True

    def create_systemfile(self):
        log('ModuleExecutor.create_systemfile()')

        post_data = copy.deepcopy(self.configured_systemfile)
        post_data['filecontent'] = codecs.decode(base64.b64encode(codecs.encode(post_data['filecontent'])))
        post_data = {
            'systemfile': post_data,
        }

        result = self.fetcher.post(post_data=post_data, resource='systemfile')
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

    def update_systemfile(self):
        log('ModuleExecutor.update_systemfile()')

        self.delete_systemfile()
        self.create_systemfile()

    def systemfile_identical(self):
        log('ModuleExecutor.systemfile_identical()')

        diff_list = []

        # Only the filecontents is considered for equality
        # systemfile_exists has already tested filelocation and filename for equality to be true
        bytes_received = codecs.encode(self.retrieved_systemfile['filecontent'])
        retrieved_filecontent = codecs.decode(base64.b64decode(bytes_received))
        configured_filecontent = self.configured_systemfile['filecontent']

        if retrieved_filecontent != configured_filecontent:
            str_tuple = (
                'filecontent',
                type(configured_filecontent),
                configured_filecontent,
                type(retrieved_filecontent),
                retrieved_filecontent,
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
        if not self.systemfile_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('systemfile does not exist. Will create.')
                self.create_systemfile()
        else:
            if not self.systemfile_identical():
                log('Existing systemfile does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_systemfile()
            else:
                log('Existing systemfile has identical values to configured.')

    def delete_systemfile(self):
        log('ModuleExecutor.delete_systemfile()')

        args = {
            'filename': self.configured_systemfile['filename'],
            'filelocation': self.configured_systemfile['filelocation'],
        }
        result = self.fetcher.delete(
            resource='systemfile',
            args=args,
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

        if self.systemfile_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_systemfile()

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
        filename=dict(type='str'),
        filecontent=dict(type='str'),
        filelocation=dict(type='str'),
        fileencoding=dict(type='str'),

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
