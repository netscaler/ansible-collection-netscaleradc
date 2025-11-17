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
module: vpnintranetapplication
short_description: Configuration for SSLVPN intranet application resource.
description: Configuration for SSLVPN intranet application resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
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
  clientapplication:
    type: list
    description:
      - Names of the client applications, such as PuTTY and Xshell.
    elements: str
  destip:
    type: str
    description:
      - Destination IP address, IP range, or host name of the intranet application.
        This address is the server IP address.
  destport:
    type: str
    description:
      - Destination TCP or UDP port number for the intranet application. Use a hyphen
        to specify a range of port numbers, for example 90-95.
  hostname:
    type: str
    description:
      - Name of the host for which to configure interception. The names are resolved
        during interception when users log on with the Citrix Gateway Plug-in.
  interception:
    type: str
    choices:
      - PROXY
      - TRANSPARENT
    description:
      - Interception mode for the intranet application or resource. Correct value
        depends on the type of client software used to make connections. If the interception
        mode is set to C(TRANSPARENT), users connect with the Citrix Gateway Plug-in
        for Windows. With the C(PROXY) setting, users connect with the Citrix Gateway
        Plug-in for Java.
  intranetapplication:
    type: str
    description:
      - Name of the intranet application.
  iprange:
    type: str
    description:
      - If you have multiple servers in your network, such as web, email, and file
        shares, configure an intranet application that includes the IP range for all
        the network applications. This allows users to access all the intranet applications
        contained in the IP address range.
  netmask:
    type: str
    description:
      - Destination subnet mask for the intranet application.
  protocol:
    type: str
    choices:
      - TCP
      - UDP
      - ANY
    description:
      - Protocol used by the intranet application. If protocol is set to BOTH, C(TCP)
        and C(UDP) traffic is allowed.
  spoofiip:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - IP address that the intranet application will use to route the connection
        through the virtual adapter.
  srcip:
    type: str
    description:
      - Source IP address. Required if interception mode is set to PROXY. Default
        is the loopback address, 127.0.0.1.
  srcport:
    type: int
    description:
      - Source port for the application for which the Citrix Gateway virtual server
        proxies the traffic. If users are connecting from a device that uses the Citrix
        Gateway Plug-in for Java, applications must be configured manually by using
        the source IP address and TCP port values specified in the intranet application
        profile. If a port value is not set, the destination port value is used.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample vpnintranetapplication playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vpnintranetapplication
      delegate_to: localhost
      netscaler.adc.vpnintranetapplication:
        state: present
        intranetapplication: intra_app21
        protocol: TCP
        destip: 10.100.0.57
        interception: PROXY
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
