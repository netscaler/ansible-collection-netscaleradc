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
module: cachepolicy
short_description: Configuration for Integrated Cache policy resource.
description: Configuration for Integrated Cache policy resource.
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
  action:
    type: str
    choices:
      - CACHE
      - NOCACHE
      - MAY_CACHE
      - MAY_NOCACHE
      - INVAL
    description:
      - Action to apply to content that matches the policy.
      - '* C(CACHE) or C(MAY_CACHE) action - positive cachability policy'
      - '* C(NOCACHE) or C(MAY_NOCACHE) action - negative cachability policy'
      - '* C(INVAL) action - Dynamic Invalidation Policy'
  invalgroups:
    type: list
    description:
      - Content group(s) to be invalidated when the INVAL action is applied. Maximum
        number of content groups that can be specified is 16.
    elements: str
  invalobjects:
    type: list
    description:
      - Content groups(s) in which the objects will be invalidated if the action is
        INVAL.
    elements: str
  newname:
    type: str
    description:
      - New name for the cache policy. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  policyname:
    type: str
    description:
      - Name for the policy. Must begin with an ASCII alphabetic or underscore (_)
        character, and must contain only ASCII alphanumeric, underscore, hash (#),
        period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the policy is created.
  rule:
    type: str
    description:
      - Expression against which the traffic is evaluated.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
  storeingroup:
    type: str
    description:
      - Name of the content group in which to store the object when the final result
        of policy evaluation is CACHE. The content group must exist before being mentioned
        here. Use the "show cache contentgroup" command to view the list of existing
        content groups.
  undefaction:
    type: str
    choices:
      - NOCACHE
      - RESET
    description:
      - Action to be performed when the result of rule evaluation is undefined.
  cachepolicylabel_cachepolicy_binding:
    type: dict
    description: Bindings for cachepolicylabel_cachepolicy_binding resource
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
- name: Sample cachepolicy playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cachepolicy
      delegate_to: localhost
      netscaler.adc.cachepolicy:
        state: present
        policyname: n_XM_CACHE_WO_DEVICEID_10.100.39.132
        rule: HTTP.REQ.HEADER("Host").CONTAINS("callout") && HTTP.REQ.URL.QUERY.CONTAINS("DeviceId").NOT
          && HTTP.REQ.URL.QUERY.CONTAINS("url")
        action: CACHE
        storeingroup: n_XM_WO_DEVICEID_10.100.39.132
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
