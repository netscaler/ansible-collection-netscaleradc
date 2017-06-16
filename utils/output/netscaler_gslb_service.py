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
        description:
            - "Monitor the health of the GSLB service."
            - "Default value: YES"

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

    cip:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                In the request that is forwarded to the GSLB service, insert a header that stores the client's IP
                address. Client IP header insertion is used in connection-proxy based site persistence.
            - "Default value: DISABLED"

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

    cookietimeout:
        description:
            - "Timeout value, in minutes, for the cookie, when cookie based site persistence is enabled."
            - "Minimum value = 0"
            - "Maximum value = 1440"

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

    svrtimeout:
        description:
            - >-
                Idle time, in seconds, after which a server connection is terminated. Applicable if connection proxy
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

    naptrreplacement:
        description:
            - "The replacement domain name for this NAPTR."
            - "Maximum length = 255"

    naptrorder:
        description:
            - >-
                An integer specifying the order in which the NAPTR records MUST be processed in order to accurately
                represent the ordered list of Rules. The ordering is from lowest to highest.
            - "Default value: 1"
            - "Minimum value = 1"
            - "Maximum value = 65535"

    naptrservices:
        description:
            - "Service Parameters applicable to this delegation path."
            - "Maximum length = 255"

    naptrdomainttl:
        description:
            - "Modify the TTL of the internally created naptr domain."
            - "Default value: 3600"
            - "Minimum value = 1"

    naptrpreference:
        description:
            - >-
                An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the
                number, higher the preference.
            - "Default value: 1"
            - "Minimum value = 1"
            - "Maximum value = 65535"

    ipaddress:
        description:
            - "The new IP address of the service."

    viewname:
        description:
            - >-
                Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to
                return a predetermined IP address to a specific group of clients, which are identified by using a DNS
                policy.
            - "Minimum length = 1"

    viewip:
        description:
            - "IP address to be used for the given view."

    weight:
        description:
            - >-
                Weight to assign to the monitor-service binding. A larger number specifies a greater weight.
                Contributes to the monitoring threshold, which determines the state of the service.
            - "Minimum value = 1"
            - "Maximum value = 100"

    monitor_name_svc:
        description:
            - "Name of the monitor to bind to the service."
            - "Minimum length = 1"

    newname:
        description:
            - "New name for the GSLB service."
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
        servicename=dict(type='str'),
        cnameentry=dict(type='str'),
        ip=dict(type='str'),
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
        healthmonitor=dict(type='bool'),
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
        cookietimeout=dict(type='float'),
        siteprefix=dict(type='str'),
        clttimeout=dict(type='float'),
        svrtimeout=dict(type='float'),
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
        naptrreplacement=dict(type='str'),
        naptrorder=dict(type='float'),
        naptrservices=dict(type='str'),
        naptrdomainttl=dict(type='float'),
        naptrpreference=dict(type='float'),
        ipaddress=dict(type='str'),
        viewname=dict(type='str'),
        viewip=dict(type='str'),
        weight=dict(type='float'),
        monitor_name_svc=dict(type='str'),
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
        'cookietimeout',
        'siteprefix',
        'clttimeout',
        'svrtimeout',
        'maxbandwidth',
        'downstateflush',
        'maxaaausers',
        'monthreshold',
        'hashid',
        'comment',
        'appflowlog',
        'naptrreplacement',
        'naptrorder',
        'naptrservices',
        'naptrdomainttl',
        'naptrpreference',
        'ipaddress',
        'viewname',
        'viewip',
        'weight',
        'monitor_name_svc',
        'newname',
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

    immutable_attrs = [
        'servicename',
        'cnameentry',
        'ip',
        'servername',
        'servicetype',
        'port',
        'sitename',
        'state',
        'cipheader',
        'cookietimeout',
        'clttimeout',
        'svrtimeout',
        'viewip',
        'monitor_name_svc',
        'newname',
    ]

    transforms = {
        'healthmonitor': ['bool_yes_no'],
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
