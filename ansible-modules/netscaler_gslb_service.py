#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


DOCUMENTATION = '''
---
module: XXX
short_description: XXX
description:
    - XXX

version_added: "2.3.1"

options:

    servicename:
        description:
            - >-
                Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore (_) character, and
                must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),
                equals (=), and hyphen (-) characters. Can be changed after the GSLB service is created.
            - >-
                CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation
                marks (for example, "my gslbsvc" or 'my gslbsvc').
            - "Minimum length = 1"

    cnameentry:
        description:
            - "Canonical name of the GSLB service. Used in CNAME-based GSLB."
            - "Minimum length = 1"

# TODO move documentation to ipaddress
    ip:
        description:
            - >-
                IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual
                server on the NetScaler appliance, or the IP address of another load balancing device.
            - "Minimum length = 1"

    servername:
        description:
            - "Name of the server hosting the GSLB service."
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
            - "Type of service to create."
            - "Default value: NSSVC_SERVICE_UNKNOWN"
            - >-
                Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP,
                SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE

    port:
        description:
            - "Port on which the load balancing entity represented by this GSLB service listens."
            - "Minimum value = 1"
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    publicip:
        description:
            - >-
                The public IP address that a NAT device translates to the GSLB service's private IP address.
                Optional.

    publicport:
        description:
            - >-
                The public port associated with the GSLB service's public IP address. The port is mapped to the
                service's private port number. Applicable to the local GSLB service. Optional.

    maxclient:
        description:
            - >-
                The maximum number of open connections that the service can support at any given time. A GSLB service
                whose connection count reaches the maximum is not considered when a GSLB decision is made, until the
                connection count drops below the maximum.
            - "Minimum value = 0"
            - "Maximum value = 4294967294"

    healthmonitor:
        choices:
            - 'YES'
            - 'NO'
        description:
            - "Monitor the health of the GSLB service."
            - "Default value: YES"
            - "Possible values = YES, NO"

    sitename:
        description:
            - "Name of the GSLB site to which the service belongs."
            - "Minimum length = 1"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable or disable the service."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    cip:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                In the request that is forwarded to the GSLB service, insert a header that stores the client's IP
                address. Client IP header insertion is used in connection-proxy based site persistence.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    cipheader:
        description:
            - >-
                Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If
                client IP header insertion is enabled on the service and a name is not specified for the header, the
                NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command
                or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.
            - "Minimum length = 1"

    sitepersistence:
        choices:
            - 'ConnectionProxy'
            - 'HTTPRedirect'
            - 'NONE'
        description:
            - "Use cookie-based site persistence. Applicable only to HTTP and SSL GSLB services."
            - "Possible values = ConnectionProxy, HTTPRedirect, NONE"

    siteprefix:
        description:
            - >-
                The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is
                generated internally for each bound service-domain pair by concatenating the site prefix of the
                service and the name of the domain. If the special string NONE is specified, the site-prefix string
                is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB
                requests to GSLB services by using their site domains.

    clttimeout:
        description:
            - >-
                Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy
                based site persistence is used.
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    maxbandwidth:
        description:
            - >-
                Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth
                reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption
                drops below the maximum.

    downstateflush:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Flush all active transactions associated with the GSLB service when its state transitions from UP to
                DOWN. Do not enable this option for services that must complete their transactions. Applicable if
                connection proxy based site persistence is used.
            - "Possible values = ENABLED, DISABLED"

    maxaaausers:
        description:
            - >-
                Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is
                represented by this GSLB service. A GSLB service whose user count reaches the maximum is not
                considered when a GSLB decision is made, until the count drops below the maximum.
            - "Minimum value = 0"
            - "Maximum value = 65535"

    monthreshold:
        description:
            - >-
                Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are
                bound to this GSLB service and are in the UP state is not equal to or greater than this threshold
                value, the service is marked as DOWN.
            - "Minimum value = 0"
            - "Maximum value = 65535"

    hashid:
        description:
            - "Unique hash identifier for the GSLB service, used by hash based load balancing methods."
            - "Minimum value = 1"

    comment:
        description:
            - "Any comments that you might want to associate with the GSLB service."

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable logging appflow flow information."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    ipaddress:
        description:
            - "The new IP address of the service."

extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule
import copy
import requests


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled, monkey_patch_nitro_api
    try:
        monkey_patch_nitro_api()
        from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
        from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice_lbmonitor_binding import gslbservice_lbmonitor_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        servicename=dict(type='str'),
        cnameentry=dict(type='str'),
        servername=dict(type='str'),
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
        port=dict(type='int'),
        publicip=dict(type='str'),
        publicport=dict(type='int'),
        maxclient=dict(type='float'),
        healthmonitor=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ],
        ),
        sitename=dict(type='str'),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
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
        sitepersistence=dict(
            type='str',
            choices=[
                'ConnectionProxy',
                'HTTPRedirect',
                'NONE',
            ]
        ),
        siteprefix=dict(type='str'),
        clttimeout=dict(type='float'),
        maxbandwidth=dict(type='float'),
        downstateflush=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        maxaaausers=dict(type='float'),
        monthreshold=dict(type='float'),
        hashid=dict(type='float'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        ipaddress=dict(type='str'),
    )

    hand_inserted_arguments = dict(
        monitor_bindings=dict(type='list'),
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
    try:
        client.login()
    except requests.exceptions.ConnectionError as e:
        module.fail_json(msg='Could not connect to NS. %s' % str(e))

    readwrite_attrs = [
        'servicename',
        'cnameentry',
        'ip',
        'servername',
        'servicetype',
        'port',
        'publicip',
        'publicport',
        'maxclient',
        'healthmonitor',
        'sitename',
        'state',
        'cip',
        'cipheader',
        'sitepersistence',
        'siteprefix',
        'clttimeout',
        'maxbandwidth',
        'downstateflush',
        'maxaaausers',
        'monthreshold',
        'hashid',
        'comment',
        'appflowlog',
        'ipaddress',
    ]

    readonly_attrs = [
        'gslb',
        'svrstate',
        'svreffgslbstate',
        'gslbthreshold',
        'gslbsvcstats',
        'monstate',
        'preferredlocation',
        'monitor_state',
        'statechangetimesec',
        'tickssincelaststatechange',
        'threshold',
        'clmonowner',
        'clmonview',
        '__count',
    ]

    gslbservice_lbmonitor_binding_rw_attrs = [
        'weight',
        'servicename',
        'monitor_name',
    ]

    params = copy.deepcopy(module.params)
    module.params['ip'] = module.params['ipaddress']

    # Instantiate config proxy
    gslb_service_proxy = ConfigProxy(
        actual=gslbservice(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def gslb_service_exists():
        if gslbservice.count_filtered(client, 'servicename:%s' % module.params['servicename']) > 0:
            return True
        else:
            return False

    def gslb_service_identical():
        gslb_service_list = gslbservice.get_filtered(client, 'servicename:%s' % module.params['servicename'])
        diff_dict = gslb_service_proxy.diff_object(gslb_service_list[0])
        # Ignore ip attribute missing
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def get_actual_monitor_bindings():
        log('get_actual_monitor_bindings')
        # Get actual monitor bindings and index them by monitor_name
        actual_monitor_bindings = {}
        if gslbservice_lbmonitor_binding.count(client, servicename=module.params['servicename']) != 0:
            # Get all monitor bindings associated with the named gslb vserver
            fetched_bindings = gslbservice_lbmonitor_binding.get(client, servicename=module.params['servicename'])
            # index by monitor name
            for binding in fetched_bindings:
                #complete_missing_attributes(binding, gslbservice_lbmonitor_binding_rw_attrs, fill_value=None)
                actual_monitor_bindings[binding.monitor_name] = binding
        return actual_monitor_bindings

    def get_configured_monitor_bindings():
        log('get_configured_monitor_bindings')
        configured_monitor_proxys = {}
        # Get configured monitor bindings and index them by monitor_name
        if module.params['monitor_bindings'] is not None:
            for configured_monitor_bindings in module.params['monitor_bindings']:
                binding_values = copy.deepcopy(configured_monitor_bindings)
                binding_values['servicename'] = module.params['servicename']
                proxy = ConfigProxy(
                    actual=gslbservice_lbmonitor_binding(),
                    client=client,
                    attribute_values_dict=binding_values,
                    readwrite_attrs=gslbservice_lbmonitor_binding_rw_attrs,
                    readonly_attrs=[],
                )
                configured_monitor_proxys[configured_monitor_bindings['monitor_name']] = proxy
        return configured_monitor_proxys


    def monitor_bindings_identical():
        log('monitor_bindings_identical')
        actual_bindings = get_actual_monitor_bindings()
        configured_proxys = get_configured_monitor_bindings()

        actual_keyset = set(actual_bindings.keys())
        configured_keyset = set(configured_proxys.keys())

        symmetric_difference = actual_keyset ^ configured_keyset
        if len(symmetric_difference) != 0:
            log('Symmetric difference %s' % symmetric_difference)
            return False

        # Item for item equality test
        for key, proxy in configured_proxys.items():
            if not proxy.has_equal_attributes(actual_bindings[key]):
                log('monitor binding difference %s' % proxy.diff_object(actual_bindings[key]))
                return False

        # Fallthrough to True result
        return True

    def sync_monitor_bindings():
        log('sync_monitor_bindings')

        actual_monitor_bindings = get_actual_monitor_bindings()
        configured_monitor_proxys = get_configured_monitor_bindings()

        # Delete actual bindings not in configured bindings
        for monitor_name, actual_binding in actual_monitor_bindings.items():
            if monitor_name not in configured_monitor_proxys.keys():
                log('Deleting absent binding for monitor %s' % monitor_name)
                log('dir is %s' % dir(actual_binding))
                gslbservice_lbmonitor_binding.delete(client, actual_binding)

        # Delete and re-add actual bindings that differ from configured
        for proxy_key, binding_proxy in configured_monitor_proxys.items():
            if proxy_key in actual_monitor_bindings:
                actual_binding = actual_monitor_bindings[proxy_key]
                if not binding_proxy.has_equal_attributes(actual_binding):
                    log('Deleting differing binding for monitor %s' % actual_binding.monitor_name)
                    log('dir %s' % dir(actual_binding))
                    log('attribute monitor_name %s' % getattr(actual_binding, 'monitor_name'))
                    log('attribute monitorname %s' % getattr(actual_binding, 'monitorname', None))
                    gslbservice_lbmonitor_binding.delete(client, actual_binding)
                    log('Adding anew binding for monitor %s' % binding_proxy.monitor_name)
                    binding_proxy.add()

        # Add configured monitors that are missing from actual
        for proxy_key, binding_proxy in configured_monitor_proxys.items():
            if proxy_key not in actual_monitor_bindings.keys():
                log('Adding monitor binding for monitor %s' % binding_proxy.monitor_name)
                binding_proxy.add()

    def diff():
        gslb_service_list = gslbservice.get_filtered(client, 'servicename:%s' % module.params['servicename'])
        return gslb_service_proxy.diff_object(gslb_service_list[0])

    def all_identical():
        return gslb_service_identical() and monitor_bindings_identical()

    try:
        ensure_feature_is_enabled(client, 'GSLB')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not gslb_service_exists():
                if not module.check_mode:
                    gslb_service_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not all_identical():
                # Update main configuration object
                if not gslb_service_identical():
                    if not module.check_mode:
                        gslb_service_proxy.update()

                # Update monitor bindigns
                if not monitor_bindings_identical():
                    if not module.check_mode:
                        sync_monitor_bindings()

                # Fallthrough to save and change status update
                module_result['changed'] = True
                client.save_config()
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not gslb_service_exists():
                    module.fail_json(msg='Service does not exist', **module_result)
                if not gslb_service_identical():
                    module.fail_json(msg='Service differs from configured', diff=diff(), **module_result)
                if not monitor_bindings_identical():
                    module.fail_json(msg='Monitor bindings differ from configured', diff=diff(), **module_result)

        elif module.params['operation'] == 'absent':
            if gslb_service_exists():
                if not module.check_mode:
                    gslb_service_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if gslb_service_exists():
                    module.fail_json(msg='Service still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
