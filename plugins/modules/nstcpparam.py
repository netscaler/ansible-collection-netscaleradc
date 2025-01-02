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
module: nstcpparam
short_description: Configuration for tcp parameters resource.
description: Configuration for tcp parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  ackonpush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send immediate positive acknowledgement (ACK) on receipt of TCP packets with
        PUSH flag.
  autosyncookietimeout:
    type: float
    description:
      - Timeout for the server to function in syncookie mode after the synattack.
        This is valid if TCP syncookie is disabled on the profile and server acts
        in non syncookie mode by default.
  compacttcpoptionnoop:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, non-negotiated TCP options are removed from the received packet
        while proxying it. By default, non-negotiated TCP options would be replaced
        by NOPs in the proxied packets. This option is not applicable for Citrix ADC
        generated packets.
  connflushifnomem:
    type: str
    choices:
      - 'NONE '
      - HALFCLOSED_AND_IDLE
      - FIFO
    description:
      - Flush an existing connection if no memory can be obtained for new connection.
      - ''
      - 'HALF_CLOSED_AND_IDLE: Flush a connection that is closed by us but not by
        peer, or failing that, a connection that is past configured idle time.  New
        connection fails if no such connection can be found.'
      - ''
      - 'C(FIFO): If no half-closed or idle connection can be found, flush the oldest
        non-management connection, even if it is active.  New connection fails if
        the oldest few connections are management connections.'
      - ''
      - 'Note: If you enable this setting, you should also consider lowering the zombie
        timeout and half-close timeout, while setting the Citrix ADC timeout.'
      - ''
      - 'See Also: connFlushThres argument below.'
  connflushthres:
    type: float
    description:
      - 'Flush an existing connection (as configured through -connFlushIfNoMem FIFO)
        if the system has more than specified number of connections, and a new connection
        is to be established.  Note: This value may be rounded down to be a whole
        multiple of the number of packet engines running.'
  delayedack:
    type: float
    description:
      - Timeout for TCP delayed ACK, in milliseconds.
  delinkclientserveronrst:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, Delink client and server connection, when there is outstanding
        data to be sent to the other side.
  downstaterst:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flag to switch on RST on down services.
  enhancedisngeneration:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, increase the ISN variation in SYN-ACKs sent by the NetScaler
  initialcwnd:
    type: float
    description:
      - Initial maximum upper limit on the number of TCP packets that can be outstanding
        on the TCP link to the server.
  kaprobeupdatelastactivity:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Update last activity for KA probes
  learnvsvrmss:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable maximum segment size (MSS) learning for virtual servers.
  limitedpersist:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Limit the number of persist (zero window) probes.
  maxburst:
    type: float
    description:
      - Maximum number of TCP segments allowed in a burst.
  maxdynserverprobes:
    type: float
    description:
      - Maximum number of probes that Citrix ADC can send out in 10 milliseconds,
        to dynamically learn a service. Citrix ADC probes for the existence of the
        origin in case of wildcard virtual server or services.
  maxpktpermss:
    type: float
    description:
      - Maximum number of TCP packets allowed per maximum segment size (MSS).
  maxsynackretx:
    type: float
    description:
      - When 'syncookie' is disabled in the TCP profile that is bound to the virtual
        server or service, and the number of TCP SYN+ACK retransmission by Citrix
        ADC for that virtual server or service crosses this threshold, the Citrix
        ADC responds by using the TCP SYN-Cookie mechanism.
  maxsynhold:
    type: float
    description:
      - Limit the number of client connections (SYN) waiting for status of probe system
        wide. Any new SYN packets will be dropped.
  maxsynholdperprobe:
    type: float
    description:
      - Limit the number of client connections (SYN) waiting for status of single
        probe. Any new SYN packets will be dropped.
  maxtimewaitconn:
    type: float
    description:
      - Maximum number of connections to hold in the TCP TIME_WAIT state on a packet
        engine. New connections entering TIME_WAIT state are proactively cleaned up.
  minrto:
    type: int
    description:
      - Minimum retransmission timeout, in milliseconds, specified in 10-millisecond
        increments (value must yield a whole number if divided by 10).
  mptcpchecksum:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use MPTCP DSS checksum
  mptcpclosemptcpsessiononlastsfclose:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow to send DATA FIN or FAST CLOSE on mptcp connection while sending FIN
        or RST on the last subflow.
  mptcpconcloseonpassivesf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Accept DATA_FIN/FAST_CLOSE on passive subflow
  mptcpfastcloseoption:
    type: str
    choices:
      - ACK
      - RESET
    description:
      - Allow to select option C(ACK) or C(RESET) to force the closure of an MPTCP
        connection abruptly.
  mptcpimmediatesfcloseonfin:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow subflows to close immediately on FIN before the DATA_FIN exchange is
        completed at mptcp level.
  mptcpmaxpendingsf:
    type: float
    description:
      - Maximum number of subflow connections supported in pending join state per
        mptcp connection.
  mptcpmaxsf:
    type: float
    description:
      - Maximum number of subflow connections supported in established state per mptcp
        connection.
  mptcppendingjointhreshold:
    type: float
    description:
      - Maximum system level pending join connections allowed.
  mptcpreliableaddaddr:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, Citrix ADC retransmits MPTCP ADD-ADDR option if echo response
        is not received within the timeout interval. The retransmission is attempted
        only once.
  mptcprtostoswitchsf:
    type: float
    description:
      - Number of RTO's at subflow level, after which MPCTP should start using other
        subflow.
  mptcpsendsfresetoption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow MPTCP subflows to send TCP RST Reason (MP_TCPRST) Option while sending
        TCP RST.
  mptcpsfreplacetimeout:
    type: float
    description:
      - The minimum idle time value in seconds for idle mptcp subflows after which
        the sublow is replaced by new incoming subflow if maximum subflow limit is
        reached. The priority for replacement is given to those subflow without any
        transaction
  mptcpsftimeout:
    type: float
    description:
      - The timeout value in seconds for idle mptcp subflows. If this timeout is not
        set, idle subflows are cleared after cltTimeout of vserver
  mptcpusebackupondss:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When enabled, if NS receives a DSS on a backup subflow, NS will start using
        that subflow to send data. And if disabled, NS will continue to transmit on
        current chosen subflow. In case there is some error on a subflow (like RTO's/RST
        etc.) then NS can choose a backup subflow irrespective of this tunable.
  msslearndelay:
    type: float
    description:
      - Frequency, in seconds, at which the virtual servers learn the Maximum segment
        size (MSS) from the services. The argument to enable maximum segment size
        (MSS) for virtual servers must be enabled.
  msslearninterval:
    type: float
    description:
      - Duration, in seconds, to sample the Maximum Segment Size (MSS) of the services.
        The Citrix ADC determines the best MSS to set for the virtual server based
        on this sampling. The argument to enable maximum segment size (MSS) for virtual
        servers must be enabled.
  nagle:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the Nagle algorithm on TCP connections.
  oooqsize:
    type: float
    description:
      - Maximum size of out-of-order packets queue. A value of 0 means no limit.
  pktperretx:
    type: int
    description:
      - Maximum limit on the number of packets that should be retransmitted on receiving
        a partial ACK.
  recvbuffsize:
    type: float
    description:
      - TCP Receive buffer size
  rfc5961chlgacklimit:
    type: float
    description:
      - Limits number of Challenge ACK sent per second, as recommended in RFC 5961(Improving
        TCP's Robustness to Blind In-Window Attacks)
  sack:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Selective ACKnowledgement (SACK).
  slowstartincr:
    type: int
    description:
      - Multiplier that determines the rate at which slow start increases the size
        of the TCP transmission window after each acknowledgement of successful transmission.
  synattackdetection:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Detect TCP SYN packet flood and send an SNMP trap.
  synholdfastgiveup:
    type: float
    description:
      - Maximum threshold. After crossing this threshold number of outstanding probes
        for origin, the Citrix ADC reduces the number of connection retries for probe
        connections.
  tcpfastopencookietimeout:
    type: float
    description:
      - Timeout in seconds after which a new TFO Key is computed for generating TFO
        Cookie. If zero, the same key is used always. If timeout is less than 120seconds,
        NS defaults to 120seconds timeout.
  tcpfintimeout:
    type: float
    description:
      - The amount of time in seconds, after which a TCP connnection in the TCP TIME-WAIT
        state is flushed.
  tcpmaxretries:
    type: float
    description:
      - Number of RTO's after which a connection should be freed.
  ws:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable window scaling.
  wsval:
    type: float
    description:
      - Factor used to calculate the new window size.
      - This argument is needed only when the window scaling is enabled.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nstcpparam playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nstcpparam
      delegate_to: localhost
      netscaler.adc.nstcpparam:
        state: present
        autosyncookietimeout: '100'
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
