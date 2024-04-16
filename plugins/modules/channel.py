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
module: channel
short_description: Configuration for channel resource.
description: Configuration for channel resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  bandwidthhigh:
    type: raw
    description:
      - High threshold value for the bandwidth usage of the LA channel, in Mbps. The
        Citrix ADC generates an SNMP trap message when the bandwidth usage of the
        LA channel is greater than or equal to the specified high threshold value.
  bandwidthnormal:
    type: raw
    description:
      - Normal threshold value for the bandwidth usage of the LA channel, in Mbps.
        When the bandwidth usage of the LA channel returns to less than or equal to
        the specified normal threshold after exceeding the high threshold, the Citrix
        ADC generates an SNMP trap message to indicate that the bandwidth usage has
        returned to normal.
  conndistr:
    type: str
    choices:
      - DISABLED
      - ENABLED
    description:
      - The 'connection' distribution mode for the LA channel.
  flowctl:
    type: raw
    choices:
      - 'OFF'
      - RX
      - TX
      - RXTX
      - 'ON'
    description:
      - Specifies the flow control type for this LA channel to manage the flow of
        frames. Flow control is a function as mentioned in clause 31 of the IEEE 802.3
        standard. Flow control allows congested ports to pause traffic from the peer
        device. Flow control is achieved by sending PAUSE frames.
  haheartbeat:
    type: raw
    choices:
      - 'OFF'
      - 'ON'
    description:
      - In a High Availability (HA) configuration, configure the LA channel for sending
        heartbeats. LA channel that has HA Heartbeat disabled should not send the
        heartbeats.
  hamonitor:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - In a High Availability (HA) configuration, monitor the LA channel for failure
        events. Failure of any LA channel that has HA MON enabled triggers HA failover.
  id:
    type: raw
    description:
      - ID for the LA channel or cluster LA channel or LR channel to be created. Specify
        an LA channel in LA/x notation, where x can range from 1 to 8 or cluster LA
        channel in CLA/x notation or Link redundant channel in LR/x notation, where
        x can range from 1 to 4. Cannot be changed after the LA channel is created.
  ifalias:
    type: raw
    description:
      - Alias name for the LA channel. Used only to enhance readability. To perform
        any operations, you have to specify the LA channel ID.
  ifnum:
    type: list
    description:
      - Interfaces to be bound to the LA channel of a Citrix ADC or to the LA channel
        of a cluster configuration.
      - For an LA channel of a Citrix ADC, specify an interface in C/U notation (for
        example, 1/3).
      - For an LA channel of a cluster configuration, specify an interface in N/C/U
        notation (for example, 2/1/3).
      - 'where C can take one of the following values:'
      - '* 0 - Indicates a management interface.'
      - '* 1 - Indicates a 1 Gbps port.'
      - '* 10 - Indicates a 10 Gbps port.'
      - U is a unique integer for representing an interface in a particular port group.
      - N is the ID of the node to which an interface belongs in a cluster configuration.
      - Use spaces to separate multiple entries.
    elements: str
  lamac:
    type: str
    description:
      - Specifies a MAC address for the LA channels configured in Citrix ADC virtual
        appliances (VPX). This MAC address is persistent after each reboot.
      - If you don't specify this parameter, a MAC address is generated randomly for
        each LA channel. These MAC addresses change after each reboot.
  linkredundancy:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Link Redundancy for Cluster LAG.
  lrminthroughput:
    type: raw
    description:
      - Specifies the minimum throughput threshold (in Mbps) to be met by the active
        subchannel. Setting this parameter automatically divides an LACP channel into
        logical subchannels, with one subchannel active and the others in standby
        mode.  When the maximum supported throughput of the active channel falls below
        the lrMinThroughput value, link failover occurs and a standby subchannel becomes
        active.
  macdistr:
    type: str
    choices:
      - SOURCE
      - DESTINATION
      - BOTH
    description:
      - The  'MAC' distribution mode for the LA channel.
  mode:
    type: str
    choices:
      - MANUAL
      - AUTO
    description:
      - The initital mode for the LA channel.
  mtu:
    type: raw
    description:
      - The Maximum Transmission Unit (MTU) is the largest packet size, measured in
        bytes excluding 14 bytes ethernet header and 4 bytes CRC, that can be transmitted
        and received by an interface. The default value of MTU is 1500 on all the
        interface of Citrix ADC, some Cloud Platforms will restrict Citrix ADC to
        use the lesser default value. Any MTU value more than 1500 is called Jumbo
        MTU and will make the interface as jumbo enabled. The Maximum Jumbo MTU in
        Citrix ADC is 9216, however, some Virtualized / Cloud Platforms will have
        lesser Maximum Jumbo MTU Value (9000). In the case of Cluster, the Backplane
        interface requires an MTU value of 78 bytes more than the Max MTU configured
        on any other Data-Plane Interface. When the Data plane interfaces are all
        at default 1500 MTU, Cluster Back Plane will be automatically set to 1578
        (1500 + 78) MTU. If a Backplane interface is reset to Data Plane Interface,
        then the 1578 MTU will be automatically reset to the default MTU of 1500(or
        whatever lesser default value). If any data plane interface of a Cluster is
        configured with a Jumbo MTU ( > 1500), then all backplane interfaces require
        to be configured with a minimum MTU of 'Highest Data Plane MTU in the Cluster
        + 78'. That makes the maximum Jumbo MTU for any Data-Plane Interface in a
        Cluster System to be '9138 (9216 - 78)., where 9216 is the maximum Jumbo MTU.
        On certain Virtualized / Cloud Platforms, the maximum  possible MTU is restricted
        to a lesser value, Similar calculation can be applied, Maximum Data Plane
        MTU in Cluster = (Maximum possible MTU - 78).
  speed:
    type: raw
    choices:
      - AUTO
      - 10
      - 100
      - 1000
      - 10000
      - 25000
      - 40000
      - 50000
      - 100000
    description:
      - Ethernet speed of the channel, in Mbps. If the speed of any bound interface
        is greater than or equal to the value set for this parameter, the state of
        the interface is UP. Otherwise, the state is INACTIVE. Bound Interfaces whose
        state is INACTIVE do not process any traffic.
  tagall:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Adds a four-byte 802.1q tag to every packet sent on this channel.  The C(ON)
        setting applies tags for all VLANs that are bound to this channel. C(OFF)
        applies the tag for all VLANs other than the native VLAN.
  throughput:
    type: raw
    description:
      - Low threshold value for the throughput of the LA channel, in Mbps. In an high
        availability (HA) configuration, failover is triggered when the LA channel
        has HA MON enabled and the throughput is below the specified threshold.
  trunk:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This is deprecated by tagall
  channel_interface_binding:
    type: dict
    description: Bindings for channel_interface_binding resource
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
- name: Sample Playbook
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Sample Task | channel
      delegate_to: localhost
      netscaler.adc.channel:
        state: present
        id: LA/1
        throughput: '0'
        lrminthroughput: '0'
        bandwidthhigh: '0'
        bandwidthnormal: '0'
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
