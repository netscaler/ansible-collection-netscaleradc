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
module: citrix_adm_poll_instances
short_description: Force the poll instances network function on the target Citrix ADM.
description:
    - Force the poll instances network function on the target Citrix ADM.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)



extends_documentation_fragment: citrix.citrixadm_modules.citrixadm
'''

EXAMPLES = '''
- name: Get all ns
  delegate_to: localhost
  register: ns_facts
  citrix_adm_poll_instances:
    mas_ip: 192.1681.1.1
    mas_user: nsroot
    mas_pass: nsroot

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
from ansible_collections.citrix.citrixadm_modules.plugins.module_utils.citrix_adm import (
    MASResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines
)


def poll_instances(module, module_result):

    log('poll_instances')

    # Process HTTP headers
    http_headers = {}
    http_headers['Content-Type'] = 'application/json'

    nitro_auth_token = module.params.get('nitro_auth_token')
    if nitro_auth_token is not None:
        http_headers['Cookie'] = "SESSID=%s" % nitro_auth_token

    nitro_user = module.params.get('nitro_user')
    if nitro_user is not None:
        http_headers['X-NITRO-USER'] = nitro_user

    nitro_pass = module.params.get('nitro_pass')
    if nitro_pass is not None:
        http_headers['X-NITRO-PASS'] = nitro_pass

    url = '%s://%s/nitro/v2/config/ns_emon_poll_policy' % (
        module.params['nitro_protocol'],
        module.params['nsip'],
    )

    poll_payload = {
        'params': {
            'action': 'do_poll'
        },
        'ns_emon_poll_policy': {},
    }

    r, info = fetch_url(
        module,
        url=url,
        headers=http_headers,
        data=module.jsonify(poll_payload),
        method='POST',
    )

    log('info: %s' % info)

    # Anything but a 200 is an error
    status = info.get('status')
    http_msg = info.get('msg')
    if status != 200:
        msg = 'Poll instances failure. HTTP status %s, msg: %s' % (status, http_msg)
        module.fail_json(msg=msg, **module_result)


def main():

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    module_result = dict(
        changed=True,
        failed=False,
        loglines=loglines,
    )

    poll_instances(module, module_result)

    module.exit_json(**module_result)


if __name__ == '__main__':
    main()
