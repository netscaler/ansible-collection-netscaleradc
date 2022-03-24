#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Citrix Systems, Inc.
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
module: citrix_adm_provision_vpx
short_description: Provision a VPX.
description:
    - Provision a VPX through the ADM provisioning service.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    poll_interval:
        description:
            - Time interval in seconds between job poll operation.
        type: int
        default: 10

    fail_on_stall:
        description:
            - Boolean flag. Set to true for the module to fail when a status of job stalled is reported.
        type: bool
        default: true

    provisioning_profile:
        description:
            - "Provisioning profile"
        type: dict
        suboptions:
            name:
                description:
                    - Name of the ProvisioningProfile.
            instance_type:
                description:
                    - Only NetScaler is supported as of now
            site_id:
                description:
                    - Reference to MAS site which has location info where instance has to be provisioned.
            type:
                description:
                    - Platform type
            deployment_details:
                description:
                    - Deployment details
                type: dict
                suboptions:
                    target:
                        description:
                            - IP of managed SDX where Citrix ADC is going to be provisioned.
                    nitro:
                        description:
                            - Payload to create ADC instance which is to be sent to SDX.
            mas_registration_details:
                description:
                    - MAS registration details
                type: dict
                suboptions:
                    mas_agent_id:
                        description:
                            - Reference to MAS Agent that has to be used in order to add and manage provisioned instance in MAS.
                    access_profile_id:
                        description:
                            - Reference to Instance/Device Access Profile to be set for instance being provisioned.


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
- name: Provision vpx
  delegate_to: localhost
  citrix.adm.citrix_adm_provision_vpx:
    nitro_protocol: https
    nsip: railay.adm.cloud.com
    customer_id: "{{ customer_id }}"
    is_cloud: true
    bearer_token: "{{ login_result.access_token }}"

    state: present

    provisioning_profile:
        instance_type: "NetScaler"
        name: "{{ vpx_name }}"
        type: sdx
        site_id: "cfa47930-f3f6-475f-9780-da93699f01cf"
        mas_registration_details:
            mas_agent_id: "12ea1595-9161-4f56-b1c7-bc953ced6e9e"
        instance_capacity_details:
            config_job_templates:
                - "c4a977d1-5633-03e6-961f-eb4e99a93f85"
        deployment_details:
            sdx:
                target: 10.222.74.135
                nitro:
                    name: "{{ vpx_name }}"
                    ip_address: "{{ ipaddress }}"
                    config_type: 0
                    ipv4_address: "{{ ipaddress }}"
                    netmask: 255.255.255.192
                    gateway: 10.222.74.129
                    nexthop: ""
                    image_name: NSVPX-XEN-13.1-17.42_nc_64.xva
                    profile_name: nsroot_Notnsroot250
                    sync_operation: "false"
                    throughput_allocation_mode: "0"
                    throughput: "1000"
                    max_burst_throughput: "0"
                    burst_priority: "0"
                    license: Standard
                    number_of_acu: 0
                    number_of_scu: "0"
                    vm_memory_total: "2048"
                    pps: "1000000"
                    number_of_cores: "0"
                    l2_enabled: "false"
                    if_0_1: "true"
                    vlan_id_0_1: ""
                    if_0_2: "true"
                    vlan_id_0_2: ""
                    network_interfaces:
                      - port_name: LA/1
                        mac_address: ""
                        mac_mode: default
                        device_channel_name: ""
                        receiveuntagged: "true"
                        vlan_whitelist_array:
                          - "110"
                    nsvlan_id: ""
                    vlan_type: 1
                    nsvlan_tagged: "false"
                    nsvlan_interfaces: []
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
mps_datacenter:
    description: Facts about the named datacenter or empty if not exists.
    returned: success
    type: dict
'''

import copy
import codecs
import base64
import time

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adm.plugins.module_utils.citrix_adm import (
    NitroAPIFetcher,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines
)
from ansible.module_utils.urls import fetch_url


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        customer_id = self.module.params.get('customer_id')
        if customer_id is not None:
            api_path = 'massvc/%s/provisioning/nitro/v1/config' % customer_id
            self.nitro_api_fetcher = NitroAPIFetcher(module, api_path=api_path)
        else:
            self.nitro_api_fetcher = NitroAPIFetcher(module)

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def profile_exists(self):
        log('ModuleExecutor.profile_exists()')
        result = self.nitro_api_fetcher.get(
            resource="provisioning_profiles",
        )
        log('get result %s' % result)
        if result['http_response_data']['status'] == 200:
            for profile in result['data']['provisioning_profiles']:
                if profile['name'] == self.module.params['provisioning_profile']['name']:
                    return True
            # Fallthrough
            return False
        else:
            raise Exception('http response code is %s' % result['http_response_data']['status'])

    def create_provisioning_profile(self):
        log('ModuleExecutor.create_provisioning_profile()')
        payload = {'provisioning_profiles': self.module.params['provisioning_profile']}
        log('create profile payload is %s' % payload)

        result = self.nitro_api_fetcher.post(post_data=payload, resource='provisioning_profiles')

        log('create profile post result: %s' % result)
        if result['http_response_data']['status'] not in (200, 201):
            raise Exception('http response code is %s' % result['http_response_data']['status'])

        self.provisioning_profile_id = result['data']['provisioning_profiles'][0]['id']
        log("Provisioning profile id %s" % self.provisioning_profile_id)
        self.post_instance()

    def post_instance(self):
        log('ModuleExecutor.post_instance()')
        payload = {'instances': {
            'name': self.module.params['provisioning_profile']['name'],
            'provisioning_profile_id': self.provisioning_profile_id,
        }}

        result = self.nitro_api_fetcher.post(
            post_data=payload,
            resource='instances'
        )
        if result['http_response_data']['status'] != 200:
            raise Exception('http response code is %s' % result['http_response_data']['status'])
        self.job_id = result['data']['instance']['job_id']

        self.poll_job_id()

    def poll_job_id(self):
        log('ModuleExecutor.poll_job_id()')

        while(True):
            result = self.nitro_api_fetcher.get(
                resource='jobs',
                id=self.job_id,
            )
            log('job poll result: %s' % result)

            if result['http_response_data']['status'] != 200:
                raise Exception('http response code is %s' % result['http_response_data']['status'])

            job_status = result['data']['job']['status']

            if job_status == 'failed':
                raise Exception('job failed')

            if job_status == 'completed':
                log('Job completed')
                return

            if job_status == 'stalled':
                if self.module.params['fail_on_stall']:
                    raise Exception('Job stalled')
                else:
                    log('Job stalled')
                    break

            if job_status == 'inprogress':
                log('Job in progress')

            time.sleep(self.module.params['poll_interval'])

    def provision_vpx(self):
        log('ModuleExecutor.provision_vpx()')

        self.create_provisioning_profile()
        self.post_instance()
        self.poll_job_id()

    def delete_vpx(self):
        log('ModuleExecutor.delete_vpx()')
        # Delete is a noop since deletion of provisioning profiles
        # is not supported on ADM service as of this writing

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                if not self.profile_exists():
                    self.module_result['changed'] = True
                    if not self.module.check_mode:
                        self.provision_vpx()

            elif self.module.params['state'] == 'absent':
                if self.profile_exists():
                    self.module_result['changed'] = True
                    if not self.module.check_mode:
                        self.delete_vpx()

            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        provisioning_profile=dict(
            type='dict'
        ),
        fail_on_stall=dict(
            type='bool',
            default=True,
        ),
        poll_interval=dict(
            type='int',
            default=10,
        )
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
