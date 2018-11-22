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
module: netscaler_appfw_policy
short_description: Manage Netscaler Web Application Firewall policies.
description:
    - Manage Netscaler Web Application Firewall policies.
    - The module uses the NITRO API to make configuration changes to WAF policies on a target Netscaler.
    - The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest

version_added: "2.8.0"

options:

    name:
        description:
            - Name for the policy. 
            - Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and underscore characters. Can be changed after the policy is created.
            - 
            - The following requirement applies only to the NetScaler CLI:
            - If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my policy" or 'my policy'\).
        type: str

    rule:
        description:
            - Name of the NetScaler named rule, or a NetScaler default syntax expression, that the policy uses to determine whether to filter the connection through the application firewall with the designated profile.
        type: str

    profilename:
        description:
            - Name of the application firewall profile to use if the policy matches.
        type: str

    comment:
        description:
            - Any comments to preserve information about the policy for later reference.
        type: str

    logaction:
        description:
            - Where to log information for connections that match this policy.
        type: str


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- name: Setup appfw policy
  delegate_to: localhost
  netscaler_appfw_policy:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 192.168.1.1
    state: present
    name: policy_integration_test
    rule: 'HTTP.REQ.HOSTNAME.DOMAIN.EQ("blog.example.com")'
    profilename: APPFW_BLOCK
    comment: 'policy test comment'

- name: Remove appfw policy
  delegate_to: localhost
  netscaler_appfw_policy:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 192.168.1.1
    state: absent
    name: policy_integration_test
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

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import NitroResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):
    
    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'appfwpolicy'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attibute_config = {
            
            'appfwpolicy': {
                'attributes_list': [
                    
                    'name',
                    'rule',
                    'profilename',
                    'comment',
                    'logaction',
                    'newname',
                ],
                'transforms': {
                    
                },
                'get_id_attributes': [
                    
                    'name',
                ],
                'delete_id_attributes': [
                    
                    'name',
                ],
            },
            

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )


    def update_or_create(self):
        # Check if main object exists
        config = NitroResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attibute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attibute_config[self.main_nitro_class]['transforms'],
        )

        # Create or update main object
        try:
            appfw_policy_exists = config.exists(get_id_attributes=self.attibute_config[self.main_nitro_class]['get_id_attributes'])
        except NitroException as e:
            # This is the no such policy exists exception
            if e.errorcode == 2054:
                appfw_policy_exists = False
            else:
                raise

        if not appfw_policy_exists:
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.create()
        else:
            if not config.values_subgroup_of_actual():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    config.update(id_attribute='name')


    

    def delete(self):
        # Check if main object exists
        config = NitroResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attibute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attibute_config[self.main_nitro_class]['transforms'],
        )

        try:
            appfw_policy_exists = config.exists(get_id_attributes=self.attibute_config[self.main_nitro_class]['get_id_attributes'])
        except NitroException as e:
            # This is the no such policy exists exception
            if e.errorcode == 2054:
                appfw_policy_exists = False
            else:
                raise
        if appfw_policy_exists:
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
        
        name=dict(type='str'),
        
        rule=dict(type='str'),
        
        profilename=dict(type='str'),
        
        comment=dict(type='str'),
        
        logaction=dict(type='str'),
        
        appfwpolicy_csvserver_bindings=dict(type='dict'),
        denyurl_bindings=dict(type='dict'),
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