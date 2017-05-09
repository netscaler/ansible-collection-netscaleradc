#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


DOCUMENTATION = '''
---
module: _
short_description: _
description:
    - _

version_added: 2.3.1

options:

    name:
        description:
            - >-
                Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and
                must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign
                (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
            - >-
                CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation
                marks (for example, "my vserver" or 'my vserver'). .
            - "Minimum length = 1"

    servicetype:
        choices:
            - 'HTTP'
            - 'FTP'
            - 'TCP'
            - 'UDP'
            - 'SSL'
            - 'SSL_BRIDGE'
            - 'SSL_TCP'
            - 'DTLS'
            - 'NNTP'
            - 'DNS'
            - 'DHCPRA'
            - 'ANY'
            - 'SIP_UDP'
            - 'SIP_TCP'
            - 'SIP_SSL'
            - 'DNS_TCP'
            - 'RTSP'
            - 'PUSH'
            - 'SSL_PUSH'
            - 'RADIUS'
            - 'RDP'
            - 'MYSQL'
            - 'MSSQL'
            - 'DIAMETER'
            - 'SSL_DIAMETER'
            - 'TFTP'
            - 'ORACLE'
            - 'SMPP'
            - 'SYSLOGTCP'
            - 'SYSLOGUDP'
            - 'FIX'
            - 'SSL_FIX'
        description:
            - "Protocol used by the service (also called the service type)."
            - >-
                Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, DNS, DHCPRA, ANY,
                SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, RTSP, PUSH, SSL_PUSH, RADIUS, RDP, MYSQL, MSSQL, DIAMETER,
                SSL_DIAMETER, TFTP, ORACLE, SMPP, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX

    ipv46:
        description:
            - "IPv4 or IPv6 address to assign to the virtual server."

    ippattern:
        description:
            - >-
                IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual
                server. The IP Mask parameter specifies which part of the destination IP address is matched against
                the pattern. Mutually exclusive with the IP Address parameter.
            - >-
                For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is
                255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with
                the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range
                from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as
                0.0.255.255 (a reverse mask).
            - >-
                If a destination IP address matches more than one IP pattern, the pattern with the longest match is
                selected, and the associated virtual server processes the request. For example, if virtual servers
                vs1 and vs2 have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and
                0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of
                vs1. If a destination IP address matches two or more virtual servers to the same extent, the request
                is processed by the virtual server whose port number matches the port number in the request.

    ipmask:
        description:
            - >-
                IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing
                non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether
                the first n bits or the last n bits of the destination IP address in a client request are to be
                matched with the corresponding bits in the IP pattern. The former is called a forward mask. The
                latter is called a reverse mask.

    port:
        description:
            - "Port number for the virtual server."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    range:
        description:
            - >-
                Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual
                server then functions as a network virtual server, accepting traffic on any of the generated IP
                addresses. The IP addresses are generated automatically, as follows:
            - >-
                * For a range of n, the last octet of the address specified by the IP Address parameter increments
                n-1 times.
            - "* If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1."
            - >-
                Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array
                of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name
                parameters to specify the range. For example:
            - "add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80."
            - "Default value: 1"
            - "Minimum value = 1"
            - "Maximum value = 254"

    persistencetype:
        choices:
            - 'SOURCEIP'
            - 'COOKIEINSERT'
            - 'SSLSESSION'
            - 'RULE'
            - 'URLPASSIVE'
            - 'CUSTOMSERVERID'
            - 'DESTIP'
            - 'SRCIPDESTIP'
            - 'CALLID'
            - 'RTSPSID'
            - 'DIAMETER'
            - 'FIXSESSION'
            - 'NONE'
        description:
            - "Type of persistence for the virtual server. Available settings function as follows:"
            - "* SOURCEIP - Connections from the same client IP address belong to the same persistence session."
            - >-
                * COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from
                a server, belong to the same persistence session.
            - "* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session."
            - >-
                * CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this
                persistence type, set the Server ID (CustomServerID) parameter for each service and configure the
                Rule parameter to identify the server ID in a request.
            - "* RULE - All connections that match a user defined rule belong to the same persistence session."
            - >-
                * URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence
                session. The server ID is the hexadecimal representation of the IP address and port of the service to
                which the request must be forwarded. This persistence type requires a rule to identify the server ID
                in the request.
            - "* DESTIP - Connections to the same destination IP address belong to the same persistence session."
            - >-
                * SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to
                the same persistence session.
            - "* CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session."
            - "* RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session."
            - >-
                * FIXSESSION - Connections that have the same SenderCompID and TargetCompID values belong to the same
                persistence session.
            - >-
                Possible values = SOURCEIP, COOKIEINSERT, SSLSESSION, RULE, URLPASSIVE, CUSTOMSERVERID, DESTIP,
                SRCIPDESTIP, CALLID, RTSPSID, DIAMETER, FIXSESSION, NONE

    timeout:
        description:
            - "Time period for which a persistence session is in effect."
            - "Default value: 2"
            - "Minimum value = 0"
            - "Maximum value = 1440"

    persistencebackup:
        choices:
            - 'SOURCEIP'
            - 'NONE'
        description:
            - >-
                Backup persistence type for the virtual server. Becomes operational if the primary persistence
                mechanism fails.
            - "Possible values = SOURCEIP, NONE"

    backuppersistencetimeout:
        description:
            - "Time period for which backup persistence is in effect."
            - "Default value: 2"
            - "Minimum value = 2"
            - "Maximum value = 1440"

    lbmethod:
        choices:
            - 'ROUNDROBIN'
            - 'LEASTCONNECTION'
            - 'LEASTRESPONSETIME'
            - 'URLHASH'
            - 'DOMAINHASH'
            - 'DESTINATIONIPHASH'
            - 'SOURCEIPHASH'
            - 'SRCIPDESTIPHASH'
            - 'LEASTBANDWIDTH'
            - 'LEASTPACKETS'
            - 'TOKEN'
            - 'SRCIPSRCPORTHASH'
            - 'LRTM'
            - 'CALLIDHASH'
            - 'CUSTOMLOAD'
            - 'LEASTREQUEST'
            - 'AUDITLOGHASH'
            - 'STATICPROXIMITY'
        description:
            - "Load balancing method. The available settings function as follows:"
            - >-
                * ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to
                services to enforce weighted round robin distribution.
            - "* LEASTCONNECTION (default) - Select the service with the fewest connections."
            - "* LEASTRESPONSETIME - Select the service with the lowest average response time."
            - "* LEASTBANDWIDTH - Select the service currently handling the least traffic."
            - "* LEASTPACKETS - Select the service currently serving the lowest number of packets per second."
            - "* CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors."
            - >-
                * LRTM - Select the service with the lowest response time. Response times are learned through
                monitoring probes. This method also takes the number of active connections into account.
            - >-
                Also available are a number of hashing methods, in which the appliance extracts a predetermined
                portion of the request, creates a hash of the portion, and then checks whether any previous requests
                had the same hash value. If it finds a match, it forwards the request to the service that served
                those previous requests. Following are the hashing methods:
            - "* URLHASH - Create a hash of the request URL (or part of the URL)."
            - >-
                * DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The
                domain name is taken from either the URL or the Host header. If the domain name appears in both
                locations, the URL is preferred. If the request does not contain a domain name, the load balancing
                method defaults to LEASTCONNECTION.
            - "* DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header."
            - "* SOURCEIPHASH - Create a hash of the source IP address in the IP header."
            - >-
                * TOKEN - Extract a token from the request, create a hash of the token, and then select the service
                to which any previous requests with the same token hash value were sent.
            - >-
                * SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and
                destination IP address in the IP header.
            - "* SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header."
            - "* CALLIDHASH - Create a hash of the SIP Call-ID header."
            - "Default value: LEASTCONNECTION"
            - >-
                Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, URLHASH, DOMAINHASH,
                DESTINATIONIPHASH, SOURCEIPHASH, SRCIPDESTIPHASH, LEASTBANDWIDTH, LEASTPACKETS, TOKEN,
                SRCIPSRCPORTHASH, LRTM, CALLIDHASH, CUSTOMLOAD, LEASTREQUEST, AUDITLOGHASH, STATICPROXIMITY

    hashlength:
        description:
            - >-
                Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing
                methods.
            - "Default value: 80"
            - "Minimum value = 1"
            - "Maximum value = 4096"

    netmask:
        description:
            - >-
                IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing
                method is DESTINATIONIPHASH or SOURCEIPHASH.
            - "Minimum length = 1"

    v6netmasklen:
        description:
            - >-
                Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is
                required by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.
            - "Default value: 128"
            - "Minimum value = 1"
            - "Maximum value = 128"

    backuplbmethod:
        choices:
            - 'ROUNDROBIN'
            - 'LEASTCONNECTION'
            - 'LEASTRESPONSETIME'
            - 'SOURCEIPHASH'
            - 'LEASTBANDWIDTH'
            - 'LEASTPACKETS'
            - 'CUSTOMLOAD'
        description:
            - "Backup load balancing method. Becomes operational if the primary load balancing me"
            - "thod fails or cannot be used."
            - "Valid only if the primary method is based on static proximity."
            - "Default value: ROUNDROBIN"
            - >-
                Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH,
                LEASTPACKETS, CUSTOMLOAD

    cookiename:
        description:
            - >-
                Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of
                cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.

    rule:
        description:
            - >-
                Expression, or name of a named expression, against which traffic is evaluated. Written in the classic
                or default syntax.
            - "Note:"
            - >-
                Maximum length of a string literal in the expression is 255 characters. A longer string can be split
                into smaller strings of up to 255 characters each, and the smaller strings concatenated with the +
                operator. For example, you can create a 500-character string as follows: '"<string of 255
                characters>" + "<string of 245 characters>"'
            - "The following requirements apply only to the NetScaler CLI:"
            - >-
                * If the expression includes one or more spaces, enclose the entire expression in double quotation
                marks.
            - >-
                * If the expression itself includes double quotation marks, escape the quotations by using the \
                character.
            - >-
                * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not
                have to escape the double quotation marks.
            - "Default value: \"none\""

    listenpolicy:
        description:
            - >-
                Default syntax expression identifying traffic accepted by the virtual server. Can be either an
                expression (for example, CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In
                the above example, the virtual server accepts all requests whose destination IP address is in the
                192.0.2.0/24 subnet.
            - "Default value: \"NONE\""

    listenpriority:
        description:
            - >-
                Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If
                a request matches the listen policies of more than one virtual server the virtual server whose listen
                policy has the highest priority (the lowest priority number) accepts the request.
            - "Default value: 101"
            - "Minimum value = 0"
            - "Maximum value = 101"

    resrule:
        description:
            - >-
                Default syntax expression specifying which part of a server's response to use for creating rule based
                persistence sessions (persistence type RULE). Can be either an expression or the name of a named
                expression.
            - "Example:"
            - "HTTP.RES.HEADER(\"setcookie\").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE(\"server1\")."
            - "Default value: \"none\""

    persistmask:
        description:
            - "Persistence mask for IP based persistence types, for IPv4 virtual servers."
            - "Minimum length = 1"

    v6persistmasklen:
        description:
            - "Persistence mask for IP based persistence types, for IPv6 virtual servers."
            - "Default value: 128"
            - "Minimum value = 1"
            - "Maximum value = 128"

    pq:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    sc:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Use SureConnect on the virtual server."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    rtspnat:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Use network address translation (NAT) for RTSP data connections."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    m:
        choices:
            - 'IP'
            - 'MAC'
            - 'IPTUNNEL'
            - 'TOS'
        description:
            - "Redirection mode for load balancing. Available settings function as follows:"
            - >-
                * IP - Before forwarding a request to a server, change the destination IP address to the server's IP
                address.
            - >-
                * MAC - Before forwarding a request to a server, change the destination MAC address to the server's
                MAC address. The destination IP address is not changed. MAC-based redirection mode is used mostly in
                firewall load balancing deployments.
            - >-
                * IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the
                destination IP address to the IP address of the server and the source IP address to the subnet IP
                (SNIP). The client IP packets are not modified. Applicable to both IPv4 and IPv6 packets.
            - "* TOS - Encode the virtual server's TOS ID in the TOS field of the IP header."
            - "You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR)."
            - "Default value: IP"
            - "Possible values = IP, MAC, IPTUNNEL, TOS"

    tosid:
        description:
            - >-
                TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.
            - "Minimum value = 1"
            - "Maximum value = 63"

    datalength:
        description:
            - >-
                Length of the token to be extracted from the data segment of an incoming packet, for use in the token
                method of load balancing. The length of the token, specified in bytes, must not be greater than 24
                KB. Applicable to virtual servers of type TCP.
            - "Minimum value = 1"
            - "Maximum value = 100"

    dataoffset:
        description:
            - >-
                Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers,
                of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP
                payload.
            - "Minimum value = 0"
            - "Maximum value = 25400"

    sessionless:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load
                balancing of intrusion detection system (IDS) servers and scenarios involving direct server return
                (DSR), where session information is unnecessary.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "State of the load balancing virtual server."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    connfailover:
        choices:
            - 'DISABLED'
            - 'STATEFUL'
            - 'STATELESS'
        description:
            - >-
                Mode in which the connection failover feature must operate for the virtual server. After a failover,
                established TCP connections and UDP packet flows are kept active and resumed on the secondary
                appliance. Clients remain connected to the same servers. Available settings function as follows:
            - >-
                * STATEFUL - The primary appliance shares state information with the secondary appliance, in real
                time, resulting in some runtime processing overhead.
            - >-
                * STATELESS - State information is not shared, and the new primary appliance tries to re-create the
                packet flow on the basis of the information contained in the packets it receives.
            - "* DISABLED - Connection failover does not occur."
            - "Default value: DISABLED"
            - "Possible values = DISABLED, STATEFUL, STATELESS"

    redirurl:
        description:
            - "URL to which to redirect traffic if the virtual server becomes unavailable."
            - >-
                WARNING! Make sure that the domain in the URL does not match the domain specified for a content
                switching policy. If it does, requests are continuously redirected to the unavailable virtual server.
            - "Minimum length = 1"

    cacheable:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can
                forward requests only to a transparent cache redirection virtual server that has an IP address and
                port combination of *:80, so such a cache redirection virtual server must be configured on the
                appliance.
            - "Default value: NO"
            - "Possible values = YES, NO"

    clttimeout:
        description:
            - "Idle time, in seconds, after which a client connection is terminated."
            - "Minimum value = 0"
            - "Maximum value = 31536000"

    somethod:
        choices:
            - 'CONNECTION'
            - 'DYNAMICCONNECTION'
            - 'BANDWIDTH'
            - 'HEALTH'
            - 'NONE'
        description:
            - "Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:"
            - "* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold."
            - >-
                * DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server
                exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a
                spillover threshold for this setting, because the threshold is implied by the Max Clients settings of
                bound services.
            - >-
                * BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and
                outgoing traffic exceeds the threshold.
            - >-
                * HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below
                the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with
                weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2
                and svc3 transition to DOWN.
            - "* NONE - Spillover does not occur."
            - "Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE"

    sopersistence:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                If spillover occurs, maintain source IP address based persistence for both primary and backup virtual
                servers.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    sopersistencetimeout:
        description:
            - "Timeout for spillover persistence, in minutes."
            - "Default value: 2"
            - "Minimum value = 2"
            - "Maximum value = 1440"

    healththreshold:
        description:
            - >-
                Threshold in percent of active services below which vserver state is made down. If this threshold is
                0, vserver state will be up even if one bound service is up.
            - "Default value: 0"
            - "Minimum value = 0"
            - "Maximum value = 100"

    sothreshold:
        description:
            - >-
                Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a
                bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a
                percentage for the HEALTH method (do not enter the percentage symbol).
            - "Minimum value = 1"
            - "Maximum value = 4294967287"

    sobackupaction:
        choices:
            - 'DROP'
            - 'ACCEPT'
            - 'REDIRECT'
        description:
            - >-
                Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or
                exists.
            - "Possible values = DROP, ACCEPT, REDIRECT"

    redirectportrewrite:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Rewrite the port and change the protocol to ensure successful HTTP redirects from services."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    downstateflush:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                Flush all active transactions associated with a virtual server whose state transitions from UP to
                DOWN. Do not enable this option for applications that must complete their transactions.
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    backupvserver:
        description:
            - >-
                Name of the backup virtual server to which to forward requests if the primary virtual server goes
                DOWN or reaches its spillover threshold.
            - "Minimum length = 1"

    disableprimaryondown:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                If the primary virtual server goes down, do not allow it to return to primary status until manually
                enabled.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    insertvserveripport:
        choices:
            - 'OFF'
            - 'VIPADDR'
            - 'V6TOV4MAPPING'
        description:
            - >-
                Insert an HTTP header, whose value is the IP address and port number of the virtual server, before
                forwarding a request to the server. The format of the header is <vipHeader>: <virtual server IP
                address>_<port number >, where vipHeader is the name that you specify for the header. If the virtual
                server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate
                it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the
                value of this parameter determines which IP address is inserted in the header, as follows:
            - >-
                * VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the
                virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is
                ignored.
            - >-
                * V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a
                mapped IPv4 address is not configured, insert the IPv6 address.
            - "* OFF - Disable header insertion."
            - "Possible values = OFF, VIPADDR, V6TOV4MAPPING"

    vipheader:
        description:
            - "Name for the inserted header. The default name is vip-header."
            - "Minimum length = 1"

    authenticationhost:
        description:
            - >-
                Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be
                redirected for authentication. Make sure that the Authentication parameter is set to ENABLED.
            - "Minimum length = 3"
            - "Maximum length = 252"

    authentication:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Enable or disable user authentication."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    authn401:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - "Enable or disable user authentication with HTTP 401 responses."
            - "Default value: OFF"
            - "Possible values = ON, OFF"

    authnvsname:
        description:
            - "Name of an authentication virtual server with which to authenticate users."
            - "Minimum length = 1"
            - "Maximum length = 252"

    push:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Process traffic with the push virtual server that is bound to this load balancing virtual server."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    pushvserver:
        description:
            - >-
                Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes
                updates received on the load balancing virtual server that you are configuring.
            - "Minimum length = 1"

    pushlabel:
        description:
            - >-
                Expression for extracting a label from the server's response. Can be either an expression or the name
                of a named expression.
            - "Default value: \"none\""

    pushmulticlients:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
                updates.
            - "Default value: NO"
            - "Possible values = YES, NO"

    tcpprofilename:
        description:
            - "Name of the TCP profile whose settings are to be applied to the virtual server."
            - "Minimum length = 1"
            - "Maximum length = 127"

    httpprofilename:
        description:
            - "Name of the HTTP profile whose settings are to be applied to the virtual server."
            - "Minimum length = 1"
            - "Maximum length = 127"

    dbprofilename:
        description:
            - "Name of the DB profile whose settings are to be applied to the virtual server."
            - "Minimum length = 1"
            - "Maximum length = 127"

    comment:
        description:
            - "Any comments that you might want to associate with the virtual server."

    l2conn:
        choices:
            - 'ON'
            - 'OFF'
        description:
            - >-
                Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source
                IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows
                multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the NetScaler appliance.
            - "Possible values = ON, OFF"

    oracleserverversion:
        choices:
            - '10G'
            - '11G'
        description:
            - "Oracle server version."
            - "Default value: 10G"
            - "Possible values = 10G, 11G"

    mssqlserverversion:
        choices:
            - '70'
            - '2000'
            - '2000SP1'
            - '2005'
            - '2008'
            - '2008R2'
            - '2012'
            - '2014'
        description:
            - >-
                For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this
                parameter if you expect some clients to run a version different from the version of the database.
                This setting provides compatibility between the client-side and server-side connections by ensuring
                that all communication conforms to the server's version.
            - "Default value: 2008R2"
            - "Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014"

    mysqlprotocolversion:
        description:
            - "MySQL protocol version that the virtual server advertises to clients."

    mysqlserverversion:
        description:
            - "MySQL server version string that the virtual server advertises to clients."
            - "Minimum length = 1"
            - "Maximum length = 31"

    mysqlcharacterset:
        description:
            - "Character set that the virtual server advertises to clients."

    mysqlservercapabilities:
        description:
            - "Server capabilities that the virtual server advertises to clients."

    appflowlog:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Apply AppFlow logging to the virtual server."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    netprofile:
        description:
            - >-
                Name of the network profile to associate with the virtual server. If you set this parameter, the
                virtual server uses only the IP addresses in the network profile as source IP addresses when
                initiating connections with servers.
            - "Minimum length = 1"
            - "Maximum length = 127"

    icmpvsrresponse:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - >-
                How the NetScaler appliance responds to ping requests received for an IP address that is common to
                one or more virtual servers. Available settings function as follows:
            - >-
                * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always
                responds to the ping requests.
            - >-
                * If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to
                the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not
                respond.
            - >-
                * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at
                least one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.
            - >-
                Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is
                available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add
                ip command in the CLI or the Create IP dialog box in the GUI.
            - "Default value: PASSIVE"
            - "Possible values = PASSIVE, ACTIVE"

    rhistate:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - >-
                Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the
                VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to
                VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate
                (RHI STATE) settings on the virtual servers associated with the VIP address:
            - >-
                * If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the
                route for the VIP address.
            - >-
                * If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for
                the VIP address if at least one of the associated virtual servers is in UP state.
            - >-
                * If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the
                route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to
                ACTIVE, is in UP state.
            - "Default value: PASSIVE"
            - "Possible values = PASSIVE, ACTIVE"

    newservicerequest:
        description:
            - >-
                Number of requests, or percentage of the load on existing services, by which to increase the load on
                a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is
                applicable. A zero value indicates that the global RR startup parameter is applied. Changing the
                value to zero will cause services currently in slow start to take the full traffic as determined by
                the LB method. Subsequently, any new services added will use the global RR factor.
            - "Default value: 0"

    newservicerequestunit:
        choices:
            - 'PER_SECOND'
            - 'PERCENT'
        description:
            - "Units in which to increment load at each interval in slow-start mode."
            - "Default value: PER_SECOND"
            - "Possible values = PER_SECOND, PERCENT"

    newservicerequestincrementinterval:
        description:
            - >-
                Interval, in seconds, between successive increments in the load on a new service or a service whose
                state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.
            - "Default value: 0"
            - "Minimum value = 0"
            - "Maximum value = 3600"

    minautoscalemembers:
        description:
            - "Minimum number of members expected to be present when vserver is used in Autoscale."
            - "Default value: 0"
            - "Minimum value = 0"
            - "Maximum value = 5000"

    maxautoscalemembers:
        description:
            - "Maximum number of members expected to be present when vserver is used in Autoscale."
            - "Default value: 0"
            - "Minimum value = 0"
            - "Maximum value = 5000"

    persistavpno:
        description:
            - "Persist AVP number for Diameter Persistency."
            - "In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP,"
            - "define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X"
            - "is nested inside AVP Y which is nested in Z, then define the list as Z Y X."
            - "Minimum value = 1"

    skippersistency:
        choices:
            - 'Bypass'
            - 'ReLb'
            - 'None'
        description:
            - >-
                This argument decides the behavior incase the service which is selected from an existing persistence
                session has reached threshold.
            - "Default value: None"
            - "Possible values = Bypass, ReLb, None"

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID
                of 0.
            - "Minimum value = 0"
            - "Maximum value = 4094"

    authnprofile:
        description:
            - "Name of the authentication profile to be used when authentication is turned on."

    macmoderetainvlan:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "This option is used to retain vlan information of incoming packet when macmode is enabled."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    dbslb:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Enable database specific load balancing for MySQL and MSSQL service types."
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    dns64:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "This argument is for enabling/disabling the dns64 on lbvserver."
            - "Possible values = ENABLED, DISABLED"

    bypassaaaa:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns
                server.
            - "Default value: NO"
            - "Possible values = YES, NO"

    recursionavailable:
        choices:
            - 'YES'
            - 'NO'
        description:
            - >-
                When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on.
                Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers
                thatsupport recursive queries.
            - "Default value: NO"
            - "Possible values = YES, NO"

    processlocal:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - >-
                By turning on this option packets destined to a vserver in a cluster will not under go any steering.
                Turn this option for single packet request response mode or when the upstream device is performing a
                proper RSS for connection based distribution.
            - "Default value: DISABLED"
            - "Possible values = ENABLED, DISABLED"

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to
                the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.
            - "Minimum length = 1"
            - "Maximum length = 127"

    weight:
        description:
            - "Weight to assign to the specified service."
            - "Minimum value = 1"
            - "Maximum value = 100"

    servicename:
        description:
            - "Service to bind to the virtual server."
            - "Minimum length = 1"

    redirurlflags:
        description:
            - "The redirect URL to be unset."

    newname:
        description:
            - "New name for the virtual server."
            - "Minimum length = 1"


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled
    try:
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        name=dict(type='str'),
        servicetype=dict(
            type='str',
            choices=[
                'HTTP',
                'FTP',
                'TCP',
                'UDP',
                'SSL',
                'SSL_BRIDGE',
                'SSL_TCP',
                'DTLS',
                'NNTP',
                'DNS',
                'DHCPRA',
                'ANY',
                'SIP_UDP',
                'SIP_TCP',
                'SIP_SSL',
                'DNS_TCP',
                'RTSP',
                'PUSH',
                'SSL_PUSH',
                'RADIUS',
                'RDP',
                'MYSQL',
                'MSSQL',
                'DIAMETER',
                'SSL_DIAMETER',
                'TFTP',
                'ORACLE',
                'SMPP',
                'SYSLOGTCP',
                'SYSLOGUDP',
                'FIX',
                'SSL_FIX',
            ]
        ),
        ipv46=dict(type='str'),
        ippattern=dict(type='str'),
        ipmask=dict(type='str'),
        port=dict(type='int'),
        range=dict(type='float'),
        persistencetype=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'COOKIEINSERT',
                'SSLSESSION',
                'RULE',
                'URLPASSIVE',
                'CUSTOMSERVERID',
                'DESTIP',
                'SRCIPDESTIP',
                'CALLID',
                'RTSPSID',
                'DIAMETER',
                'FIXSESSION',
                'NONE',
            ]
        ),
        timeout=dict(type='float'),
        persistencebackup=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'NONE',
            ]
        ),
        backuppersistencetimeout=dict(type='float'),
        lbmethod=dict(
            type='str',
            choices=[
                'ROUNDROBIN',
                'LEASTCONNECTION',
                'LEASTRESPONSETIME',
                'URLHASH',
                'DOMAINHASH',
                'DESTINATIONIPHASH',
                'SOURCEIPHASH',
                'SRCIPDESTIPHASH',
                'LEASTBANDWIDTH',
                'LEASTPACKETS',
                'TOKEN',
                'SRCIPSRCPORTHASH',
                'LRTM',
                'CALLIDHASH',
                'CUSTOMLOAD',
                'LEASTREQUEST',
                'AUDITLOGHASH',
                'STATICPROXIMITY',
            ]
        ),
        hashlength=dict(type='float'),
        netmask=dict(type='str'),
        v6netmasklen=dict(type='float'),
        backuplbmethod=dict(
            type='str',
            choices=[
                'ROUNDROBIN',
                'LEASTCONNECTION',
                'LEASTRESPONSETIME',
                'SOURCEIPHASH',
                'LEASTBANDWIDTH',
                'LEASTPACKETS',
                'CUSTOMLOAD',
            ]
        ),
        cookiename=dict(type='str'),
        rule=dict(type='str'),
        listenpolicy=dict(type='str'),
        listenpriority=dict(type='float'),
        resrule=dict(type='str'),
        persistmask=dict(type='str'),
        v6persistmasklen=dict(type='float'),
        pq=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        sc=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        rtspnat=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        m=dict(
            type='str',
            choices=[
                'IP',
                'MAC',
                'IPTUNNEL',
                'TOS',
            ]
        ),
        tosid=dict(type='float'),
        datalength=dict(type='float'),
        dataoffset=dict(type='float'),
        sessionless=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        connfailover=dict(
            type='str',
            choices=[
                'DISABLED',
                'STATEFUL',
                'STATELESS',
            ]
        ),
        redirurl=dict(type='str'),
        cacheable=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        clttimeout=dict(type='float'),
        somethod=dict(
            type='str',
            choices=[
                'CONNECTION',
                'DYNAMICCONNECTION',
                'BANDWIDTH',
                'HEALTH',
                'NONE',
            ]
        ),
        sopersistence=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        sopersistencetimeout=dict(type='float'),
        healththreshold=dict(type='float'),
        sothreshold=dict(type='float'),
        sobackupaction=dict(
            type='str',
            choices=[
                'DROP',
                'ACCEPT',
                'REDIRECT',
            ]
        ),
        redirectportrewrite=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        downstateflush=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        backupvserver=dict(type='str'),
        disableprimaryondown=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        insertvserveripport=dict(
            type='str',
            choices=[
                'OFF',
                'VIPADDR',
                'V6TOV4MAPPING',
            ]
        ),
        vipheader=dict(type='str'),
        authenticationhost=dict(type='str'),
        authentication=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        authn401=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        authnvsname=dict(type='str'),
        push=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        pushvserver=dict(type='str'),
        pushlabel=dict(type='str'),
        pushmulticlients=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        dbprofilename=dict(type='str'),
        comment=dict(type='str'),
        l2conn=dict(
            type='str',
            choices=[
                'ON',
                'OFF',
            ]
        ),
        oracleserverversion=dict(
            type='str',
            choices=[
                '10G',
                '11G',
            ]
        ),
        mssqlserverversion=dict(
            type='str',
            choices=[
                '70',
                '2000',
                '2000SP1',
                '2005',
                '2008',
                '2008R2',
                '2012',
                '2014',
            ]
        ),
        mysqlprotocolversion=dict(type='float'),
        mysqlserverversion=dict(type='str'),
        mysqlcharacterset=dict(type='float'),
        mysqlservercapabilities=dict(type='float'),
        appflowlog=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        netprofile=dict(type='str'),
        icmpvsrresponse=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ]
        ),
        rhistate=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ]
        ),
        newservicerequest=dict(type='float'),
        newservicerequestunit=dict(
            type='str',
            choices=[
                'PER_SECOND',
                'PERCENT',
            ]
        ),
        newservicerequestincrementinterval=dict(type='float'),
        minautoscalemembers=dict(type='float'),
        maxautoscalemembers=dict(type='float'),
        persistavpno=dict(type='list'),
        skippersistency=dict(
            type='str',
            choices=[
                'Bypass',
                'ReLb',
                'None',
            ]
        ),
        td=dict(type='float'),
        authnprofile=dict(type='str'),
        macmoderetainvlan=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        dbslb=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        dns64=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        bypassaaaa=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        recursionavailable=dict(
            type='str',
            choices=[
                'YES',
                'NO',
            ]
        ),
        processlocal=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        dnsprofilename=dict(type='str'),
        weight=dict(type='float'),
        servicename=dict(type='str'),
        redirurlflags=dict(type='bool'),
        newname=dict(type='str'),
    )

    hand_inserted_arguments = dict(
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    readwrite_attrs = [
        'name',
        'servicetype',
        'ipv46',
        'ippattern',
        'ipmask',
        'port',
        'range',
        'persistencetype',
        'timeout',
        'persistencebackup',
        'backuppersistencetimeout',
        'lbmethod',
        'hashlength',
        'netmask',
        'v6netmasklen',
        'backuplbmethod',
        'cookiename',
        'rule',
        'listenpolicy',
        'listenpriority',
        'resrule',
        'persistmask',
        'v6persistmasklen',
        'pq',
        'sc',
        'rtspnat',
        'm',
        'tosid',
        'datalength',
        'dataoffset',
        'sessionless',
        'state',
        'connfailover',
        'redirurl',
        'cacheable',
        'clttimeout',
        'somethod',
        'sopersistence',
        'sopersistencetimeout',
        'healththreshold',
        'sothreshold',
        'sobackupaction',
        'redirectportrewrite',
        'downstateflush',
        'backupvserver',
        'disableprimaryondown',
        'insertvserveripport',
        'vipheader',
        'authenticationhost',
        'authentication',
        'authn401',
        'authnvsname',
        'push',
        'pushvserver',
        'pushlabel',
        'pushmulticlients',
        'tcpprofilename',
        'httpprofilename',
        'dbprofilename',
        'comment',
        'l2conn',
        'oracleserverversion',
        'mssqlserverversion',
        'mysqlprotocolversion',
        'mysqlserverversion',
        'mysqlcharacterset',
        'mysqlservercapabilities',
        'appflowlog',
        'netprofile',
        'icmpvsrresponse',
        'rhistate',
        'newservicerequest',
        'newservicerequestunit',
        'newservicerequestincrementinterval',
        'minautoscalemembers',
        'maxautoscalemembers',
        'persistavpno',
        'skippersistency',
        'td',
        'authnprofile',
        'macmoderetainvlan',
        'dbslb',
        'dns64',
        'bypassaaaa',
        'recursionavailable',
        'processlocal',
        'dnsprofilename',
        'lbprofilename',
        'redirectfromport',
        'httpsredirecturl',
        'weight',
        'servicename',
        'redirurlflags',
        'newname',
    ]

    readonly_attrs = [
        'value',
        'ipmapping',
        'ngname',
        'type',
        'curstate',
        'effectivestate',
        'status',
        'lbrrreason',
        'redirect',
        'precedence',
        'homepage',
        'dnsvservername',
        'domain',
        'policyname',
        'cachevserver',
        'health',
        'gotopriorityexpression',
        'ruletype',
        'groupname',
        'cookiedomain',
        'map',
        'gt2gb',
        'consolidatedlconn',
        'consolidatedlconngbl',
        'thresholdvalue',
        'bindpoint',
        'invoke',
        'labeltype',
        'labelname',
        'version',
        'totalservices',
        'activeservices',
        'statechangetimesec',
        'statechangetimeseconds',
        'statechangetimemsec',
        'tickssincelaststatechange',
        'isgslb',
        'vsvrdynconnsothreshold',
        'backupvserverstatus',
        '__count',
    ]

    immutable_attrs = [
        'name',
        'servicetype',
        'ipv46',
        'port',
        'range',
        'state',
        'redirurl',
        'vipheader',
        'newservicerequestunit',
        'td',
        'servicename',
        'redirurlflags',
        'newname',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        immutable_attrs=immutable_attrs,
    )

    def _exists():
        if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def _identical():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = _proxy.diff_object(_list[0])
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        return _proxy.diff_object(_list[0])

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not _exists():
                if not module.check_mode:
                    _proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not _identical():

                # Check if we try to change value of immutable attributes
                immutables_changed = get_immutables_intersection(gslb_site_proxy, diff().keys())
                if immutables_changed != []:
                    module.fail_json(msg='Cannot update immutable attributes %s' % (immutables_changed,), diff=diff(), **module_result)

                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='_ does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='_ differs from configured', diff=diff(), **module_result)

        elif module.params['operation'] == 'absent':
            if _exists():
                if not module.check_mode:
                    _proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if _exists():
                    module.fail_json(msg='_ still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
