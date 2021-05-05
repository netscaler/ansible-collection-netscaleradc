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
module: citrix_adm_ns_device_profile
short_description: Manage Citrix ADM ADC instances.
description:
    - Manage Citrix ADM ADC instances.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - "Profile Name."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    svm_ns_comm:
        description:
            - "Communication protocol (http or https) with Instances."
            - " Minimum length =  1"
            - " Maximum length =  10"
        type: str

    use_global_setting_for_communication_with_ns:
        description:
            - "True, if the communication with Instance needs to be global and not device specific."
        type: bool

    id:
        description:
            - "Id is system generated key for all the device profiles."
        type: str

    type:
        description:
            - >-
                Profile Type, This must be with in specified supported instance types:
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    snmpsecurityname:
        description:
            - "SNMP v3 security name for this profile."
            - " Maximum length =  31"
        type: str

    snmpauthprotocol:
        description:
            - "SNMP v3 auth protocol for this profile."
        type: str

    ssl_private_key:
        description:
            - "SSL Private Key for key based authentication."
        type: str

    ssl_cert:
        description:
            - "SSL Certificate for certificate based authentication."
        type: str

    http_port:
        description:
            - "HTTP port to connect to the device."
        type: str

    ns_profile_name:
        description:
            - "Profile Name, This is one of the already created Citrix ADC profiles."
        type: str

    ssh_port:
        description:
            - "SSH port to connect to the device."
        type: str

    password:
        description:
            - "Instance credentials.Password for this profile."
            - " Minimum length =  1"
            - " Maximum length =  127"
            - "This attribute cannot be updated. Delete and recreate the profile instead."
        type: str

    snmpsecuritylevel:
        description:
            - "SNMP v3 security level for this profile."
        type: str

    snmpcommunity:
        description:
            - "SNMP community for this profile."
            - " Maximum length =  31"
        type: str

    passphrase:
        description:
            - "Passphrase with which private key is encrypted."
            - "This attribute cannot be updated. Delete and recreate the profile instead."
        type: str

    snmpprivprotocol:
        description:
            - "SNMP v3 priv protocol for this profile."
        type: str

    https_port:
        description:
            - "HTTPS port to connect to the device."
        type: str

    username:
        description:
            - "Instance credentials.Username provided in the profile will be used to contact the instance."
            - " Minimum length =  1"
            - " Maximum length =  127"
        type: str

    host_password:
        description:
            - "Host Password for this profile.Used for BLX form factor of ADC."
            - " Minimum length =  1"
            - " Maximum length =  127"
            - "This attribute cannot be updated. Delete and recreate the profile instead."
        type: str

    max_wait_time_reboot:
        description:
            - "Max waiting time to reboot Citrix ADC."
        type: str

    snmpprivpassword:
        description:
            - "SNMP v3 priv password for this profile."
            - " Minimum length =  8"
            - " Maximum length =  31"
            - "This attribute cannot be updated. Delete and recreate the profile instead."
        type: str

    snmpversion:
        description:
            - "SNMP version for this profile."
        type: str

    cb_profile_name:
        description:
            - "Profile Name, This is one of the already created Citrix SD-WAN profiles."
        type: str

    snmpauthpassword:
        description:
            - "SNMP v3 auth password for this profile."
            - " Minimum length =  8"
            - " Maximum length =  31"
            - "This attribute cannot be updated. Delete and recreate the profile instead."
        type: str

    host_username:
        description:
            - "Host User Name for this profile.Used for BLX form factor of ADC."
            - " Minimum length =  1"
            - " Maximum length =  127"
        type: str


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
citrix_adm_ns_device_profile:
  adm_ip: 10.222.74.111
  adm_user: nsroot
  adm_pass: nsroot

  state: present

  name: ansible_profile
  username: nsroot
  password: password1234
  host_password: otherpassword
  http_port: 9080
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

ns_device_profile:
    description: Dictionary containing the attributes of the created profile
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
        self.main_nitro_class = 'ns_device_profile'
        self.fetcher = NitroAPIFetcher(module)

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'ns_device_profile': {
                'attributes_list': [
                    'name',
                    'svm_ns_comm',
                    'use_global_setting_for_communication_with_ns',
                    'id',
                    'type',
                    'snmpsecurityname',
                    'snmpauthprotocol',
                    'ssl_private_key',
                    'ssl_cert',
                    'http_port',
                    'ns_profile_name',
                    'ssh_port',
                    'password',
                    'snmpsecuritylevel',
                    'snmpcommunity',
                    'passphrase',
                    'snmpprivprotocol',
                    'https_port',
                    'username',
                    'host_password',
                    'max_wait_time_reboot',
                    'snmpprivpassword',
                    'snmpversion',
                    'cb_profile_name',
                    'snmpauthpassword',
                    'host_username',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
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
        self.calculate_configured_ns_device_profile()
        self.fetch_ns_device_profile()

    def calculate_configured_ns_device_profile(self):
        log('ModuleExecutor.calculate_configured_ns_device_profile()')
        self.configured_ns_device_profile = {}
        for attribute in self.attribute_config['ns_device_profile']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['ns_device_profile']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_ns_device_profile[attribute] = value

        log('calculated configured ns_device_profile %s' % self.configured_ns_device_profile)

    def fetch_ns_device_profile(self):
        log('ModuleExecutor.fetch_ns_device_profile()')
        self.fetched_ns_device_profile = {}

        # The following fetch will always succeed
        # The result will be an array of all existing profiles
        result = self.fetcher.get('ns_device_profile')
        log('get result %s' % result)

        for ns_device_profile in result['data']['ns_device_profile']:
            match = True
            for get_id_attribute in self.attribute_config['ns_device_profile']['get_id_attributes']:
                fetched_value = ns_device_profile.get(get_id_attribute)
                configured_value = self.configured_ns_device_profile.get(get_id_attribute)
                # Do not compare if it is not defined
                if configured_value is None:
                    continue
                # Emulate AND between get_id_attributes
                if configured_value != fetched_value:
                    match = False
            if match:
                self.fetched_ns_device_profile = ns_device_profile

        log('fetched ns_device_profile device %s' % self.fetched_ns_device_profile)


    def ns_device_profile_exists(self):
        log('ModuleExecutor.ns_device_profile_exists()')

        if self.fetched_ns_device_profile == {}:
            return False
        else:
            return True

    def ns_device_profile_identical(self):
        log('ModuleExecutor.ns_device_profile_identical()')
        is_identical = True

        # Compare simple attributes
        skip_attributes = [
            'password',
            'host_password',
            'passphrase',
            'snmpprivpassword',
            'snmpauthpassword',
        ]
        for attribute in self.configured_ns_device_profile:
            if attribute in skip_attributes:
                continue
            configured_value = self.configured_ns_device_profile.get(attribute)
            fetched_value = self.fetched_ns_device_profile.get(attribute)
            if configured_value != fetched_value:
                is_identical = False
                str_tuple = (attribute, type(configured_value), configured_value, type(fetched_value), fetched_value)
                log('Attribute %s differs. configured: (%s) %s  fetched: (%s) %s' % str_tuple)

        return is_identical

    def create_ns_device_profile(self):
        log('ModuleExecutor.create_ns_device_profile()')

        post_data = {
            'ns_device_profile': self.configured_ns_device_profile,
        }

        log('post data: %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='ns_device_profile')

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

    def update_ns_device_profile(self):
        log('ModuleExecutor.update_ns_device_profile()')

        put_payload = self.configured_ns_device_profile

        put_data = {
            'ns_device_profile': put_payload
        }

        log('request put data: %s' % put_data)

        id = self.fetched_ns_device_profile['id']
        result = self.fetcher.put(put_data=put_data, resource='ns_device_profile', id=id)

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

    def delete_ns_device_profile(self):
        log('ModuleExecutor.delete_ns_device_profile()')

        id = self.fetched_ns_device_profile['id']

        result = self.fetcher.delete(resource='ns_device_profile', id=id)
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

        if not self.ns_device_profile_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.create_ns_device_profile()
        else:
            if not self.ns_device_profile_identical():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_ns_device_profile()

        # Update with fetched ns device profile key
        self.fetch_ns_device_profile()
        self.module_result['ns_device_profile'] = self.fetched_ns_device_profile


    def delete(self):
        log('ModuleExecutor.delete()')

        if self.ns_device_profile_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_ns_device_profile()

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
        name=dict(
            type='str'
        ),
        svm_ns_comm=dict(
            type='str'
        ),
        use_global_setting_for_communication_with_ns=dict(
            type='bool'
        ),
        id=dict(
            type='str'
        ),
        type=dict(
            type='str'
        ),
        snmpsecurityname=dict(
            type='str'
        ),
        snmpauthprotocol=dict(
            type='str'
        ),
        ssl_private_key=dict(
            type='str'
        ),
        ssl_cert=dict(
            type='str'
        ),
        http_port=dict(
            type='str'
        ),
        ns_profile_name=dict(
            type='str'
        ),
        ssh_port=dict(
            type='str'
        ),
        password=dict(
            type='str',
            no_log=True
        ),
        snmpsecuritylevel=dict(
            type='str'
        ),
        snmpcommunity=dict(
            type='str'
        ),
        passphrase=dict(
            type='str',
            no_log=True
        ),
        snmpprivprotocol=dict(
            type='str'
        ),
        https_port=dict(
            type='str'
        ),
        username=dict(
            type='str'
        ),
        host_password=dict(
            type='str',
            no_log=True
        ),
        max_wait_time_reboot=dict(
            type='str'
        ),
        snmpprivpassword=dict(
            type='str',
            no_log=True
        ),
        snmpversion=dict(
            type='str'
        ),
        cb_profile_name=dict(
            type='str'
        ),
        snmpauthpassword=dict(
            type='str',
            no_log=True
        ),
        host_username=dict(
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
