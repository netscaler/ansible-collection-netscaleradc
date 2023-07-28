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
module: quicprofile
short_description: Configuration for QUIC profile resource.
description: Configuration for QUIC profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ackdelayexponent:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        indicating an exponent that the remote QUIC endpoint should use, to decode
        the ACK Delay field in QUIC ACK frames sent by the Citrix ADC.
    type: int
    default: 3
  activeconnectionidlimit:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the maximum number of QUIC connection IDs from the remote QUIC
        endpoint, that the Citrix ADC is willing to store.
    type: int
    default: 3
  activeconnectionmigration:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Specify whether the Citrix ADC should allow the remote QUIC endpoint to perform
        active QUIC connection migration.
    type: str
    default: ENABLED
  congestionctrlalgorithm:
    choices:
      - Default
      - NewReno
      - CUBIC
      - BBR
    description:
      - Specify the congestion control algorithm to be used for QUIC connections.
        The default congestion control algorithm is C(CUBIC).
    type: str
    default: Default
  initialmaxdata:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial value, in bytes, for the maximum amount of data that
        can be sent on a QUIC connection.
    type: int
    default: 1048576
  initialmaxstreamdatabidilocal:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial flow control limit, in bytes, for bidirectional QUIC
        streams initiated by the Citrix ADC.
    type: int
    default: 262144
  initialmaxstreamdatabidiremote:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial flow control limit, in bytes, for bidirectional QUIC
        streams initiated by the remote QUIC endpoint.
    type: int
    default: 262144
  initialmaxstreamdatauni:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial flow control limit, in bytes, for unidirectional streams
        initiated by the remote QUIC endpoint.
    type: int
    default: 262144
  initialmaxstreamsbidi:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial maximum number of bidirectional streams the remote
        QUIC endpoint may initiate.
    type: int
    default: 100
  initialmaxstreamsuni:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the initial maximum number of unidirectional streams the remote
        QUIC endpoint may initiate.
    type: int
    default: 10
  maxackdelay:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the maximum amount of time, in milliseconds, by which the Citrix
        ADC will delay sending acknowledgments.
    type: int
    default: 20
  maxidletimeout:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the maximum idle timeout, in seconds, for a QUIC connection. A
        QUIC connection will be silently discarded by the Citrix ADC if it remains
        idle for longer than the minimum of the idle timeout values advertised by
        the Citrix ADC and the remote QUIC endpoint, and three times the current Probe
        Timeout (PTO).
    type: int
    default: 180
  maxudpdatagramsperburst:
    description:
      - An integer value, specifying the maximum number of UDP datagrams that can
        be transmitted by the Citrix ADC in a single transmission burst on a QUIC
        connection.
    type: int
    default: 8
  maxudppayloadsize:
    description:
      - An integer value advertised by the Citrix ADC to the remote QUIC endpoint,
        specifying the size of the largest UDP datagram payload, in bytes, that the
        Citrix ADC is willing to receive on a QUIC connection.
    type: int
    default: 1472
  name:
    description:
      - Name for the QUIC profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-)
        characters. Cannot be changed after the profile is created.
    type: str
  newtokenvalidityperiod:
    description:
      - An integer value, specifying the validity period, in seconds, of address validation
        tokens issued through QUIC NEW_TOKEN frames sent by the Citrix ADC.
    type: int
    default: 300
  retrytokenvalidityperiod:
    description:
      - An integer value, specifying the validity period, in seconds, of address validation
        tokens issued through QUIC Retry packets sent by the Citrix ADC.
    type: int
    default: 10
  statelessaddressvalidation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Specify whether the Citrix ADC should perform stateless address validation
        for QUIC clients, by sending tokens in QUIC Retry packets during QUIC connection
        establishment, and by sending tokens in QUIC NEW_TOKEN frames after QUIC connection
        establishment.
    type: str
    default: ENABLED
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
