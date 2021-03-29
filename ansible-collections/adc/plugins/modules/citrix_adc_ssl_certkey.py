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
module: citrix_adc_ssl_certkey
short_description: Manage ssl cerificate keys.
description:
    - Manage ssl cerificate keys.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    certkey:
        description:
            - >-
                Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore
                character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon
                at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is
            - "The following requirement applies only to the Citrix ADC CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                "my cert" or 'my cert').
            - "Minimum length =  1"
        type: str

    cert:
        description:
            - >-
                Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key
                The certificate file should be present on the appliance's hard-disk drive or solid-state drive.
                a certificate in any location other than the default might cause inconsistency in a high availability
                /nsconfig/ssl/ is the default path.
            - "Minimum length =  1"
        type: str

    key:
        description:
            - >-
                Name of and, optionally, path to the private-key file that is used to form the certificate-key pair.
                certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a
                in any location other than the default might cause inconsistency in a high availability setup.
                is the default path.
            - "Minimum length =  1"
        type: str

    password:
        description:
            - >-
                Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys
                PEM format.
        type: bool

    fipskey:
        description:
            - >-
                Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance,
                a key that was imported into the HSM.
            - "Minimum length =  1"
        type: str

    hsmkey:
        description:
            - >-
                Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS
            - "Minimum length =  1"
        type: str

    inform:
        choices:
            - 'DER'
            - 'PEM'
            - 'PFX'
        description:
            - >-
                Input format of the certificate and the private-key files. The three formats supported by the
                are:
            - "PEM - Privacy Enhanced Mail"
            - "DER - Distinguished Encoding Rule"
            - "PFX - Personal Information Exchange."
        type: str

    passplain:
        description:
            - >-
                Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM
            - "Minimum length =  1"
        type: str

    expirymonitor:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Issue an alert when the certificate is about to expire."
        type: str

    notificationperiod:
        description:
            - >-
                Time, in number of days, before certificate expiration, at which to generate an alert that the
                is about to expire.
            - "Minimum value = C(10)"
            - "Maximum value = C(100)"
        type: str

    bundle:
        description:
            - >-
                Parse the certificate chain as a single file after linking the server certificate to its issuer's
                within the file.
        type: bool

    deletefromdevice:
        description:
            - "Delete cert/key file from file system."
        type: bool

    linkcertkeyname:
        description:
            - "Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair."
            - "Minimum length =  1"
        type: str

    nodomaincheck:
        description:
            - "Override the check for matching domain names during a certificate update operation."
        type: bool

    ocspstaplingcache:
        description:
            - "Clear cached ocspStapling response in certkey."
        type: bool


extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
- name: Setup ssl certkey
  delegate_to: localhost
  citrix_adc_ssl_certkey:
    nitro_user: nsroot
    nitro_pass: nsroot
    nsip: 172.18.0.2

    certkey: certirificate_1
    cert: server.crt
    key: server.key
    expirymonitor: enabled
    notificationperiod: 30
    inform: PEM
    password: False
    passplain: somesecret
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
        self.main_nitro_class = 'sslcertkey'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'sslcertkey': {
                'attributes_list': [
                    'certkey',
                    'cert',
                    'key',
                    'password',
                    'fipskey',
                    'hsmkey',
                    'inform',
                    'passplain',
                    'expirymonitor',
                    'notificationperiod',
                    'bundle',
                    'deletefromdevice',
                    'linkcertkeyname',
                    'nodomaincheck',
                    'ocspstaplingcache',
                ],
                'transforms': {
                    'expirymonitor': lambda v: v.upper(),
                    'bundle': lambda v: 'YES' if v else 'NO',
                },
                'get_id_attributes': [
                    'certkey',
                ],
                'delete_id_attributes': [
                    'certkey',
                    'deletefromdevice',
                ],
                'non_updateable_attributes': [
                ],
            },
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.change_keys = [
            'cert',
            'key',
            'fipskey',
            'inform',
        ]

        self.update_keys = [
            'expirymonitor',
            'notificationperiod',
        ]

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_ssl_certkey()

    def calculate_configured_ssl_certkey(self):
        log('ModuleExecutor.calculate_configured_ssl_certkey()')
        self.configured_ssl_certkey = {}
        for attribute in self.attribute_config['sslcertkey']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['sslcertkey']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_ssl_certkey[attribute] = value

        log('calculated configured ssl certkey %s' % self.configured_ssl_certkey)

    def ssl_certkey_exists(self):
        log('ModuleExecutor.ssl_certkey_exists()')
        result = self.fetcher.get('sslcertkey', self.module.params['certkey'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 1540:
            return False
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        # Fallthrough
        return True

    def create_ssl_certkey(self):
        log('ModuleExecutor.create_ssl_certkey()')

        processed_data = copy.deepcopy(self.configured_ssl_certkey)

        # No domain check is flag for change operation
        if 'nodomaincheck' in processed_data:
            del processed_data['nodomaincheck']

        # Flag for the delete operation
        if 'deletefromdevice' in processed_data:
            del processed_data['deletefromdevice']

        post_data = {
            'sslcertkey': processed_data
        }

        result = self.fetcher.post(post_data=post_data, resource='sslcertkey')
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

    def _get_configured_for_identical_comparison(self):
        log('ModuleExecutor._get_configured_for_identical_comparison()')
        configured = {}
        skip_attributes = [
            'password',  # Never returned from NITRO API
            'passplain',  # Never returned from NITRO API
            'nodomaincheck',  # Flag for change operation
            'bundle',  # Flag for create operation
            'deletefromdevice',  # Flag for the delete operation
        ]
        for attribute in self.configured_ssl_certkey:
            if attribute in skip_attributes:
                continue
            configured[attribute] = self.configured_ssl_certkey[attribute]

        log('Configured for comparison %s' % configured)

        return configured

    def ssl_certkey_identical(self):
        log('ModuleExecutor.ssl_certkey_identical()')
        result = self.fetcher.get('sslcertkey', self.configured_ssl_certkey['certkey'])
        self.retrieved_ssl_certkey = result['data']['sslcertkey'][0]

        # Keep track of what keys are different for update and change operations
        self.differing_keys = []

        diff_list = []
        for attribute in self._get_configured_for_identical_comparison():
            retrieved_value = self.retrieved_ssl_certkey.get(attribute)
            configured_value = self.configured_ssl_certkey.get(attribute)

            if retrieved_value != configured_value:
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                self.differing_keys.append(attribute)
                diff_list.append('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)

            self.module_result['diff_list'] = diff_list

        if diff_list != []:
            return False
        else:
            return True

    def do_change_operation(self):
        log('ModuleExecutor.do_change_operation()')
        processed_data = copy.deepcopy(self.configured_ssl_certkey)

        # bundle is a flag for the create operation
        if 'bundle' in processed_data:
            del processed_data['bundle']

        # Flag for the delete operation
        if 'deletefromdevice' in processed_data:
            del processed_data['deletefromdevice']

        # Remove attributes that are used in the update operation
        for attribute in self.update_keys:
            if attribute in processed_data:
                del processed_data[attribute]

        post_data = {
            'sslcertkey': processed_data
        }

        # Do change operation
        result = self.fetcher.post(
            post_data=post_data,
            resource='sslcertkey',
            action='update',
        )

        log('post data: %s' % post_data)
        log('result of post: %s' % result)

        if result['http_response_data']['status'] == 200:
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

    def do_update_operation(self):
        log('ModuleExecutor.do_update_operation()')

        processed_data = {}
        processed_data['certkey'] = self.configured_ssl_certkey['certkey']

        for attribute in self.update_keys:
            if attribute in self.configured_ssl_certkey:
                processed_data[attribute] = self.configured_ssl_certkey[attribute]

        put_data = {
            'sslcertkey': processed_data
        }

        result = self.fetcher.put(put_data=put_data, resource='sslcertkey')

        log('put data %s' % put_data)
        log('result of put %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def update_ssl_certkey(self):
        log('ModuleExecutor.update_ssl_certkey()')

        changed_keys = list(frozenset(self.differing_keys) & frozenset(self.change_keys))
        if len(changed_keys) > 0:
            log('Keys that force change operation %s' % changed_keys)
            self.do_change_operation()

        updated_keys = list(frozenset(self.differing_keys) & frozenset(self.update_keys))
        if len(updated_keys) > 0:
            log('Keys that force update operations %s' % updated_keys)
            self.do_update_operation()

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        if not self.ssl_certkey_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('ssl certkey does not exist. Will create.')
                self.create_ssl_certkey()
        elif not self.ssl_certkey_identical():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('ssl certkey not identical. Will update.')
                self.update_ssl_certkey()
        else:
            self.module_result['changed'] = False

    def delete_ssl_certkey(self):
        log('ModuleExecutor.delete_ssl_certkey()')

        args = {}

        # Add delete flag if defined
        if 'deletefromdevice' in self.configured_ssl_certkey:
            if self.configured_ssl_certkey['deletefromdevice']:
                args['deletefromdevice'] = 'true'
            else:
                args['deletefromdevice'] = 'false'

        result = self.fetcher.delete(
            resource='sslcertkey',
            id=self.configured_ssl_certkey['certkey'],
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

        if self.ssl_certkey_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_ssl_certkey()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
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
        certkey=dict(type='str'),
        cert=dict(type='str'),
        key=dict(type='str'),
        password=dict(type='bool'),
        fipskey=dict(type='str'),
        hsmkey=dict(type='str'),
        inform=dict(
            type='str',
            choices=[
                'DER',
                'PEM',
                'PFX',
            ],
        ),
        passplain=dict(type='str'),
        expirymonitor=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        notificationperiod=dict(type='str'),
        bundle=dict(type='bool'),
        deletefromdevice=dict(type='bool'),
        linkcertkeyname=dict(type='str'),
        nodomaincheck=dict(type='bool'),
        ocspstaplingcache=dict(type='bool'),

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
