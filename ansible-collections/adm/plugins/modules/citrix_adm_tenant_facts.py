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
module: citrix_adm_tenant_facts
short_description: Retrieve facts about Citrix ADM tenants.
description: Retrieve facts about Citrix ADM tenants.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - "Name of the Tenant."
            - "Minimum length = 1"
            - "Maximum length = 512"
        type: str


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
FIXME
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

tenant:
    description: List containing the details of the requested tenants.
    returned: success
    type: list
'''

import codecs

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible_collections.citrix.adm.plugins.module_utils.citrix_adm import (
    MASResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'tenant'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'tenant': {
                'attributes_list': [
                    'name',
                ],
                'transforms': {
                    'enable_session_timeout': lambda v: "true" if v else "false",
                    'external_authentication': lambda v: "true" if v else "false",
                },
                'get_id_attributes': [
                    'name',
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

    def get_tenant_facts(self):
        url = '%s://%s/nitro/v2/config/tenant' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
        )

        filter_list = []
        for attribute in self.attribute_config['tenant']['get_id_attributes']:
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

        return data.get('tenant', [])

    def main(self):
        try:
            tenant = self.get_tenant_facts()
            self.module_result.update(dict(tenant=tenant))
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
