#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_service_group
short_description: Manage service group configuration in Netscaler
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
            
            - Name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the service has been created.
            
            - Minimum length = 1
            

    ip:
        
        description:
            
            - IP to assign to the service.
            
            - Minimum length = 1
            

    servername:
        
        description:
            
            - Name of the server that hosts the service.
            
            - Minimum length = 1
            

    servicetype:
        choices: ['HTTP', 'FTP', 'TCP', 'UDP', 'SSL', 'SSL_BRIDGE', 'SSL_TCP', 'DTLS', 'NNTP', 'RPCSVR', 'DNS', 'ADNS', 'SNMP', 'RTSP', 'DHCPRA', 'ANY', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'DNS_TCP', 'ADNS_TCP', 'MYSQL', 'MSSQL', 'ORACLE', 'RADIUS', 'RADIUSListener', 'RDP', 'DIAMETER', 'SSL_DIAMETER', 'TFTP', 'SMPP', 'PPTP', 'GRE', 'SYSLOGTCP', 'SYSLOGUDP', 'FIX', 'SSL_FIX']
        description:
            
            - Protocol in which data is exchanged with the service.
            
            - Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX
            

    port:
        
        description:
            
            - Port number of the service.
            
            - Range 1 - 65535
            
            - * in CLI is represented as 65535 in NITRO API
            

    cleartextport:
        
        description:
            
            - Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.
            
            - Minimum value = 1
            

    cachetype:
        choices: ['TRANSPARENT', 'REVERSE', 'FORWARD']
        description:
            
            - Cache type supported by the cache server.
            
            - Possible values = TRANSPARENT, REVERSE, FORWARD
            

    maxclient:
        
        description:
            
            - Maximum number of simultaneous open connections to the service.
            
            - Minimum value = 0
            
            - Maximum value = 4294967294
            

    healthmonitor:
        choices: ['YES', 'NO']
        description:
            
            - Monitor the health of this service. Available settings function as follows:
            
            - YES - Send probes to check the health of the service.
            
            - NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.
            
            - Default value: YES
            
            - Possible values = YES, NO
            

    maxreq:
        
        description:
            
            - Maximum number of requests that can be sent on a persistent connection to the service.
            
            - Note: Connection requests beyond this value are rejected.
            
            - Minimum value = 0
            
            - Maximum value = 65535
            

    cacheable:
        choices: ['YES', 'NO']
        description:
            
            - Use the transparent cache redirection virtual server to forward requests to the cache server.
            
            - Note: Do not specify this parameter if you set the Cache Type parameter.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    cip:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.
            
            - Possible values = ENABLED, DISABLED
            

    cipheader:
        
        description:
            
            - Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".
            
            - Minimum length = 1
            

    usip:
        choices: ['YES', 'NO']
        description:
            
            - Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.
            
            - Possible values = YES, NO
            

    pathmonitor:
        choices: ['YES', 'NO']
        description:
            
            - Path monitoring for clustering.
            
            - Possible values = YES, NO
            

    pathmonitorindv:
        choices: ['YES', 'NO']
        description:
            
            - Individual Path monitoring decisions.
            
            - Possible values = YES, NO
            

    useproxyport:
        choices: ['YES', 'NO']
        description:
            
            - Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.
            
            - Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.
            
            - Possible values = YES, NO
            

    sc:
        choices: ['ON', 'OFF']
        description:
            
            - State of SureConnect for the service.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    sp:
        choices: ['ON', 'OFF']
        description:
            
            - Enable surge protection for the service.
            
            - Possible values = ON, OFF
            

    rtspsessionidremap:
        choices: ['ON', 'OFF']
        description:
            
            - Enable RTSP session ID mapping for the service.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    clttimeout:
        
        description:
            
            - Time, in seconds, after which to terminate an idle client connection.
            
            - Minimum value = 0
            
            - Maximum value = 31536000
            

    svrtimeout:
        
        description:
            
            - Time, in seconds, after which to terminate an idle server connection.
            
            - Minimum value = 0
            
            - Maximum value = 31536000
            

    customserverid:
        
        description:
            
            - Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.
            
            - Default value: "None"
            

    serverid:
        
        description:
            
            - The identifier for the service. This is used when the persistency type is set to Custom Server ID.
            

    cka:
        choices: ['YES', 'NO']
        description:
            
            - Enable client keep-alive for the service.
            
            - Possible values = YES, NO
            

    tcpb:
        choices: ['YES', 'NO']
        description:
            
            - Enable TCP buffering for the service.
            
            - Possible values = YES, NO
            

    cmp:
        choices: ['YES', 'NO']
        description:
            
            - Enable compression for the service.
            
            - Possible values = YES, NO
            

    maxbandwidth:
        
        description:
            
            - Maximum bandwidth, in Kbps, allocated to the service.
            
            - Minimum value = 0
            
            - Maximum value = 4294967287
            

    accessdown:
        choices: ['YES', 'NO']
        description:
            
            - Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    monthreshold:
        
        description:
            
            - Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.
            
            - Minimum value = 0
            
            - Maximum value = 65535
            

    state:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Initial state of the service.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    tcpprofilename:
        
        description:
            
            - Name of the TCP profile that contains TCP configuration settings for the service.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    httpprofilename:
        
        description:
            
            - Name of the HTTP profile that contains HTTP configuration settings for the service.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    hashid:
        
        description:
            
            - A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.
            
            - Minimum value = 1
            

    comment:
        
        description:
            
            - Any information about the service.
            

    appflowlog:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Enable logging of AppFlow information.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    netprofile:
        
        description:
            
            - Network profile to use for the service.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    td:
        
        description:
            
            - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.
            
            - Minimum value = 0
            
            - Maximum value = 4094
            

    processlocal:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.
            
            - Default value: DISABLED
            
            - Possible values = ENABLED, DISABLED
            

    dnsprofilename:
        
        description:
            
            - Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.
            
            - Minimum length = 1
            
            - Maximum length = 127
            

    ipaddress:
        
        description:
            
            - The new IP address of the service.
            

    weight:
        
        description:
            
            - Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.
            
            - Minimum value = 1
            
            - Maximum value = 100
            

    monitor_name_svc:
        
        description:
            
            - Name of the monitor bound to the specified service.
            
            - Minimum length = 1
            

    riseapbrstatsmsgcode:
        
        description:
            
            - The code indicating the rise apbr status.
            

    delay:
        
        description:
            
            - Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
            

    graceful:
        choices: ['YES', 'NO']
        description:
            
            - Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    all:
        
        description:
            
            - Display both user-configured and dynamically learned services.
            

    Internal:
        
        description:
            
            - Display only dynamically learned services.
            

    newname:
        
        description:
            
            - New name for the service. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
            
            - Minimum length = 1
            

    numofconnections:
        
        description:
            
            - This will tell the number of client side connections are still open.
            

    policyname:
        
        description:
            
            - The name of the policyname for which this service is bound.
            

    serviceconftype:
        
        description:
            
            - The configuration type of the service.
            

    serviceconftype2:
        choices: ['Configured', 'Dynamic', 'Internal']
        description:
            
            - The configuration type of the service (Internal/Dynamic/Configured).
            
            - Possible values = Configured, Dynamic, Internal
            

    value:
        choices: ['Certkey not bound', 'SSL feature disabled']
        description:
            
            - SSL status.
            
            - Possible values = Certkey not bound, SSL feature disabled
            

    gslb:
        choices: ['REMOTE', 'LOCAL']
        description:
            
            - The GSLB option for the corresponding virtual server.
            
            - Possible values = REMOTE, LOCAL
            

    dup_state:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Added this field for getting state value from table.
            
            - Possible values = ENABLED, DISABLED
            

    publicip:
        
        description:
            
            - public ip.
            

    publicport:
        
        description:
            
            - public port.
            
            - Minimum value = 1
            
            - Range 1 - 65535
            
            - * in CLI is represented as 65535 in NITRO API
            

    svrstate:
        choices: ['UP', 'DOWN', 'UNKNOWN', 'BUSY', 'OUT OF SERVICE', 'GOING OUT OF SERVICE', 'DOWN WHEN GOING OUT OF SERVICE', 'NS_EMPTY_STR', 'Unknown', 'DISABLED']
        description:
            
            - The state of the service.
            
            - Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED
            

    monitor_state:
        choices: ['UP', 'DOWN', 'UNKNOWN', 'BUSY', 'OUT OF SERVICE', 'GOING OUT OF SERVICE', 'DOWN WHEN GOING OUT OF SERVICE', 'NS_EMPTY_STR', 'Unknown', 'DISABLED']
        description:
            
            - The running state of the monitor on this service.
            
            - Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED
            

    monstatcode:
        
        description:
            
            - The code indicating the monitor response.
            

    lastresponse:
        
        description:
            
            - The string form of monstatcode.
            

    responsetime:
        
        description:
            
            - Response time of this monitor.
            

    riseapbrstatsmsgcode2:
        
        description:
            
            - The code indicating other rise stats.
            

    monstatparam1:
        
        description:
            
            - First parameter for use with message code.
            

    monstatparam2:
        
        description:
            
            - Second parameter for use with message code.
            

    monstatparam3:
        
        description:
            
            - Third parameter for use with message code.
            

    statechangetimesec:
        
        description:
            
            - Time when last state change happened. Seconds part.
            

    statechangetimemsec:
        
        description:
            
            - Time at which last state change happened. Milliseconds part.
            

    tickssincelaststatechange:
        
        description:
            
            - Time in 10 millisecond ticks since the last state change.
            

    stateupdatereason:
        
        description:
            
            - Checks state update reason on the secondary node.
            

    clmonowner:
        
        description:
            
            - Tells the mon owner of the service.
            
            - Minimum value = 0
            
            - Maximum value = 32
            

    clmonview:
        
        description:
            
            - Tells the view id of the monitoring owner.
            

    serviceipstr:
        
        description:
            
            - This field has been intorduced to show the dbs services ip.
            

    oracleserverversion:
        choices: ['10G', '11G']
        description:
            
            - Oracle server version.
            
            - Default value: 10G
            
            - Possible values = 10G, 11G
            

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
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        from nssrc.com.citrix.netscaler.nitro.resource.stat.basic.service_stats import service_stats
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
            name=dict(
        type='str',
        
        ),
        
            ip=dict(
        type='str',
        
        ),
        
            servername=dict(
        type='str',
        
        ),
        
            servicetype=dict(
        type='str',
        choices=[u'HTTP', u'FTP', u'TCP', u'UDP', u'SSL', u'SSL_BRIDGE', u'SSL_TCP', u'DTLS', u'NNTP', u'RPCSVR', u'DNS', u'ADNS', u'SNMP', u'RTSP', u'DHCPRA', u'ANY', u'SIP_UDP', u'SIP_TCP', u'SIP_SSL', u'DNS_TCP', u'ADNS_TCP', u'MYSQL', u'MSSQL', u'ORACLE', u'RADIUS', u'RADIUSListener', u'RDP', u'DIAMETER', u'SSL_DIAMETER', u'TFTP', u'SMPP', u'PPTP', u'GRE', u'SYSLOGTCP', u'SYSLOGUDP', u'FIX', u'SSL_FIX']
        ),
        
            port=dict(
        type='int',
        
        ),
        
            cleartextport=dict(
        type='int',
        
        ),
        
            cachetype=dict(
        type='str',
        choices=[u'TRANSPARENT', u'REVERSE', u'FORWARD']
        ),
        
            maxclient=dict(
        type='float',
        
        ),
        
            healthmonitor=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            maxreq=dict(
        type='float',
        
        ),
        
            cacheable=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            cip=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            cipheader=dict(
        type='str',
        
        ),
        
            usip=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            pathmonitor=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            pathmonitorindv=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            useproxyport=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            sc=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            sp=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            rtspsessionidremap=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            clttimeout=dict(
        type='float',
        
        ),
        
            svrtimeout=dict(
        type='float',
        
        ),
        
            customserverid=dict(
        type='str',
        
        ),
        
            serverid=dict(
        type='float',
        
        ),
        
            cka=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            tcpb=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            cmp=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            maxbandwidth=dict(
        type='float',
        
        ),
        
            accessdown=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            monthreshold=dict(
        type='float',
        
        ),
        
            state=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            downstateflush=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            tcpprofilename=dict(
        type='str',
        
        ),
        
            httpprofilename=dict(
        type='str',
        
        ),
        
            hashid=dict(
        type='float',
        
        ),
        
            comment=dict(
        type='str',
        
        ),
        
            appflowlog=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            netprofile=dict(
        type='str',
        
        ),
        
            td=dict(
        type='float',
        
        ),
        
            processlocal=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            dnsprofilename=dict(
        type='str',
        
        ),
        
            ipaddress=dict(
        type='str',
        
        ),
        
            weight=dict(
        type='float',
        
        ),
        
            monitor_name_svc=dict(
        type='str',
        
        ),
        
            riseapbrstatsmsgcode=dict(
        type='int',
        
        ),
        
            delay=dict(
        type='float',
        
        ),
        
            graceful=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            all=dict(
        type='bool',
        
        ),
        
            Internal=dict(
        type='bool',
        
        ),
        
            newname=dict(
        type='str',
        
        ),
        
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

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
    readwrite_attrs = [u'name', u'ip', u'servername', u'servicetype', u'port', u'cleartextport', u'cachetype', u'maxclient', u'healthmonitor', u'maxreq', u'cacheable', u'cip', u'cipheader', u'usip', u'pathmonitor', u'pathmonitorindv', u'useproxyport', u'sc', u'sp', u'rtspsessionidremap', u'clttimeout', u'svrtimeout', u'customserverid', u'serverid', u'cka', u'tcpb', u'cmp', u'maxbandwidth', u'accessdown', u'monthreshold', u'state', u'downstateflush', u'tcpprofilename', u'httpprofilename', u'hashid', u'comment', u'appflowlog', u'netprofile', u'td', u'processlocal', u'dnsprofilename', u'ipaddress', u'weight', u'monitor_name_svc', u'riseapbrstatsmsgcode', u'delay', u'graceful', u'all', u'Internal', u'newname']
    readonly_attrs = [u'numofconnections', u'policyname', u'serviceconftype', u'serviceconftype2', u'value', u'gslb', u'dup_state', u'publicip', u'publicport', u'svrstate', u'monitor_state', u'monstatcode', u'lastresponse', u'responsetime', u'riseapbrstatsmsgcode2', u'monstatparam1', u'monstatparam2', u'monstatparam3', u'statechangetimesec', u'statechangetimemsec', u'tickssincelaststatechange', u'stateupdatereason', u'clmonowner', u'clmonview', u'serviceipstr', u'oracleserverversion', u'__count']

    service_proxy = ConfigProxy(
        actual=service(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def service_exists():
        if service.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def service_identical():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = service_proxy.diff_object(service_list[0])
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff_list():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        return service_proxy.diff_object(service_list[0])


    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not service_exists():
                if not module.check_mode:
                    service_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not service_identical():
                if not module.check_mode:
                    service_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not service_exists():
                module.fail_json(msg='Service does not exist')
            if not service_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())

        elif module.params['operation'] == 'absent':
            if service_exists():
                if not module.check_mode:
                    service_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if service_exists():
                module.fail_json(msg='Service still exists')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()