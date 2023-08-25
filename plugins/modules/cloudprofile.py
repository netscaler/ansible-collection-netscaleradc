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
module: cloudprofile
short_description: Configuration for cloud profile resource.
description: Configuration for cloud profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  azurepollperiod:
    description:
      - Azure polling period (in seconds)
    type: int
    default: 60
  azuretagname:
    description:
      - Azure tag name
    type: str
  azuretagvalue:
    description:
      - Azure tag value
    type: str
  boundservicegroupsvctype:
    choices:
      - HTTP
      - FTP
      - TCP
      - UDP
      - SSL
      - SSL_BRIDGE
      - SSL_TCP
      - DTLS
      - NNTP
      - RPCSVR
      - DNS
      - ADNS
      - SNMP
      - RTSP
      - DHCPRA
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - DNS_TCP
      - ADNS_TCP
      - MYSQL
      - MSSQL
      - ORACLE
      - MONGO
      - MONGO_TLS
      - RADIUS
      - RADIUSListener
      - RDP
      - DIAMETER
      - SSL_DIAMETER
      - TFTP
      - SMPP
      - PPTP
      - GRE
      - SYSLOGTCP
      - SYSLOGUDP
      - FIX
      - SSL_FIX
      - USER_TCP
      - USER_SSL_TCP
      - QUIC
      - IPFIX
      - LOGSTREAM
      - LOGSTREAM_SSL
      - MQTT
      - MQTT_TLS
      - QUIC_BRIDGE
    description:
      - The type of bound service
    type: str
  delay:
    description:
      - Time, in seconds, after which all the services configured on the server are
        disabled.
    type: int
  graceful:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
    type: str
    default: 'NO'
  ipaddress:
    description:
      - IPv4 or IPv6 address to assign to the virtual server.
    type: str
  name:
    description:
      - Name for the Cloud profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the profile is created.
    type: str
  port:
    description:
      - Port number for the virtual server.
    type: int
  servicegroupname:
    description:
      - servicegroups bind to this server
    type: str
  servicetype:
    choices:
      - HTTP
      - FTP
      - TCP
      - UDP
      - SSL
      - SSL_BRIDGE
      - SSL_TCP
      - DTLS
      - NNTP
      - DNS
      - DHCPRA
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - DNS_TCP
      - RTSP
      - PUSH
      - SSL_PUSH
      - RADIUS
      - RDP
      - MYSQL
      - MSSQL
      - DIAMETER
      - SSL_DIAMETER
      - TFTP
      - ORACLE
      - SMPP
      - SYSLOGTCP
      - SYSLOGUDP
      - FIX
      - SSL_FIX
      - PROXY
      - USER_TCP
      - USER_SSL_TCP
      - QUIC
      - IPFIX
      - LOGSTREAM
      - MONGO
      - MONGO_TLS
      - MQTT
      - MQTT_TLS
      - QUIC_BRIDGE
      - HTTP_QUIC
    description:
      - Protocol used by the service (also called the service type).
    type: str
  type:
    choices:
      - autoscale
      - azuretags
    description:
      - Type of cloud profile that you want to create, Vserver or based on Azure Tags
    type: str
  vservername:
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
    type: str
  vsvrbindsvcport:
    description:
      - The port number to be used for the bound service.
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
