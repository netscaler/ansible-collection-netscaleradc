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
module: lsngroup_lsntransportprofile_binding
short_description: Binding Resource definition for describing association between
  lsngroup and lsntransportprofile resources
description: Binding Resource definition for describing association between lsngroup
  and lsntransportprofile resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  groupname:
    type: str
    description:
      - 'Name for the LSN group. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the LSN group is created. The following requirement
        applies only to the Citrix ADC CLI: If the name includes one or more spaces,
        enclose the name in double or single quotation marks (for example, "lsn group1"
        or ''lsn group1'').'
  transportprofilename:
    type: str
    description:
      - Name of the LSN transport profile to bind to the specified LSN group. Bind
        a profile for each protocol for which you want to specify settings.
      - ''
      - By default, one LSN transport profile with default settings for TCP, UDP,
        and ICMP protocols is bound to an LSN group during its creation. This profile
        is called a default transport.
      - ''
      - An LSN transport profile that you bind to an LSN group overrides the default
        LSN transport profile for that protocol.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lsngroup_lsntransportprofile_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lsngroup_lsntransportprofile_binding
      delegate_to: localhost
      netscaler.adc.lsngroup_lsntransportprofile_binding:
        state: present
        groupname: group1
        transportprofilename: icmp
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
