#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

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
    type: int
    default: 120
  opencontactpinhole:
    description:
      - ENABLE/DISABLE ContactPinhole creation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  openrecordroutepinhole:
    description:
      - ENABLE/DISABLE RecordRoutePinhole creation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  openregisterpinhole:
    description:
      - ENABLE/DISABLE RegisterPinhole creation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  openroutepinhole:
    description:
      - ENABLE/DISABLE RoutePinhole creation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  openviapinhole:
    description:
      - ENABLE/DISABLE ViaPinhole creation.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  registrationtimeout:
    description:
      - SIP registration timeout in seconds.
    type: int
    default: 60
  rport:
    description:
      - ENABLE/DISABLE rport.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
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
    type: int
    default: 600
  sipsrcportrange:
    description:
      - Source port range for SIP_UDP and SIP_TCP.
    type: str
  siptransportprotocol:
    description:
      - SIP ALG Profile transport protocol type.
    type: str
    choices:
      - TCP
      - UDP
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
