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
module: hanode
short_description: Configuration for node resource.
description: Configuration for node resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  deadinterval:
    description:
      - Number of seconds after which a peer node is marked DOWN if heartbeat messages
        are not received from the peer node.
    type: int
    default: 3
  failsafe:
    description:
      - Keep one node primary if both nodes fail the health check, so that a partially
        available node can back up data and handle traffic. This mode is set independently
        on each node.
    type: str
    choices:
      - true
      - false
  haprop:
    description:
      - 'Automatically propagate all commands from the primary to the secondary node,
        except the following:'
      - '* All HA configuration related commands. For example, add ha node, set ha
        node, and bind ha node. '
      - '* All Interface related commands. For example, set interface and unset interface.'
      - '* All channels related commands. For example, add channel, set channel, and
        bind channel.'
      - The propagated command is executed on the secondary node before it is executed
        on the primary. If command propagation fails, or if command execution fails
        on the secondary, the primary node executes the command and logs an error.  Command
        propagation uses port 3010.
      - 'Note: After enabling propagation, run force synchronization on either node.'
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  hastatus:
    description:
      - The HA status of the node. The HA status STAYSECONDARY is used to force the
        secondary device stay as secondary independent of the state of the Primary
        device. For example, in an existing HA setup, the Primary node has to be upgraded
        and this process would take few seconds. During the upgradation, it is possible
        that the Primary node may suffer from a downtime for a few seconds. However,
        the Secondary should not take over as the Primary node. Thus, the Secondary
        node should remain as Secondary even if there is a failure in the Primary
        node.
      - "\t STAYPRIMARY configuration keeps the node in primary state in case if it\
        \ is healthy, even if the peer node was the primary node initially. If the\
        \ node with STAYPRIMARY setting (and no peer node) is added to a primary node\
        \ (which has this node as the peer) then this node takes over as the new primary\
        \ and the older node becomes secondary. ENABLED state means normal HA operation\
        \ without any constraints/preferences. DISABLED state disables the normal\
        \ HA operation of the node."
    type: str
    choices:
      - ENABLED
      - STAYSECONDARY
      - DISABLED
      - STAYPRIMARY
  hasync:
    description:
      - Automatically maintain synchronization by duplicating the configuration of
        the primary node on the secondary node. This setting is not propagated. Automatic
        synchronization requires that this setting be enabled (the default) on the
        current secondary node. Synchronization uses TCP port 3010.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  hellointerval:
    description:
      - Interval, in milliseconds, between heartbeat messages sent to the peer node.
        The heartbeat messages are UDP packets sent to port 3003 of the peer node.
    type: int
    default: 200
  id:
    description:
      - Number that uniquely identifies the node. For self node, it will always be
        0. Peer node values can range from 1-64.
    type: int
  inc:
    description:
      - 'This option is required if the HA nodes reside on different networks. When
        this mode is enabled, the following independent network entities and configurations
        are neither propagated nor synced to the other node: MIPs, SNIPs, VLANs, routes
        (except LLB routes), route monitors, RNAT rules (except any RNAT rule with
        a VIP as the NAT IP), and dynamic routing configurations. They are maintained
        independently on each node.'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ipaddress:
    description:
      - The NSIP or NSIP6 address of the node to be added for an HA configuration.
        This setting is neither propagated nor synchronized.
    type: str
  maxflips:
    description:
      - Max number of flips allowed before becoming sticky primary
    type: int
  maxfliptime:
    description:
      - Interval after which flipping of node states can again start
    type: int
  syncstatusstrictmode:
    description:
      - strict mode flag for sync status
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  syncvlan:
    description:
      - Vlan on which HA related communication is sent. This include sync, propagation
        , connection mirroring , LB persistency config sync, persistent session sync
        and session state sync. However HA heartbeats can go all interfaces.
    type: int
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
