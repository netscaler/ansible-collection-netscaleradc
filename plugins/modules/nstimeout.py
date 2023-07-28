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
module: nstimeout
short_description: Configuration for timeout resource.
description: Configuration for timeout resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  anyclient:
    description:
      - Global idle timeout, in seconds, for non-TCP client connections. This value
        is over ridden by the client timeout that is configured on individual entities.
    type: int
  anyserver:
    description:
      - Global idle timeout, in seconds, for non TCP server connections. This value
        is over ridden by the server timeout that is configured on individual entities.
    type: int
  anytcpclient:
    description:
      - Global idle timeout, in seconds, for TCP client connections. This value takes
        precedence over  entity level timeout settings (vserver/service). This is
        applicable only to transport protocol TCP.
    type: int
  anytcpserver:
    description:
      - Global idle timeout, in seconds, for TCP server connections. This value takes
        precedence over entity level timeout settings ( vserver/service). This is
        applicable only to transport protocol TCP.
    type: int
  client:
    description:
      - Client idle timeout (in seconds). If zero, the service-type default value
        is taken when service is created.
    type: int
  halfclose:
    description:
      - Idle timeout, in seconds, for connections that are in TCP half-closed state.
    type: int
    default: 10
  httpclient:
    description:
      - Global idle timeout, in seconds, for client connections of HTTP service type.
        This value is over ridden by the client timeout that is configured on individual
        entities.
    type: int
  httpserver:
    description:
      - Global idle timeout, in seconds, for server connections of HTTP service type.
        This value is over ridden by the server timeout that is configured on individual
        entities.
    type: int
  newconnidletimeout:
    description:
      - Timer interval, in seconds, for new TCP NATPCB connections on which no data
        was received.
    type: int
    default: 4
  nontcpzombie:
    description:
      - Interval at which the zombie clean-up process for non-TCP connections should
        run. Inactive IP NAT connections will be cleaned up.
    type: int
    default: 60
  reducedfintimeout:
    description:
      - Alternative idle timeout, in seconds, for closed TCP NATPCB connections.
    type: int
    default: 30
  reducedrsttimeout:
    description:
      - Timer interval, in seconds, for abruptly terminated TCP NATPCB connections.
    type: int
  server:
    description:
      - Server idle timeout (in seconds).  If zero, the service-type default value
        is taken when service is created.
    type: int
  tcpclient:
    description:
      - Global idle timeout, in seconds, for non-HTTP client connections of TCP service
        type. This value is over ridden by the client timeout that is configured on
        individual entities.
    type: int
  tcpserver:
    description:
      - Global idle timeout, in seconds, for non-HTTP server connections of TCP service
        type. This value is over ridden by the server timeout that is configured on
        entities.
    type: int
  zombie:
    description:
      - Interval, in seconds, at which the Citrix ADC zombie cleanup process must
        run. This process cleans up inactive TCP connections.
    type: int
    default: 120
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
