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
module: lsnappsattributes
short_description: Configuration for LSN Application Attributes resource.
description: Configuration for LSN Application Attributes resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  name:
    type: str
    description:
      - 'Name for the LSN Application Port ATTRIBUTES. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the LSN application profile is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "lsn application profile1" or ''lsn application profile1'').'
  port:
    type: str
    description:
      - This is used for Displaying Port/Port range in CLI/Nitro.Lowport, Highport
        values are populated and used for displaying.Port numbers or range of port
        numbers to match against the destination port of the incoming packet from
        a subscriber. When the destination port is matched, the LSN application profile
        is applied for the LSN session. Separate a range of ports with a hyphen. For
        example, 40-90.
  sessiontimeout:
    type: float
    description:
      - Timeout, in seconds, for an idle LSN session. If an LSN session is idle for
        a time that exceeds this value, the Citrix ADC removes the session.This timeout
        does not apply for a TCP LSN session when a FIN or RST message is received
        from either of the endpoints.
  transportprotocol:
    type: str
    choices:
      - TCP
      - UDP
      - ICMP
    description:
      - Name of the protocol(C(TCP),C(UDP)) for which the parameters of this LSN application
        port ATTRIBUTES applies
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
