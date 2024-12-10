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
---
module: lbprofile
short_description: Configuration for LB profile resource.
description: Configuration for LB profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  computedadccookieattribute:
    type: str
    description:
      - 'ComputedADCCookieAttribute accepts ns variable as input in form of string
        starting with $ (to understand how to configure ns variable, please check
        man add ns variable). policies can be configured to modify this variable for
        every transaction and the final value of the variable after policy evaluation
        will be appended as attribute to Citrix ADC cookie (for example: LB cookie
        persistence , GSLB sitepersistence, CS cookie persistence, LB group cookie
        persistence). Only one of ComputedADCCookieAttribute, LiteralADCCookieAttribute
        can be set.'
      - ''
      - Sample usage -
      - '             add ns variable lbvar -type TEXT(100) -scope Transaction'
      - '             add ns assignment lbassign -variable $lbvar -set "\\";SameSite=Strict\\""'
      - '             add rewrite policy lbpol <valid policy expression> lbassign'
      - '             bind rewrite global lbpol 100 next -type RES_OVERRIDE'
      - '             add lb profile lbprof -ComputedADCCookieAttribute "$lbvar"'
      - '             For incoming client request, if above policy evaluates TRUE,
        then SameSite=Strict will be appended to ADC generated cookie'
  cookiepassphrase:
    type: str
    description:
      - Use this parameter to specify the passphrase used to generate secured persistence
        cookie value. It specifies the passphrase with a maximum of 31 characters.
  dbslb:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable database specific load balancing for MySQL and MSSQL service types.
  httponlycookieflag:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute
        limits the scope of a cookie to HTTP requests and helps mitigate the risk
        of cross-site scripting attacks.
  lbhashalgorithm:
    type: str
    choices:
      - DEFAULT
      - PRAC
      - JARH
    description:
      - This option dictates the hashing algorithm used for hash based LB methods
        (URLHASH, DOMAINHASH, SOURCEIPHASH, DESTINATIONIPHASH, SRCIPDESTIPHASH, SRCIPSRCPORTHASH,
        TOKEN, USER_TOKEN, CALLIDHASH).
  lbhashfingers:
    type: float
    description:
      - This option is used to specify the number of fingers to be used in PRAC and
        JARH algorithms for hash based LB methods. Increasing the number of fingers
        might give better distribution of traffic at the expense of additional memory.
  lbprofilename:
    type: str
    description:
      - Name of the LB profile.
  literaladccookieattribute:
    type: str
    description:
      - 'String configured as LiteralADCCookieAttribute will be appended as attribute
        for Citrix ADC cookie (for example: LB cookie persistence , GSLB site persistence,
        CS cookie persistence, LB group cookie persistence).'
      - ''
      - Sample usage -
      - '             add lb profile lbprof -LiteralADCCookieAttribute ";SameSite=None"'
  processlocal:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option packets destined to a vserver in a cluster will
        not under go any steering. Turn this option for single pa
      - cket request response mode or when the upstream device is performing a proper
        RSS for connection based distribution.
  proximityfromself:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use the ADC location instead of client IP for static proximity LB or GSLB
        decision.
  storemqttclientidandusername:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option allows to store the MQTT clientid and username in transactional
        logs
  useencryptedpersistencecookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Encode persistence cookie values using SHA2 hash.
  usesecuredpersistencecookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Encode persistence cookie values using SHA2 hash.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lbprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lbprofile
      delegate_to: localhost
      netscaler.adc.lbprofile:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
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
