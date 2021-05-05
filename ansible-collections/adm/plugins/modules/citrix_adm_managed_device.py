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
module: citrix_adm_managed_device
short_description: Manage Citrix ADM ADC instances.
description:
    - Manage Citrix ADM ADC instances.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    instance_classifier:
        description:
            - "Value based on which certain features may be enabled/disabled in ADM for the instance."
        type: int

    hostname:
        description:
            - "Assign hostname to managed device, if this is not provided, name will be set as host name ."
            - " Minimum length =  1"
            - " Maximum length =  256"
        type: str

    std_bw_config:
        description:
            - "Standard Bandwidth running."
        type: int

    gateway_deployment:
        description:
            - "Is this device acting as Gateway.."
        type: bool

    gateway_ipv6:
        description:
            - "Gateway IPv6 Address."
        type: str

    instance_available:
        description:
            - "Instance license available."
        type: int

    device_finger_print:
        description:
            - "Fingerprint/thumb-print from UMS public certificate for SSL communication."
        type: str

    name:
        description:
            - "Name of managed device."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    ent_bw_available:
        description:
            - "Enterprise Bandwidth configured."
        type: int

    description:
        description:
            - "Description of managed device."
            - " Minimum length =  1"
            - " Maximum length =  512"
        type: str

    is_autoscale_group:
        description:
            - "Does this device belong to an Autoscale Group.."
        type: bool

    geo_support:
        description:
            - "Is this device configured to support GEO location.."
        type: bool

    sslvpn_config:
        description:
            - "sslvpn license maximum."
        type: int

    mastools_version:
        description:
            - "Mastools version if the device is embedded agent."
        type: str

    sysservices:
        description:
            - "System Services."
        type: str

    ent_bw_total:
        description:
            - "Enterprise Bandwidth Total."
        type: int

    vcpu_config:
        description:
            - "Number of vCPU allocated for the device."
        type: int

    netmask:
        description:
            - "Netmask of managed device."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    autoprovisioned:
        description:
            - "Device is auto-provisioned or not."
        type: bool

    ent_bw_config:
        description:
            - "Enterprise Bandwidth configured."
        type: int

    datacenter_id:
        description:
            - "Datacenter Id is system generated key for data center."
        type: str

    instance_config:
        description:
            - "Instance license running."
        type: int

    is_managed:
        description:
            - "Is Managed."
        type: bool

    discovery_time:
        description:
            - "discovery time."
        type: str

    instance_mode:
        description:
            - "Denotes state- primary,secondary,clip,clusternode."
        type: str

    instance_total:
        description:
            - "Instance license."
        type: int

    is_ha_configured:
        description:
            - "Is HA configured."
        type: bool

    trust_id:
        description:
            - "Device ID obtained from trust service."
        type: str

    ipv4_address:
        description:
            - "IPv4 Address."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    profile_name:
        description:
            - "Device Profile Name that is attached with this managed device."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    std_bw_available:
        description:
            - "Standard Bandwidth Available."
        type: int

    servicepackage:
        description:
            - "Service Package Name of the device."
        type: str

    last_updated_time:
        description:
            - "Last Updated Time."
        type: str

    plt_bw_total:
        description:
            - "Total Platinum Bandwidth."
        type: int

    id:
        description:
            - "Id is system generated key for all the managed devices."
        type: str

    mgmt_ip_address:
        description:
            - "Management IP Address for this Managed Device."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    ipv6_address:
        description:
            - "IPv6 Address."
        type: str

    partition_id:
        description:
            - "ID of admin partition."
        type: str

    license_edition:
        description:
            - "Edition of instance."
        type: str

    plt_bw_available:
        description:
            - "Platinum Bandwidth Available."
        type: int

    device_family:
        description:
            - "Device Family."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    template_interval:
        description:
            - "Template refresh interval."
        type: int

    type:
        description:
            - "Type of device, (Xen | NS)."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    gateway:
        description:
            - "Default Gateway of managed device."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    internal_annotation:
        description:
            - "Internal annotation used by ADM.Example, if a device is marked for delete."
        type: str

    config_type:
        description:
            - "Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both."
            - " Maximum value =  "
        type: int

    node_id:
        description:
            - "Node identification of a device."
        type: str

    isolation_policy:
        description:
            - "Isolation Policy of the Device."
        type: str

    ip_address:
        description:
            - "IP Address for this managed device."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    provision_request_id:
        description:
            - "Value is set only if the instance was provisioned from Citrix ADM."
        type: str

    httpxforwardedfor:
        description:
            - "HTTP x-Forwardedfor header flag.."
            - " Minimum length =  1"
            - " Maximum length =  10"
        type: str

    std_bw_total:
        description:
            - "Standard Bandwidth."
        type: int

    display_name:
        description:
            - "Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    plt_bw_config:
        description:
            - "Platinum Bandwidth configured."
        type: int

    partition_name:
        description:
            - "Citrix ADC Admin Partition Name."
            - " Maximum length =  512"
        type: str

    agent_id:
        description:
            - "Agent Id."
        type: str

    sslvpn_total:
        description:
            - "sslvpn license."
        type: int

    peer_device_ip:
        description:
            - "Peer Device IP address for instance of type BLX ADC.."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    profile_password:
        description:
            - "Password specified by the user for this Citrix ADC Instance.."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    file_name:
        description:
            - "File name which contains comma separated instances to be  discovered."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    profile_username:
        description:
            - "User Name specified by the user for this Citrix ADC Instance.."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    file_location_path:
        description:
            - "File Location on Client for upload/download."
            - " Minimum length =  1"
        type: str

    peer_host_device_ip:
        description:
            - "Peer Host Device IP Address for instance of type BLX ADC.."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    device_host_ip:
        description:
            - "Device Host IP Address for instance of type BLX ADC.."
            - " Minimum length =  1"
            - " Maximum length =  64"
        type: str

    tr_task_id:
        description:
            - "Task Id used by Triton to identify NS."
        type: str

    entity_tag:
        description:
            - "Array of tag_name and tag_value pair assocaited with an entity."
        type: list
        elements: dict


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
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

managed_device:
    description: Dictionary containing the attributes of the created ADC instance
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
        self.main_nitro_class = 'managed_device'
        self.fetcher = NitroAPIFetcher(module)

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'managed_device': {
                'attributes_list': [
                    'instance_classifier',
                    'hostname',
                    'std_bw_config',
                    'gateway_deployment',
                    'gateway_ipv6',
                    'instance_available',
                    'device_finger_print',
                    'name',
                    'ent_bw_available',
                    'description',
                    'is_autoscale_group',
                    'geo_support',
                    'sslvpn_config',
                    'mastools_version',
                    'sysservices',
                    'ent_bw_total',
                    'vcpu_config',
                    'netmask',
                    'autoprovisioned',
                    'ent_bw_config',
                    'datacenter_id',
                    'instance_config',
                    'is_managed',
                    'discovery_time',
                    'instance_mode',
                    'instance_total',
                    'is_ha_configured',
                    'trust_id',
                    'ipv4_address',
                    'profile_name',
                    'std_bw_available',
                    'servicepackage',
                    'last_updated_time',
                    'plt_bw_total',
                    'id',
                    'mgmt_ip_address',
                    'ipv6_address',
                    'partition_id',
                    'license_edition',
                    'plt_bw_available',
                    'device_family',
                    'template_interval',
                    'type',
                    'gateway',
                    'internal_annotation',
                    'config_type',
                    'node_id',
                    'isolation_policy',
                    'ip_address',
                    'provision_request_id',
                    'httpxforwardedfor',
                    'std_bw_total',
                    'display_name',
                    'plt_bw_config',
                    'partition_name',
                    'agent_id',
                    'sslvpn_total',
                    'peer_device_ip',
                    'profile_password',
                    'file_name',
                    'profile_username',
                    'file_location_path',
                    'peer_host_device_ip',
                    'device_host_ip',
                    'tr_task_id',
                    'entity_tag',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'ip_address',
                ],
                'delete_id_attributes': [
                ],
            },

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )
        self.calculate_configured_managed_device()
        self.fetch_managed_device()

    def calculate_configured_managed_device(self):
        log('ModuleExecutor.calculate_configured_managed_device()')
        self.configured_managed_device = {}
        for attribute in self.attribute_config['managed_device']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['managed_device']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_managed_device[attribute] = value

        log('calculated configured managed_device %s' % self.configured_managed_device)

    def fetch_managed_device(self):
        log('ModuleExecutor.fetch_managed_device()')
        self.fetched_managed_device = {}

        # The following fetch will always succeed
        # The result will be an array of all existing managed devices
        result = self.fetcher.get('managed_device')
        log('get result %s' % result)

        for managed_device in result['data']['managed_device']:
            match = True
            for get_id_attribute in self.attribute_config['managed_device']['get_id_attributes']:
                fetched_value = managed_device.get(get_id_attribute)
                configured_value = self.configured_managed_device.get(get_id_attribute)
                # Do not compare if it is not defined
                if configured_value is None:
                    continue
                # Emulate AND between get_id_attributes
                if configured_value != fetched_value:
                    match = False
            if match:
                self.fetched_managed_device = managed_device

        log('fetched managed device %s' % self.fetched_managed_device)


    def managed_device_exists(self):
        log('ModuleExecutor.managed_device_exists()')

        if self.fetched_managed_device == {}:
            return False
        else:
            return True

    def managed_device_identical(self):
        log('ModuleExecutor.managed_device_identical()')
        is_identical = True

        # Compare simple attributes
        for attribute in self.configured_managed_device:
            configured_value = self.configured_managed_device.get(attribute)
            fetched_value = self.fetched_managed_device.get(attribute)
            if configured_value != fetched_value:
                is_identical = False
                str_tuple = (attribute, type(configured_value), configured_value, type(fetched_value), fetched_value)
                log('Attribute %s differs. configured: (%s) %s  fetched: (%s) %s' % str_tuple)

        return is_identical

    def create_managed_device(self):
        log('ModuleExecutor.create_managed_device()')

        post_data = {
            'managed_device': self.configured_managed_device,
        }

        log('post data: %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='managed_device', action='add_device')

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

    def update_managed_device(self):
        log('ModuleExecutor.update_managed_device()')

        put_payload = self.configured_managed_device

        put_data = {
            'managed_device': put_payload
        }

        log('request put data: %s' % put_data)

        id = self.fetched_managed_device['id']
        result = self.fetcher.put(put_data=put_data, resource='managed_device', id=id)

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

    def delete_managed_device(self):
        log('ModuleExecutor.delete_managed_device()')

        id = self.fetched_managed_device['id']

        result = self.fetcher.delete(resource='managed_device', id=id)
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

        if not self.managed_device_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.create_managed_device()
        else:
            if not self.managed_device_identical():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_managed_device()

        # Update with managed device key
        self.fetch_managed_device()
        self.module_result['managed_device'] = self.fetched_managed_device


    def delete(self):
        log('ModuleExecutor.delete()')

        if self.managed_device_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_managed_device()

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
        instance_classifier=dict(
            type='int'
        ),
        hostname=dict(
            type='str'
        ),
        std_bw_config=dict(
            type='int'
        ),
        gateway_deployment=dict(
            type='bool'
        ),
        gateway_ipv6=dict(
            type='str'
        ),
        instance_available=dict(
            type='int'
        ),
        device_finger_print=dict(
            type='str'
        ),
        name=dict(
            type='str'
        ),
        ent_bw_available=dict(
            type='int'
        ),
        description=dict(
            type='str'
        ),
        is_autoscale_group=dict(
            type='bool'
        ),
        geo_support=dict(
            type='bool'
        ),
        sslvpn_config=dict(
            type='int'
        ),
        mastools_version=dict(
            type='str'
        ),
        sysservices=dict(
            type='str'
        ),
        ent_bw_total=dict(
            type='int'
        ),
        vcpu_config=dict(
            type='int'
        ),
        netmask=dict(
            type='str'
        ),
        autoprovisioned=dict(
            type='bool'
        ),
        ent_bw_config=dict(
            type='int'
        ),
        datacenter_id=dict(
            type='str'
        ),
        instance_config=dict(
            type='int'
        ),
        is_managed=dict(
            type='bool'
        ),
        discovery_time=dict(
            type='str'
        ),
        instance_mode=dict(
            type='str'
        ),
        instance_total=dict(
            type='int'
        ),
        is_ha_configured=dict(
            type='bool'
        ),
        trust_id=dict(
            type='str'
        ),
        ipv4_address=dict(
            type='str'
        ),
        profile_name=dict(
            type='str'
        ),
        std_bw_available=dict(
            type='int'
        ),
        servicepackage=dict(
            type='str'
        ),
        last_updated_time=dict(
            type='str'
        ),
        plt_bw_total=dict(
            type='int'
        ),
        id=dict(
            type='str'
        ),
        mgmt_ip_address=dict(
            type='str'
        ),
        ipv6_address=dict(
            type='str'
        ),
        partition_id=dict(
            type='str'
        ),
        license_edition=dict(
            type='str'
        ),
        plt_bw_available=dict(
            type='int'
        ),
        device_family=dict(
            type='str'
        ),
        template_interval=dict(
            type='int'
        ),
        type=dict(
            type='str'
        ),
        gateway=dict(
            type='str'
        ),
        internal_annotation=dict(
            type='str'
        ),
        config_type=dict(
            type='int'
        ),
        node_id=dict(
            type='str'
        ),
        isolation_policy=dict(
            type='str'
        ),
        ip_address=dict(
            type='str'
        ),
        provision_request_id=dict(
            type='str'
        ),
        httpxforwardedfor=dict(
            type='str'
        ),
        std_bw_total=dict(
            type='int'
        ),
        display_name=dict(
            type='str'
        ),
        plt_bw_config=dict(
            type='int'
        ),
        partition_name=dict(
            type='str'
        ),
        agent_id=dict(
            type='str'
        ),
        sslvpn_total=dict(
            type='int'
        ),
        peer_device_ip=dict(
            type='str'
        ),
        profile_password=dict(
            type='str'
        ),
        file_name=dict(
            type='str'
        ),
        profile_username=dict(
            type='str'
        ),
        file_location_path=dict(
            type='str'
        ),
        peer_host_device_ip=dict(
            type='str'
        ),
        device_host_ip=dict(
            type='str'
        ),
        tr_task_id=dict(
            type='str'
        ),
        entity_tag=dict(
            type='list',
            elements='dict'
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
