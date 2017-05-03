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
                    'supported_by': 'commiter',
                    'version': '1.0'}


DOCUMENTATION = '''
---
module: netscaler_servicegroup
short_description: Manage service group configuration in Netscaler
description:
    - Manage service group configuration in Netscaler
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance

version_added: 2.2.3
options:

    servicegroupname:
        description:
            - >-
                Name of the service group.
                Must begin with an ASCII alphabetic or underscore (_) character, and must contain
                only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),
                equals (=), and hyphen (-) characters. Can be changed after the name is created.
            - Minimum length = 1
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
        description:
            - Protocol used to exchange data with the service.

    cachetype:
        choices: ['TRANSPARENT', 'REVERSE', 'FORWARD']
        description:
            - Cache type supported by the cache server.
            - Possible values = TRANSPARENT, REVERSE, FORWARD

    maxclient:
        description:
            - Maximum number of simultaneous open connections for the service group.
            - Minimum value = 0
            - Maximum value = 4294967294


    maxreq:
        description:
            - Maximum number of requests that can be sent on a persistent connection to the service group.
            - Note. Connection requests beyond this value are rejected.
            - Minimum value = 0
            - Maximum value = 65535

    cacheable:
        choices: ['YES', 'NO']
        description:
            - Use the transparent cache redirection virtual server to forward the request to the cache server.
            - Note. Do not set this parameter if you set the Cache Type.
            - Default value = NO
            - Possible values = YES, NO


    cip:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Insert the Client IP header in requests forwarded to the service.
            - Possible values = ENABLED, DISABLED

    cipheader:
        description:
            - >-
                Name of the HTTP header whose value must be set to the IP address of the client.
                Used with the Client IP parameter. If client IP insertion is enabled, and the client
                IP header is not specified, the value of Client IP Header parameter or the value set
                by the set ns config command is used as client's IP header name.
            - Minimum length = 1

    usip:
        choices: ['YES', 'NO']
        description:
            - >-
                Use client's IP address as the source IP address when initiating connection
                to the server. With the NO setting, which is the default, a mapped IP (MIP)
                address or subnet IP (SNIP) address is used as the source IP address to
                initiate server side connections.

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
            - >-
                Use the proxy port as the source port when initiating connections
                with the server. With the NO setting, the client-side connection port
                is used as the source port for the server-side connection.
            - Note. This parameter is available only when the Use Source IP (USIP) parameter is set to YES.
            - Possible values = YES, NO

    healthmonitor:
        choices: ['YES', 'NO']
        description:
            - Monitor the health of this service. Available settings function as follows.
            - YES - Send probes to check the health of the service.
            - NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.
            - Default value = YES

    sc:
        choices: ['ON', 'OFF']
        description:
            - State of the SureConnect feature for the service group.
            - Default value = OFF

    sp:
        choices: ['ON', 'OFF']
        description:
            - Enable surge protection for the service group.
            - Default value = OFF

    rtspsessionidremap:
        choices: ['ON', 'OFF']
        description:
            - Enable RTSP session ID mapping for the service group.
            - Default value = OFF

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
            - Default value = ENABLED

    downstateflush:
        choices: ['ENABLED', 'DISABLED']
        description:
            - >-
                Flush all active transactions associated with all the services in the service
                group whose state transitions from UP to DOWN. Do not enable this option for
                applications that must complete their transactions.
            - Default value = ENABLED

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
            - Default value = ENABLED

    netprofile:
        description:
            - Network profile for the service group.
            - Minimum length = 1
            - Maximum length = 127

    autoscale:
        choices: ['DISABLED', 'DNS', 'POLICY']
        description:
            - Auto scale option for a servicegroup.
            - Default value = DISABLED

    memberport:
        description:
            - member port.

    graceful:
        choices: ['YES', 'NO']
        description:
            - Wait for all existing connections to the service to terminate before shutting down the service.
            - Default value = NO

    servicemembers:
        description:
            - A list of dictionaries describing each service member of the service group
            - The dictionary for each member must contain the following keys.
            - ip. The ip address of the service member
            - port. The port of the service member
            - weight. The weight of this service member

    monitorbindings:
        description:
            - A list of monitornames to bind to this service
            - Note that the monitors must have already been setup using the netscaler_lb_monitor module

extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
# Monitor monitor-1 must have been already setup with the netscaler_lb_monitor module

- name: Setup http service group
  local_action:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    ssl_cert_validation: no

    module: netscaler_servicegroup
    operation: present

    servicegroupname: service-group-1
    servicetype: HTTP
    servicemembers:
        - ip: 10.78.78.78
          port: 80
          weight: 50
        - ip: 10.79.79.79
          port: 80
          weight: 50

    monitorbindings:
      - monitor-1
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

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
'''

from ansible.module_utils.basic import AnsibleModule
import copy


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_lbmonitor_binding import servicegroup_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor_servicegroup_binding import lbmonitor_servicegroup_binding
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

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
                'SSL_FIX'
            ]
        ),
        cachetype=dict(
            type='str',
            choices=[u'TRANSPARENT', u'REVERSE', u'FORWARD']
        ),
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
        graceful=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
    )

    hand_inserted_arguments = dict(
        servicemembers=dict(type='list'),
        monitorbindings=dict(type='list'),
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
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution

    client = get_nitro_client(module)
    client.login()

    # Instantiate service group configuration object
    readwrite_attrs = [
        'servicegroupname',
        'servicetype',
        'cachetype',
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
        'state',
        'downstateflush',
        'tcpprofilename',
        'httpprofilename',
        'comment',
        'appflowlog',
        'netprofile',
        'autoscale',
        'memberport',
        'graceful',
    ]

    readonly_attrs = [
        'numofconnections',
        'serviceconftype',
        'value',
        'svrstate',
        'ip',
        'monstatcode',
        'monstatparam1',
        'monstatparam2',
        'monstatparam3',
        'statechangetimemsec',
        'stateupdatereason',
        'clmonowner',
        'clmonview',
        'groupcount',
        'riseapbrstatsmsgcode2',
        'serviceipstr',
        'servicegroupeffectivestate'
    ]

    servicegroup_proxy = ConfigProxy(
        actual=servicegroup(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs
    )

    def service_group_exists():
        log('Checking if service group exists')
        if servicegroup.count_filtered(client, 'servicegroupname:%s' % module.params['servicegroupname']) > 0:
            return True
        else:
            return False

    def service_group_identical():
        log('Checking if service group is identical')
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
        if module.params['servicemembers'] is None:
            return members

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

    def get_configured_monitor_bindings():
        log('Entering get_configured_monitor_bindings')
        bindings = {}
        if 'monitorbindings' in module.params and module.params['monitorbindings'] is not None:
            for binding in module.params['monitorbindings']:
                readwrite_attrs = [
                    'monitorname',
                    'servicegroupname',
                ]
                readonly_attrs = []
                if isinstance(binding, dict):
                    attribute_values_dict = copy.deepcopy(binding)
                else:
                    attribute_values_dict = {
                        'monitorname': binding
                    }
                attribute_values_dict['servicegroupname'] = module.params['servicegroupname']
                binding_proxy = ConfigProxy(
                    actual=lbmonitor_servicegroup_binding(),
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
        if servicegroup_lbmonitor_binding.count(client, module.params['servicegroupname']) == 0:
            return bindings

        # Fallthrough to rest of execution
        for binding in servicegroup_lbmonitor_binding.get(client, module.params['servicegroupname']):
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
            configured_proxy = configured_bindings[key]
            if any([configured_proxy.monitorname != actual_bindings[key].monitor_name,
                    configured_proxy.servicegroupname != actual_bindings[key].servicegroupname]):
                return False

        # Fallthrought to success
        return True

    def sync_monitor_bindings():
        log('Entering sync_monitor_bindings')
        # Delete existing bindings
        for binding in get_actual_monitor_bindings().values():
            b = lbmonitor_servicegroup_binding()
            b.monitorname = binding.monitor_name
            b.servicegroupname = module.params['servicegroupname']
            # Cannot remove default monitor bindings
            if b.monitorname in ('tcp-default', 'ping-default'):
                continue
            lbmonitor_servicegroup_binding.delete(client, b)
            continue

            binding.monitorname = binding.monitor_name
            log('Will delete %s' % dir(binding))
            log('Name %s' % binding.name)
            log('monitor Name %s' % binding.monitor_name)
            binding.delete(client, binding)
            # service_lbmonitor_binding.delete(client, binding)

        # Apply configured bindings

        for binding in get_configured_monitor_bindings().values():
            binding.add()

    try:
        if module.params['operation'] == 'present':
            log('Applying actions for operation present')
            if not service_group_exists():
                if not module.check_mode:
                    log('Adding service group')
                    servicegroup_proxy.add()
                    # TODO: why is the line below necessary?
                    # servicegroup_proxy.update()
                    client.save_config()
                    # log('Updating service group')
                    # servicegroup_proxy.update()
                    # client.save_config()
                module_result['changed'] = True
            elif not service_group_identical():
                if not module.check_mode:
                    servicegroup_proxy.update()
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

            if not service_group_servicemembers_identical():
                if not module.check_mode:
                    delete_all_servicegroup_members()
                    add_all_servicegroup_members()
                    client.save_config()
                module_result['changed'] = True

            # Sanity check for operation
            log('Sanity checks for operation present')
            if not service_group_exists():
                module.fail_json(msg='Service group is not present', **module_result)
            if not service_group_identical():
                module.fail_json(msg='Service group is not identical to configuration', **module_result)
            if not service_group_servicemembers_identical():
                module.fail_json(msg='Service group members differ from configuration', **module_result)
            if not monitor_bindings_identical():
                module.fail_json(msg='Monitor bindings are not identical', **module_result)

        elif module.params['operation'] == 'absent':
            log('Applying actions for operation absent')
            if service_group_exists():
                if not module.check_mode:
                    servicegroup_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            log('Sanity checks for operation absent')
            if service_group_exists():
                module.fail_json(msg='Service group is present', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
