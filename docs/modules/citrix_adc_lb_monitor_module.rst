:orphan:

.. _citrix_adc_lb_monitor_module:

citrix_adc_lb_monitor - Manage load balancing monitors
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage load balancing monitors.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.



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
    * - Snmpoid

        *(str)*
      -
      - SNMP OID for ``SNMP`` monitors.

        Minimum length = 1
    * - acctapplicationid

        *(list)*
      -
      - List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.

        Minimum value = ``0``

        Maximum value = ``4294967295``
    * - action

        *(str)*
      - Choices:

          - NONE
          - LOG
          - DOWN
      - Action to perform when the response to an inline monitor (a monitor of type ``HTTP-INLINE``) indicates that the service is down. A service monitored by an inline monitor is considered ``DOWN`` if the response code is not one of the codes that have been specified for the Response Code parameter.

        Available settings function as follows:

        * ``NONE`` - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.

        * ``LOG`` - Log the event in NSLOG or SYSLOG.

        * ``DOWN`` - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as ``DOWN``. Also, log the event in NSLOG or SYSLOG.
    * - alertretries

        *(int)*
      -
      - Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.

        Minimum value = ``0``

        Maximum value = ``32``
    * - application

        *(str)*
      -
      - Name of the application used to determine the state of the service. Applicable to monitors of type ``CITRIX-XML-SERVICE``.

        Minimum length = 1
    * - attribute

        *(str)*
      -
      - Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.

        Minimum length = 1
    * - authapplicationid

        *(list)*
      -
      - List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.

        Minimum value = ``0``

        Maximum value = ``4294967295``
    * - basedn

        *(str)*
      -
      - The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for ``LDAP`` service monitoring.

        Minimum length = 1
    * - binddn

        *(str)*
      -
      - The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to ``LDAP`` monitors.

        Minimum length = 1
    * - customheaders

        *(str)*
      -
      - Custom header string to include in the monitoring probes.
    * - database

        *(str)*
      -
      - Name of the database to connect to during authentication.

        Minimum length = 1
    * - destip

        *(str)*
      -
      - IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.
    * - destport

        *(int)*
      -
      - TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type ``USER``, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type ``PING``.
    * - deviation

        *(float)*
      -
      - Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.

        Minimum value = ``0``

        Maximum value = ``20939``
    * - dispatcherip

        *(str)*
      -
      - IP address of the dispatcher to which to send the probe.
    * - dispatcherport

        *(int)*
      -
      - Port number on which the dispatcher listens for the monitoring probe.
    * - domain

        *(str)*
      -
      - Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by ``CITRIX-XD-DDC`` and ``CITRIX-WI-EXTENDED`` monitors for logging on to the DDC servers and Web Interface servers, respectively.
    * - downtime

        *(int)*
      -
      - Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.

        Minimum value = ``1``

        Maximum value = ``20939``
    * - evalrule

        *(str)*
      -
      - Default syntax expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds.

        For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule ``MYSQL.RES.ROW(10`` .TEXT_ELEM(2).EQ("MySQL")).
    * - failureretries

        *(int)*
      -
      - Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.

        Minimum value = ``0``

        Maximum value = ``32``
    * - filename

        *(str)*
      -
      - Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to ``FTP-EXTENDED`` monitors.

        Minimum length = 1
    * - filter

        *(str)*
      -
      - Filter criteria for the LDAP query. Optional.

        Minimum length = 1
    * - firmwarerevision

        *(float)*
      -
      - Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
    * - group

        *(str)*
      -
      - Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.

        Minimum length = 1
    * - hostipaddress

        *(str)*
      -
      - Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.

        Minimum length = 1
    * - hostname

        *(str)*
      -
      - Hostname in the FQDN format (Example: ``porche.cars.org``). Applicable to ``STOREFRONT`` monitors.

        Minimum length = 1
    * - httprequest

        *(str)*
      -
      - HTTP request to send to the server (for example, ``HEAD /file.html``).
    * - inbandsecurityid

        *(str)*
      - Choices:

          - NO_INBAND_SECURITY
          - TLS
      - Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - interval

        *(int)*
      -
      - Time interval between two successive probes. Must be greater than the value of Response Time-out.

        Minimum value = ``1``

        Maximum value = ``20940``
    * - ipaddress

        *(list)*
      -
      - Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to ``DNS`` monitors.

        Minimum length = 1
    * - iptunnel

        *(bool)*
      -
      - Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.
    * - lasversion

        *(str)*
      -
      - Version number of the Citrix Advanced Access Control Logon Agent. Required by the ``CITRIX-AAC-LAS`` monitor.
    * - logonpointname

        *(str)*
      -
      - Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to ``CITRIX-AAC-LAS`` and ``CITRIX-AAC-LOGINPAGE`` monitors.
    * - lrtm

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - maxforwards

        *(float)*
      -
      - Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type ``SIP-UDP``.

        Minimum value = ``0``

        Maximum value = ``255``
    * - monitorname

        *(str)*
      -
      - Name for the monitor. Must begin with an ASCII alphanumeric or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore, hash ``#``, period ``.``, space `` ``, colon ``:``, at ``@``, equals ``=``, and hyphen ``-`` characters.

        Minimum length = 1
    * - mssqlprotocolversion

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
      - Version of MSSQL server that is to be monitored.
    * - netprofile

        *(str)*
      -
      - Name of the network profile.

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
      - The password with which to authenticate to the netscaler node.
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
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - oraclesid

        *(str)*
      -
      - Name of the service identifier that is used to connect to the Oracle database during authentication.

        Minimum length = 1
    * - originhost

        *(str)*
      -
      - Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

        Minimum length = 1
    * - originrealm

        *(str)*
      -
      - Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

        Minimum length = 1
    * - password

        *(str)*
      -
      - Password that is required for logging on to the ``RADIUS``, ``NNTP``, ``FTP``, ``FTP-EXTENDED``, ``MYSQL``, ``MSSQL``, ``POP3``, ``CITRIX-AG``, ``CITRIX-XD-DDC``, ``CITRIX-WI-EXTENDED``, ``CITRIX-XNC-ECV`` or ``CITRIX-XDM`` server. Used in conjunction with the user name specified for the ``username`` parameter.

        Minimum length = 1
    * - productname

        *(str)*
      -
      - Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

        Minimum length = 1
    * - query

        *(str)*
      -
      - Domain name to resolve as part of monitoring the DNS service (for example, ``example.com``).
    * - querytype

        *(str)*
      - Choices:

          - Address
          - Zone
          - AAAA
      - Type of DNS record for which to send monitoring queries. Set to ``Address`` for querying A records, ``AAAA`` for querying AAAA records, and ``Zone`` for querying the SOA record.
    * - radaccountsession

        *(str)*
      -
      - Account Session ID to be used in Account Request Packet. Applicable to monitors of type ``RADIUS_ACCOUNTING``.

        Minimum length = 1
    * - radaccounttype

        *(float)*
      -
      - Account Type to be used in Account Request Packet. Applicable to monitors of type ``RADIUS_ACCOUNTING``.

        Minimum value = 0

        Maximum value = 15
    * - radapn

        *(str)*
      -
      - Called Station Id to be used in Account Request Packet. Applicable to monitors of type ``RADIUS_ACCOUNTING``.

        Minimum length = 1
    * - radframedip

        *(str)*
      -
      - Source ip with which the packet will go out . Applicable to monitors of type ``RADIUS_ACCOUNTING``.
    * - radkey

        *(str)*
      -
      - Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type ``RADIUS`` and ``RADIUS_ACCOUNTING``.

        Minimum length = 1
    * - radmsisdn

        *(str)*
      -
      - Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type ``RADIUS_ACCOUNTING``.

        Minimum length = 1
    * - radnasid

        *(str)*
      -
      - NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type ``RADIUS``.

        Minimum length = 1
    * - radnasip

        *(str)*
      -
      - Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type ``RADIUS`` and ``RADIUS_ACCOUNTING``.
    * - recv

        *(str)*
      -
      - String expected from the server for the service to be marked as UP. Applicable to ``TCP-ECV``, ``HTTP-ECV``, and ``UDP-ECV`` monitors.
    * - respcode

        *(list)*
      -
      - Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. ``HTTP`` monitors and ``RADIUS`` monitors mark the service as ``DOWN``, while ``HTTP-INLINE`` monitors perform the action indicated by the Action parameter.
    * - resptimeout

        *(int)*
      -
      - Amount of time for which the appliance must wait before it marks a probe as FAILED. Must be less than the value specified for the Interval parameter.

        Note: For ``UDP-ECV`` monitors for which a receive string is not configured, response timeout does not apply. For ``UDP-ECV`` monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.

        Minimum value = ``1``

        Maximum value = ``20939``
    * - resptimeoutthresh

        *(float)*
      -
      - Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.

        Minimum value = ``0``

        Maximum value = ``100``
    * - retries

        *(int)*
      -
      - Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.

        Minimum value = ``1``

        Maximum value = ``127``
    * - reverse

        *(bool)*
      -
      - Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.
    * - rtsprequest

        *(str)*
      -
      - RTSP request to send to the server (for example, ``"OPTIONS *"``).
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - scriptargs

        *(str)*
      -
      - String of arguments for the script. The string is copied verbatim into the request.
    * - scriptname

        *(str)*
      -
      - Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.

        Minimum length = 1
    * - secondarypassword

        *(str)*
      -
      - Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to ``CITRIX-AG`` monitors.
    * - secure

        *(bool)*
      -
      - Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a ``CITRIX-AG`` monitor, because a CITRIX-AG monitor uses a secure connection by default.
    * - send

        *(str)*
      -
      - String to send to the service. Applicable to ``TCP-ECV``, ``HTTP-ECV``, and ``UDP-ECV`` monitors.
    * - sipmethod

        *(str)*
      - Choices:

          - OPTIONS
          - INVITE
          - REGISTER
      - SIP method to use for the query. Applicable only to monitors of type ``SIP-UDP``.
    * - sipreguri

        *(str)*
      -
      - SIP user to be registered. Applicable only if the monitor is of type ``SIP-UDP`` and the SIP Method parameter is set to ``REGISTER``.

        Minimum length = 1
    * - sipuri

        *(str)*
      -
      - SIP URI string to send to the service (for example, ``sip:sip.test``). Applicable only to monitors of type ``SIP-UDP``.

        Minimum length = 1
    * - sitepath

        *(str)*
      -
      - URL of the logon page. For monitors of type ``CITRIX-WEB-INTERFACE``, to monitor a dynamic page under the site path, terminate the site path with a slash ``/``. Applicable to ``CITRIX-WEB-INTERFACE``, ``CITRIX-WI-EXTENDED`` and ``CITRIX-XDM`` monitors.

        Minimum length = 1
    * - snmpcommunity

        *(str)*
      -
      - Community name for ``SNMP`` monitors.

        Minimum length = 1
    * - snmpthreshold

        *(str)*
      -
      - Threshold for ``SNMP`` monitors.

        Minimum length = 1
    * - snmpversion

        *(str)*
      - Choices:

          - V1
          - V2
      - SNMP version to be used for ``SNMP`` monitors.
    * - sqlquery

        *(str)*
      -
      - SQL query for a ``MYSQL-ECV`` or ``MSSQL-ECV`` monitor. Sent to the database server after the server authenticates the connection.

        Minimum length = 1
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - storedb

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Store the database list populated with the responses to monitor probes. Used in database specific load balancing if ``MSSQL-ECV``/C(MYSQL-ECV) monitor is configured.
    * - storefrontacctservice

        *(bool)*
      -
      - Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.
    * - storefrontcheckbackendservices

        *(bool)*
      -
      - This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.
    * - storename

        *(str)*
      -
      - Store Name. For monitors of type ``STOREFRONT``, ``storename`` is an optional argument defining storefront service store name. Applicable to ``STOREFRONT`` monitors.

        Minimum length = 1
    * - successretries

        *(int)*
      -
      - Number of consecutive successful probes required to transition a service's state from DOWN to UP.

        Minimum value = ``1``

        Maximum value = ``32``
    * - supportedvendorids

        *(list)*
      -
      - List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.

        Minimum value = ``1``

        Maximum value = ``4294967295``
    * - tos

        *(bool)*
      -
      - Probe the service by encoding the destination IP address in the IP TOS (6) bits.
    * - tosid

        *(float)*
      -
      - The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.

        Minimum value = ``1``

        Maximum value = ``63``
    * - transparent

        *(bool)*
      -
      - The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.
    * - trofscode

        *(float)*
      -
      - Code expected when the server is under maintenance.
    * - trofsstring

        *(str)*
      -
      - String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.
    * - type

        *(str)*
      - Choices:

          - PING
          - TCP
          - HTTP
          - TCP-ECV
          - HTTP-ECV
          - UDP-ECV
          - DNS
          - FTP
          - LDNS-PING
          - LDNS-TCP
          - LDNS-DNS
          - RADIUS
          - USER
          - HTTP-INLINE
          - SIP-UDP
          - SIP-TCP
          - LOAD
          - FTP-EXTENDED
          - SMTP
          - SNMP
          - NNTP
          - MYSQL
          - MYSQL-ECV
          - MSSQL-ECV
          - ORACLE-ECV
          - LDAP
          - POP3
          - CITRIX-XML-SERVICE
          - CITRIX-WEB-INTERFACE
          - DNS-TCP
          - RTSP
          - ARP
          - CITRIX-AG
          - CITRIX-AAC-LOGINPAGE
          - CITRIX-AAC-LAS
          - CITRIX-XD-DDC
          - ND6
          - CITRIX-WI-EXTENDED
          - DIAMETER
          - RADIUS_ACCOUNTING
          - STOREFRONT
          - APPC
          - SMPP
          - CITRIX-XNC-ECV
          - CITRIX-XDM
          - CITRIX-STA-SERVICE
          - CITRIX-STA-SERVICE-NHOP
      - Type of monitor that you want to create.
    * - units1

        *(str)*
      - Choices:

          - SEC
          - MSEC
          - MIN
      - Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.
    * - units2

        *(str)*
      - Choices:

          - SEC
          - MSEC
          - MIN
      - Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.
    * - units3

        *(str)*
      - Choices:

          - SEC
          - MSEC
          - MIN
      - monitor interval units.
    * - units4

        *(str)*
      - Choices:

          - SEC
          - MSEC
          - MIN
      - monitor response timeout units.
    * - username

        *(str)*
      -
      - User name with which to probe the ``RADIUS``, ``NNTP``, ``FTP``, ``FTP-EXTENDED``, ``MYSQL``, ``MSSQL``, ``POP3``, ``CITRIX-AG``, ``CITRIX-XD-DDC``, ``CITRIX-WI-EXTENDED``, ``CITRIX-XNC`` or ``CITRIX-XDM`` server.

        Minimum length = 1
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - validatecred

        *(bool)*
      -
      - Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type ``CITRIX-XD-DDC``.
    * - vendorid

        *(float)*
      -
      - Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
    * - vendorspecificacctapplicationids

        *(list)*
      -
      - List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.

        Minimum value = ``0``

        Maximum value = ``4294967295``
    * - vendorspecificauthapplicationids

        *(list)*
      -
      - List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.

        Minimum value = ``0``

        Maximum value = ``4294967295``
    * - vendorspecificvendorid

        *(float)*
      -
      - Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.

        Minimum value = 1



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Set lb monitor
      local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
    
        module: citrix_adc_lb_monitor
        state: present
    
        monitorname: monitor_1
        type: HTTP-INLINE
        action: DOWN
        respcode: ['400']


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

        {'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2'}
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
