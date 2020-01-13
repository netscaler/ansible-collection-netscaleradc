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
module: citrix_adm_mpsgroup
short_description: Manage Citrix ADM user groups.
description: Manage Citrix ADM user groups.

version_added: "2.8.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    authscope_props:
        description:
            - "authscope_props"
        type: list

    allow_application_only:
        description:
            - "Checks if only application centic page is needed."
        type: bool

    session_timeout:
        description:
            - "Session timeout for the Group."
        type: str

    permission:
        choices:
            - 'admin'
            - 'read-only'
        description:
            - "Permission for the group (admin/read-only)."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    name:
        description:
            - "Group Name."
            - "Minimum length = 1"
            - "Maximum length = 64"
        type: str

    session_timeout_unit:
        description:
            - "Session timeout unit for the Group."
        type: str

    description:
        description:
            - "Description of Group."
            - "Minimum length = 1"
            - "Maximum length = 1024"
        type: str

    assign_all_apps:
        description:
            - "Assign All Applications (YES|NO)."
        type: bool

    enable_session_timeout:
        description:
            - "Enables session timeout for group."
        type: bool

    tenant_id:
        description:
            - "Id of the tenant."
            - "Minimum length = 1"
            - "Maximum length = 128"
        type: str

    assign_all_devices:
        description:
            - "Assign All Instances (YES|NO)."
        type: bool

    id:
        description:
            - "Id is system generated key for all the system groups."
        type: str

    role:
        choices:
            - 'admin'
            - 'nonadmin'
        description:
            - "Role (admin|nonadmin)."
        type: str

    roles:
        description:
            - "Roles assigned to the group."
        type: list

    application_names_without_regex:
        description:
            - "selected application names that are part of this group."
        type: list

    standalone_instances_id:
        description:
            - "Stand alone instances belong to this groupp."
        type: list

    users:
        description:
            - "Users belong to the group."
        type: list

    application_names:
        description:
            - "All Application names that are part of this group."
            - "This includes selected appnames as well as applications which are result of defined regex."
        type: list

    application_names_with_regex:
        description:
            - "Application names defined with regex that are part of this group"
        type: list


extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- name: Setup mpsuser
  delegate_to: localhost
  citrix_adm_mpsgroup:
    mas_ip: 192.168.1.1
    mas_user: nsroot
    mas_pass: nsroot

    state: present

    name: test_mpsgroup
    permission: read-only
    allow_application_only: true
    session_timeout: 10
    session_timeout_unit: Minutes
    description: some description
    assign_all_apps: true
    enable_session_timeout: true
    assign_all_devices: false
    role: admin
    roles:
      - admin
    application_names_without_regex: []
    application_names: []
    application_names_with_regex: []
    standalone_instances_id: []
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

mpsgroup:
    description: Dictionary containing the attributes of the created mpsgroup
    returned: success
    type: dict
'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import MASResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'mpsgroup'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'mpsgroup': {
                'attributes_list': [
                    'authscope_props',
                    'allow_application_only',
                    'session_timeout',
                    'permission',
                    'name',
                    'session_timeout_unit',
                    'description',
                    'assign_all_apps',
                    'enable_session_timeout',
                    'tenant_id',
                    'assign_all_devices',
                    'id',
                    'role',
                    'roles',
                    'application_names_without_regex',
                    'standalone_instances_id',
                    'users',
                    'application_names',
                    'application_names_with_regex',
                ],
                'transforms': {
                    'enable_session_timeout': lambda v: "true" if v else "false",
                    'allow_application_only': lambda v: "true" if v else "false",
                    'assign_all_apps': lambda v: "true" if v else "false",
                    'assign_all_devices': lambda v: "true" if v else "false",
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
        self.module_result.update(dict(mpsgroup=config.actual_dict))

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
        authscope_props=dict(
            type='list'
        ),
        allow_application_only=dict(
            type='bool'
        ),
        session_timeout=dict(
            type='str'
        ),
        permission=dict(
            type='str',
            choices=[
                'admin',
                'read-only',
            ],
        ),
        name=dict(
            type='str'
        ),
        session_timeout_unit=dict(
            type='str'
        ),
        description=dict(
            type='str'
        ),
        assign_all_apps=dict(
            type='bool'
        ),
        enable_session_timeout=dict(
            type='bool'
        ),
        tenant_id=dict(
            type='str'
        ),
        assign_all_devices=dict(
            type='bool'
        ),
        id=dict(
            type='str'
        ),
        role=dict(
            type='str',
            choices=[
                'admin',
                'nonadmin',
            ],
        ),
        roles=dict(
            type='list'
        ),
        application_names_without_regex=dict(
            type='list'
        ),
        standalone_instances_id=dict(
            type='list'
        ),
        users=dict(
            type='list'
        ),
        application_names=dict(
            type='list'
        ),
        application_names_with_regex=dict(
            type='list'
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
