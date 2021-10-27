:orphan:

.. _citrix_adc_servicegroup_module:

citrix_adc_servicegroup - Manage service group configuration in Citrix ADC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage service group configuration in Citrix ADC.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.




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
      - Enable logging of AppFlow information for the specified service group.
    * - autodisabledelay

        *(str)*
      -
      - The time allowed (in seconds) for a graceful shutdown. During this period, new connections or will continue to be sent to this service for clients who already have a persistent session on the Connections or requests from fresh or new clients who do not yet have a persistence sessions on the will not be sent to the service. Instead, they will be load balanced among other available services. the delay time expires, no new requests or connections will be sent to the service.
    * - autodisablegraceful

        *(bool)*
      -
      - Indicates graceful shutdown of the service. System will wait for all outstanding connections to this to be closed before disabling the service.
    * - autoscale

        *(str)*
      - Choices:

          - DISABLED
          - DNS
          - POLICY
          - CLOUD
          - API
      - Auto scale option for a servicegroup.
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - cacheable

        *(bool)*
      -
      - Use the transparent cache redirection virtual server to forward the request to the cache server.

        Note: Do not set this parameter if you set the Cache Type.
    * - cachetype

        *(str)*
      - Choices:

          - TRANSPARENT
          - REVERSE
          - FORWARD
      - Cache type supported by the cache server.
    * - cip

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Insert the Client IP header in requests forwarded to the service.
    * - cipheader

        *(str)*
      -
      - Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of IP Header parameter or the value set by the set ns config command is used as client's IP header name.

        Minimum length =  1
    * - cka

        *(bool)*
      -
      - Enable client keep-alive for the service group.
    * - clttimeout

        *(int)*
      -
      - Time, in seconds, after which to terminate an idle client connection.

        Minimum value = ``0``

        Maximum value = ``31536000``
    * - cmp

        *(bool)*
      -
      - Enable compression for the specified service.
    * - comment

        *(str)*
      -
      - Any information about the service group.
    * - customserverid

        *(str)*
      -
      - The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.
    * - dbsttl

        *(str)*
      -
      - Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates use the TTL received in DNS response for monitors.
    * - delay

        *(str)*
      -
      - Time, in seconds, allocated for a shutdown of the services in the service group. During this period, requests are sent to the service only for clients who already have persistent sessions on the Requests from new clients are load balanced among other available services. After the delay time no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``true`` the server state will be set to ``disabled``.

        When set to ``false`` the server state will be set to ``enabled``.
    * - downstateflush

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with all the services in the service group whose state from UP to DOWN. Do not enable this option for applications that must complete their transactions.
    * - dup_weight

        *(str)*
      -
      - weight of the monitor that is bound to servicegroup.

        Minimum value = ``1``
    * - graceful

        *(bool)*
      -
      - Wait for all existing connections to the service to terminate before shutting down the service.
    * - hashid

        *(str)*
      -
      - The hash identifier for the service. This must be unique for each service. This parameter is used by based load balancing methods.

        Minimum value = ``1``
    * - healthmonitor

        *(bool)*
      -
      - Monitor the health of this service.  Available settings function as follows:

        YES - Send probes to check the health of the service.

        NO - Do not send probes to check the health of the service. With the NO option, the appliance shows service as UP at all times.
    * - httpprofilename

        *(str)*
      -
      - Name of the HTTP profile that contains HTTP configuration settings for the service group.

        Minimum length =  1

        Maximum length =  127
    * - includemembers

        *(bool)*
      -
      - Display the members of the listed service groups in addition to their settings. Can be specified when service group name is provided in the command. In that case, the details displayed for each service are identical to the details displayed when a service group name is provided, except that bound are not displayed.
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
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
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
    * - maxbandwidth

        *(str)*
      -
      - Maximum bandwidth, in Kbps, allocated for all the services in the service group.

        Minimum value = ``0``

        Maximum value = ``4294967287``
    * - maxclient

        *(str)*
      -
      - Maximum number of simultaneous open connections for the service group.

        Minimum value = ``0``

        Maximum value = ``4294967294``
    * - maxreq

        *(str)*
      -
      - Maximum number of requests that can be sent on a persistent connection to the service group.

        Note: Connection requests beyond this value are rejected.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - memberport

        *(int)*
      -
      - member port.
    * - monconnectionclose

        *(str)*
      - Choices:

          - RESET
          - FIN
      - Close monitoring connections by sending the service a connection termination message with the bit set.
    * - monitor_bindings

        *(dict)*
      -
      - A list of monitor to bind to the servicegroup
    * - monitor_name_svc

        *(str)*
      -
      - Name of the monitor bound to the service group. Used to assign a weight to the monitor.

        Minimum length =  1
    * - monthreshold

        *(str)*
      -
      - Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to a service as UP or DOWN.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - nameserver

        *(str)*
      -
      - Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use global nameserver.
    * - netprofile

        *(str)*
      -
      - Network profile for the service group.

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
    * - pathmonitor

        *(bool)*
      -
      - Path monitoring for clustering.
    * - pathmonitorindv

        *(bool)*
      -
      - Individual Path monitoring decisions.
    * - port

        *(int)*
      -
      - Server port number.

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - riseapbrstatsmsgcode

        *(int)*
      -
      - The code indicating the rise apbr status.
    * - rtspsessionidremap

        *(bool)*
      -
      - Enable RTSP session ID mapping for the service group.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - sc

        *(bool)*
      -
      - State of the SureConnect feature for the service group.
    * - serverid

        *(str)*
      -
      - The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
    * - servername

        *(str)*
      -
      - Name of the server to which to bind the service group.

        Minimum length =  1
    * - servicegroupname

        *(str)*
      -
      - Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and (-) characters. Can be changed after the name is created.

        Minimum length =  1
    * - servicemembers

        *(dict)*
      -
      - A list of dictionaries describing each service member of the service group.
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
      - Protocol used to exchange data with the service.
    * - sp

        *(bool)*
      -
      - Enable surge protection for the service group.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - svrtimeout

        *(int)*
      -
      - Time, in seconds, after which to terminate an idle server connection.

        Minimum value = ``0``

        Maximum value = ``31536000``
    * - tcpb

        *(bool)*
      -
      - Enable TCP buffering for the service group.
    * - tcpprofilename

        *(str)*
      -
      - Name of the TCP profile that contains TCP configuration settings for the service group.

        Minimum length =  1

        Maximum length =  127
    * - td

        *(str)*
      -
      - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of

        Minimum value = ``0``

        Maximum value = ``4094``
    * - useproxyport

        *(bool)*
      -
      - Use the proxy port as the source port when initiating connections with the server. With the NO the client-side connection port is used as the source port for the server-side connection.

        Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.
    * - usip

        *(bool)*
      -
      - Use client's IP address as the source IP address when initiating connection to the server. With the setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the IP address to initiate server side connections.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - weight

        *(str)*
      -
      - Weight to assign to the servers in the service group. Specifies the capacity of the servers relative the other servers in the load balancing configuration. The higher the weight, the higher the of requests sent to the service.

        Minimum value = ``1``

        Maximum value = ``100``



Examples
--------

.. code-block:: yaml+jinja
    
    # The LB Monitors monitor-1 and monitor-2 must already exist
    # Service members defined by C(ip) must not redefine an existing server's ip address.
    # Service members defined by C(servername) must already exist.
    
    - name: Setup http service with ip members
      delegate_to: localhost
      citrix_adc_servicegroup:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        servicegroupname: service-group-1
        servicetype: HTTP
        servicemembers:
            mode: exact
            attributes:
              - ip: 10.78.78.78
                port: 80
                weight: 50
              - ip: 10.79.79.79
                port: 80
                weight: 40
              - servername: server-1
                port: 80
                weight: 10
    
        monitor_bindings:
            mode: exact
            attributes:
              - monitor_name: monitor-1
                weight: 50
              - monitor_name: monitor-2
                weight: 50


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
