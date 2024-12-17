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
module: gslbvserver_gslbservice_binding
short_description: Binding Resource definition for describing association between
  gslbvserver and gslbservice resources
description: Binding Resource definition for describing association between gslbvserver
  and gslbservice resources
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
  domainname:
    type: str
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
  name:
    type: str
    description:
      - Name of the virtual server on which to perform the binding operation.
  order:
    type: float
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
  servicename:
    type: str
    description:
      - Name of the GSLB service for which to change the weight.
  weight:
    type: float
    description:
      - Weight for the service.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample gslbvserver_gslbservice_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure gslbvserver_gslbservice_binding
      delegate_to: localhost
      netscaler.adc.gslbvserver_gslbservice_binding:

        state: present
        name: backup_gslb_portal.bx.com
        servicename: GSLB_SVC_USE2_portal.bx.com
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
