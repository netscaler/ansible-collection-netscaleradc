#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adc_lb_vserver
short_description: Manage load balancing vserver configuration
description:
    - Manage load balancing vserver configuration
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    name:
        description:
            - >-
                Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and
                contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@),
                sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
            - >-
                CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation
                (for example, "my vserver" or 'my vserver'). .
            - "Minimum length =  1"
        type: str

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
            - 'PROXY'
            - 'USER_TCP'
            - 'USER_SSL_TCP'
            - 'QUIC'
            - 'IPFIX'
            - 'LOGSTREAM'
        description:
            - "Protocol used by the service (also called the service type)."
        type: str

    ipv46:
        description:
            - "IPv4 or IPv6 address to assign to the virtual server."
        type: str

    ippattern:
        description:
            - >-
                IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual
                The IP Mask parameter specifies which part of the destination IP address is matched against the
                Mutually exclusive with the IP Address parameter.
            - >-
                For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is
                (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20
                in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to
                You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).
            - >-
                If a destination IP address matches more than one IP pattern, the pattern with the longest match is
                and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2
                the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a
                IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP
                matches two or more virtual servers to the same extent, the request is processed by the virtual
                whose port number matches the port number in the request.
        type: str

    ipmask:
        description:
            - >-
                IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing
                octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first
                bits or the last n bits of the destination IP address in a client request are to be matched with the
                bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
        type: str

    port:
        description:
            - "Port number for the virtual server."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    ipset:
        description:
            - >-
                The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current
                vserver.
            - "Minimum length =  1"
        type: str

    range:
        description:
            - >-
                Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual
                then functions as a network virtual server, accepting traffic on any of the generated IP addresses.
                IP addresses are generated automatically, as follows:
            - >-
                * For a range of n, the last octet of the address specified by the IP Address parameter increments
                times.
            - "* If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1."
            - >-
                Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array
                virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name
                to specify the range. For example:
            - "add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80."
            - "Minimum value = C(1)"
            - "Maximum value = C(254)"
        type: str

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
            - 'USERSESSION'
            - 'NONE'
        description:
            - "Type of persistence for the virtual server. Available settings function as follows:"
            - "* SOURCEIP - Connections from the same client IP address belong to the same persistence session."
            - >-
                * COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from
                server, belong to the same persistence session.
            - "* SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session."
            - >-
                * CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this
                type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter
                identify the server ID in a request.
            - "* RULE - All connections that match a user defined rule belong to the same persistence session."
            - >-
                * URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence
                The server ID is the hexadecimal representation of the IP address and port of the service to which
                request must be forwarded. This persistence type requires a rule to identify the server ID in the
            - "* DESTIP - Connections to the same destination IP address belong to the same persistence session."
            - >-
                * SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to
                same persistence session.
            - "* CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session."
            - "* RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session."
            - >-
                * FIXSESSION - Connections that have the same SenderCompID and TargetCompID values belong to the same
                session.
            - >-
                * USERSESSION - Persistence session is created based on the persistence parameter value provided from
                extension.
        type: str

    timeout:
        description:
            - "Time period for which a persistence session is in effect."
            - "Minimum value = C(0)"
            - "Maximum value = C(1440)"
        type: int

    persistencebackup:
        choices:
            - 'SOURCEIP'
            - 'NONE'
        description:
            - >-
                Backup persistence type for the virtual server. Becomes operational if the primary persistence
                fails.
        type: str

    backuppersistencetimeout:
        description:
            - "Time period for which backup persistence is in effect."
            - "Minimum value = C(2)"
            - "Maximum value = C(1440)"
        type: int

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
            - 'USER_TOKEN'
        description:
            - "Load balancing method.  The available settings function as follows:"
            - >-
                * ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to
                to enforce weighted round robin distribution.
            - "* LEASTCONNECTION (default) - Select the service with the fewest connections."
            - "* LEASTRESPONSETIME - Select the service with the lowest average response time."
            - "* LEASTBANDWIDTH - Select the service currently handling the least traffic."
            - "* LEASTPACKETS - Select the service currently serving the lowest number of packets per second."
            - "* CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors."
            - >-
                * LRTM - Select the service with the lowest response time. Response times are learned through
                probes. This method also takes the number of active connections into account.
            - >-
                Also available are a number of hashing methods, in which the appliance extracts a predetermined
                of the request, creates a hash of the portion, and then checks whether any previous requests had the
                hash value. If it finds a match, it forwards the request to the service that served those previous
                Following are the hashing methods:
            - "* URLHASH - Create a hash of the request URL (or part of the URL)."
            - >-
                * DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The
                name is taken from either the URL or the Host header. If the domain name appears in both locations,
                URL is preferred. If the request does not contain a domain name, the load balancing method defaults
                LEASTCONNECTION.
            - "* DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header."
            - "* SOURCEIPHASH - Create a hash of the source IP address in the IP header."
            - >-
                * TOKEN - Extract a token from the request, create a hash of the token, and then select the service
                which any previous requests with the same token hash value were sent.
            - >-
                * SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and
                IP address in the IP header.
            - "* SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header."
            - "* CALLIDHASH - Create a hash of the SIP Call-ID header."
            - "* USER_TOKEN - Same as TOKEN LB method but token needs to be provided from an extension."
        type: str

    hashlength:
        description:
            - >-
                Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing
            - "Minimum value = C(1)"
            - "Maximum value = C(4096)"
        type: str

    netmask:
        description:
            - >-
                IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing
                is DESTINATIONIPHASH or SOURCEIPHASH.
            - "Minimum length =  1"
        type: str

    v6netmasklen:
        description:
            - >-
                Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is
                by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.
            - "Minimum value = C(1)"
            - "Maximum value = C(128)"
        type: str

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
        type: str

    cookiename:
        description:
            - >-
                Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of
                with a maximum of 32 characters. If not specified, cookie name is internally generated.
        type: str

    rule:
        description:
            - "Expression, or name of a named expression, against which traffic is evaluated."
            - "The following requirements apply only to the Citrix ADC CLI:"
            - >-
                * If the expression includes one or more spaces, enclose the entire expression in double quotation
            - >-
                * If the expression itself includes double quotation marks, escape the quotations by using the \
            - >-
                * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not
                to escape the double quotation marks.
        type: str

    listenpolicy:
        description:
            - >-
                Expression identifying traffic accepted by the virtual server. Can be either an expression (for
                CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the
                server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.
        type: str

    listenpriority:
        description:
            - >-
                Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If
                request matches the listen policies of more than one virtual server the virtual server whose listen
                has the highest priority (the lowest priority number) accepts the request.
            - "Minimum value = C(0)"
            - "Maximum value = C(101)"
        type: str

    resrule:
        description:
            - >-
                Expression specifying which part of a server's response to use for creating rule based persistence
                (persistence type RULE). Can be either an expression or the name of a named expression.
            - "Example:"
            - "HTTP.RES.HEADER(\\"setcookie\\").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE(\\"server1\\")."
        type: str

    persistmask:
        description:
            - "Persistence mask for IP based persistence types, for IPv4 virtual servers."
            - "Minimum length =  1"
        type: str

    v6persistmasklen:
        description:
            - "Persistence mask for IP based persistence types, for IPv6 virtual servers."
            - "Minimum value = C(1)"
            - "Maximum value = C(128)"
        type: str

    pq:
        description:
            - "Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers."
        type: bool

    sc:
        description:
            - "Use SureConnect on the virtual server."
        type: bool

    rtspnat:
        description:
            - "Use network address translation (NAT) for RTSP data connections."
        type: bool

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
            - >-
                * MAC - Before forwarding a request to a server, change the destination MAC address to the server's
                address. The destination IP address is not changed. MAC-based redirection mode is used mostly in
                load balancing deployments.
            - >-
                * IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the
                IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The
                IP packets are not modified. Applicable to both IPv4 and IPv6 packets.
            - "* TOS - Encode the virtual server's TOS ID in the TOS field of the IP header."
            - "You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR)."
        type: str

    tosid:
        description:
            - >-
                TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.
            - "Minimum value = C(1)"
            - "Maximum value = C(63)"
        type: str

    datalength:
        description:
            - >-
                Length of the token to be extracted from the data segment of an incoming packet, for use in the token
                of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB.
                to virtual servers of type TCP.
            - "Minimum value = C(1)"
            - "Maximum value = C(100)"
        type: str

    dataoffset:
        description:
            - >-
                Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers,
                type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP
            - "Minimum value = C(0)"
            - "Maximum value = C(25400)"
        type: str

    sessionless:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load
                of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where
                information is unnecessary.
        type: str

    trofspersistence:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                When value is ENABLED, Trofs persistence is honored. When value is DISABLED, Trofs persistence is not
        type: str

    connfailover:
        choices:
            - 'DISABLED'
            - 'STATEFUL'
            - 'STATELESS'
        description:
            - >-
                Mode in which the connection failover feature must operate for the virtual server. After a failover,
                TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients
                connected to the same servers. Available settings function as follows:
            - >-
                * STATEFUL - The primary appliance shares state information with the secondary appliance, in real
                resulting in some runtime processing overhead.
            - >-
                * STATELESS - State information is not shared, and the new primary appliance tries to re-create the
                flow on the basis of the information contained in the packets it receives.
            - "* DISABLED - Connection failover does not occur."
        type: str

    redirurl:
        description:
            - "URL to which to redirect traffic if the virtual server becomes unavailable."
            - >-
                WARNING! Make sure that the domain in the URL does not match the domain specified for a content
                policy. If it does, requests are continuously redirected to the unavailable virtual server.
            - "Minimum length =  1"
        type: str

    cacheable:
        description:
            - >-
                Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can
                requests only to a transparent cache redirection virtual server that has an IP address and port
                of *:80, so such a cache redirection virtual server must be configured on the appliance.
        type: bool

    clttimeout:
        description:
            - "Idle time, in seconds, after which a client connection is terminated."
            - "Minimum value = C(0)"
            - "Maximum value = C(31536000)"
        type: int

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
                the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover
                for this setting, because the threshold is implied by the Max Clients settings of bound services.
            - >-
                * BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and
                traffic exceeds the threshold.
            - >-
                * HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below
                threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights
                2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3
                to DOWN.
            - "* NONE - Spillover does not occur."
        type: str

    sopersistence:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                If spillover occurs, maintain source IP address based persistence for both primary and backup virtual
        type: str

    sopersistencetimeout:
        description:
            - "Timeout for spillover persistence, in minutes."
            - "Minimum value = C(2)"
            - "Maximum value = C(1440)"
        type: str

    healththreshold:
        description:
            - >-
                Threshold in percent of active services below which vserver state is made down. If this threshold is
                vserver state will be up even if one bound service is up.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    sothreshold:
        description:
            - >-
                Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a
                value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for
                HEALTH method (do not enter the percentage symbol).
            - "Minimum value = C(1)"
            - "Maximum value = C(4294967287)"
        type: str

    sobackupaction:
        choices:
            - 'DROP'
            - 'ACCEPT'
            - 'REDIRECT'
        description:
            - >-
                Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or
        type: str

    redirectportrewrite:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Rewrite the port and change the protocol to ensure successful HTTP redirects from services."
        type: str

    downstateflush:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                Flush all active transactions associated with a virtual server whose state transitions from UP to
                Do not enable this option for applications that must complete their transactions.
        type: str

    backupvserver:
        description:
            - >-
                Name of the backup virtual server to which to forward requests if the primary virtual server goes
                or reaches its spillover threshold.
            - "Minimum length =  1"
        type: str

    disableprimaryondown:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                If the primary virtual server goes down, do not allow it to return to primary status until manually
        type: str

    insertvserveripport:
        choices:
            - 'OFF'
            - 'VIPADDR'
            - 'V6TOV4MAPPING'
        description:
            - >-
                Insert an HTTP header, whose value is the IP address and port number of the virtual server, before
                a request to the server. The format of the header is <vipHeader>: <virtual server IP address>_<port
                >, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6
                the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If
                have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter
                which IP address is inserted in the header, as follows:
            - >-
                * VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the
                server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.
            - >-
                * V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a
                IPv4 address is not configured, insert the IPv6 address.
            - "* OFF - Disable header insertion."
        type: str

    vipheader:
        description:
            - "Name for the inserted header. The default name is vip-header."
            - "Minimum length =  1"
        type: str

    authenticationhost:
        description:
            - >-
                Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be
                for authentication. Make sure that the Authentication parameter is set to ENABLED.
            - "Minimum length =  3"
            - "Maximum length =  252"
        type: str

    authentication:
        description:
            - "Enable or disable user authentication."
        type: bool

    authn401:
        description:
            - "Enable or disable user authentication with HTTP 401 responses."
        type: bool

    authnvsname:
        description:
            - "Name of an authentication virtual server with which to authenticate users."
            - "Minimum length =  1"
            - "Maximum length =  252"
        type: str

    push:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Process traffic with the push virtual server that is bound to this load balancing virtual server."
        type: str

    pushvserver:
        description:
            - >-
                Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes
                received on the load balancing virtual server that you are configuring.
            - "Minimum length =  1"
        type: str

    pushlabel:
        description:
            - >-
                Expression for extracting a label from the server's response. Can be either an expression or the name
                a named expression.
        type: str

    pushmulticlients:
        description:
            - >-
                Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
        type: bool

    tcpprofilename:
        description:
            - "Name of the TCP profile whose settings are to be applied to the virtual server."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    httpprofilename:
        description:
            - "Name of the HTTP profile whose settings are to be applied to the virtual server."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    dbprofilename:
        description:
            - "Name of the DB profile whose settings are to be applied to the virtual server."
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    comment:
        description:
            - "Any comments that you might want to associate with the virtual server."
        type: str

    l2conn:
        description:
            - >-
                Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source
                port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple
                and non-TCP connections with the same 4-tuple to co-exist on the Citrix ADC.
        type: bool

    oracleserverversion:
        choices:
            - '10G'
            - '11G'
        description:
            - "Oracle server version."
        type: str

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
                if you expect some clients to run a version different from the version of the database. This setting
                compatibility between the client-side and server-side connections by ensuring that all communication
                to the server's version.
        type: str

    mysqlprotocolversion:
        description:
            - "MySQL protocol version that the virtual server advertises to clients."
        type: str

    mysqlserverversion:
        description:
            - "MySQL server version string that the virtual server advertises to clients."
            - "Minimum length =  1"
            - "Maximum length =  31"
        type: str

    mysqlcharacterset:
        description:
            - "Character set that the virtual server advertises to clients."
        type: str

    mysqlservercapabilities:
        description:
            - "Server capabilities that the virtual server advertises to clients."
        type: str

    appflowlog:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Apply AppFlow logging to the virtual server."
        type: str

    netprofile:
        description:
            - >-
                Name of the network profile to associate with the virtual server. If you set this parameter, the
                server uses only the IP addresses in the network profile as source IP addresses when initiating
                with servers.
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    icmpvsrresponse:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - >-
                How the Citrix ADC responds to ping requests received for an IP address that is common to one or more
                servers. Available settings function as follows:
            - >-
                * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always
                to the ping requests.
            - >-
                * If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to
                ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not
            - >-
                * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at
                one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.
            - >-
                Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is
                at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip
                in the CLI or the Create IP dialog box in the GUI.
        type: str

    rhistate:
        choices:
            - 'PASSIVE'
            - 'ACTIVE'
        description:
            - >-
                Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the
                address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to
                the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE)
                on the virtual servers associated with the VIP address:
            - >-
                * If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route
                the VIP address.
            - >-
                * If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the
                address if at least one of the associated virtual servers is in UP state.
            - >-
                * If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route
                the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is
                UP state.
        type: str

    newservicerequest:
        description:
            - >-
                Number of requests, or percentage of the load on existing services, by which to increase the load on
                new service at each interval in slow-start mode. A non-zero value indicates that slow-start is
                A zero value indicates that the global RR startup parameter is applied. Changing the value to zero
                cause services currently in slow start to take the full traffic as determined by the LB method.
                any new services added will use the global RR factor.
        type: str

    newservicerequestunit:
        choices:
            - 'PER_SECOND'
            - 'PERCENT'
        description:
            - "Units in which to increment load at each interval in slow-start mode."
        type: str

    newservicerequestincrementinterval:
        description:
            - >-
                Interval, in seconds, between successive increments in the load on a new service or a service whose
                has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.
            - "Minimum value = C(0)"
            - "Maximum value = C(3600)"
        type: str

    minautoscalemembers:
        description:
            - "Minimum number of members expected to be present when vserver is used in Autoscale."
            - "Minimum value = C(0)"
            - "Maximum value = C(5000)"
        type: str

    maxautoscalemembers:
        description:
            - "Maximum number of members expected to be present when vserver is used in Autoscale."
            - "Minimum value = C(0)"
            - "Maximum value = C(5000)"
        type: str

    persistavpno:
        description:
            - "Persist AVP number for Diameter Persistency."
            - "In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP,"
            - "define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X"
            - "is nested inside AVP Y which is nested in Z, then define the list as  Z Y X."
            - "Minimum value = C(1)"
        type: list
        elements: int

    skippersistency:
        choices:
            - 'Bypass'
            - 'ReLb'
            - 'None'
        description:
            - >-
                This argument decides the behavior incase the service which is selected from an existing persistence
                has reached threshold.
        type: str

    td:
        description:
            - >-
                Integer value that uniquely identifies the traffic domain in which you want to configure the entity.
                you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of
            - "Minimum value = C(0)"
            - "Maximum value = C(4094)"
        type: str

    authnprofile:
        description:
            - "Name of the authentication profile to be used when authentication is turned on."
        type: str

    macmoderetainvlan:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "This option is used to retain vlan information of incoming packet when macmode is enabled."
        type: str

    dbslb:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "Enable database specific load balancing for MySQL and MSSQL service types."
        type: str

    dns64:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - "This argument is for enabling/disabling the dns64 on lbvserver."
        type: str

    bypassaaaa:
        description:
            - >-
                If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns
        type: bool

    recursionavailable:
        description:
            - >-
                When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on.
                one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport
                queries.
        type: bool

    processlocal:
        choices:
            - 'enabled'
            - 'disabled'
        description:
            - >-
                By turning on this option packets destined to a vserver in a cluster will not under go any steering.
                this option for single packet request response mode or when the upstream device is performing a
                RSS for connection based distribution.
        type: str

    dnsprofilename:
        description:
            - >-
                Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to
                transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.
            - "Minimum length =  1"
            - "Maximum length =  127"
        type: str

    lbprofilename:
        description:
            - "Name of the LB profile which is associated to the vserver."
        type: str

    redirectfromport:
        description:
            - "Port number for the virtual server, from which we absorb the traffic for http redirect."
            - "Minimum value = C(1)"
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"
        type: int

    httpsredirecturl:
        description:
            - "URL to which to redirect traffic if the traffic is recieved from redirect port."
        type: str

    retainconnectionsoncluster:
        description:
            - >-
                This option enables you to retain existing connections on a node joining a Cluster system or when a
                is being configured for passive timeout. By default, this option is disabled.
        type: bool

    adfsproxyprofile:
        description:
            - "Name of the adfsProxy profile to be used to support ADFSPIP protocol for ADFS servers."
        type: str

    weight:
        description:
            - "Weight to assign to the specified service."
            - "Minimum value = C(1)"
            - "Maximum value = C(100)"
        type: str

    servicename:
        description:
            - "Service to bind to the virtual server."
            - "Minimum length =  1"
        type: str

    redirurlflags:
        description:
            - "The redirect URL to be unset."
        type: bool


    disabled:
        description:
            - When set to C(true) the server state will be set to C(disabled).
            - When set to C(false) the server state will be set to C(enabled).
        type: bool
        default: false

    ssl_certkey:
        type: str
        description:
            - The name of the ssl certificate that is bound to this service.
            - The ssl certificate must already exist.
            - Creating the certificate can be done with the M(citrix_adc_ssl_certkey) module.
            - This option is only applicable only when C(servicetype) is C(SSL).

    servicebindings:
        type: list
        elements: dict
        description:
            - List of services along with the weights that are load balanced.
            - The following suboptions are available.
        suboptions:
            servicename:
                description:
                    - "Service to bind to the virtual server."
                    - "Minimum length =  1"
                type: str
            weight:
                description:
                    - "Weight to assign to the specified service."
                    - "Minimum value = C(1)"
                    - "Maximum value = C(100)"
                type: str

    servicegroupbindings:
        type: list
        elements: dict
        description:
            - List of services along with the weights that are load balanced.
            - The following suboptions are available.
        suboptions:
            servicegroupname:
                description:
                    - "The service group name bound to the selected load balancing virtual server."
                type: str
            weight:
                description:
                    - >-
                        Integer specifying the weight of the service. A larger number specifies a greater weight. Defines the
                        of the service relative to the other services in the load balancing configuration. Determines the
                        given to the service in load balancing decisions.
                    - "Minimum value = C(1)"
                    - "Maximum value = C(100)"
                type: str

    appfw_policybindings:
        type: list
        elements: dict
        description:
            - List of services along with the weights that are load balanced.
            - The following suboptions are available.
        suboptions:
            policyname:
                description:
                    - "Name of the policy bound to the LB vserver."
                type: str
            priority:
                description:
                    - "Priority."
                type: str
            gotopriorityexpression:
                description:
                    - >-
                        Expression specifying the priority of the next policy which will get evaluated if the current policy
                        evaluates to TRUE.
                type: str
            bindpoint:
                choices:
                    - 'REQUEST'
                    - 'RESPONSE'
                description:
                    - "The bindpoint to which the policy is bound."
                type: str
            invoke:
                description:
                    - "Invoke policies bound to a virtual server or policy label."
                type: bool
            labeltype:
                choices:
                    - 'reqvserver'
                    - 'resvserver'
                    - 'policylabel'
                description:
                    - "The invocation type."
                type: str
            labelname:
                description:
                    - "Name of the label invoked."
                type: str

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
# Citrix ADC services service-http-1, service-http-2 must have been already created with the citrix_adc_service module

- name: Create a load balancing vserver bound to services
  delegate_to: localhost
  citrix_adc_lb_vserver:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    validate_certs: no

    state: present

    name: lb_vserver_1
    servicetype: HTTP
    timeout: 12
    ipv46: 6.93.3.3
    port: 80
    servicebindings:
        - servicename: service-http-1
          weight: 80
        - servicename: service-http-2
          weight: 20

# Service group service-group-1 must have been already created with the citrix_adc_servicegroup module

- name: Create load balancing vserver bound to servicegroup
  delegate_to: localhost
  citrix_adc_lb_vserver:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    validate_certs: no
    state: present

    name: lb_vserver_2
    servicetype: HTTP
    ipv46: 6.92.2.2
    port: 80
    timeout: 10
    servicegroupbindings:
        - servicegroupname: service-group-1
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines,
    NitroAPIFetcher
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)
        self.main_nitro_class = 'lbvserver'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'lbvserver': {
                'attributes_list': [
                    'name',
                    'servicetype',
                    'ipv46',
                    'ippattern',
                    'ipmask',
                    'port',
                    'ipset',
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
                    'trofspersistence',
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
                    'retainconnectionsoncluster',
                    'adfsproxyprofile',
                    'weight',
                    'servicename',
                    'redirurlflags',
                ],
                'transforms': {
                    'pq': lambda v: 'ON' if v else 'OFF',
                    'sc': lambda v: 'ON' if v else 'OFF',
                    'rtspnat': lambda v: 'ON' if v else 'OFF',
                    'sessionless': lambda v: v.upper(),
                    'trofspersistence': lambda v: v.upper(),
                    'cacheable': lambda v: 'YES' if v else 'NO',
                    'sopersistence': lambda v: v.upper(),
                    'redirectportrewrite': lambda v: v.upper(),
                    'downstateflush': lambda v: v.upper(),
                    'disableprimaryondown': lambda v: v.upper(),
                    'authentication': lambda v: 'ON' if v else 'OFF',
                    'authn401': lambda v: 'ON' if v else 'OFF',
                    'push': lambda v: v.upper(),
                    'pushmulticlients': lambda v: 'YES' if v else 'NO',
                    'l2conn': lambda v: 'ON' if v else 'OFF',
                    'appflowlog': lambda v: v.upper(),
                    'macmoderetainvlan': lambda v: v.upper(),
                    'dbslb': lambda v: v.upper(),
                    'dns64': lambda v: v.upper(),
                    'bypassaaaa': lambda v: 'YES' if v else 'NO',
                    'recursionavailable': lambda v: 'YES' if v else 'NO',
                    'processlocal': lambda v: v.upper(),
                    'retainconnectionsoncluster': lambda v: 'YES' if v else 'NO',
                    'clttimeout': str,
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'name',
                ],
                'non_updateable_attributes': [
                    'servicetype',
                    'port',
                    'range',
                    'state',
                    'td',
                    'redirurlflags',
                    'newname',
                ],
            },
            'servicebindings': {
                'attributes_list': [
                    'servicename',
                    'weight',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'servicename',
                ]
            },
            'servicegroupbindings': {
                'attributes_list': [
                    'servicegroupname',
                    'weight',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'servicegroupname',
                ]
            },
            'appfw_policybindings': {
                'attributes_list': [
                    'policyname',
                    'priority',
                    'gotopriorityexpression',
                    'bindpoint',
                    'invoke',
                    'labeltype',
                    'labelname',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'name',
                ],
                'delete_id_attributes': [
                    'policyname',
                    'priority',
                    'bindpoint',
                    'name',
                ]
            },
        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        # Calculate functions will apply transforms to values read from playbook
        self.calculate_configured_lbvserver()
        self.calculate_configured_service_bindings()
        self.calculate_configured_servicegroup_bindings()
        self.calculate_configured_appfwpolicy_bindings()

    def calculate_configured_lbvserver(self):
        log('ModuleExecutor.calculate_configured_lbvserver()')
        self.configured_lbvserver = {}
        for attribute in self.attribute_config['lbvserver']['attributes_list']:
            value = self.module.params.get(attribute)
            # Skip null values
            if value is None:
                continue
            transform = self.attribute_config['lbvserver']['transforms'].get(attribute)
            if transform is not None:
                value = transform(value)
            self.configured_lbvserver[attribute] = value

        log('calculated configured lbvserver %s' % self.configured_lbvserver)

    def calculate_configured_service_bindings(self):
        log('ModuleExecutor.calculate_configured_service_bindings()')
        self.configured_service_bindings = []
        if self.module.params.get('servicebindings') is None:
            return
        for service in self.module.params['servicebindings']:
            binding = {}
            binding['name'] = self.module.params['name']
            for attribute in self.attribute_config['servicebindings']['attributes_list']:
                # Disregard null values
                value = service.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['servicebindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_service_bindings.append(binding)
        log('calculated configured service bindings %s' % self.configured_service_bindings)

    def calculate_configured_servicegroup_bindings(self):
        log('ModuleExecutor.calculate_configured_servicegroup_bindings()')
        self.configured_servicegroup_bindings = []
        if self.module.params.get('servicegroupbindings') is None:
            return
        for servicegroup in self.module.params['servicegroupbindings']:
            binding = {}
            binding['name'] = self.module.params['name']
            for attribute in self.attribute_config['servicegroupbindings']['attributes_list']:
                # Disregard null values
                value = servicegroup.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['servicegroupbindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_servicegroup_bindings.append(binding)
        log('calculated configured servicegroup bindings %s' % self.configured_servicegroup_bindings)

    def calculate_configured_appfwpolicy_bindings(self):
        log('ModuleExecutor.calculate_configured_appfwpolicy_bindings()')
        self.configured_appfwpolicy_bindings = []
        if self.module.params.get('appfw_policybindings') is None:
            return
        for appfwpolicy in self.module.params['appfw_policybindings']:
            binding = {}
            binding['name'] = self.module.params['name']
            for attribute in self.attribute_config['appfw_policybindings']['attributes_list']:
                # Disregard null values
                value = appfwpolicy.get(attribute)
                if value is None:
                    continue
                transform = self.attribute_config['appfw_policybindings']['transforms'].get(attribute)
                if transform is not None:
                    value = transform(value)
                binding[attribute] = value
            self.configured_appfwpolicy_bindings.append(binding)
        log('calculated configured appfwpolicy bindings %s' % self.configured_appfwpolicy_bindings)

    def lbvserver_exists(self):
        log('ModuleExecutor.lbvserver_exists()')
        result = self.fetcher.get('lbvserver', self.module.params['name'])

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            return True
        elif result['nitro_errorcode'] == 258:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def create_lbvserver(self):
        log('ModuleExecutor.create_lbvserver()')

        post_data = {
            'lbvserver': self.configured_lbvserver
        }

        result = self.fetcher.post(post_data=post_data, resource='lbvserver')
        log('post data: %s' % post_data)
        log('result of post: %s' % result)
        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def update_lbvserver(self):
        log('ModuleExecutor.update_lbvserver()')

        # Catching trying to change non updateable attributes is done in self.lbvserver_identical()
        put_payload = copy.deepcopy(self.configured_lbvserver)
        for attribute in self.configured_lbvserver.keys():
            if attribute in self.attribute_config['lbvserver']['non_updateable_attributes']:
                del put_payload[attribute]

        put_data = {
            'lbvserver': put_payload
        }

        log('request put data: %s' % put_data)
        result = self.fetcher.put(put_data=put_data, resource='lbvserver')

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def lbvserver_identical(self):
        log('ModuleExecutor.lbvserver_identical()')
        result = self.fetcher.get('lbvserver', self.module.params['name'])
        retrieved_object = result['data']['lbvserver'][0]

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        diff_list = []
        non_updateable_list = []
        # Iterate over keys that already exist in the playbook
        for attribute in self.configured_lbvserver.keys():
            retrieved_value = retrieved_object.get(attribute)
            configured_value = self.configured_lbvserver.get(attribute)
            if retrieved_value != configured_value:
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                diff_list.append('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                # Also append changed values to the non updateable list
                if attribute in self.attribute_config['lbvserver']['non_updateable_attributes']:
                    non_updateable_list.append(attribute)

        self.module_result['diff_list'] = diff_list
        if non_updateable_list != []:
            msg = 'Cannot change value for the following non updateable attributes %s' % non_updateable_list
            self.module.fail_json(msg=msg, **self.module_result)

        if diff_list != []:
            return False
        else:
            return True

    def update_or_create(self):
        log('ModuleExecutor.update_or_create()')

        # Create or update main object
        if not self.lbvserver_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                log('lbvserver does not exist. Will create.')
                self.create_lbvserver()
        else:
            if not self.lbvserver_identical():
                log('Existing lbvserver does not have identical values to configured. Will update.')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.update_lbvserver()
            else:
                log('Existing lbvserver has identical values to configured.')

        # This will also take into account check mode
        self.sync_bindings()

    def delete_lbvserver(self):
        log('ModuleExecutor.delete_lbvserver()')

        # First unbind any existing appfwpolicies
        self.configured_appfwpolicy_bindings = []
        self.sync_appfwpolicy_bindings()

        result = self.fetcher.delete(resource='lbvserver', id=self.module.params['name'])
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete(self):
        log('ModuleExecutor.delete()')

        if self.lbvserver_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.delete_lbvserver()

    def _get_transformed_dict(self, transforms, values_dict):
        actual_values_dict = {}
        for key in values_dict:
            value = values_dict.get(key)
            transform = transforms.get(key)
            if transform is not None:
                value = transform(values_dict.get(key))
            actual_values_dict[key] = value

        return actual_values_dict

    def get_existing_service_bindings(self):
        log('ModuleExecutor.get_existing_service_bindings()')
        result = self.fetcher.get('lbvserver_service_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'lbvserver_service_binding' in result['data']:
            return result['data']['lbvserver_service_binding']
        else:
            return []

    def add_service_binding(self, configured_dict):
        log('ModuleExecutor.add_service_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.module.params['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['servicebindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'lbvserver_service_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='lbvserver_service_binding',
            id=self.module.params['name'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_service_binding(self, configured_dict):
        log('ModuleExecutor.delete_service_binding()')

        service_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['servicebindings']['delete_id_attributes']:
            value = service_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='lbvserver_service_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def service_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.service_binding_identical()')

        ret_val = True
        for key in configured.keys():
            configured_value = configured.get(key)
            retrieved_value = retrieved.get(key)
            if configured_value != retrieved_value:
                str_tuple = (
                    key,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                log('Service binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_service_bindings(self):
        log('ModuleExecutor.sync_service_bindings()')

        # Parent lbvserver should already exist
        existing_service_bindings = self.get_existing_service_bindings()

        log('existing_service_bindings %s' % existing_service_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_service_binding in existing_service_bindings:
            for configured_service_binding in self.configured_service_bindings:
                if self.service_binding_identical(configured_service_binding, existing_service_binding):
                    configured_already_present.append(configured_service_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.delete_service_binding(existing_service_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_service_binding in self.configured_service_bindings:
            if configured_service_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.add_service_binding(configured_service_binding)

    def get_existing_servicegroup_bindings(self):
        log('ModuleExecutor.get_existing_servicegroup_bindings()')
        result = self.fetcher.get('lbvserver_servicegroup_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'lbvserver_servicegroup_binding' in result['data']:
            return result['data']['lbvserver_servicegroup_binding']
        else:
            return []

    def add_servicegroup_binding(self, configured_dict):
        log('ModuleExecutor.add_servicegroup_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.module.params['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['servicegroupbindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'lbvserver_servicegroup_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='lbvserver_servicegroup_binding',
            id=self.module.params['name'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_servicegroup_binding(self, configured_dict):
        log('ModuleExecutor.delete_servicegroup_binding()')

        servicegroup_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['servicegroupbindings']['delete_id_attributes']:
            value = servicegroup_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='lbvserver_servicegroup_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def servicegroup_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.servicegroup_binding_identical()')

        ret_val = True
        for key in configured.keys():
            configured_value = configured.get(key)
            retrieved_value = retrieved.get(key)
            if configured_value != retrieved_value:
                str_tuple = (
                    key,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                log('Servicegroup binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_servicegroup_bindings(self):
        log('ModuleExecutor.sync_servicegroup_bindings()')

        # Parent lbvserver should already exist
        existing_servicegroup_bindings = self.get_existing_servicegroup_bindings()

        log('existing_servicegroup_bindings %s' % existing_servicegroup_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_servicegroup_binding in existing_servicegroup_bindings:
            for configured_servicegroup_binding in self.configured_servicegroup_bindings:
                if self.servicegroup_binding_identical(configured_servicegroup_binding, existing_servicegroup_binding):
                    configured_already_present.append(configured_servicegroup_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.delete_servicegroup_binding(existing_servicegroup_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_servicegroup_binding in self.configured_servicegroup_bindings:
            if configured_servicegroup_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.add_servicegroup_binding(configured_servicegroup_binding)

    def get_existing_appfwpolicy_bindings(self):
        log('ModuleExecutor.get_existing_appfwpolicy_bindings()')
        result = self.fetcher.get('lbvserver_appfwpolicy_binding', self.module.params['name'])

        if result['nitro_errorcode'] == 258:
            return []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'lbvserver_appfwpolicy_binding' in result['data']:
            return result['data']['lbvserver_appfwpolicy_binding']
        else:
            return []

    def add_appfwpolicy_binding(self, configured_dict):
        log('ModuleExecutor.add_appfwpolicy_binding()')

        put_values = copy.deepcopy(configured_dict)
        put_values['name'] = self.module.params['name']
        put_values = self._get_transformed_dict(
            transforms=self.attribute_config['appfw_policybindings']['transforms'],
            values_dict=put_values
        )
        put_data = {'lbvserver_appfwpolicy_binding': put_values}
        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='lbvserver_appfwpolicy_binding',
            id=self.module.params['name'],
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_appfwpolicy_binding(self, configured_dict):
        log('ModuleExecutor.delete_appfwpolicy_binding()')

        appfwpolicy_binding = copy.deepcopy(configured_dict)

        args = {}
        for attribute in self.attribute_config['appfw_policybindings']['delete_id_attributes']:
            value = appfwpolicy_binding.get(attribute)
            if value is not None and value != '':
                log('Appending to args %s:%s' % (attribute, value))
                args[attribute] = value

        result = self.fetcher.delete(
            resource='lbvserver_appfwpolicy_binding',
            id=self.module.params['name'],
            args=args
        )

        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def appfwpolicy_binding_identical(self, configured, retrieved):
        log('ModuleExecutor.appfwpolicy_binding_identical()')

        ret_val = True
        for key in configured.keys():
            configured_value = configured.get(key)
            retrieved_value = retrieved.get(key)
            if configured_value != retrieved_value:
                str_tuple = (
                    key,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                log('Appfwpolicy binding attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)
                ret_val = False
        return ret_val

    def sync_appfwpolicy_bindings(self):
        log('ModuleExecutor.sync_appfwpolicy_bindings()')

        # Parent lbvserver should already exist
        existing_appfwpolicy_bindings = self.get_existing_appfwpolicy_bindings()

        log('existing_appfwpolicy_bindings %s' % existing_appfwpolicy_bindings)

        # First get the existing bindings
        configured_already_present = []

        # Delete any binding that is not exactly as the configured
        for existing_appfwpolicy_binding in existing_appfwpolicy_bindings:
            for configured_appfwpolicy_binding in self.configured_appfwpolicy_bindings:
                if self.appfwpolicy_binding_identical(configured_appfwpolicy_binding, existing_appfwpolicy_binding):
                    configured_already_present.append(configured_appfwpolicy_binding)
                    break
            else:
                log('Will delete binding')
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.delete_appfwpolicy_binding(existing_appfwpolicy_binding)

        # Create the bindings objects that we marked in previous loop
        log('configured_already_present %s' % configured_already_present)
        for configured_appfwpolicy_binding in self.configured_appfwpolicy_bindings:
            if configured_appfwpolicy_binding in configured_already_present:
                log('Configured binding already exists')
                continue
            else:
                log('Configured binding does not already exist')
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.add_appfwpolicy_binding(configured_appfwpolicy_binding)

    def add_sslcertkey_binding(self, sslcertkey):
        log('ModuleExecutor.add_sslcertkey_binding()')

        put_data = {
            'sslvserver_sslcertkey_binding': {
                'vservername': self.module.params['name'],
                'certkeyname': sslcertkey,
            }
        }

        log('put data %s' % put_data)
        result = self.fetcher.put(
            put_data=put_data,
            resource='sslvserver_sslcertkey_binding',
        )

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def delete_sslcertkey_binding(self, sslcertkey):
        log('ModuleExecutor.delete_sslcertkey_binding()')

        args = {
            'certkeyname': sslcertkey,
        }

        result = self.fetcher.delete(
            resource='sslvserver_sslcertkey_binding',
            id=self.module.params['name'],
            args=args
        )

    def sync_sslcertkey_bindings(self):
        log('ModuleExecutor.sync_sslcertkey_bindings()')

        # Read for the existing binding
        bound_lbvserver = None
        result = self.fetcher.get('sslvserver_sslcertkey_binding', self.module.params['name'])

        if result['nitro_errorcode'] in [461, 1544]:
            bound_sslcertkeys = []
        elif result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        elif 'sslvserver_sslcertkey_binding' in result['data']:
            bound_sslcertkeys = result['data']['sslvserver_sslcertkey_binding']
        else:
            bound_sslcertkeys = []

        configured_sslcertkey = self.module.params.get('ssl_certkey')
        found_configured = False

        # Delete all keys that do not match
        for binding in bound_sslcertkeys:
            if binding['certkeyname'] != configured_sslcertkey:
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.delete_sslcertkey_binding(binding['certkeyname'])
            else:
                found_configured = True

        # Add if not found
        if configured_sslcertkey is not None and not found_configured:
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.add_sslcertkey_binding(configured_sslcertkey)

    def sync_bindings(self):
        log('ModuleExecutor.sync_bindings()')
        self.sync_service_bindings()
        self.sync_servicegroup_bindings()
        self.sync_appfwpolicy_bindings()
        self.sync_sslcertkey_bindings()

    def do_state_change(self):
        log('ModuleExecutor.do_state_change()')
        if self.module.check_mode:
            return

        # Fallthrough
        post_data = {
            'lbvserver': {
                'name': self.configured_lbvserver['name'],
            }
        }

        disabled = self.module.params['disabled']

        if disabled:
            action = 'disable'
        else:
            action = 'enable'

        log('disable/enable post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource='lbvserver', action=action)
        log('result of post %s' % result)

        if result['http_response_data']['status'] != 200:
            msg = 'Disable/Enable operation failed'
            self.module.fail_json(msg=msg, **self.module_result)

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create()
                self.do_state_change()
            elif self.module.params['state'] == 'absent':
                self.delete()

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

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
                'PROXY',
                'USER_TCP',
                'USER_SSL_TCP',
                'QUIC',
                'IPFIX',
                'LOGSTREAM',
            ],
        ),
        ipv46=dict(type='str'),
        ippattern=dict(type='str'),
        ipmask=dict(type='str'),
        port=dict(type='int'),
        ipset=dict(type='str'),
        range=dict(type='str'),
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
                'USERSESSION',
                'NONE',
            ],
        ),
        timeout=dict(type='int'),
        persistencebackup=dict(
            type='str',
            choices=[
                'SOURCEIP',
                'NONE',
            ],
        ),
        backuppersistencetimeout=dict(type='int'),
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
                'USER_TOKEN',
            ],
        ),
        hashlength=dict(type='str'),
        netmask=dict(type='str'),
        v6netmasklen=dict(type='str'),
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
            ],
        ),
        cookiename=dict(type='str'),
        rule=dict(type='str'),
        listenpolicy=dict(type='str'),
        listenpriority=dict(type='str'),
        resrule=dict(type='str'),
        persistmask=dict(type='str'),
        v6persistmasklen=dict(type='str'),
        pq=dict(type='bool'),
        sc=dict(type='bool'),
        rtspnat=dict(type='bool'),
        m=dict(
            type='str',
            choices=[
                'IP',
                'MAC',
                'IPTUNNEL',
                'TOS',
            ],
        ),
        tosid=dict(type='str'),
        datalength=dict(type='str'),
        dataoffset=dict(type='str'),
        sessionless=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        trofspersistence=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        connfailover=dict(
            type='str',
            choices=[
                'DISABLED',
                'STATEFUL',
                'STATELESS',
            ],
        ),
        redirurl=dict(type='str'),
        cacheable=dict(type='bool'),
        clttimeout=dict(type='int'),
        somethod=dict(
            type='str',
            choices=[
                'CONNECTION',
                'DYNAMICCONNECTION',
                'BANDWIDTH',
                'HEALTH',
                'NONE',
            ],
        ),
        sopersistence=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        sopersistencetimeout=dict(type='str'),
        healththreshold=dict(type='str'),
        sothreshold=dict(type='str'),
        sobackupaction=dict(
            type='str',
            choices=[
                'DROP',
                'ACCEPT',
                'REDIRECT',
            ],
        ),
        redirectportrewrite=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        downstateflush=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        backupvserver=dict(type='str'),
        disableprimaryondown=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        insertvserveripport=dict(
            type='str',
            choices=[
                'OFF',
                'VIPADDR',
                'V6TOV4MAPPING',
            ],
        ),
        vipheader=dict(type='str'),
        authenticationhost=dict(type='str'),
        authentication=dict(type='bool'),
        authn401=dict(type='bool'),
        authnvsname=dict(type='str'),
        push=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        pushvserver=dict(type='str'),
        pushlabel=dict(type='str'),
        pushmulticlients=dict(type='bool'),
        tcpprofilename=dict(type='str'),
        httpprofilename=dict(type='str'),
        dbprofilename=dict(type='str'),
        comment=dict(type='str'),
        l2conn=dict(type='bool'),
        oracleserverversion=dict(
            type='str',
            choices=[
                '10G',
                '11G',
            ],
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
            ],
        ),
        mysqlprotocolversion=dict(type='str'),
        mysqlserverversion=dict(type='str'),
        mysqlcharacterset=dict(type='str'),
        mysqlservercapabilities=dict(type='str'),
        appflowlog=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        netprofile=dict(type='str'),
        icmpvsrresponse=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ],
        ),
        rhistate=dict(
            type='str',
            choices=[
                'PASSIVE',
                'ACTIVE',
            ],
        ),
        newservicerequest=dict(type='str'),
        newservicerequestunit=dict(
            type='str',
            choices=[
                'PER_SECOND',
                'PERCENT',
            ],
        ),
        newservicerequestincrementinterval=dict(type='str'),
        minautoscalemembers=dict(type='str'),
        maxautoscalemembers=dict(type='str'),
        persistavpno=dict(
            type='list',
            elements='int',
        ),
        skippersistency=dict(
            type='str',
            choices=[
                'Bypass',
                'ReLb',
                'None',
            ],
        ),
        td=dict(type='str'),
        authnprofile=dict(type='str'),
        macmoderetainvlan=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        dbslb=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        dns64=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        bypassaaaa=dict(type='bool'),
        recursionavailable=dict(type='bool'),
        processlocal=dict(
            type='str',
            choices=[
                'enabled',
                'disabled',
            ],
        ),
        dnsprofilename=dict(type='str'),
        lbprofilename=dict(type='str'),
        redirectfromport=dict(type='int'),
        httpsredirecturl=dict(type='str'),
        retainconnectionsoncluster=dict(type='bool'),
        adfsproxyprofile=dict(type='str'),
        weight=dict(type='str'),
        servicename=dict(type='str'),
        redirurlflags=dict(type='bool'),

        disabled=dict(
            type='bool',
            default=False,
        ),
        ssl_certkey=dict(type='str'),

        servicebindings=dict(
            type='list',
            elements='dict',
            options=dict(
                servicename=dict(type='str'),
                weight=dict(type='str'),
            ),
        ),

        servicegroupbindings=dict(
            type='list',
            elements='dict',
            options=dict(
                servicegroupname=dict(type='str'),
                weight=dict(type='str'),
            ),
        ),

        appfw_policybindings=dict(
            type='list',
            elements='dict',
            options=dict(
                policyname=dict(type='str'),
                priority=dict(type='str'),
                gotopriorityexpression=dict(type='str'),
                bindpoint=dict(
                    type='str',
                    choices=[
                        'REQUEST',
                        'RESPONSE',
                    ]
                ),
                invoke=dict(type='bool'),
                labeltype=dict(
                    type='str',
                    choices=[
                        'reqvserver',
                        'resvserver',
                        'policylabel',
                    ]
                ),
                labelname=dict(type='str'),
            ),
        ),
    )

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
