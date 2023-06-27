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
module: vrid
short_description: Configuration for Virtual Router ID resource.
description: Configuration for Virtual Router ID resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  all:
    description:
      - Remove all the configured VMAC addresses from the Citrix ADC.
    type: bool
  id:
    description:
      - Integer that uniquely identifies the VMAC address. The generic VMAC address
        is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with
        a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c,
        where 3c is the hexadecimal representation of 60.
    type: int
  ownernode:
    description:
      - In a cluster setup, assign a cluster node as the owner of this VMAC address
        for IP based VRRP configuration. If no owner is configured, owner node is
        displayed as ALL and one node is dynamically elected as the owner.
    type: int
  preemption:
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'In an active-active mode configuration, make a backup VIP address the master
        if its priority becomes higher than that of a master VIP address bound to
        this VMAC address. '
      - If you disable pre-emption while a backup VIP address is the master, the backup
        VIP address remains master until the original master VIP's priority becomes
        higher than that of the current master.
    type: str
    default: ENABLED
  preemptiondelaytimer:
    description:
      - Preemption delay time, in seconds, in an active-active configuration. If any
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
    choices:
      - ENABLED
      - DISABLED
    description:
      - In an active-active mode configuration, enable the backup VIP address to process
        any traffic instead of dropping it.
    type: str
    default: DISABLED
  trackifnumpriority:
    description:
      - Priority by which the Effective priority will be reduced if any of the tracked
        interfaces goes down in an active-active configuration.
    type: int
  tracking:
    choices:
      - NONE
      - ONE
      - ALL
      - PROGRESSIVE
    description:
      - The effective priority (EP) value, relative to the base priority (BP) value
        in an active-active mode configuration. When EP is set to a value other than
        None, it is EP, not BP, which determines the master VIP address.
      - 'Available settings function as follows:'
      - '* C(NONE) - No tracking. EP = BP'
      - '* C(ALL) -  If the status of all virtual servers is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* C(ONE) - If the status of at least one virtual server is UP, EP = BP. Otherwise,
        EP = 0.'
      - '* C(PROGRESSIVE) - If the status of all virtual servers is UP, EP = BP. If
        the status of all virtual servers is DOWN, EP = 0. Otherwise EP = BP (1 -
        K/N), where N is the total number of virtual servers associated with the VIP
        address and K is the number of virtual servers for which the status is DOWN.'
      - 'Default: C(NONE).'
    type: str
    default: NONE
  vrid6_channel_binding:
    type: dict
    description: Bindings for vrid6_channel_binding resource
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
  vrid6_interface_binding:
    type: dict
    description: Bindings for vrid6_interface_binding resource
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
  vrid6_trackinterface_binding:
    type: dict
    description: Bindings for vrid6_trackinterface_binding resource
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
  vrid_channel_binding:
    type: dict
    description: Bindings for vrid_channel_binding resource
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
  vrid_interface_binding:
    type: dict
    description: Bindings for vrid_interface_binding resource
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
  vrid_trackinterface_binding:
    type: dict
    description: Bindings for vrid_trackinterface_binding resource
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
