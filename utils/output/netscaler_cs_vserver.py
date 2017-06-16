#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


DOCUMENTATION = '''
---
module: _
short_description: _
description:
    - _

version_added: 2.3.1

options:

    name:
        description:
            - >-
                Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore
                (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
                colon (:), at sign (@), equal sign (=), and hyphen (-) characters.
            - "Cannot be changed after the CS virtual server is created."
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, my server or my server).
            - "Minimum length = 1"

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID
                of 0.
            - "Minimum value = 0"
            - "Maximum value = 4094"

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
        description:
            - "Protocol used by the virtual server."

    ipv46:
        description:
            - "IP address of the content switching virtual server."
            - "Minimum length = 1"

    targettype:
        choices:
            - 'GSLB'
        description:
            - "Virtual server target type."

    dnsrecordtype:
        choices:
            - 'A'
            - 'AAAA'
            - 'CNAME'
            - 'NAPTR'
        description:
            - "."
            - "Default value: NSGSLB_IPV4"

    persistenceid:
        description:
            - "."
            - "Minimum value = 0"
            - "Maximum value = 65535"

    ippattern:
        description:
            - >-
                IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual
                server. The IP Mask parameter specifies which part of the destination IP address is matched against
                the pattern. Mutually exclusive with the IP Address parameter.
            - >-
                For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is
                255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with
                the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range
                from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as
                0.0.255.255 (a reverse mask).
            - >-
                If a destination IP address matches more than one IP pattern, the pattern with the longest match is
                selected, and the associated virtual server processes the request. For example, if the virtual
                servers, vs1 and vs2, have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255
                and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern
                of vs1. If a destination IP address matches two or more virtual servers to the same extent, the
                request is processed by the virtual server whose port number matches the port number in the request.

    ipmask:
        description:
            - >-
                IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing
                non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether
                the first n bits or the last n bits of the destination IP address in a client request are to be
                matched with the corresponding bits in the IP pattern. The former is called a forward mask. The
                latter is called a reverse mask.

    range:
        description:
            - >-
                Number of consecutive IP addresses, starting with the address specified by the IP Address parameter,
                to include in a range of addresses assigned to this virtual server.
            - "Default value: 1"
            - "Minimum value = 1"
            - "Maximum value = 254"

    port:
        description:
            - "Port number for content switching virtual server."
            - "Minimum value = 1"
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Initial state of the load balancing virtual server."
            - "Default value: ENABLED"

    stateupdate:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Enable state updates for a specific content switching virtual server. By default, the Content
                Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers
                bound to it. This parameter interacts with the global setting as follows:
            - "Global Level | Vserver Level | Result"
            - "ENABLED ENABLED ENABLED"
            - "ENABLED DISABLED ENABLED"
            - "DISABLED ENABLED ENABLED"
            - "DISABLED DISABLED DISABLED"
            - >-
                If you want to enable state updates for only some content switching virtual servers, be sure to
                disable the state update parameter.
            - "Default value: DISABLED"

    cacheable:
        description:
            - >-
                Use this option to specify whether a virtual server, used for load balancing or content switching,
                routes requests to the cache redirection virtual server before sending it to the configured servers.
            - "Default value: NO"

    redirecturl:
        description:
            - >-
                URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the
                virtual server should be either HTTP or SSL.
            - >-
                Caution: Make sure that the domain in the URL does not match the domain specified for a content
                switching policy. If it does, requests are continuously redirected to the unavailable virtual server.
            - "Minimum length = 1"

    clttimeout:
        description:
            - "Idle time, in seconds, after which the client connection is terminated. The default values are:"
            - "180 seconds for HTTP/SSL-based services."
            - "9000 seconds for other TCP-based services."
            - "120 seconds for DNS-based services."
            - "120 seconds for other UDP-based services."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    precedence:
        choices:
            - 'RULE'
            - 'URL'
        description:
            - >-
                Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual
                server. With the default (RULE) setting, incoming requests are evaluated against the rule-based
                content switching policies. If none of the rules match, the URL in the request is evaluated against
                the URL-based content switching policies.
            - "Default value: RULE"

    casesensitive:
        description:
            - >-
                Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON
                setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set
                by content switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the
                same target.
            - "Default value: ON"

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
                reaches the spillover threshold. Connection spillover is based on the number of connections.
                Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.

    sopersistence:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Maintain source-IP based persistence on primary and backup virtual servers."
            - "Default value: DISABLED"

    sopersistencetimeout:
        description:
            - "Time-out value, in minutes, for spillover persistence."
            - "Default value: 2"
            - "Minimum value = 2"
            - "Maximum value = 1440"

    sothreshold:
        description:
            - >-
                Depending on the spillover method, the maximum number of connections or the maximum total bandwidth
                (Kbps) that a virtual server can handle before spillover occurs.
            - "Minimum value = 1"
            - "Maximum value = 4294967287"

    sobackupaction:
        choices:
            - 'DROP'
            - 'ACCEPT'
            - 'REDIRECT'
        description:
            - >-
                Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or
                exists.

    redirectportrewrite:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "State of port rewrite while performing HTTP redirect."
            - "Default value: DISABLED"

    downstateflush:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Flush all active transactions associated with a virtual server whose state transitions from UP to
                DOWN. Do not enable this option for applications that must complete their transactions.
            - "Default value: ENABLED"

    backupvserver:
        description:
            - >-
                Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or
                underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.),
                space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the
                backup virtual server is created. You can assign a different backup virtual server or rename the
                existing virtual server.
            - "The following requirement applies only to the NetScaler CLI:"
            - "If the name includes one or more spaces, enclose the name in double or single quotation marks."
            - "Minimum length = 1"

    disableprimaryondown:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Continue forwarding the traffic to backup virtual server even after the primary server comes UP from
                the DOWN state.
            - "Default value: DISABLED"

    insertvserveripport:
        choices:
            - 'OFF'
            - 'VIPADDR'
            - 'V6TOV4MAPPING'
        description:
            - >-
                Insert the virtual server's VIP address and port number in the request header. Available values
                function as follows:
            - "VIPADDR - Header contains the vserver's IP address and port number without any translation."
            - "OFF - The virtual IP and port header insertion option is disabled."
            - >-
                V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the
                vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the
                set ns ip6 command.

    vipheader:
        description:
            - "Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter."
            - "Minimum length = 1"

    rtspnat:
        description:
            - "Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections."
            - "Default value: OFF"

    authenticationhost:
        description:
            - >-
                FQDN of the authentication virtual server. The service type of the virtual server should be either
                HTTP or SSL.
            - "Minimum length = 3"
            - "Maximum length = 252"

    authentication:
        description:
            - "Authenticate users who request a connection to the content switching virtual server."
            - "Default value: OFF"

    listenpolicy:
        description:
            - >-
                String specifying the listen policy for the content switching virtual server. Can be either the name
                of an existing expression or an in-line expression.
            - "Default value: \\"NONE\\""

    listenpriority:
        description:
            - >-
                Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If
                a request matches the listen policies of more than one virtual server the virtual server whose listen
                policy has the highest priority (the lowest priority number) accepts the request.
            - "Default value: 101"
            - "Minimum value = 0"
            - "Maximum value = 100"

    authn401:
        description:
            - "Enable HTTP 401-response based authentication."
            - "Default value: OFF"

    authnvsname:
        description:
            - >-
                Name of authentication virtual server that authenticates the incoming user requests to this content
                switching virtual server. .
            - "Minimum length = 1"
            - "Maximum length = 252"

    push:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Process traffic with the push virtual server that is bound to this content switching virtual server
                (specified by the Push VServer parameter). The service type of the push virtual server should be
                either HTTP or SSL.
            - "Default value: DISABLED"

    pushvserver:
        description:
            - >-
                Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes
                updates received on the client-facing load balancing virtual server.
            - "Minimum length = 1"

    pushlabel:
        description:
            - >-
                Expression for extracting the label from the response received from server. This string can be either
                an existing rule name or an inline expression. The service type of the virtual server should be
                either HTTP or SSL.
            - "Default value: \\"none\\""

    pushmulticlients:
        description:
            - >-
                Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
                updates.
            - "Default value: NO"

    tcpprofilename:
        description:
            - "Name of the TCP profile containing TCP configuration settings for the virtual server."
            - "Minimum length = 1"
            - "Maximum length = 127"

    httpprofilename:
        description:
            - >-
                Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service
                type of the virtual server should be either HTTP or SSL.
            - "Minimum length = 1"
            - "Maximum length = 127"

    dbprofilename:
        description:
            - "Name of the DB profile."
            - "Minimum length = 1"
            - "Maximum length = 127"

    oracleserverversion:
        choices:
            - '10G'
            - '11G'
        description:
            - "Oracle server version."
            - "Default value: 10G"

    comment:
        description:
            - "Information about this virtual server."

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
            - "Default value: 2008R2"

    l2conn:
        description:
            - "Use L2 Parameters to identify a connection."

    mysqlprotocolversion:
        description:
            - "The protocol version returned by the mysql vserver."
            - "Default value: 10"

    mysqlserverversion:
        description:
            - "The server version string returned by the mysql vserver."
            - "Minimum length = 1"
            - "Maximum length = 31"

    mysqlcharacterset:
        description:
            - "The character set returned by the mysql vserver."
            - "Default value: 8"

    mysqlservercapabilities:
        description:
            - "The server capabilities returned by the mysql vserver."
            - "Default value: 41613"

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable logging appflow flow information."
            - "Default value: ENABLED"

    netprofile:
        description:
            - "The name of the network profile."
            - "Minimum length = 1"
            - "Maximum length = 127"

    icmpvsrresponse:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - "Can be active or passive."
            - "Default value: PASSIVE"

    rhistate:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - "A host route is injected according to the setting on the virtual servers"
            - >-
                * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always
                injects the hostroute.
            - >-
                * If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even
                if one virtual server is UP.
            - >-
                * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if
                one virtual server set to ACTIVE is UP.
            - "Default value: PASSIVE"

    authnprofile:
        description:
            - "Name of the authentication profile to be used when authentication is turned on."

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the
                transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.
            - "Minimum length = 1"
            - "Maximum length = 127"

    domainname:
        description:
            - "Domain name for which to change the time to live (TTL) and/or backup service IP address."
            - "Minimum length = 1"

    ttl:
        description:
            - "."
            - "Minimum value = 1"

    backupip:
        description:
            - "."
            - "Minimum length = 1"

    cookiedomain:
        description:
            - "."
            - "Minimum length = 1"

    cookietimeout:
        description:
            - "."
            - "Minimum value = 0"
            - "Maximum value = 1440"

    sitedomainttl:
        description:
            - "."
            - "Minimum value = 1"

    newname:
        description:
            - >-
                New name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character,
                and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign
                (@), equal sign (=), and hyphen (-) characters.
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, my name or my name).
            - "Minimum length = 1"


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled, get_immutables_intersection
try:
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False


def _exists(client, module):
    if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
        return True
    else:
        return False


def _identical(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    diff_dict = _proxy.diff_object(_list[0])
    if len(diff_dict) == 0:
        return True
    else:
        return False


def diff_list(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    return _proxy.diff_object(_list[0])


def main():

    module_specific_arguments = dict(
        name=dict(type='str'),
        td=dict(type='float'),
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
        persistenceid=dict(type='float'),
        ippattern=dict(type='str'),
        ipmask=dict(type='str'),
        range=dict(type='float'),
        port=dict(type='int'),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        stateupdate=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        cacheable=dict(type='bool'),
        redirecturl=dict(type='str'),
        clttimeout=dict(type='float'),
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
                'ENABLED',
                'DISABLED',
            ]
        ),
        sopersistencetimeout=dict(type='float'),
        sothreshold=dict(type='float'),
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
                'ENABLED',
                'DISABLED',
            ]
        ),
        downstateflush=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        backupvserver=dict(type='str'),
        disableprimaryondown=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
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
        listenpriority=dict(type='float'),
        authn401=dict(type='bool'),
        authnvsname=dict(type='str'),
        push=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
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
        mysqlprotocolversion=dict(type='float'),
        mysqlserverversion=dict(type='str'),
        mysqlcharacterset=dict(type='float'),
        mysqlservercapabilities=dict(type='float'),
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
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
        domainname=dict(type='str'),
        ttl=dict(type='float'),
        backupip=dict(type='str'),
        cookiedomain=dict(type='str'),
        cookietimeout=dict(type='float'),
        sitedomainttl=dict(type='float'),
        newname=dict(type='str'),
    )

    hand_inserted_arguments = dict(
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not PYTHON_SDK_IMPORTED:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)

    try:
        client.login()
    except nitro_exception as e:
        msg = "nitro exception during login. errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg)
    except Exception as e:
        if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
            module.fail_json(msg='Connection error %s' % str(e))
        elif str(type(e)) == "<class 'requests.exceptions.SSLError'>":
            module.fail_json(msg='SSL Error %s' % str(e))
        else:
            module.fail_json(msg='Unexpected error during login %s' % str(e))

    readwrite_attrs = [
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
        'state',
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
        'domainname',
        'ttl',
        'backupip',
        'cookiedomain',
        'cookietimeout',
        'sitedomainttl',
        'newname',
    ]

    readonly_attrs = [
        'ip',
        'value',
        'ngname',
        'type',
        'curstate',
        'sc',
        'status',
        'cachetype',
        'redirect',
        'homepage',
        'dnsvservername',
        'domain',
        'policyname',
        'servicename',
        'weight',
        'cachevserver',
        'targetvserver',
        'priority',
        'url',
        'gotopriorityexpression',
        'bindpoint',
        'invoke',
        'labeltype',
        'labelname',
        'gt2gb',
        'statechangetimesec',
        'statechangetimemsec',
        'tickssincelaststatechange',
        'ruletype',
        'lbvserver',
        'targetlbvserver',
        '__count',
    ]

    immutable_attrs = [
        'name',
        'td',
        'servicetype',
        'ipv46',
        'targettype',
        'range',
        'port',
        'state',
        'vipheader',
        'newname',
    ]

    transforms = {
        'cacheable': ['bool_yes_no'],
        'rtspnat': ['bool_on_off'],
        'authn401': ['bool_on_off'],
        'casesensitive': ['bool_on_off'],
        'authentication': ['bool_on_off'],
        'l2conn': ['bool_on_off'],
        'pushmulticlients': ['bool_yes_no'],
    }

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
        transforms=transforms,
    )

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate state
        if module.params['state'] == 'present':
            if not _exists(client, module):
                if not module.check_mode:
                    _proxy.add()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            elif not _identical(client, module, _proxy):

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(_proxy, diff_list(client, module, _proxy).keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(client, module, _proxy), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if not _exists(client, module):
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical(client, module, _proxy):
                    module.fail_json(msg='_ differs from configured', diff=diff(client, module, _proxy), **module_result)

        elif module.params['state'] == 'absent':
            if _exists(client, module):
                if not module.check_mode:
                    _proxy.delete()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if _exists(client, module):
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
