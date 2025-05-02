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
module: systemuser
short_description: Configuration for system user resource.
description: Configuration for system user resource.
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
  allowedmanagementinterface:
    type: list
    choices:
      - CLI
      - API
    description:
      - Allowed Management interfaces to the system user. By default user is allowed
        from both C(API) and C(CLI) interfaces. If management interface for a user
        is set to C(API), then user is not allowed to access NS through C(CLI). GUI
        interface will come under C(API) interface
    elements: str
  externalauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Whether to use external authentication servers for the system user authentication
        or not
  logging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Users logging privilege
  maxsession:
    type: float
    description:
      - Maximum number of client connection allowed per user
  password:
    type: str
    description:
      - Password for the system user. Can include any ASCII character.
  promptstring:
    type: str
    description:
      - 'String to display at the command-line prompt. Can consist of letters, numbers,
        hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:),
        underscore (_), and the following variables:'
      - '* %u - Will be replaced by the user name.'
      - '* %h - Will be replaced by the hostname of the Citrix ADC.'
      - '* %t - Will be replaced by the current time in 12-hour format.'
      - '* %T - Will be replaced by the current time in 24-hour format.'
      - '* %d - Will be replaced by the current date.'
      - '* %s - Will be replaced by the state of the Citrix ADC.'
      - ''
      - 'Note: The 63-character limit for the length of the string does not apply
        to the characters that replace the variables.'
  timeout:
    type: float
    description:
      - CLI session inactivity timeout, in seconds. If Restrictedtimeout argument
        of system parameter is enabled, Timeout can have values in the range [300-86400]
        seconds. If Restrictedtimeout argument of system parameter is disabled, Timeout
        can have values in the range [0, 10-100000000] seconds. Default value is 900
        seconds.
  username:
    type: str
    description:
      - Name for a user. Must begin with a letter, number, or the underscore (_) character,
        and must contain only alphanumeric, hyphen (-), period (.), hash (#), space
        ( ), at (@), equal (=), colon (:), and underscore characters. Cannot be changed
        after the user is added.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my user" or ''my user'').'
  systemuser_nspartition_binding:
    type: dict
    description: Bindings for systemuser_nspartition_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  systemuser_systemcmdpolicy_binding:
    type: dict
    description: Bindings for systemuser_systemcmdpolicy_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample systemuser playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure systemuser
      delegate_to: localhost
      netscaler.adc.systemuser:
        state: present
        username: guest
        password: guest
        promptstring: guest
        timeout: 300
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
