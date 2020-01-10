#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2018 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adm_ns_facts
short_description: Retrieve facts about Citrix ADM managed instances.
description: Retrieve facts about Citrix ADM managed instances.

version_added: "2.8.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - "Name of managed device."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    id:
        description:
            - "Id is system generated key for all the managed devices."
        type: str

    ipv4_address:
        description:
            - "IPv4 Address."
            - "Minimum length = 1"
            - "Maximum length = 64"
        type: str

    ipv6_address:
        description:
            - "IPv6 Address."
        type: str

    ip_address:
        description:
            - "IP Address for this managed device."
            - "Minimum length = 1"
            - "Maximum length = 64"
        type: str


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- name: Get all ns
  delegate_to: localhost
  register: ns_facts
  citrix_adm_ns_facts:
    mas_ip: 192.1681.1.1
    mas_user: nsroot
    mas_pass: nsroot

    ipaddress: 192.168.1.2

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

ns_facts:
    description: List containing the details of the requested ns instances
    returned: success
    type: list
'''

import codecs

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.network.netscaler.netscaler import MASResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'ns'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'ns': {
                'attributes_list': [
                    'name',
                    'id',
                    'ipv4_address',
                    'ipv6_address',
                    'ip_address',
                ],
                'transforms': {
                    'enable_session_timeout': lambda v: "true" if v else "false",
                    'external_authentication': lambda v: "true" if v else "false",
                },
                'get_id_attributes': [
                    'name',
                    'id',
                    'ipv4_address',
                    'ipv6_address',
                    'ip_address',
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

    def get_ns_facts(self):
        url = '%s://%s/nitro/v2/config/ns' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
        )

        filter_list = []
        for attribute in self.attribute_config['ns']['get_id_attributes']:
            attribute_value = self.module.params.get(attribute)
            if attribute_value is not None:
                filter_list.append('%s:%s' % (attribute, attribute_value))

        filter_str = ','.join(filter_list)
        if filter_str != '':
            url = '%s?filter=%s' % (url, filter_str)

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            method='GET',
        )
        log('r: %s' % r)
        log('info: %s' % info)

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

        if status != 200:
            log('Failing for status')
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            log('Failing for nitro')
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

        return data.get('ns', [])

    def main(self):
        try:
            ns = self.get_ns_facts()
            self.module_result.update(dict(ns=ns))
            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        name=dict(
            type='str'
        ),
        id=dict(
            type='str'
        ),
        ipv4_address=dict(
            type='str'
        ),
        ipv6_address=dict(
            type='str'
        ),
        ip_address=dict(
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
