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
module: citrix_adc_nspartition
short_description: Manage Citrix ADC partitions
description:
    - Manage Citrix ADC partitions

version_added: "1.2.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    partitionname:
        description:
            - >-
                Name of the Partition. Must begin with an ASCII alphanumeric or underscore (_) character, and must
                only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and
                (-) characters.
            - "Minimum length =  1"
        type: str

    maxbandwidth:
        description:
            - >-
                Maximum bandwidth, in Kbps, that the partition can consume. A zero value indicates the bandwidth is
                on the partition and it can consume up to the system limits.
        type: str

    minbandwidth:
        description:
            - >-
                Minimum bandwidth, in Kbps, that the partition can consume. A zero value indicates the bandwidth is
                on the partition and it can consume up to the system limits.
        type: str

    maxconn:
        description:
            - >-
                Maximum number of concurrent connections that can be open in the partition. A zero value indicates no
                on number of open connections.
        type: str

    maxmemlimit:
        description:
            - >-
                Maximum memory, in megabytes, allocated to the partition. A zero value indicates the memory is
                on the partition and it can consume up to the system limits.
            - "Minimum value = C(0)"
            - "Maximum value = C(1048576)"
        type: str

    partitionmac:
        description:
            - >-
                Special MAC address for the partition which is used for communication over shared vlans in this
                If not specified, the MAC address is auto-generated.
        type: str


    switch_partition:
        description:
            - When set to C(true) the module will perform the switch partition operation
        type: bool

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup partition
  delegate_to: localhost
  citrix_adc_nspartition:
    nsip: 10.74.22.22
    nitro_user: nsroot
    nitro_pass: secret

    state: present

    partitionname: par1
    maxbandwidth: 10240
    switch_partition: yes
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
            'nspartition': {
                'attributes_list': [
                    'partitionname',
                    'maxbandwidth',
                    'minbandwidth',
                    'maxconn',
                    'maxmemlimit',
                    'partitionmac',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'partitionname',
                ],
                'delete_id_attributes': [
                    'partitionname',
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
        self.calculate_configured_nspartition()

    def calculate_configured_nspartition(self):
        log('ModuleExecutor.calculate_configured_nspartition()')
        self.configured_nspartition = {}
        for attribute in self.attribute_config['nspartition']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['nspartition']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_nspartition[attribute] = value

        log('calculated configured nspartition %s' % self.configured_nspartition)

    def nspartition_exists(self):
        log('ModuleExecutor.nspartition_exists()')

        result = self.fetcher.get('nspartition', id=self.module.params['partitionname'])

        log('get result %s' % result)

        # nspartition does not exist
        if result['nitro_errorcode'] == 2755:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Fallthrough

        # Save retrieved nspartition contents for nspartition_identical()
        self.retrieved_nspartition = result['data']['nspartition'][0]

        return True

    def create_nspartition(self):
        log('ModuleExecutor.create_nspartition()')

        post_data = copy.deepcopy(self.configured_nspartition)

        post_data = {
            'nspartition': post_data
        }

        result = self.fetcher.post(post_data=post_data, resource='nspartition')
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

    def update_nspartition(self):
        log('ModuleExecutor.update_nspartition()')

        # Catching trying to change non updateable attributes is done in self.nspartition_identical()
        put_payload = copy.deepcopy(self.configured_nspartition)
        for attribute in self.attribute_config['nspartition']['non_updateable_attributes']:
            if attribute in put_payload:
                del put_payload[attribute]

        put_data = {
            'nspartition': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='nspartition')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def nspartition_identical(self):
        log('ModuleExecutor.nspartition_identical()')

        diff_list = []
        non_updateable_list = []
        for attribute in self.configured_nspartition.keys():
            retrieved_value = self.retrieved_nspartition.get(attribute)
            configured_value = self.configured_nspartition.get(attribute)
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
                entry = 'Attribute "%s" differs. Playbook parameter: "%s". Retrieved NITRO object: "%s"' % (attribute, configured_value, retrieved_value)
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['nspartition']['non_updateable_attributes']:
                    non_updateable_list.append(attribute)

        self.module_result['diff_list'] = diff_list
        if non_updateable_list != []:
            msg = 'Cannot change value for the following non updateable attributes %s' % non_updateable_list
            self.module.fail_json(msg=msg, **self.module_result)

        if diff_list != []:
            return False
        else:
            return True

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.nspartition_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('nspartition does not exist. Will create.')
                self.create_nspartition()
        else:
            if not self.nspartition_identical():
                log('Existing nspartition does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_nspartition()
            else:
                log('Existing nspartition has identical values to configured.')

    def delete_nspartition(self):
        log('ModuleExecutor.delete_nspartition()')

        result = self.fetcher.delete(
            resource='nspartition',
            id=self.module.params['partitionname'],
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

        if self.nspartition_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_nspartition()

    def switch_partition(self):
        log('ModuleExecutor.switch_partition')

        post_data = {
            'nspartition':{
                'partitionname': self.module.params['partitionname'],
            }
        }

        result = self.fetcher.post(post_data=post_data, resource='nspartition', action='Switch')

        if result['http_response_data']['status'] != 200:
            msg = 'Switch partition operation failed'
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
                if self.module.params.get('switch_partition', False):
                    self.switch_partition()
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
        partitionname=dict(type='str'),
        maxbandwidth=dict(type='str'),
        minbandwidth=dict(type='str'),
        maxconn=dict(type='str'),
        maxmemlimit=dict(type='str'),
        partitionmac=dict(type='str'),

        switch_partition=dict(
            type='bool',
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
