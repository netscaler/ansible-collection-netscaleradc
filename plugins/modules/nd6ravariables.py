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
module: nd6ravariables
short_description: Configuration for nd6 Router Advertisment configuration variables
  resource.
description: Configuration for nd6 Router Advertisment configuration variables resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ceaserouteradv:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Cease router advertisements on this vlan.
    type: str
    default: 'NO'
  currhoplimit:
    description:
      - Current Hop limit.
    type: float
    default: 64
  defaultlifetime:
    description:
      - Default life time, in seconds.
    type: int
    default: 1800
  linkmtu:
    description:
      - The Link MTU.
    type: float
  managedaddrconfig:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Value to be placed in the Managed address configuration flag field.
    type: str
    default: 'NO'
  maxrtadvinterval:
    description:
      - Maximum time allowed between unsolicited multicast RAs, in seconds.
    type: float
    default: 600
  minrtadvinterval:
    description:
      - Minimum time interval between RA messages, in seconds.
    type: float
    default: 198
  onlyunicastrtadvresponse:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Send only Unicast Router Advertisements in respond to Router Solicitations.
    type: str
    default: 'NO'
  otheraddrconfig:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Value to be placed in the Other configuration flag field.
    type: str
    default: 'NO'
  reachabletime:
    description:
      - Reachable time, in milliseconds.
    type: float
  retranstime:
    description:
      - Retransmission time, in milliseconds.
    type: float
  sendrouteradv:
    choices:
      - 'YES'
      - 'NO'
    description:
      - whether the router sends periodic RAs and responds to Router Solicitations.
    type: str
    default: 'NO'
  srclinklayeraddroption:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Include source link layer address option in RA messages.
    type: str
    default: 'YES'
  vlan:
    description:
      - The VLAN number.
    type: float
  nd6ravariables_onlinkipv6prefix_binding:
    type: dict
    description: Bindings for nd6ravariables_onlinkipv6prefix_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
