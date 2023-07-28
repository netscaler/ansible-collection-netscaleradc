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
module: vpnglobal_vpnclientlessaccesspolicy_binding
short_description: Binding Resource definition for describing association between
  vpnglobal and vpnclientlessaccesspolicy resources
description: Binding Resource definition for describing association between vpnglobal
  and vpnclientlessaccesspolicy resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
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
  globalbindtype:
    choices:
      - SYSTEM_GLOBAL
      - VPN_GLOBAL
      - RNAT_GLOBAL
      - APPFW_GLOBAL
    description:
      - '0'
    type: str
  gotopriorityexpression:
    description:
      - Applicable only to advance vpn session policy. An expression or other value
        specifying the priority of the next policy which will get evaluated if the
        current policy rule evaluates to TRUE.
    type: str
  groupextraction:
    description:
      - Bind the Authentication policy to a tertiary chain which will be used only
        for group extraction.  The user will not authenticate against this server,
        and this will only be called it primary and/or secondary authentication has
        succeeded.
    type: bool
  policyname:
    description:
      - The name of the policy.
    type: str
  priority:
    description:
      - Integer specifying the policy's priority. The lower the priority number, the
        higher the policy's priority. Maximum value for default syntax policies is
        2147483647 and for classic policies is 64000.
    type: int
  secondary:
    description:
      - Bind the authentication policy as the secondary policy to use in a two-factor
        configuration. A user must then authenticate not only to a primary authentication
        server but also to a secondary authentication server. User groups are aggregated
        across both authentication servers. The user name must be exactly the same
        on both authentication servers, but the authentication servers can require
        different passwords.
    type: bool
  type:
    choices:
      - REQ_OVERRIDE
      - REQ_DEFAULT
      - RES_OVERRIDE
      - RES_DEFAULT
    description:
      - Bindpoint to which the policy is bound
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
