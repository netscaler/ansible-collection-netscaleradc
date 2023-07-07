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

    nitro_auth_token:
        description:
            - The authentication token provided by a login operation.
        version_added: "2.6.0"
        type: str

    api_path:
        type: str
        description:
            - Base NITRO API path.
            - Define only in case of an ADM service proxy call

notes:
  - For more information on using Ansible to manage NetScaler ADC Network devices see U(https://www.ansible.com/integrations/networks/citrixadc).
'''
