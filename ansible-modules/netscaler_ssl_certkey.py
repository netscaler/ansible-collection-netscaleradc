#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_ssl_certkey
short_description: Manage cs vserver
description:
    - Manage service group configuration in Netscaler

version_added: 2.2
options:
    nsip:
        description:
            - The Nescaler ip address.
        required: True

    certkey:
        description:
            - "Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is created."
            - The following requirement applies only to the NetScaler CLI.
            - If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cert" or 'my cert').
            - Minimum length = 1

    cert:
        description:
            - Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.
            - Minimum length = 1

    key:
        description:
            - Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.
            - Minimum length = 1

    password:
        description:
            - Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format.

    fipskey:
        description:
            - Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance, or a key that was imported into the HSM.
            - Minimum length = 1

    hsmkey:
        description:
            - Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS appliance.
            - Minimum length = 1

    inform:
        choices: ['DER', 'PEM', 'PFX']
        description:
            - Input format of the certificate and the private-key files. The three formats supported by the appliance are.
            - PEM - Privacy Enhanced Mail
            - DER - Distinguished Encoding Rule
            - PFX - Personal Information Exchange.
            - Default value = PEM

    passplain:
        description:
            - Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.
            - Minimum length = 1

    expirymonitor:
        choices: ['ENABLED', 'DISABLED']
        description:
            - Issue an alert when the certificate is about to expire.
            
    notificationperiod:
        description:
            - Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.
            - Minimum value = 10
            - Maximum value = 100

    bundle:
        choices: ['YES', 'NO']
        description:
            - Parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file.
            - Default value = NO

    linkcertkeyname:
        description:
            - Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair.
            - Minimum length = 1
'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Connect to netscaler appliance
    netscaler_service_group:
        nsip: "172.17.0.2"
'''

# TODO: Update as module progresses
RETURN = '''
config_updated:
    description: determine if a change in the netscaler configuration happened
    returned: always
    type: boolean
    sample: False
'''

from ansible.module_utils.basic import AnsibleModule
import StringIO


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
        from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
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
            choices=[u'DER', u'PEM', u'PFX']
        ),
        passplain=dict(type='str'),
        expirymonitor=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        notificationperiod=dict(type='float'),
        bundle=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        linkcertkeyname=dict(type='str'),
        nodomaincheck=dict(type='bool'),
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode = True,
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



    # Instantiate Service Config object
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
        'nodomaincheck'
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
    ]

    sslcertkey_proxy = ConfigProxy(
        actual=sslcertkey(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def key_exists():
        log('Entering key_exists')
        log('certkey is %s' % module.params['certkey'])
        all_certificates = sslcertkey.get(client)
        certkeys = [ item.certkey for item in all_certificates ]
        if module.params['certkey'] in certkeys:
            return True
        else:
            return False

    def key_identical():
        log('Entering key_identical')
        sslcertkey_list = sslcertkey.get_filtered(client, 'certkey:%s' % module.params['certkey'])
        diff_dict = sslcertkey_proxy.diff_object(sslcertkey_list[0])
        if 'password' in diff_dict:
            del diff_dict['password']
        if 'passplain' in diff_dict:
            del diff_dict['passplain']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff_list():
        sslcertkey_list = sslcertkey.get_filtered(client, 'certkey:%s' % module.params['certkey'])
        return sslcertkey_proxy.diff_object(sslcertkey_list[0])

    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            log('Applying present operation')
            if not key_exists():
                if not module.check_mode:
                    log('Adding certificate key')
                    sslcertkey_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not key_identical():
                if not module.check_mode:
                    sslcertkey_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False



            # Sanity check for operation
            if not key_exists():
                module.fail_json(msg='Service does not exist')
            if not key_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())

        elif module.params['operation'] == 'absent':
            if key_exists():
                if not module.check_mode:
                    sslcertkey_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if key_exists():
                module.fail_json(msg='Service still exists')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()
