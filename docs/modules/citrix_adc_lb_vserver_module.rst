:orphan:

.. _citrix_adc_lb_vserver_module:

citrix_adc_lb_vserver - Manage load balancing vserver configuration
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage load balancing vserver configuration
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - adfsproxyprofile

        *(str)*
      -
      - Name of the adfsProxy profile to be used to support ADFSPIP protocol for ADFS servers.
    * - api_path

        *(str)*
      -
      - Base NITRO API path.

        Define only in case of an ADM service proxy call
    * - appflowlog

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Apply AppFlow logging to the virtual server.
    * - appfw_policybindings

        *(list)*
      -
      - List of services along with the weights that are load balanced.

        The following suboptions are available.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - bindpoint

                *(str)*
              - Choices:

                  - REQUEST
                  - RESPONSE
              - The bindpoint to which the policy is bound.
            * - gotopriorityexpression

                *(str)*
              -
              - Expression specifying the priority of the next policy which will get evaluated if the current policy evaluates to TRUE.
            * - invoke

                *(bool)*
              -
              - Invoke policies bound to a virtual server or policy label.
            * - labelname

                *(str)*
              -
              - Name of the label invoked.
            * - labeltype

                *(str)*
              - Choices:

                  - reqvserver
                  - resvserver
                  - policylabel
              - The invocation type.
            * - policyname

                *(str)*
              -
              - Name of the policy bound to the LB vserver.
            * - priority

                *(str)*
              -
              - Priority.

    * - authentication

        *(bool)*
      -
      - Enable or disable user authentication.
    * - authenticationhost

        *(str)*
      -
      - Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be for authentication. Make sure that the Authentication parameter is set to ENABLED.

        Minimum length =  3

        Maximum length =  252
    * - authn401

        *(bool)*
      -
      - Enable or disable user authentication with HTTP 401 responses.
    * - authnprofile

        *(str)*
      -
      - Name of the authentication profile to be used when authentication is turned on.
    * - authnvsname

        *(str)*
      -
      - Name of an authentication virtual server with which to authenticate users.

        Minimum length =  1

        Maximum length =  252
    * - backuplbmethod

        *(str)*
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - SOURCEIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - CUSTOMLOAD
      - Backup load balancing method. Becomes operational if the primary load balancing me

        thod fails or cannot be used.

        Valid only if the primary method is based on static proximity.
    * - backuppersistencetimeout

        *(int)*
      -
      - Time period for which backup persistence is in effect.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - backupvserver

        *(str)*
      -
      - Name of the backup virtual server to which to forward requests if the primary virtual server goes or reaches its spillover threshold.

        Minimum length =  1
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - bypassaaaa

        *(bool)*
      -
      - If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns
    * - cacheable

        *(bool)*
      -
      - Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can requests only to a transparent cache redirection virtual server that has an IP address and port of *:80, so such a cache redirection virtual server must be configured on the appliance.
    * - clttimeout

        *(int)*
      -
      - Idle time, in seconds, after which a client connection is terminated.

        Minimum value = ``0``

        Maximum value = ``31536000``
    * - comment

        *(str)*
      -
      - Any comments that you might want to associate with the virtual server.
    * - connfailover

        *(str)*
      - Choices:

          - DISABLED
          - STATEFUL
          - STATELESS
      - Mode in which the connection failover feature must operate for the virtual server. After a failover, TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients connected to the same servers. Available settings function as follows:

        * STATEFUL - The primary appliance shares state information with the secondary appliance, in real resulting in some runtime processing overhead.

        * STATELESS - State information is not shared, and the new primary appliance tries to re-create the flow on the basis of the information contained in the packets it receives.

        * DISABLED - Connection failover does not occur.
    * - cookiename

        *(str)*
      -
      - Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of with a maximum of 32 characters. If not specified, cookie name is internally generated.
    * - datalength

        *(str)*
      -
      - Length of the token to be extracted from the data segment of an incoming packet, for use in the token of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. to virtual servers of type TCP.

        Minimum value = ``1``

        Maximum value = ``100``
    * - dataoffset

        *(str)*
      -
      - Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP

        Minimum value = ``0``

        Maximum value = ``25400``
    * - dbprofilename

        *(str)*
      -
      - Name of the DB profile whose settings are to be applied to the virtual server.

        Minimum length =  1

        Maximum length =  127
    * - dbslb

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Enable database specific load balancing for MySQL and MSSQL service types.
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``true`` the server state will be set to ``disabled``.

        When set to ``false`` the server state will be set to ``enabled``.
    * - disableprimaryondown

        *(str)*
      - Choices:

          - enabled
          - disabled
      - If the primary virtual server goes down, do not allow it to return to primary status until manually
    * - dns64

        *(str)*
      - Choices:

          - enabled
          - disabled
      - This argument is for enabling/disabling the dns64 on lbvserver.
    * - dnsprofilename

        *(str)*
      -
      - Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.

        Minimum length =  1

        Maximum length =  127
    * - downstateflush

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with a virtual server whose state transitions from UP to Do not enable this option for applications that must complete their transactions.
    * - hashlength

        *(str)*
      -
      - Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing

        Minimum value = ``1``

        Maximum value = ``4096``
    * - healththreshold

        *(str)*
      -
      - Threshold in percent of active services below which vserver state is made down. If this threshold is vserver state will be up even if one bound service is up.

        Minimum value = ``0``

        Maximum value = ``100``
    * - httpprofilename

        *(str)*
      -
      - Name of the HTTP profile whose settings are to be applied to the virtual server.

        Minimum length =  1

        Maximum length =  127
    * - httpsredirecturl

        *(str)*
      -
      - URL to which to redirect traffic if the traffic is recieved from redirect port.
    * - icmpvsrresponse

        *(str)*
      - Choices:

          - PASSIVE
          - ACTIVE
      - How the Citrix ADC responds to ping requests received for an IP address that is common to one or more servers. Available settings function as follows:

        * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always to the ping requests.

        * If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not

        * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.

        Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip in the CLI or the Create IP dialog box in the GUI.
    * - insertvserveripport

        *(str)*
      - Choices:

          - OFF
          - VIPADDR
          - V6TOV4MAPPING
      - Insert an HTTP header, whose value is the IP address and port number of the virtual server, before a request to the server. The format of the header is <vipHeader>: <virtual server IP address>_<port >, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter which IP address is inserted in the header, as follows:

        * VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.

        * V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a IPv4 address is not configured, insert the IPv6 address.

        * OFF - Disable header insertion.
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - ipmask

        *(str)*
      -
      - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first bits or the last n bits of the destination IP address in a client request are to be matched with the bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
    * - ippattern

        *(str)*
      -
      - IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual The IP Mask parameter specifies which part of the destination IP address is matched against the Mutually exclusive with the IP Address parameter.

        For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).

        If a destination IP address matches more than one IP pattern, the pattern with the longest match is and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2 the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP matches two or more virtual servers to the same extent, the request is processed by the virtual whose port number matches the port number in the request.
    * - ipset

        *(str)*
      -
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current vserver.

        Minimum length =  1
    * - ipv46

        *(str)*
      -
      - IPv4 or IPv6 address to assign to the virtual server.
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - l2conn

        *(bool)*
      -
      - Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple and non-TCP connections with the same 4-tuple to co-exist on the Citrix ADC.
    * - lbmethod

        *(str)*
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - URLHASH
          - DOMAINHASH
          - DESTINATIONIPHASH
          - SOURCEIPHASH
          - SRCIPDESTIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - TOKEN
          - SRCIPSRCPORTHASH
          - LRTM
          - CALLIDHASH
          - CUSTOMLOAD
          - LEASTREQUEST
          - AUDITLOGHASH
          - STATICPROXIMITY
          - USER_TOKEN
      - Load balancing method.  The available settings function as follows:

        * ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to to enforce weighted round robin distribution.

        * LEASTCONNECTION (default) - Select the service with the fewest connections.

        * LEASTRESPONSETIME - Select the service with the lowest average response time.

        * LEASTBANDWIDTH - Select the service currently handling the least traffic.

        * LEASTPACKETS - Select the service currently serving the lowest number of packets per second.

        * CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors.

        * LRTM - Select the service with the lowest response time. Response times are learned through probes. This method also takes the number of active connections into account.

        Also available are a number of hashing methods, in which the appliance extracts a predetermined of the request, creates a hash of the portion, and then checks whether any previous requests had the hash value. If it finds a match, it forwards the request to the service that served those previous Following are the hashing methods:

        * URLHASH - Create a hash of the request URL (or part of the URL).

        * DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The name is taken from either the URL or the Host header. If the domain name appears in both locations, URL is preferred. If the request does not contain a domain name, the load balancing method defaults LEASTCONNECTION.

        * DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header.

        * SOURCEIPHASH - Create a hash of the source IP address in the IP header.

        * TOKEN - Extract a token from the request, create a hash of the token, and then select the service which any previous requests with the same token hash value were sent.

        * SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and IP address in the IP header.

        * SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header.

        * CALLIDHASH - Create a hash of the SIP Call-ID header.

        * USER_TOKEN - Same as TOKEN LB method but token needs to be provided from an extension.
    * - lbprofilename

        *(str)*
      -
      - Name of the LB profile which is associated to the vserver.
    * - listenpolicy

        *(str)*
      -
      - Expression identifying traffic accepted by the virtual server. Can be either an expression (for CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.
    * - listenpriority

        *(str)*
      -
      - Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If request matches the listen policies of more than one virtual server the virtual server whose listen has the highest priority (the lowest priority number) accepts the request.

        Minimum value = ``0``

        Maximum value = ``101``
    * - m

        *(str)*
      - Choices:

          - IP
          - MAC
          - IPTUNNEL
          - TOS
      - Redirection mode for load balancing. Available settings function as follows:

        * IP - Before forwarding a request to a server, change the destination IP address to the server's IP

        * MAC - Before forwarding a request to a server, change the destination MAC address to the server's address. The destination IP address is not changed. MAC-based redirection mode is used mostly in load balancing deployments.

        * IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The IP packets are not modified. Applicable to both IPv4 and IPv6 packets.

        * TOS - Encode the virtual server's TOS ID in the TOS field of the IP header.

        You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR).
    * - macmoderetainvlan

        *(str)*
      - Choices:

          - enabled
          - disabled
      - This option is used to retain vlan information of incoming packet when macmode is enabled.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``

        When true and adm service is the api proxy the following option must also be defined: ``bearer_token``

        When true you must define a target ADC by defining any of the following parameters

        I(instance_ip)

        I(instance_id)

        I(instance_name)
    * - maxautoscalemembers

        *(str)*
      -
      - Maximum number of members expected to be present when vserver is used in Autoscale.

        Minimum value = ``0``

        Maximum value = ``5000``
    * - minautoscalemembers

        *(str)*
      -
      - Minimum number of members expected to be present when vserver is used in Autoscale.

        Minimum value = ``0``

        Maximum value = ``5000``
    * - mssqlserverversion

        *(str)*
      - Choices:

          - 70
          - 2000
          - 2000SP1
          - 2005
          - 2008
          - 2008R2
          - 2012
          - 2014
      - For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this if you expect some clients to run a version different from the version of the database. This setting compatibility between the client-side and server-side connections by ensuring that all communication to the server's version.
    * - mysqlcharacterset

        *(str)*
      -
      - Character set that the virtual server advertises to clients.
    * - mysqlprotocolversion

        *(str)*
      -
      - MySQL protocol version that the virtual server advertises to clients.
    * - mysqlservercapabilities

        *(str)*
      -
      - Server capabilities that the virtual server advertises to clients.
    * - mysqlserverversion

        *(str)*
      -
      - MySQL server version string that the virtual server advertises to clients.

        Minimum length =  1

        Maximum length =  31
    * - name

        *(str)*
      -
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.

        CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation (for example, "my vserver" or 'my vserver'). .

        Minimum length =  1
    * - netmask

        *(str)*
      -
      - IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing is DESTINATIONIPHASH or SOURCEIPHASH.

        Minimum length =  1
    * - netprofile

        *(str)*
      -
      - Name of the network profile to associate with the virtual server. If you set this parameter, the server uses only the IP addresses in the network profile as source IP addresses when initiating with servers.

        Minimum length =  1

        Maximum length =  127
    * - newservicerequest

        *(str)*
      -
      - Number of requests, or percentage of the load on existing services, by which to increase the load on new service at each interval in slow-start mode. A non-zero value indicates that slow-start is A zero value indicates that the global RR startup parameter is applied. Changing the value to zero cause services currently in slow start to take the full traffic as determined by the LB method. any new services added will use the global RR factor.
    * - newservicerequestincrementinterval

        *(str)*
      -
      - Interval, in seconds, between successive increments in the load on a new service or a service whose has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.

        Minimum value = ``0``

        Maximum value = ``3600``
    * - newservicerequestunit

        *(str)*
      - Choices:

          - PER_SECOND
          - PERCENT
      - Units in which to increment load at each interval in slow-start mode.
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Citrix ADC node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout

        *(float)*
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - oracleserverversion

        *(str)*
      - Choices:

          - 10G
          - 11G
      - Oracle server version.
    * - persistavpno

        *(list)*
      -
      - Persist AVP number for Diameter Persistency.

        In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP,

        define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X

        is nested inside AVP Y which is nested in Z, then define the list as  Z Y X.

        Minimum value = ``1``
    * - persistencebackup

        *(str)*
      - Choices:

          - SOURCEIP
          - NONE
      - Backup persistence type for the virtual server. Becomes operational if the primary persistence fails.
    * - persistencetype

        *(str)*
      - Choices:

          - SOURCEIP
          - COOKIEINSERT
          - SSLSESSION
          - RULE
          - URLPASSIVE
          - CUSTOMSERVERID
          - DESTIP
          - SRCIPDESTIP
          - CALLID
          - RTSPSID
          - DIAMETER
          - FIXSESSION
          - USERSESSION
          - NONE
      - Type of persistence for the virtual server. Available settings function as follows:

        * SOURCEIP - Connections from the same client IP address belong to the same persistence session.

        * COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from server, belong to the same persistence session.

        * SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.

        * CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter identify the server ID in a request.

        * RULE - All connections that match a user defined rule belong to the same persistence session.

        * URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence The server ID is the hexadecimal representation of the IP address and port of the service to which request must be forwarded. This persistence type requires a rule to identify the server ID in the

        * DESTIP - Connections to the same destination IP address belong to the same persistence session.

        * SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to same persistence session.

        * CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session.

        * RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session.

        * FIXSESSION - Connections that have the same SenderCompID and TargetCompID values belong to the same session.

        * USERSESSION - Persistence session is created based on the persistence parameter value provided from extension.
    * - persistmask

        *(str)*
      -
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.

        Minimum length =  1
    * - port

        *(int)*
      -
      - Port number for the virtual server.

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - pq

        *(bool)*
      -
      - Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers.
    * - processlocal

        *(str)*
      - Choices:

          - enabled
          - disabled
      - By turning on this option packets destined to a vserver in a cluster will not under go any steering. this option for single packet request response mode or when the upstream device is performing a RSS for connection based distribution.
    * - push

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Process traffic with the push virtual server that is bound to this load balancing virtual server.
    * - pushlabel

        *(str)*
      -
      - Expression for extracting a label from the server's response. Can be either an expression or the name a named expression.
    * - pushmulticlients

        *(bool)*
      -
      - Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
    * - pushvserver

        *(str)*
      -
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes received on the load balancing virtual server that you are configuring.

        Minimum length =  1
    * - range

        *(str)*
      -
      - Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual then functions as a network virtual server, accepting traffic on any of the generated IP addresses. IP addresses are generated automatically, as follows:

        * For a range of n, the last octet of the address specified by the IP Address parameter increments times.

        * If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.

        Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name to specify the range. For example:

        add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80.

        Minimum value = ``1``

        Maximum value = ``254``
    * - recursionavailable

        *(bool)*
      -
      - When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport queries.
    * - redirectfromport

        *(int)*
      -
      - Port number for the virtual server, from which we absorb the traffic for http redirect.

        Minimum value = ``1``

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - redirectportrewrite

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Rewrite the port and change the protocol to ensure successful HTTP redirects from services.
    * - redirurl

        *(str)*
      -
      - URL to which to redirect traffic if the virtual server becomes unavailable.

        WARNING! Make sure that the domain in the URL does not match the domain specified for a content policy. If it does, requests are continuously redirected to the unavailable virtual server.

        Minimum length =  1
    * - redirurlflags

        *(bool)*
      -
      - The redirect URL to be unset.
    * - resrule

        *(str)*
      -
      - Expression specifying which part of a server's response to use for creating rule based persistence (persistence type RULE). Can be either an expression or the name of a named expression.

        Example:

        HTTP.RES.HEADER(\"setcookie\").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE(\"server1\").
    * - retainconnectionsoncluster

        *(bool)*
      -
      - This option enables you to retain existing connections on a node joining a Cluster system or when a is being configured for passive timeout. By default, this option is disabled.
    * - rhistate

        *(str)*
      - Choices:

          - PASSIVE
          - ACTIVE
      - Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) on the virtual servers associated with the VIP address:

        * If you set RHI STATE to PASSIVE on all virtual servers, the Citrix ADC always advertises the route the VIP address.

        * If you set RHI STATE to ACTIVE on all virtual servers, the Citrix ADC advertises the route for the address if at least one of the associated virtual servers is in UP state.

        * If you set RHI STATE to ACTIVE on some and PASSIVE on others, the Citrix ADC advertises the route the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is UP state.
    * - rtspnat

        *(bool)*
      -
      - Use network address translation (NAT) for RTSP data connections.
    * - rule

        *(str)*
      -
      - Expression, or name of a named expression, against which traffic is evaluated.

        The following requirements apply only to the Citrix ADC CLI:

        * If the expression includes one or more spaces, enclose the entire expression in double quotation

        * If the expression itself includes double quotation marks, escape the quotations by using the \

        * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not to escape the double quotation marks.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - sc

        *(bool)*
      -
      - Use SureConnect on the virtual server.
    * - servicebindings

        *(list)*
      -
      - List of services along with the weights that are load balanced.

        The following suboptions are available.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - servicename

                *(str)*
              -
              - Service to bind to the virtual server.

                Minimum length =  1
            * - weight

                *(str)*
              -
              - Weight to assign to the specified service.

                Minimum value = ``1``

                Maximum value = ``100``

    * - servicegroupbindings

        *(list)*
      -
      - List of services along with the weights that are load balanced.

        The following suboptions are available.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - servicegroupname

                *(str)*
              -
              - The service group name bound to the selected load balancing virtual server.
            * - weight

                *(str)*
              -
              - Integer specifying the weight of the service. A larger number specifies a greater weight. Defines the of the service relative to the other services in the load balancing configuration. Determines the given to the service in load balancing decisions.

                Minimum value = ``1``

                Maximum value = ``100``

    * - servicename

        *(str)*
      -
      - Service to bind to the virtual server.

        Minimum length =  1
    * - servicetype

        *(str)*
      - Choices:

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
      - Protocol used by the service (also called the service type).
    * - sessionless

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where information is unnecessary.
    * - skippersistency

        *(str)*
      - Choices:

          - Bypass
          - ReLb
          - None
      - This argument decides the behavior incase the service which is selected from an existing persistence has reached threshold.
    * - sobackupaction

        *(str)*
      - Choices:

          - DROP
          - ACCEPT
          - REDIRECT
      - Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or
    * - somethod

        *(str)*
      - Choices:

          - CONNECTION
          - DYNAMICCONNECTION
          - BANDWIDTH
          - HEALTH
          - NONE
      - Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:

        * CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.

        * DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover for this setting, because the threshold is implied by the Max Clients settings of bound services.

        * BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and traffic exceeds the threshold.

        * HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 to DOWN.

        * NONE - Spillover does not occur.
    * - sopersistence

        *(str)*
      - Choices:

          - enabled
          - disabled
      - If spillover occurs, maintain source IP address based persistence for both primary and backup virtual
    * - sopersistencetimeout

        *(str)*
      -
      - Timeout for spillover persistence, in minutes.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - sothreshold

        *(str)*
      -
      - Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for HEALTH method (do not enter the percentage symbol).

        Minimum value = ``1``

        Maximum value = ``4294967287``
    * - ssl_certkey

        *(str)*
      -
      - The name of the ssl certificate that is bound to this service.

        The ssl certificate must already exist.

        Creating the certificate can be done with the citrix_adc_ssl_certkey module.

        This option is only applicable only when ``servicetype`` is ``SSL``.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - tcpprofilename

        *(str)*
      -
      - Name of the TCP profile whose settings are to be applied to the virtual server.

        Minimum length =  1

        Maximum length =  127
    * - td

        *(str)*
      -
      - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of

        Minimum value = ``0``

        Maximum value = ``4094``
    * - timeout

        *(int)*
      -
      - Time period for which a persistence session is in effect.

        Minimum value = ``0``

        Maximum value = ``1440``
    * - tosid

        *(str)*
      -
      - TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.

        Minimum value = ``1``

        Maximum value = ``63``
    * - trofspersistence

        *(str)*
      - Choices:

          - enabled
          - disabled
      - When value is ENABLED, Trofs persistence is honored. When value is DISABLED, Trofs persistence is not
    * - v6netmasklen

        *(str)*
      -
      - Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.

        Minimum value = ``1``

        Maximum value = ``128``
    * - v6persistmasklen

        *(str)*
      -
      - Persistence mask for IP based persistence types, for IPv6 virtual servers.

        Minimum value = ``1``

        Maximum value = ``128``
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - vipheader

        *(str)*
      -
      - Name for the inserted header. The default name is vip-header.

        Minimum length =  1
    * - weight

        *(str)*
      -
      - Weight to assign to the specified service.

        Minimum value = ``1``

        Maximum value = ``100``



Examples
--------

.. code-block:: yaml+jinja
    
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


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0'}
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
