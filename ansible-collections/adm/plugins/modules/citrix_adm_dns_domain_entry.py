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
module: citrix_adm_dns_domain_entry
short_description: Manage Citrix ADM domain names.
description: Manage Citrix ADM domain names.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    tenant_id:
        description:
            - "Tenant Id of the DNS Domain Entries."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    name:
        description:
            - "DNS Domain Name."
            - " Minimum length =  1"
            - " Maximum length =  128"
        type: str

    id:
        description:
            - "Id is system generated key for all the DNS Domain Entries."
        type: str

    description:
        description:
            - "Description of DNS Domain Entry."
            - " Minimum length =  1"
            - " Maximum length =  1024"
        type: str


extends_documentation_fragment: citrix.adm.citrixadm
'''

EXAMPLES = '''
- name: Setup dns domain entry
  delegate_to: localhost
  citrix_adm_dns_domain_entry:
    mas_ip: 192.168.1.1
    mas_user: nsroot
    mas_pass: nsroot

    state: present

    name: test.com
    description: test.com domain description
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
dns_domain_entry:
    description: The created dns domain entry object.
    returned: success
    type: dict
'''

import copy

from ansible.module_utils.basic import AnsibleModule
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
        self.main_nitro_class = 'dns_domain_entry'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'dns_domain_entry': {
                'attributes_list': [
                    'tenant_id',
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

    def main_object_exists(self, config):
        try:
            main_object_exists = config.exists(
                get_id_attributes=self.attribute_config[self.main_nitro_class]['get_id_attributes'],
                use_filter=True,
            )
        except NitroException as e:
            raise

        return main_object_exists

    def get_main_config(self):
        config = MASResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attribute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attribute_config[self.main_nitro_class]['transforms'],
            api_path='nitro/v2/config',
        )

        return config

    def update_or_create(self):
        # Check if main object exists
        config = self.get_main_config()

        if not self.main_object_exists(config):
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.create()
        else:
            if not config.values_subset_of_actual():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    config.update(id_attribute='id')

        # Return the actual object
        config.get_actual_instance(
            get_id_attributes=self.attribute_config[self.main_nitro_class]['get_id_attributes'],
            success_codes=[None, 0],
            use_filter=True
        )
        self.module_result.update(dict(dns_domain_entry=config.actual_dict))

    def delete(self):
        # Check if main object exists
        config = self.get_main_config()

        if self.main_object_exists(config):
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.delete(delete_id_attributes=self.attribute_config[self.main_nitro_class]['delete_id_attributes'])

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
