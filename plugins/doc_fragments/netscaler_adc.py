# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

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
        default: true
        type: bool

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
        default: "nitro/v1/config"

notes:
  - For more information on using Ansible to manage NetScaler ADC Network devices see U(https://www.ansible.com/integrations/networks/citrixadc).
'''
