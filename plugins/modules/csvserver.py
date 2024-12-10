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
module: csvserver
short_description: Configuration for CS virtual server resource.
description: Configuration for CS virtual server resource.
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
  apiprofile:
    type: str
    description:
      - The API profile where one or more API specs are bounded to.
  appflowlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging appflow flow information
  authentication:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Authenticate users who request a connection to the content switching virtual
        server.
  authenticationhost:
    type: str
    description:
      - FQDN of the authentication virtual server. The service type of the virtual
        server should be either HTTP or SSL.
  authn401:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable HTTP 401-response based authentication.
  authnprofile:
    type: str
    description:
      - Name of the authentication profile to be used when authentication is turned
        on.
  authnvsname:
    type: str
    description:
      - Name of authentication virtual server that authenticates the incoming user
        requests to this content switching virtual server.
  backupip:
    type: str
    description:
      - '0'
  backuppersistencetimeout:
    type: float
    description:
      - Time period for which backup persistence is in effect.
  backupvserver:
    type: str
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
  cacheable:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use this option to specify whether a virtual server, used for load balancing
        or content switching, routes requests to the cache redirection virtual server
        before sending it to the configured servers.
  casesensitive:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Consider case in URLs (for policies that use URLs instead of RULES). For example,
        with the C(ON) setting, the URLs /a/1.html and /A/1.HTML are treated differently
        and can have different targets (set by content switching policies). With the
        C(OFF) setting, /a/1.html and /A/1.HTML are switched to the same target.
  clttimeout:
    type: float
    description:
      - 'Idle time, in seconds, after which the client connection is terminated. The
        default values are:'
      - 180 seconds for HTTP/SSL-based services.
      - 9000 seconds for other TCP-based services.
      - 120 seconds for DNS-based services.
      - 120 seconds for other UDP-based services.
  comment:
    type: str
    description:
      - Information about this virtual server.
  cookiedomain:
    type: str
    description:
      - '0'
  cookiename:
    type: str
    description:
      - Use this parameter to  specify the cookie name for COOKIE peristence type.
        It specifies the name of cookie with a maximum of 32 characters. If not specified,
        cookie name is internally generated.
  cookietimeout:
    type: float
    description:
      - '0'
  dbprofilename:
    type: str
    description:
      - Name of the DB profile.
  disableprimaryondown:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Continue forwarding the traffic to backup virtual server even after the primary
        server comes UP from the DOWN state.
  dnsprofilename:
    type: str
    description:
      - Name of the DNS profile to be associated with the VServer. DNS profile properties
        will applied to the transactions processed by a VServer. This parameter is
        valid only for DNS and DNS-TCP VServers.
  dnsrecordtype:
    type: str
    choices:
      - A
      - AAAA
      - CNAME
      - NAPTR
    description:
      - '0'
  domainname:
    type: str
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
  downstateflush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with a virtual server whose state
        transitions from UP to DOWN. Do not enable this option for applications that
        must complete their transactions.
  dtls:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option starts/stops the dtls service on the vserver
  httpprofilename:
    type: str
    description:
      - Name of the HTTP profile containing HTTP configuration settings for the virtual
        server. The service type of the virtual server should be either HTTP or SSL.
  httpsredirecturl:
    type: str
    description:
      - URL to which all HTTP traffic received on the port specified in the -redirectFromPort
        parameter is redirected.
  icmpvsrresponse:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - Can be active or passive
  insertvserveripport:
    type: str
    choices:
      - 'OFF'
      - VIPADDR
      - V6TOV4MAPPING
    description:
      - 'Insert the virtual server''s VIP address and port number in the request header.
        Available values function as follows:'
      - '        C(VIPADDR) - Header contains the vserver''s IP address and port number
        without any translation.'
      - '        C(OFF)     - The virtual IP and port header insertion option is disabled.'
      - '        C(V6TOV4MAPPING) - Header contains the mapped IPv4 address corresponding
        to the IPv6 address of the vserver and the port number. An IPv6 address can
        be mapped to a user-specified IPv4 address using the set ns ip6 command.'
  ipmask:
    type: str
    description:
      - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have
        leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255).
        Accordingly, the mask specifies whether the first n bits or the last n bits
        of the destination IP address in a client request are to be matched with the
        corresponding bits in the IP pattern. The former is called a forward mask.
        The latter is called a reverse mask.
  ippattern:
    type: str
    description:
      - IP address pattern, in dotted decimal notation, for identifying packets to
        be accepted by the virtual server. The IP Mask parameter specifies which part
        of the destination IP address is matched against the pattern. Mutually exclusive
        with the IP Address parameter.
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
  ipset:
    type: str
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current cs vserver
  ipv46:
    type: str
    description:
      - IP address of the content switching virtual server.
  l2conn:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use L2 Parameters to identify a connection
  listenpolicy:
    type: str
    description:
      - String specifying the listen policy for the content switching virtual server.
        Can be either the name of an existing expression or an in-line expression.
  listenpriority:
    type: float
    description:
      - Integer specifying the priority of the listen policy. A higher number specifies
        a lower priority. If a request matches the listen policies of more than one
        virtual server the virtual server whose listen policy has the highest priority
        (the lowest priority number) accepts the request.
  mssqlserverversion:
    type: str
    choices:
      - '70'
      - '2000'
      - 2000SP1
      - '2005'
      - '2008'
      - 2008R2
      - '2012'
      - '2014'
    description:
      - The version of the MSSQL server
  mysqlcharacterset:
    type: float
    description:
      - The character set returned by the mysql vserver.
  mysqlprotocolversion:
    type: float
    description:
      - The protocol version returned by the mysql vserver.
  mysqlservercapabilities:
    type: float
    description:
      - The server capabilities returned by the mysql vserver.
  mysqlserverversion:
    type: str
    description:
      - The server version string returned by the mysql vserver.
  name:
    type: str
    description:
      - Name for the content switching virtual server. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters.
      - Cannot be changed after the CS virtual server is created.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, my server or my server).
  netprofile:
    type: str
    description:
      - The name of the network profile.
  newname:
    type: str
    description:
      - New name for the virtual server. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my name" or 'my name').
  oracleserverversion:
    type: str
    choices:
      - 10G
      - 11G
    description:
      - Oracle server version
  persistencebackup:
    type: str
    choices:
      - SOURCEIP
      - NONE
    description:
      - Backup persistence type for the virtual server. Becomes operational if the
        primary persistence mechanism fails.
  persistenceid:
    type: float
    description:
      - '0'
  persistencetype:
    type: str
    choices:
      - SOURCEIP
      - COOKIEINSERT
      - SSLSESSION
      - NONE
    description:
      - 'Type of persistence for the virtual server. Available settings function as
        follows:'
      - '* C(SOURCEIP) - Connections from the same client IP address belong to the
        same persistence session.'
      - '* C(COOKIEINSERT) - Connections that have the same HTTP Cookie, inserted
        by a Set-Cookie directive from a server, belong to the same persistence session.'
      - '* C(SSLSESSION) - Connections that have the same SSL Session ID belong to
        the same persistence session.'
  persistmask:
    type: str
    description:
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.
  port:
    type: int
    description:
      - Port number for content switching virtual server.
  precedence:
    type: str
    choices:
      - RULE
      - URL
    description:
      - Type of precedence to use for both C(RULE)-based and C(URL)-based policies
        on the content switching virtual server. With the default (C(RULE)) setting,
        incoming requests are evaluated against the rule-based content switching policies.
        If none of the rules match, the C(URL) in the request is evaluated against
        the C(URL)-based content switching policies.
  probeport:
    type: int
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select port for HTTP/TCP monitring
  probeprotocol:
    type: str
    choices:
      - TCP
      - HTTP
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select C(HTTP) or C(TCP) probes for healthcheck
  probesuccessresponsecode:
    type: str
    description:
      - HTTP code to return in SUCCESS case.
  push:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Process traffic with the push virtual server that is bound to this content
        switching virtual server (specified by the Push VServer parameter). The service
        type of the push virtual server should be either HTTP or SSL.
  pushlabel:
    type: str
    description:
      - Expression for extracting the label from the response received from server.
        This string can be either an existing rule name or an inline expression. The
        service type of the virtual server should be either HTTP or SSL.
  pushmulticlients:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Allow multiple Web 2.0 connections from the same client to connect to the
        virtual server and expect updates.
  pushvserver:
    type: str
    description:
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which
        the server pushes updates received on the client-facing load balancing virtual
        server.
  quicprofilename:
    type: str
    description:
      - Name of QUIC profile which will be attached to the Content Switching VServer.
  range:
    type: float
    description:
      - Number of consecutive IP addresses, starting with the address specified by
        the IP Address parameter, to include in a range of addresses assigned to this
        virtual server.
  redirectfromport:
    type: int
    description:
      - Port number for the virtual server, from which we absorb the traffic for http
        redirect
  redirectportrewrite:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of port rewrite while performing HTTP redirect.
  redirecturl:
    type: str
    description:
      - URL to which traffic is redirected if the virtual server becomes unavailable.
        The service type of the virtual server should be either HTTP or SSL.
      - 'Caution: Make sure that the domain in the URL does not match the domain specified
        for a content switching policy. If it does, requests are continuously redirected
        to the unavailable virtual server.'
  rhistate:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - A host route is injected according to the setting on the virtual servers
      - '            * If set to C(PASSIVE) on all the virtual servers that share
        the IP address, the appliance always injects the hostroute.'
      - '            * If set to C(ACTIVE) on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to C(ACTIVE) on some virtual servers and C(PASSIVE)
        on the others, the appliance, injects even if one virtual server set to C(ACTIVE)
        is UP.'
  rtspnat:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable network address translation (NAT) for real-time streaming protocol
        (RTSP) connections.
  servicetype:
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
      - DOT
      - SSL_PROXY
    description:
      - Protocol used by the virtual server.
  sitedomainttl:
    type: float
    description:
      - '0'
  sobackupaction:
    type: str
    choices:
      - DROP
      - ACCEPT
      - REDIRECT
    description:
      - Action to be performed if spillover is to take effect, but no backup chain
        to spillover is usable or exists
  somethod:
    type: str
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
    description:
      - Type of spillover used to divert traffic to the backup virtual server when
        the primary virtual server reaches the spillover threshold. Connection spillover
        is based on the number of connections. Bandwidth spillover is based on the
        total Kbps of incoming and outgoing traffic.
  sopersistence:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Maintain source-IP based persistence on primary and backup virtual servers.
  sopersistencetimeout:
    type: float
    description:
      - Time-out value, in minutes, for spillover persistence.
  sothreshold:
    type: float
    description:
      - Depending on the spillover method, the maximum number of connections or the
        maximum total bandwidth (Kbps) that a virtual server can handle before spillover
        occurs.
  stateupdate:
    type: str
    choices:
      - ENABLED
      - DISABLED
      - UPDATEONBACKENDUPDATE
    description:
      - 'Enable state updates for a specific content switching virtual server. By
        default, the Content Switching virtual server is always UP, regardless of
        the state of the Load Balancing virtual servers bound to it. This parameter
        interacts with the global setting as follows:'
      - Global Level | Vserver Level | Result
      - C(ENABLED)      C(ENABLED)        C(ENABLED)
      - C(ENABLED)      C(DISABLED)       C(ENABLED)
      - C(DISABLED)     C(ENABLED)        C(ENABLED)
      - C(DISABLED)     C(DISABLED)       C(DISABLED)
      - If you want to enable state updates for only some content switching virtual
        servers, be sure to disable the state update parameter.
  targettype:
    type: str
    choices:
      - GSLB
    description:
      - Virtual server target type.
  tcpprobeport:
    type: int
    description:
      - Port number for external TCP probe. NetScaler provides support for external
        TCP health check of the vserver status over the selected port. This option
        is only supported for vservers assigned with an IPAddress or ipset.
  tcpprofilename:
    type: str
    description:
      - Name of the TCP profile containing TCP configuration settings for the virtual
        server.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  timeout:
    type: float
    description:
      - Time period for which a persistence session is in effect.
  ttl:
    type: float
    description:
      - '0'
  v6persistmasklen:
    type: float
    description:
      - Persistence mask for IP based persistence types, for IPv6 virtual servers.
  vipheader:
    type: str
    description:
      - Name of virtual server IP and port header, for use with the VServer IP Port
        Insertion parameter.
  csvserver_analyticsprofile_binding:
    type: dict
    description: Bindings for csvserver_analyticsprofile_binding resource
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
  csvserver_appflowpolicy_binding:
    type: dict
    description: Bindings for csvserver_appflowpolicy_binding resource
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
  csvserver_appfwpolicy_binding:
    type: dict
    description: Bindings for csvserver_appfwpolicy_binding resource
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
  csvserver_appqoepolicy_binding:
    type: dict
    description: Bindings for csvserver_appqoepolicy_binding resource
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
  csvserver_auditnslogpolicy_binding:
    type: dict
    description: Bindings for csvserver_auditnslogpolicy_binding resource
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
  csvserver_auditsyslogpolicy_binding:
    type: dict
    description: Bindings for csvserver_auditsyslogpolicy_binding resource
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
  csvserver_authorizationpolicy_binding:
    type: dict
    description: Bindings for csvserver_authorizationpolicy_binding resource
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
  csvserver_botpolicy_binding:
    type: dict
    description: Bindings for csvserver_botpolicy_binding resource
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
  csvserver_cachepolicy_binding:
    type: dict
    description: Bindings for csvserver_cachepolicy_binding resource
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
  csvserver_cmppolicy_binding:
    type: dict
    description: Bindings for csvserver_cmppolicy_binding resource
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
  csvserver_contentinspectionpolicy_binding:
    type: dict
    description: Bindings for csvserver_contentinspectionpolicy_binding resource
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
  csvserver_cspolicy_binding:
    type: dict
    description: Bindings for csvserver_cspolicy_binding resource
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
  csvserver_domain_binding:
    type: dict
    description: Bindings for csvserver_domain_binding resource
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
  csvserver_feopolicy_binding:
    type: dict
    description: Bindings for csvserver_feopolicy_binding resource
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
  csvserver_gslbvserver_binding:
    type: dict
    description: Bindings for csvserver_gslbvserver_binding resource
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
  csvserver_lbvserver_binding:
    type: dict
    description: Bindings for csvserver_lbvserver_binding resource
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
  csvserver_responderpolicy_binding:
    type: dict
    description: Bindings for csvserver_responderpolicy_binding resource
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
  csvserver_rewritepolicy_binding:
    type: dict
    description: Bindings for csvserver_rewritepolicy_binding resource
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
  csvserver_spilloverpolicy_binding:
    type: dict
    description: Bindings for csvserver_spilloverpolicy_binding resource
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
  csvserver_tmtrafficpolicy_binding:
    type: dict
    description: Bindings for csvserver_tmtrafficpolicy_binding resource
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
  csvserver_transformpolicy_binding:
    type: dict
    description: Bindings for csvserver_transformpolicy_binding resource
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
  csvserver_vpnvserver_binding:
    type: dict
    description: Bindings for csvserver_vpnvserver_binding resource
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
- name: Sample csvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure csvserver
      delegate_to: localhost
      netscaler.adc.csvserver:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: ADNS_TCP_EXT
        servicetype: DNS_TCP
        ipv46: 10.189.1.7
        port: 53
        ipset: ipset_adns
        clttimeout: 180
        persistencetype: NONE
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
