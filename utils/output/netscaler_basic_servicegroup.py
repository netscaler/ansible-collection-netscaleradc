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

    servicegroupname:
        description:
            - >-
                Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                (=), and hyphen (-) characters. Can be changed after the name is created.
            - "Minimum length = 1"

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
            - "Protocol used to exchange data with the service."
            - >-
                Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP,
                RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS,
                RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX,
                SSL_FIX

    cachetype:
        choices:
            - 'TRANSPARENT'
            - 'REVERSE'
            - 'FORWARD'
        description:
            - "Cache type supported by the cache server."
            - "Possible values = TRANSPARENT, REVERSE, FORWARD"

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID
                of 0.
            - "Minimum value = 0"
            - "Maximum value = 4094"

    maxclient:
        description:
            - "Maximum number of simultaneous open connections for the service group."
            - "Minimum value = 0"
            - "Maximum value = 4294967294"

    maxreq:
        description:
            - "Maximum number of requests that can be sent on a persistent connection to the service group."
            - "Note: Connection requests beyond this value are rejected."
            - "Minimum value = 0"
            - "Maximum value = 65535"

    cacheable:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Use the transparent cache redirection virtual server to forward the request to the cache server."
            - "Note: Do not set this parameter if you set the Cache Type."
            - "Default value: NO"
            - "Possible values = YES, NO"

    cip:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Insert the Client IP header in requests forwarded to the service."
            - "Possible values = ENABLED, DISABLED"

    cipheader:
        description:
            - >-
                Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client
                IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value
                of Client IP Header parameter or the value set by the set ns config command is used as client's IP
                header name.
            - "Minimum length = 1"

    usip:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Use client's IP address as the source IP address when initiating connection to the server. With the
                NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as
                the source IP address to initiate server side connections.
            - "Possible values = YES, NO"

    pathmonitor:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Path monitoring for clustering."
            - "Possible values = YES, NO"

    pathmonitorindv:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Individual Path monitoring decisions."
            - "Possible values = YES, NO"

    useproxyport:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Use the proxy port as the source port when initiating connections with the server. With the NO
                setting, the client-side connection port is used as the source port for the server-side connection.
            - "Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES."
            - "Possible values = YES, NO"

    healthmonitor:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Monitor the health of this service. Available settings function as follows:"
            - "YES - Send probes to check the health of the service."
            - >-
                NO - Do not send probes to check the health of the service. With the NO option, the appliance shows
                the service as UP at all times.
            - "Default value: YES"
            - "Possible values = YES, NO"

    sc:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "State of the SureConnect feature for the service group."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    sp:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Enable surge protection for the service group."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    rtspsessionidremap:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Enable RTSP session ID mapping for the service group."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    clttimeout:
        description:
            - "Time, in seconds, after which to terminate an idle client connection."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    svrtimeout:
        description:
            - "Time, in seconds, after which to terminate an idle server connection."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    cka:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Enable client keep-alive for the service group."
            - "Possible values = YES, NO"

    tcpb:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Enable TCP buffering for the service group."
            - "Possible values = YES, NO"

    cmp:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Enable compression for the specified service."
            - "Possible values = YES, NO"

    maxbandwidth:
        description:
            - "Maximum bandwidth, in Kbps, allocated for all the services in the service group."
            - "Minimum value = 0"
            - "Maximum value = 4294967287"

    monthreshold:
        description:
            - >-
                Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to
                mark a service as UP or DOWN.
            - "Minimum value = 0"
            - "Maximum value = 65535"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Initial state of the service group."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    downstateflush:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Flush all active transactions associated with all the services in the service group whose state
                transitions from UP to DOWN. Do not enable this option for applications that must complete their
                transactions.
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    tcpprofilename:
        description:
            - "Name of the TCP profile that contains TCP configuration settings for the service group."
            - "Minimum length = 1"
            - "Maximum length = 127"

    httpprofilename:
        description:
            - "Name of the HTTP profile that contains HTTP configuration settings for the service group."
            - "Minimum length = 1"
            - "Maximum length = 127"

    comment:
        description:
            - "Any information about the service group."

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable logging of AppFlow information for the specified service group."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    netprofile:
        description:
            - "Network profile for the service group."
            - "Minimum length = 1"
            - "Maximum length = 127"

    autoscale:
        choices:
            - 'DISABLED'
            - 'DNS'
            - 'POLICY'
        description:
            - "Auto scale option for a servicegroup."
            - "Default value: DISABLED"
            - "Possible values = DISABLED, DNS, POLICY"

    memberport:
        description:
            - "member port."

    servername:
        description:
            - "Name of the server to which to bind the service group."
            - "Minimum length = 1"

    port:
        description:
            - "Server port number."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    weight:
        description:
            - >-
                Weight to assign to the servers in the service group. Specifies the capacity of the servers relative
                to the other servers in the load balancing configuration. The higher the weight, the higher the
                percentage of requests sent to the service.
            - "Minimum value = 1"
            - "Maximum value = 100"

    customserverid:
        description:
            - "The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID."
            - "Default value: \"None\""

    serverid:
        description:
            - "The identifier for the service. This is used when the persistency type is set to Custom Server ID."

    hashid:
        description:
            - >-
                The hash identifier for the service. This must be unique for each service. This parameter is used by
                hash based load balancing methods.
            - "Minimum value = 1"

    monitor_name_svc:
        description:
            - "Name of the monitor bound to the service group. Used to assign a weight to the monitor."
            - "Minimum length = 1"

    dup_weight:
        description:
            - "weight of the monitor that is bound to servicegroup."
            - "Minimum value = 1"

    riseapbrstatsmsgcode:
        description:
            - "The code indicating the rise apbr status."

    delay:
        description:
            - >-
                Time, in seconds, allocated for a shutdown of the services in the service group. During this period,
                new requests are sent to the service only for clients who already have persistent sessions on the
                appliance. Requests from new clients are load balanced among other available services. After the
                delay time expires, no requests are sent to the service, and the service is marked as unavailable
                (OUT OF SERVICE).

    graceful:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Wait for all existing connections to the service to terminate before shutting down the service."
            - "Default value: NO"
            - "Possible values = YES, NO"

    includemembers:
        description:
            - >-
                Display the members of the listed service groups in addition to their settings. Can be specified when
                no service group name is provided in the command. In that case, the details displayed for each
                service group are identical to the details displayed when a service group name is provided, except
                that bound monitors are not displayed.

    newname:
        description:
            - "New name for the service group."
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


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled
    try:
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
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
                'SSL_FIX',
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
        td=dict(type='float'),
        maxclient=dict(type='float'),
        maxreq=dict(type='float'),
        cacheable=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        cip=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        cipheader=dict(type='str'),
        usip=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        pathmonitor=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        pathmonitorindv=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        useproxyport=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        healthmonitor=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        sc=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        sp=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        rtspsessionidremap=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        clttimeout=dict(type='float'),
        svrtimeout=dict(type='float'),
        cka=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        tcpb=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        cmp=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        maxbandwidth=dict(type='float'),
        monthreshold=dict(type='float'),
        state=dict(
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
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        netprofile=dict(type='str'),
        autoscale=dict(
            type='str',
            choices=[
                'DISABLED',
                'DNS',
                'POLICY',
            ]
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
            choices=[
                'YES',
                'NO',
            ]
        ),
        includemembers=dict(type='bool'),
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
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    readwrite_attrs = [
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
        'state',
        'downstateflush',
        'tcpprofilename',
        'httpprofilename',
        'comment',
        'appflowlog',
        'netprofile',
        'autoscale',
        'memberport',
        'monconnectionclose',
        'servername',
        'port',
        'weight',
        'customserverid',
        'serverid',
        'hashid',
        'monitor_name_svc',
        'dup_weight',
        'riseapbrstatsmsgcode',
        'delay',
        'graceful',
        'includemembers',
        'newname',
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
        'servicegroupeffectivestate',
        '__count',
    ]

    immutable_attrs = [
        'servicegroupname',
        'servicetype',
        'cachetype',
        'td',
        'cipheader',
        'state',
        'autoscale',
        'memberport',
        'servername',
        'port',
        'serverid',
        'monitor_name_svc',
        'dup_weight',
        'riseapbrstatsmsgcode',
        'delay',
        'graceful',
        'includemembers',
        'newname',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
    )

    def _exists():
        if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def _identical():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = _proxy.diff_object(_list[0])
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        return _proxy.diff_object(_list[0])

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not _exists():
                if not module.check_mode:
                    _proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not _identical():

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(gslb_site_proxy, diff().keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='_ differs from configured', diff=diff(), **module_result)

        elif module.params['operation'] == 'absent':
            if _exists():
                if not module.check_mode:
                    _proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if _exists():
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
