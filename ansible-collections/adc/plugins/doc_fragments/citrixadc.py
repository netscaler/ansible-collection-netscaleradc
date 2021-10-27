from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = '''

options:
    nsip:
        description:
            - The ip address of the Citrix ADC appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. 192.168.1.1:555."
        aliases:
            - mas_ip
        required: True
        type: str

    nitro_user:
        description:
            - The username with which to authenticate to the Citrix ADC node.
        required: False
        aliases:
            - mas_user
        type: str

    nitro_pass:
        description:
            - The password with which to authenticate to the Citrix ADC node.
        required: False
        aliases:
            - mas_pass
        type: str

    nitro_protocol:
        choices: [ 'http', 'https' ]
        default: https
        description:
            - Which protocol to use when accessing the nitro API objects.
        type: str

    validate_certs:
        description:
            - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        required: false
        default: 'yes'
        type: bool

    nitro_timeout:
        description:
            - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC
        default: 310
        type: float

    state:
        choices: ['present', 'absent']
        default: 'present'
        description:
            - The state of the resource being configured by the module on the Citrix ADC node.
            - When present the resource will be created if needed and configured according to the module's parameters.
            - When absent the resource will be deleted from the Citrix ADC node.
        type: str

    save_config:
        description:
            - If true the module will save the configuration on the Citrix ADC node if it makes any changes.
            - The module will not save the configuration on the Citrix ADC node if it made no changes.
        type: bool
        default: true

    mas_proxy_call:
        description:
            - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.
            - "When true you must also define the following options: I(nitro_auth_token)"
            - "When true and adm service is the api proxy the following option must also be defined: I(bearer_token)"
            - "When true you must define a target ADC by defining any of the following parameters"
            - "I(instance_ip)"
            - "I(instance_id)"
            - "I(instance_name)"
        type: bool
        default: false
        version_added: "2.6.0"

    nitro_auth_token:
        description:
            - The authentication token provided by a login operation.
        aliases:
            - mas_auth_token
        version_added: "2.6.0"
        type: str

    instance_ip:
        description:
            - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.
            - It is meaningful only when having set C(mas_proxy_call) to C(true)
        version_added: "2.6.0"
        type: str

    instance_name:
        type: str
        description:
            - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.

    instance_id:
        type: str
        description:
            - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.

    is_cloud:
        type: bool
        default: false
        description:
            - When performing a Proxy API call with ADM service set this to C(true)

    api_path:
        type: str
        description:
            - Base NITRO API path.
            - Define only in case of an ADM service proxy call

    bearer_token:
        type: str
        description:
            - Authentication bearer token.
            - Needed when doing an ADM service proxy call.

notes:
  - For more information on using Ansible to manage Citrix ADC Network devices see U(https://www.ansible.com/ansible-netscaler).
'''
