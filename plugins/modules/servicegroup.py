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
module: servicegroup
short_description: Configuration for service group resource.
description: Configuration for service group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    description:
      - Enable logging of AppFlow information for the specified service group.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  autodisabledelay:
    description:
      - The time allowed (in seconds) for a graceful shutdown. During this period,
        new connections or requests will continue to be sent to this service for clients
        who already have a persistent session on the system. Connections or requests
        from fresh or new clients who do not yet have a persistence sessions on the
        system will not be sent to the service. Instead, they will be load balanced
        among other available services. After the delay time expires, no new requests
        or connections will be sent to the service.
    type: int
  autodisablegraceful:
    description:
      - Indicates graceful shutdown of the service. System will wait for all outstanding
        connections to this service to be closed before disabling the service.
    type: str
    choices:
      - true
      - false
  autoscale:
    description:
      - Auto scale option for a servicegroup
    type: str
    default: DISABLED
    choices:
      - DISABLED
      - DNS
      - POLICY
      - CLOUD
      - API
  cacheable:
    description:
      - Use the transparent cache redirection virtual server to forward the request
        to the cache server.
      - 'Note: Do not set this parameter if you set the Cache Type.'
    type: str
    choices:
      - true
      - false
  cachetype:
    description:
      - Cache type supported by the cache server.
    type: str
    choices:
      - TRANSPARENT
      - REVERSE
      - FORWARD
  cip:
    description:
      - Insert the Client IP header in requests forwarded to the service.
    type: str
    choices:
      - ENABLED
      - DISABLED
  cipheader:
    description:
      - Name of the HTTP header whose value must be set to the IP address of the client.
        Used with the Client IP parameter. If client IP insertion is enabled, and
        the client IP header is not specified, the value of Client IP Header parameter
        or the value set by the set ns config command is used as client's IP header
        name.
    type: str
  cka:
    description:
      - Enable client keep-alive for the service group.
    type: str
    choices:
      - true
      - false
  clttimeout:
    description:
      - Time, in seconds, after which to terminate an idle client connection.
    type: int
  cmp:
    description:
      - Enable compression for the specified service.
    type: str
    choices:
      - true
      - false
  comment:
    description:
      - Any information about the service group.
    type: str
  customserverid:
    description:
      - The identifier for this IP:Port pair. Used when the persistency type is set
        to Custom Server ID.
    type: str
    default: '"None"'
  dbsttl:
    description:
      - Specify the TTL for DNS record for domain based service.The default value
        of ttl is 0 which indicates to use the TTL received in DNS response for monitors
    type: int
  delay:
    description:
      - Time, in seconds, allocated for a shutdown of the services in the service
        group. During this period, new requests are sent to the service only for clients
        who already have persistent sessions on the appliance. Requests from new clients
        are load balanced among other available services. After the delay time expires,
        no requests are sent to the service, and the service is marked as unavailable
        (OUT OF SERVICE).
    type: int
  downstateflush:
    description:
      - Flush all active transactions associated with all the services in the service
        group whose state transitions from UP to DOWN. Do not enable this option for
        applications that must complete their transactions.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  dup_weight:
    description:
      - weight of the monitor that is bound to servicegroup.
    type: int
  graceful:
    description:
      - Wait for all existing connections to the service to terminate before shutting
        down the service.
    type: str
    choices:
      - true
      - false
  hashid:
    description:
      - The hash identifier for the service. This must be unique for each service.
        This parameter is used by hash based load balancing methods.
    type: int
  healthmonitor:
    description:
      - 'Monitor the health of this service.  Available settings function as follows:'
      - YES - Send probes to check the health of the service.
      - NO - Do not send probes to check the health of the service. With the NO option,
        the appliance shows the service as UP at all times.
    type: str
    default: true
    choices:
      - true
      - false
  httpprofilename:
    description:
      - Name of the HTTP profile that contains HTTP configuration settings for the
        service group.
    type: str
  includemembers:
    description:
      - Display the members of the listed service groups in addition to their settings.
        Can be specified when no service group name is provided in the command. In
        that case, the details displayed for each service group are identical to the
        details displayed when a service group name is provided, except that bound
        monitors are not displayed.
    type: bool
  maxbandwidth:
    description:
      - Maximum bandwidth, in Kbps, allocated for all the services in the service
        group.
    type: int
  maxclient:
    description:
      - Maximum number of simultaneous open connections for the service group.
    type: int
  maxreq:
    description:
      - 'Maximum number of requests that can be sent on a persistent connection to
        the service group. '
      - 'Note: Connection requests beyond this value are rejected.'
    type: int
  memberport:
    description:
      - member port
    type: int
  monconnectionclose:
    description:
      - Close monitoring connections by sending the service a connection termination
        message with the specified bit set.
    type: str
    default: NONE
    choices:
      - RESET
      - FIN
  monitor_name_svc:
    description:
      - Name of the monitor bound to the service group. Used to assign a weight to
        the monitor.
    type: str
  monthreshold:
    description:
      - Minimum sum of weights of the monitors that are bound to this service. Used
        to determine whether to mark a service as UP or DOWN.
    type: int
  nameserver:
    description:
      - Specify the nameserver to which the query for bound domain needs to be sent.
        If not specified, use the global nameserver
    type: str
  netprofile:
    description:
      - Network profile for the service group.
    type: str
  newname:
    description:
      - New name for the service group.
    type: str
  order:
    description:
      - Order number to be assigned to the servicegroup member
    type: int
  pathmonitor:
    description:
      - Path monitoring for clustering
    type: str
    choices:
      - true
      - false
  pathmonitorindv:
    description:
      - Individual Path monitoring decisions.
    type: str
    choices:
      - true
      - false
  port:
    description:
      - Server port number.
    type: int
  rtspsessionidremap:
    description:
      - Enable RTSP session ID mapping for the service group.
    type: str
    choices:
      - true
      - false
  serverid:
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
    type: int
  servername:
    description:
      - Name of the server to which to bind the service group.
    type: str
  servicegroupname:
    description:
      - Name of the service group. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the name is created.
    type: str
  servicetype:
    description:
      - Protocol used to exchange data with the service.
    type: str
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
  sp:
    description:
      - Enable surge protection for the service group.
    type: str
    choices:
      - true
      - false
  state:
    description:
      - Initial state of the service group.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  svrtimeout:
    description:
      - Time, in seconds, after which to terminate an idle server connection.
    type: int
  tcpb:
    description:
      - Enable TCP buffering for the service group.
    type: str
    choices:
      - true
      - false
  tcpprofilename:
    description:
      - Name of the TCP profile that contains TCP configuration settings for the service
        group.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  useproxyport:
    description:
      - 'Use the proxy port as the source port when initiating connections with the
        server. With the NO setting, the client-side connection port is used as the
        source port for the server-side connection. '
      - 'Note: This parameter is available only when the Use Source IP (USIP) parameter
        is set to YES.'
    type: str
    choices:
      - true
      - false
  usip:
    description:
      - Use client's IP address as the source IP address when initiating connection
        to the server. With the NO setting, which is the default, a mapped IP (MIP)
        address or subnet IP (SNIP) address is used as the source IP address to initiate
        server side connections.
    type: str
    choices:
      - true
      - false
  weight:
    description:
      - Weight to assign to the servers in the service group. Specifies the capacity
        of the servers relative to the other servers in the load balancing configuration.
        The higher the weight, the higher the percentage of requests sent to the service.
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
