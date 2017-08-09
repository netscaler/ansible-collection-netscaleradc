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

version_added: "2.4.0"

author: George Nikolopoulos (@giorgos-nikolopoulos)

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
            - 'disabled'
            - 'enabled'
        description:
            - "Initial state of the server."
            - "Default value: enabled"

    ipv6address:
        description:
            - >-
                Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use
                the server in the IPv4 addressing mode.
            - "Default value: NO"
        type: bool

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
        description:
            - >-
                Shut down gracefully, without accepting any new connections, and disabling each service when all of
                its connections are closed.
            - "Default value: NO"
        type: bool

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

from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled, get_immutables_intersection
try:
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False


def _exists(client, module):
    if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
        return True
    else:
        return False


def _identical(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    diff_dict = _proxy.diff_object(_list[0])
    if len(diff_dict) == 0:
        return True
    else:
        return False


def diff_list(client, module, _proxy):
    _list = _.get_filtered(client, 'name:%s' % module.params['name'])
    return _proxy.diff_object(_list[0])


def main():

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
                'enabled',
                'disabled',
            ]
        ),
        ipv6address=dict(type='bool'),
        comment=dict(type='str'),
        td=dict(type='float'),
        domainresolvenow=dict(type='bool'),
        delay=dict(type='float'),
        graceful=dict(type='bool'),
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
    if not PYTHON_SDK_IMPORTED:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)

    try:
        client.login()
    except nitro_exception as e:
        msg = "nitro exception during login. errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg)
    except Exception as e:
        if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
            module.fail_json(msg='Connection error %s' % str(e))
        elif str(type(e)) == "<class 'requests.exceptions.SSLError'>":
            module.fail_json(msg='SSL Error %s' % str(e))
        else:
            module.fail_json(msg='Unexpected error during login %s' % str(e))

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

    immutable_attrs = [
        'name',
        'domain',
        'state',
        'ipv6address',
        'td',
        'delay',
        'graceful',
        'Internal',
        'newname',
    ]

    transforms = {
        'graceful': ['bool_yes_no'],
        'ipv6address': ['bool_yes_no'],
    }

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
        transforms=transforms,
    )

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate state
        if module.params['state'] == 'present':
            if not _exists(client, module):
                if not module.check_mode:
                    _proxy.add()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            elif not _identical(client, module, _proxy):

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(_proxy, diff_list(client, module, _proxy).keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(client, module, _proxy), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if not _exists(client, module):
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical(client, module, _proxy):
                    module.fail_json(msg='_ differs from configured', diff=diff(client, module, _proxy), **module_result)

        elif module.params['state'] == 'absent':
            if _exists(client, module):
                if not module.check_mode:
                    _proxy.delete()
                    if module.params['save_config']:
                        client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for state
            if not module.check_mode:
                if _exists(client, module):
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
