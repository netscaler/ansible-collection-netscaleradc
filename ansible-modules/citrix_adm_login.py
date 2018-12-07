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
module: citrix_adm_login
short_description: FIXME
description: FIXME

version_added: "2.8.0"

extends_documentation_fragment: netscaler
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
session_id:
    description: The session id to be used as authentication token on subsequent module calls.
    returned: success
    type: str
    sample: "##1A44A1437AD74D6158FC51FC95A0009D93FA8C1A8E2CCCEF9F4FD4DA2039"

'''

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.netscaler.netscaler import NitroAPIFetcher, NitroException, netscaler_common_arguments, log, loglines


def main():

    module = AnsibleModule(
        argument_spec=netscaler_common_arguments,
        supports_check_mode=False,
    )

    try:
        fetcher = NitroAPIFetcher(module, api_path='nitro/v2/config')

        module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        post_data = {
            'login': {
                'username': module.params['nitro_user'],
                'password': module.params['nitro_pass'],
            }
        }
        result = fetcher.post(post_data=post_data, resource='login')
        log('POST result %s' % result)
        log(result['nitro_errorcode'])
        if result['nitro_errorcode'] not in (None, 0):
            errorcode = result.get('nitro_errorcode')
            message = result.get('nitro_message')
            severity = result.get('nitro_severity')
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(errorcode), message, severity)
            module.fail_json(msg=msg, **module_result)
        else:
            module_result.update(dict(session_id=result['data']['login'][0]['sessionid']))
            module.exit_json(**module_result)
    except Exception as e:
        msg = 'Exception %s: %s' % (type(e), str(e))
        module.fail_json(msg=msg, **module_result)


if __name__ == '__main__':
    main()
