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
---
module: service
short_description: Configuration for service resource.
description: Configuration for service resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  internal:
    type: bool
    description:
      - Display only dynamically learned services.
  accessdown:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use Layer 2 mode to bridge the packets sent to this service if it is marked
        as DOWN. If the service is DOWN, and this parameter is disabled, the packets
        are dropped.
  all:
    type: bool
    description:
      - Display both user-configured and dynamically learned services.
  appflowlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging of AppFlow information.
  cacheable:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use the transparent cache redirection virtual server to forward requests to
        the cache server.
      - 'Note: Do not specify this parameter if you set the Cache Type parameter.'
  cachetype:
    type: str
    choices:
      - TRANSPARENT
      - REVERSE
      - FORWARD
    description:
      - Cache type supported by the cache server.
  cip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Before forwarding a request to the service, insert an HTTP header with the
        client's IPv4 or IPv6 address as its value. Used if the server needs the client's
        IP address for security, accounting, or other purposes, and setting the Use
        Source IP parameter is not a viable option.
  cipheader:
    type: str
    description:
      - Name for the HTTP header whose value must be set to the IP address of the
        client. Used with the Client IP parameter. If you set the Client IP parameter,
        and you do not specify a name for the header, the appliance uses the header
        name specified for the global Client IP Header parameter (the cipHeader parameter
        in the set ns param CLI command or the Client IP Header parameter in the Configure
        HTTP Parameters dialog box at System > Settings > Change HTTP parameters).
        If the global Client IP Header parameter is not specified, the appliance inserts
        a header with the name "client-ip."
  cka:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable client keep-alive for the service.
  cleartextport:
    type: int
    description:
      - Port to which clear text data must be sent after the appliance decrypts incoming
        SSL traffic. Applicable to transparent SSL services.
  clttimeout:
    type: float
    description:
      - Time, in seconds, after which to terminate an idle client connection.
  cmp:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable compression for the service.
  comment:
    type: str
    description:
      - Any information about the service.
  contentinspectionprofilename:
    type: str
    description:
      - Name of the ContentInspection profile that contains IPS/IDS communication
        related setting for the service
  customserverid:
    type: str
    description:
      - Unique identifier for the service. Used when the persistency type for the
        virtual server is set to Custom Server ID.
  delay:
    type: float
    description:
      - Time, in seconds, allocated to the Citrix ADC for a graceful shutdown of the
        service. During this period, new requests are sent to the service only for
        clients who already have persistent sessions on the appliance. Requests from
        new clients are load balanced among other available services. After the delay
        time expires, no requests are sent to the service, and the service is marked
        as unavailable (OUT OF SERVICE).
  dnsprofilename:
    type: str
    description:
      - Name of the DNS profile to be associated with the service. DNS profile properties
        will applied to the transactions processed by a service. This parameter is
        valid only for ADNS, ADNS-TCP and ADNS-DOT services.
  downstateflush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with a service whose state transitions
        from UP to DOWN. Do not enable this option for applications that must complete
        their transactions.
  graceful:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Shut down gracefully, not accepting any new connections, and disabling the
        service when all of its connections are closed.
  hashid:
    type: float
    description:
      - A numerical identifier that can be used by hash based load balancing methods.
        Must be unique for each service.
  healthmonitor:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - 'Monitor the health of this service. Available settings function as follows:'
      - C(YES) - Send probes to check the health of the service.
      - C(NO) - Do not send probes to check the health of the service. With the C(NO)
        option, the appliance shows the service as UP at all times.
  httpprofilename:
    type: str
    description:
      - Name of the HTTP profile that contains HTTP configuration settings for the
        service.
  ip:
    type: str
    description:
      - IP to assign to the service.
  ipaddress:
    type: str
    description:
      - The new IP address of the service.
  maxbandwidth:
    type: float
    description:
      - Maximum bandwidth, in Kbps, allocated to the service.
  maxclient:
    type: float
    description:
      - Maximum number of simultaneous open connections to the service.
  maxreq:
    type: float
    description:
      - Maximum number of requests that can be sent on a persistent connection to
        the service.
      - 'Note: Connection requests beyond this value are rejected.'
  monconnectionclose:
    type: str
    choices:
      - RESET
      - FIN
    description:
      - Close monitoring connections by sending the service a connection termination
        message with the specified bit set.
  monitor_name_svc:
    type: str
    description:
      - Name of the monitor bound to the specified service.
  monthreshold:
    type: float
    description:
      - Minimum sum of weights of the monitors that are bound to this service. Used
        to determine whether to mark a service as UP or DOWN.
  name:
    type: str
    description:
      - Name for the service. Must begin with an ASCII alphabetic or underscore (_)
        character, and must contain only ASCII alphanumeric, underscore, hash (#),
        period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the service has been created.
  netprofile:
    type: str
    description:
      - Network profile to use for the service.
  newname:
    type: str
    description:
      - New name for the service. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  pathmonitor:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Path monitoring for clustering
  pathmonitorindv:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Individual Path monitoring decisions
  port:
    type: int
    description:
      - Port number of the service.
  processlocal:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option packets destined to a service in a cluster will
        not under go any steering. Turn this option for single packet request response
        mode or when the upstream device is performing a proper RSS for connection
        based distribution.
  quicprofilename:
    type: str
    description:
      - Name of QUIC profile which will be attached to the service.
  rtspsessionidremap:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable RTSP session ID mapping for the service.
  serverid:
    type: float
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
  servername:
    type: str
    description:
      - Name of the server that hosts the service.
  servicetype:
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
      - DOT
      - ADNS_DOT
      - HTTP_QUIC
    description:
      - Protocol in which data is exchanged with the service.
  sp:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable surge protection for the service.
  svrtimeout:
    type: float
    description:
      - Time, in seconds, after which to terminate an idle server connection.
  tcpb:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable TCP buffering for the service.
  tcpprofilename:
    type: str
    description:
      - Name of the TCP profile that contains TCP configuration settings for the service.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  useproxyport:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use the proxy port as the source port when initiating connections with the
        server. With the C(NO) setting, the client-side connection port is used as
        the source port for the server-side connection.
      - 'Note: This parameter is available only when the Use Source IP (USIP) parameter
        is set to C(YES).'
  usip:
    type: str
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
  weight:
    type: float
    description:
      - Weight to assign to the monitor-service binding. When a monitor is UP, the
        weight assigned to its binding with the service determines how much the monitor
        contributes toward keeping the health of the service above the value configured
        for the Monitor Threshold parameter.
  service_lbmonitor_binding:
    type: dict
    description: Bindings for service_lbmonitor_binding resource
    suboptions:
      mode:
        type: str
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
        type: str
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
        type: str
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
---
- name: Sample service playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure service
      delegate_to: localhost
      netscaler.adc.service:

        state: present
        name: nshttpd-vpn-127.0.0.1-81
        cip: ENABLED
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
