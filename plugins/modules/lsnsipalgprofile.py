#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
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
  datasessionidletimeout:
    description:
      - Idle timeout for the data channel sessions in seconds.
    type: float
    default: 120
  opencontactpinhole:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE ContactPinhole creation.
    type: str
    default: ENABLED
  openrecordroutepinhole:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RecordRoutePinhole creation.
    type: str
    default: ENABLED
  openregisterpinhole:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RegisterPinhole creation.
    type: str
    default: ENABLED
  openroutepinhole:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE RoutePinhole creation.
    type: str
    default: ENABLED
  openviapinhole:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE ViaPinhole creation.
    type: str
    default: ENABLED
  registrationtimeout:
    description:
      - SIP registration timeout in seconds.
    type: float
    default: 60
  rport:
    choices:
      - ENABLED
      - DISABLED
    description:
      - ENABLE/DISABLE rport.
    type: str
    default: ENABLED
  sipalgprofilename:
    description:
      - The name of the SIPALG Profile.
    type: str
  sipdstportrange:
    description:
      - Destination port range for SIP_UDP and SIP_TCP.
    type: str
  sipsessiontimeout:
    description:
      - SIP control channel session timeout in seconds.
    type: float
    default: 600
  sipsrcportrange:
    description:
      - Source port range for SIP_UDP and SIP_TCP.
    type: str
  siptransportprotocol:
    choices:
      - TCP
      - UDP
    description:
      - SIP ALG Profile transport protocol type.
    type: str
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
