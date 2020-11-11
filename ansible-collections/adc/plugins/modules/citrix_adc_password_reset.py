#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2020 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adc_password_reset
short_description: Perform default password reset.
description:
    - Perform default password reset.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    nsip:
        type: str
        description:
            - The ip address of the netscaler appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. 192.168.1.1:555."
        required: True

    username:
        type: str
        description:
            - Username we want to reset password for
        required: True

    password:
        type: str
        description:
            - Default password of target ADC
        required: True

    new_password:
        type: str
        description:
            - New password for target ADC
        required: True

    nitro_protocol:
        type: str
        choices: [ 'http', 'https' ]
        description:
            - Which protocol to use when accessing the nitro API objects.
        required: True

    validate_certs:
        type: bool
        description:
            - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        required: True

'''

EXAMPLES = '''
- name: Password reset
  delegate_to: localhost
  citrix_adc_password_reset:
    nsip: 10.10.11.2
    username: nsroot
    nitro_protocol: https
    validate_certs: no
    password: nsroot
    new_password: verysecret
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
    sample: Non zero nitro errorcode 278
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    log,
    loglines,
    NitroAPIFetcher
)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        username=dict(
            type='str',
            required=True,
        ),
        password=dict(
            type='str',
            required=True,
            no_log=True,
        ),
        new_password=dict(
            type='str',
            required=True,
            no_log=True,
        ),
        nsip=dict(
            type='str',
            required=True,
        ),
        nitro_protocol=dict(
            required=True,
            type='str',
            choices=['https', 'http'],
        ),
        validate_certs=dict(
            required=True,
            type='bool'
        ),
    )

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )
    post_data = {
        'login': {
            'username': module.params['username'],
            'password': module.params['password'],
            'new_password': module.params['new_password'],
        }
    }

    fetcher = NitroAPIFetcher(module)
    result = fetcher.post(post_data=post_data, resource='login')

    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    log('{0}'.format(result))
    if result['nitro_errorcode'] == 0:
        module_result['changed'] = True
        module.exit_json(**module_result)
    else:
        msg = 'Non zero nitro errorcode {0}'.format(result['nitro_errorcode'])
        module.fail_json(msg=msg, **module_result)


if __name__ == '__main__':
    main()
