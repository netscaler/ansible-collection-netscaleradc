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
                Name for the content switching action. Must begin with an ASCII alphanumeric or underscore (_)
                character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon
                (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the content
                switching action is created.
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, ?my action? or ?my action?).

    targetlbvserver:
        description:
            - "Name of the load balancing virtual server to which the content is switched."

    targetvserver:
        description:
            - "Name of the VPN virtual server to which the content is switched."

    targetvserverexpr:
        description:
            - "Information about this content switching action."

    comment:
        description:
            - "Comments associated with this cs action."

    newname:
        description:
            - >-
                New name for the content switching action. Must begin with an ASCII alphanumeric or underscore (_)
                character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon
                (:), at sign (@), equal sign (=), and hyphen (-) characters.
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, my name or my name).
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
        targetlbvserver=dict(type='str'),
        targetvserver=dict(type='str'),
        targetvserverexpr=dict(type='str'),
        comment=dict(type='str'),
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
        'targetlbvserver',
        'targetvserver',
        'targetvserverexpr',
        'comment',
        'newname',
    ]

    readonly_attrs = [
        'hits',
        'referencecount',
        'undefhits',
        'builtin',
        '__count',
    ]

    immutable_attrs = [
        'name',
        'newname',
    ]

    transforms = {
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
