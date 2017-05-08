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

version_added: 2.3.1

options:

    name:
        description:
            - "Name for the server."
            - >-
                Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII
                alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
                characters.
            - "Can be changed after the name is created."
            - "Minimum length = 1"

    ipaddress:
        description:
            - >-
                IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the
                name of the server, instead of its IP address, when creating a service. Note: If you do not create a
                server entry, the server IP address that you enter when you create a service becomes the name of the
                server.

    domain:
        description:
            - "Domain name of the server. For a domain based configuration, you must create the server first."
            - "Minimum length = 1"

    translationip:
        description:
            - "IP address used to transform the server's DNS-resolved IP address."

    translationmask:
        description:
            - "The netmask of the translation ip."

    domainresolveretry:
        description:
            - >-
                Time, in seconds, for which the NetScaler appliance must wait, after DNS resolution fails, before
                sending the next DNS query to resolve the domain name.
            - "Default value: 5"
            - "Minimum value = 5"
            - "Maximum value = 20939"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Initial state of the server."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    ipv6address:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use
                the server in the IPv4 addressing mode.
            - "Default value: NO"
            - "Possible values = YES, NO"

    comment:
        description:
            - "Any information about the server."

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID
                of 0.
            - "Minimum value = 0"
            - "Maximum value = 4094"

    domainresolvenow:
        description:
            - "Immediately send a DNS query to resolve the server's domain name."

    delay:
        description:
            - "Time, in seconds, after which all the services configured on the server are disabled."

    graceful:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Shut down gracefully, without accepting any new connections, and disabling each service when all of
                its connections are closed.
            - "Default value: NO"
            - "Possible values = YES, NO"

    Internal:
        description:
            - "Display names of the servers that have been created for internal use."

    newname:
        description:
            - >-
                New name for the server. Must begin with an ASCII alphabetic or underscore (_) character, and must
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                (=), and hyphen (-) characters.
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
        ipaddress=dict(type='str'),
        domain=dict(type='str'),
        translationip=dict(type='str'),
        translationmask=dict(type='str'),
        domainresolveretry=dict(type='int'),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        ipv6address=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        comment=dict(type='str'),
        td=dict(type='float'),
        domainresolvenow=dict(type='bool'),
        delay=dict(type='float'),
        graceful=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        Internal=dict(type='bool'),
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
        'ipaddress',
        'domain',
        'translationip',
        'translationmask',
        'domainresolveretry',
        'state',
        'ipv6address',
        'comment',
        'td',
        'domainresolvenow',
        'delay',
        'graceful',
        'Internal',
        'newname',
    ]

    readonly_attrs = [
        'statechangetimesec',
        'tickssincelaststatechange',
        'autoscale',
        'customserverid',
        'monthreshold',
        'maxclient',
        'maxreq',
        'maxbandwidth',
        'usip',
        'cka',
        'tcpb',
        'cmp',
        'clttimeout',
        'svrtimeout',
        'cipheader',
        'cip',
        'cacheable',
        'sc',
        'sp',
        'downstateflush',
        'appflowlog',
        'boundtd',
        '__count',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
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
                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='Service does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='Service differs from configured', diff=diff(), **module_result)

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
                    module.fail_json(msg='Service still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
