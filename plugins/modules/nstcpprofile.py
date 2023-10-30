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
module: nstcpprofile
short_description: Configuration for TCP profile resource.
description: Configuration for TCP profile resource.
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
  ackaggregation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable ACK Aggregation.
    default: DISABLED
  ackonpush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send immediate positive acknowledgement (ACK) on receipt of TCP packets with
        PUSH flag.
    default: ENABLED
  applyadaptivetcp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Apply Adaptive TCP optimizations
    default: DISABLED
  buffersize:
    type: float
    description:
      - TCP buffering size, in bytes.
    default: 8190
  burstratecontrol:
    type: str
    choices:
      - DISABLED
      - FIXED
      - DYNAMIC
    description:
      - TCP Burst Rate Control C(DISABLED)/C(FIXED)/C(DYNAMIC). C(FIXED) requires
        a TCP rate to be set.
    default: DISABLED
  clientiptcpoption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Client IP in TCP options
    default: DISABLED
  clientiptcpoptionnumber:
    type: float
    description:
      - ClientIP TCP Option number
  delayedack:
    type: float
    description:
      - Timeout for TCP delayed ACK, in milliseconds.
    default: 100
  dropestconnontimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Silently drop tcp established connections on idle timeout
    default: DISABLED
  drophalfclosedconnontimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Silently drop tcp half closed connections on idle timeout
    default: DISABLED
  dsack:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable DSACK.
    default: ENABLED
  dupackthresh:
    type: float
    description:
      - TCP dupack threshold.
    default: 3
  dynamicreceivebuffering:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable dynamic receive buffering. When enabled, allows the receive
        buffer to be adjusted dynamically based on memory and network conditions.
      - 'Note: The buffer size argument must be set for dynamic adjustments to take
        place.'
    default: DISABLED
  ecn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable TCP Explicit Congestion Notification.
    default: DISABLED
  establishclientconn:
    type: str
    choices:
      - AUTOMATIC
      - CONN_ESTABLISHED
      - ON_FIRST_DATA
    description:
      - Establishing Client Client connection on First data/ Final-ACK / Automatic
    default: AUTOMATIC
  fack:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable FACK (Forward ACK).
    default: DISABLED
  flavor:
    type: str
    choices:
      - Default
      - Westwood
      - BIC
      - CUBIC
      - Nile
    description:
      - Set TCP congestion control algorithm.
    default: Default
  frto:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable FRTO (Forward RTO-Recovery).
    default: DISABLED
  hystart:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable CUBIC Hystart
    default: DISABLED
  initialcwnd:
    type: float
    description:
      - Initial maximum upper limit on the number of TCP packets that can be outstanding
        on the TCP link to the server.
    default: 4
  ka:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send periodic TCP keep-alive (KA) probes to check if peer is still up.
    default: DISABLED
  kaconnidletime:
    type: float
    description:
      - Duration, in seconds, for the connection to be idle, before sending a keep-alive
        (KA) probe.
  kamaxprobes:
    type: float
    description:
      - Number of keep-alive (KA) probes to be sent when not acknowledged, before
        assuming the peer to be down.
  kaprobeinterval:
    type: float
    description:
      - Time interval, in seconds, before the next keep-alive (KA) probe, if the peer
        does not respond.
  kaprobeupdatelastactivity:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Update last activity for the connection after receiving keep-alive (KA) probes.
    default: ENABLED
  maxburst:
    type: float
    description:
      - Maximum number of TCP segments allowed in a burst.
    default: 6
  maxcwnd:
    type: float
    description:
      - TCP Maximum Congestion Window.
    default: 524288
  maxpktpermss:
    type: float
    description:
      - Maximum number of TCP packets allowed per maximum segment size (MSS).
  minrto:
    type: float
    description:
      - Minimum retransmission timeout, in milliseconds, specified in 10-millisecond
        increments (value must yield a whole number if divided by  10).
    default: 1000
  mpcapablecbit:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set C bit in MP-CAPABLE Syn-Ack sent by Citrix ADC
    default: DISABLED
  mptcp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Multipath TCP.
    default: DISABLED
  mptcpdropdataonpreestsf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable silently dropping the data on Pre-Established subflow. When
        enabled, DSS data packets are dropped silently instead of dropping the connection
        when data is received on pre established subflow.
    default: DISABLED
  mptcpfastopen:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are
        accepted before receiving the third ack of SYN handshake.
    default: DISABLED
  mptcpsessiontimeout:
    type: float
    description:
      - MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions
        are flushed after vserver's client idle timeout.
  mss:
    type: float
    description:
      - Maximum number of octets to allow in a TCP data segment.
  nagle:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the Nagle algorithm on TCP connections.
    default: DISABLED
  name:
    type: str
    description:
      - Name for a TCP profile. Must begin with a letter, number, or the underscore
        \(_\) character. Other characters allowed, after the first character, are
        the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon
        \(:\), and equal \(=\) characters. The name of a TCP profile cannot be changed
        after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my tcp profile" or ''my tcp profile''\).'
  oooqsize:
    type: float
    description:
      - Maximum size of out-of-order packets queue. A value of 0 means no limit.
    default: 64
  pktperretx:
    type: float
    description:
      - Maximum limit on the number of packets that should be retransmitted on receiving
        a partial ACK.
    default: 1
  rateqmax:
    type: float
    description:
      - Maximum connection queue size in bytes, when BurstRateControl is used
  rstmaxack:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable acceptance of RST that is out of window yet echoes highest
        ACK sequence number. Useful only in proxy mode.
    default: DISABLED
  rstwindowattenuate:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable RST window attenuation to protect against spoofing. When
        enabled, will reply with corrective ACK when a sequence number is invalid.
    default: DISABLED
  sack:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Selective ACKnowledgement (SACK).
    default: DISABLED
  sendbuffsize:
    type: float
    description:
      - TCP Send Buffer Size
    default: 8190
  sendclientportintcpoption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Client Port number along with Client IP in TCP-Options. ClientIpTcpOption
        must be C(ENABLED)
    default: DISABLED
  slowstartincr:
    type: float
    description:
      - Multiplier that determines the rate at which slow start increases the size
        of the TCP transmission window after each acknowledgement of successful transmission.
    default: 2
  slowstartthreshold:
    type: float
    description:
      - TCP Slow Start Threhsold Value.
    default: 524288
  spoofsyndrop:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable drop of invalid SYN packets to protect against spoofing.
        When disabled, established connections will be reset when a SYN packet is
        received.
    default: ENABLED
  syncookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients.
        Disabling SYNCOOKIE prevents SYN attack protection on the Citrix ADC.
    default: ENABLED
  taillossprobe:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - TCP tail loss probe optimizations
    default: DISABLED
  tcpfastopen:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable TCP Fastopen. When enabled, NS can receive or send Data
        in SYN or SYN-ACK packets.
    default: DISABLED
  tcpfastopencookiesize:
    type: float
    description:
      - TCP FastOpen Cookie size. This accepts only even numbers. Odd number is trimmed
        down to nearest even number.
    default: 8
  tcpmode:
    type: str
    choices:
      - TRANSPARENT
      - ENDPOINT
    description:
      - TCP Optimization modes C(TRANSPARENT) / C(ENDPOINT).
    default: TRANSPARENT
  tcprate:
    type: float
    description:
      - TCP connection payload send rate in Kb/s
  tcpsegoffload:
    type: str
    choices:
      - AUTOMATIC
      - DISABLED
    description:
      - Offload TCP segmentation to the NIC. If set to C(AUTOMATIC), TCP segmentation
        will be offloaded to the NIC, if the NIC supports it.
    default: AUTOMATIC
  timestamp:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or Disable TCP Timestamp option (RFC 1323)
    default: DISABLED
  ws:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable window scaling.
    default: DISABLED
  wsval:
    type: float
    description:
      - Factor used to calculate the new window size.
      - This argument is needed only when window scaling is enabled.
    default: 4
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
