:orphan:

.. _citrix_adc_gslb_vserver_module:

citrix_adc_gslb_vserver - Configure gslb vserver entities in Netscaler.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Configure gslb vserver entities in Netscaler.



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
    * - appflowlog

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Enable logging appflow flow information.
    * - backuplbmethod

        *(str)*
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - SOURCEIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - STATICPROXIMITY
          - RTT
          - CUSTOMLOAD
      - Backup load balancing method. Becomes operational if the primary load balancing method fails or cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static proximity.
    * - comment

        *(str)*
      -
      - Any comments that you might want to associate with the GSLB virtual server.
    * - considereffectivestate

        *(str)*
      - Choices:

          - NONE
          - STATE_ONLY
      - If the primary state of all bound GSLB services is DOWN, consider the effective states of all the GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To disregard the effective state, set the parameter to NONE.

        The effective state of a GSLB service is the ability of the corresponding virtual server to serve traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP state.
    * - cookie_domain

        *(str)*
      -
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``yes`` the GSLB Vserver state will be set to ``disabled``.

        When set to ``no`` the GSLB Vserver state will be set to ``enabled``.

        Note that due to limitations of the underlying NITRO API a ``disabled`` state change alone does not cause the module result to report a changed status.
    * - disableprimaryondown

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to the UP state. Used when spillover is configured for the virtual server.
    * - dnsrecordtype

        *(str)*
      - Choices:

          - A
          - AAAA
          - CNAME
          - NAPTR
      - DNS record type to associate with the GSLB virtual server's domain name.

        Default value: A

        Possible values = A, AAAA, CNAME, NAPTR
    * - domain_bindings

        *(list)*
      -
      - List of bindings for domains for this glsb vserver.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - cookietimeout
              -
              - Timeout, in minutes, for the GSLB site cookie.
            * - domainname
              -
              - Domain name for which to change the time to live (TTL) and/or backup service IP address.
            * - sitedomainttl
              -
              - TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.

                Minimum value = ``1``
            * - ttl
              -
              - Time to live (TTL) for the domain.

    * - domainname

        *(str)*
      -
      - Domain name for which to change the time to live (TTL) and/or backup service IP address.
    * - dynamicweight

        *(str)*
      - Choices:

          - SERVICECOUNT
          - SERVICEWEIGHT
          - DISABLED
      - Specify if the appliance should consider the service count, service weights, or ignore both when using weight-based load balancing methods. The state of the number of services bound to the virtual server help the appliance to select the service.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - lbmethod

        *(str)*
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - SOURCEIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - STATICPROXIMITY
          - RTT
          - CUSTOMLOAD
      - Load balancing method for the GSLB virtual server.

        Default value: LEASTCONNECTION

        Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - mir

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Include multiple IP addresses in the DNS responses sent to clients.
    * - name

        *(str)*
      -
      - Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore ``_``, hash ``#``, period ``.``, space, colon ``:``, at ``@``, equals ``=``, and hyphen ``-`` characters. Can be changed after the virtual server is created.

        Minimum length = 1
    * - netmask

        *(str)*
      -
      - IPv4 network mask for use in the SOURCEIPHASH load balancing method.

        Minimum length = 1
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
    * - persistenceid

        *(float)*
      -
      - The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites to identify the GSLB virtual server, and is required if source IP address based or spill over based persistence is enabled on the virtual server.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - persistencetype

        *(str)*
      - Choices:

          - SOURCEIP
          - NONE
      - Use source IP address based persistence for the virtual server.

        After the load balancing method selects a service for the first packet, the IP address received in response to the DNS query is used for subsequent requests from the same client.
    * - persistmask

        *(str)*
      -
      - The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.

        Minimum length = 1
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - service_bindings

        *(list)*
      -
      - List of bindings for gslb services bound to this gslb virtual server.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - servicename
              -
              - Name of the GSLB service for which to change the weight.
            * - weight
              -
              - Weight to assign to the GSLB service.

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
          - NNTP
          - ANY
          - SIP_UDP
          - SIP_TCP
          - SIP_SSL
          - RADIUS
          - RDP
          - RTSP
          - MYSQL
          - MSSQL
          - ORACLE
      - Protocol used by services bound to the virtual server.

        
    * - sobackupaction

        *(str)*
      - Choices:

          - DROP
          - ACCEPT
          - REDIRECT
      - Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.
    * - somethod

        *(str)*
      - Choices:

          - CONNECTION
          - DYNAMICCONNECTION
          - BANDWIDTH
          - HEALTH
          - NONE
      - Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:

        * ``CONNECTION`` - Spillover occurs when the number of client connections exceeds the threshold.

        * ``DYNAMICCONNECTION`` - Spillover occurs when the number of client connections at the GSLB virtual server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of the bound GSLB services.

        * ``BANDWIDTH`` - Spillover occurs when the bandwidth consumed by the GSLB virtual server's incoming and outgoing traffic exceeds the threshold.

        * ``HEALTH`` - Spillover occurs when the percentage of weights of the GSLB services that are UP drops below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN.

        * ``NONE`` - Spillover does not occur.
    * - sopersistence

        *(str)*
      - Choices:

          - enabled
          - disabled
      - If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB virtual servers.
    * - sopersistencetimeout

        *(float)*
      -
      - Timeout for spillover persistence, in minutes.

        Default value: ``2``

        Minimum value = ``2``

        Maximum value = ``1440``
    * - sothreshold

        *(float)*
      -
      - Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).

        Minimum value = ``1``

        Maximum value = ``4294967287``
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - timeout

        *(float)*
      -
      - Idle time, in minutes, after which a persistence entry is cleared.

        Default value: ``2``

        Minimum value = ``2``

        Maximum value = ``1440``
    * - tolerance

        *(float)*
      -
      - Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a site's RTT deviates from the lowest RTT by more than the specified tolerance, the site is not considered when the NetScaler appliance makes a GSLB decision. The appliance implements the round robin method of global server load balancing between sites whose RTT values are within the specified tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the site with the lowest RTT.

        Minimum value = ``0``

        Maximum value = ``100``
    * - v6netmasklen

        *(float)*
      -
      - Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the ``SOURCEIPHASH`` load balancing method.

        Default value: ``128``

        Minimum value = ``1``

        Maximum value = ``128``
    * - v6persistmasklen

        *(float)*
      -
      - Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.

        Default value: ``128``

        Minimum value = ``1``

        Maximum value = ``128``
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    


Return Values
-------------
