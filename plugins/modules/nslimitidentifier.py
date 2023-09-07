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
module: nslimitidentifier
short_description: Configuration for limit Indetifier resource.
description: Configuration for limit Indetifier resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  limitidentifier:
    description:
      - Name for a rate limit identifier. Must begin with an ASCII letter or underscore
        (_) character, and must consist only of ASCII alphanumeric or underscore characters.
        Reserved words must not be used.
    type: str
  limittype:
    choices:
      - BURSTY
      - SMOOTH
    description:
      - Smooth or bursty request type.
      - '* C(SMOOTH) - When you want the permitted number of requests in a given interval
        of time to be spread evenly across the timeslice'
      - '* C(BURSTY) - When you want the permitted number of requests to exhaust the
        quota anytime within the timeslice.'
      - This argument is needed only when the mode is set to REQUEST_RATE.
    type: str
    default: BURSTY
  maxbandwidth:
    description:
      - Maximum bandwidth permitted, in kbps.
    type: float
  mode:
    choices:
      - CONNECTION
      - REQUEST_RATE
      - NONE
    description:
      - Defines the type of traffic to be tracked.
      - '* C(REQUEST_RATE) - Tracks requests/timeslice.'
      - '* C(CONNECTION) - Tracks active transactions.'
      - ''
      - Examples
      - ''
      - '1. To permit 20 requests in 10 ms and 2 traps in 10 ms:'
      - add limitidentifier limit_req -mode request_rate -limitType smooth -timeslice
        1000 -Threshold 2000 -trapsInTimeSlice 200
      - ''
      - '2. To permit 50 requests in 10 ms:'
      - set  limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold
        5000 -limitType smooth
      - ''
      - '3. To permit 1 request in 40 ms:'
      - set limitidentifier limit_req -mode request_rate -timeslice 2000 -Threshold
        50 -limitType smooth
      - ''
      - '4. To permit 1 request in 200 ms and 1 trap in 130 ms:'
      - set limitidentifier limit_req -mode request_rate -timeslice 1000 -Threshold
        5 -limitType smooth -trapsInTimeSlice 8
      - ''
      - '5. To permit 5000 requests in 1000 ms and 200 traps in 1000 ms:'
      - set limitidentifier limit_req  -mode request_rate -timeslice 1000 -Threshold
        5000 -limitType BURSTY
    type: str
    default: REQUEST_RATE
  selectorname:
    description:
      - Name of the rate limit selector. If this argument is NULL, rate limiting will
        be applied on all traffic received by the virtual server or the Citrix ADC
        (depending on whether the limit identifier is bound to a virtual server or
        globally) without any filtering.
    type: str
  threshold:
    description:
      - Maximum number of requests that are allowed in the given timeslice when requests
        (mode is set as REQUEST_RATE) are tracked per timeslice.
      - When connections (mode is set as CONNECTION) are tracked, it is the total
        number of connections that would be let through.
    type: float
    default: 1
  timeslice:
    description:
      - Time interval, in milliseconds, specified in multiples of 10, during which
        requests are tracked to check if they cross the threshold. This argument is
        needed only when the mode is set to REQUEST_RATE.
    type: float
    default: 1000
  trapsintimeslice:
    description:
      - Number of traps to be sent in the timeslice configured. A value of 0 indicates
        that traps are disabled.
    type: float
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
