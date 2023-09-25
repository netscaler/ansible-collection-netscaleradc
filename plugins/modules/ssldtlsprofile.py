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
module: ssldtlsprofile
short_description: Configuration for DTLS profile resource.
description: Configuration for DTLS profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  helloverifyrequest:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send a Hello Verify request to validate the client.
    type: str
    default: ENABLED
  maxbadmacignorecount:
    description:
      - Maximum number of bad MAC errors to ignore for a connection prior disconnect.
        Disabling parameter terminateSession terminates session immediately when bad
        MAC is detected in the connection.
    type: float
    default: 100
  maxholdqlen:
    description:
      - Maximum number of datagrams that can be queued at DTLS layer for processing
    type: float
    default: 32
  maxpacketsize:
    description:
      - Maximum number of packets to reassemble. This value helps protect against
        a fragmented packet attack.
    type: float
    default: 120
  maxrecordsize:
    description:
      - Maximum size of records that can be sent if PMTU is disabled.
    type: float
    default: 1459
  maxretrytime:
    description:
      - Wait for the specified time, in seconds, before resending the request.
    type: float
    default: 3
  name:
    description:
      - Name for the DTLS profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-)
        characters. Cannot be changed after the profile is created.
    type: str
  pmtudiscovery:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Source for the maximum record size value. If C(ENABLED), the value is taken
        from the PMTU table. If C(DISABLED), the value is taken from the profile.
    type: str
    default: DISABLED
  terminatesession:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Terminate the session if the message authentication code (MAC) of the client
        and server do not match.
    type: str
    default: DISABLED
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
