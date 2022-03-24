#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Citrix Systems, Inc.
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
module: citrix_adm_get_bearer_token
short_description: Generate Citrix cloud bearer token
description:
    - Generate Citrix cloud bearer token

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    customer_id:
        description:
            - Customer id for which to generate token
        type: str

    api_client_id:
        description:
            - Id of API client
        type: str

    api_client_secret:
        description:
            - Secret of API client
        type: str

    endpoint:
        description:
            - API endpoint for bearer token
            - Can be any of the following
            - api-ap-s.cloud.com
            - api-eu.cloud.com
            - api-us.cloud.com
        type: str

'''

EXAMPLES = '''
- name: Get Citrix cloud bearer token
  delegate_to: localhost
  register: login_result
  citrix.adm.citrix_adm_get_bearer_token:
    customer_id: "{{ customer_id }}"
    api_client_id: "{{ api_client_id }}"
    api_client_secret: "{{ api_client_secret }}"
    endpoint: api-eu.cloud.com
'''

RETURN = '''
access_token:
    description: Bearer token
    returned: success
    type: str
    sample: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2l
'''

import sys
if sys.version_info[0] == 2:
    from urllib import urlencode
elif sys.version_info[0] == 3:
    from urllib.parse import urlencode

import codecs
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.basic import AnsibleModule


def main():

    argument_spec = dict(
        customer_id=dict(
            type='str',
        ),
        api_client_id=dict(
            type='str',
        ),
        api_client_secret=dict(
            type='str',
            no_log=True,
        ),
        endpoint=dict(
            type='str',
        ),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    url = 'https://{0}/cctrustoauth2/{1}/tokens/clients'.format(module.params['endpoint'], module.params['customer_id'])
    data = {
        'grant_type': 'client_credentials',
        'client_id': module.params['api_client_id'],
        'client_secret': module.params['api_client_secret'],
    }

    headers = {}
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['Accept'] = 'application/json'

    payload = codecs.encode(urlencode(data))
    r, info = fetch_url(
        module,
        url=url,
        headers=headers,
        data=payload,
        method='POST',
    )

    if r is not None:
        http_response_body = codecs.decode(r.read(), 'utf-8')
    elif 'body' in info:
        http_response_body = codecs.decode(info['body'], 'utf-8')
    else:
        http_response_body = ''

    if info['status'] != 200:
        result = {}
        result['http_response_data'] = info
        result['http_response_body'] = module.from_json(http_response_body)
        module.fail_json(msg="Return code not 200", **result)
    else:
        module.exit_json(**module.from_json(http_response_body))


if __name__ == '__main__':
    main()
