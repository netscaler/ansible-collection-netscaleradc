#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: vpnintranetapplication
short_description: Configuration for SSLVPN intranet application resource.
description: Configuration for SSLVPN intranet application resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  clientapplication:
    description:
      - Names of the client applications, such as PuTTY and Xshell.
    type: list
    elements: str
  destip:
    description:
      - Destination IP address, IP range, or host name of the intranet application.
        This address is the server IP address.
    type: str
  destport:
    description:
      - Destination TCP or UDP port number for the intranet application. Use a hyphen
        to specify a range of port numbers, for example 90-95.
    type: str
  hostname:
    description:
      - Name of the host for which to configure interception. The names are resolved
        during interception when users log on with the Citrix Gateway Plug-in.
    type: str
  interception:
    choices:
      - PROXY
      - TRANSPARENT
    description:
      - Interception mode for the intranet application or resource. Correct value
        depends on the type of client software used to make connections. If the interception
        mode is set to C(TRANSPARENT), users connect with the Citrix Gateway Plug-in
        for Windows. With the C(PROXY) setting, users connect with the Citrix Gateway
        Plug-in for Java.
    type: str
  intranetapplication:
    description:
      - Name of the intranet application.
    type: str
  iprange:
    description:
      - If you have multiple servers in your network, such as web, email, and file
        shares, configure an intranet application that includes the IP range for all
        the network applications. This allows users to access all the intranet applications
        contained in the IP address range.
    type: str
  netmask:
    description:
      - Destination subnet mask for the intranet application.
    type: str
  protocol:
    choices:
      - TCP
      - UDP
      - ANY
    description:
      - Protocol used by the intranet application. If protocol is set to BOTH, C(TCP)
        and C(UDP) traffic is allowed.
    type: str
  spoofiip:
    choices:
      - true
      - false
    description:
      - IP address that the intranet application will use to route the connection
        through the virtual adapter.
    type: str
    default: true
  srcip:
    description:
      - Source IP address. Required if interception mode is set to PROXY. Default
        is the loopback address, 127.0.0.1.
    type: str
  srcport:
    description:
      - Source port for the application for which the Citrix Gateway virtual server
        proxies the traffic. If users are connecting from a device that uses the Citrix
        Gateway Plug-in for Java, applications must be configured manually by using
        the source IP address and TCP port values specified in the intranet application
        profile. If a port value is not set, the destination port value is used.
    type: int
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
