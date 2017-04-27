#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_cs_vserver
short_description: Manage cs vserver
description:
    - Manage service group configuration in Netscaler

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True

    certkey:
        
        description:
            
            - Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is created.
            
            - The following requirement applies only to the NetScaler CLI:
            
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
            
            - Input format of the certificate and the private-key files. The three formats supported by the appliance are:
            
            - PEM - Privacy Enhanced Mail
            
            - DER - Distinguished Encoding Rule
            
            - PFX - Personal Information Exchange.
            
            - Default value: PEM
            
            - Possible values = DER, PEM, PFX
            

    passplain:
        
        description:
            
            - Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.
            
            - Minimum length = 1
            

    expirymonitor:
        choices: ['ENABLED', 'DISABLED']
        description:
            
            - Issue an alert when the certificate is about to expire.
            
            - Possible values = ENABLED, DISABLED
            

    notificationperiod:
        
        description:
            
            - Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.
            
            - Minimum value = 10
            
            - Maximum value = 100
            

    bundle:
        choices: ['YES', 'NO']
        description:
            
            - Parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file.
            
            - Default value: NO
            
            - Possible values = YES, NO
            

    linkcertkeyname:
        
        description:
            
            - Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair.
            
            - Minimum length = 1
            

    nodomaincheck:
        
        description:
            
            - Override the check for matching domain names during a certificate update operation.
            

    signaturealg:
        
        description:
            
            - Signature algorithm.
            

    serial:
        
        description:
            
            - Serial number.
            

    issuer:
        
        description:
            
            - Issuer name.
            

    clientcertnotbefore:
        
        description:
            
            - Not-Before date.
            

    clientcertnotafter:
        
        description:
            
            - Not-After date.
            

    daystoexpiration:
        
        description:
            
            - Days remaining for the certificate to expire.
            

    subject:
        
        description:
            
            - Subject name.
            

    publickey:
        
        description:
            
            - Public key algorithm.
            

    publickeysize:
        
        description:
            
            - Size of the public key.
            

    version:
        
        description:
            
            - Version.
            

    priority:
        
        description:
            
            - ocsp priority.
            

    status:
        choices: ['Valid', 'Not yet valid', 'Expired']
        description:
            
            - Status of the certificate.
            
            - Possible values = Valid, Not yet valid, Expired
            

    passcrypt:
        
        description:
            
            - Passcrypt.
            
            - Minimum length = 1
            

    data:
        
        description:
            
            - Vserver Id.
            

    servicename:
        
        description:
            
            - Service name to which the certificate key pair is bound.
            

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
        from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        
        certkey=dict(
        type='str',
        
        ),
        
        cert=dict(
        type='str',
        
        ),
        
        key=dict(
        type='str',
        
        ),
        
        password=dict(
        type='bool',
        
        ),
        
        fipskey=dict(
        type='str',
        
        ),
        
        hsmkey=dict(
        type='str',
        
        ),
        
        inform=dict(
        type='str',
        choices=[u'DER', u'PEM', u'PFX']
        ),
        
        passplain=dict(
        type='str',
        
        ),
        
        expirymonitor=dict(
        type='str',
        choices=[u'ENABLED', u'DISABLED']
        ),
        
        notificationperiod=dict(
        type='float',
        
        ),
        
        bundle=dict(
        type='str',
        choices=[u'YES', u'NO']
        ),
        
        linkcertkeyname=dict(
        type='str',
        
        ),
        
        nodomaincheck=dict(
        type='bool',
        
        ),
        
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
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()



    # Instantiate Service Config object
    readwrite_attrs = [u'certkey', u'cert', u'key', u'password', u'fipskey', u'hsmkey', u'inform', u'passplain', u'expirymonitor', u'notificationperiod', u'bundle', u'linkcertkeyname', u'nodomaincheck']
    readonly_attrs = [u'signaturealg', u'certificatetype', u'serial', u'issuer', u'clientcertnotbefore', u'clientcertnotafter', u'daystoexpiration', u'subject', u'publickey', u'publickeysize', u'version', u'priority', u'status', u'passcrypt', u'data', u'servicename', u'__count']

    service_proxy = ConfigProxy(
        actual=service(),
        client=client,
        attribute_values_dict = module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def service_exists():
        if service.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def service_identical():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = service_proxy.diff_object(service_list[0])
        if 'ip' in diff_dict:
            del diff_dict['ip']
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff_list():
        service_list = service.get_filtered(client, 'name:%s' % module.params['name'])
        return service_proxy.diff_object(service_list[0])


    try:

        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not service_exists():
                if not module.check_mode:
                    service_proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not service_identical():
                if not module.check_mode:
                    service_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not service_exists():
                module.fail_json(msg='Service does not exist')
            if not service_identical():
                module.fail_json(msg='Service differs from configured', diff=diff_list())

        elif module.params['operation'] == 'absent':
            if service_exists():
                if not module.check_mode:
                    service_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if service_exists():
                module.fail_json(msg='Service still exists')

    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)

if __name__ == "__main__":
    main()