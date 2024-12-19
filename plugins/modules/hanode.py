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
module: hanode
short_description: Configuration for node resource.
description: Configuration for node resource.
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
  deadinterval:
    type: float
    description:
      - Number of seconds after which a peer node is marked DOWN if heartbeat messages
        are not received from the peer node.
  failsafe:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Keep one node primary if both nodes fail the health check, so that a partially
        available node can back up data and handle traffic. This mode is set independently
        on each node.
  haprop:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Automatically propagate all commands from the primary to the secondary node,
        except the following:'
      - '* All HA configuration related commands. For example, add ha node, set ha
        node, and bind ha node.'
      - '* All Interface related commands. For example, set interface and unset interface.'
      - '* All channels related commands. For example, add channel, set channel, and
        bind channel.'
      - The propagated command is executed on the secondary node before it is executed
        on the primary. If command propagation fails, or if command execution fails
        on the secondary, the primary node executes the command and logs an error.  Command
        propagation uses port 3010.
      - 'Note: After enabling propagation, run force synchronization on either node.'
  hastatus:
    type: str
    choices:
      - ENABLED
      - STAYSECONDARY
      - DISABLED
      - STAYPRIMARY
    description:
      - The HA status of the node. The HA status C(STAYSECONDARY) is used to force
        the secondary device stay as secondary independent of the state of the Primary
        device. For example, in an existing HA setup, the Primary node has to be upgraded
        and this process would take few seconds. During the upgradation, it is possible
        that the Primary node may suffer from a downtime for a few seconds. However,
        the Secondary should not take over as the Primary node. Thus, the Secondary
        node should remain as Secondary even if there is a failure in the Primary
        node.
      - "\t C(STAYPRIMARY) configuration keeps the node in primary state in case if\
        \ it is healthy, even if the peer node was the primary node initially. If\
        \ the node with C(STAYPRIMARY) setting (and no peer node) is added to a primary\
        \ node (which has this node as the peer) then this node takes over as the\
        \ new primary and the older node becomes secondary. C(ENABLED) state means\
        \ normal HA operation without any constraints/preferences. C(DISABLED) state\
        \ disables the normal HA operation of the node."
  hasync:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Automatically maintain synchronization by duplicating the configuration of
        the primary node on the secondary node. This setting is not propagated. Automatic
        synchronization requires that this setting be enabled (the default) on the
        current secondary node. Synchronization uses TCP port 3010.
  hellointerval:
    type: float
    description:
      - Interval, in milliseconds, between heartbeat messages sent to the peer node.
        The heartbeat messages are UDP packets sent to port 3003 of the peer node.
  id:
    type: float
    description:
      - Number that uniquely identifies the node. For self node, it will always be
        0. Peer node values can range from 1-64.
  inc:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'This option is required if the HA nodes reside on different networks. When
        this mode is enabled, the following independent network entities and configurations
        are neither propagated nor synced to the other node: MIPs, SNIPs, VLANs, routes
        (except LLB routes), route monitors, RNAT rules (except any RNAT rule with
        a VIP as the NAT IP), and dynamic routing configurations. They are maintained
        independently on each node.'
  ipaddress:
    type: str
    description:
      - The NSIP or NSIP6 address of the node to be added for an HA configuration.
        This setting is neither propagated nor synchronized.
  maxflips:
    type: float
    description:
      - Max number of flips allowed before becoming sticky primary
  maxfliptime:
    type: float
    description:
      - Interval after which flipping of node states can again start
  rpcnodepassword:
    type: str
    description:
      - Password to be used in authentication with the peer rpc node.
  syncstatusstrictmode:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - strict mode flag for sync status
  syncvlan:
    type: float
    description:
      - Vlan on which HA related communication is sent. This include sync, propagation
        , connection mirroring , LB persistency config sync, persistent session sync
        and session state sync. However HA heartbeats can go all interfaces.
  hanode_routemonitor6_binding:
    type: dict
    description: Bindings for hanode_routemonitor6_binding resource
    suboptions:
      mode:
        type: str
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
  hanode_routemonitor_binding:
    type: dict
    description: Bindings for hanode_routemonitor_binding resource
    suboptions:
      mode:
        type: str
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
---
- name: Sample hanode playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure hanode
      delegate_to: localhost
      netscaler.adc.hanode:
        state: present
        ipaddress: 10.189.96.60
        inc: ENABLED
        hanode_id: '1'
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
