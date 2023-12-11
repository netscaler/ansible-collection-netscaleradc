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
module: nsparam
short_description: Configuration for Citrix ADC parameters resource.
description: Configuration for Citrix ADC parameters resource.
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
  advancedanalyticsstats:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Disable/Enable advanace analytics stats
    default: DISABLED
  aftpallowrandomsourceport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow the FTP server to come from a random source port for active FTP data
        connections
    default: DISABLED
  cip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the insertion of the actual client IP address into the HTTP
        header request passed from the client to one, some, or all servers attached
        to the system. The passed address can then be accessed through a minor modification
        to the server.
      - '* If the CIP header is specified, it will be used as the client IP header.'
      - '* If the CIP header is not specified, the value that has been set will be
        used as the client IP header.'
  cipheader:
    type: str
    description:
      - Text that will be used as the client IP address header.
  cookieversion:
    type: str
    choices:
      - '0'
      - '1'
    description:
      - Version of the cookie inserted by the system.
  crportrange:
    type: str
    description:
      - Port range for cache redirection services.
  exclusivequotamaxclient:
    type: float
    description:
      - Percentage of maxClient to be given to PEs.
    default: 80
  exclusivequotaspillover:
    type: float
    description:
      - Percentage of maximum limit to be given to PEs.
    default: 80
  ftpportrange:
    type: str
    description:
      - Minimum and maximum port (port range) that FTP services are allowed to use.
  grantquotamaxclient:
    type: float
    description:
      - Percentage of shared quota to be granted at a time for maxClient.
    default: 10
  grantquotaspillover:
    type: float
    description:
      - Percentage of shared quota to be granted at a time for spillover.
    default: 10
  httpport:
    type: list
    description:
      - HTTP ports on the web server. This allows the system to perform connection
        off-load for any client request that has a destination port matching one of
        these configured ports.
    elements: int
  icaports:
    type: list
    description:
      - The ICA ports on the Web server. This allows the system to perform connection
        off-load for any
      - '                      client request that has a destination port matching
        one of these configured ports.'
    elements: int
  internaluserlogin:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enables/disables the internal user from logging in to the appliance. Before
        disabling internal user login, you must have key-based authentication set
        up on the appliance. The file name for the key pair must be "ns_comm_key".
    default: ENABLED
  ipttl:
    type: float
    description:
      - Set the IP Time to Live (TTL) and Hop Limit value for all outgoing packets
        from Citrix ADC.
    default: 255
  maxconn:
    type: float
    description:
      - Maximum number of connections that will be made from the appliance to the
        web server(s) attached to it. The value entered here is applied globally to
        all attached servers.
  maxreq:
    type: float
    description:
      - Maximum number of requests that the system can pass on a particular connection
        between the appliance and a server attached to it. Setting this value to 0
        allows an unlimited number of requests to be passed. This value is overridden
        by the maximum number of requests configured on the individual service.
  mgmthttpport:
    type: int
    description:
      - This allow the configuration of management HTTP port.
    default: 80
  mgmthttpsport:
    type: int
    description:
      - This allows the configuration of management HTTPS port.
    default: 443
  pmtumin:
    type: float
    description:
      - Minimum path MTU value that Citrix ADC will process in the ICMP fragmentation
        needed message. If the ICMP message contains a value less than this value,
        then this value is used instead.
    default: 576
  pmtutimeout:
    type: float
    description:
      - Interval, in minutes, for flushing the PMTU entries.
    default: 10
  proxyprotocol:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Disable/Enable v1 or v2 proxy protocol header for client info insertion
    default: DISABLED
  securecookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable secure flag for persistence cookie.
    default: ENABLED
  secureicaports:
    type: list
    description:
      - The Secure ICA ports on the Web server. This allows the system to perform
        connection off-load for any
      - '            client request that has a destination port matching one of these
        configured ports.'
    elements: int
  servicepathingressvlan:
    type: float
    description:
      - VLAN on which the subscriber traffic arrives on the appliance.
  tcpcip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the insertion of the client TCP/IP header in TCP payload
        passed from the client to one, some, or all servers attached to the system.
        The passed address can then be accessed through a minor modification to the
        server.
    default: DISABLED
  timezone:
    type: str
    description:
      - Time zone for the Citrix ADC. Name of the time zone should be specified as
        argument.
    default: CoordinatedUniversalTime
  useproxyport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable use_proxy_port setting
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
