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
module: subscriberparam
short_description: Configuration for Subscriber Params resource.
description: Configuration for Subscriber Params resource.
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
  idleaction:
    type: str
    choices:
      - ccrTerminate
      - delete
      - ccrUpdate
    description:
      - q!Once idleTTL exprires on a subscriber session, Citrix ADC will take an idle
        action on that session. idleAction could be chosen from one of these ==>
      - '1. C(ccrTerminate): (default) send CCR-T to inform PCRF about session termination
        and C(delete) the session.  '
      - '2. C(delete): Just C(delete) the subscriber session without informing PCRF.'
      - '3. C(ccrUpdate): Do not C(delete) the session and instead send a CCR-U to
        PCRF requesting for an updated session. !'
    default: ccrTerminate
  idlettl:
    type: float
    description:
      - 'q!Idle Timeout, in seconds, after which Citrix ADC will take an idleAction
        on a subscriber session (refer to ''idleAction'' arguement in ''set subscriber
        param'' for more details on idleAction). Any data-plane or control plane activity
        updates the idleTimeout on subscriber session. idleAction could be to ''just
        delete the session'' or ''delete and CCR-T'' (if PCRF is configured) or ''do
        not delete but send a CCR-U''. '
      - Zero value disables the idle timeout. !
  interfacetype:
    type: str
    choices:
      - None
      - RadiusOnly
      - RadiusAndGx
      - GxOnly
    description:
      - Subscriber Interface refers to Citrix ADC interaction with control plane protocols,
        RADIUS and GX.
      - 'Types of subscriber interface: NONE, C(RadiusOnly), C(RadiusAndGx), C(GxOnly).'
      - 'NONE: Only static subscribers can be configured.'
      - 'C(RadiusOnly): GX interface is absent. Subscriber information is obtained
        through RADIUS Accounting messages.'
      - 'C(RadiusAndGx): Subscriber ID obtained through RADIUS Accounting is used
        to query PCRF. Subscriber information is obtained from both RADIUS and PCRF.'
      - 'C(GxOnly): RADIUS interface is absent. Subscriber information is queried
        using Subscriber IP or IP+VLAN.'
    default: None
  ipv6prefixlookuplist:
    type: list
    description:
      - The ipv6PrefixLookupList should consist of all the ipv6 prefix lengths assigned
        to the UE's'
    elements: int
  keytype:
    type: str
    choices:
      - IP
      - IPANDVLAN
    description:
      - Type of subscriber key type C(IP) or C(IPANDVLAN). C(IPANDVLAN) option can
        be used only when the interfaceType is set to gxOnly.
      - Changing the lookup method should result to the subscriber session database
        being flushed.
    default: IP
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
