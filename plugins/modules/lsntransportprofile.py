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
module: lsntransportprofile
short_description: Configuration for LSN Transport Profile resource.
description: Configuration for LSN Transport Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  finrsttimeout:
    description:
      - Timeout, in seconds, for a TCP LSN session after a FIN or RST message is received
        from one of the endpoints.
      - ''
      - If a TCP LSN session is idle (after the Citrix ADC receives a FIN or RST message)
        for a time that exceeds this value, the Citrix ADC ADC removes the session.
      - ''
      - Since the LSN feature of the Citrix ADC does not maintain state information
        of any TCP LSN sessions, this timeout accommodates the transmission of the
        FIN or RST, and ACK messages from the other endpoint so that both endpoints
        can properly close the connection.
    type: int
    default: 30
  groupsessionlimit:
    description:
      - Maximum number of concurrent LSN sessions(for the specified protocol) allowed
        for all subscriber of a group to which this profile has bound. This limit
        will get split across the Citrix ADCs packet engines and rounded down. When
        the number of LSN sessions reaches the limit for a group in packet engine,
        the Citrix ADC does not allow the subscriber of that group to open additional
        sessions through that packet engine.
    type: int
  portpreserveparity:
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Enable port parity between a subscriber port and its mapped LSN NAT port.
        For example, if a subscriber initiates a connection from an odd numbered port,
        the Citrix ADC allocates an odd numbered LSN NAT port for this connection. '
      - You must set this parameter for proper functioning of protocols that require
        the source port to be even or odd numbered, for example, in peer-to-peer applications
        that use RTP or RTCP protocol.
    type: str
    default: DISABLED
  portpreserverange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If a subscriber initiates a connection from a well-known port (0-1023), allocate
        a NAT port from the well-known port range (0-1023) for this connection. For
        example, if a subscriber initiates a connection from port 80, the Citrix ADC
        can allocate port 100 as the NAT port for this connection.
      - ''
      - This parameter applies to dynamic NAT without port block allocation. It also
        applies to Deterministic NAT if the range of ports allocated includes well-known
        ports.
      - ''
      - When all the well-known ports of all the available NAT IP addresses are used
        in different subscriber's connections (LSN sessions), and a subscriber initiates
        a connection from a well-known port, the Citrix ADC drops this connection.
    type: str
    default: DISABLED
  portquota:
    description:
      - Maximum number of LSN NAT ports to be used at a time by each subscriber for
        the specified protocol. For example, each subscriber can be limited to a maximum
        of 500 TCP NAT ports. When the LSN NAT mappings for a subscriber reach the
        limit, the Citrix ADC does not allocate additional NAT ports for that subscriber.
    type: int
  sessionquota:
    description:
      - 'Maximum number of concurrent LSN sessions allowed for each subscriber for
        the specified protocol. '
      - When the number of LSN sessions reaches the limit for a subscriber, the Citrix
        ADC does not allow the subscriber to open additional sessions.
    type: int
  sessiontimeout:
    description:
      - Timeout, in seconds, for an idle LSN session. If an LSN session is idle for
        a time that exceeds this value, the Citrix ADC removes the session.
      - ''
      - This timeout does not apply for a TCP LSN session when a FIN or RST message
        is received from either of the endpoints.
    type: int
    default: 120
  stuntimeout:
    description:
      - STUN protocol timeout
    type: int
    default: 600
  syncheck:
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Silently drop any non-SYN packets for connections for which there is no LSN-NAT
        session present on the Citrix ADC. '
      - ''
      - 'If you disable this parameter, the Citrix ADC accepts any non-SYN packets
        and creates a new LSN session entry for this connection. '
      - ''
      - 'Following are some reasons for the Citrix ADC to receive such packets:'
      - ''
      - '* LSN session for a connection existed but the Citrix ADC removed this session
        because the LSN session was idle for a time that exceeded the configured session
        timeout.'
      - '* Such packets can be a part of a DoS attack.'
    type: str
    default: ENABLED
  synidletimeout:
    description:
      - SYN Idle timeout
    type: int
    default: 60
  transportprofilename:
    description:
      - 'Name for the LSN transport profile. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the LSN transport profile is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "lsn transport profile1" or ''lsn transport profile1'').'
    type: str
  transportprotocol:
    choices:
      - TCP
      - UDP
      - ICMP
    description:
      - Protocol for which to set the LSN transport profile parameters.
    type: str
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
