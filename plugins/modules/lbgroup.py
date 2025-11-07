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
module: lbgroup
short_description: Configuration for LB group resource.
description: Configuration for LB group resource.
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
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
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
  backuppersistencetimeout:
    type: int
    description:
      - Time period, in minutes, for which backup persistence is in effect.
  cookiedomain:
    type: str
    description:
      - Domain attribute for the HTTP cookie.
  cookiename:
    type: str
    description:
      - Use this parameter to specify the cookie name for COOKIE peristence type.
        It specifies the name of cookie with a maximum of 32 characters. If not specified,
        cookie name is internally generated.
  mastervserver:
    type: str
    description:
      - When USE_VSERVER_PERSISTENCE is enabled, one can use this setting to designate
        a member vserver as master which is responsible to create the persistence
        sessions
  name:
    type: str
    description:
      - Name of the load balancing virtual server group.
  newname:
    type: str
    description:
      - New name for the load balancing virtual server group.
  persistencebackup:
    type: str
    choices:
      - SOURCEIP
      - NONE
    description:
      - Type of backup persistence for the group.
  persistencetype:
    type: str
    choices:
      - SOURCEIP
      - COOKIEINSERT
      - RULE
      - NONE
    description:
      - 'Type of persistence for the group. Available settings function as follows:'
      - '* C(SOURCEIP) - Create persistence sessions based on the client IP.'
      - '* C(COOKIEINSERT) - Create persistence sessions based on a cookie in client
        requests. The cookie is inserted by a Set-Cookie directive from the server,
        in its first response to a client.'
      - '* C(RULE) - Create persistence sessions based on a user defined rule.'
      - '* C(NONE) - Disable persistence for the group.'
  persistmask:
    type: str
    description:
      - Persistence mask to apply to source IPv4 addresses when creating source IP
        based persistence sessions.
  rule:
    type: str
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - ''
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
  timeout:
    type: int
    description:
      - Time period for which a persistence session is in effect.
  usevserverpersistency:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use this parameter to enable vserver level persistence on group members. This
        allows member vservers to have their own persistence, but need to be compatible
        with other members persistence rules. When this setting is enabled persistence
        sessions created by any of the members can be shared by other member vservers.
  v6persistmasklen:
    type: int
    description:
      - Persistence mask to apply to source IPv6 addresses when creating source IP
        based persistence sessions.
  lbgroup_lbvserver_binding:
    type: dict
    description: Bindings for lbgroup_lbvserver_binding resource
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
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lbgroup playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lbgroup
      delegate_to: localhost
      netscaler.adc.lbgroup:
        state: present
        name: webgrp
        persistencetype: COOKIEINSERT
        persistencebackup: SOURCEIP
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
