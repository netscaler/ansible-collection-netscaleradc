:orphan:

.. _citrix_adc_service_module:

citrix_adc_service - Manage service configuration in Citrix ADC
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage service configuration in Citrix ADC.
- This module allows the creation, deletion and modification of Citrix ADC services.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.
- This module supports check mode.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - accessdown

        *(bool)*
      - Default:

        *False*
      - Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.
    * - appflowlog

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Enable logging of AppFlow information.
    * - cacheable

        *(bool)*
      - Default:

        *False*
      - Use the transparent cache redirection virtual server to forward requests to the cache server.

        Note: Do not specify this parameter if you set the Cache Type parameter.
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
      - Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.
    * - cipheader

        *(str)*
      -
      - Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System > Settings > Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".

        Minimum length = 1
    * - cka

        *(bool)*
      -
      - Enable client keep-alive for the service.
    * - cleartextport

        *(int)*
      -
      - Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.

        Minimum value = 1
    * - clttimeout

        *(float)*
      -
      - Time, in seconds, after which to terminate an idle client connection.

        Minimum value = 0

        Maximum value = 31536000
    * - cmp

        *(bool)*
      -
      - Enable compression for the service.
    * - comment

        *(str)*
      -
      - Any information about the service.
    * - customserverid

        *(str)*
      - Default:

        *None*
      - Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``yes`` the service state will be set to DISABLED.

        When set to ``no`` the service state will be set to ENABLED.

        Note that due to limitations of the underlying NITRO API a ``disabled`` state change alone does not cause the module result to report a changed status.
    * - dnsprofilename

        *(str)*
      -
      - Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.

        Minimum length = 1

        Maximum length = 127
    * - downstateflush

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
    * - graceful

        *(bool)*
      - Default:

        *False*
      - Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.
    * - hashid

        *(float)*
      -
      - A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.

        Minimum value = 1
    * - healthmonitor

        *(bool)*
      - Default:

        *True*
      - Monitor the health of this service
    * - httpprofilename

        *(str)*
      -
      - Name of the HTTP profile that contains HTTP configuration settings for the service.

        Minimum length = 1

        Maximum length = 127
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - ip

        *(str)*
      -
      - IP to assign to the service.

        Minimum length = 1
    * - ipaddress

        *(str)*
      -
      - The new IP address of the service.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - maxbandwidth

        *(float)*
      -
      - Maximum bandwidth, in Kbps, allocated to the service.

        Minimum value = 0

        Maximum value = 4294967287
    * - maxclient

        *(float)*
      -
      - Maximum number of simultaneous open connections to the service.

        Minimum value = 0

        Maximum value = 4294967294
    * - maxreq

        *(float)*
      -
      - Maximum number of requests that can be sent on a persistent connection to the service.

        Note: Connection requests beyond this value are rejected.

        Minimum value = 0

        Maximum value = 65535
    * - monitor_bindings

        *(list)*
      -
      - A list of load balancing monitors to bind to this service.

        Each monitor entry is a dictionary which may contain the following options.

        Note that if not using the built in monitors they must first be setup.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - dup_state
              - Choices:

                  - enabled
                  - disabled
              - State of the monitor.

                The state setting for a monitor of a given type affects all monitors of that type.

                For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled.

                If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.
            * - dup_weight
              -
              - Weight to assign to the binding between the monitor and service.
            * - monitorname
              -
              - Name of the monitor.
            * - weight
              -
              - Weight to assign to the binding between the monitor and service.

    * - monthreshold

        *(float)*
      -
      - Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.

        Minimum value = 0

        Maximum value = 65535
    * - name

        *(str)*
      -
      - Name for the service. Must begin with an ASCII alphabetic or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore ``_``, hash ``#``, period ``.``, space `` ``, colon ``:``, at ``@``, equals ``=``, and hyphen ``-`` characters. Cannot be changed after the service has been created.

        Minimum length = 1
    * - netprofile

        *(str)*
      -
      - Network profile to use for the service.

        Minimum length = 1

        Maximum length = 127
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
    * - port

        *(int)*
      -
      - Port number of the service.

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - processlocal

        *(str)*
      - Choices:

          - enabled
          - disabled
      - By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.
    * - rtspsessionidremap

        *(bool)*
      - Default:

        *False*
      - Enable RTSP session ID mapping for the service.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - servername

        *(str)*
      -
      - Name of the server that hosts the service.

        Minimum length = 1
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
      - Protocol in which data is exchanged with the service.
    * - sp

        *(bool)*
      -
      - Enable surge protection for the service.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - svrtimeout

        *(float)*
      -
      - Time, in seconds, after which to terminate an idle server connection.

        Minimum value = 0

        Maximum value = 31536000
    * - tcpb

        *(bool)*
      -
      - Enable TCP buffering for the service.
    * - tcpprofilename

        *(str)*
      -
      - Name of the TCP profile that contains TCP configuration settings for the service.

        Minimum length = 1

        Maximum length = 127
    * - useproxyport

        *(bool)*
      -
      - Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.

        Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.
    * - usip

        *(bool)*
      -
      - Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    # Monitor monitor-1 must have been already setup
    
    - name: Setup http service
      gather_facts: False
      delegate_to: localhost
      citrix_adc_service:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        name: service-http-1
        servicetype: HTTP
        ipaddress: 10.78.0.1
        port: 80
    
        monitor_bindings:
          - monitor-1


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
      - A dictionary with a list of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' }
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
