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

    servicegroupname:
        description:
            - Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the name is created.
            - Minimum length = 1
    servicetype:
        choices: ['HTTP', 'FTP', 'TCP', 'UDP', 'SSL', 'SSL_BRIDGE', 'SSL_TCP', 'DTLS', 'NNTP', 'RPCSVR', 'DNS', 'ADNS', 'SNMP', 'RTSP', 'DHCPRA', 'ANY', 'SIP_UDP', 'SIP_TCP', 'SIP_SSL', 'DNS_TCP', 'ADNS_TCP', 'MYSQL', 'MSSQL', 'ORACLE', 'RADIUS', 'RADIUSListener', 'RDP', 'DIAMETER', 'SSL_DIAMETER', 'TFTP', 'SMPP', 'PPTP', 'GRE', 'SYSLOGTCP', 'SYSLOGUDP', 'FIX', 'SSL_FIX']
        description:
            - Protocol used to exchange data with the service.
            - Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX
            

    cachetype:
        choices: ['TRANSPARENT', 'REVERSE', 'FORWARD']
        description:
            - Cache type supported by the cache server.
            - Possible values = TRANSPARENT, REVERSE, FORWARD
            

    td:
        
        description:
            - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.
            - Minimum value = 0
            - Maximum value = 4094
            

    maxclient:
        description:
            - Maximum number of simultaneous open connections for the service group.
            - Minimum value = 0
            - Maximum value = 4294967294
            

    maxreq:
        description:
            - Maximum number of requests that can be sent on a persistent connection to the service group.
            - Note: Connection requests beyond this value are rejected.
            - Minimum value = 0
            - Maximum value = 65535

    cacheable:
        choices: ['YES', 'NO']
        description:
            - Use the transparent cache redirection virtual server to forward the request to the cache server.
            - Note: Do not set this parameter if you set the Cache Type.
            - Default value: NO
            - Possible values = YES, NO
            

    cip:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Insert the Client IP header in requests forwarded to the service.
            - Possible values = ENABLED, DISABLED

    cipheader:
        description:
            - Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.
            - Minimum length = 1
            
    usip:
        choices: ['YES', 'NO']
        description:
            - Use client's IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections.
            
    pathmonitor:
        choices: ['YES', 'NO']
        description:
            - Path monitoring for clustering.

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

    healthmonitor:
        choices: ['YES', 'NO']
        description:
            - Monitor the health of this service. Available settings function as follows:
            - YES - Send probes to check the health of the service.
            - NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.
            - Default value: YES

    sc:
        choices: ['ON', 'OFF']
        description:
            - State of the SureConnect feature for the service group.
            - Default value: OFF

    sp:
        choices: ['ON', 'OFF']
        description:
            - Enable surge protection for the service group.
            - Default value: OFF

    rtspsessionidremap:
        choices: ['ON', 'OFF']
        description:
            - Enable RTSP session ID mapping for the service group.
            - Default value: OFF

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
            
    cka:
        choices: ['YES', 'NO']
        description:
            - Enable client keep-alive for the service group.
            
    tcpb:
        choices: ['YES', 'NO']
        description:
            - Enable TCP buffering for the service group.

    cmp:
        choices: ['YES', 'NO']
        description:
            - Enable compression for the specified service.

    maxbandwidth:
        description:
            - Maximum bandwidth, in Kbps, allocated for all the services in the service group.
            - Minimum value = 0
            - Maximum value = 4294967287

    monthreshold:
        description:
            - Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.
            - Minimum value = 0
            - Maximum value = 65535

    state:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Initial state of the service group.
            - Default value: ENABLED

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
            - Default value: ENABLED

    tcpprofilename:
        description:
            - Name of the TCP profile that contains TCP configuration settings for the service group.
            - Minimum length = 1
            - Maximum length = 127

    httpprofilename:
        description:
            - Name of the HTTP profile that contains HTTP configuration settings for the service group.
            - Minimum length = 1
            - Maximum length = 127

    comment:
        description:
            - Any information about the service group.

    appflowlog:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Enable logging of AppFlow information for the specified service group.
            - Default value: ENABLED

    netprofile:
        description:
            - Network profile for the service group.
            - Minimum length = 1
            - Maximum length = 127

    autoscale:
        choices: ['DISABLED', 'DNS', 'POLICY']
        description:
            - Auto scale option for a servicegroup.
            - Default value: DISABLED

    memberport:
        description:
            - member port.

    servername:
        description:
            - Name of the server to which to bind the service group.
            - Minimum length = 1

    port:
        description:
            - Server port number.
            - Range 1 - 65535
            - * in CLI is represented as 65535 in NITRO API

    weight:
        description:
            - Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.
            - Minimum value = 1
            - Maximum value = 100

    customserverid:
        description:
            - The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.
            - Default value: "None"

    serverid:
        description:
            - The identifier for the service. This is used when the persistency type is set to Custom Server ID.

    hashid:
        description:
            - The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.
            - Minimum value = 1

    monitor_name_svc:
        description:
            - Name of the monitor bound to the service group. Used to assign a weight to the monitor.
            - Minimum length = 1

    dup_weight:
        description:
            - weight of the monitor that is bound to servicegroup.
            - Minimum value = 1

    riseapbrstatsmsgcode:
        description:
            - The code indicating the rise apbr status.

    delay:
        description:
            - Time, in seconds, allocated for a shutdown of the services in the service group. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).

    graceful:
        choices: ['YES', 'NO']
        description:
            - Wait for all existing connections to the service to terminate before shutting down the service.
            - Default value: NO

    includemembers:
        description:
            - Display the members of the listed service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
            
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
import copy


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        servicegroupname=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[u'HTTP', u'FTP', u'TCP', u'UDP', u'SSL', u'SSL_BRIDGE', u'SSL_TCP', u'DTLS', u'NNTP', u'RPCSVR', u'DNS', u'ADNS', u'SNMP', u'RTSP', u'DHCPRA', u'ANY', u'SIP_UDP', u'SIP_TCP', u'SIP_SSL', u'DNS_TCP', u'ADNS_TCP', u'MYSQL', u'MSSQL', u'ORACLE', u'RADIUS', u'RADIUSListener', u'RDP', u'DIAMETER', u'SSL_DIAMETER', u'TFTP', u'SMPP', u'PPTP', u'GRE', u'SYSLOGTCP', u'SYSLOGUDP', u'FIX', u'SSL_FIX']
        ),
        cachetype=dict(
            type='str',
            choices=[u'TRANSPARENT', u'REVERSE', u'FORWARD']
        ),
        td=dict(type='float'),
        maxclient=dict(type='float'),
        maxreq=dict(type='float'),
        cacheable=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        cip=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        cipheader=dict(type='str'),
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
        healthmonitor=dict(
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
        clttimeout=dict(type='float'),
        svrtimeout=dict(type='float'),
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
        maxbandwidth=dict(type='float'),
        monthreshold=dict(type='float'),
        state=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        downstateflush=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        netprofile=dict(type='str'),
        autoscale=dict(
            type='str',
            choices=[u'DISABLED', u'DNS', u'POLICY']
        ),
        memberport=dict(type='int'),
        servername=dict(type='str'),
        port=dict(type='int'),
        weight=dict(type='float'),
        customserverid=dict(type='str'),
        serverid=dict(type='float'),
        hashid=dict(type='float'),
        monitor_name_svc=dict(type='str'),
        dup_weight=dict(type='float'),
        riseapbrstatsmsgcode=dict(type='int'),
        delay=dict(type='float'),
        graceful=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        includemembers=dict(type='bool'),
        
        # Following arguments are hand inserted
        servicemembers = dict(type='list'),
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
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

    # Instantiate service group configuration object
    readwrite_attrs = [u'servicegroupname', u'servicetype', u'cachetype', u'td', u'maxclient', u'maxreq', u'cacheable', u'cip', u'cipheader', u'usip', u'pathmonitor', u'pathmonitorindv', u'useproxyport', u'healthmonitor', u'sc', u'sp', u'rtspsessionidremap', u'clttimeout', u'svrtimeout', u'cka', u'tcpb', u'cmp', u'maxbandwidth', u'monthreshold', u'state', u'downstateflush', u'tcpprofilename', u'httpprofilename', u'comment', u'appflowlog', u'netprofile', u'autoscale', u'memberport', u'servername', u'port', u'weight', u'customserverid', u'serverid', u'hashid', u'monitor_name_svc', u'dup_weight', u'riseapbrstatsmsgcode', u'delay', u'graceful', u'includemembers']
    readonly_attrs = [u'numofconnections', u'serviceconftype', u'value', u'svrstate', u'ip', u'monstatcode', u'monstatparam1', u'monstatparam2', u'monstatparam3', u'statechangetimemsec', u'stateupdatereason', u'clmonowner', u'clmonview', u'groupcount', u'riseapbrstatsmsgcode2', u'serviceipstr', u'servicegroupeffectivestate']
    servicegroup_proxy = ConfigProxy(
        actual=servicegroup(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs
    )

    def service_group_exists():
        log('service_group_exists')
        if servicegroup.count_filtered(client, 'servicegroupname:%s' % module.params['servicegroupname']) > 0:
            return True
        else:
            return False

    def service_group_identical():
        log('service_group_identical')
        servicegroups = servicegroup.get_filtered(client, 'servicegroupname:%s' % module.params['servicegroupname'])
        if servicegroup_proxy.has_equal_attributes(servicegroups[0]):
            return True
        else:
            return False

    def get_servicegroups_from_module_params():
        log('get_servicegroups_from_module_params')
        readwrite_attrs = [u'servicegroupname', u'ip', u'port', u'state', u'hashid', u'serverid', u'servername', u'customserverid', u'weight']
        readonly_attrs = [u'delay', u'statechangetimesec', u'svrstate', u'tickssincelaststatechange', u'graceful', u'__count']

        members = []
        for config in module.params['servicemembers']:
            # Make a copy to update
            config = copy.deepcopy(config)
            config['servicegroupname'] = module.params['servicegroupname']
            member_proxy = ConfigProxy(
                actual=servicegroup_servicegroupmember_binding(),
                client=client,
                attribute_values_dict=config,
                readwrite_attrs=readwrite_attrs,
                readonly_attrs=readonly_attrs
            )
            members.append(member_proxy)
        return members



    def service_group_servicemembers_identical():
        log('service_group_servicemembers_identical')
        service_group_members = servicegroup_servicegroupmember_binding.get(client, module.params['servicegroupname'])
        module_service_groups = get_servicegroups_from_module_params()
        log('Number of service group members %s' % len(service_group_members))
        if len(service_group_members) != len(module_service_groups):
            return False

        # Fallthrough to member evaluation
        identical_count = 0
        for actual_member in service_group_members:
            for member in module_service_groups:
                if member.has_equal_attributes(actual_member):
                    identical_count += 1
                    break
        if identical_count != len(service_group_members):
            return False

        # Fallthrough to success
        return True

    def delete_all_servicegroup_members():
        log('delete_all_servicegroup_members')
        if servicegroup_servicegroupmember_binding.count(client, module.params['servicegroupname']) == 0:
            return
        service_group_members = servicegroup_servicegroupmember_binding.get(client, module.params['servicegroupname'])
        log('len %s' % len(service_group_members))
        log('count %s' % servicegroup_servicegroupmember_binding.count(client, module.params['servicegroupname']))
        for member in service_group_members:
            log('%s' % dir(member))
            log('ip %s' % member.ip)
            log('servername %s' % member.servername)
            if all([
                hasattr(member, 'ip'),
                member.ip is not None,
                hasattr(member, 'servername'),
                member.servername is not None,
            ]):
                member.ip = None

            member.servicegroupname = module.params['servicegroupname']
            servicegroup_servicegroupmember_binding.delete(client, member)

    def add_all_servicegroup_members():
        log('add_all_servicegroup_members')
        for member in get_servicegroups_from_module_params():
            member.add()

    try:
        if module.params['operation'] == 'present':
            log('Checking present')
            if not service_group_exists():
                if not module.check_mode:
                    servicegroup_proxy.add()
                    servicegroup_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            elif not service_group_identical():
                if not module.check_mode:
                    servicegroup_proxy.update()
                    client.save_config()
                module_result['changed'] = True

            if not service_group_servicemembers_identical():
                if not module.check_mode:
                    delete_all_servicegroup_members()
                    add_all_servicegroup_members()
                    client.save_config()
                module_result['changed'] = True

            # Sanity check for operation
            log('sanity check')
            '''
            if not service_group_exists():
                module.fail_json(msg='Service group is not present', loglines=loglines)
            if not service_group_identical():
                module.fail_json(msg='Service group is not identical to configuration', loglines=loglines)
            if not service_group_servicemembers_identical():
                module.fail_json(msg='Service group members differ from configuration', loglines=loglines)
                '''

        elif module.params['operation'] == 'absent':
            if service_group_exists():
                if not module.check_mode:
                    servicegroup_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if service_group_exists():
                module.fail_json(msg='Service group is present')
        module_result['configured_servicegroup'] = {}
        module_result['configured_servicegroup']['actual_rw_attributes'] = servicegroup_proxy.get_actual_rw_attributes(filter='servicegroupname')
        module_result['configured_servicegroup']['actual_ro_attributes'] = servicegroup_proxy.get_actual_ro_attributes(filter='servicegroupname')
        module_result['configured_servicegroup']['missing_rw_attributes'] = list(set(readwrite_attrs) - set(module_result['configured_servicegroup']['actual_rw_attributes'].keys()))
        module_result['configured_servicegroup']['missing_ro_attributes'] = list(set(readonly_attrs) - set(module_result['configured_servicegroup']['actual_ro_attributes'].keys()))

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, loglines=loglines)

    client.logout()

    module.exit_json(loglines=loglines, **module_result )

if __name__ == "__main__":
    main()
