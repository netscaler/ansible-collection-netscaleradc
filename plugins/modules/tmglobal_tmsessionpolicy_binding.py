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
module: tmglobal_tmsessionpolicy_binding
short_description: Binding Resource definition for describing association between
  tmglobal and tmsessionpolicy resources
description: Binding Resource definition for describing association between tmglobal
  and tmsessionpolicy resources
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
  builtin:
    type: list
    choices:
      - MODIFIABLE
      - DELETABLE
      - IMMUTABLE
      - PARTITION_ALL
    description:
      - Indicates that a variable is a built-in (SYSTEM INTERNAL) type.
    elements: str
  feature:
    type: str
    choices:
      - WL
      - WebLogging
      - SP
      - SurgeProtection
      - LB
      - LoadBalancing
      - CS
      - ContentSwitching
      - CR
      - CacheRedirection
      - SC
      - SureConnect
      - CMP
      - CMPcntl
      - CompressionControl
      - PQ
      - PriorityQueuing
      - HDOSP
      - HttpDoSProtection
      - SSLVPN
      - AAA
      - GSLB
      - GlobalServerLoadBalancing
      - SSL
      - SSLOffload
      - SSLOffloading
      - CF
      - ContentFiltering
      - IC
      - IntegratedCaching
      - OSPF
      - OSPFRouting
      - RIP
      - RIPRouting
      - BGP
      - BGPRouting
      - REWRITE
      - IPv6PT
      - IPv6protocoltranslation
      - AppFw
      - ApplicationFirewall
      - RESPONDER
      - push
      - NSPush
      - NetScalerPush
      - AppFlow
      - CloudBridge
      - ISIS
      - ISISRouting
      - CH
      - CallHome
      - AppQoE
      - ContentAccelerator
      - SYSTEM
      - RISE
      - FEO
      - LSN
      - LargeScaleNAT
      - RDPProxy
      - Rep
      - Reputation
      - URLFiltering
      - VideoOptimization
      - ForwardProxy
      - SSLInterception
      - AdaptiveTCP
      - CQA
      - CI
      - ContentInspection
      - Bot
      - APIGateway
    description:
      - The feature to be checked while applying this config
  gotopriorityexpression:
    type: str
    description:
      - Expression specifying the priority of the next policy which will get evaluated
        if the current policy rule evaluates to TRUE.
  policyname:
    type: str
    description:
      - The name of the policy.
  priority:
    type: float
    description:
      - The priority of the policy.
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
