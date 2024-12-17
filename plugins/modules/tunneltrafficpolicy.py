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
module: tunneltrafficpolicy
short_description: Configuration for tunnel policy resource.
description: Configuration for tunnel policy resource.
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
  action:
    type: str
    description:
      - Name of the built-in compression action to associate with the policy.
  comment:
    type: str
    description:
      - Any comments to preserve information about this policy.
  logaction:
    type: str
    description:
      - Name of the messagelog action to use for requests that match this policy.
  name:
    type: str
    description:
      - Name for the tunnel traffic policy.
      - Must begin with an ASCII alphanumeric or underscore (_) character, and must
        contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed
        after the policy is created.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policy" or 'my policy)'.
  newname:
    type: str
    description:
      - New name for the tunnel traffic policy. Must begin with an ASCII alphabetic
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), e
      - quals (=), and hyphen (-) characters.
      - Choose a name that reflects the function that the policy performs.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my tunnel policy" or 'my tunnel policy').
  rule:
    type: str
    description:
      - Expression, against which traffic is evaluated.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '*  If the expression includes blank spaces, the entire expression must be
        enclosed in double quotation marks.'
      - '*  If the expression itself includes double quotation marks, you must escape
        the quotations by using the \ character. '
      - '*  Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample tunneltrafficpolicy playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure tunneltrafficpolicy
      delegate_to: localhost
      netscaler.adc.tunneltrafficpolicy:

        state: present
        name: compress
        rule: url == /*.asp
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
