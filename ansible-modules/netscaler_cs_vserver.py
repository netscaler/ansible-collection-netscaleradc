#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_cs_vserver
short_description: Manage cs vserver
description:
    - Manage service group configuration in Netscaler

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True

    name:
        
        description:
            
            - Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters.
            
            - Cannot be changed after the CS virtual server is created.
            
            - The following requirement applies only to the NetScaler CLI:
            
            - If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my server or my server).
            
            - Minimum length = 1
            

    td:
        
        description:
            
            - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.
            
            - Minimum value = 0
            
            - Maximum value = 4094
            

    servicetype:
        choices: ['HTTP', 'SSL', 'TCP', 'FTP', 'RTSP', 'SSL_TCP', 'UDP', 'DNS', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'ANY', 'RADIUS', 'RDP', 'MYSQL', 'MSSQL', 'DIAMETER', 'SSL_DIAMETER', 'DNS_TCP', 'ORACLE', 'SMPP']
        description:
            
            - Protocol used by the virtual server.
            
            - Possible values = HTTP, SSL, TCP, FTP, RTSP, SSL_TCP, UDP, DNS, SIP_UDP, SIP_TCP, SIP_SSL, ANY, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, DNS_TCP, ORACLE, SMPP
            

    ipv46:
        
        description:
            
            - IP address of the content switching virtual server.
            
            - Minimum length = 1
            

    targettype:
        choices: ['GSLB']
        description:
            
            - Virtual server target type.
            
            - Possible values = GSLB
            

    dnsrecordtype:
        choices: ['A', 'AAAA', 'CNAME', 'NAPTR']
        description:
            
            - .
            
            - Default value: NSGSLB_IPV4
            
            - Possible values = A, AAAA, CNAME, NAPTR
            

    persistenceid:
        
        description:
            
            - .
            
            - Minimum value = 0
            
            - Maximum value = 65535
            

    ippattern:
        
        description:
            
            - IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter.
            
            - For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
            
            - If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if the virtual servers, vs1 and vs2, have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
            

    ipmask:
        
        description:
            
            - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
            

    range:
        
        description:
            
            - Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, to include in a range of addresses assigned to this virtual server.
            
            - Default value: 1
            
            - Minimum value = 1
            
            - Maximum value = 254
            

    port:
        
        description:
            
            - Port number for content switching virtual server.
            
            - Minimum value = 1
            
            - Range 1 - 65535
            
            - * in CLI is represented as 65535 in NITRO API
            

    state:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Initial state of the load balancing virtual server.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    stateupdate:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Enable state updates for a specific content switching virtual server. By default, the Content Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to it. This parameter interacts with the global setting as follows:
            
            - Global Level | Vserver Level | Result
            
            - ENABLED ENABLED ENABLED
            
            - ENABLED DISABLED ENABLED
            
            - DISABLED ENABLED ENABLED
            
            - DISABLED DISABLED DISABLED
            
            - If you want to enable state updates for only some content switching virtual servers, be sure to disable the state update parameter.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    cacheable:
        choices: ['YES', 'NO']
        description:
            
            - Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    redirecturl:
        
        description:
            
            - URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the virtual server should be either HTTP or SSL.
            
            - Caution: Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.
            
            - Minimum length = 1
            

    clttimeout:
        
        description:
            
            - Idle time, in seconds, after which the client connection is terminated. The default values are:
            
            - 180 seconds for HTTP/SSL-based services.
            
            - 9000 seconds for other TCP-based services.
            
            - 120 seconds for DNS-based services.
            
            - 120 seconds for other UDP-based services.
            
            - Minimum value = 0
            
            - Maximum value = 31536000
            

    precedence:
        choices: ['RULE', 'URL']
        description:
            
            - Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual server. With the default (RULE) setting, incoming requests are evaluated against the rule-based content switching policies. If none of the rules match, the URL in the request is evaluated against the URL-based content switching policies.
            
            - Default value: RULE
            
            - Possible values = RULE, URL
            

    casesensitive:
        choices: ['ON', 'OFF']
        description:
            
            - Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by content switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the same target.
            
            - Default value: ON
            
            - Possible values = ON, OFF
            

    somethod:
        choices: ['CONNECTION', 'DYNAMICCONNECTION', 'BANDWIDTH', 'HEALTH', 'NONE']
        description:
            
            - Type of spillover used to divert traffic to the backup virtual server when the primary virtual server reaches the spillover threshold. Connection spillover is based on the number of connections. Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.
            
            - Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE
            

    sopersistence:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Maintain source-IP based persistence on primary and backup virtual servers.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    sopersistencetimeout:
        
        description:
            
            - Time-out value, in minutes, for spillover persistence.
            
            - Default value: 2
            
            - Minimum value = 2
            
            - Maximum value = 1440
            

    sothreshold:
        
        description:
            
            - Depending on the spillover method, the maximum number of connections or the maximum total bandwidth (Kbps) that a virtual server can handle before spillover occurs.
            
            - Minimum value = 1
            
            - Maximum value = 4294967287
            

    sobackupaction:
        choices: ['DROP', 'ACCEPT', 'REDIRECT']
        description:
            
            - Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.
            
            - Possible values = DROP, ACCEPT, REDIRECT
            

    redirectportrewrite:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - State of port rewrite while performing HTTP redirect.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    backupvserver:
        
        description:
            
            - Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup virtual server is created. You can assign a different backup virtual server or rename the existing virtual server.
            
            - The following requirement applies only to the NetScaler CLI:
            
            - If the name includes one or more spaces, enclose the name in double or single quotation marks.
            
            - Minimum length = 1
            

    disableprimaryondown:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Continue forwarding the traffic to backup virtual server even after the primary server comes UP from the DOWN state.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    insertvserveripport:
        choices: ['OFF', 'VIPADDR', 'V6TOV4MAPPING']
        description:
            
            - Insert the virtual server's VIP address and port number in the request header. Available values function as follows:
            
            - VIPADDR - Header contains the vserver's IP address and port number without any translation.
            
            - OFF - The virtual IP and port header insertion option is disabled.
            
            - V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.
            
            - Possible values = OFF, VIPADDR, V6TOV4MAPPING
            

    vipheader:
        
        description:
            
            - Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.
            
            - Minimum length = 1
            

    rtspnat:
        choices: ['ON', 'OFF']
        description:
            
            - Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    authenticationhost:
        
        description:
            
            - FQDN of the authentication virtual server. The service type of the virtual server should be either HTTP or SSL.
            
            - Minimum length = 3
            
            - Maximum length = 252
            

    authentication:
        choices: ['ON', 'OFF']
        description:
            
            - Authenticate users who request a connection to the content switching virtual server.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    listenpolicy:
        
        description:
            
            - String specifying the listen policy for the content switching virtual server. Can be either the name of an existing expression or an in-line expression.
            
            - Default value: "NONE"
            

    listenpriority:
        
        description:
            
            - Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.
            
            - Default value: 101
            
            - Minimum value = 0
            
            - Maximum value = 100
            

    authn401:
        choices: ['ON', 'OFF']
        description:
            
            - Enable HTTP 401-response based authentication.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    authnvsname:
        
        description:
            
            - Name of authentication virtual server that authenticates the incoming user requests to this content switching virtual server. .
            
            - Minimum length = 1
            
            - Maximum length = 252
            

    push:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Process traffic with the push virtual server that is bound to this content switching virtual server (specified by the Push VServer parameter). The service type of the push virtual server should be either HTTP or SSL.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    pushvserver:
        
        description:
            
            - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the client-facing load balancing virtual server.
            
            - Minimum length = 1
            

    pushlabel:
        
        description:
            
            - Expression for extracting the label from the response received from server. This string can be either an existing rule name or an inline expression. The service type of the virtual server should be either HTTP or SSL.
            
            - Default value: "none"
            

    pushmulticlients:
        choices: ['YES', 'NO']
        description:
            
            - Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    tcpprofilename:
        
        description:
            
            - Name of the TCP profile containing TCP configuration settings for the virtual server.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    httpprofilename:
        
        description:
            
            - Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service type of the virtual server should be either HTTP or SSL.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    dbprofilename:
        
        description:
            
            - Name of the DB profile.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    oracleserverversion:
        choices: ['10G', '11G']
        description:
            
            - Oracle server version.
            
            - Default value: 10G
            
            - Possible values = 10G, 11G
            

    comment:
        
        description:
            
            - Information about this virtual server.
            

    mssqlserverversion:
        choices: ['70', '2000', '2000SP1', '2005', '2008', '2008R2', '2012', '2014']
        description:
            
            - The version of the MSSQL server.
            
            - Default value: 2008R2
            
            - Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014
            

    l2conn:
        choices: ['ON', 'OFF']
        description:
            
            - Use L2 Parameters to identify a connection.
            
            - Possible values = ON, OFF
            

    mysqlprotocolversion:
        
        description:
            
            - The protocol version returned by the mysql vserver.
            
            - Default value: 10
            

    mysqlserverversion:
        
        description:
            
            - The server version string returned by the mysql vserver.
            
            - Minimum length = 1
            
            - Maximum length = 31
            

    mysqlcharacterset:
        
        description:
            
            - The character set returned by the mysql vserver.
            
            - Default value: 8
            

    mysqlservercapabilities:
        
        description:
            
            - The server capabilities returned by the mysql vserver.
            
            - Default value: 41613
            

    appflowlog:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Enable logging appflow flow information.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    netprofile:
        
        description:
            
            - The name of the network profile.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    icmpvsrresponse:
        choices: ['PASSIVE', 'ACTIVE']
        description:
            
            - Can be active or passive.
            
            - Default value: PASSIVE
            
            - Possible values = PASSIVE, ACTIVE
            

    rhistate:
        choices: ['PASSIVE', 'ACTIVE']
        description:
            
            - A host route is injected according to the setting on the virtual servers
            
            - * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always injects the hostroute.
            
            - * If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.
            
            - * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if one virtual server set to ACTIVE is UP.
            
            - Default value: PASSIVE
            
            - Possible values = PASSIVE, ACTIVE
            

    authnprofile:
        
        description:
            
            - Name of the authentication profile to be used when authentication is turned on.
            

    dnsprofilename:
        
        description:
            
            - Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    domainname:
        
        description:
            
            - Domain name for which to change the time to live (TTL) and/or backup service IP address.
            
            - Minimum length = 1
            

    ttl:
        
        description:
            
            - .
            
            - Minimum value = 1
            

    backupip:
        
        description:
            
            - .
            
            - Minimum length = 1
            

    cookiedomain:
        
        description:
            
            - .
            
            - Minimum length = 1
            

    cookietimeout:
        
        description:
            
            - .
            
            - Minimum value = 0
            
            - Maximum value = 1440
            

    sitedomainttl:
        
        description:
            
            - .
            
            - Minimum value = 1
            

'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Connect to netscaler appliance
    netscaler_service_group:
        nsip: "172.17.0.2"
'''

# TODO: Update as module progresses
RETURN = '''
config_updated:
    description: determine if a change in the netscaler configuration happened
    returned: always
    type: boolean
    sample: False
'''

from ansible.module_utils.basic import AnsibleModule
import StringIO


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_cspolicy_binding import csvserver_cspolicy_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
        name=dict(type='str'),
        td=dict(type='float'),
        servicetype=dict(
            type='str',
            choices=[u'HTTP', u'SSL', u'TCP', u'FTP', u'RTSP', u'SSL_TCP', u'UDP', u'DNS', u'SIP_UDP', u'SIP_TCP', u'SIP_SSL', u'ANY', u'RADIUS', u'RDP', u'MYSQL', u'MSSQL', u'DIAMETER', u'SSL_DIAMETER', u'DNS_TCP', u'ORACLE', u'SMPP']
        ),
        
        ipv46=dict(type='str'),
        targettype=dict(
            type='str',
            choices=[u'GSLB']
        ),
        dnsrecordtype=dict(
            type='str',
            choices=[u'A', u'AAAA', u'CNAME', u'NAPTR']
        ),
        persistenceid=dict(type='float'),
        ippattern=dict(type='str'),
        ipmask=dict(type='str'),
        range=dict(type='float'),
        port=dict(type='int'),
        state=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        stateupdate=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        cacheable=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        redirecturl=dict(type='str'),
        clttimeout=dict(type='float'),
        precedence=dict(
            type='str',
            choices=[u'RULE', u'URL']
        ),
        casesensitive=dict(
            type='str',
            choices=[u'ON', u'OFF']
        ),
        somethod=dict(
            type='str',
            choices=[u'CONNECTION', u'DYNAMICCONNECTION', u'BANDWIDTH', u'HEALTH', u'NONE']
        ),
        sopersistence=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        sopersistencetimeout=dict(type='float'),
        sothreshold=dict(type='float'),
        sobackupaction=dict(
            type='str',
            choices=[u'DROP', u'ACCEPT', u'REDIRECT']
        ),
        redirectportrewrite=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        downstateflush=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        backupvserver=dict(type='str'),
        disableprimaryondown=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        insertvserveripport=dict(
            type='str',
            choices=[u'OFF', u'VIPADDR', u'V6TOV4MAPPING']
        ),
        vipheader=dict(type='str'),
        rtspnat=dict(
            type='str',
            choices=[u'ON', u'OFF']
        ),
        authenticationhost=dict(type='str'),
        authentication=dict(
            type='str',
            choices=[u'ON', u'OFF']
        ),
        listenpolicy=dict(type='str'),
        listenpriority=dict(type='float'),
        authn401=dict(
            type='str',
            choices=[u'ON', u'OFF']
        ),
        authnvsname=dict(type='str'),
        push=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        pushvserver=dict(type='str'),
        pushlabel=dict(type='str'),
        pushmulticlients=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        dbprofilename=dict(type='str'),
        oracleserverversion=dict(
            type='str',
            choices=[u'10G', u'11G']
        ),
        comment=dict(type='str'),
        mssqlserverversion=dict(
            type='str',
            choices=[u'70', u'2000', u'2000SP1', u'2005', u'2008', u'2008R2', u'2012', u'2014']
        ),
        l2conn=dict(
            type='str',
            choices=[u'ON', u'OFF']
        ),
        mysqlprotocolversion=dict(type='float'),
        mysqlserverversion=dict(type='str'),
        mysqlcharacterset=dict(type='float'),
        mysqlservercapabilities=dict(type='float'),
        appflowlog=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        netprofile=dict(type='str'),
        icmpvsrresponse=dict(
            type='str',
            choices=[u'PASSIVE', u'ACTIVE']
        ),
        rhistate=dict(
            type='str',
            choices=[u'PASSIVE', u'ACTIVE']
        ),
        authnprofile=dict(type='str'),
        dnsprofilename=dict(type='str'),
        domainname=dict(type='str'),
        ttl=dict(type='float'),
        backupip=dict(type='str'),
        cookiedomain=dict(type='str'),
        cookietimeout=dict(type='float'),
        sitedomainttl=dict(type='float'),
    )

    hand_inserted_arguments = dict(
        policybindings=dict(type='list'),
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode = True,
    )
    module_result = dict(
        changed=False,
        failed=False,
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()



    # Instantiate Service Config object

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
    ]
    csvserver_proxy = ConfigProxy(
        actual=csvserver(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def cs_vserver_exists():
        if csvserver.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def cs_vserver_identical():
        service_list = csvserver.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = csvserver_proxy.diff_object(service_list[0])
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def get_configured_policybindings():
        bindings = {}
        for binding in module.params['policybindings']:
            binding['name'] = module.params['name']
            key = binding['policyname']
            binding_proxy = ConfigProxy(
                actual = csvserver_cspolicy_binding(),
                client=client,
                readwrite_attrs = [
                    'priority',
                    'bindpoint',
                    'policyname',
                    'labelname',
                    'name',
                    'gotopriorityexpression',
                    'targetlbvserver',
                    'invoke',
                    'labeltype',
                ],
                readonly_attrs=[],
                attribute_values_dict=binding
            )
            bindings[key] = binding_proxy
        return bindings





    def get_actual_policybindings():
        bindings = {}
        if csvserver_cspolicy_binding.count(client, name=module.params['name']) == 0:
            return bindings

        for binding in csvserver_cspolicy_binding.get(client,name=module.params['name']):
            key = binding.policyname
            bindings[key] = binding

        return bindings

    def cs_policybindings_identical():
        actual_bindings = get_actual_policybindings()
        configured_bindings = get_configured_policybindings()

        actual_keyset = set(actual_bindings.keys())
        configured_keyset = set(configured_bindings.keys())
        if len(actual_keyset ^ configured_keyset) > 0:
            return False

        # Compare item to item
        for key in actual_bindings.keys():
            configured_binding_proxy = configured_bindings[key]
            actual_binding_object = actual_bindings[key]
            if not configured_binding_proxy.has_equal_attributes(actual_binding_object):
                return False

        # Fallthrough to success
        return True

    def sync_cs_policybindings():

        # Delete all actual bindings
        for binding in get_actual_policybindings().values():
            csvserver_cspolicy_binding.delete(client,binding)

        # Add all configured bindings

        for binding in get_configured_policybindings().values():
            binding.add()

    def diff_list():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        return csvserver_proxy.diff_object(service_list[0])


    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not cs_vserver_exists():
                if not module.check_mode:
                    csvserver_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not cs_vserver_identical():
                if not module.check_mode:
                    csvserver_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Check policybindings
            if not cs_policybindings_identical():
                if not module.check_mode:
                    sync_cs_policybindings()
                    client.save_config()
                module_result['changed'] = True

            # Sanity check for operation
            if not cs_vserver_exists():
                module.fail_json(msg='Service does not exist')
            if not cs_vserver_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())
            if not cs_policybindings_identical():
                module.fail_json(msg='Policy bindings differ')

        elif module.params['operation'] == 'absent':
            if cs_vserver_exists():
                if not module.check_mode:
                    csvserver_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if cs_vserver_exists():
                module.fail_json(msg='Service still exists')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()
