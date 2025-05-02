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
module: responderpolicylabel
short_description: Configuration for responder policy label resource.
description: Configuration for responder policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about this responder policy label.
  labelname:
    type: str
    description:
      - Name for the responder policy label. Must begin with a letter, number, or
        the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters. Cannot be changed after the responder policy
        label is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my responder policy label" or my responder
        policy label').
  newname:
    type: str
    description:
      - New name for the responder policy label. Must begin with a letter, number,
        or the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
  policylabeltype:
    type: str
    choices:
      - HTTP
      - OTHERTCP
      - SIP_UDP
      - SIP_TCP
      - MYSQL
      - MSSQL
      - NAT
      - DIAMETER
      - RADIUS
      - DNS
      - MQTT
      - MQTT_JUMBO
      - QUIC_BRIDGE
      - HTTP_QUIC
    description:
      - 'Type of responses sent by the policies bound to this policy label. Types
        are:'
      - '* C(HTTP) - C(HTTP) responses.'
      - '* C(OTHERTCP) - NON-C(HTTP) TCP responses.'
      - '* C(SIP_UDP) - SIP responses.'
      - '* C(RADIUS) - C(RADIUS) responses.'
      - '* C(MYSQL) - SQL responses in MySQL format.'
      - '* C(MSSQL) - SQL responses in Microsoft SQL format.'
      - '* C(NAT) - C(NAT) response.'
      - '* C(MQTT) - Trigger policies bind with C(MQTT) type.'
      - '* C(MQTT_JUMBO) - Trigger policies bind with C(MQTT) Jumbo type.'
  responderpolicylabel_responderpolicy_binding:
    type: dict
    description: Bindings for responderpolicylabel_responderpolicy_binding resource
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
- name: Sample responderpolicylabel playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure responderpolicylabel
      delegate_to: localhost
      netscaler.adc.responderpolicylabel:
        state: present
        labelname: ia_respolabl5
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
