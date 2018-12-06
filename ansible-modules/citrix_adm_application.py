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
module: citrix_adm_application
short_description: Manage applications on Citrix ADM.
description:
    - Manage applications on Citrix ADM.
    - Note that due to limitations on the underlying NITRO API an update is always forced when I(state=present).

version_added: "2.8.0"

options:

    throughput_avg:
        description:
            - Sum of throughput across all vips of the app.
        type: str

    app_category:
        description:
            - Application Category.
            - Minimum length = 1
            - Maximum length = 255
        type: str

    curclntconnections:
        description:
            - curclntconnections Value across all vips of the app.
        type: str

    name:
        description:
            - Application Name.
            - Maximum length = 1024
        type: str

    cursrvrconnections:
        description:
            - cursrvrconnections Value across all vips of the app.
        type: str

    application_managed:
        description:
            - Managed field.
        type: bool

    id:
        description:
            - Id is system generated key..
        type: str

    family:
        description:
            - Application Family.
            - Minimum length = 1
            - Maximum length = 255
        type: str

    app_criteria:
        description:
            - Application criteria.
        type: list

    app_components:
        description:
            - Application components.
        type: list

    no_of_auth:
        description:
            - Number of AUTH VIPs.
        type: str

    no_of_gslb:
        description:
            - Number of GSLB VIPs.
        type: str

    no_of_gslbsvc:
        description:
            - Number of LB VIPs.
        type: str

    no_of_cr:
        description:
            - Number of CR VIPs.
        type: str

    no_of_cs:
        description:
            - Number of CS VIPs.
        type: str

    no_of_svc:
        description:
            - Number of Services.
        type: str

    no_of_svcgrp:
        description:
            - Number of Service Groups.
        type: str

    no_of_haproxy_be:
        description:
            - Number of Banckends.
        type: str

    force_delete:
        description:
            - force delete.
        type: bool

    no_of_svr:
        description:
            - Number of Servers.
        type: str

    stylebook_params:
        description:
            - Stylebook Parameter.
        type: str

    no_of_lb:
        description:
            - Number of LB VIPs.
        type: str

    no_of_vpn:
        description:
            - Number of VPN VIPs.
        type: str

    no_of_haproxy_fe:
        description:
            - Number of Frontends.
        type: str

    application_ids:
        description:
            - Application IDs that are part of this application.
        type: list


    poll_after_delete:
        description:
            - Poll the instances after deleting an application to update the application list immediately.
            - By default Citrix ADM will poll every 30 minutes.
        type: bool
        default: false

    poll_delay:
        description:
            - Time in seconds to wait between the delete operation and the subsequent poll operation.
            - This is only relevant when I(state) is set to C(absent) and I(poll_after_delete) is set to C(true).
        type: int
        default: 10

    check_create:
        description:
            - Check if the application was created on the target citrix adm.
            - Return the created application in the module results.
        type: bool
        default: true

    check_create_delay:
        description:
            - Time in seconds to wait between the create/update operation and retrieval of the created application.
            - This delay should be non zero as the newly created/updated application might not be immediately available to be fetched by the target Citrix ADM.
        type: int
        default: 10

extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
vars:
stylebook_params:
  name: "basic-lb-config"
  namespace: "com.example.stylebooks"
  version: "0.1"
  configpack_payload:
    parameters:
      name: "playbook5_test_application_name"
      ip: "192.168.5.2"
      lb-alg: "ROUNDROBIN"
      svc-servers:
        - "192.168.5.3"
      svc-port: "80"
    targets:
      - id: "6a28b48b-e7c0-4770-b499-3ddb85b47561"

- name: Login to citrix_adm
  delegate_to: localhost
  register: login_result
  citrix_adm_login:
    mas_ip: 192.168.1.1
    mas_user: nsroot
    mas_pass: nsroot

- name: Setup application
  delegate_to: localhost
  citrix_adm_application:
    mas_ip: 192.168.1.1
    nitro_auth_token: "{{ login_result.session_id }}"

    state: present

    app_category: test_category
    name: playbook5_test_application_name-lb_10.78.60.209_lb
    stylebook_params: "{{ stylebook_params | to_json }}"
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

application:
    description: Dictionary containing all the attributes of the created application
    returned: success
    type: dict
'''

import codecs
import time

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.network.netscaler.netscaler import netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'application'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            
            'application': {
                'attributes_list': [
                    
                    'throughput_avg',
                    'app_category',
                    'curclntconnections',
                    'name',
                    'cursrvrconnections',
                    'application_managed',
                    'id',
                    'family',
                    'app_criteria',
                    'app_components',
                    'no_of_auth',
                    'no_of_gslb',
                    'no_of_gslbsvc',
                    'no_of_cr',
                    'no_of_cs',
                    'no_of_svc',
                    'no_of_svcgrp',
                    'no_of_haproxy_be',
                    'force_delete',
                    'no_of_svr',
                    'stylebook_params',
                    'no_of_lb',
                    'no_of_vpn',
                    'no_of_haproxy_fe',
                    'application_ids',
                ],
                'transforms': {
                    
                },
                'get_id_attributes': [
                    
                    'name',
                    'id',
                ],
                'delete_id_attributes': [
                    
                    'id',
                ],
            },
            

        }

        # Process HTTP headers
        self.http_headers = {}
        self.http_headers['Content-Type'] = 'application/json'

        nitro_auth_token = self.module.params.get('nitro_auth_token')
        if nitro_auth_token is not None:
            self.http_headers['Cookie'] = "SESSID=%s" % nitro_auth_token

        nitro_user = self.module.params.get('nitro_user')
        if nitro_user is not None:
            self.http_headers['X-NITRO-USER'] = nitro_user

        nitro_pass = self.module.params.get('nitro_pass')
        if nitro_pass is not None:
            self.http_headers['X-NITRO-PASS'] = nitro_pass


        # Prepare module result
        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def _parse_response_body(self, r):
        if r is not None:
            http_response_body = codecs.decode(r.read(), 'utf-8')
            log('http_response_body %s' % http_response_body)
            try:
                data = self.module.from_json(http_response_body)
                log('data %s' % data)
            except ValueError:
                data = {}
                log('Cannot parse response data')
        return data


    def get_application(self):
        url = '%s://%s/nitro/v2/config/application' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
        )

        filter_list = []
        for attribute in self.attribute_config['application']['get_id_attributes']:
            attribute_value = self.module.params.get(attribute)
            if attribute_value is not None:
                filter_list.append('%s:%s' % (attribute, attribute_value))

        filter_str = ','.join(filter_list)
        if filter_str != '':
            url = '%s?filter=%s' % (url, filter_str)

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            method='GET',
        )
        log('info: %s' % info)

        # Anything but a 200 is an error
        status = info.get('status')
        http_msg = info.get('msg')
        if status != 200:
            msg = 'HTTP status %s, msg: %s' % (status, http_msg)
            self.module.fail_json(msg=msg, **self.module_result)

        if r is not None:
            http_response_body = codecs.decode(r.read(), 'utf-8')
            log('http_response_body %s' % http_response_body)
            try:
                data = self.module.from_json(http_response_body)
                log('data %s' % data)
            except ValueError:
                data = {}
                self.module.fail_json(msg='Cannot parse GET http response data', **self.module_result)

            # Parse data to get application object
            application_list = data.get('application')
            if not isinstance(application_list, list):
                self.module.fail_json(msg='GET body does not contain application data', **self.module_result)

            if len(application_list) == 0:
                return None
            elif len(application_list) > 1:
                self.module.fail_json(msg='GET body does contains multiple application entries', **self.module_result)
            else:
                return application_list[0]
        else:
            self.module.fail_json(msg='GET response does not have a body', **self.module_result)

    def construct_request_data(self):
        data_dict = {}
        for attribute in self.attribute_config['application']['attributes_list']:
            attr_val = self.module.params.get(attribute)
            if attr_val is not None:
                data_dict[attribute] = attr_val

        ret_val = { 'application': data_dict }
        return ret_val

    def post_application(self):
        log('post_application')
        request_data = self.construct_request_data()
        payload = '%s' % self.module.jsonify(request_data)

        log('request data %s' % request_data)
        log('payload %s' % payload)

        url = '%s://%s/nitro/v2/config/application' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
        )

        log('url %s' % url)

        log('headers %s' % self.http_headers)
        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=payload,
            method='POST',
        )

        log('info: %s' % info)

        data = self._parse_response_body(r)
        nitro_errorcode = data.get('errorcode')

        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        if status != 200:
            log('Fail due to status')
            msg = 'HTTP status fail status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            log('Fail due to nitro_errorcode')
            log('nitro error code %s %s' % (type(nitro_errorcode), nitro_errorcode))
            msg = 'nitro_errorcode fail HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)


    def put_application(self, application):
        log('put_application')
        request_data = self.construct_request_data()
        payload='%s' % self.module.jsonify(request_data)

        log('request data %s' % request_data)
        log('payload %s' % payload)

        application_id = application.get('id')
        if application_id is None:
            self.module.fail_json('Cannot update application without id', **self.module_result)

        url = '%s://%s/nitro/v2/config/application/%s' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
            application_id,
        )

        log('url %s' % url)
        log('headers %s' % self.http_headers)

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=payload,
            method='PUT',
        )

        log('info: %s' % info)

        data = self._parse_response_body(r)

        nitro_errorcode = data.get('errorcode')

        # Anything but a 200 is an error
        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        if status != 200:
            msg = 'HTTP status fail status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            msg = 'nitro_errorcode fail. HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

    def delete_application(self, application):
        log('delete_application')

        application_id = application.get('id')
        if application_id is None:
            self.module.fail_json('Cannot delete application without id', **self.module_result)

        stylebook_params = self.module.from_json(self.module.params['stylebook_params'])
        log('stylebook_params %s' % stylebook_params)

        url = '%s://%s/nitro/v2/config/application/%s?args=stylebook_params:%s/%s/%s,configpack_id:%s' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
            application_id,
            stylebook_params['namespace'],
            stylebook_params['version'],
            stylebook_params['name'],
            application['configpack_id'],
        )

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            method='DELETE',
        )

        log('info: %s' % info)

        data = self._parse_response_body(r)
        nitro_errorcode = data.get('errorcode')

        status = info.get('status')
        http_msg = info.get('msg')

        message_tuple = (
            status,
            http_msg,
            data.get('errorcode'),
            data.get('message'),
            data.get('severity'),
        )
        # Anything but a 200 is an error
        if status != 200:
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)
        elif nitro_errorcode not in (0, None):
            msg = 'HTTP status %s, msg: %s. nitro_errorcode=%s nitro_message=%s nitro_severity=%s' % message_tuple
            self.module.fail_json(msg=msg, **self.module_result)

    def poll_instances(self):
        log('poll_instances')

        url = '%s://%s/nitro/v2/config/ns_emon_poll_policy' % (
            self.module.params['nitro_protocol'],
            self.module.params['nsip'],
        )

        poll_payload = {
            "params":{
                "action":"do_poll"
            },
            "ns_emon_poll_policy":{},
        }

        r, info = fetch_url(
            self.module,
            url=url,
            headers=self.http_headers,
            data=self.module.jsonify(poll_payload),
            method='POST',
        )

        log('r: %s' % r.read())
        log('info: %s' % info)

        # Anything but a 200 is an error
        status = info.get('status')
        http_msg = info.get('msg')
        if status != 200:
            msg = 'Poll instances failure. HTTP status %s, msg: %s' % (status, http_msg)
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:
            application = self.get_application()
            log('existing application %s' % application)
            if self.module.params['state'] == 'present':
                self.module_result['changed'] = True
                if application is None:
                    self.post_application()
                else:
                    self.put_application(application)

                # Return the created/updated application in the module results
                if self.module.params['check_create']:
                    time.sleep(self.module.params['check_create_delay'])
                    created_application = self.get_application()
                    if created_application is None:
                        self.module.fail_json(msg='Failed to create application', **self.module_result)
                    else:
                        self.module_result.update(dict(application=created_application))

            elif self.module.params['state'] == 'absent':
                if application is not None:
                    self.module_result['changed'] = True
                    self.delete_application(application=application)

                if self.module.params['poll_after_delete']:
                    time.sleep(self.module.params['poll_delay'])
                    self.poll_instances()

            self.module.exit_json(**self.module_result)

        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)



def main():


    argument_spec = dict()

    module_specific_arguments = dict(
        
        throughput_avg=dict(type='str',),

        
        app_category=dict(type='str',),

        
        curclntconnections=dict(type='str',),

        
        name=dict(type='str',),

        
        cursrvrconnections=dict(type='str',),

        
        application_managed=dict(type='bool',),

        
        id=dict(type='str',),

        
        family=dict(type='str',),

        
        app_criteria=dict(type='list',),

        
        app_components=dict(type='list',),

        
        no_of_auth=dict(type='str',),

        
        no_of_gslb=dict(type='str',),

        
        no_of_gslbsvc=dict(type='str',),

        
        no_of_cr=dict(type='str',),

        
        no_of_cs=dict(type='str',),

        
        no_of_svc=dict(type='str',),

        
        no_of_svcgrp=dict(type='str',),

        
        no_of_haproxy_be=dict(type='str',),

        
        force_delete=dict(type='bool',),

        
        no_of_svr=dict(type='str',),

        
        stylebook_params=dict(type='str',),

        
        no_of_lb=dict(type='str',),

        
        no_of_vpn=dict(type='str',),

        
        no_of_haproxy_fe=dict(type='str',),

        
        application_ids=dict(type='list',),

        
        poll_after_delete=dict(
            type='bool',
            default=False,
        ),
        poll_delay=dict(
            type='int',
            default=10,
        ),
        check_create=dict(
            type='bool',
            default=True,
        ),
        check_create_delay=dict(
            type='int',
            default=10,
        )
    )


    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)


    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()