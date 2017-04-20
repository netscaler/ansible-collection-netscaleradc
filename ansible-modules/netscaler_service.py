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
            

    port:
        description:
            - Port number of the service.
            - Range 1 - 65535
            - in CLI is represented as 65535 in NITRO API
            
    cleartextport:
        description:
            - Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.
            - Minimum value = 1
            

    cachetype:
        choices: ['TRANSPARENT', 'REVERSE', 'FORWARD']
        description:
            - Cache type supported by the cache server.
            

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

    cip:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.
            
    cipheader:
        description:
            - Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".
            - Minimum length = 1
            

    usip:
        choices: ['YES', 'NO']
        description:
            - Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.

    pathmonitor:
        choices: ['YES', 'NO']
        description:
            - Path monitoring for clustering.

    pathmonitorindv:
        choices: ['YES', 'NO']
        description:
            - Individual Path monitoring decisions.

    useproxyport:
        choices: ['YES', 'NO']
        description:
            - Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.
            - Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.
            

    sc:
        choices: ['ON', 'OFF']
        description:
            - State of SureConnect for the service.
            - Default value: OFF

    sp:
        choices: ['ON', 'OFF']
        description:
            - Enable surge protection for the service.

    rtspsessionidremap:
        choices: ['ON', 'OFF']
        description:
            - Enable RTSP session ID mapping for the service.
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

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
            - Default value: ENABLED

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

    all:
        description:
            - Display both user-configured and dynamically learned services.

    Internal:
        description:
            - Display only dynamically learned services.

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
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor_service_binding import lbmonitor_service_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonbindings_service_binding import lbmonbindings_service_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        name=dict( type='str',),
        ip=dict(type='str'),
        servername=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[u'HTTP', u'FTP', u'TCP', u'UDP', u'SSL', u'SSL_BRIDGE', u'SSL_TCP', u'DTLS', u'NNTP', u'RPCSVR', u'DNS', u'ADNS', u'SNMP', u'RTSP', u'DHCPRA', u'ANY', u'SIP_UDP', u'SIP_TCP', u'SIP_SSL', u'DNS_TCP', u'ADNS_TCP', u'MYSQL', u'MSSQL', u'ORACLE', u'RADIUS', u'RADIUSListener', u'RDP', u'DIAMETER', u'SSL_DIAMETER', u'TFTP', u'SMPP', u'PPTP', u'GRE', u'SYSLOGTCP', u'SYSLOGUDP', u'FIX', u'SSL_FIX']
        ),
        port=dict(type='int'),
        cleartextport=dict(type='int'),
        cachetype=dict(
            type='str',
            choices=[u'TRANSPARENT', u'REVERSE', u'FORWARD']
        ),
        maxclient=dict(type='float'),
        healthmonitor=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
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
        customserverid=dict(type='str'),
        serverid=dict(type='float'),
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
        accessdown=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
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
        hashid=dict(type='float'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        netprofile=dict(type='str'),
        td=dict(type='float'),
        processlocal=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        dnsprofilename=dict(type='str'),
        ipaddress=dict(type='str'),
        weight=dict(type='float'),
        monitor_name_svc=dict(type='str'),
        riseapbrstatsmsgcode=dict(type='int'),
        delay=dict(type='float'),
        graceful=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        all=dict(type='bool'),
        Internal=dict(type='bool'),
    )

    hand_inserted_arguments = dict(
        monitorbindings=dict(type='list'),
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
        loglines=loglines,
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
        'state',
        'downstateflush',
        'tcpprofilename',
        'httpprofilename',
        'hashid',
        'comment',
        'appflowlog',
        'netprofile',
        'td',
        'processlocal',
        'dnsprofilename',
        'ipaddress',
        'weight',
        'monitor_name_svc',
        'riseapbrstatsmsgcode',
        'delay',
        'graceful',
        'all',
        'Internal'
    ]

    readonly_attrs = [
        'numofconnections',
        'policyname',
        'serviceconftype',
        'serviceconftype2',
        'value',
        'gslb',
        'dup_state',
        'publicip',
        'publicport',
        'svrstate',
        'monitor_state',
        'monstatcode',
        'lastresponse',
        'responsetime',
        'riseapbrstatsmsgcode2',
        'monstatparam1',
        'monstatparam2',
        'monstatparam3',
        'statechangetimesec',
        'statechangetimemsec',
        'tickssincelaststatechange',
        'stateupdatereason',
        'clmonowner',
        'clmonview',
        'serviceipstr',
        'oracleserverversion',
    ]

    # Translate module arguments to correspondign config oject attributes
    if module.params['ip'] is None:
        module.params['ip'] = module.params['ipaddress']

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
        log('other ipaddress is %s' % service_list[0].ipaddress)
        # the actual ip address is stored in the ipaddress attribute
        # of the retrieved object
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff_list():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        diff_object = service_proxy.diff_object(service_list[0])
        if 'ip' in diff_object:
            del diff_object['ip']
        return diff_object

    def get_configured_monitor_bindings():
        log('Entering get_configured_monitor_bindings')
        bindings = {}
        if 'monitorbindings' in module.params and module.params['monitorbindings'] is not None:
            for binding in module.params['monitorbindings']:
                readwrite_attrs = [
                    'monitorname',
                    'servicename',
                ]
                readonly_attrs = []
                if isinstance(binding, dict):
                    attribute_values_dict = copy.deepcopy(binding)
                else:
                    attribute_values_dict = {
                        'monitorname': binding
                    }
                attribute_values_dict['servicename'] = module.params['name']
                binding_proxy = ConfigProxy(
                    actual=lbmonitor_service_binding(),
                    client=client,
                    attribute_values_dict=attribute_values_dict,
                    readwrite_attrs=readwrite_attrs,
                    readonly_attrs=readonly_attrs,
                )
                key = attribute_values_dict['monitorname']
                bindings[key] = binding_proxy
        return bindings

    def get_actual_monitor_bindings():
        log('Entering get_actual_monitor_bindings')
        bindings = {}
        if service_lbmonitor_binding.count(client, module.params['name']) == 0:
            return bindings

        # Fallthrough to rest of execution
        for binding in service_lbmonitor_binding.get(client, module.params['name']):
            log('Gettign actual monitor with name %s' % binding.monitor_name)
            key = binding.monitor_name
            bindings[key] = binding

        return bindings

    def monitor_bindings_identical():
        log('Entering monitor_bindings_identical')
        configured_bindings = get_configured_monitor_bindings()
        actual_bindings = get_actual_monitor_bindings()

        configured_key_set = set(configured_bindings.keys())
        actual_key_set = set(actual_bindings.keys())
        symmetrical_diff = configured_key_set ^ actual_key_set
        for default_monitor in ('tcp-default', 'ping-default'):
            if default_monitor in symmetrical_diff:
                log('Excluding %s monitor from key comparison' % default_monitor)
                symmetrical_diff.remove(default_monitor)
        if len(symmetrical_diff) > 0:
            return False

        # Compare key to key
        for key in configured_key_set:
            configured_proxy=configured_bindings[key]
            if any([configured_proxy.monitorname != actual_bindings[key].monitor_name,
                    configured_proxy.servicename !=  actual_bindings[key].name]):
                return False

        # Fallthrought to success
        return True


    def sync_monitor_bindings():
        log('Entering sync_monitor_bindings')
        # Delete existing bindings
        for binding in get_actual_monitor_bindings().values():
            b = lbmonitor_service_binding()
            b.monitorname = binding.monitor_name
            b.servicename = module.params['name']
            # Cannot remove default monitor bindings
            if b.monitorname in ('tcp-default', 'ping-default'):
                continue
            lbmonitor_service_binding.delete(client, b)
            continue

            binding.monitorname = binding.monitor_name
            log('Will delete %s' % dir(binding))
            log('Name %s' % binding.name)
            log('monitor Name %s' % binding.monitor_name)
            binding.delete(client, binding)
            #service_lbmonitor_binding.delete(client, binding)

        # Apply configured bindings

        for binding in get_configured_monitor_bindings().values():
            binding.add()


    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not service_exists():
                if not module.check_mode:
                    service_proxy.add()
                    service_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            elif not service_identical():
                if not module.check_mode:
                    service_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Check bindings
            if not monitor_bindings_identical():
                if not module.check_mode:
                    sync_monitor_bindings()
                    client.save_config()
                module_result['changed'] = True

            # Sanity check for operation
            if not service_exists():
                module.fail_json(msg='Service does not exist')
            if not service_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())

            if not monitor_bindings_identical():
                module.fail_json(msg='Monitor bindings are not identical',loglines=loglines)

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

        module_result['configured_service'] = {}
        module_result['configured_service']['actual_rw_attributes'] = service_proxy.get_actual_rw_attributes()
        module_result['configured_service']['actual_ro_attributes'] = service_proxy.get_actual_ro_attributes()
        module_result['configured_service']['missing_rw_attributes'] = list(set(readwrite_attrs) - set(module_result['configured_service']['actual_rw_attributes'].keys()))
        module_result['configured_service']['missing_ro_attributes'] = list(set(readonly_attrs) - set(module_result['configured_service']['actual_ro_attributes'].keys()))

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module_result['loglines'] = loglines
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()
