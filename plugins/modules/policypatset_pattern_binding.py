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
module: policypatset_pattern_binding
short_description: Binding Resource definition for describing association between
  policypatset and pattern resources
description: Binding Resource definition for describing association between policypatset
  and pattern resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  String:
    description:
      - String of characters that constitutes a pattern. For more information about
        the characters that can be used, refer to the character set parameter.
      - 'Note: Minimum length for pattern sets used in rewrite actions of type REPLACE_ALL,
        DELETE_ALL, INSERT_AFTER_ALL, and INSERT_BEFORE_ALL, is three characters.'
    type: str
  builtin:
    choices:
      - MODIFIABLE
      - DELETABLE
      - IMMUTABLE
      - PARTITION_ALL
    description:
      - Indicates that a variable is a built-in (SYSTEM INTERNAL) type.
    type: list
    elements: str
  charset:
    choices:
      - ASCII
      - UTF_8
    description:
      - Character set associated with the characters in the string.
      - 'Note: UTF-8 characters can be entered directly (if the UI supports it) or
        can be encoded as a sequence of hexadecimal bytes ''\xNN''. For example, the
        UTF-8 character '''' can be encoded as ''\xC3\xBC''.'
    type: str
  comment:
    description:
      - Any comments to preserve information about this patset or a pattern bound
        to this patset.
    type: str
  feature:
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
    type: str
  index:
    description:
      - The index of the string associated with the patset.
    type: int
  name:
    description:
      - Name of the pattern set to which to bind the string.
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
