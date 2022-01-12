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
module: citrix_adc_nsip
short_description: Manage Citrix ADC nsip address
description:
    - Manage Citrix ADC nsip address

version_added: "1.2.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    ipaddress:
        description:
            - "IPv4 address to create on the Citrix ADC. Cannot be changed after the IP address is created."
            - "Minimum length =  1"
        type: str

    netmask:
        description:
            - "Subnet mask associated with the IP address."
        type: str

    type:
        choices:
            - 'SNIP'
            - 'VIP'
            - 'NSIP'
            - 'GSLBsiteIP'
            - 'CLIP'
        description:
            - >-
                Type of the IP address to create on the Citrix ADC. Cannot be changed after the IP address is
                The following are the different types of Citrix ADC owned IP addresses:
            - >-
                * A Subnet IP (SNIP) address is used by the Citrix ADC to communicate with the servers. The Citrix
                also uses the subnet IP address when generating its own packets, such as packets related to dynamic
                protocols, or to send monitor probes to check the health of the servers.
            - >-
                * A Virtual IP (VIP) address is the IP address associated with a virtual server. It is the IP address
                which clients connect. An appliance managing a wide range of traffic may have many VIPs configured.
                of the attributes of the VIP address are customized to meet the requirements of the virtual server.
            - >-
                * A GSLB site IP (GSLBIP) address is associated with a GSLB site. It is not mandatory to specify a
                address when you initially configure the Citrix ADC. A GSLBIP address is used only when you create a
                site.
            - >-
                * A Cluster IP (CLIP) address is the management address of the cluster. All cluster configurations
                be performed by accessing the cluster through this IP address.
        type: str

    arp:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Respond to ARP requests for this IP address."
        type: str

    icmp:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Respond to ICMP requests for this IP address."
        type: str

    vserver:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Use this option to set (enable or disable) the virtual server attribute for this IP address."
        type: str

    telnet:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow Telnet access to this IP address."
        type: str

    ftp:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow File Transfer Protocol (FTP) access to this IP address."
        type: str

    gui:
        choices:
            - 'ENABLED'
            - 'SECUREONLY'
            - 'DISABLED'
        description:
            - "Allow graphical user interface (GUI) access to this IP address."
        type: str

    ssh:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow secure shell (SSH) access to this IP address."
        type: str

    snmp:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow Simple Network Management Protocol (SNMP) access to this IP address."
        type: str

    mgmtaccess:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow access to management applications on this IP address."
        type: str

    restrictaccess:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Block access to nonmanagement applications on this IP. This option is applicable for MIPs, SNIPs, and
                and is disabled by default. Nonmanagement applications can run on the underlying Citrix ADC Free BSD
                system.
        type: str

    dynamicrouting:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Allow dynamic routing on this IP address. Specific to Subnet IP (SNIP) address."
        type: str

    decrementttl:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Decrement TTL by 1 when ENABLED.This setting is applicable only for UDP traffic."
        type: str

    ospf:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Use this option to enable or disable OSPF on this IP address for the entity."
        type: str

    bgp:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Use this option to enable or disable BGP on this IP address for the entity."
        type: str

    rip:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Use this option to enable or disable RIP on this IP address for the entity."
        type: str

    hostroute:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Option to push the VIP to ZebOS routing table for Kernel route redistribution through dynamic routing
        type: str

    advertiseondefaultpartition:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Advertise VIPs from Shared VLAN on Default Partition."
        type: str

    networkroute:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Option to push the SNIP subnet to ZebOS routing table for Kernel route redistribution through dynamic
                protocol.
        type: str

    tag:
        description:
            - "Tag value for the network/host route associated with this IP."
        type: str

    hostrtgw:
        description:
            - "IP address of the gateway of the route for this VIP address."
        type: str

    metric:
        description:
            - "Integer value to add to or subtract from the cost of the route advertised for the VIP address."
            - "Minimum value = C(-16777215)"
        type: int

    vserverrhilevel:
        choices:
            - 'ONE_VSERVER'
            - 'ALL_VSERVERS'
            - 'NONE'
            - 'VSVR_CNTRLD'
        description:
            - >-
                Advertise the route for the Virtual IP (VIP) address on the basis of the state of the virtual servers
                with that VIP.
            - >-
                * NONE - Advertise the route for the VIP address, regardless of the state of the virtual servers
                with the address.
            - >-
                * ONE VSERVER - Advertise the route for the VIP address if at least one of the associated virtual
                is in UP state.
            - >-
                * ALL VSERVER - Advertise the route for the VIP address if all of the associated virtual servers are
                UP state.
            - >-
                * VSVR_CNTRLD - Advertise the route for the VIP address according to the RHIstate (RHI STATE)
                setting on all the associated virtual servers of the VIP address along with their states.
            - >-
                When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI
                for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated
                the VIP address:
            - >-
                * If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route
                the VIP address.
            - >-
                * If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the
                address if at least one of the associated virtual servers is in UP state.
            - >-
                *If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route
                the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is
                UP state.
        type: str

    vserverrhimode:
        choices:
            - 'DYNAMIC_ROUTING'
            - 'RISE'
        description:
            - "Advertise the route for the Virtual IP (VIP) address using dynamic routing protocols or using RISE"
            - >-
                * DYNMAIC_ROUTING - Advertise the route for the VIP address using dynamic routing protocols (default)
            - "* RISE - Advertise the route for the VIP address using RISE."
        type: str

    ospflsatype:
        choices:
            - 'TYPE1'
            - 'TYPE5'
        description:
            - >-
                Type of LSAs to be used by the OSPF protocol, running on the Citrix ADC, for advertising the route
                this VIP address.
        type: str

    ospfarea:
        description:
            - >-
                ID of the area in which the type1 link-state advertisements (LSAs) are to be advertised for this
                IP (VIP) address by the OSPF protocol running on the Citrix ADC. When this parameter is not set, the
                is advertised on all areas.
            - "Minimum value = C(0)"
            - "Maximum value = C(4294967294)"
        type: str

    vrid:
        description:
            - >-
                A positive integer that uniquely identifies a VMAC address for binding to this VIP address. This
                is used to set up Citrix ADCs in an active-active configuration using VRRP.
            - "Minimum value = C(1)"
            - "Maximum value = C(255)"
        type: str

    icmpresponse:
        choices:
            - 'NONE'
            - 'ONE_VSERVER'
            - 'ALL_VSERVERS'
            - 'VSVR_CNTRLD'
        description:
            - >-
                Respond to ICMP requests for a Virtual IP (VIP) address on the basis of the states of the virtual
                associated with that VIP. Available settings function as follows:
            - >-
                * NONE - The Citrix ADC responds to any ICMP request for the VIP address, irrespective of the states
                the virtual servers associated with the address.
            - >-
                * ONE VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if at least one of
                associated virtual servers is in UP state.
            - >-
                * ALL VSERVER - The Citrix ADC responds to any ICMP request for the VIP address if all of the
                virtual servers are in UP state.
            - >-
                * VSVR_CNTRLD - The behavior depends on the ICMP VSERVER RESPONSE setting on all the associated
                servers.
            - "The following settings can be made for the ICMP VSERVER RESPONSE parameter on a virtual server:"
            - "* If you set ICMP VSERVER RESPONSE to PASSIVE on all virtual servers, Citrix ADC always responds."
            - >-
                * If you set ICMP VSERVER RESPONSE to ACTIVE on all virtual servers, Citrix ADC responds if even one
                server is UP.
            - >-
                * When you set ICMP VSERVER RESPONSE to ACTIVE on some and PASSIVE on others, Citrix ADC responds if
                one virtual server set to ACTIVE is UP.
        type: str

    ownernode:
        description:
            - >-
                The owner node in a Cluster for this IP address. Owner node can vary from 0 to 31. If ownernode is
                specified then the IP is treated as Striped IP.
        type: str

    arpresponse:
        choices:
            - 'NONE'
            - 'ONE_VSERVER'
            - 'ALL_VSERVERS'
        description:
            - >-
                Respond to ARP requests for a Virtual IP (VIP) address on the basis of the states of the virtual
                associated with that VIP. Available settings function as follows:
            - >-
                * NONE - The Citrix ADC responds to any ARP request for the VIP address, irrespective of the states
                the virtual servers associated with the address.
            - >-
                * ONE VSERVER - The Citrix ADC responds to any ARP request for the VIP address if at least one of the
                virtual servers is in UP state.
            - >-
                * ALL VSERVER - The Citrix ADC responds to any ARP request for the VIP address if all of the
                virtual servers are in UP state.
        type: str

    ownerdownresponse:
        description:
            - "in cluster system, if the owner node is down, whether should it respond to icmp/arp."
        type: bool

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of
                TD id 4095 is used reserved for LSN use .
            - "Minimum value = C(0)"
            - "Maximum value = C(4095)"
        type: str

    arpowner:
        description:
            - "The arp owner in a Cluster for this IP address. It can vary from 0 to 31."
        type: str


    disabled:
        description:
            - When set to C(true) the nsip state will be set to C(disabled).
            - When set to C(false) the nsip state will be set to C(enabled).
        type: bool

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

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
'''

import base64
import codecs
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

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'nsip': {
                'attributes_list': [
                    'ipaddress',
                    'netmask',
                    'type',
                    'arp',
                    'icmp',
                    'vserver',
                    'telnet',
                    'ftp',
                    'gui',
                    'ssh',
                    'snmp',
                    'mgmtaccess',
                    'restrictaccess',
                    'dynamicrouting',
                    'decrementttl',
                    'ospf',
                    'bgp',
                    'rip',
                    'hostroute',
                    'advertiseondefaultpartition',
                    'networkroute',
                    'tag',
                    'hostrtgw',
                    'metric',
                    'vserverrhilevel',
                    'vserverrhimode',
                    'ospflsatype',
                    'ospfarea',
                    'vrid',
                    'icmpresponse',
                    'ownernode',
                    'arpresponse',
                    'ownerdownresponse',
                    'td',
                    'arpowner',
                ],
                'transforms': {
                    'arp': lambda v: v.upper(),
                    'icmp': lambda v: v.upper(),
                    'vserver': lambda v: v.upper(),
                    'telnet': lambda v: v.upper(),
                    'ftp': lambda v: v.upper(),
                    'ssh': lambda v: v.upper(),
                    'snmp': lambda v: v.upper(),
                    'mgmtaccess': lambda v: v.upper(),
                    'restrictaccess': lambda v: v.upper(),
                    'dynamicrouting': lambda v: v.upper(),
                    'decrementttl': lambda v: v.upper(),
                    'ospf': lambda v: v.upper(),
                    'bgp': lambda v: v.upper(),
                    'rip': lambda v: v.upper(),
                    'hostroute': lambda v: v.upper(),
                    'advertiseondefaultpartition': lambda v: v.upper(),
                    'networkroute': lambda v: v.upper(),
                    'ownerdownresponse': lambda v: 'YES' if v else 'NO',
                },
                'get_id_attributes': [
                ],
                'delete_id_attributes': [
                    'ipaddress',
                    'td',
                ],
                'non_updateable_attributes': [
                    'type',
                    'state',
                    'ownernode',
                ],
            },
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_nsip()

    def calculate_configured_nsip(self):
        log('ModuleExecutor.calculate_configured_nsip()')
        self.configured_nsip = {}
        for attribute in self.attribute_config['nsip']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['nsip']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_nsip[attribute] = value

        log('calculated configured nsip %s' % self.configured_nsip)

    def nsip_exists(self):
        log('ModuleExecutor.nsip_exists()')
        args = {}
        args['ipaddress'] = self.module.params['ipaddress']
        result = self.fetcher.get('nsip', args=args)

        log('get result %s' % result)

        # NSIP does not exist
        if result['nitro_errorcode'] == 258:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        # Fallthrough

        # Save retrieved file contents for nsip_identical()
        self.retrieved_nsip = result['data']['nsip'][0]

        return True

    def create_nsip(self):
        log('ModuleExecutor.create_nsip()')

        post_data = copy.deepcopy(self.configured_nsip)

        post_data = {
            'nsip': post_data
        }

        result = self.fetcher.post(post_data=post_data, resource='nsip')
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

    def update_nsip(self):
        log('ModuleExecutor.update_nsip()')

        # Catching trying to change non updateable attributes is done in self.nsip_identical()
        put_payload = copy.deepcopy(self.configured_nsip)
        for attribute in self.attribute_config['nsip']['non_updateable_attributes']:
            if attribute in put_payload:
                del put_payload[attribute]

        put_data = {
            'nsip': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='nsip')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def nsip_identical(self):
        log('ModuleExecutor.nsip_identical()')

        diff_list = []
        non_updateable_list = []
        for attribute in self.configured_nsip.keys():
            retrieved_value = self.retrieved_nsip.get(attribute)
            configured_value = self.configured_nsip.get(attribute)
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
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['nsip']['non_updateable_attributes']:
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
        if not self.nsip_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('nsip does not exist. Will create.')
                self.create_nsip()
        else:
            if not self.nsip_identical():
                log('Existing nsip does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_nsip()
            else:
                log('Existing nsip has identical values to configured.')

    def delete_nsip(self):
        log('ModuleExecutor.delete_nsip()')

        args = {}

        td = self.configured_nsip.get('td')
        if td is not None:
            args['td'] = td


        result = self.fetcher.delete(
            resource='nsip',
            id=self.module.params['ipaddress'],
            args=args,
        )
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.nsip_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_nsip()

    def do_state_change(self):
        log('ModuleExecutor.do_state_change()')
        if self.module.check_mode:
            return

        # Fallthrough
        post_data = {
            'nsip': {
                'ipaddress': self.configured_nsip['ipaddress'],
            }
        }

        # Append td if defined
        td = self.configured_nsip.get('td')
        if td is not None:
            post_data['nsip']['td'] = td
        

        disabled = self.module.params.get('disabled')
        # Do not operate if disabled is not defined
        if disabled is None:
            return

        # Fallthrough
        if disabled:
            action = 'disable'
        else:
            action = 'enable'

        log('disable/enable post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='nsip', action=action)
        log('result of post %s' % result)

        if result['http_response_data']['status'] != 200:
            msg = 'Disable/Enable operation failed'
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
                self.do_state_change()
            elif self.module.params['state'] == 'absent':
                self.delete()

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
        ipaddress=dict(type='str'),
        netmask=dict(type='str'),
        type=dict(
            type='str',
            choices=[
                'SNIP',
                'VIP',
                'NSIP',
                'GSLBsiteIP',
                'CLIP',
            ],
        ),
        arp=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        icmp=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        vserver=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        telnet=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        ftp=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        gui=dict(
            type='str',
            choices=[
                'ENABLED',
                'SECUREONLY',
                'DISABLED',
            ],
        ),
        ssh=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        snmp=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        mgmtaccess=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        restrictaccess=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        dynamicrouting=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        decrementttl=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        ospf=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        bgp=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        rip=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        hostroute=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        advertiseondefaultpartition=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        networkroute=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        tag=dict(type='str'),
        hostrtgw=dict(type='str'),
        metric=dict(type='int'),
        vserverrhilevel=dict(
            type='str',
            choices=[
                'ONE_VSERVER',
                'ALL_VSERVERS',
                'NONE',
                'VSVR_CNTRLD',
            ],
        ),
        vserverrhimode=dict(
            type='str',
            choices=[
                'DYNAMIC_ROUTING',
                'RISE',
            ],
        ),
        ospflsatype=dict(
            type='str',
            choices=[
                'TYPE1',
                'TYPE5',
            ],
        ),
        ospfarea=dict(type='str'),
        vrid=dict(type='str'),
        icmpresponse=dict(
            type='str',
            choices=[
                'NONE',
                'ONE_VSERVER',
                'ALL_VSERVERS',
                'VSVR_CNTRLD',
            ],
        ),
        ownernode=dict(type='str'),
        arpresponse=dict(
            type='str',
            choices=[
                'NONE',
                'ONE_VSERVER',
                'ALL_VSERVERS',
            ],
        ),
        ownerdownresponse=dict(type='bool'),
        td=dict(type='str'),
        arpowner=dict(type='str'),

        disabled=dict(
            type='bool',
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
