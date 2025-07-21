#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: interface
short_description: Configuration for interface resource.
description: Configuration for interface resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  autoneg:
    type: str
    choices:
      - DISABLED
      - ENABLED
    description:
      - Auto-negotiation state of the interface. With the C(ENABLED) setting, the
        Citrix ADC auto-negotiates the speed and duplex settings with the peer network
        device on the link. The Citrix ADC appliance auto-negotiates the settings
        of only those parameters (speed or duplex mode) for which the value is set
        as AUTO.
  bandwidthhigh:
    type: int
    description:
      - High threshold value for the bandwidth usage of the interface, in Mbps. The
        Citrix ADC generates an SNMP trap message when the bandwidth usage of the
        interface is greater than or equal to the specified high threshold value.
  bandwidthnormal:
    type: int
    description:
      - Normal threshold value for the bandwidth usage of the interface, in Mbps.
        When the bandwidth usage of the interface becomes less than or equal to the
        specified normal threshold after exceeding the high threshold, the Citrix
        ADC generates an SNMP trap message to indicate that the bandwidth usage has
        returned to normal.
  duplex:
    type: str
    choices:
      - AUTO
      - HALF
      - FULL
    description:
      - The duplex mode for the interface. Notes:* If you set the duplex mode to C(AUTO),
        the Citrix ADC attempts to auto-negotiate the duplex mode of the interface
        when it is UP. You must enable auto negotiation on the interface. If you set
        a duplex mode other than C(AUTO), you must specify the same duplex mode for
        the peer network device. Mismatched speed and duplex settings between the
        peer devices of a link lead to link errors, packet loss, and other errors.
  flowctl:
    type: str
    choices:
      - 'OFF'
      - RX
      - TX
      - RXTX
      - 'ON'
    description:
      - 802.3x flow control setting for the interface.  The 802.3x specification does
        not define flow control for 10 Mbps and 100 Mbps speeds, but if a Gigabit
        Ethernet interface operates at those speeds, the flow control settings can
        be applied. The flow control setting that is finally applied to an interface
        depends on auto-negotiation. With the C(ON) option, the peer negotiates the
        flow control, but the appliance then forces two-way flow control for the interface.
  haheartbeat:
    type: str
    choices:
      - 'OFF'
      - 'ON'
    description:
      - In a High Availability (HA) or Cluster configuration, configure the interface
        for sending heartbeats. In an HA or Cluster configuration, an interface that
        has HA Heartbeat disabled should not send the heartbeats.
  hamonitor:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - In a High Availability (HA) configuration, monitor the interface for failure
        events. In an HA configuration, an interface that has HA MON enabled and is
        not bound to any Failover Interface Set (FIS), is a critical interface. Failure
        or disabling of any critical interface triggers HA failover.
  id:
    type: str
    description:
      - 'Interface number, in C/U format, where C can take one of the following values:'
      - '* 0 - Indicates a management interface.'
      - '* 1 - Indicates a 1 Gbps port.'
      - '* 10 - Indicates a 10 Gbps port.'
      - '* LA - Indicates a link aggregation port.'
      - '* LO - Indicates a loop back port.'
      - U is a unique integer for representing an interface in a particular port group.
  ifalias:
    type: str
    description:
      - Alias name for the interface. Used only to enhance readability. To perform
        any operations, you have to specify the interface ID.
  lacpkey:
    type: int
    description:
      - Integer identifying the LACP LA channel to which the interface is to be bound.
      - For an LA channel of the Citrix ADC, this digit specifies the variable x of
        an LA channel in LA/x notation, where x can range from 1 to 8. For example,
        if you specify 3 as the LACP key for an LA channel, the interface is bound
        to the LA channel LA/3.
      - For an LA channel of a cluster configuration, this digit specifies the variable
        y of a cluster LA channel in CLA/(y-4) notation, where y can range from 5
        to 8. For example, if you specify 6 as the LACP key for a cluster LA channel,
        the interface is bound to the cluster LA channel CLA/2.
  lacpmode:
    type: str
    choices:
      - DISABLED
      - ACTIVE
      - PASSIVE
    description:
      - Bind the interface to a LA channel created by the Link Aggregation control
        protocol (LACP).
      - 'Available settings function as follows:'
      - '* Active - The LA channel port of the Citrix ADC generates LACPDU messages
        on a regular basis, regardless of any need expressed by its peer device to
        receive them.'
      - '* Passive - The LA channel port of the Citrix ADC does not transmit LACPDU
        messages unless the peer device port is in the active mode. That is, the port
        does not speak unless spoken to.'
      - '* Disabled - Unbinds the interface from the LA channel. If this is the only
        interface in the LA channel, the LA channel is removed.'
  lacppriority:
    type: int
    description:
      - LACP port priority, expressed as an integer. The lower the number, the higher
        the priority. The Citrix ADC limits the number of interfaces in an LA channel
        to sixteen.
  lacptimeout:
    type: str
    choices:
      - LONG
      - SHORT
    description:
      - Interval at which the Citrix ADC sends LACPDU messages to the peer device
        on the LA channel.
      - 'Available settings function as follows:'
      - C(LONG) - 30 seconds.
      - C(SHORT) - 1 second.
  lagtype:
    type: str
    choices:
      - NODE
      - CLUSTER
    description:
      - Type of entity (Citrix ADC or cluster configuration) for which to create the
        channel.
  linkredundancy:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Link Redundancy for Cluster LAG.
  lldpmode:
    type: str
    choices:
      - NONE
      - TRANSMITTER
      - RECEIVER
      - TRANSCEIVER
    description:
      - Link Layer Discovery Protocol (LLDP) mode for an interface. The resultant
        LLDP mode of an interface depends on the LLDP mode configured at the global
        and the interface levels.
  lrsetpriority:
    type: int
    description:
      - LRSET port priority, expressed as an integer ranging from 1 to 1024. The highest
        priority is 1. The Citrix ADC limits the number of interfaces in an LRSET
        to 8. Within a LRSET the highest LR Priority Interface is considered as the
        first candidate for the Active interface, if the interface is UP.
  mtu:
    type: int
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
  ringsize:
    type: int
    description:
      - The receive ringsize of the interface. A higher number provides more number
        of buffers in handling incoming traffic.
  ringtype:
    type: str
    choices:
      - Elastic
      - Fixed
    description:
      - The receive ringtype of the interface (C(Fixed) or C(Elastic)). A fixed ring
        type pre-allocates configured number of buffers irrespective of traffic rate.
        In contrast, an elastic ring, expands and shrinks based on incoming traffic
        rate.
  speed:
    type: str
    choices:
      - AUTO
      - '10'
      - '100'
      - '1000'
      - '10000'
      - '25000'
      - '40000'
      - '50000'
      - '100000'
    description:
      - Ethernet speed of the interface, in Mbps.
      - 'Notes:'
      - '* If you set the speed as AUTO, the Citrix ADC attempts to auto-negotiate
        or auto-sense the link speed of the interface when it is UP. You must enable
        auto negotiation on the interface.'
      - '* If you set a speed other than AUTO, you must specify the same speed for
        the peer network device. Mismatched speed and duplex settings between the
        peer devices of a link lead to link errors, packet loss, and other errors.'
      - Some interfaces do not support certain speeds. If you specify an unsupported
        speed, an error message appears.
  tagall:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Add a four-byte 802.1q tag to every packet sent on this interface.  The C(ON)
        setting applies the tag for this interface's native VLAN. C(OFF) applies the
        tag for all VLANs other than the native VLAN.
  throughput:
    type: int
    description:
      - Low threshold value for the throughput of the interface, in Mbps. In an HA
        configuration, failover is triggered if the interface has HA MON enabled and
        the throughput is below the specified the threshold.
  trunk:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This argument is deprecated by tagall.
  trunkallowedvlan:
    type: list
    description:
      - 'VLAN ID or range of VLAN IDs will be allowed on this trunk interface. In
        the command line interface, separate the range with a hyphen. For example:
        40-90.'
    elements: str
  trunkmode:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Accept and send 802.1q VLAN tagged packets, based on Allowed Vlan List of
        this interface.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample interface playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure interface
      delegate_to: localhost
      netscaler.adc.interface:
        state: present
        hamonitor: 'OFF'
        haheartbeat: 'OFF'
        throughput: '0'
        bandwidthhigh: '0'
        bandwidthnormal: '0'
        intftype: Loopback
        ifnum:
          - LO/1
        interface_id: LO/1
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
