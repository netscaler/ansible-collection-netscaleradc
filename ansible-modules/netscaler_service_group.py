#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_service_group
short_description: Manage service group configuration in Netscaler
description:
    - Manage service group configuration in Netscaler

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True
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


def main():
    from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_servicegroup_binding import lbvserver_servicegroup_binding
    from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    import netscaler

    module_specific_arguments = dict(
        weight=dict(type='float'),
        name=dict(type='str'),
        servicename=dict(type='str'),
        servicegroupname=dict(type='str'),
    )

    argument_spec = dict()

    argument_spec.update(netscaler.netscaler_common_arguments)

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(argument_spec=argument_spec)

    # do the login stuff
    client = nitro_service(module.params['nsip'], module.params['nitro_protocol'])
    client.set_credential(module.params['nitro_user'], module.params['nitro_pass'])
    client.timeout = float(module.params['nitro_timeout'])
    client.certvalidation = module.params['ssl_cert_validation']
    client.login()

    actual = lbvserver_servicegroup_binding()
    lbvserver_servicegroup_binding_proxy = netscaler.ConfigProxy(actual, client, module_specific_arguments, module)
    try:
        if module.params['state'] == 'enabled':
            lbvserver_servicegroup_binding_proxy.add()
            print('I did it')
        elif module.params['state'] == 'disabled':
            lbvserver_servicegroup_binding_proxy.delete()
            print('I did it')
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg)

    # save and exit
    client.save_config()
    client.logout()

    module.exit_json(failed=False)

if __name__ == "__main__":
    main()
