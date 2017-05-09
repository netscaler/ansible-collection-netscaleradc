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

    certkey:
        description:
            - >-
                Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore
                (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
                colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key
                pair is created.
            - "The following requirement applies only to the NetScaler CLI:"
            - >-
                If the name includes one or more spaces, enclose the name in double or single quotation marks (for
                example, "my cert" or 'my cert').
            - "Minimum length = 1"

    cert:
        description:
            - >-
                Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key
                pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive.
                Storing a certificate in any location other than the default might cause inconsistency in a high
                availability setup. /nsconfig/ssl/ is the default path.
            - "Minimum length = 1"

    key:
        description:
            - >-
                Name of and, optionally, path to the private-key file that is used to form the certificate-key pair.
                The certificate file should be present on the appliance's hard-disk drive or solid-state drive.
                Storing a certificate in any location other than the default might cause inconsistency in a high
                availability setup. /nsconfig/ssl/ is the default path.
            - "Minimum length = 1"

    password:
        description:
            - >-
                Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys
                in PEM format.

    fipskey:
        description:
            - >-
                Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance,
                or a key that was imported into the HSM.
            - "Minimum length = 1"

    hsmkey:
        description:
            - >-
                Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS
                appliance.
            - "Minimum length = 1"

    inform:
        choices:
            - 'DER'
            - 'PEM'
            - 'PFX'
        description:
            - >-
                Input format of the certificate and the private-key files. The three formats supported by the
                appliance are:
            - "PEM - Privacy Enhanced Mail"
            - "DER - Distinguished Encoding Rule"
            - "PFX - Personal Information Exchange."
            - "Default value: PEM"
            - "Possible values = DER, PEM, PFX"

    passplain:
        description:
            - >-
                Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM
                format.
            - "Minimum length = 1"

    expirymonitor:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Issue an alert when the certificate is about to expire."
            - "Possible values = ENABLED, DISABLED"

    notificationperiod:
        description:
            - >-
                Time, in number of days, before certificate expiration, at which to generate an alert that the
                certificate is about to expire.
            - "Minimum value = 10"
            - "Maximum value = 100"

    bundle:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Parse the certificate chain as a single file after linking the server certificate to its issuer's
                certificate within the file.
            - "Default value: NO"
            - "Possible values = YES, NO"

    linkcertkeyname:
        description:
            - "Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair."
            - "Minimum length = 1"

    nodomaincheck:
        description:
            - "Override the check for matching domain names during a certificate update operation."


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
            ]
        ),
        passplain=dict(type='str'),
        expirymonitor=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        notificationperiod=dict(type='float'),
        bundle=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        linkcertkeyname=dict(type='str'),
        nodomaincheck=dict(type='bool'),
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
        'linkcertkeyname',
        'nodomaincheck',
    ]

    readonly_attrs = [
        'signaturealg',
        'certificatetype',
        'serial',
        'issuer',
        'clientcertnotbefore',
        'clientcertnotafter',
        'daystoexpiration',
        'subject',
        'publickey',
        'publickeysize',
        'version',
        'priority',
        'status',
        'passcrypt',
        'data',
        'servicename',
        '__count',
    ]

    immutable_attrs = [
        'certkey',
        'cert',
        'key',
        'password',
        'fipskey',
        'hsmkey',
        'inform',
        'passplain',
        'bundle',
        'linkcertkeyname',
        'nodomaincheck',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
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

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(gslb_site_proxy, diff().keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='_ differs from configured', diff=diff(), **module_result)

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
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
