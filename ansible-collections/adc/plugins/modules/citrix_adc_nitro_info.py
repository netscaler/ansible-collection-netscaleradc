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
module: citrix_adc_nitro_info
short_description: Retrieve information from various NITRO API endpoints
description:
    - Retrieve information from various NITRO API endpoints.
    - The nitro information is returned at the C(nitro_info) key of the result variable.
    - You must register the result to a variable to access the nitro information.


version_added: "1.1.0"

author: George Nikolopoulos (@giorgos-nikolopoulos)

options:

    nsip:
        type: str
        description:
            - The IP address of the Citrix ADC or Citrix ADM instance where the Nitro API calls will be made.
            - "The port can be specified with the colon C(:). E.g. C(192.168.1.1:555)."
        required: true
        aliases:
            - mas_ip

    nitro_user:
        type: str
        description:
            - The username with which to authenticate to the Citrix ADC node.
        aliases:
            - mas_user

    nitro_pass:
        type: str
        description:
            - The password with which to authenticate to the Citrix ADC node.
        aliases:
            - mas_pass

    nitro_protocol:
        type: str
        choices:
            - http
            - https
        default: https
        description:
            - Which protocol to use when accessing the Nitro API objects.

    validate_certs:
        type: bool
        description:
            - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        default: 'yes'

    nitro_auth_token:
        type: str
        description:
            - The authentication token provided by the C(mas_login) operation. It is required when issuing Nitro API calls through a Citrix ADM proxy.
        aliases:
            - mas_auth_token

    mas_proxy_call:
        description:
            - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.
            - "When true you must also define the following options: I(nitro_auth_token), I(instance_ip)."
        type: bool
        default: false

    instance_ip:
        type: str
        description:
            - The IP address of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.

    instance_name:
        type: str
        description:
            - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.

    instance_id:
        type: str
        description:
            - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.

    endpoint:
        type: str
        description:
            - The endpoint for which we retrieve information.
        required: true

    nitro_info_key:
        type: str
        description:
            - The key which contains the requested info.
            - If not set it will default to the value of the I(endpoint) option.

    nitro_empty_errorcodes:
        type: list
        elements: int
        description:
            - A list of errorcodes which signify that no data exist for this endpoint.
            - The NITRO error will not cause the module execution to fail.

    args:
        type: dict
        description:
            - A dictionary which defines the args query parameter.

    filter:
        type: dict
        description:
            - A dictionary which defines the filter query parameter.

    attrs:
        type: dict
        description:
            - A dictionary which defines the attrs query parameter.

'''

EXAMPLES = '''
- name: Get sslparameters
  delegate_to: localhost
  citrix_adc_nitro_info:
    nitro_user: '{{ nitro_user }}'
    nitro_pass: '{{ nitro_pass }}'
    nsip: '{{ nsip }}'
    validate_certs: no
    endpoint: sslparameter

- name: Get a resource with args
  delegate_to: localhost
  citrix_adc_nitro_info:
    nitro_user: '{{ nitro_user }}'
    nitro_pass: '{{ nitro_pass }}'
    nsip: '{{ nsip }}'
    validate_certs: no
    endpoint: interface
    args:
      id: LO/1
    nitro_info_key: Interface

- name: Get an empty errorcode
  delegate_to: localhost
  citrix_adc_nitro_info:
    nitro_user: '{{ nitro_user }}'
    nitro_pass: '{{ nitro_pass }}'
    nsip: '{{ nsip }}'
    validate_certs: no
    endpoint: dnsnsrec/nosuchdomain.com
    nitro_empty_errorcodes:
      - 258
    nitro_info_key: dnsnsrec
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

nitro_info:
    returned: success
    description:
        - The result of the nitro request.
        - If no data were found an empty list will be returned.
        - Depending on the endpoint this will either be a list of dictionaries or a standalone dictionary. 
    type: list
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    netscaler_common_arguments,
    log,
    loglines,
    NitroAPIFetcher
)


def get_nitro_api_info(module):
    log('In get_nitro_api_info')

    fetcher = NitroAPIFetcher(module=module)

    endpoint = module.params.get('endpoint')
    args = module.params.get('args', None)
    attrs = module.params.get('attrs', None)
    filter = module.params.get('filter', None)

    nitro_info_key = module.params.get('nitro_info_key', None)
    if nitro_info_key is None:
        nitro_info_key = endpoint

    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    get_result = fetcher.get(resource=endpoint, args=args, attrs=attrs, filter=filter)
    log("get_result: %s" % get_result)
    data = get_result.get('data')

    # data key is always expected from a NITRO request
    if data is None:
        module_result['failed'] = True
        module.fail_json(msg='There is no data key in get result', **module_result)

    nitro_empty_errorcodes = module.params.get('nitro_empty_errorcodes')
    if nitro_empty_errorcodes is None:
        nitro_empty_errorcodes = []

    # Resource does not exist and appropriate errorcode returned
    errorcode = data.get('errorcode', 0)
    if errorcode in nitro_empty_errorcodes:
        module.exit_json(nitro_info=[], **module_result)

    acceptable_errorcodes = [0]
    acceptable_errorcodes.extend(nitro_empty_errorcodes)

    # Errorcode that signifies actual error
    if errorcode not in acceptable_errorcodes:
        msg = 'NITRO error %s. message: %s' % (errorcode, data.get('message'))
        module.fail_json(msg=msg, **module_result)

    nitro_info = data.get(nitro_info_key)

    # Fail if the data do not contain expected key
    if nitro_info is None:
        module_result['failed'] = True
        module.fail_json(msg='There is no nitro_info_key "%s"' % nitro_info_key, **module_result)

    module.exit_json(nitro_info=nitro_info, **module_result)


def main():

    argument_spec = dict()

    netscaler_picked_arguments = {}
    pick_keys = [
        'nsip',
        'nitro_user',
        'nitro_pass',
        'nitro_protocol',
        'validate_certs',
        'mas_proxy_call',
        'nitro_auth_token',
        'instance_ip',
    ]
    for key in pick_keys:
        netscaler_picked_arguments[key] = netscaler_common_arguments[key]

    argument_spec.update(netscaler_picked_arguments)

    module_specific_arguments = dict(

        instance_name=dict(type='str'),
        instance_id=dict(type='str'),

        endpoint=dict(
            type='str',
            required=True,
        ),
        args=dict(type='dict'),
        attrs=dict(type='dict'),
        filter=dict(type='dict'),
        nitro_info_key=dict(type='str'),
        nitro_empty_errorcodes=dict(
            type='list',
            elements='int',
        ),
    )

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    try:
        result = get_nitro_api_info(module=module)
    except Exception as e:
        msg = 'Exception %s: %s' % (type(e), str(e))
        module.fail_json(failed=True, msg=msg)


if __name__ == '__main__':
    main()
