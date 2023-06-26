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
module: channel
short_description: Configuration for channel resource.
description: Configuration for channel resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bandwidthhigh:
    description:
      - High threshold value for the bandwidth usage of the LA channel, in Mbps. The
        Citrix ADC generates an SNMP trap message when the bandwidth usage of the
        LA channel is greater than or equal to the specified high threshold value.
    type: int
  bandwidthnormal:
    description:
      - Normal threshold value for the bandwidth usage of the LA channel, in Mbps.
        When the bandwidth usage of the LA channel returns to less than or equal to
        the specified normal threshold after exceeding the high threshold, the Citrix
        ADC generates an SNMP trap message to indicate that the bandwidth usage has
        returned to normal.
    type: int
  conndistr:
    description:
      - The 'connection' distribution mode for the LA channel.
    type: str
    choices:
      - DISABLED
      - ENABLED
  flowctl:
    description:
      - Specifies the flow control type for this LA channel to manage the flow of
        frames. Flow control is a function as mentioned in clause 31 of the IEEE 802.3
        standard. Flow control allows congested ports to pause traffic from the peer
        device. Flow control is achieved by sending PAUSE frames.
    type: str
    choices:
      - false
      - RX
      - TX
      - RXTX
      - true
  haheartbeat:
    description:
      - In a High Availability (HA) configuration, configure the LA channel for sending
        heartbeats. LA channel that has HA Heartbeat disabled should not send the
        heartbeats.
    type: str
    default: true
    choices:
      - false
      - true
  hamonitor:
    description:
      - In a High Availability (HA) configuration, monitor the LA channel for failure
        events. Failure of any LA channel that has HA MON enabled triggers HA failover.
    type: str
    default: true
    choices:
      - true
      - false
  id:
    description:
      - ID for the LA channel or cluster LA channel or LR channel to be created. Specify
        an LA channel in LA/x notation, where x can range from 1 to 8 or cluster LA
        channel in CLA/x notation or Link redundant channel in LR/x notation, where
        x can range from 1 to 4. Cannot be changed after the LA channel is created.
    type: str
  ifalias:
    description:
      - Alias name for the LA channel. Used only to enhance readability. To perform
        any operations, you have to specify the LA channel ID.
    type: str
    default: '" "'
  ifnum:
    description:
      - Interfaces to be bound to the LA channel of a Citrix ADC or to the LA channel
        of a cluster configuration.
      - 'For an LA channel of a Citrix ADC, specify an interface in C/U notation (for
        example, 1/3). '
      - For an LA channel of a cluster configuration, specify an interface in N/C/U
        notation (for example, 2/1/3).
      - 'where C can take one of the following values:'
      - '* 0 - Indicates a management interface.'
      - '* 1 - Indicates a 1 Gbps port.'
      - '* 10 - Indicates a 10 Gbps port.'
      - U is a unique integer for representing an interface in a particular port group.
      - N is the ID of the node to which an interface belongs in a cluster configuration.
      - Use spaces to separate multiple entries.
    type: list
    elements: str
  lamac:
    description:
      - 'Specifies a MAC address for the LA channels configured in Citrix ADC virtual
        appliances (VPX). This MAC address is persistent after each reboot. '
      - If you don't specify this parameter, a MAC address is generated randomly for
        each LA channel. These MAC addresses change after each reboot.
    type: str
  linkredundancy:
    description:
      - Link Redundancy for Cluster LAG.
    type: str
    choices:
      - true
      - false
  lrminthroughput:
    description:
      - Specifies the minimum throughput threshold (in Mbps) to be met by the active
        subchannel. Setting this parameter automatically divides an LACP channel into
        logical subchannels, with one subchannel active and the others in standby
        mode.  When the maximum supported throughput of the active channel falls below
        the lrMinThroughput value, link failover occurs and a standby subchannel becomes
        active.
    type: int
  macdistr:
    description:
      - The  'MAC' distribution mode for the LA channel.
    type: str
    choices:
      - SOURCE
      - DESTINATION
      - BOTH
  mode:
    description:
      - The initital mode for the LA channel.
    type: str
    choices:
      - MANUAL
      - AUTO
  mtu:
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
    type: int
    default: 1500
  speed:
    description:
      - Ethernet speed of the channel, in Mbps. If the speed of any bound interface
        is greater than or equal to the value set for this parameter, the state of
        the interface is UP. Otherwise, the state is INACTIVE. Bound Interfaces whose
        state is INACTIVE do not process any traffic.
    type: str
    default: AUTO
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
  state:
    description:
      - Enable or disable the LA channel.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tagall:
    description:
      - Adds a four-byte 802.1q tag to every packet sent on this channel.  The ON
        setting applies tags for all VLANs that are bound to this channel. OFF applies
        the tag for all VLANs other than the native VLAN.
    type: str
    choices:
      - true
      - false
  throughput:
    description:
      - Low threshold value for the throughput of the LA channel, in Mbps. In an high
        availability (HA) configuration, failover is triggered when the LA channel
        has HA MON enabled and the throughput is below the specified threshold.
    type: int
  trunk:
    description:
      - This is deprecated by tagall
    type: str
    choices:
      - true
      - false
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