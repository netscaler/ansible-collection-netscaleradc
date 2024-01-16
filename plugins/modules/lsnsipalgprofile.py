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
module: lsnsipalgprofile
short_description: Configuration for LSN SIPALG Profile resource.
description: Configuration for LSN SIPALG Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  datasessionidletimeout:
    type: float
    description:
      - Idle timeout for the data channel sessions in seconds.
  opencontactpinhole:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE ContactPinhole creation.
  openrecordroutepinhole:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RecordRoutePinhole creation.
  openregisterpinhole:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RegisterPinhole creation.
  openroutepinhole:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RoutePinhole creation.
  openviapinhole:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE ViaPinhole creation.
  registrationtimeout:
    type: float
    description:
      - SIP registration timeout in seconds.
  rport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE rport.
  sipalgprofilename:
    type: str
    description:
      - The name of the SIPALG Profile.
  sipdstportrange:
    type: str
    description:
      - Destination port range for SIP_UDP and SIP_TCP.
  sipsessiontimeout:
    type: float
    description:
      - SIP control channel session timeout in seconds.
  sipsrcportrange:
    type: str
    description:
      - Source port range for SIP_UDP and SIP_TCP.
  siptransportprotocol:
    type: str
    choices:
      - TCP
      - UDP
    description:
      - SIP ALG Profile transport protocol type.
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
