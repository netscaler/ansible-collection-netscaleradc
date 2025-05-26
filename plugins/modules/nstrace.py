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
module: nstrace
short_description: Configuration for nstrace operations resource.
description: Configuration for nstrace operations resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
  capdroppkt:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Captures Dropped Packets if set to C(ENABLED).
  capsslkeys:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Capture SSL Master keys. Master keys will not be captured on FIPS machine.
      - '                Warning: The captured keys can be used to decrypt information
        that may be confidential. The captured key files have to be stored in a secure
        environment'
  doruntimecleanup:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable runtime temp file cleanup
  fileid:
    type: str
    description:
      - ID for the trace file name for uniqueness. Should be used only with -name
        option.
  filename:
    type: str
    description:
      - Name of the trace file.
  filesize:
    type: float
    description:
      - File size, in MB, treshold for rollover. If free disk space is less than 2GB
        at the time of rollover, trace will stop
  filter:
    type: str
    description:
      - 'Filter expression for nstrace. Maximum length of filter is 255 and it can
        be of following format:'
      - '     <expression> [<relop> <expression>]'
      - ''
      - '     <relop> = ( && | || )'
      - ''
      - '     <expression> =:'
      - '     CONNECTION.<qualifier>.<qualifier-method>.(<qualifier-value>)'
      - ''
      - '     <qualifier> = SRCIP'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv4 address.'
      - '     example = CONNECTION.SRCIP.EQ(127.0.0.1)'
      - ''
      - '     <qualifier> = DSTIP'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv4 address.'
      - '     example = CONNECTION.DSTIP.EQ(127.0.0.1)'
      - ''
      - '     <qualifier> = IP'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv4 address.'
      - '     example = CONNECTION.IP.EQ(127.0.0.1)'
      - ''
      - '     <qualifier> = SRCIPv6'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv6 address.'
      - '     example = CONNECTION.SRCIPv6.EQ(2001:db8:0:0:1::1)'
      - ''
      - '     <qualifier> = DSTIPv6'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv6 address.'
      - '     example = CONNECTION.DSTIPv6.EQ(2001:db8:0:0:1::1)'
      - ''
      - '     <qualifier> = IPv6'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = A valid IPv6 address.'
      - '     example = CONNECTION.IPv6.EQ(2001:db8:0:0:1::1)'
      - ''
      - '     <qualifier> = SRCPORT'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid port number.'
      - '     example = CONNECTION.SRCPORT.EQ(80)'
      - ''
      - '     <qualifier> = DSTPORT'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid port number.'
      - '     example = CONNECTION.DSTPORT.EQ(80)'
      - ''
      - '     <qualifier> = PORT'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid port number.'
      - '     example = CONNECTION.PORT.EQ(80)'
      - ''
      - '     <qualifier> = VLANID'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid VLAN ID.'
      - '     example = CONNECTION.VLANID.EQ(0)'
      - ''
      - '     <qualifier> = CONNID'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid PCB dev number.'
      - '     example = CONNECTION.CONNID.EQ(0)'
      - ''
      - '     <qualifier> = PPEID'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid core ID.'
      - '       example = CONNECTION.PPEID.EQ(0)'
      - ''
      - '     <qualifier> = SVCNAME'
      - '     <qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH'
      - '                         | ENDSWITH ]'
      - '     <qualifier-value>  = A valid text string.'
      - '     example = CONNECTION.SVCNAME.EQ("name")'
      - ''
      - '     <qualifier> = LB_VSERVER.NAME'
      - '     <qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH'
      - '                        | ENDSWITH ]'
      - '     <qualifier-value>  = LB vserver name.'
      - '     example = CONNECTION.LB_VSERVER.NAME.EQ("name")'
      - ''
      - '     <qualifier> = CS_VSERVER.NAME'
      - '     <qualifier-method> = [ EQ | NE | CONTAINS | STARTSWITH'
      - '                        | ENDSWITH ]'
      - '     <qualifier-value>  = CS vserver name.'
      - '     example = CONNECTION.CS_VSERVER.NAME.EQ("name")'
      - ''
      - '     <qualifier> = INTF'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  =  A valid interface id in the'
      - '                    form of x/y.'
      - '     example = CONNECTION.INTF.EQ("x/y")'
      - ''
      - '     <qualifier> = SERVICE_TYPE'
      - '     <qualifier-method> = [ EQ | NE ]'
      - '     <qualifier-value>  = ( SVC_HTTP | FTP | TCP | UDP | SSL |'
      - '        SSL_BRIDGE | SSL_TCP | NNTP | RPCSVR | RPCSVRS |'
      - '        RPCCLNT | SVC_DNS | ADNS | SNMP | RTSP | DHCPRA | ANY|'
      - '        MONITOR | MONITOR_UDP | MONITOR_PING | SIP_UDP |'
      - '        SVC_MYSQL | SVC_MSSQL | FIX | SSL_FIX | PKTSTEER |'
      - '        SVC_AAA | SERVICE_UNKNOWN )'
      - '     example = CONNECTION.SERVICE_TYPE.EQ(ANY)'
      - ''
      - '     <qualifier> = TRAFFIC_DOMAIN_ID'
      - '     <qualifier-method> = [ EQ | NE | GT | GE | LT | LE'
      - '                         | BETWEEN ]'
      - '     <qualifier-value>  = A valid traffic domain ID.'
      - '     example = CONNECTION.TRAFFIC_DOMAIN_ID.EQ(0)'
      - ''
      - '     eg: start nstrace -filter "CONNECTION.SRCIP.EQ(127.0.0.1) || (CONNECTION.SVCNAME.NE("s1")
        && CONNECTION.SRCPORT.EQ(80))"'
      - '     The filter expression should be given in double quotes.'
      - ''
      - 'common use cases:'
      - ''
      - Trace capturing full sized traffic from/to ip 10.102.44.111, excluding loopback
        traffic
      - start nstrace -size 0 -filter "CONNECTION.IP.NE(127.0.0.1) && CONNECTION.IP.EQ(10.102.44.111)"
      - ''
      - Trace capturing all traffic to (terminating at) port 80 or 443
      - start nstrace -size 0 -filter "CONNECTION.DSTPORT.EQ(443) || CONNECTION.DSTPORT.EQ(80)"
      - ''
      - Trace capturing all backend traffic specific to service service1 along with
        corresponding client side traffic
      - start nstrace -size 0 -filter "CONNECTION.SVCNAME.EQ("service1")" -link ENABLED
      - ''
      - Trace capturing all traffic through NetScaler interface 1/1
      - start nstrace -filter "CONNECTION.INTF.EQ("1/1")"
      - ''
      - Trace capturing all traffic specific through vlan 2
      - start nstrace -filter "CONNECTION.VLANID.EQ(2)"
      - ''
      - Trace capturing all frontend (client side) traffic specific to lb vserver
        vserver1 along with corresponding server side traffic
      - start nstrace -size 0 -filter "CONNECTION.LB_VSERVER.NAME.EQ("vserver1")"
        -link ENABLED
  inmemorytrace:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Logs packets in appliance's memory and dumps the trace file on stopping the
        nstrace operation
  link:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Includes filtered connection's peer traffic.
  merge:
    type: str
    choices:
      - ONSTOP
      - ONTHEFLY
      - NOMERGE
    description:
      - Specify how traces across PE's are merged
  mode:
    type: list
    choices:
      - TX
      - TXB
      - RX
      - IPV6
      - NEW_RX
      - C2C
      - NS_FR_TX
      - APPFW
      - MPTCP
      - PolicyBased
      - HTTP_QUIC
    description:
      - 'Capturing mode for trace. Mode can be any of the following values or combination
        of these values:'
      - '      C(RX)          Received packets before NIC pipelining (Filter does
        not work when C(RX) capturing mode is ON)'
      - '      C(NEW_RX)      Received packets after NIC pipelining'
      - '      C(TX)          Transmitted packets'
      - '      C(TXB)         Packets buffered for transmission'
      - '      C(IPV6)        Translated IPv6 packets'
      - '      C(C2C)         Capture C(C2C) message'
      - '      C(NS_FR_TX)    C(TX)/C(TXB) packets are not captured in flow receiver.'
      - '      C(MPTCP)       C(MPTCP) master flow'
      - '      C(HTTP_QUIC)   HTTP-over-QUIC stream data and stream events'
      - '      Default mode: C(NEW_RX) C(TXB)'
    elements: str
  nf:
    type: float
    description:
      - Number of files to be generated in cycle.
  nodeid:
    type: float
    description:
      - Unique number that identifies the cluster node.
  nodes:
    type: list
    description:
      - Nodes on which tracing is started.
    elements: int
  pernic:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use separate trace files for each interface. Works only with cap format.
  size:
    type: float
    description:
      - Size of the captured data. Set 0 for full packet trace.
  skiplocalssh:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - skip local SSH packets
  skiprpc:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - skip RPC packets
  time:
    type: float
    description:
      - Time per file (sec).
  tracebuffers:
    type: float
    description:
      - Number of 16KB trace buffers
  traceformat:
    type: str
    choices:
      - NSCAP
      - PCAP
    description:
      - Format in which trace will be generated
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
