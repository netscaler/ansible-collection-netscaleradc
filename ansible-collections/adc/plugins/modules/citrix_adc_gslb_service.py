#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adc_gslb_service
short_description: Manage GSLB services
description:
    - Manage GSLB services
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    servicename:
        description:
            - >-
                Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore (_) character, and
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals
                and hyphen (-) characters. Can be changed after the GSLB service is created.
            - >-
                CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation
                (for example, "my gslbsvc" or 'my gslbsvc').
            - "Minimum length =  1"
        type: str

    cnameentry:
        description:
            - "Canonical name of the GSLB service. Used in CNAME-based GSLB."
            - "Minimum length =  1"
        type: str

    servername:
        description:
            - "Name of the server hosting the GSLB service."
            - "Minimum length =  1"
        type: str

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
        type: str

    port:
        description:
            - "Port on which the load balancing entity represented by this GSLB service listens."
            - "Minimum value = C(1)"
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    publicip:
        description:
            - >-
                The public IP address that a NAT device translates to the GSLB service's private IP address.
        type: str

    publicport:
        description:
            - >-
                The public port associated with the GSLB service's public IP address. The port is mapped to the
                private port number. Applicable to the local GSLB service. Optional.
        type: int

    maxclient:
        description:
            - >-
                The maximum number of open connections that the service can support at any given time. A GSLB service
                connection count reaches the maximum is not considered when a GSLB decision is made, until the
                count drops below the maximum.
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967294)"
        type: str

    healthmonitor:
        description:
            - "Monitor the health of the GSLB service."
        type: bool

    sitename:
        description:
            - "Name of the GSLB site to which the service belongs."
            - "Minimum length =  1"
        type: str

    cip:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                In the request that is forwarded to the GSLB service, insert a header that stores the client's IP
                Client IP header insertion is used in connection-proxy based site persistence.
        type: str

    cipheader:
        description:
            - >-
                Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If
                IP header insertion is enabled on the service and a name is not specified for the header, the Citrix
                uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the
                IP Header parameter in the Configure HTTP Parameters dialog box.
            - "Minimum length =  1"
        type: str

    sitepersistence:
        choices:
            - 'ConnectionProxy'
            - 'HTTPRedirect'
            - 'NONE'
        description:
            - "Use cookie-based site persistence. Applicable only to HTTP and SSL GSLB services."
        type: str

    cookietimeout:
        description:
            - "Timeout value, in minutes, for the cookie, when cookie based site persistence is enabled."
            - "Minimum value = C(0)"
            - "Maximum value = C(1440)"
        type: str

    siteprefix:
        description:
            - >-
                The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is
                internally for each bound service-domain pair by concatenating the site prefix of the service and the
                of the domain. If the special string NONE is specified, the site-prefix string is unset. When
                HTTP redirect site persistence, the Citrix ADC redirects GSLB requests to GSLB services by using
                site domains.
        type: str

    clttimeout:
        description:
            - >-
                Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy
                site persistence is used.
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: int

    svrtimeout:
        description:
            - >-
                Idle time, in seconds, after which a server connection is terminated. Applicable if connection proxy
                site persistence is used.
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: str

    maxbandwidth:
        description:
            - >-
                Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth
                the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops
                the maximum.
        type: str

    downstateflush:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Flush all active transactions associated with the GSLB service when its state transitions from UP to
                Do not enable this option for services that must complete their transactions. Applicable if
                proxy based site persistence is used.
        type: str

    maxaaausers:
        description:
            - >-
                Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is
                by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a
                decision is made, until the count drops below the maximum.
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    monthreshold:
        description:
            - >-
                Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are
                to this GSLB service and are in the UP state is not equal to or greater than this threshold value,
                service is marked as DOWN.
            - "Minimum value = C(0)"
            - "Maximum value = C(65535)"
        type: str

    hashid:
        description:
            - "Unique hash identifier for the GSLB service, used by hash based load balancing methods."
            - "Minimum value = C(1)"
        type: str

    comment:
        description:
            - "Any comments that you might want to associate with the GSLB service."
        type: str

    appflowlog:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Enable logging appflow flow information."
        type: str

    naptrreplacement:
        description:
            - "The replacement domain name for this NAPTR."
            - "Maximum length =  255"
        type: str

    naptrorder:
        description:
            - >-
                An integer specifying the order in which the NAPTR records MUST be processed in order to accurately
                the ordered list of Rules. The ordering is from lowest to highest.
            - "Minimum value = C(1)"
            - "Maximum value = C(65535)"
        type: str

    naptrservices:
        description:
            - "Service Parameters applicable to this delegation path."
            - "Maximum length =  255"
        type: str

    naptrdomainttl:
        description:
            - "Modify the TTL of the internally created naptr domain."
            - "Minimum value = C(1)"
        type: str

    naptrpreference:
        description:
            - >-
                An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the
                higher the preference.
            - "Minimum value = C(1)"
            - "Maximum value = C(65535)"
        type: str

    ipaddress:
        description:
            - "The new IP address of the service."
        type: str

    viewname:
        description:
            - >-
                Name of the DNS view of the service. A DNS view is used in global server load balancing (GSLB) to
                a predetermined IP address to a specific group of clients, which are identified by using a DNS
            - "Minimum length =  1"
        type: str

    viewip:
        description:
            - "IP address to be used for the given view."
        type: str

    weight:
        description:
            - >-
                Weight to assign to the monitor-service binding. A larger number specifies a greater weight.
                to the monitoring threshold, which determines the state of the service.
            - "Minimum value = C(1)"
            - "Maximum value = C(100)"
        type: str

    monitor_name_svc:
        description:
            - "Name of the monitor to bind to the service."
            - "Minimum length =  1"
        type: str

    newname:
        description:
            - "New name for the GSLB service."
            - "Minimum length =  1"
        type: str


    disabled:
        description:
            - When set to C(true) the gslb service state will be set to C(disabled).
            - When set to C(false) the gslb service state will be set to C(enabled).
        type: bool

    monitor_bindings:
        type: list
        elements: dict
        description:
            - List of lbmonitor bindings.
        suboptions:
            monitor_name:
                description:
                    - "Monitor name."
                type: str
            monstate:
                choices:
                    - 'enabled'
                    - 'disabled'
                description:
                    - "State of the monitor bound to gslb service."
                type: str
            weight:
                description:
                    - >-
                        Weight to assign to the monitor-service binding. A larger number specifies a greater weight.
                        to the monitoring threshold, which determines the state of the service.
                    - "Minimum value = C(1)"
                    - "Maximum value = C(100)"
                type: str


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
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
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines,
    NitroAPIFetcher
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)
        self.main_nitro_class = 'gslbservice'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'gslbservice': {
                'attributes_list': [
                    'servicename',
                    'cnameentry',
                    'servername',
                    'servicetype',
                    'port',
                    'publicip',
                    'publicport',
                    'maxclient',
                    'healthmonitor',
                    'sitename',
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
                ],
                'transforms': {
                    'healthmonitor': lambda v: 'YES' if v else 'NO',
                    'cip': lambda v: v.upper(),
                    'downstateflush': lambda v: v.upper(),
                    'appflowlog': lambda v: v.upper(),
                },
                'get_id_attributes': [
                    'servicename',
                ],
                'delete_id_attributes': [
                    'servicename',
                ],
                'non_updateable_attributes': [
                    'cnameentry',
                    'ip',
                    'servername',
                    'servicetype',
                    'port',
                    'sitename',
                    'state',
                    'cookietimeout',
                    'clttimeout',
                    'svrtimeout',
                    'newname',
                ],
            },
            'monitor_bindings': {
                'attributes_list': [
                    'monitor_name',
                    'monstate',
                    'weight',
                ],
                'transforms': {
                    'monstate': lambda v: v.upper(),
                },
                'get_id_attributes': [
                    'servicename',
                ],
                'delete_id_attributes': [
                    'monitor_name',
                    'servicename',
                ]
            },
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.prepared_list = []

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_gslbservice()
        self.calculate_configured_monitor_bindings()

    def calculate_configured_gslbservice(self):
        log('ModuleExecutor.calculate_configured_gslbservice()')
        self.configured_gslbservice = {}
        for attribute in self.attribute_config['gslbservice']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['gslbservice']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_gslbservice[attribute] = value

        # Add state
        disabled_value = self.module.params.get('disabled')
        if disabled_value is not None:
            if disabled_value:
                self.configured_gslbservice['state'] = 'DISABLED'
            else:
                self.configured_gslbservice['state'] = 'ENABLED'

        log('calculated configured glsbservice %s' % self.configured_gslbservice)

    def calculate_configured_monitor_bindings(self):
        log('ModuleExecutor.calculate_configured_monitor_bindings()')
        self.configured_monitor_bindings = []
        if self.module.params.get('monitor_bindings') is None:
            return
        for monitor_binding in self.module.params['monitor_bindings']:
            binding = {}
            binding['servicename'] = self.module.params['servicename']
            for attribute in self.attribute_config['monitor_bindings']['attributes_list']:
                # Disregard null values
                value = monitor_binding.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['monitor_bindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_monitor_bindings.append(binding)
        log('calculated configured monitor bindings %s' % self.configured_monitor_bindings)

    def gslbservice_exists(self):
        log('ModuleExecutor.gslbservice_exists()')
        result = self.fetcher.get('gslbservice', self.module.params['servicename'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            return True
        elif result['nitro_errorcode'] in [258, 1835]:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def create_gslbservice(self):
        log('ModuleExecutor.create_gslbservice()')

        gslbservice_data = copy.deepcopy(self.configured_gslbservice)
        # ip is only valid during creation
        gslbservice_data['ip'] = self.configured_gslbservice.get('ipaddress')
        post_data = {
            'gslbservice': gslbservice_data
        }

        result = self.fetcher.post(post_data=post_data, resource='gslbservice')
        log('post data: %s' % post_data)
        log('result of post: %s' % result)
        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def update_gslbservice(self):
        log('ModuleExecutor.update_gslbservice()')

        # Catching trying to change non updateable attributes is done in self.gslbservice_identical()
        put_payload = copy.deepcopy(self.configured_gslbservice)
        for attribute in self.configured_gslbservice.keys():
            if attribute in self.attribute_config['gslbservice']['non_updateable_attributes']:
                del put_payload[attribute]

        put_data = {
            'gslbservice': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='gslbservice')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def gslbservice_identical(self):
        log('ModuleExecutor.gslbservice_identical()')
        result = self.fetcher.get('gslbservice', self.module.params['servicename'])
        retrieved_object = result['data']['gslbservice'][0]

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        non_updateable_list = []
        # Iterate over keys that already exist in the playbook
        for attribute in self.configured_gslbservice.keys():
            retrieved_value = retrieved_object.get(attribute)
            configured_value = self.configured_gslbservice.get(attribute)
            if retrieved_value != configured_value:
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                diff_list.append('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                entry = 'Attribute "%s" differs. Playbook parameter: "%s". Retrieved NITRO object: "%s"' % (attribute, configured_value, retrieved_value)
                self.prepared_list.append(entry)
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['gslbservice']['non_updateable_attributes']:
                    non_updateable_list.append(attribute)

        self.module_result['diff_list'] = diff_list
        if non_updateable_list != []:
            msg = 'Cannot change value for the following non updateable attributes %s' % non_updateable_list
            self.module.fail_json(msg=msg, **self.module_result)

        if diff_list != []:
            return False
        else:
            return True

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.gslbservice_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Create gslb service')
            if not self.module.check_mode:
                log('gslb service does not exist. Will create.')
                self.create_gslbservice()
        else:
            if not self.gslbservice_identical():
                log('Existing gslb service does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_gslbservice()
            else:
                log('Existing gslb service has identical values to configured.')

        # This will also take into account check mode
        self.sync_bindings()

    def delete_gslbservice(self):
        log('ModuleExecutor.delete_gslbservice()')

        result = self.fetcher.delete(resource='gslbservice', id=self.module.params['servicename'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.gslbservice_exists():
            self.module_result['changed'] = True
            self.prepared_list.append('Delete gslb service')
            if not self.module.check_mode:
                self.delete_gslbservice()

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def get_existing_monitor_bindings(self):
        log('ModuleExecutor.get_existing_monitor_bindings()')
        result = self.fetcher.get('gslbservice_lbmonitor_binding', self.module.params['servicename'])

        if result['nitro_errorcode'] in [258, 1835]:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'gslbservice_lbmonitor_binding' in result['data']:
            return result['data']['gslbservice_lbmonitor_binding']
        else:
            return []

    def add_monitor_binding(self, configured_dict):
        log('ModuleExecutor.add_monitor_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['servicename'] = self.module.params['servicename']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['monitor_bindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'gslbservice_lbmonitor_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='gslbservice_lbmonitor_binding',
            id=self.module.params['servicename'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_monitor_binding(self, configured_dict):
        log('ModuleExecutor.delete_monitor_binding()')

        monitor_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['monitor_bindings']['delete_id_attributes']:
            value = monitor_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='gslbservice_lbmonitor_binding',
            id=self.module.params['servicename'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def monitor_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.monitor_binding_identical()')

        ret_val = True
        for key in configured.keys():
            configured_value = configured.get(key)
            retrieved_value = retrieved.get(key)
            if configured_value != retrieved_value:
                str_tuple = (
                    key,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                log('Monitor binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_monitor_bindings(self):
        log('ModuleExecutor.sync_monitor_bindings()')

        # Parent gslbservice should already exist
        existing_monitor_bindings = self.get_existing_monitor_bindings()

        log('existing_monitor_bindings %s' % existing_monitor_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_monitor_binding in existing_monitor_bindings:
            for configured_monitor_binding in self.configured_monitor_bindings:
                if self.monitor_binding_identical(configured_monitor_binding, existing_monitor_binding):
                    configured_already_present.append(configured_monitor_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                reduced_dict = self.reduced_dict(
                    existing_monitor_binding,
                    self.attribute_config['monitor_bindings']['attributes_list']
                )
                self.prepared_list.append('Delete monitor binding %s' % reduced_dict)
                if not self.module.check_mode:
                    self.delete_monitor_binding(existing_monitor_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_monitor_binding in self.configured_monitor_bindings:
            if configured_monitor_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            reduced_dict = self.reduced_dict(
                configured_monitor_binding,
                self.attribute_config['monitor_bindings']['attributes_list']
            )
            self.prepared_list.append('Add policy binding %s' % reduced_dict)
            if not self.module.check_mode:
                self.add_monitor_binding(configured_monitor_binding)


    def reduced_dict(self, dictionary, include_keys):
        reduced = {}
        for key in dictionary:
            if key in include_keys:
                reduced[key] = dictionary[key]

        return reduced

    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        self.sync_monitor_bindings()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
            elif self.module.params['state'] == 'absent':
                self.delete()

            if self.module._diff:
                self.module_result['diff'] = {'prepared': '\n'.join(self.prepared_list)}

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

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
        maxclient=dict(type='str'),
        healthmonitor=dict(type='bool'),
        sitename=dict(type='str'),
        cip=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
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
        cookietimeout=dict(type='str'),
        siteprefix=dict(type='str'),
        clttimeout=dict(type='int'),
        svrtimeout=dict(type='str'),
        maxbandwidth=dict(type='str'),
        downstateflush=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        maxaaausers=dict(type='str'),
        monthreshold=dict(type='str'),
        hashid=dict(type='str'),
        comment=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ]
        ),
        naptrreplacement=dict(type='str'),
        naptrorder=dict(type='str'),
        naptrservices=dict(type='str'),
        naptrdomainttl=dict(type='str'),
        naptrpreference=dict(type='str'),
        ipaddress=dict(type='str'),
        viewname=dict(type='str'),
        viewip=dict(type='str'),
        weight=dict(type='str'),
        monitor_name_svc=dict(type='str'),
        newname=dict(type='str'),

        disabled=dict(
            type='bool',
        ),

        monitor_bindings=dict(
            type='list',
            elements='dict',
            options=dict(
                monitor_name=dict(type='str'),
                monstate=dict(
                    type='str',
                    choices=[
                        'enabled',
                        'disabled',
                    ]
                ),
                weight=dict(type='str'),
            ),
        ),

    )

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
