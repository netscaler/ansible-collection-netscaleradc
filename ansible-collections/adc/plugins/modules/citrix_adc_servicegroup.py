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
module: citrix_adc_servicegroup
short_description: Manage service group configuration in Netscaler
description:
    - Manage service group configuration in Netscaler.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

version_added: "2.4.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    servicegroupname:
        description:
            - >-
                Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must
                only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and
                (-) characters. Can be changed after the name is created.
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
            - "Protocol used to exchange data with the service."
        type: str

    cachetype:
        choices:
            - 'TRANSPARENT'
            - 'REVERSE'
            - 'FORWARD'
        description:
            - "Cache type supported by the cache server."
        type: str

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of
            - "Minimum value = C(0)"
            - "Maximum value = C(4094)"
        type: str

    maxclient:
        description:
            - "Maximum number of simultaneous open connections for the service group."
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967294)"
        type: str

    maxreq:
        description:
            - "Maximum number of requests that can be sent on a persistent connection to the service group."
            - "Note: Connection requests beyond this value are rejected."
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    cacheable:
        description:
            - "Use the transparent cache redirection virtual server to forward the request to the cache server."
            - "Note: Do not set this parameter if you set the Cache Type."
        type: bool

    cip:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Insert the Client IP header in requests forwarded to the service."
        type: str

    cipheader:
        description:
            - >-
                Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client
                parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of
                IP Header parameter or the value set by the set ns config command is used as client's IP header name.
            - "Minimum length =  1"
        type: str

    usip:
        description:
            - >-
                Use client's IP address as the source IP address when initiating connection to the server. With the
                setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the
                IP address to initiate server side connections.
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

    healthmonitor:
        description:
            - "Monitor the health of this service.  Available settings function as follows:"
            - "YES - Send probes to check the health of the service."
            - >-
                NO - Do not send probes to check the health of the service. With the NO option, the appliance shows
                service as UP at all times.
        type: bool

    sc:
        description:
            - "State of the SureConnect feature for the service group."
        type: bool

    sp:
        description:
            - "Enable surge protection for the service group."
        type: bool

    rtspsessionidremap:
        description:
            - "Enable RTSP session ID mapping for the service group."
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

    cka:
        description:
            - "Enable client keep-alive for the service group."
        type: bool

    tcpb:
        description:
            - "Enable TCP buffering for the service group."
        type: bool

    cmp:
        description:
            - "Enable compression for the specified service."
        type: bool

    maxbandwidth:
        description:
            - "Maximum bandwidth, in Kbps, allocated for all the services in the service group."
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967287)"
        type: str

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
                Flush all active transactions associated with all the services in the service group whose state
                from UP to DOWN. Do not enable this option for applications that must complete their transactions.
        type: str

    tcpprofilename:
        description:
            - "Name of the TCP profile that contains TCP configuration settings for the service group."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    httpprofilename:
        description:
            - "Name of the HTTP profile that contains HTTP configuration settings for the service group."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    comment:
        description:
            - "Any information about the service group."
        type: str

    appflowlog:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Enable logging of AppFlow information for the specified service group."
        type: str

    netprofile:
        description:
            - "Network profile for the service group."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    autoscale:
        choices:
            - 'DISABLED'
            - 'DNS'
            - 'POLICY'
            - 'CLOUD'
            - 'API'
        description:
            - "Auto scale option for a servicegroup."
        type: str

    memberport:
        description:
            - "member port."
        type: int

    autodisablegraceful:
        description:
            - >-
                Indicates graceful shutdown of the service. System will wait for all outstanding connections to this
                to be closed before disabling the service.
        type: bool

    autodisabledelay:
        description:
            - >-
                The time allowed (in seconds) for a graceful shutdown. During this period, new connections or
                will continue to be sent to this service for clients who already have a persistent session on the
                Connections or requests from fresh or new clients who do not yet have a persistence sessions on the
                will not be sent to the service. Instead, they will be load balanced among other available services.
                the delay time expires, no new requests or connections will be sent to the service.
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

    servername:
        description:
            - "Name of the server to which to bind the service group."
            - "Minimum length =  1"
        type: str

    port:
        description:
            - "Server port number."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    weight:
        description:
            - >-
                Weight to assign to the servers in the service group. Specifies the capacity of the servers relative
                the other servers in the load balancing configuration. The higher the weight, the higher the
                of requests sent to the service.
            - "Minimum value = C(1)"
            - "Maximum value = C(100)"
        type: str

    customserverid:
        description:
            - "The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID."
        type: str

    serverid:
        description:
            - "The  identifier for the service. This is used when the persistency type is set to Custom Server ID."
        type: str

    hashid:
        description:
            - >-
                The hash identifier for the service. This must be unique for each service. This parameter is used by
                based load balancing methods.
            - "Minimum value = C(1)"
        type: str

    nameserver:
        description:
            - >-
                Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use
                global nameserver.
        type: str

    dbsttl:
        description:
            - >-
                Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates
                use the TTL received in DNS response for monitors.
        type: str

    monitor_name_svc:
        description:
            - "Name of the monitor bound to the service group. Used to assign a weight to the monitor."
            - "Minimum length =  1"
        type: str

    dup_weight:
        description:
            - "weight of the monitor that is bound to servicegroup."
            - "Minimum value = C(1)"
        type: str

    riseapbrstatsmsgcode:
        description:
            - "The code indicating the rise apbr status."
        type: int

    delay:
        description:
            - >-
                Time, in seconds, allocated for a shutdown of the services in the service group. During this period,
                requests are sent to the service only for clients who already have persistent sessions on the
                Requests from new clients are load balanced among other available services. After the delay time
                no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
        type: str

    graceful:
        description:
            - "Wait for all existing connections to the service to terminate before shutting down the service."
        type: bool

    includemembers:
        description:
            - >-
                Display the members of the listed service groups in addition to their settings. Can be specified when
                service group name is provided in the command. In that case, the details displayed for each service
                are identical to the details displayed when a service group name is provided, except that bound
                are not displayed.
        type: bool


    disabled:
        description:
            - When set to C(true) the server state will be set to C(disabled).
            - When set to C(false) the server state will be set to C(enabled).
        type: bool
        default: false

    servicemembers:
        description: A list of dictionaries describing each service member of the service group.
        type: dict
        suboptions:
            mode:
                type: str
                description:
                    - "If mode is C(exact):"
                    - Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.
                    - Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.
                    - >-
                        Any existing bindings that are defined in the attributes list but have differing attribute values
                        will first be deleted and then recreated with the defined attribute values.
                    - "If mode is C(bind):"
                    - Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - "If mode is C(unbind):"
                    - Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - "If mode is C(dsapi):"
                    - The desired state API will be used to bind/unbind members.
                    - As far as selection is concerned it is identical to the C(exact) method.
                    - In this mode a result of C(changed=true) will always be reported.
                    - >-
                        The reason is in order to capitalize on the speed of the desired state API we do not read
                        the existing members from the servicegroup.
                    - As a result of this we are unable to assert if the declared configuration will actually change the target ADC configuration.
                    - Note that in order to use this mode the servicegroup must have set the following option value I(autoscale=API).
                    - "Also for this mode only the following suboptions can be used: I(ip), I(port), I(weight), I(state)"
                choices:
                    - exact
                    - bind
                    - unbind
                    - dsapi
            attributes:
                description: List of service members attributes.
                type: list
                elements: dict
                suboptions:
                    ip:
                        description:
                            - "IP Address."
                        type: str
                    port:
                        description:
                            - "Server port number."
                            - "Range 1 - 65535"
                            - "* in CLI is represented as 65535 in NITRO API"
                        type: int
                    weight:
                        description:
                            - >-
                                Weight to assign to the servers in the service group. Specifies the capacity of the servers relative
                                the other servers in the load balancing configuration. The higher the weight, the higher the
                                of requests sent to the service.
                            - "Minimum value = C(1)"
                            - "Maximum value = C(100)"
                        type: str
                    servername:
                        description:
                            - "Name of the server to which to bind the service group."
                            - "Minimum length =  1"
                        type: str
                    customserverid:
                        description:
                            - "The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID."
                        type: str
                    serverid:
                        description:
                            - "The  identifier for the service. This is used when the persistency type is set to Custom Server ID."
                        type: str
                    state:
                        choices:
                            - 'enabled'
                            - 'disabled'
                        description:
                            - "Initial state of the service group."
                        type: str
                    hashid:
                        description:
                            - >-
                                The hash identifier for the service. This must be unique for each service. This parameter is used by
                                based load balancing methods.
                            - "Minimum value = C(1)"
                        type: str
                    nameserver:
                        description:
                            - >-
                                Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use
                                global nameserver.
                        type: str
                    dbsttl:
                        description:
                            - >-
                                Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates
                                use the TTL received in DNS response for monitors.
                        type: str


    monitor_bindings:
        description: A list of monitor to bind to the servicegroup
        type: dict
        suboptions:
            mode:
                type: str
                description:
                    - "If mode is C(exact):"
                    - Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.
                    - Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.
                    - >-
                        Any existing bindings that are defined in the attributes list but have differing attribute values
                        will first be deleted and then recreated with the defined attribute values.
                    - "If mode is C(bind):"
                    - Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.
                    - >-
                        Any bindings defined in the attributes list that exist on the target Citrix ADC but have
                        different attribute values will first be deleted and then recreated with the defined attribute values.
                    - Existing bindings that are not on the attributes list remain unaffected.
                    - "If mode is C(unbind):"
                    - Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.
                    - Existing bindings that are not on the attributes list remain unaffected.
                choices:
                    - exact
                    - bind
                    - unbind
            attributes:
                description: List of monitor bindings attributes.
                type: list
                elements: dict
                suboptions:
                    monitor_name:
                        description:
                            - "Monitor name."
                        type: str
                    monstate:
                        choices:
                            - 'enabled'
                            - 'disabled'
                        description:
                            - "Monitor state."
                        type: str
                    weight:
                        description:
                            - >-
                                Weight to assign to the servers in the service group. Specifies the capacity of the servers relative
                                the other servers in the load balancing configuration. The higher the weight, the higher the
                                of requests sent to the service.
                            - "Minimum value = C(1)"
                            - "Maximum value = C(100)"
                        type: str
                    passive:
                        description:
                            - >-
                                Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision
                                threshold is breached.
                        type: bool
                    port:
                        description:
                            - "Port number of the service. Each service must have a unique port number."
                            - "Range 1 - 65535"
                            - "* in CLI is represented as 65535 in NITRO API"
                        type: int
                    customserverid:
                        description:
                            - >-
                                Unique service identifier. Used when the persistency type for the virtual server is set to Custom
                                ID.
                        type: str
                    serverid:
                        description:
                            - "The  identifier for the service. This is used when the persistency type is set to Custom Server ID."
                        type: str
                    state:
                        choices:
                            - 'enabled'
                            - 'disabled'
                        description:
                            - "Initial state of the service after binding."
                        type: str
                    hashid:
                        description:
                            - "Unique numerical identifier used by hash based load balancing methods to identify a service."
                            - "Minimum value = C(1)"
                        type: str
                    nameserver:
                        description:
                            - >-
                                Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use
                                global nameserver.
                        type: str
                    dbsttl:
                        description:
                            - >-
                                Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates
                                use the TTL received in DNS response for monitors.
                        type: str

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
# The LB Monitors monitor-1 and monitor-2 must already exist
# Service members defined by C(ip) must not redefine an existing server's ip address.
# Service members defined by C(servername) must already exist.

- name: Setup http service with ip members
  delegate_to: localhost
  citrix_adc_servicegroup:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    servicegroupname: service-group-1
    servicetype: HTTP
    servicemembers:
        mode: exact
        attributes:
          - ip: 10.78.78.78
            port: 80
            weight: 50
          - ip: 10.79.79.79
            port: 80
            weight: 40
          - servername: server-1
            port: 80
            weight: 10

    monitor_bindings:
        mode: exact
        attributes:
          - monitor_name: monitor-1
            weight: 50
          - monitor_name: monitor-2
            weight: 50
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
    loglines,
    NitroAPIFetcher
)

class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)
        self.main_nitro_class = 'servicegroup'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'servicegroup': {
                'attributes_list': [
                    'servicegroupname',
                    'servicetype',
                    'cachetype',
                    'td',
                    'maxclient',
                    'maxreq',
                    'cacheable',
                    'cip',
                    'cipheader',
                    'usip',
                    'pathmonitor',
                    'pathmonitorindv',
                    'useproxyport',
                    'healthmonitor',
                    'sc',
                    'sp',
                    'rtspsessionidremap',
                    'clttimeout',
                    'svrtimeout',
                    'cka',
                    'tcpb',
                    'cmp',
                    'maxbandwidth',
                    'monthreshold',
                    'downstateflush',
                    'tcpprofilename',
                    'httpprofilename',
                    'comment',
                    'appflowlog',
                    'netprofile',
                    'autoscale',
                    'memberport',
                    'autodisablegraceful',
                    'autodisabledelay',
                    'monconnectionclose',
                    'servername',
                    'port',
                    'weight',
                    'customserverid',
                    'serverid',
                    'hashid',
                    'nameserver',
                    'dbsttl',
                    'monitor_name_svc',
                    'dup_weight',
                    'riseapbrstatsmsgcode',
                    'delay',
                    'graceful',
                    'includemembers',
                ],
                'transforms': {
                    'cacheable': lambda v: 'YES' if v else 'NO',
                    'cip': lambda v: v.upper(),
                    'usip': lambda v: 'YES' if v else 'NO',
                    'pathmonitor': lambda v: 'YES' if v else 'NO',
                    'pathmonitorindv': lambda v: 'YES' if v else 'NO',
                    'useproxyport': lambda v: 'YES' if v else 'NO',
                    'healthmonitor': lambda v: 'YES' if v else 'NO',
                    'sc': lambda v: 'ON' if v else 'OFF',
                    'sp': lambda v: 'ON' if v else 'OFF',
                    'rtspsessionidremap': lambda v: 'ON' if v else 'OFF',
                    'cka': lambda v: 'YES' if v else 'NO',
                    'tcpb': lambda v: 'YES' if v else 'NO',
                    'cmp': lambda v: 'YES' if v else 'NO',
                    'downstateflush': lambda v: v.upper(),
                    'appflowlog': lambda v: v.upper(),
                    'autodisablegraceful': lambda v: 'YES' if v else 'NO',
                    'graceful': lambda v: 'YES' if v else 'NO',
                },
                'get_id_attributes': [
                    'servicegroupname',
                ],
                'delete_id_attributes': [
                    'servicegroupname',
                ],
                'non_updateable_attributes': [
                    'servicetype',
                    'cachetype',
                    'td',
                    'state',
                    'autoscale',
                    'memberport',
                    'riseapbrstatsmsgcode',
                    'delay',
                    'graceful',
                    'includemembers',
                    'newname',
                ],
            },
            'servicemembers': {
                'attributes_list': [
                    'ip',
                    'port',
                    'weight',
                    'servername',
                    'customserverid',
                    'serverid',
                    'state',
                    'hashid',
                    'nameserver',
                    'dbsttl',
                ],
                'transforms': {
                    'state': lambda v: v.upper(),
                    'weight': str,
                },
                'get_id_attributes': [
                    'servicegroupname',
                ],
                'delete_id_attributes': [
                    'ip',
                    'port',
                    'servername',
                    'servicegroupname',
                ]
            },
            'monitor_bindings': {
                'attributes_list': [
                    'monitor_name',
                    'monstate',
                    'weight',
                    'passive',
                    'port',
                    'customserverid',
                    'serverid',
                    'state',
                    'hashid',
                    'nameserver',
                    'dbsttl',
                ],
                'transforms': {
                    'monstate': lambda v: v.upper(),
                    'state': lambda v: v.upper(),
                    'weight': str,
                },
                'get_id_attributes': [
                    'servicegroupname',
                ],
                'delete_id_attributes': [
                    'monitor_name',
                    'servicegroupname',
                    'port',
                ]
            }
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.prepared_list = []

        self.calculate_configured_servicegroup()
        self.calculate_configured_servicemembers()
        self.calculate_configured_monitor_bindings()

    def calculate_configured_servicegroup(self):
        log('ModuleExecutor.calculate_configured_servicegroup()')
        self.configured_servicegroup = {}
        for attribute in self.attribute_config['servicegroup']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['servicegroup']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_servicegroup[attribute] = value

        log('calculated configured servicegroup %s' % self.configured_servicegroup)

    def calculate_configured_servicemembers(self):
        log('ModuleExecutor.calculate_configured_servicemembers()')
        self.configured_servicemembers = []
        if self.module.params.get('servicemembers') is None:
            return
        for servicemember in self.module.params['servicemembers']['attributes']:
            member = {}
            member['servicegroupname'] = self.module.params['servicegroupname']
            for attribute in self.attribute_config['servicemembers']['attributes_list']:
                # Disregard null values
                value = servicemember.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['servicemembers']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                member[attribute] = value
            self.configured_servicemembers.append(member)
        log('calculated configured service members %s' % self.configured_servicemembers)

    def calculate_configured_monitor_bindings(self):
        log('ModuleExecutor.calculate_configured_monitor_bindings()')
        self.configured_monitor_bindings = []
        if self.module.params.get('monitor_bindings') is None:
            return
        for monitor_binding in self.module.params['monitor_bindings']['attributes']:
            member = {}
            member['servicegroupname'] = self.module.params['servicegroupname']
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

    def servicegroup_exists(self):
        log('ModuleExecutor.servicegroup_exists()')
        result = self.fetcher.get('servicegroup', self.module.params['servicegroupname'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            return True
        elif result['nitro_errorcode'] == 258:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def _construct_present_values_dict(self):
        non_null_attributes = self._get_non_null_attributes()
        present_attributes = list(set(self.attribute_config['servicegroup']['attributes_list']) & set(non_null_attributes))
        values_dict = {}
        for attribute in present_attributes:
            if attribute in self.attribute_config['servicegroup']['transforms']:
                log('Found transform for %s' % attribute)
                configured_value = self.attribute_config['servicegroup']['transforms'][attribute](self.module.params[attribute])
            else:
                configured_value = self.module.params[attribute]
            values_dict[attribute] = configured_value
        return values_dict

    def create_servicegroup(self):
        log('ModuleExecutor.create_servicegroup()')

        post_data = {
            'servicegroup': self.configured_servicegroup
        }

        result = self.fetcher.post(post_data=post_data, resource='servicegroup')
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

    def update_servicegroup(self):
        log('ModuleExecutor.update_servicegroup()')

        # Catching trying to change non updateable attributes is done in self.servicegroup_identical()
        put_payload = copy.deepcopy(self.configured_servicegroup)
        for attribute in self.attribute_config['servicegroup']['non_updateable_attributes']:
            if attribute in put_payload:
                del put_payload[attribute]
        # Check that non updateable values have not changed
        put_data = {
            'servicegroup': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='servicegroup')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def _get_non_null_attributes(self):
        attributes_list = []
        for key in self.module.params.keys():
            if self.module.params.get(key) is not None:
                attributes_list.append(key)

        return attributes_list

    def servicegroup_identical(self):
        log('ModuleExecutor.servicegroup_identical()')
        result = self.fetcher.get('servicegroup', self.module.params['servicegroupname'])
        retrieved_object = result['data']['servicegroup'][0]

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        # Only compare present attributes
        non_null_attributes = self._get_non_null_attributes()
        present_attributes = list(set(self.attribute_config['servicegroup']['attributes_list']) & set(non_null_attributes))
        diff_list = []
        non_updateable_list = []
        for attribute in self.configured_servicegroup.keys():
            retrieved_value = retrieved_object.get(attribute)
            configured_value = self.configured_servicegroup.get(attribute)
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
                self.prepared_list.append('Attribute "%s" differs. Playbook parameter: "%s". Retrieved NITRO object: "%s"' % (attribute, configured_value, retrieved_value) )
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['servicegroup']['non_updateable_attributes']:
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
        if not self.servicegroup_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Create servicegroup')
            if not self.module.check_mode:
                log('Service group does not exist. Will create.')
                self.create_servicegroup()
        else:
            if not self.servicegroup_identical():
                log('Existing servicegroup does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_servicegroup()
            else:
                log('Existing servicegroup has identical values to configured.')

        self.sync_bindings()

    def delete_servicegroup(self):

        result = self.fetcher.delete(resource='servicegroup', id=self.module.params['servicegroupname'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.servicegroup_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Delete servicegroup')
            if not self.module.check_mode:
                self.delete_servicegroup()

    def get_existing_servicemembers(self):
        log('ModuleExecutor.get_existing_servicemembers()')
        result = self.fetcher.get('servicegroup_servicegroupmember_binding', self.module.params['servicegroupname'])

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'servicegroup_servicegroupmember_binding' in result['data']:
            return result['data']['servicegroup_servicegroupmember_binding']
        else:
            return []

    def servicemember_identical(self, configured, retrieved):
        log('ModuleExecutor.servicemember_identical()')

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
                log('Servicemember attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def add_servicemember(self, configured_dict):
        put_values = copy.deepcopy(configured_dict)
        put_values['servicegroupname'] = self.module.params['servicegroupname']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['servicemembers']['transforms'],
            values_dict=put_values
        )
        put_data = {'servicegroup_servicegroupmember_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='servicegroup_servicegroupmember_binding',
            id=self.module.params['servicegroupname'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_servicemember(self, configured_dict):
        log('ModuleExecutor.delete_servicemember()')
        servicemember = copy.deepcopy(configured_dict)
        # If both ip and servername are present favor servername
        if servicemember.get('ip') is not None and servicemember.get('servername') is not None:
            del servicemember['ip']

        args = {}
        for attribute in self.attribute_config['servicemembers']['delete_id_attributes']:
            value = servicemember.get(attribute)
            if value is not None:
                args[attribute] = value

        result = self.fetcher.delete(
            resource='servicegroup_servicegroupmember_binding',
            id=self.module.params['servicegroupname'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def apply_dsapi(self):
        log('ModuleExecutor.apply_dsapi()')

        members = []
        for configured in self.configured_servicemembers:
            member = copy.deepcopy(configured)
            del member['servicegroupname']
            members.append(member)

        put_data = {
            'servicegroup_servicegroupmemberlist_binding': {
                'servicegroupname': self.module.params['servicegroupname'],
                'members': members,
            }
        }
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='servicegroup_servicegroupmemberlist_binding',
        )

        log('put result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def sync_servicemembers(self):

        binding_key = 'servicemembers'
        binding_object = 'servicegroup_servicegroupmember_binding'

        def filter_delete_values_dict(existing_binding_values_dict):
            # If both ip and servername are present favor servername
            if existing_binding_values_dict.get('ip') is not None and existing_binding_values_dict.get('servername') is not None:
                del existing_binding_values_dict['ip']

        if self.module.params.get(binding_key) is None:
            return

        log('ModuleExecutor syncing binding %s' % binding_key)

        mode = self.module.params[binding_key]['mode']
        log('mode is %s' % mode)

        try:
            existing_servicemembers = self.get_existing_servicemembers()
        except NitroException as e:
            if e.errorcode == 258:
                existing_servicemembers = []
            else:
                raise

        log('existing_servicemembers %s' % existing_servicemembers)

        # First get the existing bindings
        configured_already_present = []
        if mode == 'exact':
            # Delete any binding that is not exactly as the configured
            for existing_servicemember in existing_servicemembers:
                for configured_servicemember in self.configured_servicemembers:
                    if self.servicemember_identical(configured_servicemember, existing_servicemember):
                        configured_already_present.append(configured_servicemember)
                        break
                else:
                    log('Will delete binding')
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        existing_servicemember,
                        self.attribute_config['servicemembers']['attributes_list']
                    )
                    self.prepared_list.append('Delete servicemember %s' % reduced_dict)
                    if not self.module.check_mode:
                        self.delete_servicemember(existing_servicemember)

            # Create the bindings objects that we marked in previous loop
            log('configured_already_present %s' % configured_already_present)
            for configured_servicemember in self.configured_servicemembers:
                if configured_servicemember in configured_already_present:
                    log('Configured binding already exists')
                    continue
                else:
                    log('Configured binding does not already exist')
                self.module_result['changed'] = True
                reduced_dict = self.reduced_dict(
                    configured_servicemember,
                    self.attribute_config['servicemembers']['attributes_list']
                )
                self.prepared_list.append('Add servicemember %s' % reduced_dict)
                if not self.module.check_mode:
                    self.add_servicemember(configured_servicemember)

        elif mode == 'bind':
            for configured_servicemember in self.configured_servicemembers:
                create_servicemember = True
                for existing_servicemember in existing_servicemembers:
                    if self.servicemember_identical(configured_servicemember, existing_servicemember):
                        create_servicemember = False
                        break
                if create_servicemember:
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        configured_servicemember,
                        self.attribute_config['servicemembers']['attributes_list']
                    )
                    self.prepared_list.append('Add servicemember %s' % reduced_dict)
                    if not self.module.check_mode:
                        self.add_servicemember(configured_servicemember)

        elif mode == 'unbind':
            for configured_servicemember in self.configured_servicemembers:
                delete_servicemember = False
                for existing_servicemember in existing_servicemembers:
                    if self.servicemember_identical(configured_servicemember, existing_servicemember):
                        delete_servicemember = True
                        break
                if delete_servicemember:
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        configured_servicemember,
                        self.attribute_config['servicemembers']['attributes_list']
                    )
                    self.prepared_list.append('Delete servicemember %s' % reduced_dict)
                    if not self.module.check_mode:
                        self.delete_servicemember(configured_servicemember)
        elif mode == 'dsapi':
            log('dsapi application')
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.apply_dsapi()

    def get_existing_monitor_bindings(self):
        log('ModuleExecutor.get_existing_monitor_bindings()')
        result = self.fetcher.get('servicegroup_lbmonitor_binding', self.module.params['servicegroupname'])

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'servicegroup_lbmonitor_binding' in result['data']:
            return result['data']['servicegroup_lbmonitor_binding']
        else:
            return []

    def add_monitor_binding(self, configured_dict):
        log('ModuleExecutor.add_monitor_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['servicegroupname'] = self.module.params['servicegroupname']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['monitor_bindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'servicegroup_lbmonitor_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='servicegroup_lbmonitor_binding',
            id=self.module.params['servicegroupname'],
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
            resource='servicegroup_lbmonitor_binding',
            id=self.module.params['servicegroupname'],
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

        if self.module.params.get('monitor_bindings') is None:
            return

        log('ModuleExecutor syncing monitor bindings')

        mode = self.module.params['monitor_bindings']['mode']

        try:
            existing_monitor_bindings = self.get_existing_monitor_bindings()
        except NitroException as e:
            if e.errorcode == 258:
                # Setting this to empty list for correct diff when creating servicegroup
                existing_monitor_bindings = []
            else:
                raise

        log('existing_monitor_bindings %s' % existing_monitor_bindings)

        # First get the existing bindings
        configured_already_present = []
        if mode == 'exact':
            # Delete any binding that is not exactly as the configured
            for existing_monitor_binding in existing_monitor_bindings:
                for configured_monitor_binding in self.configured_monitor_bindings:
                    if self.monitor_binding_identical(configured_monitor_binding, existing_monitor_binding):
                        configured_already_present.append(configured_monitor_binding)
                        break
                else:
                    log('Will delete binding')
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        existing_monitor_binding,
                        self.attribute_config['monitor_bindings']['attributes_list']
                    )
                    self.prepared_list.append('Delete monitor binding %s' % reduced_dict)
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
                reduced_dict = self.reduced_dict(
                    configured_monitor_binding,
                    self.attribute_config['monitor_bindings']['attributes_list']
                )
                self.prepared_list.append('Add monitor binding %s' % reduced_dict)
                if not self.module.check_mode:
                    self.add_monitor_binding(configured_monitor_binding)

        elif mode == 'bind':
            for configured_monitor_binding in self.configured_monitor_bindings:
                create_servicemember = True
                for existing_monitor_binding in existing_monitor_bindings:
                    if self.monitor_binding_identical(configured_monitor_binding, existing_monitor_binding):
                        create_servicemember = False
                        break
                if create_servicemember:
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        configured_monitor_binding,
                        self.attribute_config['monitor_bindings']['attributes_list']
                    )
                    self.prepared_list.append('Add monitor binding %s' % reduced_dict)
                    if not self.module.check_mode:
                        self.add_monitor_binding(configured_monitor_binding)

        elif mode == 'unbind':
            for configured_monitor_binding in self.configured_monitor_bindings:
                delete_servicemember = False
                for existing_monitor_binding in existing_monitor_bindings:
                    if self.monitor_binding_identical(configured_monitor_binding, existing_monitor_binding):
                        delete_servicemember = True
                        break
                if delete_servicemember:
                    self.module_result['changed'] = True
                    reduced_dict = self.reduced_dict(
                        configured_monitor_binding,
                        self.attribute_config['monitor_bindings']['attributes_list']
                    )
                    self.prepared_list.append('Delete monitor binding %s' % reduced_dict)
                    if not self.module.check_mode:
                        self.delete_servicemember(configured_monitor_binding)

    def reduced_dict(self, dictionary, include_keys):
        reduced = {}
        for key in dictionary:
            if key in include_keys:
                reduced[key] = dictionary[key]

        return reduced

    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        self.sync_servicemembers()
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
            'servicegroup': {
                'servicegroupname': self.configured_servicegroup['servicegroupname'],
            }
        }
        for attribute in operation_attributes:
            value = self.configured_servicegroup.get(attribute)
            if value is not None:
                post_data['servicegroup'][attribute] = value

        disabled = self.module.params['disabled']
        args = {}
        if disabled:
            action = 'disable'
        else:
            action = 'enable'

        log('disable/enable post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='servicegroup', action=action)
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

            if self.module._diff :
                self.module_result['diff'] = { 'prepared': '\n'.join(self.prepared_list) }

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
        servicegroupname=dict(type='str'),
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
        cachetype=dict(
            type='str',
            choices=[
                'TRANSPARENT',
                'REVERSE',
                'FORWARD',
            ]
        ),
        td=dict(type='str'),
        maxclient=dict(type='str'),
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
        healthmonitor=dict(type='bool'),
        sc=dict(type='bool'),
        sp=dict(type='bool'),
        rtspsessionidremap=dict(type='bool'),
        clttimeout=dict(type='int'),
        svrtimeout=dict(type='int'),
        cka=dict(type='bool'),
        tcpb=dict(type='bool'),
        cmp=dict(type='bool'),
        maxbandwidth=dict(type='str'),
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
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        netprofile=dict(type='str'),
        autoscale=dict(
            type='str',
            choices=[
                'DISABLED',
                'DNS',
                'POLICY',
                'CLOUD',
                'API',
            ]
        ),
        memberport=dict(type='int'),
        autodisablegraceful=dict(type='bool'),
        autodisabledelay=dict(type='str'),
        monconnectionclose=dict(
            type='str',
            choices=[
                'RESET',
                'FIN',
            ]
        ),
        servername=dict(type='str'),
        port=dict(type='int'),
        weight=dict(type='str'),
        customserverid=dict(type='str'),
        serverid=dict(type='str'),
        hashid=dict(type='str'),
        nameserver=dict(type='str'),
        dbsttl=dict(type='str'),
        monitor_name_svc=dict(type='str'),
        dup_weight=dict(type='str'),
        riseapbrstatsmsgcode=dict(type='int'),
        delay=dict(type='str'),
        graceful=dict(type='bool'),
        includemembers=dict(type='bool'),

        disabled=dict(
            type='bool',
            default=False,
        ),

        servicemembers=dict(
            type='dict',
            options=dict(
                mode=dict(type='str', choices=['exact', 'bind', 'unbind', 'dsapi']),
                attributes=dict(
                    type='list',
                    elements='dict',
                    options=dict(
                        ip=dict(type='str'),
                        port=dict(type='int'),
                        weight=dict(type='str'),
                        servername=dict(type='str'),
                        customserverid=dict(type='str'),
                        serverid=dict(type='str'),
                        state=dict(
                            type='str',
                            choices=[
                                'enabled',
                                'disabled',
                            ]
                        ),
                        hashid=dict(type='str'),
                        nameserver=dict(type='str'),
                        dbsttl=dict(type='str'),
                    ),
                ),
            )
        ),

        monitor_bindings=dict(
            type='dict',
            options=dict(
                mode=dict(type='str', choices=['exact', 'bind', 'unbind']),
                attributes=dict(
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
                        port=dict(type='int'),
                        customserverid=dict(type='str'),
                        serverid=dict(type='str'),
                        state=dict(
                            type='str',
                            choices=[
                                'enabled',
                                'disabled',
                            ]
                        ),
                        hashid=dict(type='str'),
                        nameserver=dict(type='str'),
                        dbsttl=dict(type='str'),
                    ),
                ),
            )
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
