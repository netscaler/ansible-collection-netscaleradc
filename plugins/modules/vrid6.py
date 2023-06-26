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
module: vrid6
short_description: Configuration for Virtual Router ID for IPv6 resource.
description: Configuration for Virtual Router ID for IPv6 resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  all:
    description:
      - Remove all configured VMAC6 addresses from the Citrix ADC.
    type: bool
  id:
    description:
      - Integer value that uniquely identifies a VMAC6 address.
    type: int
  ownernode:
    description:
      - In a cluster setup, assign a cluster node as the owner of this VMAC address
        for IP based VRRP configuration. If no owner is configured, ow ner node is
        displayed as ALL and one node is dynamically elected as the owner.
    type: int
  preemption:
    description:
      - In an active-active mode configuration, make a backup VIP address the master
        if its priority becomes higher than that of a master VIP address bound to
        this VMAC address.
      - '             If you disable pre-emption while a backup VIP address is the
        master, the backup VIP address remains master until the original master VIP''s
        priority becomes higher than that of the current master.'
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  preemptiondelaytimer:
    description:
      - Preemption delay time in seconds, in an active-active configuration. If any
        high priority node will come in network, it will wait for these many seconds
        before becoming master.
    type: int
  priority:
    description:
      - Base priority (BP), in an active-active mode configuration, which ordinarily
        determines the master VIP address.
    type: int
    default: 255
  sharing:
    description:
      - In an active-active mode configuration, enable the backup VIP address to process
        any traffic instead of dropping it.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  trackifnumpriority:
    description:
      - Priority by which the Effective priority will be reduced if any of the tracked
        interfaces goes down in an active-active configuration.
    type: int
  tracking:
    description:
      - The effective priority (EP) value, relative to the base priority (BP) value
        in an active-active mode configuration. When EP is set to a value other than
        None, it is EP, not BP, which determines the master VIP address.
      - 'Available settings function as follows:'
      - '* NONE - No tracking. EP = BP'
      - '* ALL -  If the status of all virtual servers is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* ONE - If the status of at least one virtual server is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* PROGRESSIVE - If the status of all virtual servers is UP, EP = BP. If the
        status of all virtual servers is DOWN, EP = 0. Otherwise EP = BP (1 - K/N),
        where N is the total number of virtual servers associated with the VIP address
        and K is the number of virtual servers for which the status is DOWN.'
      - 'Default: NONE.'
    type: str
    default: NONE
    choices:
      - NONE
      - ONE
      - ALL
      - PROGRESSIVE
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