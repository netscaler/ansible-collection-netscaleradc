#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_lb_vserver
short_description: Manage lbvserver configuration in Netscaler
description:
    - Manages configuration of lb vserver in Netscaler appliances

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True
'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Connect to netscaler appliance
    netscaler_lb_vserver:
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

# TODO
# Actual implementation of the module goes here





# TODO add actual module instantiation code

def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines

    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_servicegroup_binding import lbvserver_servicegroup_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
            name=dict(
        type='str',
        
        ),
        
            servicetype=dict(
        type='str',
        choices=[u'HTTP', u'FTP', u'TCP', u'UDP', u'SSL', u'SSL_BRIDGE', u'SSL_TCP', u'DTLS', u'NNTP', u'DNS', u'DHCPRA', u'ANY', u'SIP_UDP', u'SIP_TCP', u'SIP_SSL', u'DNS_TCP', u'RTSP', u'PUSH', u'SSL_PUSH', u'RADIUS', u'RDP', u'MYSQL', u'MSSQL', u'DIAMETER', u'SSL_DIAMETER', u'TFTP', u'ORACLE', u'SMPP', u'SYSLOGTCP', u'SYSLOGUDP', u'FIX', u'SSL_FIX']
        ),
        
            ipv46=dict(
        type='str',
        
        ),
        
            ippattern=dict(
        type='str',
        
        ),
        
            ipmask=dict(
        type='str',
        
        ),
        
            port=dict(
        type='int',
        
        ),
        
            range=dict(
        type='float',
        
        ),
        
            persistencetype=dict(
        type='str',
        choices=[u'SOURCEIP', u'COOKIEINSERT', u'SSLSESSION', u'RULE', u'URLPASSIVE', u'CUSTOMSERVERID', u'DESTIP', u'SRCIPDESTIP', u'CALLID', u'RTSPSID', u'DIAMETER', u'FIXSESSION', u'NONE']
        ),
        
            timeout=dict(
        type='float',
        
        ),
        
            persistencebackup=dict(
        type='str',
        choices=[u'SOURCEIP', u'NONE']
        ),
        
            backuppersistencetimeout=dict(
        type='float',
        
        ),
        
            lbmethod=dict(
        type='str',
        choices=[u'ROUNDROBIN', u'LEASTCONNECTION', u'LEASTRESPONSETIME', u'URLHASH', u'DOMAINHASH', u'DESTINATIONIPHASH', u'SOURCEIPHASH', u'SRCIPDESTIPHASH', u'LEASTBANDWIDTH', u'LEASTPACKETS', u'TOKEN', u'SRCIPSRCPORTHASH', u'LRTM', u'CALLIDHASH', u'CUSTOMLOAD', u'LEASTREQUEST', u'AUDITLOGHASH', u'STATICPROXIMITY']
        ),
        
            hashlength=dict(
        type='float',
        
        ),
        
            netmask=dict(
        type='str',
        
        ),
        
            v6netmasklen=dict(
        type='float',
        
        ),
        
            backuplbmethod=dict(
        type='str',
        choices=[u'ROUNDROBIN', u'LEASTCONNECTION', u'LEASTRESPONSETIME', u'SOURCEIPHASH', u'LEASTBANDWIDTH', u'LEASTPACKETS', u'CUSTOMLOAD']
        ),
        
            cookiename=dict(
        type='str',
        
        ),
        
            rule=dict(
        type='str',
        
        ),
        
            listenpolicy=dict(
        type='str',
        
        ),
        
            listenpriority=dict(
        type='float',
        
        ),
        
            resrule=dict(
        type='str',
        
        ),
        
            persistmask=dict(
        type='str',
        
        ),
        
            v6persistmasklen=dict(
        type='float',
        
        ),
        
            pq=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            sc=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            rtspnat=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            m=dict(
        type='str',
        choices=[u'IP', u'MAC', u'IPTUNNEL', u'TOS']
        ),
        
            tosid=dict(
        type='float',
        
        ),
        
            datalength=dict(
        type='float',
        
        ),
        
            dataoffset=dict(
        type='float',
        
        ),
        
            sessionless=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            state=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            connfailover=dict(
        type='str',
        choices=[u'DISABLED', u'STATEFUL', u'STATELESS']
        ),
        
            redirurl=dict(
        type='str',
        
        ),
        
            cacheable=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            clttimeout=dict(
        type='float',
        
        ),
        
            somethod=dict(
        type='str',
        choices=[u'CONNECTION', u'DYNAMICCONNECTION', u'BANDWIDTH', u'HEALTH', u'NONE']
        ),
        
            sopersistence=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            sopersistencetimeout=dict(
        type='float',
        
        ),
        
            healththreshold=dict(
        type='float',
        
        ),
        
            sothreshold=dict(
        type='float',
        
        ),
        
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
        
            backupvserver=dict(
        type='str',
        
        ),
        
            disableprimaryondown=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            insertvserveripport=dict(
        type='str',
        choices=[u'OFF', u'VIPADDR', u'V6TOV4MAPPING']
        ),
        
            vipheader=dict(
        type='str',
        
        ),
        
            authenticationhost=dict(
        type='str',
        
        ),
        
            authentication=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            authn401=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            authnvsname=dict(
        type='str',
        
        ),
        
            push=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            pushvserver=dict(
        type='str',
        
        ),
        
            pushlabel=dict(
        type='str',
        
        ),
        
            pushmulticlients=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            tcpprofilename=dict(
        type='str',
        
        ),
        
            httpprofilename=dict(
        type='str',
        
        ),
        
            dbprofilename=dict(
        type='str',
        
        ),
        
            comment=dict(
        type='str',
        
        ),
        
            l2conn=dict(
        type='str',
        choices=[u'ON', u'OFF']
        ),
        
            oracleserverversion=dict(
        type='str',
        choices=[u'10G', u'11G']
        ),
        
            mssqlserverversion=dict(
        type='str',
        choices=[u'70', u'2000', u'2000SP1', u'2005', u'2008', u'2008R2', u'2012', u'2014']
        ),
        
            mysqlprotocolversion=dict(
        type='float',
        
        ),
        
            mysqlserverversion=dict(
        type='str',
        
        ),
        
            mysqlcharacterset=dict(
        type='float',
        
        ),
        
            mysqlservercapabilities=dict(
        type='float',
        
        ),
        
            appflowlog=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            netprofile=dict(
        type='str',
        
        ),
        
            icmpvsrresponse=dict(
        type='str',
        choices=[u'PASSIVE', u'ACTIVE']
        ),
        
            rhistate=dict(
        type='str',
        choices=[u'PASSIVE', u'ACTIVE']
        ),
        
            newservicerequest=dict(
        type='float',
        
        ),
        
            newservicerequestunit=dict(
        type='str',
        choices=[u'PER_SECOND', u'PERCENT']
        ),
        
            newservicerequestincrementinterval=dict(
        type='float',
        
        ),
        
            minautoscalemembers=dict(
        type='float',
        
        ),
        
            maxautoscalemembers=dict(
        type='float',
        
        ),
        
            persistavpno=dict(
        type='list',
        
        ),
        
            skippersistency=dict(
        type='str',
        choices=[u'Bypass', u'ReLb', u'None']
        ),
        
            td=dict(
        type='float',
        
        ),
        
            authnprofile=dict(
        type='str',
        
        ),
        
            macmoderetainvlan=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            dbslb=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            dns64=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            bypassaaaa=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            recursionavailable=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
            processlocal=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
            dnsprofilename=dict(
        type='str',
        
        ),
        
            weight=dict(
        type='float',
        
        ),
        
            servicename=dict(
        type='str',
        
        ),
        
            redirurlflags=dict(
        type='bool',
        
        ),
        
            newname=dict(
        type='str',
        
        ),
        
    )

    argument_spec = dict()
    argument_spec.update(module_specific_arguments)
    argument_spec.update(netscaler_common_arguments)

    # Hand wired arguments
    argument_spec.update(dict( servicebindings=dict(type='list')))
    argument_spec.update(dict( servicegroupbindings=dict(type='list')))

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

    # Instantiate lb vserver object
    readwrite_attrs = [u'name', u'servicetype', u'ipv46', u'ippattern', u'ipmask', u'port', u'range', u'persistencetype', u'timeout', u'persistencebackup', u'backuppersistencetimeout', u'lbmethod', u'hashlength', u'netmask', u'v6netmasklen', u'backuplbmethod', u'cookiename', u'rule', u'listenpolicy', u'listenpriority', u'resrule', u'persistmask', u'v6persistmasklen', u'pq', u'sc', u'rtspnat', u'm', u'tosid', u'datalength', u'dataoffset', u'sessionless', u'state', u'connfailover', u'redirurl', u'cacheable', u'clttimeout', u'somethod', u'sopersistence', u'sopersistencetimeout', u'healththreshold', u'sothreshold', u'sobackupaction', u'redirectportrewrite', u'downstateflush', u'backupvserver', u'disableprimaryondown', u'insertvserveripport', u'vipheader', u'authenticationhost', u'authentication', u'authn401', u'authnvsname', u'push', u'pushvserver', u'pushlabel', u'pushmulticlients', u'tcpprofilename', u'httpprofilename', u'dbprofilename', u'comment', u'l2conn', u'oracleserverversion', u'mssqlserverversion', u'mysqlprotocolversion', u'mysqlserverversion', u'mysqlcharacterset', u'mysqlservercapabilities', u'appflowlog', u'netprofile', u'icmpvsrresponse', u'rhistate', u'newservicerequest', u'newservicerequestunit', u'newservicerequestincrementinterval', u'minautoscalemembers', u'maxautoscalemembers', u'persistavpno', u'skippersistency', u'td', u'authnprofile', u'macmoderetainvlan', u'dbslb', u'dns64', u'bypassaaaa', u'recursionavailable', u'processlocal', u'dnsprofilename', u'weight', u'servicename', u'redirurlflags', u'newname']
    readonly_attrs = [u'value', u'ipmapping', u'ngname', u'type', u'curstate', u'effectivestate', u'status', u'lbrrreason', u'redirect', u'precedence', u'homepage', u'dnsvservername', u'domain', u'policyname', u'cachevserver', u'health', u'gotopriorityexpression', u'ruletype', u'groupname', u'cookiedomain', u'map', u'gt2gb', u'consolidatedlconn', u'consolidatedlconngbl', u'thresholdvalue', u'bindpoint', u'invoke', u'labeltype', u'labelname', u'version', u'totalservices', u'activeservices', u'statechangetimesec', u'statechangetimeseconds', u'statechangetimemsec', u'tickssincelaststatechange', u'isgslb', u'vsvrdynconnsothreshold', u'backupvserverstatus', u'__count']

    lbvserver_proxy = ConfigProxy(
        actual=lbvserver(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def lbvserver_exists():
        log('lbvserver_exists')
        if lbvserver.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False


    def lbvserver_identical():
        log('lbvserver_identical')
        lbvserver_list = lbvserver.get_filtered(client, 'name:%s' % module.params['name'])
        log('diff %s' %  lbvserver_proxy.diff_object(lbvserver_list[0]))
        if lbvserver_proxy.has_equal_attributes(lbvserver_list[0]):
            return True
        else:
            return False

    def lbvserver_diff():
        lbvserver_list = lbvserver.get_filtered(client, 'name:%s' % module.params['name'])
        return lbvserver_proxy.diff_object(lbvserver_list[0])


    def get_configured_service_bindings():

        readwrite_attrs = [u'weight', u'name', u'servicename', u'servicegroupname']
        readonly_attrs = [u'preferredlocation', u'vserverid', u'vsvrbindsvcip', u'servicetype', u'cookieipport', u'port', u'vsvrbindsvcport', u'curstate', u'ipv46', u'dynamicweight', u'__count']

        configured_bindings = {}
        if 'servicebindings' in module.params and module.params['servicebindings'] is not None:
            for binding in module.params['servicebindings']:
                attribute_values_dict = copy.deepcopy(binding)
                attribute_values_dict['name'] = module.params['name']
                key = binding['servicename'].strip()
                configured_bindings[key] = ConfigProxy(
                        actual=lbvserver_service_binding(),
                        client=client,
                        attribute_values_dict=attribute_values_dict,
                        readwrite_attrs=readwrite_attrs,
                        readonly_attrs=readonly_attrs,
                    )
        return configured_bindings

    def get_configured_servicegroup_bindings():
        readwrite_attrs = [u'weight', u'name', u'servicename', u'servicegroupname']
        readonly_attrs = []

        configured_bindings = {}

        if 'servicegroupbindings' in module.params and module.params['servicegroupbindings'] is not None:
            for binding in module.params['servicegroupbindings']:
                attribute_values_dict = copy.deepcopy(binding)
                attribute_values_dict['name'] = module.params['name']
                key = binding['servicegroupname'].strip()
                configured_bindings[key] = ConfigProxy(
                        actual=lbvserver_servicegroup_binding(),
                        client=client,
                        attribute_values_dict=attribute_values_dict,
                        readwrite_attrs=readwrite_attrs,
                        readonly_attrs=readonly_attrs,
                    )

        return configured_bindings

    def get_service_bindings():
        if lbvserver_service_binding.count(client, module.params['name']) == 0:
            return {}
        bindigs_list = lbvserver_service_binding.get(client, module.params['name'])
        bindings = {}
        for item in bindigs_list:
            key = item.servicename
            bindings[key] = item

        return bindings

    def get_servicegroup_bindings():
        log('count %s' % lbvserver_servicegroup_binding.count(client, module.params['name']))
        if lbvserver_servicegroup_binding.count(client, module.params['name']) == 0:
            return {}
        bindigs_list = lbvserver_servicegroup_binding.get(client, module.params['name'])
        bindings = {}
        for item in bindigs_list:
            key = item.servicegroupname
            bindings[key] = item

        return bindings



    def service_bindings_identical():
        log('service_bindings_identical')

        # Compare servicegroup keysets
        configured_servicegroup_bindings = get_configured_servicegroup_bindings()
        servicegroup_bindings = get_servicegroup_bindings()
        configured_keyset = set(configured_servicegroup_bindings.keys())
        service_keyset = set(servicegroup_bindings.keys())
        log('len %s' % len(configured_keyset ^ service_keyset))
        if len(configured_keyset ^ service_keyset) > 0:
            return False

        # Compare servicegroup item to item
        for key in configured_servicegroup_bindings.keys():
            conf = configured_servicegroup_bindings[key]
            serv = servicegroup_bindings[key]
            log('sg diff %s' % conf.diff_object(serv))
            if not conf.has_equal_attributes(serv):
                return False

        # Compare service keysets
        configured_service_bindings = get_configured_service_bindings()
        service_bindings = get_service_bindings()
        configured_keyset = set(configured_service_bindings.keys())
        service_keyset = set(service_bindings.keys())
        if len(configured_keyset ^ service_keyset) > 0:
            return False

        # Compare service item to item
        for key in configured_service_bindings.keys():
            conf = configured_service_bindings[key]
            serv = service_bindings[key]
            log('s diff %s' % conf.diff_object(serv))
            if not conf.has_equal_attributes(serv):
                return False

        # Fallthrough to success
        return True

    def delete_all_servicegroup_bindings():
        log('delete_all_servicegroup_bindings')
        if lbvserver_servicegroup_binding.count(client, module.params['name']) == 0:
            return
        for binding in lbvserver_servicegroup_binding.get(client, module.params['name']):
            binding.name = module.params['name']
            binding.servicename = None
            log('%s %s' % (binding.servicename, binding.servicegroupname))
            lbvserver_servicegroup_binding.delete(client, binding)

    def delete_all_service_bindings():
        log('delete_all_service_bindings')
        if lbvserver_service_binding.count(client, module.params['name']) == 0:
            return
        for binding in lbvserver_service_binding.get(client, module.params['name']):
            binding.name = module.params['name']
            binding.servicegroupname = ''
            binding.delete(client, binding)

    def sync_service_bindings():
        log('sync_service_bindings')
        delete_all_service_bindings()
        delete_all_servicegroup_bindings()

        log('adding service bindings')
        for binding in get_configured_service_bindings().values():
            binding.add()

        log('adding servicegroup bindings')
        for binding in get_configured_servicegroup_bindings().values():
            binding.add()


    try:
        if module.params['operation'] == 'present':
            if not lbvserver_exists():
                log('Add lb vserver')
                if not module.check_mode:
                    lbvserver_proxy.add()
                    lbvserver_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            elif not lbvserver_identical():
                log('Update lb vserver')
                if not module.check_mode:
                    lbvserver_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                log('Present noop')

            if not service_bindings_identical():
                if not module.check_mode:
                    sync_service_bindings()
                    client.save_config()
                module_result['changed'] = True

            # Sanity check
            if not module.check_mode:
                if not lbvserver_exists():
                    module.fail_json(msg='Did not create lb vserver with name %s' % module.params['name'])
                if not lbvserver_identical():
                    module.fail_json(msg='lb vserver %s is not configured correctly' % module.params['name'], diff=lbvserver_diff())
                if not service_bindings_identical():
                    module.fail_json(msg='Service bindings not identical', loglines=loglines)

        elif module.params['operation'] == 'absent':
            if lbvserver_exists():
                if not module.check_mode:
                    log('Delete lb vserver')
                    lbvserver_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                log('Absent noop')
                module_result['changed'] = False

            # Sanity check
            if not module.check_mode:
                if lbvserver_exists():
                    module.fail_json(msg='Lb vserver %s still exists' % module.params['name'])

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, loglines=loglines)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()