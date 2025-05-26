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
module: nstimeout
short_description: Configuration for timeout resource.
description: Configuration for timeout resource.
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
  anyclient:
    type: float
    description:
      - Global idle timeout, in seconds, for non-TCP client connections. This value
        is over ridden by the client timeout that is configured on individual entities.
  anyserver:
    type: float
    description:
      - Global idle timeout, in seconds, for non TCP server connections. This value
        is over ridden by the server timeout that is configured on individual entities.
  anytcpclient:
    type: float
    description:
      - Global idle timeout, in seconds, for TCP client connections. This value takes
        precedence over  entity level timeout settings (vserver/service). This is
        applicable only to transport protocol TCP.
  anytcpserver:
    type: float
    description:
      - Global idle timeout, in seconds, for TCP server connections. This value takes
        precedence over entity level timeout settings ( vserver/service). This is
        applicable only to transport protocol TCP.
  client:
    type: float
    description:
      - Client idle timeout (in seconds). If zero, the service-type default value
        is taken when service is created.
  halfclose:
    type: float
    description:
      - Idle timeout, in seconds, for connections that are in TCP half-closed state.
  httpclient:
    type: float
    description:
      - Global idle timeout, in seconds, for client connections of HTTP service type.
        This value is over ridden by the client timeout that is configured on individual
        entities.
  httpserver:
    type: float
    description:
      - Global idle timeout, in seconds, for server connections of HTTP service type.
        This value is over ridden by the server timeout that is configured on individual
        entities.
  newconnidletimeout:
    type: float
    description:
      - Timer interval, in seconds, for new TCP NATPCB connections on which no data
        was received.
  nontcpzombie:
    type: float
    description:
      - Interval at which the zombie clean-up process for non-TCP connections should
        run. Inactive IP NAT connections will be cleaned up.
  reducedfintimeout:
    type: float
    description:
      - Alternative idle timeout, in seconds, for closed TCP NATPCB connections.
  reducedrsttimeout:
    type: float
    description:
      - Timer interval, in seconds, for abruptly terminated TCP NATPCB connections.
  server:
    type: float
    description:
      - Server idle timeout (in seconds).  If zero, the service-type default value
        is taken when service is created.
  tcpclient:
    type: float
    description:
      - Global idle timeout, in seconds, for non-HTTP client connections of TCP service
        type. This value is over ridden by the client timeout that is configured on
        individual entities.
  tcpserver:
    type: float
    description:
      - Global idle timeout, in seconds, for non-HTTP server connections of TCP service
        type. This value is over ridden by the server timeout that is configured on
        entities.
  zombie:
    type: float
    description:
      - Interval, in seconds, at which the Citrix ADC zombie cleanup process must
        run. This process cleans up inactive TCP connections.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample nstimeout playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure nstimeout
      delegate_to: localhost
      netscaler.adc.nstimeout:
        state: present
        newconnidletimeout: '25'
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
