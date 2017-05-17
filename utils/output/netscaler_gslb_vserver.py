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
                Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore (_) character,
                and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),
                equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.
            - "CLI Users:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, "my vserver" or 'my vserver').
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
            - 'NNTP'
            - 'ANY'
            - 'SIP_UDP'
            - 'SIP_TCP'
            - 'SIP_SSL'
            - 'RADIUS'
            - 'RDP'
            - 'RTSP'
            - 'MYSQL'
            - 'MSSQL'
            - 'ORACLE'
        description:
            - "Protocol used by services bound to the virtual server."
            - >-
                Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP,
                SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE

    iptype:
        choices:
            - 'IPV4'
            - 'IPV6'
        description:
            - "The IP type for this GSLB vserver."
            - "Default value: IPV4"
            - "Possible values = IPV4, IPV6"

    dnsrecordtype:
        choices:
            - 'A'
            - 'AAAA'
            - 'CNAME'
            - 'NAPTR'
        description:
            - "DNS record type to associate with the GSLB virtual server's domain name."
            - "Default value: A"
            - "Possible values = A, AAAA, CNAME, NAPTR"

    lbmethod:
        choices:
            - 'ROUNDROBIN'
            - 'LEASTCONNECTION'
            - 'LEASTRESPONSETIME'
            - 'SOURCEIPHASH'
            - 'LEASTBANDWIDTH'
            - 'LEASTPACKETS'
            - 'STATICPROXIMITY'
            - 'RTT'
            - 'CUSTOMLOAD'
        description:
            - "Load balancing method for the GSLB virtual server."
            - "Default value: LEASTCONNECTION"
            - >-
                Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH,
                LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD

    backupsessiontimeout:
        description:
            - >-
                A non zero value enables the feature whose minimum value is 2 minutes. The feature can be disabled by
                setting the value to zero. The created session is in effect for a specific client per domain.
            - "Minimum value = 0"
            - "Maximum value = 1440"

    backuplbmethod:
        choices:
            - 'ROUNDROBIN'
            - 'LEASTCONNECTION'
            - 'LEASTRESPONSETIME'
            - 'SOURCEIPHASH'
            - 'LEASTBANDWIDTH'
            - 'LEASTPACKETS'
            - 'STATICPROXIMITY'
            - 'RTT'
            - 'CUSTOMLOAD'
        description:
            - >-
                Backup load balancing method. Becomes operational if the primary load balancing method fails or
                cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static
                proximity.
            - >-
                Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH,
                LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD

    netmask:
        description:
            - "IPv4 network mask for use in the SOURCEIPHASH load balancing method."
            - "Minimum length = 1"

    v6netmasklen:
        description:
            - >-
                Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by
                the SOURCEIPHASH load balancing method.
            - "Default value: 128"
            - "Minimum value = 1"
            - "Maximum value = 128"

    tolerance:
        description:
            - >-
                Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a
                site's RTT deviates from the lowest RTT by more than the specified tolerance, the site is not
                considered when the NetScaler appliance makes a GSLB decision. The appliance implements the round
                robin method of global server load balancing between sites whose RTT values are within the specified
                tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the
                site with the lowest RTT.
            - "Minimum value = 0"
            - "Maximum value = 100"

    persistencetype:
        choices:
            - 'SOURCEIP'
            - 'NONE'
        description:
            - "Use source IP address based persistence for the virtual server."
            - >-
                After the load balancing method selects a service for the first packet, the IP address received in
                response to the DNS query is used for subsequent requests from the same client.
            - "Possible values = SOURCEIP, NONE"

    persistenceid:
        description:
            - >-
                The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites
                to identify the GSLB virtual server, and is required if source IP address based or spill over based
                persistence is enabled on the virtual server.
            - "Minimum value = 0"
            - "Maximum value = 65535"

    persistmask:
        description:
            - >-
                The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based
                persistence.
            - "Minimum length = 1"

    v6persistmasklen:
        description:
            - >-
                Number of bits to consider in an IPv6 source IP address when creating source IP address based
                persistence sessions.
            - "Default value: 128"
            - "Minimum value = 1"
            - "Maximum value = 128"

    timeout:
        description:
            - "Idle time, in minutes, after which a persistence entry is cleared."
            - "Default value: 2"
            - "Minimum value = 2"
            - "Maximum value = 1440"

    edr:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Send clients an empty DNS response when the GSLB virtual server is DOWN."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    mir:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Include multiple IP addresses in the DNS responses sent to clients."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    disableprimaryondown:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to
                the UP state. Used when spillover is configured for the virtual server.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    dynamicweight:
        choices:
            - 'SERVICECOUNT'
            - 'SERVICEWEIGHT'
            - 'DISABLED'
        description:
            - >-
                Specify if the appliance should consider the service count, service weights, or ignore both when
                using weight-based load balancing methods. The state of the number of services bound to the virtual
                server help the appliance to select the service.
            - "Default value: DISABLED"
            - "Possible values = SERVICECOUNT, SERVICEWEIGHT, DISABLED"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "State of the GSLB virtual server."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    considereffectivestate:
        choices:
            - 'NONE'
            - 'STATE_ONLY'
        description:
            - >-
                If the primary state of all bound GSLB services is DOWN, consider the effective states of all the
                GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of
                the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To
                disregard the effective state, set the parameter to NONE.
            - >-
                The effective state of a GSLB service is the ability of the corresponding virtual server to serve
                traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB
                service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP
                state.
            - "Default value: NONE"
            - "Possible values = NONE, STATE_ONLY"

    comment:
        description:
            - "Any comments that you might want to associate with the GSLB virtual server."

    somethod:
        choices:
            - 'CONNECTION'
            - 'DYNAMICCONNECTION'
            - 'BANDWIDTH'
            - 'HEALTH'
            - 'NONE'
        description:
            - "Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:"
            - "* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold."
            - >-
                * DYNAMICCONNECTION - Spillover occurs when the number of client connections at the GSLB virtual
                server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not
                specify a spillover threshold for this setting, because the threshold is implied by the Max Clients
                settings of the bound GSLB services.
            - >-
                * BANDWIDTH - Spillover occurs when the bandwidth consumed by the GSLB virtual server's incoming and
                outgoing traffic exceeds the threshold.
            - >-
                * HEALTH - Spillover occurs when the percentage of weights of the GSLB services that are UP drops
                below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual
                server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1
                and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN.
            - "* NONE - Spillover does not occur."
            - "Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE"

    sopersistence:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB
                virtual servers.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    sopersistencetimeout:
        description:
            - "Timeout for spillover persistence, in minutes."
            - "Default value: 2"
            - "Minimum value = 2"
            - "Maximum value = 1440"

    sothreshold:
        description:
            - >-
                Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a
                bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a
                percentage for the HEALTH method (do not enter the percentage symbol).
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
            - "Possible values = DROP, ACCEPT, REDIRECT"

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable logging appflow flow information."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    backupvserver:
        description:
            - >-
                Name of the backup GSLB virtual server to which the appliance should to forward requests if the
                status of the primary GSLB virtual server is down or exceeds its spillover threshold.
            - "Minimum length = 1"

    servicename:
        description:
            - "Name of the GSLB service for which to change the weight."
            - "Minimum length = 1"

    weight:
        description:
            - "Weight to assign to the GSLB service."
            - "Minimum value = 1"
            - "Maximum value = 100"

    domainname:
        description:
            - "Domain name for which to change the time to live (TTL) and/or backup service IP address."
            - "Minimum length = 1"

    ttl:
        description:
            - "Time to live (TTL) for the domain."
            - "Minimum value = 1"

    backupip:
        description:
            - >-
                The IP address of the backup service for the specified domain name. Used when all the services bound
                to the domain are down, or when the backup chain of virtual servers is down.
            - "Minimum length = 1"

    cookie_domain:
        description:
            - "The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response."
            - "Minimum length = 1"

    cookietimeout:
        description:
            - "Timeout, in minutes, for the GSLB site cookie."
            - "Minimum value = 0"
            - "Maximum value = 1440"

    sitedomainttl:
        description:
            - >-
                TTL, in seconds, for all internally created site domains (created when a site prefix is configured on
                a GSLB service) that are associated with this virtual server.
            - "Minimum value = 1"

    newname:
        description:
            - "New name for the GSLB virtual server."
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
        name=dict(type='str'),
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
                'NNTP',
                'ANY',
                'SIP_UDP',
                'SIP_TCP',
                'SIP_SSL',
                'RADIUS',
                'RDP',
                'RTSP',
                'MYSQL',
                'MSSQL',
                'ORACLE',
            ]
        ),
        iptype=dict(
            type='str',
            choices=[
                'IPV4',
                'IPV6',
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
        lbmethod=dict(
            type='str',
            choices=[
                'ROUNDROBIN',
                'LEASTCONNECTION',
                'LEASTRESPONSETIME',
                'SOURCEIPHASH',
                'LEASTBANDWIDTH',
                'LEASTPACKETS',
                'STATICPROXIMITY',
                'RTT',
                'CUSTOMLOAD',
            ]
        ),
        backupsessiontimeout=dict(type='float'),
        backuplbmethod=dict(
            type='str',
            choices=[
                'ROUNDROBIN',
                'LEASTCONNECTION',
                'LEASTRESPONSETIME',
                'SOURCEIPHASH',
                'LEASTBANDWIDTH',
                'LEASTPACKETS',
                'STATICPROXIMITY',
                'RTT',
                'CUSTOMLOAD',
            ]
        ),
        netmask=dict(type='str'),
        v6netmasklen=dict(type='float'),
        tolerance=dict(type='float'),
        persistencetype=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'NONE',
            ]
        ),
        persistenceid=dict(type='float'),
        persistmask=dict(type='str'),
        v6persistmasklen=dict(type='float'),
        timeout=dict(type='float'),
        edr=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        mir=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        disableprimaryondown=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        dynamicweight=dict(
            type='str',
            choices=[
                'SERVICECOUNT',
                'SERVICEWEIGHT',
                'DISABLED',
            ]
        ),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        considereffectivestate=dict(
            type='str',
            choices=[
                'NONE',
                'STATE_ONLY',
            ]
        ),
        comment=dict(type='str'),
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
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        backupvserver=dict(type='str'),
        servicename=dict(type='str'),
        weight=dict(type='float'),
        domainname=dict(type='str'),
        ttl=dict(type='float'),
        backupip=dict(type='str'),
        cookie_domain=dict(type='str'),
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
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    readwrite_attrs = [
        'name',
        'servicetype',
        'iptype',
        'dnsrecordtype',
        'lbmethod',
        'backupsessiontimeout',
        'backuplbmethod',
        'netmask',
        'v6netmasklen',
        'tolerance',
        'persistencetype',
        'persistenceid',
        'persistmask',
        'v6persistmasklen',
        'timeout',
        'edr',
        'ecs',
        'ecsaddrvalidation',
        'mir',
        'disableprimaryondown',
        'dynamicweight',
        'state',
        'considereffectivestate',
        'comment',
        'somethod',
        'sopersistence',
        'sopersistencetimeout',
        'sothreshold',
        'sobackupaction',
        'appflowlog',
        'backupvserver',
        'servicename',
        'weight',
        'domainname',
        'ttl',
        'backupip',
        'cookie_domain',
        'cookietimeout',
        'sitedomainttl',
        'newname',
    ]

    readonly_attrs = [
        'curstate',
        'status',
        'lbrrreason',
        'iscname',
        'sitepersistence',
        'totalservices',
        'activeservices',
        'statechangetimesec',
        'statechangetimemsec',
        'tickssincelaststatechange',
        'health',
        'policyname',
        'priority',
        'gotopriorityexpression',
        'type',
        'vsvrbindsvcip',
        'vsvrbindsvcport',
        '__count',
    ]

    immutable_attrs = [
        'name',
        'servicetype',
        'iptype',
        'backupsessiontimeout',
        'state',
        'cookie_domain',
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
