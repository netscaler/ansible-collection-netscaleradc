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
module: icaparameter
short_description: Configuration for Config Parameters for NS ICA resource.
description: Configuration for Config Parameters for NS ICA resource.
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
  dfpersistence:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable DF Persistence
  edtgwinputholdsize:
    type: int
    description:
      - Size (in entries, must be a power of 2) of the per-direction EDT gateway out-of-order
        inputhold ring buffer allocated when gateway-side EDT termination is enabled.
        Non-power-of-2 values fall back to the compile-time default.
  edtgwrtxbufsize:
    type: int
    description:
      - Size (in entries, must be a power of 2) of the per-direction EDT retransmit
        ring buffer allocated when gateway-side EDT termination is enabled. Non-power-of-2
        values fall back to the compile-time default.
  edtgwtermination:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable gateway-side EDT termination. When C(ENABLED), the NetScaler
        gateway terminates the EDT/UDT connection from the peer and originates a new
        EDT connection toward the backend (independent ISNs per leg, gateway-level
        OOO buffering, gateway-originated NAKs, retransmit buffering). When C(DISABLED),
        EDT is forwarded transparently.
  edtholdqpctenabled:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable strict per-channel HoldQ partitioning based on edtHoldqPrimaryPercent.
        When C(DISABLED) (default), lossy packets are dropped only when total queue
        space is at or below the primary reserve. When C(ENABLED), each channel gets
        a strict budget and packets are dropped when their channel partition is full.
  edtholdqprimarypercent:
    type: int
    description:
      - Percentage of EDT DTLS HoldQ reserved for primary (reliable) channel. Lossy
        channel gets the remainder. Default is 50.
  edtlosstolerant:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable EDT Loss Tolerant feature
  edtpmtuddf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable DF enforcement for EDT PMTUD Control Blocks
  edtpmtuddftimeout:
    type: int
    description:
      - DF enforcement timeout for EDTPMTUDDF
  edtpmtudrediscovery:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable EDT PMTUD Rediscovery
  enablesronhafailover:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable/Disable Session Reliability on HA failover. The default value is No
  hdxinsightnonnsap:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable/Disable HDXInsight for Non NSAP ICA Sessions. The default value is
        Yes
  insightonlytodirector:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable HDX Insight data to Director even if HDX Insight policy is
        not configured on Gateway and Network Telemtry policy is enabled on VDA.
  l7latencyfrequency:
    type: int
    description:
      - Specify the time interval/period for which L7 Client Latency value is to be
        calculated. By default, L7 Client Latency is calculated for every packet.
        The default value is 0
  supporticawithsesstimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable ICA launch support with client detection when ICA session
        timeout or Smartcontrol is enabled. It is C(DISABLED) by default.
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
