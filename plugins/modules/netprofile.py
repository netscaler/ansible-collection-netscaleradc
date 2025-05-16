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
module: netprofile
short_description: Configuration for Network profile resource.
description: Configuration for Network profile resource.
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
  mbf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Response will be sent using learnt info if enabled. When creating a netprofile,
        if you do not set this parameter, the netprofile inherits the global MBF setting
        (available in the enable ns mode and disable ns mode CLI commands, or in the
        System > Settings > Configure modes > Configure Modes dialog box). However,
        you can override this setting after you create the netprofile
  name:
    type: str
    description:
      - Name for the net profile. Must begin with a letter, number, or the underscore
        character (_), and can consist of letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the profile is created. Choose a name
        that helps identify the net profile.
  overridelsn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - USNIP/USIP settings override LSN settings for configured
      - '              service/virtual server traffic..'
  proxyprotocol:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Proxy Protocol Action (Enabled/Disabled)
  proxyprotocolaftertlshandshake:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ADC doesnt look for proxy header before TLS handshake, if enabled. Proxy protocol
        parsed after TLS handshake
  proxyprotocoltxversion:
    type: str
    choices:
      - V1
      - V2
    description:
      - Proxy Protocol Version (C(V1)/C(V2))
  srcip:
    type: str
    description:
      - IP address or the name of an IP set.
  srcippersistency:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When the net profile is associated with a virtual server or its bound services,
        this option enables the Citrix ADC to use the same  address, specified in
        the net profile, to communicate to servers for all sessions initiated from
        a particular client to the virtual server.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  netprofile_natrule_binding:
    type: dict
    description: Bindings for netprofile_natrule_binding resource
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
  netprofile_srcportset_binding:
    type: dict
    description: Bindings for netprofile_srcportset_binding resource
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
- name: Sample netprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure netprofile
      delegate_to: localhost
      netscaler.adc.netprofile:
        state: present
        name: net_test_profile2
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
