#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_server
short_description: Manage server configuration in Netscaler
description:
    - Manage server configuration in Netscaler

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True

    name:
        
        description:
            
            - Name for the server.
            
            - Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
            
            - Can be changed after the name is created.
            
            - Minimum length = 1
            

    ipaddress:
        
        description:
            
            - IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.
            

    domain:
        
        description:
            
            - Domain name of the server. For a domain based configuration, you must create the server first.
            
            - Minimum length = 1
            

    translationip:
        
        description:
            
            - IP address used to transform the server's DNS-resolved IP address.
            

    translationmask:
        
        description:
            
            - The netmask of the translation ip.
            

    domainresolveretry:
        
        description:
            
            - Time, in seconds, for which the NetScaler appliance must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.
            
            - Default value: 5
            
            - Minimum value = 5
            
            - Maximum value = 20939
            

    state:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Initial state of the server.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    ipv6address:
        choices: ['YES', 'NO']
        description:
            
            - Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    comment:
        
        description:
            
            - Any information about the server.
            

    td:
        
        description:
            
            - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.
            
            - Minimum value = 0
            
            - Maximum value = 4094
            

    domainresolvenow:
        
        description:
            
            - Immediately send a DNS query to resolve the server's domain name.
            

    delay:
        
        description:
            
            - Time, in seconds, after which all the services configured on the server are disabled.
            

    graceful:
        choices: ['YES', 'NO']
        description:
            
            - Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    Internal:
        
        description:
            
            - Display names of the servers that have been created for internal use.
            

    newname:
        
        description:
            
            - New name for the server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
            
            - Minimum length = 1
            

    statechangetimesec:
        
        description:
            
            - Time when last state change happened. Seconds part.
            

    tickssincelaststatechange:
        
        description:
            
            - Time in 10 millisecond ticks since the last state change.
            

    autoscale:
        choices: ['DISABLED', 'DNS', 'POLICY']
        description:
            
            - Auto scale option for a servicegroup.
            
            - Default value: DISABLED
            
            - Possible values = DISABLED, DNS, POLICY
            

    customserverid:
        
        description:
            
            - A positive integer to identify the service. Used when the persistency type is set to Custom Server ID.
            
            - Default value: "None"
            

    monthreshold:
        
        description:
            
            - Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.
            
            - Minimum value = 0
            
            - Maximum value = 65535
            

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
            

    maxbandwidth:
        
        description:
            
            - Maximum bandwidth, in Kbps, allocated for all the services in the service group.
            
            - Minimum value = 0
            
            - Maximum value = 4294967287
            

    usip:
        choices: ['YES', 'NO']
        description:
            
            - Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.
            
            - Possible values = YES, NO
            

    cka:
        choices: ['YES', 'NO']
        description:
            
            - Enable client keep-alive for the service group.
            
            - Possible values = YES, NO
            

    tcpb:
        choices: ['YES', 'NO']
        description:
            
            - Enable TCP buffering for the service group.
            
            - Possible values = YES, NO
            

    cmp:
        choices: ['YES', 'NO']
        description:
            
            - Enable compression for the specified service.
            
            - Possible values = YES, NO
            

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
            

    cipheader:
        
        description:
            
            - Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.
            
            - Minimum length = 1
            

    cip:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.
            
            - Possible values = ENABLED, DISABLED
            

    cacheable:
        choices: ['YES', 'NO']
        description:
            
            - Use the transparent cache redirection virtual server to forward the request to the cache server.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    sc:
        choices: ['ON', 'OFF']
        description:
            
            - State of the SureConnect feature for the service group.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    sp:
        choices: ['ON', 'OFF']
        description:
            
            - Enable surge protection for the service group.
            
            - Default value: OFF
            
            - Possible values = ON, OFF
            

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Perform delayed clean-up of connections to all services in the service group.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    appflowlog:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Enable logging of AppFlow information for the specified service group.
            
            - Default value: ENABLED
            
            - Possible values = ENABLED, DISABLED
            

    boundtd:
        
        description:
            
            - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.
            
            - Minimum value = 0
            
            - Maximum value = 4094
            

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
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.server import server
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
            name=dict(
        type='str',
        
        ),
        
            ipaddress=dict(
        type='str',
        
        ),
        
            domain=dict(
        type='str',
        
        ),
        
            translationip=dict(
        type='str',
        
        ),
        
            translationmask=dict(
        type='str',
        
        ),
        
            domainresolveretry=dict(
        type='int',
        
        ),
        
            state=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            ipv6address=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            comment=dict(
        type='str',
        
        ),
        
            td=dict(
        type='float',
        
        ),
        
            domainresolvenow=dict(
        type='bool',
        
        ),
        
            delay=dict(
        type='float',
        
        ),
        
            graceful=dict(
        type='str',
        choices=[u'YES', u'NO']
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


    # Instantiate Server Config object
    readwrite_attrs = [u'name', u'ip', u'servername', u'servicetype', u'port', u'cleartextport', u'cachetype', u'maxclient', u'healthmonitor', u'maxreq', u'cacheable', u'cip', u'cipheader', u'usip', u'pathmonitor', u'pathmonitorindv', u'useproxyport', u'sc', u'sp', u'rtspsessionidremap', u'clttimeout', u'svrtimeout', u'customserverid', u'serverid', u'cka', u'tcpb', u'cmp', u'maxbandwidth', u'accessdown', u'monthreshold', u'state', u'downstateflush', u'tcpprofilename', u'httpprofilename', u'hashid', u'comment', u'appflowlog', u'netprofile', u'td', u'processlocal', u'dnsprofilename', u'ipaddress', u'weight', u'monitor_name_svc', u'riseapbrstatsmsgcode', u'delay', u'graceful', u'all', u'Internal', u'newname']
    readonly_attrs = [u'numofconnections', u'policyname', u'serviceconftype', u'serviceconftype2', u'value', u'gslb', u'dup_state', u'publicip', u'publicport', u'svrstate', u'monitor_state', u'monstatcode', u'lastresponse', u'responsetime', u'riseapbrstatsmsgcode2', u'monstatparam1', u'monstatparam2', u'monstatparam3', u'statechangetimesec', u'statechangetimemsec', u'tickssincelaststatechange', u'stateupdatereason', u'clmonowner', u'clmonview', u'serviceipstr', u'oracleserverversion', u'__count']
    equivalent_attributes = {
        'ip': ['ipaddress',]
    }

    server_proxy = ConfigProxy(
        actual=server(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        primary_key='name',
    )

    def server_exists():
        if server.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def server_identical():
        server_list = server.get_filtered(client, 'name:%s' % module.params['name'])
        if server_proxy.has_equal_attributes(server_list[0]):
            return True
        else:
            return False

    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not server_exists():
                if not module.check_mode:
                    server_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not server_identical():
                if not module.check_mode:
                    server_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for result
            if not module.check_mode:
                if not server_exists():
                    module.fail_json(msg='Server does not seem to exist')
                if not server_identical():
                    module.fail_json(msg='Server is not configured according to parameters given')

        elif module.params['operation'] == 'absent':
            if server_exists():
                if not module.check_mode:
                    server_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for result
            if not module.check_mode:
                if server_exists():
                    module.fail_json(msg='Server seems to be present')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()

    module.exit_json(**module_result)

if __name__ == "__main__":
    main()