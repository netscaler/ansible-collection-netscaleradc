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
module: citrix_adm_configuration_template_facts
short_description: Retrieve facts about Citrix ADM configuration templates.
description: Retrieve facts about Citrix ADM configuration templates.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - "Name of the configuration template"
        type: str

extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
- name: configuration templates facts
  delegate_to: localhost
  register: config_template_result
  citrix.adm.citrix_adm_configuration_template_facts:
    nitro_protocol: https
    nsip: railay.adm.cloud.com
    customer_id: "{{ customer_id }}"
    is_cloud: true
    bearer_token: "{{ login_result.access_token }}"

    name: "ShowConfiguration"
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

configuration_template:
    description: Dictionary containing the mps configuration template facts.
    returned: success
    type: dict
'''

import codecs

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible_collections.citrix.adm.plugins.module_utils.citrix_adm import (
    NitroAPIFetcher,
    netscaler_common_arguments,
    log,
    loglines
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module

        customer_id = self.module.params.get('customer_id')
        if customer_id is not None:
            api_path = 'massvc/%s/nitro/v2/config' % customer_id
            self.nitro_api_fetcher = NitroAPIFetcher(module, api_path=api_path)
        else:
            self.nitro_api_fetcher = NitroAPIFetcher(module, api_path='nitro/v2/config')

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def get_configuration_template_facts(self):
        log('ModuleExecutor.get_configuration_template_facts()')
        result = self.nitro_api_fetcher.get(
            resource='configuration_template',
        )

        log('result of get %s' % result)

        if result['http_response_data']['status'] != 200:
            raise Exception('Status code not 200 %s' % result['http_response_data']['status'])

        templates = result['data'].get('configuration_template', [])
        log('Will look for name %s' % self.module.params.get('name'))
        for template in templates:
            log('Examinign configuration tempalate %s' % template['name'])
            if template['name'] == self.module.params.get('name'):
                return template

        return {}

    def main(self):
        try:
            configuration_template = self.get_configuration_template_facts()
            self.module_result.update(dict(configuration_template=configuration_template))
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
