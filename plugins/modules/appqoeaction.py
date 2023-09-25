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
module: appqoeaction
short_description: Configuration for AppQoS action resource.
description: Configuration for AppQoS action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  altcontentpath:
    description:
      - Path to the alternative content service to be used in the ACS
    type: str
  altcontentsvcname:
    description:
      - Name of the alternative content service to be used in the ACS
    type: str
  customfile:
    description:
      - name of the HTML page object to use as the response
    type: str
  delay:
    description:
      - Delay threshold, in microseconds, for requests that match the policy's rule.
        If the delay statistics gathered for the matching request exceed the specified
        delay, configured action triggered for that request, if there is no action
        then requests are dropped to the lowest priority level
    type: float
  dosaction:
    choices:
      - SimpleResponse
      - HICResponse
    description:
      - DoS Action to take when vserver will be considered under DoS attack and corresponding
        rule matches. Mandatory if AppQoE actions are to be used for DoS attack prevention.
    type: str
  dostrigexpression:
    description:
      - Optional expression to add second level check to trigger DoS actions. Specifically
        used for Analytics based DoS response generation
    type: str
  maxconn:
    description:
      - Maximum number of concurrent connections that can be open for requests that
        matches with rule.
    type: float
  name:
    description:
      - Name for the AppQoE action. Must begin with a letter, number, or the underscore
        symbol (_). Other characters allowed, after the first character, are the hyphen
        (-), period (.) hash (#), space ( ), at (@), equals (=), and colon (:) characters.
        This is a mandatory argument
    type: str
  numretries:
    description:
      - Retry count
    type: float
    default: 3
  polqdepth:
    description:
      - Policy queue depth threshold value. When the policy queue size (number of
        requests queued for the policy binding this action is attached to) increases
        to the specified polqDepth value, subsequent requests are dropped to the lowest
        priority level.
    type: float
  priority:
    choices:
      - HIGH
      - MEDIUM
      - LOW
      - LOWEST
    description:
      - Priority for queuing the request. If server resources are not available for
        a request that matches the configured rule, this option specifies a priority
        for queuing the request until the server resources are available again. If
        priority is not configured then Lowest priority will be used to queue the
        request.
    type: str
  priqdepth:
    description:
      - Queue depth threshold value per priorirty level. If the queue size (number
        of requests in the queue of that particular priorirty) on the virtual server
        to which this policy is bound, increases to the specified qDepth value, subsequent
        requests are dropped to the lowest priority level.
    type: float
  respondwith:
    choices:
      - ACS
      - NS
    description:
      - 'Responder action to be taken when the threshold is reached. Available settings
        function as follows:'
      - '            C(ACS) - Serve content from an alternative content service'
      - '                  Threshold : maxConn or delay'
      - '            C(NS) - Serve from the Citrix ADC (built-in response)'
      - '                 Threshold : maxConn or delay'
    type: str
  retryonreset:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Retry on TCP Reset
    type: str
    default: 'NO'
  retryontimeout:
    description:
      - Retry on request Timeout(in millisec) upon sending request to backend servers
    type: float
  tcpprofile:
    description:
      - Bind TCP Profile based on L2/L3/L7 parameters.
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
