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
module: service
short_description: Configuration for service resource.
description: Configuration for service resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  Internal:
    description:
      - Display only dynamically learned services.
    type: bool
  accessdown:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use Layer 2 mode to bridge the packets sent to this service if it is marked
        as DOWN. If the service is DOWN, and this parameter is disabled, the packets
        are dropped.
    type: str
    default: 'NO'
  all:
    description:
      - Display both user-configured and dynamically learned services.
    type: bool
  appflowlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging of AppFlow information.
    type: str
    default: ENABLED
  cacheable:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use the transparent cache redirection virtual server to forward requests to
        the cache server.
      - 'Note: Do not specify this parameter if you set the Cache Type parameter.'
    type: str
    default: 'NO'
  cachetype:
    choices:
      - TRANSPARENT
      - REVERSE
      - FORWARD
    description:
      - Cache type supported by the cache server.
    type: str
  cip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Before forwarding a request to the service, insert an HTTP header with the
        client's IPv4 or IPv6 address as its value. Used if the server needs the client's
        IP address for security, accounting, or other purposes, and setting the Use
        Source IP parameter is not a viable option.
    type: str
  cipheader:
    description:
      - Name for the HTTP header whose value must be set to the IP address of the
        client. Used with the Client IP parameter. If you set the Client IP parameter,
        and you do not specify a name for the header, the appliance uses the header
        name specified for the global Client IP Header parameter (the cipHeader parameter
        in the set ns param CLI command or the Client IP Header parameter in the Configure
        HTTP Parameters dialog box at System > Settings > Change HTTP parameters).
        If the global Client IP Header parameter is not specified, the appliance inserts
        a header with the name "client-ip."
    type: str
  cka:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable client keep-alive for the service.
    type: str
  cleartextport:
    description:
      - Port to which clear text data must be sent after the appliance decrypts incoming
        SSL traffic. Applicable to transparent SSL services.
    type: int
  clttimeout:
    description:
      - Time, in seconds, after which to terminate an idle client connection.
    type: int
  cmp:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable compression for the service.
    type: str
  comment:
    description:
      - Any information about the service.
    type: str
  contentinspectionprofilename:
    description:
      - Name of the ContentInspection profile that contains IPS/IDS communication
        related setting for the service
    type: str
  customserverid:
    description:
      - Unique identifier for the service. Used when the persistency type for the
        virtual server is set to Custom Server ID.
    type: str
    default: '"None"'
  delay:
    description:
      - Time, in seconds, allocated to the Citrix ADC for a graceful shutdown of the
        service. During this period, new requests are sent to the service only for
        clients who already have persistent sessions on the appliance. Requests from
        new clients are load balanced among other available services. After the delay
        time expires, no requests are sent to the service, and the service is marked
        as unavailable (OUT OF SERVICE).
    type: int
  dnsprofilename:
    description:
      - Name of the DNS profile to be associated with the service. DNS profile properties
        will applied to the transactions processed by a service. This parameter is
        valid only for ADNS and ADNS-TCP services.
    type: str
  downstateflush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with a service whose state transitions
        from UP to DOWN. Do not enable this option for applications that must complete
        their transactions.
    type: str
    default: ENABLED
  graceful:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Shut down gracefully, not accepting any new connections, and disabling the
        service when all of its connections are closed.
    type: str
    default: 'NO'
  hashid:
    description:
      - A numerical identifier that can be used by hash based load balancing methods.
        Must be unique for each service.
    type: int
  healthmonitor:
    choices:
      - 'YES'
      - 'NO'
    description:
      - 'Monitor the health of this service. Available settings function as follows:'
      - C(YES) - Send probes to check the health of the service.
      - C(NO) - Do not send probes to check the health of the service. With the C(NO)
        option, the appliance shows the service as UP at all times.
    type: str
    default: 'YES'
  httpprofilename:
    description:
      - Name of the HTTP profile that contains HTTP configuration settings for the
        service.
    type: str
  ip:
    description:
      - IP to assign to the service.
    type: str
  ipaddress:
    description:
      - The new IP address of the service.
    type: str
  maxbandwidth:
    description:
      - Maximum bandwidth, in Kbps, allocated to the service.
    type: int
  maxclient:
    description:
      - Maximum number of simultaneous open connections to the service.
    type: int
  maxreq:
    description:
      - 'Maximum number of requests that can be sent on a persistent connection to
        the service. '
      - 'Note: Connection requests beyond this value are rejected.'
    type: int
  monconnectionclose:
    choices:
      - RESET
      - FIN
    description:
      - Close monitoring connections by sending the service a connection termination
        message with the specified bit set.
    type: str
    default: NONE
  monitor_name_svc:
    description:
      - Name of the monitor bound to the specified service.
    type: str
  monthreshold:
    description:
      - Minimum sum of weights of the monitors that are bound to this service. Used
        to determine whether to mark a service as UP or DOWN.
    type: int
  name:
    description:
      - Name for the service. Must begin with an ASCII alphabetic or underscore (_)
        character, and must contain only ASCII alphanumeric, underscore, hash (#),
        period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the service has been created.
    type: str
  netprofile:
    description:
      - Network profile to use for the service.
    type: str
  newname:
    description:
      - New name for the service. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
    type: str
  pathmonitor:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Path monitoring for clustering
    type: str
  pathmonitorindv:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Individual Path monitoring decisions
    type: str
  port:
    description:
      - Port number of the service.
    type: int
  processlocal:
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option packets destined to a service in a cluster will
        not under go any steering. Turn this option for single packet request response
        mode or when the upstream device is performing a proper RSS for connection
        based distribution.
    type: str
    default: DISABLED
  rtspsessionidremap:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable RTSP session ID mapping for the service.
    type: str
    default: 'OFF'
  serverid:
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
    type: int
  servername:
    description:
      - Name of the server that hosts the service.
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
      - Protocol in which data is exchanged with the service.
    type: str
  sp:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable surge protection for the service.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Initial state of the service.
    type: str
    default: ENABLED
  svrtimeout:
    description:
      - Time, in seconds, after which to terminate an idle server connection.
    type: int
  tcpb:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable TCP buffering for the service.
    type: str
  tcpprofilename:
    description:
      - Name of the TCP profile that contains TCP configuration settings for the service.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  useproxyport:
    choices:
      - 'YES'
      - 'NO'
    description:
      - 'Use the proxy port as the source port when initiating connections with the
        server. With the C(NO) setting, the client-side connection port is used as
        the source port for the server-side connection. '
      - 'Note: This parameter is available only when the Use Source IP (USIP) parameter
        is set to C(YES).'
    type: str
  usip:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use the client's IP address as the source IP address when initiating a connection
        to the server. When creating a service, if you do not set this parameter,
        the service inherits the global Use Source IP setting (available in the enable
        ns mode and disable ns mode CLI commands, or in the System > Settings > Configure
        modes > Configure Modes dialog box). However, you can override this setting
        after you create the service.
    type: str
  weight:
    description:
      - Weight to assign to the monitor-service binding. When a monitor is UP, the
        weight assigned to its binding with the service determines how much the monitor
        contributes toward keeping the health of the service above the value configured
        for the Monitor Threshold parameter.
    type: int
  service_lbmonitor_binding:
    type: dict
    description: Bindings for service_lbmonitor_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  servicegroup_lbmonitor_binding:
    type: dict
    description: Bindings for servicegroup_lbmonitor_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  servicegroup_servicegroupmember_binding:
    type: dict
    description: Bindings for servicegroup_servicegroupmember_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
