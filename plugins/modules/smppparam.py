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
module: smppparam
short_description: Configuration for SMPP configuration parameters resource.
description: Configuration for SMPP configuration parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
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
  addrnpi:
    type: int
    description:
      - Numbering Plan Indicator, such as landline, data, or WAP client, used in the
        ESME address sent in the bind request.
  addrrange:
    type: str
    description:
      - Set of SME addresses, sent in the bind request, serviced by the ESME.
  addrton:
    type: int
    description:
      - Type of Number, such as an international number or a national number, used
        in the ESME address sent in the bind request.
  clientmode:
    type: str
    choices:
      - TRANSCEIVER
      - TRANSMITTERONLY
      - RECEIVERONLY
    description:
      - 'Mode in which the client binds to the ADC. Applicable settings function as
        follows:'
      - '* C(TRANSCEIVER) - Client can send and receive messages to and from the message
        center.'
      - '* C(TRANSMITTERONLY) - Client can only send messages.'
      - '* C(RECEIVERONLY) - Client can only receive messages.'
  msgqueue:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Queue SMPP messages if a client that is capable of receiving the destination
        address messages is not available.
  msgqueuesize:
    type: int
    description:
      - Maximum number of SMPP messages that can be queued. After the limit is reached,
        the Citrix ADC sends a deliver_sm_resp PDU, with an appropriate error message,
        to the message center.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
