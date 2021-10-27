:orphan:

.. _citrix_adc_cs_vserver_module:

citrix_adc_cs_vserver - Manage content switching vserver
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage content switching vserver
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
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
      - Enable logging appflow flow information.
    * - appfw_policybindings

        *(list)*
      -
      - List of appfw policy bindings

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
                  - ICA_REQUEST
                  - OTHERTCP_REQUEST
              - The bindpoint to which the policy is bound.
            * - gotopriorityexpression

                *(str)*
              -
              - Expression specifying the priority of the next policy which will get evaluated if the current policy evaluates to TRUE.
            * - invoke

                *(bool)*
              -
              - Invoke flag.
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
            * - name

                *(str)*
              -
              - Name of the content switching virtual server to which the content switching policy applies.

                Minimum length =  1
            * - policyname

                *(str)*
              -
              - Policies bound to this vserver.
            * - priority

                *(str)*
              -
              - Priority for the policy.
            * - targetlbvserver

                *(str)*
              -
              - Name of the Load Balancing virtual server to which the content is switched, if policy rule is to be TRUE. Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1 Note: Use parameter only in case of Content Switching policy bind operations to a CS vserver.

                Minimum length =  1

    * - authentication

        *(bool)*
      -
      - Authenticate users who request a connection to the content switching virtual server.
    * - authenticationhost

        *(str)*
      -
      - FQDN of the authentication virtual server. The service type of the virtual server should be either or SSL.

        Minimum length =  3

        Maximum length =  252
    * - authn401

        *(bool)*
      -
      - Enable HTTP 401-response based authentication.
    * - authnprofile

        *(str)*
      -
      - Name of the authentication profile to be used when authentication is turned on.
    * - authnvsname

        *(str)*
      -
      - Name of authentication virtual server that authenticates the incoming user requests to this content virtual server. .

        Minimum length =  1

        Maximum length =  252
    * - backupip

        *(str)*
      -
      - .

        Minimum length =  1
    * - backuppersistencetimeout

        *(str)*
      -
      - Time period for which backup persistence is in effect.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - backupvserver

        *(str)*
      -
      - Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the backup virtual is created. You can assign a different backup virtual server or rename the existing virtual server.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks.

        Minimum length =  1
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - cacheable

        *(bool)*
      -
      - Use this option to specify whether a virtual server, used for load balancing or content switching, requests to the cache redirection virtual server before sending it to the configured servers.
    * - casesensitive

        *(bool)*
      -
      - Consider case in URLs (for policies that use URLs instead of RULES). For example, with the ON the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by switching policies). With the OFF setting, /a/1.html and /A/1.HTML are switched to the same target.
    * - clttimeout

        *(int)*
      -
      - Idle time, in seconds, after which the client connection is terminated. The default values are:

        180 seconds for HTTP/SSL-based services.

        9000 seconds for other TCP-based services.

        120 seconds for DNS-based services.

        120 seconds for other UDP-based services.

        Minimum value = ``0``

        Maximum value = ``31536000``
    * - comment

        *(str)*
      -
      - Information about this virtual server.
    * - cookiedomain

        *(str)*
      -
      - .

        Minimum length =  1
    * - cookiename

        *(str)*
      -
      - Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of with a maximum of 32 characters. If not specified, cookie name is internally generated.
    * - cookietimeout

        *(str)*
      -
      - .

        Minimum value = ``0``

        Maximum value = ``1440``
    * - dbprofilename

        *(str)*
      -
      - Name of the DB profile.

        Minimum length =  1

        Maximum length =  127
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
      - Continue forwarding the traffic to backup virtual server even after the primary server comes UP from DOWN state.
    * - dnsprofilename

        *(str)*
      -
      - Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.

        Minimum length =  1

        Maximum length =  127
    * - dnsrecordtype

        *(str)*
      - Choices:

          - A
          - AAAA
          - CNAME
          - NAPTR
      - .
    * - domainname

        *(str)*
      -
      - Domain name for which to change the time to live (TTL) and/or backup service IP address.

        Minimum length =  1
    * - downstateflush

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with a virtual server whose state transitions from UP to Do not enable this option for applications that must complete their transactions.
    * - httpprofilename

        *(str)*
      -
      - Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service of the virtual server should be either HTTP or SSL.

        Minimum length =  1

        Maximum length =  127
    * - icmpvsrresponse

        *(str)*
      - Choices:

          - PASSIVE
          - ACTIVE
      - Can be active or passive.
    * - insertvserveripport

        *(str)*
      - Choices:

          - OFF
          - VIPADDR
          - V6TOV4MAPPING
      - Insert the virtual server's VIP address and port number in the request header. Available values as follows:

        VIPADDR - Header contains the vserver's IP address and port number without any translation.

        OFF     - The virtual IP and port header insertion option is disabled.

        V6TOV4MAPPING - Header contains the mapped IPv4 address corresponding to the IPv6 address of the and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns command.
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

        If a destination IP address matches more than one IP pattern, the pattern with the longest match is and the associated virtual server processes the request. For example, if the virtual servers, vs1 and have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP matches two or more virtual servers to the same extent, the request is processed by the virtual whose port number matches the port number in the request.
    * - ipset

        *(str)*
      -
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current vserver.

        Minimum length =  1
    * - ipv46

        *(str)*
      -
      - IP address of the content switching virtual server.

        Minimum length =  1
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - l2conn

        *(bool)*
      -
      - Use L2 Parameters to identify a connection.
    * - lbvserver

        *(str)*
      -
      - The default Load Balancing virtual server.
    * - listenpolicy

        *(str)*
      -
      - String specifying the listen policy for the content switching virtual server. Can be either the name an existing expression or an in-line expression.
    * - listenpriority

        *(str)*
      -
      - Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If request matches the listen policies of more than one virtual server the virtual server whose listen has the highest priority (the lowest priority number) accepts the request.

        Minimum value = ``0``

        Maximum value = ``100``
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
      - The version of the MSSQL server.
    * - mysqlcharacterset

        *(str)*
      -
      - The character set returned by the mysql vserver.
    * - mysqlprotocolversion

        *(str)*
      -
      - The protocol version returned by the mysql vserver.
    * - mysqlservercapabilities

        *(str)*
      -
      - The server capabilities returned by the mysql vserver.
    * - mysqlserverversion

        *(str)*
      -
      - The server version string returned by the mysql vserver.

        Minimum length =  1

        Maximum length =  31
    * - name

        *(str)*
      -
      - Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon at sign (@), equal sign (=), and hyphen (-) characters.

        Cannot be changed after the CS virtual server is created.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for my server or my server).

        Minimum length =  1
    * - netprofile

        *(str)*
      -
      - The name of the network profile.

        Minimum length =  1

        Maximum length =  127
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
    * - persistencebackup

        *(str)*
      - Choices:

          - SOURCEIP
          - NONE
      - Backup persistence type for the virtual server. Becomes operational if the primary persistence fails.
    * - persistenceid

        *(str)*
      -
      - .

        Minimum value = ``0``

        Maximum value = ``65535``
    * - persistencetype

        *(str)*
      - Choices:

          - SOURCEIP
          - COOKIEINSERT
          - SSLSESSION
          - NONE
      - Type of persistence for the virtual server. Available settings function as follows:

        * SOURCEIP - Connections from the same client IP address belong to the same persistence session.

        * COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from server, belong to the same persistence session.

        * SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.
    * - persistmask

        *(str)*
      -
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.

        Minimum length =  1
    * - policybindings

        *(list)*
      -
      - List of cspolicy bindings.

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
                  - ICA_REQUEST
                  - OTHERTCP_REQUEST
              - The bindpoint to which the policy is bound.
            * - gotopriorityexpression

                *(str)*
              -
              - Expression specifying the priority of the next policy which will get evaluated if the current policy evaluates to TRUE.
            * - invoke

                *(bool)*
              -
              - Invoke flag.
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
              - Policies bound to this vserver.
            * - priority

                *(str)*
              -
              - Priority for the policy.
            * - targetlbvserver

                *(str)*
              -
              - target vserver name.

    * - port

        *(int)*
      -
      - Port number for content switching virtual server.

        Minimum value = ``1``

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - precedence

        *(str)*
      - Choices:

          - RULE
          - URL
      - Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual With the default (RULE) setting, incoming requests are evaluated against the rule-based content policies. If none of the rules match, the URL in the request is evaluated against the URL-based switching policies.
    * - push

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Process traffic with the push virtual server that is bound to this content switching virtual server by the Push VServer parameter). The service type of the push virtual server should be either HTTP or
    * - pushlabel

        *(str)*
      -
      - Expression for extracting the label from the response received from server. This string can be either existing rule name or an inline expression. The service type of the virtual server should be either or SSL.
    * - pushmulticlients

        *(bool)*
      -
      - Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect
    * - pushvserver

        *(str)*
      -
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes received on the client-facing load balancing virtual server.

        Minimum length =  1
    * - range

        *(str)*
      -
      - Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, include in a range of addresses assigned to this virtual server.

        Minimum value = ``1``

        Maximum value = ``254``
    * - redirectportrewrite

        *(str)*
      - Choices:

          - enabled
          - disabled
      - State of port rewrite while performing HTTP redirect.
    * - redirecturl

        *(str)*
      -
      - URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the server should be either HTTP or SSL.

        Caution: Make sure that the domain in the URL does not match the domain specified for a content policy. If it does, requests are continuously redirected to the unavailable virtual server.

        Minimum length =  1
    * - rhistate

        *(str)*
      - Choices:

          - PASSIVE
          - ACTIVE
      - A host route is injected according to the setting on the virtual servers

        * If set to PASSIVE on all the virtual servers that share the IP address, the appliance always the hostroute.

        * If set to ACTIVE on all the virtual servers that share the IP address, the appliance injects even one virtual server is UP.

        * If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance, injects even if virtual server set to ACTIVE is UP.
    * - rtspnat

        *(bool)*
      -
      - Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - servicetype

        *(str)*
      - Choices:

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
      - Protocol used by the virtual server.
    * - sitedomainttl

        *(str)*
      -
      - .

        Minimum value = ``1``
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
      - Type of spillover used to divert traffic to the backup virtual server when the primary virtual server the spillover threshold. Connection spillover is based on the number of connections. Bandwidth is based on the total Kbps of incoming and outgoing traffic.
    * - sopersistence

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Maintain source-IP based persistence on primary and backup virtual servers.
    * - sopersistencetimeout

        *(str)*
      -
      - Time-out value, in minutes, for spillover persistence.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - sothreshold

        *(str)*
      -
      - Depending on the spillover method, the maximum number of connections or the maximum total bandwidth that a virtual server can handle before spillover occurs.

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
    * - stateupdate

        *(str)*
      - Choices:

          - ENABLED
          - DISABLED
          - UPDATEONBACKENDUPDATE
      - Enable state updates for a specific content switching virtual server. By default, the Content virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to This parameter interacts with the global setting as follows:

        Global Level | Vserver Level | Result

        ENABLED      ENABLED        ENABLED

        ENABLED      DISABLED       ENABLED

        DISABLED     ENABLED        ENABLED

        DISABLED     DISABLED       DISABLED

        If you want to enable state updates for only some content switching virtual servers, be sure to the state update parameter.
    * - targettype

        *(str)*
      - Choices:

          - GSLB
      - Virtual server target type.
    * - tcpprofilename

        *(str)*
      -
      - Name of the TCP profile containing TCP configuration settings for the virtual server.

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
    * - ttl

        *(str)*
      -
      - .

        Minimum value = ``1``
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
      - Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.

        Minimum length =  1



Examples
--------

.. code-block:: yaml+jinja
    
    # policy_1 must have been already created with the citrix_adc_cs_policy module
    # lbvserver_1 must have been already created with the citrix_adc_lb_vserver module
    
    - name: Setup content switching vserver
      delegate_to: localhost
      citrix_adc_cs_vserver:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        name: cs_vserver_1
        ipv46: 192.168.1.1
        port: 80
        servicetype: HTTP
    
        policybindings:
          - policyname: policy_1
            targetlbvserver: lbvserver_1


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
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
