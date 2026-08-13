#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: vpntrafficaction
short_description: Configuration for VPN traffic action resource.
description: Configuration for VPN traffic action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  apptimeout:
    type: int
    description:
      - Maximum amount of time, in minutes, a user can stay logged on to the web application.
  formssoaction:
    type: str
    description:
      - Name of the form-based single sign-on profile. Form-based single sign-on allows
        users to log on one time to all protected applications in your network, instead
        of requiring them to log on separately to access each one.
  fta:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Specify file type association, which is a list of file extensions that users
        are allowed to open.
  hdx:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Provide hdx proxy to the ICA traffic
  kcdaccount:
    type: str
    description:
      - Kerberos constrained delegation account name
  name:
    type: str
    description:
      - Name for the traffic action. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after a traffic action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  passwdexpression:
    type: str
    description:
      - expression that will be evaluated to obtain password for SingleSignOn
  proxy:
    type: str
    description:
      - IP address and Port of the proxy server to be used for HTTP access for this
        request.
  qual:
    type: str
    choices:
      - http
      - tcp
    description:
      - Protocol, either HTTP or TCP, to be used with the action.
  samlssoprofile:
    type: str
    description:
      - Profile to be used for doing SAML SSO to remote relying party
  sso:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Provide single sign-on to the web application.
      - "\t    NOTE : Authentication mechanisms like Basic-authentication  require\
        \ the user credentials to be sent in plaintext which is not secure if the\
        \ server is running on HTTP (instead of HTTPS)."
  userexpression:
    type: str
    description:
      - expression that will be evaluated to obtain username for SingleSignOn
  wanscaler:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use the Repeater Plug-in to optimize network traffic.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample vpntrafficaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vpntrafficaction
      delegate_to: localhost
      netscaler.adc.vpntrafficaction:
        state: present
        name: ia_trafact1
        qual: http
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
failed:
  description: Indicates if the module failed or not
  returned: always
  type: bool
  sample: false
loglines:
  description: list of logged messages by the module
  returned: always
  type: list
  sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
