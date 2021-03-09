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
module: citrix_adc_dnsnsrec
short_description: Configuration for name server record resource.
description:
    - Configuration for name server record resource.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.1.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    domain:
        description:
            - "Domain name."
            - "Minimum length =  1"
        type: str

    nameserver:
        description:
            - "Host name of the name server to add to the domain."
            - "Minimum length =  1"
        type: str

    ttl:
        description:
            - >-
                Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached
                DNS proxies. The specified TTL is applied to all the resource records that are of the same record
                and belong to the specified domain name. For example, if you add an address record, with a TTL of
                to the domain name example.com, the TTLs of all the address records of example.com are changed to
                If the TTL is not specified, the Citrix ADC uses either the DNS zone's minimum TTL or, if the SOA
                is not available on the appliance, the default value of 3600.
            - "Minimum value = C(0)"
            - "Maximum value = C(2147483647)"
        type: int


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup dnsnsrec
  delegate_to: localhost
  citrix_adc_dnsnsrec:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 10.78.22.44

    domain: test.com
    nameserver: 10.3.3.4
    ttl: 1111
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

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'dnsnsrec': {
                'attributes_list': [
                    'domain',
                    'nameserver',
                    'ttl',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'domain',
                ],
                'delete_id_attributes': [
                    'domain',
                    'nameserver',
                    'ecssubnet',
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
        self.calculate_configured_dnsnsrec()

    def calculate_configured_dnsnsrec(self):
        log('ModuleExecutor.calculate_configured_dnsnsrec()')
        self.configured_dnsnsrec = {}
        for attribute in self.attribute_config['dnsnsrec']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['dnsnsrec']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_dnsnsrec[attribute] = value

        log('calculated configured dnsnsrec %s' % self.configured_dnsnsrec)

    def dnsnsrec_exists(self):
        log('ModuleExecutor.dnsnsrec_exists()')
        result = self.fetcher.get('dnsnsrec')

        log('get result %s' % result)
        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Sort though the bound ciphers for cipheraliasname match
        for dnsnsrec in result['data'].get('dnsnsrec', []):
            match = all(
                (
                    dnsnsrec['domain'] == self.configured_dnsnsrec['domain'],
                    dnsnsrec['nameserver'] == self.configured_dnsnsrec['nameserver']
                )
            )
            if match:
                return True

        # Fallthrough
        return False

    def create_dnsnsrec(self):
        log('ModuleExecutor.create_dnsnsrec()')

        post_data = {
            'dnsnsrec': self.configured_dnsnsrec
        }

        result = self.fetcher.post(post_data=post_data, resource='dnsnsrec')
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

    def update_dnsnsrec(self):
        log('ModuleExecutor.update_dnsnsrec()')

        self.delete_dnsnsrec()
        self.create_dnsnsrec()

    def dnsnsrec_identical(self):
        log('ModuleExecutor.dnsnsrec_identical()')
        result = self.fetcher.get('dnsnsrec')
        retrieved_dnsnsrecs = result['data'].get('dnsnsrec', [])

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        # Iterate over keys that already exist in the playbook
        for retrieved_record in retrieved_dnsnsrecs:

            # Skip irrelevant ciphers
            match = all(
                (
                    retrieved_record['domain'] == self.configured_dnsnsrec['domain'],
                    retrieved_record['nameserver'] == self.configured_dnsnsrec['nameserver']
                )
            )
            if not match:
                continue

            for attribute in self.configured_dnsnsrec.keys():
                retrieved_value = retrieved_record.get(attribute)
                configured_value = self.configured_dnsnsrec.get(attribute)
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
        if not self.dnsnsrec_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('dnsnsrec does not exist. Will create.')
                self.create_dnsnsrec()
        else:
            if not self.dnsnsrec_identical():
                log('Existing dnsnsrec does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_dnsnsrec()
            else:
                log('Existing dnsnsrec has identical values to configured.')

    def delete_dnsnsrec(self):
        log('ModuleExecutor.delete_dnsnsrec()')

        args = {
            'nameserver': self.configured_dnsnsrec.get('nameserver')
        }
        result = self.fetcher.delete(
            resource='dnsnsrec',
            id=self.module.params['domain'],
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

        if self.dnsnsrec_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_dnsnsrec()

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
        domain=dict(type='str'),
        nameserver=dict(type='str'),
        ttl=dict(type='int'),

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
