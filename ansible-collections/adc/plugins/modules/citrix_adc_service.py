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
module: citrix_adc_service
short_description: Manage service configuration in Citrix ADC
description:
    - Manage service configuration in Citrix ADC.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - >-
                Name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must
                only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and
                (-) characters. Cannot be changed after the service has been created.
            - "Minimum length =  1"
        type: str

    ip:
        description:
            - "IP to assign to the service."
            - "Minimum length =  1"
        type: str

    servername:
        description:
            - "Name of the server that hosts the service."
            - "Minimum length =  1"
        type: str

    servicetype:
        choices:
            - 'HTTP'
            - 'FTP'
            - 'TCP'
            - 'UDP'
            - 'SSL'
            - 'SSL_BRIDGE'
            - 'SSL_TCP'
            - 'DTLS'
            - 'NNTP'
            - 'RPCSVR'
            - 'DNS'
            - 'ADNS'
            - 'SNMP'
            - 'RTSP'
            - 'DHCPRA'
            - 'ANY'
            - 'SIP_UDP'
            - 'SIP_TCP'
            - 'SIP_SSL'
            - 'DNS_TCP'
            - 'ADNS_TCP'
            - 'MYSQL'
            - 'MSSQL'
            - 'ORACLE'
            - 'RADIUS'
            - 'RADIUSListener'
            - 'RDP'
            - 'DIAMETER'
            - 'SSL_DIAMETER'
            - 'TFTP'
            - 'SMPP'
            - 'PPTP'
            - 'GRE'
            - 'SYSLOGTCP'
            - 'SYSLOGUDP'
            - 'FIX'
            - 'SSL_FIX'
            - 'USER_TCP'
            - 'USER_SSL_TCP'
            - 'QUIC'
            - 'IPFIX'
            - 'LOGSTREAM'
        description:
            - "Protocol in which data is exchanged with the service."
        type: str

    port:
        description:
            - "Port number of the service."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    cleartextport:
        description:
            - >-
                Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic.
                to transparent SSL services.
            - "Minimum value = C(1)"
        type: int

    cachetype:
        choices:
            - 'TRANSPARENT'
            - 'REVERSE'
            - 'FORWARD'
        description:
            - "Cache type supported by the cache server."
        type: str

    maxclient:
        description:
            - "Maximum number of simultaneous open connections to the service."
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967294)"
        type: str

    healthmonitor:
        description:
            - "Monitor the health of this service. Available settings function as follows:"
            - "YES - Send probes to check the health of the service."
            - >-
                NO - Do not send probes to check the health of the service. With the NO option, the appliance shows
                service as UP at all times.
        type: bool

    maxreq:
        description:
            - "Maximum number of requests that can be sent on a persistent connection to the service."
            - "Note: Connection requests beyond this value are rejected."
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    cacheable:
        description:
            - "Use the transparent cache redirection virtual server to forward requests to the cache server."
            - "Note: Do not specify this parameter if you set the Cache Type parameter."
        type: bool

    cip:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6
                as its value. Used if the server needs the client's IP address for security, accounting, or other
                and setting the Use Source IP parameter is not a viable option.
        type: str

    cipheader:
        description:
            - >-
                Name for the HTTP header whose value must be set to the IP address of the client. Used with the
                IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the
                uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in
                set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog
                at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not
                the appliance inserts a header with the name "client-ip.".
            - "Minimum length =  1"
        type: str

    usip:
        description:
            - >-
                Use the client's IP address as the source IP address when initiating a connection to the server. When
                a service, if you do not set this parameter, the service inherits the global Use Source IP setting
                in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes
                Configure Modes dialog box). However, you can override this setting after you create the service.
        type: bool

    pathmonitor:
        description:
            - "Path monitoring for clustering."
        type: bool

    pathmonitorindv:
        description:
            - "Individual Path monitoring decisions."
        type: bool

    useproxyport:
        description:
            - >-
                Use the proxy port as the source port when initiating connections with the server. With the NO
                the client-side connection port is used as the source port for the server-side connection.
            - "Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES."
        type: bool

    sc:
        description:
            - "State of SureConnect for the service."
        type: bool

    sp:
        description:
            - "Enable surge protection for the service."
        type: bool

    rtspsessionidremap:
        description:
            - "Enable RTSP session ID mapping for the service."
        type: bool

    clttimeout:
        description:
            - "Time, in seconds, after which to terminate an idle client connection."
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: int

    svrtimeout:
        description:
            - "Time, in seconds, after which to terminate an idle server connection."
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: int

    customserverid:
        description:
            - >-
                Unique identifier for the service. Used when the persistency type for the virtual server is set to
                Server ID.
        type: str

    serverid:
        description:
            - "The  identifier for the service. This is used when the persistency type is set to Custom Server ID."
        type: str

    cka:
        description:
            - "Enable client keep-alive for the service."
        type: bool

    tcpb:
        description:
            - "Enable TCP buffering for the service."
        type: bool

    cmp:
        description:
            - "Enable compression for the service."
        type: bool

    maxbandwidth:
        description:
            - "Maximum bandwidth, in Kbps, allocated to the service."
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967287)"
        type: str

    accessdown:
        description:
            - >-
                Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service
                DOWN, and this parameter is disabled, the packets are dropped.
        type: bool

    monthreshold:
        description:
            - >-
                Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to
                a service as UP or DOWN.
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    downstateflush:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do
                enable this option for applications that must complete their transactions.
        type: str

    tcpprofilename:
        description:
            - "Name of the TCP profile that contains TCP configuration settings for the service."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    httpprofilename:
        description:
            - "Name of the HTTP profile that contains HTTP configuration settings for the service."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    contentinspectionprofilename:
        description:
            - >-
                Name of the ContentInspection profile that contains IPS/IDS communication related setting for the
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    hashid:
        description:
            - >-
                A numerical identifier that can be used by hash based load balancing methods. Must be unique for each
            - "Minimum value = C(1)"
        type: str

    comment:
        description:
            - "Any information about the service."
        type: str

    appflowlog:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Enable logging of AppFlow information."
        type: str

    netprofile:
        description:
            - "Network profile to use for the service."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of
            - "Minimum value = C(0)"
            - "Maximum value = C(4094)"
        type: str

    processlocal:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                By turning on this option packets destined to a service in a cluster will not under go any steering.
                this option for single packet request response mode or when the upstream device is performing a
                RSS for connection based distribution.
        type: str

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the service. DNS profile properties will applied to the
                processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    monconnectionclose:
        choices:
            - 'RESET'
            - 'FIN'
        description:
            - >-
                Close monitoring connections by sending the service a connection termination message with the
                bit set.
        type: str

    ipaddress:
        description:
            - "The new IP address of the service."
        type: str

    weight:
        description:
            - >-
                Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its
                with the service determines how much the monitor contributes toward keeping the health of the service
                the value configured for the Monitor Threshold parameter.
            - "Minimum value = C(1)"
            - "Maximum value = C(100)"
        type: str

    monitor_name_svc:
        description:
            - "Name of the monitor bound to the specified service."
            - "Minimum length =  1"
        type: str

    riseapbrstatsmsgcode:
        description:
            - "The code indicating the rise apbr status."
        type: int

    delay:
        description:
            - >-
                Time, in seconds, allocated to the Citrix ADC for a graceful shutdown of the service. During this
                new requests are sent to the service only for clients who already have persistent sessions on the
                Requests from new clients are load balanced among other available services. After the delay time
                no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
        type: str

    graceful:
        description:
            - >-
                Shut down gracefully, not accepting any new connections, and disabling the service when all of its
                are closed.
        type: bool

    all:
        description:
            - "Display both user-configured and dynamically learned services."
        type: bool

    Internal:
        description:
            - "Display only dynamically learned services."
        type: bool


    disabled:
        description:
            - When set to C(true) the service state will be set to C(disabled).
            - When set to C(false) the service state will be set to C(enabled).
        type: bool
        default: false

    ignore_monitors:
        description:
            - A list of monitor names to ignore when syncing monitors for the service
            - Used to ignore default monitors that cannot be unbound from the service
        type: list
        default:
            - tcp-default
            - ping-default
            - default-path-monitor

    monitor_bindings:
        description: A list of monitor to bind to the service
        suboptions:
            description: List of monitor bindings attributes.
            type: list
            elements: dict
            suboptions:
                monitor_name:
                    description:
                        - "The monitor Names."
                    type: str
                monstate:
                    choices:
                        - 'enabled'
                        - 'disabled'
                    description:
                        - "The configured state (enable/disable) of the monitor on this server."
                    type: str
                weight:
                    description:
                        - >-
                            Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its
                            with the service determines how much the monitor contributes toward keeping the health of the service
                            the value configured for the Monitor Threshold parameter.
                        - "Minimum value = C(1)"
                        - "Maximum value = C(100)"
                    type: str
                passive:
                    description:
                        - >-
                            Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision
                            threshold is breached.
                    type: bool

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
# Monitor monitor-1 must have been already setup

- name: Setup http service
  gather_facts: False
  delegate_to: localhost
  citrix_adc_service:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    name: service-http-1
    servicetype: HTTP
    ipaddress: 10.78.0.1
    port: 80

    monitor_bindings:
      - monitor-1
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

diff:
    description: A dictionary with a list of differences between the actual configured object and the configuration specified in the module

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
    loglines,
    NitroAPIFetcher
)

class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)
        self.main_nitro_class = 'service'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'service': {
                'attributes_list': [
                    'name',
                    'ip',
                    'servername',
                    'servicetype',
                    'port',
                    'cleartextport',
                    'cachetype',
                    'maxclient',
                    'healthmonitor',
                    'maxreq',
                    'cacheable',
                    'cip',
                    'cipheader',
                    'usip',
                    'pathmonitor',
                    'pathmonitorindv',
                    'useproxyport',
                    'sc',
                    'sp',
                    'rtspsessionidremap',
                    'clttimeout',
                    'svrtimeout',
                    'customserverid',
                    'serverid',
                    'cka',
                    'tcpb',
                    'cmp',
                    'maxbandwidth',
                    'accessdown',
                    'monthreshold',
                    'downstateflush',
                    'tcpprofilename',
                    'httpprofilename',
                    'contentinspectionprofilename',
                    'hashid',
                    'comment',
                    'appflowlog',
                    'netprofile',
                    'td',
                    'processlocal',
                    'dnsprofilename',
                    'monconnectionclose',
                    'ipaddress',
                    'weight',
                    'monitor_name_svc',
                    'riseapbrstatsmsgcode',
                    'delay',
                    'graceful',
                    'all',
                    'Internal',
                ],
                'transforms': {
                    'healthmonitor': lambda v: 'YES' if v else 'NO',
                    'cacheable': lambda v: 'YES' if v else 'NO',
                    'cip': lambda v: v.upper(),
                    'usip': lambda v: 'YES' if v else 'NO',
                    'pathmonitor': lambda v: 'YES' if v else 'NO',
                    'pathmonitorindv': lambda v: 'YES' if v else 'NO',
                    'useproxyport': lambda v: 'YES' if v else 'NO',
                    'sc': lambda v: 'ON' if v else 'OFF',
                    'sp': lambda v: 'ON' if v else 'OFF',
                    'rtspsessionidremap': lambda v: 'ON' if v else 'OFF',
                    'cka': lambda v: 'YES' if v else 'NO',
                    'tcpb': lambda v: 'YES' if v else 'NO',
                    'cmp': lambda v: 'YES' if v else 'NO',
                    'accessdown': lambda v: 'YES' if v else 'NO',
                    'downstateflush': lambda v: v.upper(),
                    'appflowlog': lambda v: v.upper(),
                    'processlocal': lambda v: v.upper(),
                    'graceful': lambda v: 'YES' if v else 'NO',
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'name',
                ],
                'non_updateable_attributes': [
                    'ip',
                    'servername',
                    'servicetype',
                    'port',
                    'cleartextport',
                    'cachetype',
                    'state',
                    'td',
                    'riseapbrstatsmsgcode',
                    'delay',
                    'graceful',
                    'all',
                    'Internal',
                    'newname',
                ],
            },
            'monitor_bindings': {
                'attributes_list': [
                    'monitor_name',
                    'monstate',
                    'weight',
                    'passive',
                ],
                'transforms': {
                    'monstate': lambda v: v.upper(),
                    'weight': lambda v: str(v),
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'monitor_name',
                    'name',
                ]
            }
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.calculate_configured_service()
        self.calculate_configured_monitor_bindings()

    def calculate_configured_service(self):
        log('ModuleExecutor.calculate_configured_service()')
        self.configured_service= {}
        for attribute in self.attribute_config['service']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['service']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_service[attribute] = value

        log('calculated configured service%s' % self.configured_service)

    def calculate_configured_monitor_bindings(self):
        log('ModuleExecutor.calculate_configured_monitor_bindings()')
        self.configured_monitor_bindings = []
        if self.module.params.get('monitor_bindings') is None:
            return

        for monitor_binding in self.module.params['monitor_bindings']:
            member = {}
            member['name'] = self.module.params['name']
            for attribute in self.attribute_config['monitor_bindings']['attributes_list']:
                # Disregard null values
                value = monitor_binding.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['monitor_bindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                member[attribute] = value
            self.configured_monitor_bindings.append(member)
        log('calculated configured monitor bindings %s' % self.configured_monitor_bindings)

    def service_exists(self):
        log('ModuleExecutor.service_exists()')
        result = self.fetcher.get('service', self.module.params['name'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            return True
        elif result['nitro_errorcode'] == 344:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def create_service(self):
        log('ModuleExecutor.create_service()')

        post_data = copy.deepcopy(self.configured_service)

        # Need to copy ipaddress to the ip attribute just for the create function
        if 'ip' not in post_data and 'ipaddress' in post_data:
            post_data['ip'] = post_data['ipaddress']

        post_data = {
            'service': post_data
        }

        result = self.fetcher.post(post_data=post_data, resource='service')
        log('post data: %s' % post_data)
        log('result of post: %s' % result)
        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def update_service(self):
        log('ModuleExecutor.update_service()')

        # Catching trying to change non updateable attributes is done in self.service_identical()
        put_payload = copy.deepcopy(self.configured_service)
        for attribute in self.attribute_config['service']['non_updateable_attributes']:
            if attribute in put_payload:
                del put_payload[attribute]
        # Check that non updateable values have not changed
        put_data = {
            'service': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='service')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def service_identical(self):
        log('ModuleExecutor.service_identical()')
        result = self.fetcher.get('service', self.module.params['name'])
        retrieved_object = result['data']['service'][0]

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        non_updateable_list = []
        for attribute in self.configured_service.keys():
            retrieved_value = retrieved_object.get(attribute)
            configured_value = self.configured_service.get(attribute)
            if retrieved_value != configured_value:
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                diff_list.append('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['service']['non_updateable_attributes']:
                    non_updateable_list.append(attribute)

        self.module_result['diff_list'] = diff_list
        if non_updateable_list != []:
            msg = 'Cannot change value for the following non updateable attributes %s' % non_updateable_list
            self.module.fail_json(msg=msg, **self.module_result)

        if diff_list != []:
            return False
        else:
            return True

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.service_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('Service does not exist. Will create.')
                self.create_service()
        else:
            if not self.service_identical():
                log('Existing service does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_service()
            else:
                log('Existing service has identical values to configured.')

        self.sync_bindings()

    def delete_service(self):

        result = self.fetcher.delete(resource='service', id=self.module.params['name'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.service_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_service()

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def get_existing_monitor_bindings(self):
        log('ModuleExecutor.get_existing_monitor_bindings()')
        result = self.fetcher.get('service_lbmonitor_binding', self.module.params['name'])

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'service_lbmonitor_binding' in result['data']:
            return result['data']['service_lbmonitor_binding']
        else:
            return []

    def add_monitor_binding(self, configured_dict):
        log('ModuleExecutor.add_monitor_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.configured_service['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['monitor_bindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'service_lbmonitor_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='service_lbmonitor_binding',
            id=self.configured_service['name'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_monitor_binding(self, configured_dict):
        log('ModuleExecutor.delete_monitor_binding()')

        monitor_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['monitor_bindings']['delete_id_attributes']:
            value = monitor_binding.get(attribute)
            if value is not None:
                args[attribute] = value

        result = self.fetcher.delete(
            resource='service_lbmonitor_binding',
            id=self.configured_service['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def monitor_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.monitor_binding_identical()')

        ret_val = True
        for key in configured.keys():
            configured_value = configured.get(key)
            retrieved_value = retrieved.get(key)
            if configured_value != retrieved_value:
                str_tuple = (
                    key,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                log('Monitor binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_monitor_bindings(self):
        log('ModuleExecutor.sync_monitor_bindings()')

        try:
            existing_monitor_bindings = self.get_existing_monitor_bindings()
        except NitroException as e:
            if e.errorcode == 344:
                log('Parent Service does not exist. Nothing to do for binding.')
                return
            else:
                raise

        log('existing_monitor_bindings %s' % existing_monitor_bindings)

        # Exclude the ignored monitors
        filtered_monitor_bindings = []
        for monitor in existing_monitor_bindings:
            if monitor['monitor_name'] in self.module.params.get('ignore_monitors', []):
                continue
            filtered_monitor_bindings.append(monitor)

        log('filtered_monitor_bindings %s' % filtered_monitor_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_monitor_binding in filtered_monitor_bindings:
            for configured_monitor_binding in self.configured_monitor_bindings:
                if self.monitor_binding_identical(configured_monitor_binding, existing_monitor_binding):
                    configured_already_present.append(configured_monitor_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.delete_monitor_binding(existing_monitor_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_monitor_binding in self.configured_monitor_bindings:
            if configured_monitor_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.add_monitor_binding(configured_monitor_binding)


    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        self.sync_monitor_bindings()

    def do_state_change(self):
        log('ModuleExecutor.do_state_change()')
        if self.module.check_mode:
            return

        # Fallthrough
        operation_attributes = [
            'graceful',
            'delay',
        ]
        post_data = {
            'service': {
                'name': self.configured_service['name'],
            }
        }
        for attribute in operation_attributes:
            value = self.configured_service.get(attribute)
            if value is not None:
                post_data['service'][attribute] = value

        disabled = self.module.params['disabled']
        args = {}
        if disabled:
            action = 'disable'
        else:
            action = 'enable'

        log('disable/enable post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='service', action=action)
        log('result of post %s' % result)

        if result['http_response_data']['status'] != 200:
            msg = 'Disable/Enable operation failed'
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
                self.do_state_change()
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
        ip=dict(type='str'),
        servername=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[
                'HTTP',
                'FTP',
                'TCP',
                'UDP',
                'SSL',
                'SSL_BRIDGE',
                'SSL_TCP',
                'DTLS',
                'NNTP',
                'RPCSVR',
                'DNS',
                'ADNS',
                'SNMP',
                'RTSP',
                'DHCPRA',
                'ANY',
                'SIP_UDP',
                'SIP_TCP',
                'SIP_SSL',
                'DNS_TCP',
                'ADNS_TCP',
                'MYSQL',
                'MSSQL',
                'ORACLE',
                'RADIUS',
                'RADIUSListener',
                'RDP',
                'DIAMETER',
                'SSL_DIAMETER',
                'TFTP',
                'SMPP',
                'PPTP',
                'GRE',
                'SYSLOGTCP',
                'SYSLOGUDP',
                'FIX',
                'SSL_FIX',
                'USER_TCP',
                'USER_SSL_TCP',
                'QUIC',
                'IPFIX',
                'LOGSTREAM',
            ]
        ),
        port=dict(type='int'),
        cleartextport=dict(type='int'),
        cachetype=dict(
            type='str',
            choices=[
                'TRANSPARENT',
                'REVERSE',
                'FORWARD',
            ]
        ),
        maxclient=dict(type='str'),
        healthmonitor=dict(type='bool'),
        maxreq=dict(type='str'),
        cacheable=dict(type='bool'),
        cip=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        cipheader=dict(type='str'),
        usip=dict(type='bool'),
        pathmonitor=dict(type='bool'),
        pathmonitorindv=dict(type='bool'),
        useproxyport=dict(type='bool'),
        sc=dict(type='bool'),
        sp=dict(type='bool'),
        rtspsessionidremap=dict(type='bool'),
        clttimeout=dict(type='int'),
        svrtimeout=dict(type='int'),
        customserverid=dict(type='str'),
        serverid=dict(type='str'),
        cka=dict(type='bool'),
        tcpb=dict(type='bool'),
        cmp=dict(type='bool'),
        maxbandwidth=dict(type='str'),
        accessdown=dict(type='bool'),
        monthreshold=dict(type='str'),
        downstateflush=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        contentinspectionprofilename=dict(type='str'),
        hashid=dict(type='str'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        netprofile=dict(type='str'),
        td=dict(type='str'),
        processlocal=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        dnsprofilename=dict(type='str'),
        monconnectionclose=dict(
            type='str',
            choices=[
                'RESET',
                'FIN',
            ]
        ),
        ipaddress=dict(type='str'),
        weight=dict(type='str'),
        monitor_name_svc=dict(type='str'),
        riseapbrstatsmsgcode=dict(type='int'),
        delay=dict(type='str'),
        graceful=dict(type='bool'),
        all=dict(type='bool'),
        Internal=dict(type='bool'),

        disabled=dict(
            type='bool',
            default=False,
        ),
        ignore_monitors=dict(
            type='list',
            default=list([
                'tcp-default',
                'ping-default',
                'default-path-monitor',
            ]),
        ),

        monitor_bindings=dict(
            type='list',
            elements='dict',
            options=dict(
                monitor_name=dict(type='str'),
                monstate=dict(
                    type='str',
                    choices=[
                        'enabled',
                        'disabled',
                    ]
                ),
                weight=dict(type='str'),
                passive=dict(type='bool'),
            ),
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
