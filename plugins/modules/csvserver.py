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
module: csvserver
short_description: Configuration for CS virtual server resource.
description: Configuration for CS virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    description:
      - Enable logging appflow flow information
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  authentication:
    description:
      - Authenticate users who request a connection to the content switching virtual
        server.
    type: str
    choices:
      - true
      - false
  authenticationhost:
    description:
      - FQDN of the authentication virtual server. The service type of the virtual
        server should be either HTTP or SSL.
    type: str
  authn401:
    description:
      - Enable HTTP 401-response based authentication.
    type: str
    choices:
      - true
      - false
  authnprofile:
    description:
      - Name of the authentication profile to be used when authentication is turned
        on.
    type: str
  authnvsname:
    description:
      - Name of authentication virtual server that authenticates the incoming user
        requests to this content switching virtual server.
    type: str
  backupip:
    description:
      - '0'
    type: str
  backuppersistencetimeout:
    description:
      - Time period for which backup persistence is in effect.
    type: int
    default: 2
  backupvserver:
    description:
      - Name of the backup virtual server that you are configuring. Must begin with
        an ASCII alphanumeric or underscore (_) character, and must contain only ASCII
        alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign
        (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup
        virtual server is created. You can assign a different backup virtual server
        or rename the existing virtual server.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks.
    type: str
  cacheable:
    description:
      - Use this option to specify whether a virtual server, used for load balancing
        or content switching, routes requests to the cache redirection virtual server
        before sending it to the configured servers.
    type: str
    choices:
      - true
      - false
  casesensitive:
    description:
      - Consider case in URLs (for policies that use URLs instead of RULES). For example,
        with the ON setting, the URLs /a/1.html and /A/1.HTML are treated differently
        and can have different targets (set by content switching policies). With the
        OFF setting, /a/1.html and /A/1.HTML are switched to the same target.
    type: str
    default: true
    choices:
      - true
      - false
  clttimeout:
    description:
      - 'Idle time, in seconds, after which the client connection is terminated. The
        default values are:'
      - 180 seconds for HTTP/SSL-based services.
      - 9000 seconds for other TCP-based services.
      - 120 seconds for DNS-based services.
      - 120 seconds for other UDP-based services.
    type: int
  comment:
    description:
      - Information about this virtual server.
    type: str
  cookiedomain:
    description:
      - '0'
    type: str
  cookiename:
    description:
      - Use this parameter to  specify the cookie name for COOKIE peristence type.
        It specifies the name of cookie with a maximum of 32 characters. If not specified,
        cookie name is internally generated.
    type: str
  cookietimeout:
    description:
      - '0'
    type: int
  dbprofilename:
    description:
      - Name of the DB profile.
    type: str
  disableprimaryondown:
    description:
      - Continue forwarding the traffic to backup virtual server even after the primary
        server comes UP from the DOWN state.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dnsprofilename:
    description:
      - Name of the DNS profile to be associated with the VServer. DNS profile properties
        will applied to the transactions processed by a VServer. This parameter is
        valid only for DNS and DNS-TCP VServers.
    type: str
  dnsrecordtype:
    description:
      - '0'
    type: str
    default: NSGSLB_IPV4
    choices:
      - A
      - AAAA
      - CNAME
      - NAPTR
  domainname:
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
    type: str
  downstateflush:
    description:
      - Flush all active transactions associated with a virtual server whose state
        transitions from UP to DOWN. Do not enable this option for applications that
        must complete their transactions.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  dtls:
    description:
      - This option starts/stops the dtls service on the vserver
    type: str
    choices:
      - true
      - false
  httpprofilename:
    description:
      - Name of the HTTP profile containing HTTP configuration settings for the virtual
        server. The service type of the virtual server should be either HTTP or SSL.
    type: str
  httpsredirecturl:
    description:
      - URL to which all HTTP traffic received on the port specified in the -redirectFromPort
        parameter is redirected.
    type: str
  icmpvsrresponse:
    description:
      - Can be active or passive
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  insertvserveripport:
    description:
      - 'Insert the virtual server''s VIP address and port number in the request header.
        Available values function as follows:'
      - '        VIPADDR - Header contains the vserver''s IP address and port number
        without any translation.'
      - '        OFF     - The virtual IP and port header insertion option is disabled.'
      - '        V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding
        to the IPv6 address of the vserver and the port number. An IPv6 address can
        be mapped to a user-specified IPv4 address using the set ns ip6 command.'
    type: str
    choices:
      - false
      - VIPADDR
      - V6TOV4MAPPING
  ipmask:
    description:
      - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have
        leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255).
        Accordingly, the mask specifies whether the first n bits or the last n bits
        of the destination IP address in a client request are to be matched with the
        corresponding bits in the IP pattern. The former is called a forward mask.
        The latter is called a reverse mask.
    type: str
  ippattern:
    description:
      - 'IP address pattern, in dotted decimal notation, for identifying packets to
        be accepted by the virtual server. The IP Mask parameter specifies which part
        of the destination IP address is matched against the pattern. Mutually exclusive
        with the IP Address parameter. '
      - For example, if the IP pattern assigned to the virtual server is 198.51.100.0
        and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the
        destination IP addresses are matched with the first 20 bits in the pattern.
        The virtual server accepts requests with IP addresses that range from 198.51.96.1
        to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such
        as 0.0.255.255 (a reverse mask).
      - If a destination IP address matches more than one IP pattern, the pattern
        with the longest match is selected, and the associated virtual server processes
        the request. For example, if the virtual servers, vs1 and vs2, have the same
        IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255,
        a destination IP address of 198.51.100.128 has the longest match with the
        IP pattern of vs1. If a destination IP address matches two or more virtual
        servers to the same extent, the request is processed by the virtual server
        whose port number matches the port number in the request.
    type: str
  ipset:
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current cs vserver
    type: str
  ipv46:
    description:
      - IP address of the content switching virtual server.
    type: str
  l2conn:
    description:
      - Use L2 Parameters to identify a connection
    type: str
    choices:
      - true
      - false
  listenpolicy:
    description:
      - String specifying the listen policy for the content switching virtual server.
        Can be either the name of an existing expression or an in-line expression.
    type: str
    default: '"NONE"'
  listenpriority:
    description:
      - Integer specifying the priority of the listen policy. A higher number specifies
        a lower priority. If a request matches the listen policies of more than one
        virtual server the virtual server whose listen policy has the highest priority
        (the lowest priority number) accepts the request.
    type: int
    default: 101
  mssqlserverversion:
    description:
      - The version of the MSSQL server
    type: str
    default: 2008R2
    choices:
      - 70
      - 2000
      - 2000SP1
      - 2005
      - 2008
      - 2008R2
      - 2012
      - 2014
  mysqlcharacterset:
    description:
      - The character set returned by the mysql vserver.
    type: int
    default: 8
  mysqlprotocolversion:
    description:
      - The protocol version returned by the mysql vserver.
    type: int
    default: 10
  mysqlservercapabilities:
    description:
      - The server capabilities returned by the mysql vserver.
    type: int
    default: 41613
  mysqlserverversion:
    description:
      - The server version string returned by the mysql vserver.
    type: str
  name:
    description:
      - 'Name for the content switching virtual server. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. '
      - Cannot be changed after the CS virtual server is created.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, my server or my server).
    type: str
  netprofile:
    description:
      - The name of the network profile.
    type: str
  newname:
    description:
      - 'New name for the virtual server. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. '
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my name" or 'my name').
    type: str
  oracleserverversion:
    description:
      - Oracle server version
    type: str
    default: 10G
    choices:
      - 10G
      - 11G
  persistencebackup:
    description:
      - Backup persistence type for the virtual server. Becomes operational if the
        primary persistence mechanism fails.
    type: str
    choices:
      - SOURCEIP
      - NONE
  persistenceid:
    description:
      - '0'
    type: int
  persistencetype:
    description:
      - 'Type of persistence for the virtual server. Available settings function as
        follows:'
      - '* SOURCEIP - Connections from the same client IP address belong to the same
        persistence session.'
      - '* COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by
        a Set-Cookie directive from a server, belong to the same persistence session.'
      - '* SSLSESSION - Connections that have the same SSL Session ID belong to the
        same persistence session.'
    type: str
    choices:
      - SOURCEIP
      - COOKIEINSERT
      - SSLSESSION
      - NONE
  persistmask:
    description:
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.
    type: str
  port:
    description:
      - Port number for content switching virtual server.
    type: int
  precedence:
    description:
      - Type of precedence to use for both RULE-based and URL-based policies on the
        content switching virtual server. With the default (RULE) setting, incoming
        requests are evaluated against the rule-based content switching policies.
        If none of the rules match, the URL in the request is evaluated against the
        URL-based content switching policies.
    type: str
    default: RULE
    choices:
      - RULE
      - URL
  probeport:
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select port for HTTP/TCP monitring
    type: int
  probeprotocol:
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select HTTP or TCP probes for healthcheck
    type: str
    choices:
      - TCP
      - HTTP
  probesuccessresponsecode:
    description:
      - HTTP code to return in SUCCESS case.
    type: str
    default: '"200 OK"'
  push:
    description:
      - Process traffic with the push virtual server that is bound to this content
        switching virtual server (specified by the Push VServer parameter). The service
        type of the push virtual server should be either HTTP or SSL.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  pushlabel:
    description:
      - Expression for extracting the label from the response received from server.
        This string can be either an existing rule name or an inline expression. The
        service type of the virtual server should be either HTTP or SSL.
    type: str
    default: '"none"'
  pushmulticlients:
    description:
      - Allow multiple Web 2.0 connections from the same client to connect to the
        virtual server and expect updates.
    type: str
    choices:
      - true
      - false
  pushvserver:
    description:
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which
        the server pushes updates received on the client-facing load balancing virtual
        server.
    type: str
  quicprofilename:
    description:
      - Name of QUIC profile which will be attached to the Content Switching VServer.
    type: str
  range:
    description:
      - Number of consecutive IP addresses, starting with the address specified by
        the IP Address parameter, to include in a range of addresses assigned to this
        virtual server.
    type: int
    default: 1
  redirectfromport:
    description:
      - Port number for the virtual server, from which we absorb the traffic for http
        redirect
    type: int
  redirectportrewrite:
    description:
      - State of port rewrite while performing HTTP redirect.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  redirecturl:
    description:
      - URL to which traffic is redirected if the virtual server becomes unavailable.
        The service type of the virtual server should be either HTTP or SSL.
      - 'Caution: Make sure that the domain in the URL does not match the domain specified
        for a content switching policy. If it does, requests are continuously redirected
        to the unavailable virtual server.'
    type: str
  rhistate:
    description:
      - A host route is injected according to the setting on the virtual servers
      - '            * If set to PASSIVE on all the virtual servers that share the
        IP address, the appliance always injects the hostroute.'
      - '            * If set to ACTIVE on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to ACTIVE on some virtual servers and PASSIVE on the
        others, the appliance, injects even if one virtual server set to ACTIVE is
        UP.'
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  rtspnat:
    description:
      - Enable network address translation (NAT) for real-time streaming protocol
        (RTSP) connections.
    type: str
    choices:
      - true
      - false
  servicetype:
    description:
      - Protocol used by the virtual server.
    type: str
    choices:
      - HTTP
      - SSL
      - TCP
      - FTP
      - RTSP
      - SSL_TCP
      - UDP
      - DNS
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - ANY
      - RADIUS
      - RDP
      - MYSQL
      - MSSQL
      - DIAMETER
      - SSL_DIAMETER
      - DNS_TCP
      - ORACLE
      - SMPP
      - PROXY
      - MONGO
      - MONGO_TLS
      - MQTT
      - MQTT_TLS
      - HTTP_QUIC
  sitedomainttl:
    description:
      - '0'
    type: int
  sobackupaction:
    description:
      - Action to be performed if spillover is to take effect, but no backup chain
        to spillover is usable or exists
    type: str
    choices:
      - DROP
      - ACCEPT
      - REDIRECT
  somethod:
    description:
      - Type of spillover used to divert traffic to the backup virtual server when
        the primary virtual server reaches the spillover threshold. Connection spillover
        is based on the number of connections. Bandwidth spillover is based on the
        total Kbps of incoming and outgoing traffic.
    type: str
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
  sopersistence:
    description:
      - Maintain source-IP based persistence on primary and backup virtual servers.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sopersistencetimeout:
    description:
      - Time-out value, in minutes, for spillover persistence.
    type: int
    default: 2
  sothreshold:
    description:
      - Depending on the spillover method, the maximum number of connections or the
        maximum total bandwidth (Kbps) that a virtual server can handle before spillover
        occurs.
    type: int
  state:
    description:
      - Initial state of the load balancing virtual server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  stateupdate:
    description:
      - 'Enable state updates for a specific content switching virtual server. By
        default, the Content Switching virtual server is always UP, regardless of
        the state of the Load Balancing virtual servers bound to it. This parameter
        interacts with the global setting as follows:'
      - Global Level | Vserver Level | Result
      - ENABLED      ENABLED        ENABLED
      - ENABLED      DISABLED       ENABLED
      - DISABLED     ENABLED        ENABLED
      - DISABLED     DISABLED       DISABLED
      - If you want to enable state updates for only some content switching virtual
        servers, be sure to disable the state update parameter.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
      - UPDATEONBACKENDUPDATE
  targettype:
    description:
      - Virtual server target type.
    type: str
    choices:
      - GSLB
  tcpprobeport:
    description:
      - Port number for external TCP probe. NetScaler provides support for external
        TCP health check of the vserver status over the selected port. This option
        is only supported for vservers assigned with an IPAddress or ipset.
    type: int
  tcpprofilename:
    description:
      - Name of the TCP profile containing TCP configuration settings for the virtual
        server.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  timeout:
    description:
      - Time period for which a persistence session is in effect.
    type: int
    default: 2
  ttl:
    description:
      - '0'
    type: int
  v6persistmasklen:
    description:
      - Persistence mask for IP based persistence types, for IPv6 virtual servers.
    type: int
    default: 128
  vipheader:
    description:
      - Name of virtual server IP and port header, for use with the VServer IP Port
        Insertion parameter.
    type: str
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
