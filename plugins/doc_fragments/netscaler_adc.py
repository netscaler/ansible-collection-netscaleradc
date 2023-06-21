from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = '''

options:
    nsip:
        description:
            - The ip address of the NetScaler ADC appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. 192.168.1.1:555."
        required: True
        type: str

    nitro_user:
        description:
            - The username with which to authenticate to the NetScaler ADC node.
        required: False
        type: str

    nitro_pass:
        description:
            - The password with which to authenticate to the NetScaler ADC node.
        required: False
        type: str

    nitro_protocol:
        choices: [ 'http', 'https' ]
        default: https
        description:
            - Which protocol to use when accessing the nitro API objects.
        type: str

    validate_certs:
        description:
            - If C(false), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        required: false
        default: false
        type: bool

    nitro_timeout:
        description:
            - Time in seconds until a timeout error is thrown when establishing a new session with NetScaler ADC
        default: 310
        type: float

    state:
        choices: ['present', 'absent', 'enabled', 'disabled']
        default: 'present'
        description:
            - The state of the resource being configured by the module on the NetScaler ADC node.
            - C(enabled) and C(disabled) are only valid for resources that can be enabled or disabled.
            - When C(present) the resource will be created if needed and configured according to the module's parameters.
            - When C(absent) the resource will be deleted from the NetScaler ADC node.
            - When C(enabled) the resource will be enabled on the NetScaler ADC node.
            - When C(disabled) the resource will be disabled on the NetScaler ADC node.
        type: str

    save_config:
        description:
            - If C(true) the module will save the configuration on the NetScaler ADC node if it makes any changes.
            - The module will not save the configuration on the NetScaler ADC node if it made no changes.
        type: bool
        default: false

    mas_proxy_call:
        description:
            - If C(true) the underlying NITRO API calls made by the module will be proxied through a NetScaler ADM node to the target NetScaler ADC instance.
            - "When C(true) you must also define the following options: I(nitro_auth_token)"
            - "When C(true) and adm service is the api proxy the following option must also be defined: I(bearer_token)"
            - "When C(true) you must define a target ADC by defining any of the following parameters"
            - "I(instance_ip)"
            - "I(instance_id)"
            - "I(instance_name)"
        type: bool
        default: false
        version_added: "2.6.0"

    nitro_auth_token:
        description:
            - The authentication token provided by a login operation.
        version_added: "2.6.0"
        type: str

    instance_ip:
        description:
            - The target NetScaler ADC instance ip address to which all underlying NITRO API calls will be proxied to.
            - It is meaningful only when having set C(mas_proxy_call) to C(true)
        version_added: "2.6.0"
        type: str

    instance_name:
        type: str
        description:
            - The name of the target NetScaler ADC instance when issuing a Nitro request through a NetScaler ADM proxy.

    instance_id:
        type: str
        description:
            - The id of the target NetScaler ADC instance when issuing a Nitro request through a NetScaler ADM proxy.

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
  - For more information on using Ansible to manage NetScaler ADC Network devices see U(https://www.ansible.com/integrations/networks/citrixadc).
'''
