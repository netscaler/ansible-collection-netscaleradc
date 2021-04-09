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
module: citrix_adm_rba_policy
short_description: Manage Citrix ADM rba policies.
description:
    - Manage Citrix ADM rba policies.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    tenant_id:
        description:
            - "Tenant Id of the RBA roles."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    statement:
        description:
            - "RBA statement."
        type: list
        elements: dict

    ui:
        description:
            - "RBA for UI components."
        type: list
        elements: dict

    name:
        description:
            - "Policy Name."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    id:
        description:
            - "Id is system generated key for all the system policys."
        type: str

    description:
        description:
            - "Description of Policy."
            - "Minimum length = 1"
            - "Maximum length = 1024"
        type: str


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
- name: Setup appfw policy
  delegate_to: localhost
  citrix.adm.citrix_adm_rba_policy:
    adm_ip: 192.168.1.1
    nitro_auth_token: "{{ login_result.session_id }}"

    state: present

    name: test_policy
    description: some description
    tenant_id: "0ea1d85a-06b8-4225-9fc8-5a7065fdd590"
    statement:
      - access_type: "true"
        operation_name: add
        parent_name: rba_policy
        resource_type: ns_gslbservice
    ui:
      - access_type: "true"
        display_name: ""
        name: ContentSwitching
        parent_name: rba_policy
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

rba_policy:
    description: Dictionary containing the attributes of the created rba_policy
    returned: success
    type: dict

'''

import copy

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
        self.main_nitro_class = 'rba_policy'
        self.fetcher = NitroAPIFetcher(module)

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'rba_policy': {
                'attributes_list': [
                    'tenant_id',
                    'statement',
                    'ui',
                    'name',
                    'id',
                    'description',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                    'id',
                ],
                'delete_id_attributes': [
                    'name',
                    'id',
                ],
            },

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )
        self.calculate_configured_rba_policy()
        self.fetch_rba_policy()

    def calculate_configured_rba_policy(self):
        log('ModuleExecutor.calculate_configured_rba_policy()')
        self.configured_rba_policy = {}
        for attribute in self.attribute_config['rba_policy']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['rba_policy']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_rba_policy[attribute] = value

        log('calculated configured rba_policy %s' % self.configured_rba_policy)

    def fetch_rba_policy(self):
        log('ModuleExecutor.fetch_rba_policy()')
        self.fetched_rba_policy = {}

        # The following fetch will always succeed
        # The result will be an array of all existing rba_policies
        result = self.fetcher.get('rba_policy')
        log('get result %s' % result)

        for rba_policy in result['data']['rba_policy']:
            match = True
            for get_id_attribute in self.attribute_config['rba_policy']['get_id_attributes']:
                fetched_value = rba_policy.get(get_id_attribute)
                configured_value = self.configured_rba_policy.get(get_id_attribute)
                # Do not compare if it is not defined
                if configured_value is None:
                    continue
                # Emulate AND between get_id_attributes
                if configured_value != fetched_value:
                    match = False
            if match:
                self.fetched_rba_policy = rba_policy

        log('fetched rba_policy %s' % self.fetched_rba_policy)


    def rba_policy_exists(self):
        log('ModuleExecutor.rba_policy_exists()')

        if self.fetched_rba_policy == {}:
            return False
        else:
            return True

    def element_in_fetched(self, item, fetched):
        # task configured item keys drive the comparison
        log('ModuleExecutor.element_in_fetched()')
        for fetched_item in fetched:
            identical = True
            for attribute in item:
                item_value = item.get(attribute)
                fetched_value = fetched_item.get(attribute)
                if item_value != fetched_value:
                    str_tuple = (attribute, type(item_value), item_value, type(fetched_value), fetched_value)
                    # Message is too verbose for normal use
                    # Leaving it commented here for debugging when needed
                    # log('fetched item differs %s item: (%s) %s fetched: (%s) %s' % str_tuple)
                    identical = False
                    break
            if identical:
                return True
        # Fallthrough

        return False

    def element_in_configured(self, item, configured):
        # task configured list item keys drive the comparison
        log('ModuleExecutor.element_in_configured()')

        for configured_item in configured:
            identical = True
            for attribute in configured_item:
                item_value = item.get(attribute)
                configured_value = configured_item.get(attribute)
                if item_value != configured_value:
                    str_tuple = (attribute, type(item_value), item_value, type(configured_value), configured_value)
                    # Message is too verbose for normal use
                    # Leaving it commented here for debugging when needed
                    # log('configured item differs %s item: (%s) %s configured: (%s) %s' % str_tuple)
                    identical = False
                    break
            if identical:
                return True
        # Fallthrough

        return False

    def rba_policy_identical(self):
        log('ModuleExecutor.rba_policy_identical()')
        is_identical = True

        # Compare simple attributes
        for attribute in self.configured_rba_policy:
            if attribute in ['ui', 'statement']:
                continue
            configured_value = self.configured_rba_policy.get(attribute)
            fetched_value = self.fetched_rba_policy.get(attribute)
            if configured_value != fetched_value:
                is_identical = False
                str_tuple = (attribute, type(configured_value), configured_value, type(fetched_value), fetched_value)
                log('Attribute %s differs. configured: (%s) %s  fetched: (%s) %s' % str_tuple)

        # Compare ui and statement elements
        for item in self.configured_rba_policy['ui']:
            if not self.element_in_fetched(item, self.fetched_rba_policy['ui']):
                log('ui element not found in fetched %s' % item)
                is_identical = False

        for item in self.configured_rba_policy['statement']:
            if not self.element_in_fetched(item, self.fetched_rba_policy['statement']):
                log('statement element not found in fetched %s' % item)
                is_identical = False

        for item in self.fetched_rba_policy['ui']:
            if not self.element_in_configured(item, self.configured_rba_policy['ui']):
                log('ui element not found in configured %s' % item)
                is_identical = False

        for item in self.fetched_rba_policy['statement']:
            if not self.element_in_configured(item, self.configured_rba_policy['statement']):
                log('statement element not found in configured %s' % item)
                is_identical = False

        return is_identical

    def create_rba_policy(self):
        log('ModuleExecutor.create_rba_policy()')

        post_data = {
            'rba_policy': self.configured_rba_policy
        }

        log('post data: %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='rba_policy')

        log('result of post: %s' % result)

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
            msg = 'Did not get nitro errorcode and http status was not 200 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def update_rba_policy(self):
        log('ModuleExecutor.update_rba_policy()')

        put_payload = self.configured_rba_policy

        put_data = {
            'rba_policy': put_payload
        }

        log('request put data: %s' % put_data)

        id = self.fetched_rba_policy['id']
        result = self.fetcher.put(put_data=put_data, resource='rba_policy', id=id)

        log('result of put: %s' % result)

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
            msg = 'Did not get nitro errorcode and http status was not 200 or 4xx (%s)' % result['http_response_data']['status']

    def delete_rba_policy(self):
        log('ModuleExecutor.delete_rba_policy()')

        id = self.fetched_rba_policy['id']

        result = self.fetcher.delete(resource='rba_policy', id=id)
        log('delete result %s' % result)

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
            msg = 'Did not get nitro errorcode and http status was not 200 or 4xx (%s)' % result['http_response_data']['status']

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        if not self.rba_policy_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.create_rba_policy()
        else:
            if not self.rba_policy_identical():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_rba_policy()

        # Update with rba_policy key
        self.fetch_rba_policy()
        self.module_result['rba_policy'] = self.fetched_rba_policy


    def delete(self):
        log('ModuleExecutor.delete()')

        if self.rba_policy_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_rba_policy()

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
        tenant_id=dict(
            type='str'
        ),
        statement=dict(
            type='list',
            elements='dict'
        ),
        ui=dict(
            type='list',
            elements='dict'
        ),
        name=dict(
            type='str'
        ),
        id=dict(
            type='str'
        ),
        description=dict(
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
