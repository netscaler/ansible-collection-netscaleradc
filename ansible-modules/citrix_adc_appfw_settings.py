#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2018 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adc_appfw_settings
short_description: Manage Citrix ADC Web Application Firewall settings.
description:
    - Manage Citrix ADC Web Application Firewall settings.
    - The module uses the NITRO API to make configuration changes to WAF settings on the target Citrix ADC.
    - The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest
    - Note that due to NITRO API limitations this module will always report a changed status even when configuration changes have not taken place.

version_added: "2.8.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)
    - Sumanth Lingappa (@sumanth-lingappa)

options:

    defaultprofile:
        description:
            - >-
                Profile to use when a connection does not match any policy. Default setting is APPFW_BYPASS, which
                unmatched connections back to the Citrix ADC without attempting to filter them further.
            - "Minimum length =  1"
        type: str

    undefaction:
        description:
            - "Profile to use when an application firewall policy evaluates to undefined (UNDEF)."
            - >-
                An UNDEF event indicates an internal error condition. The APPFW_BLOCK built-in profile is the default
                You can specify a different built-in or user-created profile as the UNDEF profile.
            - "Minimum length =  1"
        type: str

    sessiontimeout:
        description:
            - >-
                Timeout, in seconds, after which a user session is terminated. Before continuing to use the protected
                site, the user must establish a new session by opening a designated start URL.
            - "Minimum value = C(1)"
            - "Maximum value = C(65535)"
        type: str

    learnratelimit:
        description:
            - >-
                Maximum number of connections per second that the application firewall learning engine examines to
                new relaxations for learning-enabled security checks. The application firewall drops any connections
                this limit from the list of connections used by the learning engine.
            - "Minimum value = C(1)"
            - "Maximum value = C(1000)"
        type: str

    sessionlifetime:
        description:
            - >-
                Maximum amount of time (in seconds) that the application firewall allows a user session to remain
                regardless of user activity. After this time, the user session is terminated. Before continuing to
                the protected web site, the user must establish a new session by opening a designated start URL.
            - "Minimum value = C(0)"
            - "Maximum value = C(2147483647)"
        type: str

    sessioncookiename:
        description:
            - "Name of the session cookie that the application firewall uses to track user sessions."
            - >-
                Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen
                and underscore (_) symbols.
            - "The following requirement applies only to the Citrix ADC CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                "my cookie name" or 'my cookie name').
            - "Minimum length =  1"
        type: str

    clientiploggingheader:
        description:
            - >-
                Name of an HTTP header that contains the IP address that the client used to connect to the protected
                site or service.
        type: str

    importsizelimit:
        description:
            - >-
                Cumulative total maximum number of bytes in web forms imported to a protected web site. If a user
                to upload files with a total byte count higher than the specified limit, the application firewall
                the request.
            - "Minimum value = C(1)"
            - "Maximum value = C(268435456)"
        type: str

    signatureautoupdate:
        description:
            - "Flag used to enable/disable auto update signatures."
        type: bool

    signatureurl:
        description:
            - "URL to download the mapping file from server."
        type: str

    cookiepostencryptprefix:
        description:
            - "String that is prepended to all encrypted cookie values."
            - "Minimum length =  1"
        type: str

    logmalformedreq:
        description:
            - "Log requests that are so malformed that application firewall parsing doesn't occur."
        type: bool

    geolocationlogging:
        description:
            - "Enable Geo-Location Logging in CEF format logs."
        type: bool

    ceflogging:
        description:
            - "Enable CEF format logs."
        type: bool

    entitydecoding:
        description:
            - "Transform multibyte (double- or half-width) characters to single width characters."
        type: bool

    useconfigurablesecretkey:
        description:
            - "Use configurable secret key in AppFw operations."
        type: bool

    sessionlimit:
        description:
            - >-
                Maximum number of sessions that the application firewall allows to be active, regardless of user
                After the max_limit reaches, No more user session will be created .
            - "Minimum value = C(0)"
            - "Maximum value = C(500000)"
        type: str

    malformedreqaction:
        choices:
            - 'none'
            - 'block'
            - 'log'
            - 'stats'
        description:
            - "flag to define action on malformed requests that application firewall cannot parse."
        type: list



extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- name: setup basic settings
  delegate_to: localhost
  citrix_adc_appfw_settings:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 172.18.0.2
    state: present
    defaultprofile: APPFW_BYPASS
    undefaction: APPFW_BLOCK
    sessiontimeout: "1000"
    learnratelimit: "500"
    sessionlifetime: "2000"
    sessioncookiename: cookie_name
    clientiploggingheader: header_name
    importsizelimit: "268435456"
    signatureautoupdate: on
    signatureurl: http://signature.url
    cookiepostencryptprefix: prepend
    logmalformedreq: on
    geolocationlogging: on
    ceflogging: on
    entitydecoding: on
    useconfigurablesecretkey: on
    sessionlimit: "10000"
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
from ansible.module_utils.network.netscaler.netscaler import NitroResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'appfwsettings'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'appfwsettings': {
                'attributes_list': [
                    'defaultprofile',
                    'undefaction',
                    'sessiontimeout',
                    'learnratelimit',
                    'sessionlifetime',
                    'sessioncookiename',
                    'clientiploggingheader',
                    'importsizelimit',
                    'signatureautoupdate',
                    'signatureurl',
                    'cookiepostencryptprefix',
                    'logmalformedreq',
                    'geolocationlogging',
                    'ceflogging',
                    'entitydecoding',
                    'useconfigurablesecretkey',
                    'sessionlimit',
                    'malformedreqaction',
                ],
                'transforms': {
                    'signatureautoupdate': lambda v: 'ON' if v else 'OFF',
                    'logmalformedreq': lambda v: 'ON' if v else 'OFF',
                    'geolocationlogging': lambda v: 'ON' if v else 'OFF',
                    'ceflogging': lambda v: 'ON' if v else 'OFF',
                    'entitydecoding': lambda v: 'ON' if v else 'OFF',
                    'useconfigurablesecretkey': lambda v: 'ON' if v else 'OFF',
                },
                'get_id_attributes': [
                ],
                'delete_id_attributes': [
                ],
            },

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def update(self):
        log('ModuleExecutor.update()')
        # Check if main object exists
        config = NitroResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attribute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attribute_config[self.main_nitro_class]['transforms'],
        )

        self.module_result['changed'] = True
        if not self.module.check_mode:
            config.update()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update()
            elif self.module.params['state'] == 'absent':
                log('Nothing to do for state absent')

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "Nitro exception: errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        defaultprofile=dict(type='str'),
        undefaction=dict(type='str'),
        sessiontimeout=dict(type='str'),
        learnratelimit=dict(type='str'),
        sessionlifetime=dict(type='str'),
        sessioncookiename=dict(type='str'),
        clientiploggingheader=dict(type='str'),
        importsizelimit=dict(type='str'),
        signatureautoupdate=dict(type='bool'),
        signatureurl=dict(type='str'),
        cookiepostencryptprefix=dict(type='str'),
        logmalformedreq=dict(type='bool'),
        geolocationlogging=dict(type='bool'),
        ceflogging=dict(type='bool'),
        entitydecoding=dict(type='bool'),
        useconfigurablesecretkey=dict(type='bool'),
        sessionlimit=dict(type='str'),
        malformedreqaction=dict(
            type='list',
            choices=[
                'none',
                'block',
                'log',
                'stats',
            ]
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
