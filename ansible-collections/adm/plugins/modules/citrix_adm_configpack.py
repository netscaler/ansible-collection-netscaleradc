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
module: citrix_adm_configpack
short_description: Manage configpacks on Citrix ADM.
description:
    - Manage configpacks on Citrix ADM.
    - Note that due to limitations on the underlying NITRO API an update is always forced when I(state=present).

version_added: "1.0.0"

author:
    - Sumanth Lingappa (@sumanth-lingappa)

options:

    stylebook:
        description:
            - "The stylebook to be used for the configpack."
        type: dict

    parameters:
        description:
            - "The parameters to be used for the configpack."
        type: dict

    targets:
        description:
            - "The targets to which the configpack is to be applied."
        type: list

    instances_username:
        description:
            - "Target instances username. Required when when `Prompt Credentials for instance Login` is enabled in ADM System Configuration"
        type: str

    instances_password:
        description:
            - "Target instances password. Required when when `Prompt Credentials for instance Login` is enabled in ADM System Configuration"
        type: str

    change_stylebook:
        description:
            - 'true' if stylebook needs to be changed. Defaults to 'false'
        type: bool
        default: true

    old_stylebook:
        description:
            - "The old stylebook to which configpack was associated before the upgrade"
            - "This dictionary should be present if `change_stylebook` is true.
        type: dict

    check_create:
        description:
            - Check if the configpack was created on the target citrix adm.
            - Return the created configpack in the module results.
        type: bool
        default: true

    check_create_delay:
        description:
            - Time in seconds to wait between the create/update operation and retrieval of the created configpack.
            - This delay should be non zero as the newly created/updated configpack might not be immediately available to be fetched by the target Citrix ADM.
        type: int
        default: 10

extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
    - name: Login to ADM Service
      delegate_to: localhost
      register: login_result
      citrix_adm_login:
        adm_ip: "{{ adm_host }}"
        is_cloud: true
        id: "{{ client_id }}"
        secret: "{{ client_secret }}"

    - name: Get NS instance
      delegate_to: localhost
      register: ns_facts
      citrix_adm_ns_facts:
        adm_ip: "{{ adm_host }}"
        is_cloud: true
        nitro_auth_token: "{{ login_result.session_id }}"
        validate_certs: "{{ validate_certs }}"

        ip_address: "{{ instance_ip }}"

    - name: Add a configpack
      delegate_to: localhost
      register: configpack_result
      citrix_adm_configpack:
        adm_ip: "{{ adm_host }}"
        is_cloud: true
        nitro_auth_token: "{{ login_result.session_id }}"
        validate_certs: "{{ validate_certs }}"

        state: present

        check_create: true
        check_create_delay: 10
        change_stylebook: false
        old_stylebook: # This will be considered only if `change_stylebook` is true
          name: basic-lb-config-via-ansible
          namespace: com.example.stylebooks
          version: "0.1"

        parameters:
          ip: 192.199.19.1
          lb-alg: ROUNDROBIN
          name: integration_test_application
          svc-port: "80"
          svc-servers:
            - 192.199.19.3
        targets:
          - id: '{{ ns_facts.ns[0].id }}'
        stylebook:
          name: basic-lb-config-via-ansible
          namespace: com.example.stylebooks
          version: "0.1"
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

configpack:
    description: Dictionary containing all the attributes of the created configpack
    returned: success
    type: dict
'''

import codecs
import time

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible_collections.citrix.adm.plugins.module_utils.citrix_adm import netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'configpack'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'configpack': {
                'attributes_list': [
                    'parameters',
                    'stylebook',
                    'targets',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                ],
                'delete_id_attributes': [
                ],
            },

        }

        # Process HTTP headers
        self.http_headers = {}
        self.http_headers['Content-Type'] = 'application/json'

        nitro_auth_token = self.module.params.get('nitro_auth_token')
        if nitro_auth_token is not None:
            self.http_headers['Cookie'] = "SESSID=%s" % nitro_auth_token

        nitro_user = self.module.params.get('nitro_user')
        if nitro_user is not None:
            self.http_headers['X-NITRO-USER'] = nitro_user

        nitro_pass = self.module.params.get('nitro_pass')
        if nitro_pass is not None:
            self.http_headers['X-NITRO-PASS'] = nitro_pass

        instances_password = self.module.params.get('instances_password')
        if instances_password is not None:
            self.http_headers['X-INSTANCES-PASSWORD'] = instances_password

        instances_username = self.module.params.get('instances_username')
        if instances_username is not None:
            self.http_headers['X-INSTANCES-USERNAME'] = instances_username

        # Prepare module result
        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def _parse_response_body(self, r):
        if r is not None:
            http_response_body = codecs.decode(r.read(), 'utf-8')
            log('http_response_body %s' % http_response_body)
            try:
                data = self.module.from_json(http_response_body)
                log('data %s' % data)
            except ValueError:
                data = {}
                log('Cannot parse response data')
        return data

    def get_configpack(self, stylebook):
        if self.module.params.get('is_cloud'):
            url = '%s://%s/stylebook/nitro/v2/config/configpacks' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
            )
        else:
            url = '%s://%s/stylebook/nitro/v1/config/stylebooks/%s/%s/%s/configpacks' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                stylebook['namespace'],
                stylebook['version'],
                stylebook['name'],
            )

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            method='GET',
        )
        log('GET info: %s' % info)

        # Anything but a 200 is an error
        status = info.get('status')
        http_msg = info.get('msg')
        if status in {404}: # no configpack found
            return None

        if status != 200:
            msg = 'HTTP status %s, msg: %s' % (status, http_msg)
            self.module.fail_json(msg=msg, **self.module_result)

        if r is not None:
            http_response_body = codecs.decode(r.read(), 'utf-8')
            log('http_response_body %s' % http_response_body)
            try:
                data = self.module.from_json(http_response_body)
                log('data %s' % data)
            except ValueError:
                data = {}
                self.module.fail_json(msg='Cannot parse GET http response data', **self.module_result)

            # Parse data to get configpack object
            configpack_list = data.get('configpacks')
            if not isinstance(configpack_list, list):
                self.module.fail_json(msg='GET body does not contain configpack data', **self.module_result)

            if len(configpack_list) == 0:
                return None
            else:
                if self.module.params.get('is_cloud'):
                    return self.get_relevant_configpack_adm_service(configpack_list, stylebook)
                else:
                    return self.get_relevant_configpack_adm_onprem(configpack_list, stylebook)
        else:
            self.module.fail_json(msg='GET response does not have a body', **self.module_result)


    def get_relevant_configpack_adm_onprem(self, configpack_list, stylebook):
        # Get the relevant configpack object from the many configpacks returned by the GET
        # compare each configpack object with the attributes `stylebook` and `targets`
        log('get_relevant_configpack_adm_onprem')
        for configpack in configpack_list:
            if configpack['name'] == stylebook['name'] and \
                configpack['namespace'] == stylebook['namespace'] and \
                    configpack['version'] == stylebook['version']:
                if _compare_two_targets(configpack.get('targets'), self.module.params.get('targets')):
                    return configpack
        return None

    def get_relevant_configpack_adm_service(self, configpack_list, stylebook):
        # Get the relevant configpack object from the many configpacks returned by the GET
        # compare each configpack object with the attributes `stylebook` and `targets`
        log('get_relevant_configpack_adm_service')
        for configpack in configpack_list:
            if configpack.get('stylebook') == stylebook:
                if _compare_two_targets(configpack.get('targets'), self.module.params.get('targets')):
                    return configpack
        return None

    def construct_request_data(self):
        data_dict = {}
        for attribute in self.attribute_config['configpack']['attributes_list']:
            attr_val = self.module.params.get(attribute)
            if attr_val is not None:
                data_dict[attribute] = attr_val

        ret_val = {'configpack': data_dict}
        return ret_val

    def post_configpack(self):
        log('post_configpack')
        request_data = self.construct_request_data()
        payload = '%s' % self.module.jsonify(request_data)

        log('request data %s' % request_data)
        log('payload %s' % payload)

        if self.module.params.get('is_cloud'):
            url = '%s://%s/stylebook/nitro/v2/config/configpacks' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
            )
        else:
            url = '%s://%s/stylebook/nitro/v1/config/stylebooks/%s/%s/%s/configpacks' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                self.module.params['stylebook']['namespace'],
                self.module.params['stylebook']['version'],
                self.module.params['stylebook']['name'],
            )

        log('url %s' % url)

        log('headers %s' % self.http_headers)
        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=payload,
            method='POST',
        )

        log('POST info: %s' % info)

        data = self._parse_response_body(r)
        nitro_errorcode = data.get('errorcode')

        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        if status not in {200, 201, 202}:
            log('Fail due to status')
            msg = 'HTTP status fail status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            log('Fail due to nitro_errorcode')
            log('nitro error code %s %s' % (type(nitro_errorcode), nitro_errorcode))
            msg = 'nitro_errorcode fail HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

    def upgrade_configpack(self, configpack):
        log('upgrade_configpack')
        configpack_id = configpack.get('id')

        if configpack_id is None:
            self.module.fail_json('Cannot change stylebook for configpack without id', **self.module_result)

        if self.module.params.get('is_cloud'):
            request_data = {
                "upgrade": {
                    "configpack_ids": [
                        configpack_id
                    ],
                    "stylebook": {
                        "name": self.module.params['stylebook']['name'],
                        "namespace": self.module.params['stylebook']['namespace'],
                        "version": self.module.params['stylebook']['version'],
                    }
                }
            }
        else:
            request_data = {
                "upgrade": {
                    "configpacks": [
                        configpack_id
                    ],
                    "stylebook": {
                        "name": self.module.params['stylebook']['name'],
                        "namespace": self.module.params['stylebook']['namespace'],
                        "version": self.module.params['stylebook']['version'],
                    }
                }
            }
        payload = '%s' % self.module.jsonify(request_data)

        log('request data %s' % request_data)
        log('payload %s' % payload)

        if self.module.params.get('is_cloud'):
            url = '%s://%s/stylebook/nitro/v2/config/configpacks/actions/upgrade' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
            )
        else:
            url = '%s://%s/stylebook/nitro/v1/config/configpacks/actions/upgrade' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
            )

        log('url %s' % url)

        log('headers %s' % self.http_headers)
        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=payload,
            method='POST',
        )

        log('POST info: %s' % info)

        data = self._parse_response_body(r)
        nitro_errorcode = data.get('errorcode')

        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        if status not in {200, 201, 202}:
            log('Fail due to status')
            msg = 'HTTP status fail status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            log('Fail due to nitro_errorcode')
            log('nitro error code %s %s' % (type(nitro_errorcode), nitro_errorcode))
            msg = 'nitro_errorcode fail HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

    def put_configpack(self, configpack):
        log('put_configpack')
        request_data = self.construct_request_data()
        payload = '%s' % self.module.jsonify(request_data)

        log('request data %s' % request_data)
        log('payload %s' % payload)

        configpack_id = configpack.get('id')
        if configpack_id is None:
            self.module.fail_json('Cannot update configpack without id', **self.module_result)

        if self.module.params.get('is_cloud'):
            url = '%s://%s/stylebook/nitro/v2/config/configpacks/%s' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                configpack_id,
            )
        else:
            url = '%s://%s/stylebook/nitro/v1/config/stylebooks/%s/%s/%s/configpacks/%s' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                self.module.params['stylebook']['namespace'],
                self.module.params['stylebook']['version'],
                self.module.params['stylebook']['name'],
                configpack_id,
            )

        log('url %s' % url)
        log('headers %s' % self.http_headers)

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=payload,
            method='PUT',
        )

        log('PUT info: %s' % info)

        data = self._parse_response_body(r)

        nitro_errorcode = data.get('errorcode')

        # Anything but a 200 is an error
        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        if status not in {200, 201, 202}:
            msg = 'HTTP status fail status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            msg = 'nitro_errorcode fail. HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        else:
            # Check for idempotency. That is if the PUT call has modified any configuration or not.
            try:
                if data['message'] == 'No change in configuration':
                    self.module_result['changed'] = False
            except KeyError as e:
                log("KeyError: %s" % e)


    def delete_configpack(self, configpack):
        log('delete_configpack')

        configpack_id = configpack.get('id')
        if configpack_id is None:
            self.module.fail_json('Cannot delete configpack without id', **self.module_result)

        if self.module.params.get('is_cloud'):
            url = '%s://%s/stylebook/nitro/v2/config/configpacks/%s' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                configpack_id,
            )
        else:
            url = '%s://%s/stylebook/nitro/v1/config/stylebooks/%s/%s/%s/configpacks/%s' % (
                self.module.params['nitro_protocol'],
                self.module.params['nsip'],
                self.module.params['stylebook']['namespace'],
                self.module.params['stylebook']['version'],
                self.module.params['stylebook']['name'],
                configpack_id,
            )

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            method='DELETE',
        )

        log('DELETE info: %s' % info)

        data = self._parse_response_body(r)
        nitro_errorcode = data.get('errorcode')

        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        # Anything but a 200 is an error
        if status not in {200, 201, 202}:
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)


    def input_validation(self):
        # if `instances_username` is present, then `instances_password` should also be present and vice-versa
        if 'instances_username' in self.module.params and 'instances_password' not in self.module.params:
            msg = 'ERROR: Invalid Input: `instances_password` should be present when `instances_username` attribute is present'
            self.module.fail_json(msg=msg, **self.module_result)

        if 'instances_password' in self.module.params and 'instances_username' not in self.module.params:
            msg = 'ERROR: Invalid Input: `instances_username` should be present when `instances_password` attribute is present'
            self.module.fail_json(msg=msg, **self.module_result)

        # old_configpack dictionary to be present when change_stylebook is present
        if self.module.params['change_stylebook'] is True:
            if 'old_stylebook' not in self.module.params:
                msg = 'ERROR: Invalid Input: `old_stylebook` should be present when `change_stylebook` attribute is true'
                self.module.fail_json(msg=msg, **self.module_result)
            else:
                # even if old_stylebook is present, it should contain `namespace`, `name` and `version`
                if not all(key in self.module.params['old_stylebook'] for key in ('namespace', 'name', 'version')):
                    msg = 'ERROR: Invalid Input: `old_stylebook` must contain `namespace`, `name` and `version` values'
                    self.module.fail_json(msg=msg, **self.module_result)


    def main(self):
        try:
            self.input_validation()
            stylebook = self.module.params['stylebook']
            if self.module.params['change_stylebook'] is True:
                old_stylebook = self.module.params['old_stylebook']
                configpack = self.get_configpack(old_stylebook)
                if configpack is None:
                    msg = 'ERROR: Invalid Input: if `change_stylebook` is true, then the configpack should be associated with `old_stylebook`. TIP: If you are not upgrading your stylebook, change `change_stylebook` to false.'
                    self.module.fail_json(msg=msg, **self.module_result)
            else:
                configpack = self.get_configpack(stylebook)

            log('existing configpack %s' % configpack)
            if self.module.params['state'] == 'present':
                self.module_result['changed'] = True
                if configpack is None:
                    self.post_configpack()
                elif self.module.params['change_stylebook'] is True:
                    self.upgrade_configpack(configpack)
                else:
                    self.put_configpack(configpack)

                # Return the created/updated configpack in the module results
                if self.module.params['check_create']:
                    time.sleep(self.module.params['check_create_delay'])
                    created_configpack = self.get_configpack(stylebook)
                    if created_configpack is None:
                        self.module.fail_json(msg='Failed to create configpack', **self.module_result)
                    else:
                        self.module_result.update(dict(configpack=created_configpack))

            elif self.module.params['state'] == 'absent':
                if configpack is not None:
                    self.module_result['changed'] = True
                    self.delete_configpack(configpack=configpack)

            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def _compare_two_targets(existing_targets, params_targets):
    # We need to compare the existing targets with the params targets and return True if they match.
    # Existing targets' dictionary is 'instance_id' and 'instance_ip'
    # Params targets' dictionary is 'id'
    if len(existing_targets) != len(params_targets):
        return False
    for et in existing_targets:
        for params_target in params_targets:
            if et.get('instance_id') == params_target.get('id'):
                return True
    return False

def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        stylebook=dict(type='dict'),
        old_stylebook=dict(type='dict'),
        parameters=dict(type='dict'),
        targets=dict(type='list'),
        check_create=dict(type='bool', default=True),
        change_stylebook=dict(type='bool', default=False),
        check_create_delay=dict(type='int', default=10),
        instances_username=dict(
            type='str',
            no_log=True
        ),
        instances_password=dict(
            type='str',
            no_log=True
        ),
    )

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
