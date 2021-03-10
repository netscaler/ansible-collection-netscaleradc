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
module: citrix_adc_cs_vserver
short_description: Manage content switching vserver
description:
    - Manage content switching vserver
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - >-
                Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore
                character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon
                at sign (@), equal sign (=), and hyphen (-) characters.
            - "Cannot be changed after the CS virtual server is created."
            - "The following requirement applies only to the Citrix ADC CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                my server or my server).
            - "Minimum length =  1"
        type: str

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of
            - "Minimum value = C(0)"
            - "Maximum value = C(4094)"
        type: str

    servicetype:
        choices:
            - 'HTTP'
            - 'SSL'
            - 'TCP'
            - 'FTP'
            - 'RTSP'
            - 'SSL_TCP'
            - 'UDP'
            - 'DNS'
            - 'SIP_UDP'
            - 'SIP_TCP'
            - 'SIP_SSL'
            - 'ANY'
            - 'RADIUS'
            - 'RDP'
            - 'MYSQL'
            - 'MSSQL'
            - 'DIAMETER'
            - 'SSL_DIAMETER'
            - 'DNS_TCP'
            - 'ORACLE'
            - 'SMPP'
            - 'PROXY'
        description:
            - "Protocol used by the virtual server."
        type: str

    ipv46:
        description:
            - "IP address of the content switching virtual server."
            - "Minimum length =  1"
        type: str

    targettype:
        choices:
            - 'GSLB'
        description:
            - "Virtual server target type."
        type: str

    dnsrecordtype:
        choices:
            - 'A'
            - 'AAAA'
            - 'CNAME'
            - 'NAPTR'
        description:
            - "."
        type: str

    persistenceid:
        description:
            - "."
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    ippattern:
        description:
            - >-
                IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual
                The IP Mask parameter specifies which part of the destination IP address is matched against the
                Mutually exclusive with the IP Address parameter.
            - >-
                For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is
                (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20
                in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to
                You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
            - >-
                If a destination IP address matches more than one IP pattern, the pattern with the longest match is
                and the associated virtual server processes the request. For example, if the virtual servers, vs1 and
                have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a
                IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP
                matches two or more virtual servers to the same extent, the request is processed by the virtual
                whose port number matches the port number in the request.
        type: str

    ipmask:
        description:
            - >-
                IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing
                octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first
                bits or the last n bits of the destination IP address in a client request are to be matched with the
                bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
        type: str

    range:
        description:
            - >-
                Number of consecutive IP addresses, starting with the address specified by the IP Address parameter,
                include in a range of addresses assigned to this virtual server.
            - "Minimum value = C(1)"
            - "Maximum value = C(254)"
        type: str

    port:
        description:
            - "Port number for content switching virtual server."
            - "Minimum value = C(1)"
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    ipset:
        description:
            - >-
                The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current
                vserver.
            - "Minimum length =  1"
        type: str

    stateupdate:
        choices:
            - 'ENABLED'
            - 'DISABLED'
            - 'UPDATEONBACKENDUPDATE'
        description:
            - >-
                Enable state updates for a specific content switching virtual server. By default, the Content
                virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to
                This parameter interacts with the global setting as follows:
            - "Global Level | Vserver Level | Result"
            - "ENABLED      ENABLED        ENABLED"
            - "ENABLED      DISABLED       ENABLED"
            - "DISABLED     ENABLED        ENABLED"
            - "DISABLED     DISABLED       DISABLED"
            - >-
                If you want to enable state updates for only some content switching virtual servers, be sure to
                the state update parameter.
        type: str

    cacheable:
        description:
            - >-
                Use this option to specify whether a virtual server, used for load balancing or content switching,
                requests to the cache redirection virtual server before sending it to the configured servers.
        type: bool

    redirecturl:
        description:
            - >-
                URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the
                server should be either HTTP or SSL.
            - >-
                Caution: Make sure that the domain in the URL does not match the domain specified for a content
                policy. If it does, requests are continuously redirected to the unavailable virtual server.
            - "Minimum length =  1"
        type: str

    clttimeout:
        description:
            - "Idle time, in seconds, after which the client connection is terminated. The default values are:"
            - "180 seconds for HTTP/SSL-based services."
            - "9000 seconds for other TCP-based services."
            - "120 seconds for DNS-based services."
            - "120 seconds for other UDP-based services."
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: int

    precedence:
        choices:
            - 'RULE'
            - 'URL'
        description:
            - >-
                Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual
                With the default (RULE) setting, incoming requests are evaluated against the rule-based content
                policies. If none of the rules match, the URL in the request is evaluated against the URL-based
                switching policies.
        type: str

    casesensitive:
        description:
            - >-
                Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON
                the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by
                switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the same target.
        type: bool

    somethod:
        choices:
            - 'CONNECTION'
            - 'DYNAMICCONNECTION'
            - 'BANDWIDTH'
            - 'HEALTH'
            - 'NONE'
        description:
            - >-
                Type of spillover used to divert traffic to the backup virtual server when the primary virtual server
                the spillover threshold. Connection spillover is based on the number of connections. Bandwidth
                is based on the total Kbps of incoming and outgoing traffic.
        type: str

    sopersistence:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Maintain source-IP based persistence on primary and backup virtual servers."
        type: str

    sopersistencetimeout:
        description:
            - "Time-out value, in minutes, for spillover persistence."
            - "Minimum value = C(2)"
            - "Maximum value = C(1440)"
        type: str

    sothreshold:
        description:
            - >-
                Depending on the spillover method, the maximum number of connections or the maximum total bandwidth
                that a virtual server can handle before spillover occurs.
            - "Minimum value = C(1)"
            - "Maximum value = C(4294967287)"
        type: str

    sobackupaction:
        choices:
            - 'DROP'
            - 'ACCEPT'
            - 'REDIRECT'
        description:
            - >-
                Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or
        type: str

    redirectportrewrite:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "State of port rewrite while performing HTTP redirect."
        type: str

    downstateflush:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Flush all active transactions associated with a virtual server whose state transitions from UP to
                Do not enable this option for applications that must complete their transactions.
        type: str

    backupvserver:
        description:
            - >-
                Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or
                (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
                (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup virtual
                is created. You can assign a different backup virtual server or rename the existing virtual server.
            - "The following requirement applies only to the Citrix ADC CLI:"
            - "If the name includes one or more spaces, enclose the name in double or single quotation marks."
            - "Minimum length =  1"
        type: str

    disableprimaryondown:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Continue forwarding the traffic to backup virtual server even after the primary server comes UP from
                DOWN state.
        type: str

    insertvserveripport:
        choices:
            - 'OFF'
            - 'VIPADDR'
            - 'V6TOV4MAPPING'
        description:
            - >-
                Insert the virtual server's VIP address and port number in the request header. Available values
                as follows:
            - "VIPADDR - Header contains the vserver's IP address and port number without any translation."
            - "OFF     - The virtual IP and port header insertion option is disabled."
            - >-
                V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the
                and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns
                command.
        type: str

    vipheader:
        description:
            - "Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter."
            - "Minimum length =  1"
        type: str

    rtspnat:
        description:
            - "Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections."
        type: bool

    authenticationhost:
        description:
            - >-
                FQDN of the authentication virtual server. The service type of the virtual server should be either
                or SSL.
            - "Minimum length =  3"
            - "Maximum length =  252"
        type: str

    authentication:
        description:
            - "Authenticate users who request a connection to the content switching virtual server."
        type: bool

    listenpolicy:
        description:
            - >-
                String specifying the listen policy for the content switching virtual server. Can be either the name
                an existing expression or an in-line expression.
        type: str

    listenpriority:
        description:
            - >-
                Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If
                request matches the listen policies of more than one virtual server the virtual server whose listen
                has the highest priority (the lowest priority number) accepts the request.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    authn401:
        description:
            - "Enable HTTP 401-response based authentication."
        type: bool

    authnvsname:
        description:
            - >-
                Name of authentication virtual server that authenticates the incoming user requests to this content
                virtual server. .
            - "Minimum length =  1"
            - "Maximum length =  252"
        type: str

    push:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Process traffic with the push virtual server that is bound to this content switching virtual server
                by the Push VServer parameter). The service type of the push virtual server should be either HTTP or
        type: str

    pushvserver:
        description:
            - >-
                Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes
                received on the client-facing load balancing virtual server.
            - "Minimum length =  1"
        type: str

    pushlabel:
        description:
            - >-
                Expression for extracting the label from the response received from server. This string can be either
                existing rule name or an inline expression. The service type of the virtual server should be either
                or SSL.
        type: str

    pushmulticlients:
        description:
            - >-
                Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
        type: bool

    tcpprofilename:
        description:
            - "Name of the TCP profile containing TCP configuration settings for the virtual server."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    httpprofilename:
        description:
            - >-
                Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service
                of the virtual server should be either HTTP or SSL.
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    dbprofilename:
        description:
            - "Name of the DB profile."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    oracleserverversion:
        choices:
            - '10G'
            - '11G'
        description:
            - "Oracle server version."
        type: str

    comment:
        description:
            - "Information about this virtual server."
        type: str

    mssqlserverversion:
        choices:
            - '70'
            - '2000'
            - '2000SP1'
            - '2005'
            - '2008'
            - '2008R2'
            - '2012'
            - '2014'
        description:
            - "The version of the MSSQL server."
        type: str

    l2conn:
        description:
            - "Use L2 Parameters to identify a connection."
        type: bool

    mysqlprotocolversion:
        description:
            - "The protocol version returned by the mysql vserver."
        type: str

    mysqlserverversion:
        description:
            - "The server version string returned by the mysql vserver."
            - "Minimum length =  1"
            - "Maximum length =  31"
        type: str

    mysqlcharacterset:
        description:
            - "The character set returned by the mysql vserver."
        type: str

    mysqlservercapabilities:
        description:
            - "The server capabilities returned by the mysql vserver."
        type: str

    appflowlog:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Enable logging appflow flow information."
        type: str

    netprofile:
        description:
            - "The name of the network profile."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    icmpvsrresponse:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - "Can be active or passive."
        type: str

    rhistate:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - "A host route is injected according to the setting on the virtual servers"
            - >-
                * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always
                the hostroute.
            - >-
                * If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even
                one virtual server is UP.
            - >-
                * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if
                virtual server set to ACTIVE is UP.
        type: str

    authnprofile:
        description:
            - "Name of the authentication profile to be used when authentication is turned on."
        type: str

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the
                processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    persistencetype:
        choices:
            - 'SOURCEIP'
            - 'COOKIEINSERT'
            - 'SSLSESSION'
            - 'NONE'
        description:
            - "Type of persistence for the virtual server. Available settings function as follows:"
            - "* SOURCEIP - Connections from the same client IP address belong to the same persistence session."
            - >-
                * COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from
                server, belong to the same persistence session.
            - "* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session."
        type: str

    persistmask:
        description:
            - "Persistence mask for IP based persistence types, for IPv4 virtual servers."
            - "Minimum length =  1"
        type: str

    v6persistmasklen:
        description:
            - "Persistence mask for IP based persistence types, for IPv6 virtual servers."
            - "Minimum value = C(1)"
            - "Maximum value = C(128)"
        type: str

    timeout:
        description:
            - "Time period for which a persistence session is in effect."
            - "Minimum value = C(0)"
            - "Maximum value = C(1440)"
        type: int

    cookiename:
        description:
            - >-
                Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of
                with a maximum of 32 characters. If not specified, cookie name is internally generated.
        type: str

    persistencebackup:
        choices:
            - 'SOURCEIP'
            - 'NONE'
        description:
            - >-
                Backup persistence type for the virtual server. Becomes operational if the primary persistence
                fails.
        type: str

    backuppersistencetimeout:
        description:
            - "Time period for which backup persistence is in effect."
            - "Minimum value = C(2)"
            - "Maximum value = C(1440)"
        type: str

    domainname:
        description:
            - "Domain name for which to change the time to live (TTL) and/or backup service IP address."
            - "Minimum length =  1"
        type: str

    ttl:
        description:
            - "."
            - "Minimum value = C(1)"
        type: str

    backupip:
        description:
            - "."
            - "Minimum length =  1"
        type: str

    cookiedomain:
        description:
            - "."
            - "Minimum length =  1"
        type: str

    cookietimeout:
        description:
            - "."
            - "Minimum value = C(0)"
            - "Maximum value = C(1440)"
        type: str

    sitedomainttl:
        description:
            - "."
            - "Minimum value = C(1)"
        type: str


    disabled:
        description:
            - When set to C(true) the server state will be set to C(disabled).
            - When set to C(false) the server state will be set to C(enabled).
        type: bool
        default: false

    lbvserver:
        type: str
        description:
            - The default Load Balancing virtual server.

    ssl_certkey:
        type: str
        description:
            - The name of the ssl certificate that is bound to this service.
            - The ssl certificate must already exist.
            - Creating the certificate can be done with the M(citrix_adc_ssl_certkey) module.
            - This option is only applicable only when C(servicetype) is C(SSL).

    policybindings:
        type: list
        elements: dict
        description:
            - List of cspolicy bindings.
        suboptions:
            policyname:
                description:
                    - "Policies bound to this vserver."
                type: str
            targetlbvserver:
                description:
                    - "target vserver name."
                type: str
            priority:
                description:
                    - "Priority for the policy."
                type: str
            gotopriorityexpression:
                description:
                    - >-
                        Expression specifying the priority of the next policy which will get evaluated if the current policy
                        evaluates to TRUE.
                type: str
            bindpoint:
                choices:
                    - 'REQUEST'
                    - 'RESPONSE'
                    - 'ICA_REQUEST'
                    - 'OTHERTCP_REQUEST'
                description:
                    - "The bindpoint to which the policy is bound."
                type: str
            invoke:
                description:
                    - "Invoke flag."
                type: bool
            labeltype:
                choices:
                    - 'reqvserver'
                    - 'resvserver'
                    - 'policylabel'
                description:
                    - "The invocation type."
                type: str
            labelname:
                description:
                    - "Name of the label invoked."
                type: str


    appfw_policybindings:
        elements: dict
        type: list
        description:
            - List of appfw policy bindings
        suboptions:
            policyname:
                description:
                    - "Policies bound to this vserver."
                type: str
            priority:
                description:
                    - "Priority for the policy."
                type: str
            gotopriorityexpression:
                description:
                    - >-
                        Expression specifying the priority of the next policy which will get evaluated if the current policy
                        evaluates to TRUE.
                type: str
            bindpoint:
                choices:
                    - 'REQUEST'
                    - 'RESPONSE'
                    - 'ICA_REQUEST'
                    - 'OTHERTCP_REQUEST'
                description:
                    - "The bindpoint to which the policy is bound."
                type: str
            invoke:
                description:
                    - "Invoke flag."
                type: bool
            labeltype:
                choices:
                    - 'reqvserver'
                    - 'resvserver'
                    - 'policylabel'
                description:
                    - "The invocation type."
                type: str
            labelname:
                description:
                    - "Name of the label invoked."
                type: str
            name:
                description:
                    - "Name of the content switching virtual server to which the content switching policy applies."
                    - "Minimum length =  1"
                type: str
            targetlbvserver:
                description:
                    - >-
                        Name of the Load Balancing virtual server to which the content is switched, if policy rule is
                        to be TRUE. Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1 Note: Use
                        parameter only in case of Content Switching policy bind operations to a CS vserver.
                    - "Minimum length =  1"
                type: str

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
# policy_1 must have been already created with the citrix_adc_cs_policy module
# lbvserver_1 must have been already created with the citrix_adc_lb_vserver module

- name: Setup content switching vserver
  delegate_to: localhost
  citrix_adc_cs_vserver:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    state: present

    name: cs_vserver_1
    ipv46: 192.168.1.1
    port: 80
    servicetype: HTTP

    policybindings:
      - policyname: policy_1
        targetlbvserver: lbvserver_1
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
        self.main_nitro_class = 'csvserver'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'csvserver': {
                'attributes_list': [
                    'name',
                    'td',
                    'servicetype',
                    'ipv46',
                    'targettype',
                    'dnsrecordtype',
                    'persistenceid',
                    'ippattern',
                    'ipmask',
                    'range',
                    'port',
                    'ipset',
                    'stateupdate',
                    'cacheable',
                    'redirecturl',
                    'clttimeout',
                    'precedence',
                    'casesensitive',
                    'somethod',
                    'sopersistence',
                    'sopersistencetimeout',
                    'sothreshold',
                    'sobackupaction',
                    'redirectportrewrite',
                    'downstateflush',
                    'backupvserver',
                    'disableprimaryondown',
                    'insertvserveripport',
                    'vipheader',
                    'rtspnat',
                    'authenticationhost',
                    'authentication',
                    'listenpolicy',
                    'listenpriority',
                    'authn401',
                    'authnvsname',
                    'push',
                    'pushvserver',
                    'pushlabel',
                    'pushmulticlients',
                    'tcpprofilename',
                    'httpprofilename',
                    'dbprofilename',
                    'oracleserverversion',
                    'comment',
                    'mssqlserverversion',
                    'l2conn',
                    'mysqlprotocolversion',
                    'mysqlserverversion',
                    'mysqlcharacterset',
                    'mysqlservercapabilities',
                    'appflowlog',
                    'netprofile',
                    'icmpvsrresponse',
                    'rhistate',
                    'authnprofile',
                    'dnsprofilename',
                    'persistencetype',
                    'persistmask',
                    'v6persistmasklen',
                    'timeout',
                    'cookiename',
                    'persistencebackup',
                    'backuppersistencetimeout',
                    'domainname',
                    'ttl',
                    'backupip',
                    'cookiedomain',
                    'cookietimeout',
                    'sitedomainttl',
                ],
                'transforms': {
                    'cacheable': lambda v: 'YES' if v else 'NO',
                    'casesensitive': lambda v: 'ON' if v else 'OFF',
                    'sopersistence': lambda v: v.upper(),
                    'redirectportrewrite': lambda v: v.upper(),
                    'downstateflush': lambda v: v.upper(),
                    'disableprimaryondown': lambda v: v.upper(),
                    'rtspnat': lambda v: 'ON' if v else 'OFF',
                    'authentication': lambda v: 'ON' if v else 'OFF',
                    'authn401': lambda v: 'ON' if v else 'OFF',
                    'push': lambda v: v.upper(),
                    'pushmulticlients': lambda v: 'YES' if v else 'NO',
                    'l2conn': lambda v: 'ON' if v else 'OFF',
                    'appflowlog': lambda v: v.upper(),
                    'clttimeout': str,
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'name',
                ],
                'non_updateable_attributes': [
                    'td',
                    'servicetype',
                    'targettype',
                    'range',
                    'port',
                    'state',
                    'newname',
                ],
            },
            'policybindings': {
                'attributes_list': [
                    'policyname',
                    'targetlbvserver',
                    'priority',
                    'gotopriorityexpression',
                    'bindpoint',
                    'invoke',
                    'labeltype',
                    'labelname',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'policyname',
                    'priority',
                    'bindpoint',
                ]
            },
            'appfwpolicy_bindings': {
                'attributes_list': [
                    'policyname',
                    'priority',
                    'gotopriorityexpression',
                    'bindpoint',
                    'invoke',
                    'labeltype',
                    'labelname',
                    'targetlbvserver',
                ],
                'transforms': {
                    'priority': str,
                    'gotopriorityexpression': str,
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'policyname',
                    'priority',
                    'bindpoint',
                    'name',
                ]
            }
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.prepared_list = []

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_csvserver()
        self.calculate_configured_cspolicy_bindings()
        self.calculate_configured_appfwpolicy_bindings()

    def calculate_configured_csvserver(self):
        log('ModuleExecutor.calculate_configured_csvserver()')
        self.configured_csvserver = {}
        for attribute in self.attribute_config['csvserver']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['csvserver']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_csvserver[attribute] = value

        log('calculated configured csvserver %s' % self.configured_csvserver)

    def calculate_configured_cspolicy_bindings(self):
        log('ModuleExecutor.calculate_configured_cspolicy_bindings()')
        self.configured_cspolicy_bindings = []
        if self.module.params.get('policybindings') is None:
            return
        for cspolicy in self.module.params['policybindings']:
            binding = {}
            binding['name'] = self.module.params['name']
            for attribute in self.attribute_config['policybindings']['attributes_list']:
                # Disregard null values
                value = cspolicy.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['policybindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_cspolicy_bindings.append(binding)
        log('calculated configured cspolicy bindings %s' % self.configured_cspolicy_bindings)

    def calculate_configured_appfwpolicy_bindings(self):
        log('ModuleExecutor.calculate_configured_appfwpolicy_bindings()')
        self.configured_appfwpolicy_bindings = []

        if self.module.params.get('appfw_policybindings') is None:
            return

        for appfwpolicy in self.module.params['appfw_policybindings']:
            binding = {}
            binding['name'] = self.module.params['name']
            for attribute in self.attribute_config['appfwpolicy_bindings']['attributes_list']:
                # Disregard null values
                value = appfwpolicy.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['appfwpolicy_bindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_appfwpolicy_bindings.append(binding)
        log('calculated configured appfw policy binidings %s' % self.configured_appfwpolicy_bindings)

    def csvserver_exists(self):
        log('ModuleExecutor.csvserver_exists()')
        result = self.fetcher.get('csvserver', self.module.params['name'])

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

    def create_csvserver(self):
        log('ModuleExecutor.create_csvserver()')

        post_data = {
            'csvserver': self.configured_csvserver
        }

        result = self.fetcher.post(post_data=post_data, resource='csvserver')
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

    def update_csvserver(self):
        log('ModuleExecutor.update_csvserver()')

        # Catching trying to change non updateable attributes is done in self.csvserver_identical()
        put_payload = copy.deepcopy(self.configured_csvserver)
        for attribute in self.configured_csvserver.keys():
            if attribute in self.attribute_config['csvserver']['non_updateable_attributes']:
                del put_payload[attribute]

        put_data = {
            'csvserver': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='csvserver')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def csvserver_identical(self):
        log('ModuleExecutor.csvserver_identical()')
        result = self.fetcher.get('csvserver', self.module.params['name'])
        retrieved_object = result['data']['csvserver'][0]

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        non_updateable_list = []
        # Iterate over keys that already exist in the playbook
        for attribute in self.configured_csvserver.keys():
            retrieved_value = retrieved_object.get(attribute)
            configured_value = self.configured_csvserver.get(attribute)
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
                entry = 'Attribute "%s" differs. Playbook parameter: "%s". Retrieved NITRO object: "%s"' % (attribute, configured_value, retrieved_value)
                self.prepared_list.append(entry)
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['csvserver']['non_updateable_attributes']:
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
        if not self.csvserver_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Create cs vserver')
            if not self.module.check_mode:
                log('Csvserver group does not exist. Will create.')
                self.create_csvserver()
        else:
            if not self.csvserver_identical():
                log('Existing csvserver does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_csvserver()
            else:
                log('Existing csvserver has identical values to configured.')

        # This will also take into account check mode
        self.sync_bindings()

    def delete_csvserver(self):
        log('ModuleExecutor.delete_csvserver()')

        # First unbind any existing appfwpolicies
        self.configured_appfwpolicy_bindings = []
        self.sync_appfwpolicy_bindings()

        result = self.fetcher.delete(resource='csvserver', id=self.module.params['name'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.csvserver_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Delete cs vserver')
            if not self.module.check_mode:
                self.delete_csvserver()

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def get_existing_cspolicy_bindings(self):
        log('ModuleExecutor.get_existing_cspolicy_bindings()')
        result = self.fetcher.get('csvserver_cspolicy_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'csvserver_cspolicy_binding' in result['data']:
            return result['data']['csvserver_cspolicy_binding']
        else:
            return []

    def add_cspolicy_binding(self, configured_dict):
        log('ModuleExecutor.add_cspolicy_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.module.params['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['policybindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'csvserver_cspolicy_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='csvserver_cspolicy_binding',
            id=self.module.params['name'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_cspolicy_binding(self, configured_dict):
        log('ModuleExecutor.delete_cspolicy_binding()')

        cspolicy_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['policybindings']['delete_id_attributes']:
            value = cspolicy_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='csvserver_cspolicy_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def cspolicy_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.cspolicy_binding_identical()')

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
                log('Cspolicy binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_cspolicy_bindings(self):
        log('ModuleExecutor.sync_cspolicy_bindings()')

        # Parent csvserver should already exist
        existing_cspolicy_bindings = self.get_existing_cspolicy_bindings()

        log('existing_cspolicy_bindings %s' % existing_cspolicy_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_cspolicy_binding in existing_cspolicy_bindings:
            for configured_cspolicy_binding in self.configured_cspolicy_bindings:
                if self.cspolicy_binding_identical(configured_cspolicy_binding, existing_cspolicy_binding):
                    configured_already_present.append(configured_cspolicy_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                reduced_dict = self.reduced_dict(
                    existing_cspolicy_binding,
                    self.attribute_config['policybindings']['attributes_list']
                )
                self.prepared_list.append('Delete policy binding %s' % reduced_dict)
                if not self.module.check_mode:
                    self.delete_cspolicy_binding(existing_cspolicy_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_cspolicy_binding in self.configured_cspolicy_bindings:
            if configured_cspolicy_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            reduced_dict = self.reduced_dict(
                configured_cspolicy_binding,
                self.attribute_config['policybindings']['attributes_list']
            )
            self.prepared_list.append('Add policy binding %s' % reduced_dict)
            if not self.module.check_mode:
                self.add_cspolicy_binding(configured_cspolicy_binding)

    def get_existing_appfwpolicy_bindings(self):
        log('ModuleExecutor.get_existing_appfwpolicy_bindings()')
        result = self.fetcher.get('csvserver_appfwpolicy_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'csvserver_appfwpolicy_binding' in result['data']:
            return result['data']['csvserver_appfwpolicy_binding']
        else:
            return []

    def appfwpolicy_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.appfwpolicy_binding_identical()')

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
                log('Appfwpolicy binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def add_appfwpolicy_binding(self, configured_dict):
        log('ModuleExecutor.add_appfwpolicy_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.module.params['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['appfwpolicy_bindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'csvserver_appfwpolicy_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='csvserver_appfwpolicy_binding',
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_appfwpolicy_binding(self, configured_dict):
        log('ModuleExecutor.delete_appfwpolicy_binding()')

        appfwpolicy_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['appfwpolicy_bindings']['delete_id_attributes']:
            value = appfwpolicy_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='csvserver_appfwpolicy_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def sync_appfwpolicy_bindings(self):
        log('ModuleExecutor.sync_appfwpolicy_bindings()')

        # Parent csvserver should already exist
        existing_appfwpolicy_bindings = self.get_existing_appfwpolicy_bindings()

        log('existing_appfwpolicy_bindings %s' % existing_appfwpolicy_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_appfwpolicy_binding in existing_appfwpolicy_bindings:
            for configured_appfwpolicy_binding in self.configured_appfwpolicy_bindings:
                if self.appfwpolicy_binding_identical(configured_appfwpolicy_binding, existing_appfwpolicy_binding):
                    configured_already_present.append(configured_appfwpolicy_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                reduced_dict = self.reduced_dict(
                    existing_appfwpolicy_binding,
                    self.attribute_config['appfwpolicy_bindings']['attributes_list']
                )
                self.prepared_list.append('Delete appfw policy binding %s' % reduced_dict)
                if not self.module.check_mode:
                    self.delete_appfwpolicy_binding(existing_appfwpolicy_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_appfwpolicy_binding in self.configured_appfwpolicy_bindings:
            if configured_appfwpolicy_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            reduced_dict = self.reduced_dict(
                configured_appfwpolicy_binding,
                self.attribute_config['appfwpolicy_bindings']['attributes_list']
            )
            self.prepared_list.append('Add appfw policy binding %s' % reduced_dict)
            if not self.module.check_mode:
                self.add_appfwpolicy_binding(configured_appfwpolicy_binding)

    def add_sslcertkey_binding(self, sslcertkey):
        log('ModuleExecutor.add_sslcertkey_binding()')

        put_data = {
            'sslvserver_sslcertkey_binding': {
                'vservername': self.module.params['name'],
                'certkeyname': sslcertkey,
            }
        }

        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='sslvserver_sslcertkey_binding',
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_sslcertkey_binding(self, sslcertkey):
        log('ModuleExecutor.delete_sslcertkey_binding()')

        args = {
            'certkeyname': sslcertkey,
        }

        result = self.fetcher.delete(
            resource='sslvserver_sslcertkey_binding',
            id=self.module.params['name'],
            args=args
        )

    def sync_sslcertkey_bindings(self):
        log('ModuleExecutor.sync_sslcertkey_bindings()')

        # Read for the existing binding
        bound_lbvserver = None
        result = self.fetcher.get('sslvserver_sslcertkey_binding', self.module.params['name'])

        if result['nitro_errorcode'] in [461, 1544]:
            bound_sslcertkeys = []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'sslvserver_sslcertkey_binding' in result['data']:
            bound_sslcertkeys = result['data']['sslvserver_sslcertkey_binding']
        else:
            bound_sslcertkeys = []

        configured_sslcertkey = self.module.params.get('ssl_certkey')
        found_configured = False

        # Delete all keys that do not match
        for binding in bound_sslcertkeys:
            if binding['certkeyname'] != configured_sslcertkey:
                self.module_result['changed'] = True
                self.prepared_list.append('Delete ssl_certkey binding %s' % binding['certkeyname'])
                if not self.module.check_mode:
                    self.delete_sslcertkey_binding(binding['certkeyname'])
            else:
                found_configured = True

        # Add if not found
        if configured_sslcertkey is not None and not found_configured:
            self.module_result['changed'] = True
            self.prepared_list.append('Add ssl_certkey binding %s' % configured_sslcertkey)
            if not self.module.check_mode:
                self.add_sslcertkey_binding(configured_sslcertkey)
        pass

    def add_default_lbvserver(self, lbvserver_name):
        log('ModuleExecutor.add_default_lbvserver()')

        put_data = {
            'csvserver_lbvserver_binding': {
                'name': self.module.params['name'],
                'lbvserver': lbvserver_name,
            }
        }

        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='csvserver_lbvserver_binding',
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_default_lbvserver(self, lbvserver_name):
        log('ModuleExecutor.delete_default_lbvserver()')

        args = {
            'lbvserver': lbvserver_name
        }

        result = self.fetcher.delete(
            resource='csvserver_lbvserver_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def sync_default_lbvserver(self):
        log('ModuleExecutor.sync_default_lbvserver()')

        # Read for the existing binding
        bound_lbvserver = None
        result = self.fetcher.get('csvserver_lbvserver_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            bound_lbvserver = None
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'csvserver_lbvserver_binding' in result['data']:
            bound_lbvserver = result['data']['csvserver_lbvserver_binding'][0]
        else:
            bound_lbvserver = None

        configured_lbvserver = self.module.params.get('lbvserver')

        # When to delete
        if bound_lbvserver is not None and configured_lbvserver != bound_lbvserver['lbvserver']:
            self.module_result['changed'] = True
            self.prepared_list.append('Delete default lb vserver binding %s' % bound_lbvserver['lbvserver'])
            if not self.module.check_mode:
                self.delete_default_lbvserver(bound_lbvserver['lbvserver'])

        # When to add
        if configured_lbvserver is not None:
            if bound_lbvserver is None or configured_lbvserver != bound_lbvserver['lbvserver']:
                self.module_result['changed'] = True
                self.prepared_list.append('Add default lb vserver binding %s' % configured_lbvserver)
                if not self.module.check_mode:
                    self.add_default_lbvserver(configured_lbvserver)

    def reduced_dict(self, dictionary, include_keys):
        reduced = {}
        for key in dictionary:
            if key in include_keys:
                reduced[key] = dictionary[key]

        return reduced

    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        self.sync_cspolicy_bindings()
        self.sync_appfwpolicy_bindings()
        self.sync_sslcertkey_bindings()
        self.sync_default_lbvserver()

    def do_state_change(self):
        log('ModuleExecutor.do_state_change()')
        if self.module.check_mode:
            return

        # Fallthrough
        post_data = {
            'csvserver': {
                'name': self.configured_csvserver['name'],
            }
        }

        disabled = self.module.params['disabled']

        if disabled:
            action = 'disable'
        else:
            action = 'enable'

        log('disable/enable post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='csvserver', action=action)
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

            if self.module._diff:
                self.module_result['diff'] = {'prepared': '\n'.join(self.prepared_list)}

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
        td=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[
                'HTTP',
                'SSL',
                'TCP',
                'FTP',
                'RTSP',
                'SSL_TCP',
                'UDP',
                'DNS',
                'SIP_UDP',
                'SIP_TCP',
                'SIP_SSL',
                'ANY',
                'RADIUS',
                'RDP',
                'MYSQL',
                'MSSQL',
                'DIAMETER',
                'SSL_DIAMETER',
                'DNS_TCP',
                'ORACLE',
                'SMPP',
                'PROXY',
            ]
        ),
        ipv46=dict(type='str'),
        targettype=dict(
            type='str',
            choices=[
                'GSLB',
            ]
        ),
        dnsrecordtype=dict(
            type='str',
            choices=[
                'A',
                'AAAA',
                'CNAME',
                'NAPTR',
            ]
        ),
        persistenceid=dict(type='str'),
        ippattern=dict(type='str'),
        ipmask=dict(type='str'),
        range=dict(type='str'),
        port=dict(type='int'),
        ipset=dict(type='str'),
        stateupdate=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
                'UPDATEONBACKENDUPDATE',
            ]
        ),
        cacheable=dict(type='bool'),
        redirecturl=dict(type='str'),
        clttimeout=dict(type='int'),
        precedence=dict(
            type='str',
            choices=[
                'RULE',
                'URL',
            ]
        ),
        casesensitive=dict(type='bool'),
        somethod=dict(
            type='str',
            choices=[
                'CONNECTION',
                'DYNAMICCONNECTION',
                'BANDWIDTH',
                'HEALTH',
                'NONE',
            ]
        ),
        sopersistence=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        sopersistencetimeout=dict(type='str'),
        sothreshold=dict(type='str'),
        sobackupaction=dict(
            type='str',
            choices=[
                'DROP',
                'ACCEPT',
                'REDIRECT',
            ]
        ),
        redirectportrewrite=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        downstateflush=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        backupvserver=dict(type='str'),
        disableprimaryondown=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        insertvserveripport=dict(
            type='str',
            choices=[
                'OFF',
                'VIPADDR',
                'V6TOV4MAPPING',
            ]
        ),
        vipheader=dict(type='str'),
        rtspnat=dict(type='bool'),
        authenticationhost=dict(type='str'),
        authentication=dict(type='bool'),
        listenpolicy=dict(type='str'),
        listenpriority=dict(type='str'),
        authn401=dict(type='bool'),
        authnvsname=dict(type='str'),
        push=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        pushvserver=dict(type='str'),
        pushlabel=dict(type='str'),
        pushmulticlients=dict(type='bool'),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        dbprofilename=dict(type='str'),
        oracleserverversion=dict(
            type='str',
            choices=[
                '10G',
                '11G',
            ]
        ),
        comment=dict(type='str'),
        mssqlserverversion=dict(
            type='str',
            choices=[
                '70',
                '2000',
                '2000SP1',
                '2005',
                '2008',
                '2008R2',
                '2012',
                '2014',
            ]
        ),
        l2conn=dict(type='bool'),
        mysqlprotocolversion=dict(type='str'),
        mysqlserverversion=dict(type='str'),
        mysqlcharacterset=dict(type='str'),
        mysqlservercapabilities=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        netprofile=dict(type='str'),
        icmpvsrresponse=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ]
        ),
        rhistate=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ]
        ),
        authnprofile=dict(type='str'),
        dnsprofilename=dict(type='str'),
        persistencetype=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'COOKIEINSERT',
                'SSLSESSION',
                'NONE',
            ]
        ),
        persistmask=dict(type='str'),
        v6persistmasklen=dict(type='str'),
        timeout=dict(type='int'),
        cookiename=dict(type='str'),
        persistencebackup=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'NONE',
            ]
        ),
        backuppersistencetimeout=dict(type='str'),
        domainname=dict(type='str'),
        ttl=dict(type='str'),
        backupip=dict(type='str'),
        cookiedomain=dict(type='str'),
        cookietimeout=dict(type='str'),
        sitedomainttl=dict(type='str'),

        disabled=dict(
            type='bool',
            default=False,
        ),
        lbvserver=dict(
            type='str',
        ),
        ssl_certkey=dict(type='str'),

        policybindings=dict(
            type='list',
            elements='dict',
            options=dict(
                policyname=dict(type='str'),
                targetlbvserver=dict(type='str'),
                priority=dict(type='str'),
                gotopriorityexpression=dict(type='str'),
                bindpoint=dict(
                    type='str',
                    choices=[
                        'REQUEST',
                        'RESPONSE',
                        'ICA_REQUEST',
                        'OTHERTCP_REQUEST',
                    ]
                ),
                invoke=dict(type='bool'),
                labeltype=dict(
                    type='str',
                    choices=[
                        'reqvserver',
                        'resvserver',
                        'policylabel',
                    ]
                ),
                labelname=dict(type='str'),
            ),
        ),

        appfw_policybindings=dict(
            type='list',
            elements='dict',
            options=dict(
                policyname=dict(type='str'),
                priority=dict(type='str'),
                gotopriorityexpression=dict(type='str'),
                bindpoint=dict(
                    type='str',
                    choices=[
                        'REQUEST',
                        'RESPONSE',
                        'ICA_REQUEST',
                        'OTHERTCP_REQUEST',
                    ]
                ),
                invoke=dict(type='bool'),
                labeltype=dict(
                    type='str',
                    choices=[
                        'reqvserver',
                        'resvserver',
                        'policylabel',
                    ]
                ),
                labelname=dict(type='str'),
                name=dict(type='str'),
                targetlbvserver=dict(type='str'),
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
