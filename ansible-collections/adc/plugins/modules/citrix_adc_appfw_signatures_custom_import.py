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
module: citrix_adc_appfw_signatures_custom_import
short_description: Import custom Application Firewall signatures
description:
    - Import custom Application Firewall signatures.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.

version_added: "1.2.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - "Name of the signature object."
            - "Minimum length =  1"
            - "Maximum length =  31"
        type: str

    src:
        description:
            - >-
                URL (protocol, host, path, and file name) for the location at which to store the imported signatures
            - >-
                NOTE: The import fails if the object to be imported is on an HTTPS server that requires client
                authentication for access.
            - "Minimum length =  1"
            - "Maximum length =  2047"
        type: str

    xslt:
        description:
            - "XSLT file source."
            - "Maximum length =  2047"
        type: str

    xslt_builtin:
        description:
            - "Built-in XSLT file source."
        type: str

    enable_all:
        description:
            - "Enable all rules in signature file"
        type: bool

    log_all:
        description:
            - "Enable log for all rules in signature file"
        type: bool

    block_all:
        description:
            - "Disable all rules in signature file"
        type: bool

    stats_all:
        description:
            - "Enable stats for all rules in signature file"
        type: bool

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: setup appfw custom signatures 
  delegate_to: localhost
  register: result
  citrix_adc_appfw_signatures_custom_import:
    nitro_user: '{{ nitro_user }}'
    nitro_pass: '{{ nitro_pass }}'
    nsip: '{{ nsip }}'
    validate_certs: '{{ validate_certs }}'

    state: present 

    name: "custom_signatures"
    src: "local:Scan_Report_ctrx8pb_20200109.xml"
    xslt: "local:scan_Qualys_cloud_2_42_3.xsl"

    enable_all: true
    block_all: true
    log_all: true
    stats_all: false
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
'''

import copy
import tempfile
import os.path
import codecs
import base64
import shutil
import xml.etree.ElementTree as ET
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
        self.main_nitro_class = 'service'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'appfwsignatures': {
                'attributes_list': [
                    'name',
                    'src',
                    'xslt',
                    'xslt_builtin',
                ],
                'transforms': {},
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'name',
                ],
                'non_updateable_attributes': [],
            },
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.init_tmp_dir()
        self.calculate_configured_signatures()

        self.local_native_signatures = os.path.join(self.tmp_dir, self.configured_signatures['name'])

    def calculate_configured_signatures(self):
        log('ModuleExecutor.calculate_configured_signatures()')
        self.configured_signatures = {}
        for attribute in self.attribute_config['appfwsignatures']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['appfwsignatures']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_signatures[attribute] = value

        self.use_builtin_xslt = self.configured_signatures.get('xslt_builtin') is not None

        log('calculated configured appfwsignatures %s' % self.configured_signatures)

    def init_tmp_dir(self):
        log('ModuleExecutor.init_tmp_dir()')
        self.tmp_dir = tempfile.mkdtemp(prefix='appfw_signatures_custom_import_')
        log('tmp dir is %s' % self.tmp_dir)

    def cleanup_tmp_dir(self):
        log('ModuleExecutor.cleanup_tmp_dir()')

        shutil.rmtree(self.tmp_dir)


    def signatures_exists(self):
        log('ModuleExecutor.signatures_exists()')
        result = self.fetcher.get('appfwsignatures', self.module.params['name'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            return True
        elif result['nitro_errorcode'] == 3380:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def _download_file(self, remote_path, local_path):
        log('ModuleExecutor._download_file()')
        log('remote_path %s' % remote_path)
        log('local_path %s' % local_path)
        args = {}
        args['filename'] = os.path.basename(remote_path)
        args['filelocation'] = os.path.dirname(remote_path)
        result = self.fetcher.get('systemfile', args=args)

        log('get result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        bytes_received = codecs.encode(result['data']['systemfile'][0]['filecontent'])
        retrieved_filecontent = codecs.decode(base64.b64decode(bytes_received))
        with open(local_path, 'w') as fh:
            fh.write(retrieved_filecontent)

    def _ensure_remote_file_delete(self, remote_path):
        log('ModuleExecutor._ensure_remote_file_delete()')

        args = {}
        args['filename'] = os.path.basename(remote_path)
        args['filelocation'] = os.path.dirname(remote_path)
        result = self.fetcher.get('systemfile', args=args)

        log('get result %s' % result)

        # File does not exist
        if result['nitro_errorcode'] == 3441:
            return
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Fallthrough

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

    def _upload_file(self, local_path, remote_path):
        log('ModuleExecutor._upload_file()')

        self._ensure_remote_file_delete(remote_path)

        with open(local_path, 'r') as fh:
            file_data = fh.read()
        
        post_data = {
            'systemfile': {
                'filelocation': os.path.dirname(remote_path),
                'filename': os.path.basename(remote_path),
                'filecontent': codecs.decode(base64.b64encode(codecs.encode(file_data))),
            }
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

    def copy_builtin_xslt_to_vartmp(self):
        log('ModuleExecutor.copy_builtin_xslt_to_vartmp()')

        remote_path = os.path.join(
            '/',
            'netscaler',
            'scan_%s.xsl' % self.configured_signatures['xslt_builtin'],
        )

        local_path = os.path.join(
            self.tmp_dir,
            'scan_%s.xsl' % self.configured_signatures['xslt_builtin'],
        )

        self._download_file(remote_path, local_path)
        vartmp_remote_path = os.path.join(
            '/var/tmp',
            'scan_%s.xsl' % self.configured_signatures['xslt_builtin'],
        )
        self._upload_file(local_path, vartmp_remote_path)

    def download_native_singatures_file(self):
        log('ModuleExecutor.download_native_singatures_file()')
        remote_path = os.path.join('/var/download/custom', self.configured_signatures['name'])
        local_path = self.local_native_signatures
        if os.path.exists(local_path):
            return

        # Fallthrough to download

        self._download_file(
            remote_path=remote_path,
            local_path=local_path
        )

    def process_native_signatures_file(self):
        log('ModuleExecutor.process_native_signatures_file()')

        tree = ET.parse(self.local_native_signatures)
        root = tree.getroot()

        for rule in root.findall('./Signatures/SignatureRule'):
            self.process_enabled(rule)
            self.process_actions(rule)

        tree.write(self.local_native_signatures, encoding='UTF-8', xml_declaration=True)

    def process_enabled(self, rule):
        log('ModuleExecutor.process_enabled()')
        want_enabled = self._rule_want_enabled(rule)
        if want_enabled:
            rule.attrib['enabled'] = 'ON'
        else:
            if 'enabled' in rule.attrib:
                del rule.attrib['enabled']

    def process_actions(self, rule):
        log('ModuleExecutor.process_actions()')
        desired_actions = self._desired_actions_string(rule)
        if desired_actions != rule.attrib['actions']:
            rule.attrib['actions'] = desired_actions


    def initial_create_signatures(self):
        log('ModuleExecutor.initial_create_signatures()')

        post_data = {
            'name': self.configured_signatures['name'],
            'src': self.configured_signatures['src'],
            'preservedefactions': False,
        }

        if self.use_builtin_xslt:
            post_data['xslt'] = 'local:scan_%s.xsl' % self.configured_signatures['xslt_builtin']
        else:
            post_data['xslt'] = self.configured_signatures['xslt']

        log('post_data: %s' % post_data)
        self._do_import_action(post_data)


    def _do_import_action(self, post_data):
        log('ModuleExecutor._do_import_action()')

        post_data = { 'appfwsignatures': post_data }

        result = self.fetcher.post(
            resource='appfwsignatures?action=Import',
            post_data=post_data,
            #action='Import',
        )
        if result['http_response_data']['status'] == 200:
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
            raise Exception('Did not get nitro errorcode and http status was not 200 or 4xx (%s)' % result['http_response_data']['status'])

    def _do_update_action(self, post_data):
        log('ModuleExecutor._do_update_action()')

        post_data = { 'appfwsignatures': post_data }

        result = self.fetcher.post(
            resource='appfwsignatures',
            post_data=post_data,
            action='update',
        )
        if result['http_response_data']['status'] == 200:
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
            raise Exception('Did not get nitro errorcode and http status was not 200 or 4xx (%s)' % result['http_response_data']['status'])

    def create_signatures(self):
        log('ModuleExecutor.create_signatures()')

        if self.use_builtin_xslt:
            self.copy_builtin_xslt_to_vartmp()

        self.initial_create_signatures()

        self.update_signatures()

    def update_signatures(self):
        log('ModuleExecutor.update_signatures()')

        self.download_native_singatures_file()

        self.process_native_signatures_file()

        self.upload_and_update_native_signatures_file()

    def upload_and_update_native_signatures_file(self):
        log('ModuleExecutor.upload_and_update_native_signatures_file()')

        local_path = self.local_native_signatures

        native_signatures_filename = os.path.basename(self.local_native_signatures)
        remote_path = os.path.join('/var/tmp', native_signatures_filename)

        self._upload_file(local_path, remote_path)

        post_data = {
            'name': self.configured_signatures['name'],
            'src': 'local:%s' % native_signatures_filename,
            'overwrite': 'true',
        }

        self._do_import_action(post_data)

        post_data = {
            'name': self.configured_signatures['name'],
        }

        self._do_update_action(post_data)

    def signatures_identical(self):
        log('ModuleExecutor.signatures_identical()')

        self.download_native_singatures_file()

        tree = ET.parse(self.local_native_signatures)
        root = tree.getroot()

        for rule in root.findall('./Signatures/SignatureRule'):
            is_enabled = self._rule_is_enabled(rule) 
            if is_enabled and not self._rule_want_enabled(rule):
                return False
            if not is_enabled and self._rule_want_enabled(rule):
                return False
            desired_actions = self._desired_actions_string(rule)
            if desired_actions != rule.attrib['actions']:
                return False

        # Fallthrough

        return True


    def _rule_is_enabled(self, rule):
        if 'enabled' not in rule.attrib:
            return False
        if rule.attrib['enabled'] != 'ON':
            return False

        # Fallthrough

        return True

    def _rule_want_enabled(self, rule):
        enable_all = self.module.params.get('enable_all')
        if enable_all is not None and enable_all:
            return True

        return False

    def _desired_actions_string(self, rule):
        actions = []
        block_all = self.module.params.get('block_all')
        if block_all is not None and block_all:
            actions.append('block')

        log_all = self.module.params.get('log_all')
        if log_all is not None and log_all:
            actions.append('log')

        stats_all = self.module.params.get('stats_all')
        if stats_all is not None and stats_all:
            actions.append('stats')

        return ','.join(actions)



    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.signatures_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('Signatures do not exist. Will create.')
                self.create_signatures()
        else:
            if not self.signatures_identical():
                log('Existing signatures do not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_signatures()
            else:
                log('Existing signatures have identical values to configured.')

    def delete_signatures(self):
        log('ModuleExecutor.delete_signatures()')

        result = self.fetcher.delete(resource='appfwsignatures', id=self.module.params['name'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.signatures_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_signatures()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
            elif self.module.params['state'] == 'absent':
                self.delete()

            self.cleanup_tmp_dir()
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
        name=dict(type='str'),
        src=dict(type='str'),
        xslt=dict(type='str'),
        xslt_builtin=dict(type='str'),
        enable_all=dict(type='bool'),
        block_all=dict(type='bool'),
        log_all=dict(type='bool'),
        stats_all=dict(type='bool'),
    )

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[
            ('enable_all', 'disable_all'),
            ('block_all', 'unblock_all'),
            ('log_all', 'nolog_all'),
            ('stats_all', 'nostats_all'),
        ]
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
