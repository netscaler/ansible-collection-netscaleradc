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
module: lbprofile
short_description: Configuration for LB profile resource.
description: Configuration for LB profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  computedadccookieattribute:
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
    type: str
  cookiepassphrase:
    description:
      - Use this parameter to specify the passphrase used to generate secured persistence
        cookie value. It specifies the passphrase with a maximum of 31 characters.
    type: str
  dbslb:
    description:
      - Enable database specific load balancing for MySQL and MSSQL service types.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  httponlycookieflag:
    description:
      - Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute
        limits the scope of a cookie to HTTP requests and helps mitigate the risk
        of cross-site scripting attacks.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  lbhashalgorithm:
    description:
      - This option dictates the hashing algorithm used for hash based LB methods
        (URLHASH, DOMAINHASH, SOURCEIPHASH, DESTINATIONIPHASH, SRCIPDESTIPHASH, SRCIPSRCPORTHASH,
        TOKEN, USER_TOKEN, CALLIDHASH).
    type: str
    default: DEFAULT
    choices:
      - DEFAULT
      - PRAC
      - JARH
  lbhashfingers:
    description:
      - This option is used to specify the number of fingers to be used in PRAC and
        JARH algorithms for hash based LB methods. Increasing the number of fingers
        might give better distribution of traffic at the expense of additional memory.
    type: int
    default: 256
  lbprofilename:
    description:
      - Name of the LB profile.
    type: str
  literaladccookieattribute:
    description:
      - 'String configured as LiteralADCCookieAttribute will be appended as attribute
        for Citrix ADC cookie (for example: LB cookie persistence , GSLB site persistence,
        CS cookie persistence, LB group cookie persistence).'
      - ''
      - Sample usage -
      - '             add lb profile lbprof -LiteralADCCookieAttribute ";SameSite=None"'
    type: str
  processlocal:
    description:
      - By turning on this option packets destined to a vserver in a cluster will
        not under go any steering. Turn this option for single pa
      - cket request response mode or when the upstream device is performing a proper
        RSS for connection based distribution.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  storemqttclientidandusername:
    description:
      - This option allows to store the MQTT clientid and username in transactional
        logs
    type: str
    choices:
      - true
      - false
  useencryptedpersistencecookie:
    description:
      - Encode persistence cookie values using SHA2 hash.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  usesecuredpersistencecookie:
    description:
      - Encode persistence cookie values using SHA2 hash.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
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