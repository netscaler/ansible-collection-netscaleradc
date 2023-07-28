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
module: nstcpprofile
short_description: Configuration for TCP profile resource.
description: Configuration for TCP profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ackaggregation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable ACK Aggregation.
    type: str
    default: DISABLED
  ackonpush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send immediate positive acknowledgement (ACK) on receipt of TCP packets with
        PUSH flag.
    type: str
    default: ENABLED
  applyadaptivetcp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Apply Adaptive TCP optimizations
    type: str
    default: DISABLED
  buffersize:
    description:
      - TCP buffering size, in bytes.
    type: int
    default: 8190
  burstratecontrol:
    choices:
      - DISABLED
      - FIXED
      - DYNAMIC
    description:
      - TCP Burst Rate Control C(DISABLED)/C(FIXED)/C(DYNAMIC). C(FIXED) requires
        a TCP rate to be set.
    type: str
    default: DISABLED
  clientiptcpoption:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Client IP in TCP options
    type: str
    default: DISABLED
  clientiptcpoptionnumber:
    description:
      - ClientIP TCP Option number
    type: int
  delayedack:
    description:
      - Timeout for TCP delayed ACK, in milliseconds.
    type: int
    default: 100
  dropestconnontimeout:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Silently drop tcp established connections on idle timeout
    type: str
    default: DISABLED
  drophalfclosedconnontimeout:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Silently drop tcp half closed connections on idle timeout
    type: str
    default: DISABLED
  dsack:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable DSACK.
    type: str
    default: ENABLED
  dupackthresh:
    description:
      - TCP dupack threshold.
    type: int
    default: 3
  dynamicreceivebuffering:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable dynamic receive buffering. When enabled, allows the receive
        buffer to be adjusted dynamically based on memory and network conditions.
      - 'Note: The buffer size argument must be set for dynamic adjustments to take
        place.'
    type: str
    default: DISABLED
  ecn:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable TCP Explicit Congestion Notification.
    type: str
    default: DISABLED
  establishclientconn:
    choices:
      - AUTOMATIC
      - CONN_ESTABLISHED
      - ON_FIRST_DATA
    description:
      - Establishing Client Client connection on First data/ Final-ACK / Automatic
    type: str
    default: AUTOMATIC
  fack:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable FACK (Forward ACK).
    type: str
    default: DISABLED
  flavor:
    choices:
      - Default
      - Westwood
      - BIC
      - CUBIC
      - Nile
    description:
      - Set TCP congestion control algorithm.
    type: str
    default: Default
  frto:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable FRTO (Forward RTO-Recovery).
    type: str
    default: DISABLED
  hystart:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable CUBIC Hystart
    type: str
    default: DISABLED
  initialcwnd:
    description:
      - Initial maximum upper limit on the number of TCP packets that can be outstanding
        on the TCP link to the server.
    type: int
    default: 4
  ka:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send periodic TCP keep-alive (KA) probes to check if peer is still up.
    type: str
    default: DISABLED
  kaconnidletime:
    description:
      - Duration, in seconds, for the connection to be idle, before sending a keep-alive
        (KA) probe.
    type: int
  kamaxprobes:
    description:
      - Number of keep-alive (KA) probes to be sent when not acknowledged, before
        assuming the peer to be down.
    type: int
  kaprobeinterval:
    description:
      - Time interval, in seconds, before the next keep-alive (KA) probe, if the peer
        does not respond.
    type: int
  kaprobeupdatelastactivity:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Update last activity for the connection after receiving keep-alive (KA) probes.
    type: str
    default: ENABLED
  maxburst:
    description:
      - Maximum number of TCP segments allowed in a burst.
    type: int
    default: 6
  maxcwnd:
    description:
      - TCP Maximum Congestion Window.
    type: int
    default: 524288
  maxpktpermss:
    description:
      - Maximum number of TCP packets allowed per maximum segment size (MSS).
    type: int
  minrto:
    description:
      - Minimum retransmission timeout, in milliseconds, specified in 10-millisecond
        increments (value must yield a whole number if divided by  10).
    type: int
    default: 1000
  mpcapablecbit:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set C bit in MP-CAPABLE Syn-Ack sent by Citrix ADC
    type: str
    default: DISABLED
  mptcp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Multipath TCP.
    type: str
    default: DISABLED
  mptcpdropdataonpreestsf:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable silently dropping the data on Pre-Established subflow. When
        enabled, DSS data packets are dropped silently instead of dropping the connection
        when data is received on pre established subflow.
    type: str
    default: DISABLED
  mptcpfastopen:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Multipath TCP fastopen. When enabled, DSS data packets are
        accepted before receiving the third ack of SYN handshake.
    type: str
    default: DISABLED
  mptcpsessiontimeout:
    description:
      - MPTCP session timeout in seconds. If this value is not set, idle MPTCP sessions
        are flushed after vserver's client idle timeout.
    type: int
  mss:
    description:
      - Maximum number of octets to allow in a TCP data segment.
    type: int
  nagle:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the Nagle algorithm on TCP connections.
    type: str
    default: DISABLED
  name:
    description:
      - Name for a TCP profile. Must begin with a letter, number, or the underscore
        \(_\) character. Other characters allowed, after the first character, are
        the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon
        \(:\), and equal \(=\) characters. The name of a TCP profile cannot be changed
        after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my tcp profile" or ''my tcp profile''\).'
    type: str
  oooqsize:
    description:
      - Maximum size of out-of-order packets queue. A value of 0 means no limit.
    type: int
    default: 64
  pktperretx:
    description:
      - Maximum limit on the number of packets that should be retransmitted on receiving
        a partial ACK.
    type: int
    default: 1
  rateqmax:
    description:
      - Maximum connection queue size in bytes, when BurstRateControl is used
    type: int
  rstmaxack:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable acceptance of RST that is out of window yet echoes highest
        ACK sequence number. Useful only in proxy mode.
    type: str
    default: DISABLED
  rstwindowattenuate:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable RST window attenuation to protect against spoofing. When
        enabled, will reply with corrective ACK when a sequence number is invalid.
    type: str
    default: DISABLED
  sack:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Selective ACKnowledgement (SACK).
    type: str
    default: DISABLED
  sendbuffsize:
    description:
      - TCP Send Buffer Size
    type: int
    default: 8190
  sendclientportintcpoption:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send Client Port number along with Client IP in TCP-Options. ClientIpTcpOption
        must be C(ENABLED)
    type: str
    default: DISABLED
  slowstartincr:
    description:
      - Multiplier that determines the rate at which slow start increases the size
        of the TCP transmission window after each acknowledgement of successful transmission.
    type: int
    default: 2
  slowstartthreshold:
    description:
      - TCP Slow Start Threhsold Value.
    type: int
    default: 524288
  spoofsyndrop:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable drop of invalid SYN packets to protect against spoofing.
        When disabled, established connections will be reset when a SYN packet is
        received.
    type: str
    default: ENABLED
  syncookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the SYNCOOKIE mechanism for TCP handshake with clients.
        Disabling SYNCOOKIE prevents SYN attack protection on the Citrix ADC.
    type: str
    default: ENABLED
  taillossprobe:
    choices:
      - ENABLED
      - DISABLED
    description:
      - TCP tail loss probe optimizations
    type: str
    default: DISABLED
  tcpfastopen:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable TCP Fastopen. When enabled, NS can receive or send Data
        in SYN or SYN-ACK packets.
    type: str
    default: DISABLED
  tcpfastopencookiesize:
    description:
      - TCP FastOpen Cookie size. This accepts only even numbers. Odd number is trimmed
        down to nearest even number.
    type: int
    default: 8
  tcpmode:
    choices:
      - TRANSPARENT
      - ENDPOINT
    description:
      - TCP Optimization modes C(TRANSPARENT) / C(ENDPOINT).
    type: str
    default: TRANSPARENT
  tcprate:
    description:
      - TCP connection payload send rate in Kb/s
    type: int
  tcpsegoffload:
    choices:
      - AUTOMATIC
      - DISABLED
    description:
      - Offload TCP segmentation to the NIC. If set to C(AUTOMATIC), TCP segmentation
        will be offloaded to the NIC, if the NIC supports it.
    type: str
    default: AUTOMATIC
  timestamp:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or Disable TCP Timestamp option (RFC 1323)
    type: str
    default: DISABLED
  ws:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable window scaling.
    type: str
    default: DISABLED
  wsval:
    description:
      - Factor used to calculate the new window size.
      - This argument is needed only when window scaling is enabled.
    type: int
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
