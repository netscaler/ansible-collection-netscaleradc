#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
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
module: tmtrafficaction
short_description: Configuration for TM traffic action resource.
description: Configuration for TM traffic action resource.
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  apptimeout:
    type: float
    description:
      - Time interval, in minutes, of user inactivity after which the connection is
        closed.
  forcedtimeout:
    type: str
    choices:
      - START
      - STOP
      - RESET
    description:
      - Setting to start, stop or reset TM session force timer
  forcedtimeoutval:
    type: float
    description:
      - Time interval, in minutes, for which force timer should be set.
  formssoaction:
    type: str
    description:
      - Name of the configured form-based single sign-on profile.
  initiatelogout:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Initiate logout for the traffic management (TM) session if the policy evaluates
        to true. The session is then terminated after two minutes.
  kcdaccount:
    type: str
    description:
      - Kerberos constrained delegation account name
  name:
    type: str
    description:
      - Name for the traffic action. Must begin with an ASCII alphanumeric or underscore
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
  persistentcookie:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use persistent cookies for the traffic session. A persistent cookie remains
        on the user device and is sent with each HTTP request. The cookie becomes
        stale if the session ends.
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
      - Use single sign-on for the resource that the user is accessing now.
  userexpression:
    type: str
    description:
      - expression that will be evaluated to obtain username for SingleSignOn
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample tmtrafficaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure tmtrafficaction
      delegate_to: localhost
      netscaler.adc.tmtrafficaction:
        state: present
        name: kcd_sso1
        sso: 'ON'
        userexpression: AAA.USER.NAME
        passwdexpression: AAA.USER.PASSWD
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
