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

    sitename:
        description:
            - >-
                Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore (_) character, and must
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                (=), and hyphen (-) characters. Cannot be changed after the virtual server is created.
            - >-
                CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation
                marks (for example, "my gslbsite" or 'my gslbsite').
            - "Minimum length = 1"

    sitetype:
        choices:
            - 'REMOTE'
            - 'LOCAL'
        description:
            - >-
                Type of site to create. If the type is not specified, the appliance automatically detects and sets
                the type on the basis of the IP address being assigned to the site. If the specified site IP address
                is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site.
                Otherwise, it is a remote site.
            - "Default value: NONE"

    siteipaddress:
        description:
            - >-
                IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB
                sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or
                MIP address, or the IP address of the ADNS service).
            - "Minimum length = 1"

    publicip:
        description:
            - >-
                Public IP address for the local site. Required only if the appliance is deployed in a private address
                space and the site has a public IP address hosted on an external firewall or a NAT device.
            - "Minimum length = 1"

    metricexchange:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The
                appliances in the GSLB setup exchange health information once every second.
            - >-
                If you disable metrics exchange, you can use only static load balancing methods (such as round robin,
                static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load
                balancing method (such as least connection) is in operation, the appliance falls back to round robin.
                Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB
                services. Otherwise, the service is marked as DOWN.
            - "Default value: ENABLED"

    nwmetricexchange:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from
                communications with various local DNS (LDNS) servers used by clients. RTT information is used in the
                dynamic RTT load balancing method, and is exchanged every 5 seconds.
            - "Default value: ENABLED"

    sessionexchange:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Exchange persistent session entries with other GSLB sites every five seconds."
            - "Default value: ENABLED"

    triggermonitor:
        choices:
            - 'ALWAYS'
            - 'MEPDOWN'
            - 'MEPDOWN_SVCDOWN'
        description:
            - >-
                Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound.
                Available settings function as follows:
            - "* ALWAYS - Monitor the GSLB service at all times."
            - >-
                * MEPDOWN - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange
                Protocol (MEP) is disabled.
            - "MEPDOWN_SVCDOWN - Monitor the service in either of the following situations:"
            - "* The exchange of metrics through MEP is disabled."
            - >-
                * The exchange of metrics through MEP is enabled but the status of the service, learned through
                metrics exchange, is DOWN.
            - "Default value: ALWAYS"

    parentsite:
        description:
            - "Parent site of the GSLB site, in a parent-child topology."

    clip:
        description:
            - >-
                Cluster IP address. Specify this parameter to connect to the remote cluster site for GSLB auto-sync.
                Note: The cluster IP address is defined when creating the cluster.

    publicclip:
        description:
            - >-
                IP address to be used to globally access the remote cluster when it is deployed behind a NAT. It can
                be same as the normal cluster IP address.

    naptrreplacementsuffix:
        description:
            - >-
                The naptr replacement suffix configured here will be used to construct the naptr replacement field in
                NAPTR record.
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
        sitename=dict(type='str'),
        sitetype=dict(
            type='str',
            choices=[
                'REMOTE',
                'LOCAL',
            ]
        ),
        siteipaddress=dict(type='str'),
        publicip=dict(type='str'),
        metricexchange=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        nwmetricexchange=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        sessionexchange=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        triggermonitor=dict(
            type='str',
            choices=[
                'ALWAYS',
                'MEPDOWN',
                'MEPDOWN_SVCDOWN',
            ]
        ),
        parentsite=dict(type='str'),
        clip=dict(type='str'),
        publicclip=dict(type='str'),
        naptrreplacementsuffix=dict(type='str'),
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
        'sitename',
        'sitetype',
        'siteipaddress',
        'publicip',
        'metricexchange',
        'nwmetricexchange',
        'sessionexchange',
        'triggermonitor',
        'parentsite',
        'clip',
        'publicclip',
        'naptrreplacementsuffix',
    ]

    readonly_attrs = [
        'status',
        'persistencemepstatus',
        'version',
        '__count',
    ]

    immutable_attrs = [
        'sitename',
        'sitetype',
        'siteipaddress',
        'publicip',
        'parentsite',
        'clip',
        'publicclip',
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
