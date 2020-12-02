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
module: citrix_adc_appfw_xmlcontenttype
short_description: Configuration for XML Content type resource.
description: Configuration for XML Content type resource.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)
    - Sumanth Lingappa (@sumanth-lingappa)

options:

    xmlcontenttypevalue:
        description:
            - "Content type to be classified as XML."
            - "Minimum length =  1"
        type: str

    isregex:
        choices:
            - 'REGEX'
            - 'NOTREGEX'
        description:
            - "Is field name a regular expression?."
        type: str


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- hosts: citrix_adc

  gather_facts: False
  tasks:
    - name: Setup xml content type
      delegate_to: localhost
      citrix_adc_appfw_xmlcontenttype:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.2
        state: present
        xmlcontenttypevalue: prefix.*test
        isregex: REGEX
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
'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'appfwxmlcontenttype'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attibute_config = {
            'appfwxmlcontenttype': {
                'attributes_list': [
                    'xmlcontenttypevalue',
                    'isregex',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'xmlcontenttypevalue',
                ],
                'delete_id_attributes': [
                    'xmlcontenttypevalue',
                ],
            },

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def main_object_exists(self, config):
        main_object_exists = config.exists(get_id_attributes=self.attibute_config[self.main_nitro_class]['get_id_attributes'])

        return main_object_exists

    def get_main_config(self):
        manipulated_values_dict = copy.deepcopy(self.module.params)

        config = NitroResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=manipulated_values_dict,
            attributes_list=self.attibute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attibute_config[self.main_nitro_class]['transforms'],
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
            if not config.values_subgroup_of_actual():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    # PUT operation is not available in NITRO for appfwjsoncontenttype
                    config.delete(delete_id_attributes=self.attibute_config[self.main_nitro_class]['delete_id_attributes'])
                    config.create()

    def delete(self):
        # Check if main object exists
        config = self.get_main_config()

        if self.main_object_exists(config):
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.delete(delete_id_attributes=self.attibute_config[self.main_nitro_class]['delete_id_attributes'])

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
        xmlcontenttypevalue=dict(type='str'),
        isregex=dict(
            type='str',
            choices=[
                'REGEX',
                'NOTREGEX',
            ]
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
