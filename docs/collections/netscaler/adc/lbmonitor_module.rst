
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.netscaler.adc.lbmonitor_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.lbmonitor module -- Configuration for monitor resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.lbmonitor`.

.. version_added

.. rst-class:: ansible-version-added

New in netscaler.adc 2.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Configuration for monitor resource.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-acctapplicationid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-acctapplicationid:

      .. rst-class:: ansible-option-title

      **acctapplicationid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-acctapplicationid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-action"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-action:

      .. rst-class:: ansible-option-title

      **action**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-action" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE) indicates that the service is down. A service monitored by an inline monitor is considered DOWN if the response code is not one of the codes that have been specified for the Response Code parameter. 

      Available settings function as follows: 

      \* NONE - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.

      \* LOG - Log the event in NSLOG or SYSLOG. 

      \* DOWN - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NONE"`
      - :ansible-option-choices-entry:`"LOG"`
      - :ansible-option-choices-entry-default:`"DOWN"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-alertretries"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-alertretries:

      .. rst-class:: ansible-option-title

      **alertretries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-alertretries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-api_path:

      .. rst-class:: ansible-option-title

      **api_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-api_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Base NITRO API path.

      Define only in case of an ADM service proxy call


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-application"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-application:

      .. rst-class:: ansible-option-title

      **application**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-application" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-attribute:

      .. rst-class:: ansible-option-title

      **attribute**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authapplicationid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-authapplicationid:

      .. rst-class:: ansible-option-title

      **authapplicationid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authapplicationid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-basedn"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-basedn:

      .. rst-class:: ansible-option-title

      **basedn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-basedn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for LDAP service monitoring.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-bearer_token:

      .. rst-class:: ansible-option-title

      **bearer_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bearer_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Authentication bearer token.

      Needed when doing an ADM service proxy call.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-binddn"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-binddn:

      .. rst-class:: ansible-option-title

      **binddn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-binddn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-customheaders"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-customheaders:

      .. rst-class:: ansible-option-title

      **customheaders**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-customheaders" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Custom header string to include in the monitoring probes.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-database"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-database:

      .. rst-class:: ansible-option-title

      **database**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-database" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the database to connect to during authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-destip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-destip:

      .. rst-class:: ansible-option-title

      **destip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-destip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-destport"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-destport:

      .. rst-class:: ansible-option-title

      **destport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-destport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type USER, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type PING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-deviation"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-deviation:

      .. rst-class:: ansible-option-title

      **deviation**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-deviation" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dispatcherip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-dispatcherip:

      .. rst-class:: ansible-option-title

      **dispatcherip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dispatcherip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the dispatcher to which to send the probe.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dispatcherport"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-dispatcherport:

      .. rst-class:: ansible-option-title

      **dispatcherport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dispatcherport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number on which the dispatcher listens for the monitoring probe.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-domain"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-domain:

      .. rst-class:: ansible-option-title

      **domain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED monitors for logging on to the DDC servers and Web Interface servers, respectively.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-downtime"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-downtime:

      .. rst-class:: ansible-option-title

      **downtime**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-downtime" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`30`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-evalrule"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-evalrule:

      .. rst-class:: ansible-option-title

      **evalrule**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-evalrule" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds. 

      For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT\_ELEM(2).EQ("MySQL").


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-failureretries"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-failureretries:

      .. rst-class:: ansible-option-title

      **failureretries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-failureretries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filename"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-filename:

      .. rst-class:: ansible-option-title

      **filename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to FTP-EXTENDED monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filter"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-filter:

      .. rst-class:: ansible-option-title

      **filter**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filter" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter criteria for the LDAP query. Optional.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-firmwarerevision"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-firmwarerevision:

      .. rst-class:: ansible-option-title

      **firmwarerevision**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-firmwarerevision" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-group"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-group:

      .. rst-class:: ansible-option-title

      **group**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-group" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grpchealthcheck"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-grpchealthcheck:

      .. rst-class:: ansible-option-title

      **grpchealthcheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grpchealthcheck" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to enable or disable gRPC health check service.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grpcservicename"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-grpcservicename:

      .. rst-class:: ansible-option-title

      **grpcservicename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grpcservicename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to specify gRPC service name on which gRPC health check need to be performed


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grpcstatuscode"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-grpcstatuscode:

      .. rst-class:: ansible-option-title

      **grpcstatuscode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grpcstatuscode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      gRPC status codes for which to mark the service as UP. The default value is 12(health check unimplemented). If the gRPC status code 0 is received from the backend this configuration is ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostipaddress"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-hostipaddress:

      .. rst-class:: ansible-option-title

      **hostipaddress**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostipaddress" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hostname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-hostname:

      .. rst-class:: ansible-option-title

      **hostname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httprequest"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-httprequest:

      .. rst-class:: ansible-option-title

      **httprequest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-httprequest" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      HTTP request to send to the server (for example, "HEAD /file.html").


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-inbandsecurityid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-inbandsecurityid:

      .. rst-class:: ansible-option-title

      **inbandsecurityid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-inbandsecurityid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NO\_INBAND\_SECURITY"`
      - :ansible-option-choices-entry:`"TLS"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-instance_id:

      .. rst-class:: ansible-option-title

      **instance_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-instance_id" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The id of the target NetScaler ADC instance when issuing a Nitro request through a NetScaler ADM proxy.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_ip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-instance_ip:

      .. rst-class:: ansible-option-title

      **instance_ip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-instance_ip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in netscaler.adc 2.6.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The target NetScaler ADC instance ip address to which all underlying NITRO API calls will be proxied to.

      It is meaningful only when having set \ :literal:`mas\_proxy\_call`\  to \ :literal:`true`\ 


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_name"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-instance_name:

      .. rst-class:: ansible-option-title

      **instance_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-instance_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the target NetScaler ADC instance when issuing a Nitro request through a NetScaler ADM proxy.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-interval"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-interval:

      .. rst-class:: ansible-option-title

      **interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-interval" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time interval between two successive probes. Must be greater than the value of Response Time-out.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`5`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipaddress"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-ipaddress:

      .. rst-class:: ansible-option-title

      **ipaddress**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipaddress" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-iptunnel"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-iptunnel:

      .. rst-class:: ansible-option-title

      **iptunnel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-iptunnel" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-is_cloud:

      .. rst-class:: ansible-option-title

      **is_cloud**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-is_cloud" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When performing a Proxy API call with ADM service set this to \ :literal:`true`\ 


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-kcdaccount"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-kcdaccount:

      .. rst-class:: ansible-option-title

      **kcdaccount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-kcdaccount" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      KCD Account used by MSSQL monitor


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lasversion"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-lasversion:

      .. rst-class:: ansible-option-title

      **lasversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lasversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logonpointname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-logonpointname:

      .. rst-class:: ansible-option-title

      **logonpointname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logonpointname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lrtm"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-lrtm:

      .. rst-class:: ansible-option-title

      **lrtm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lrtm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-mas_proxy_call:

      .. rst-class:: ansible-option-title

      **mas_proxy_call**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mas_proxy_call" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      :ansible-option-versionadded:`added in netscaler.adc 2.6.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`true`\  the underlying NITRO API calls made by the module will be proxied through a NetScaler ADM node to the target NetScaler ADC instance.

      When \ :literal:`true`\  you must also define the following options: \ :emphasis:`nitro\_auth\_token`\ 

      When \ :literal:`true`\  and adm service is the api proxy the following option must also be defined: \ :emphasis:`bearer\_token`\ 

      When \ :literal:`true`\  you must define a target ADC by defining any of the following parameters

      \ :emphasis:`instance\_ip`\ 

      \ :emphasis:`instance\_id`\ 

      \ :emphasis:`instance\_name`\ 


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-maxforwards"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-maxforwards:

      .. rst-class:: ansible-option-title

      **maxforwards**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maxforwards" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-metric"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-metric:

      .. rst-class:: ansible-option-title

      **metric**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-metric" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-metrictable"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-metrictable:

      .. rst-class:: ansible-option-title

      **metrictable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-metrictable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Metric table to which to bind metrics.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-metricthreshold"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-metricthreshold:

      .. rst-class:: ansible-option-title

      **metricthreshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-metricthreshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Threshold to be used for that metric.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-metricweight"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-metricweight:

      .. rst-class:: ansible-option-title

      **metricweight**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-metricweight" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The weight for the specified service metric with respect to others.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-monitorname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-monitorname:

      .. rst-class:: ansible-option-title

      **monitorname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-monitorname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name for the monitor. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.

      

      CLI Users:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my monitor" or 'my monitor').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mqttclientidentifier"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-mqttclientidentifier:

      .. rst-class:: ansible-option-title

      **mqttclientidentifier**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mqttclientidentifier" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Client id to be used in Connect command


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mqttversion"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-mqttversion:

      .. rst-class:: ansible-option-title

      **mqttversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mqttversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Version of MQTT protocol used in connect message, default is version 3.1.1 [4]


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mssqlprotocolversion"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-mssqlprotocolversion:

      .. rst-class:: ansible-option-title

      **mssqlprotocolversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mssqlprotocolversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Version of MSSQL server that is to be monitored.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"70"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"2000"`
      - :ansible-option-choices-entry:`"2000SP1"`
      - :ansible-option-choices-entry:`"2005"`
      - :ansible-option-choices-entry:`"2008"`
      - :ansible-option-choices-entry:`"2008R2"`
      - :ansible-option-choices-entry:`"2012"`
      - :ansible-option-choices-entry:`"2014"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netprofile"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-netprofile:

      .. rst-class:: ansible-option-title

      **netprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the network profile.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nitro_auth_token:

      .. rst-class:: ansible-option-title

      **nitro_auth_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nitro_auth_token" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      :ansible-option-versionadded:`added in netscaler.adc 2.6.0`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The authentication token provided by a login operation.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_pass"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nitro_pass:

      .. rst-class:: ansible-option-title

      **nitro_pass**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nitro_pass" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The password with which to authenticate to the NetScaler ADC node.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_protocol"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nitro_protocol:

      .. rst-class:: ansible-option-title

      **nitro_protocol**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nitro_protocol" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Which protocol to use when accessing the nitro API objects.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"http"`
      - :ansible-option-choices-entry-default:`"https"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_timeout"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nitro_timeout:

      .. rst-class:: ansible-option-title

      **nitro_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nitro_timeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`float`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time in seconds until a timeout error is thrown when establishing a new session with NetScaler ADC


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`310.0`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_user"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nitro_user:

      .. rst-class:: ansible-option-title

      **nitro_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nitro_user" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The username with which to authenticate to the NetScaler ADC node.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nsip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-nsip:

      .. rst-class:: ansible-option-title

      **nsip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nsip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ip address of the NetScaler ADC appliance where the nitro API calls will be made.

      The port can be specified with the colon (:). E.g. 192.168.1.1:555.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-oraclesid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-oraclesid:

      .. rst-class:: ansible-option-title

      **oraclesid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-oraclesid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the service identifier that is used to connect to the Oracle database during authentication.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-originhost"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-originhost:

      .. rst-class:: ansible-option-title

      **originhost**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-originhost" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-originrealm"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-originrealm:

      .. rst-class:: ansible-option-title

      **originrealm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-originrealm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server. Used in conjunction with the user name specified for the User Name parameter.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-productname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-productname:

      .. rst-class:: ansible-option-title

      **productname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-productname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-query"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-query:

      .. rst-class:: ansible-option-title

      **query**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-query" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Domain name to resolve as part of monitoring the DNS service (for example, example.com).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-querytype"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-querytype:

      .. rst-class:: ansible-option-title

      **querytype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-querytype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of DNS record for which to send monitoring queries. Set to Address for querying A records, AAAA for querying AAAA records, and Zone for querying the SOA record.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Address"`
      - :ansible-option-choices-entry:`"Zone"`
      - :ansible-option-choices-entry:`"AAAA"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radaccountsession"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radaccountsession:

      .. rst-class:: ansible-option-title

      **radaccountsession**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radaccountsession" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radaccounttype"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radaccounttype:

      .. rst-class:: ansible-option-title

      **radaccounttype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radaccounttype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS\_ACCOUNTING.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radapn"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radapn:

      .. rst-class:: ansible-option-title

      **radapn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radapn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radframedip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radframedip:

      .. rst-class:: ansible-option-title

      **radframedip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radframedip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Source ip with which the packet will go out . Applicable to monitors of type RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radkey"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radkey:

      .. rst-class:: ansible-option-title

      **radkey**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radkey" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type RADIUS and RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radmsisdn"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radmsisdn:

      .. rst-class:: ansible-option-title

      **radmsisdn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radmsisdn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radnasid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radnasid:

      .. rst-class:: ansible-option-title

      **radnasid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radnasid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-radnasip"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-radnasip:

      .. rst-class:: ansible-option-title

      **radnasip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-radnasip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS\_ACCOUNTING.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recv"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-recv:

      .. rst-class:: ansible-option-title

      **recv**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recv" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-respcode"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-respcode:

      .. rst-class:: ansible-option-title

      **respcode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-respcode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform the action indicated by the Action parameter.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resptimeout"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-resptimeout:

      .. rst-class:: ansible-option-title

      **resptimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resptimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Amount of time for which the appliance must wait before it marks a probe as FAILED.  Must be less than the value specified for the Interval parameter.

      

      Note: For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply. For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resptimeoutthresh"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-resptimeoutthresh:

      .. rst-class:: ansible-option-title

      **resptimeoutthresh**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resptimeoutthresh" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-retries"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-retries:

      .. rst-class:: ansible-option-title

      **retries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-retries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`3`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reverse"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-reverse:

      .. rst-class:: ansible-option-title

      **reverse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reverse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rtsprequest"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-rtsprequest:

      .. rst-class:: ansible-option-title

      **rtsprequest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rtsprequest" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      RTSP request to send to the server (for example, "OPTIONS \*").


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-save_config:

      .. rst-class:: ansible-option-title

      **save_config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-save_config" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`true`\  the module will save the configuration on the NetScaler ADC node if it makes any changes.

      The module will not save the configuration on the NetScaler ADC node if it made no changes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scriptargs"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-scriptargs:

      .. rst-class:: ansible-option-title

      **scriptargs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scriptargs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      String of arguments for the script. The string is copied verbatim into the request.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scriptname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-scriptname:

      .. rst-class:: ansible-option-title

      **scriptname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scriptname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path and name of the script to execute. The script must be available on the Citrix ADC, in the /nsconfig/monitors/ directory.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secondarypassword"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-secondarypassword:

      .. rst-class:: ansible-option-title

      **secondarypassword**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secondarypassword" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secure"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-secure:

      .. rst-class:: ansible-option-title

      **secure**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secure" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-secureargs"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-secureargs:

      .. rst-class:: ansible-option-title

      **secureargs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-secureargs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of arguments for the script which should be secure


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-send"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-send:

      .. rst-class:: ansible-option-title

      **send**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-send" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-servicegroupname"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-servicegroupname:

      .. rst-class:: ansible-option-title

      **servicegroupname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-servicegroupname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the service group to which the monitor is to be bound.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-servicename"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-servicename:

      .. rst-class:: ansible-option-title

      **servicename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-servicename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the service to which the monitor is bound.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sipmethod"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sipmethod:

      .. rst-class:: ansible-option-title

      **sipmethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sipmethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SIP method to use for the query. Applicable only to monitors of type SIP-UDP.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"OPTIONS"`
      - :ansible-option-choices-entry:`"INVITE"`
      - :ansible-option-choices-entry:`"REGISTER"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sipreguri"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sipreguri:

      .. rst-class:: ansible-option-title

      **sipreguri**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sipreguri" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sipuri"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sipuri:

      .. rst-class:: ansible-option-title

      **sipuri**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sipuri" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sitepath"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sitepath:

      .. rst-class:: ansible-option-title

      **sitepath**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sitepath" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path, terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmpcommunity"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-snmpcommunity:

      .. rst-class:: ansible-option-title

      **snmpcommunity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmpcommunity" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Community name for SNMP monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-Snmpoid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-snmpoid:

      .. rst-class:: ansible-option-title

      **Snmpoid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-Snmpoid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SNMP OID for SNMP monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmpthreshold"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-snmpthreshold:

      .. rst-class:: ansible-option-title

      **snmpthreshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmpthreshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Threshold for SNMP monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snmpversion"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-snmpversion:

      .. rst-class:: ansible-option-title

      **snmpversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snmpversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SNMP version to be used for SNMP monitors.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"V1"`
      - :ansible-option-choices-entry:`"V2"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlquery"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sqlquery:

      .. rst-class:: ansible-option-title

      **sqlquery**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlquery" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-sslprofile:

      .. rst-class:: ansible-option-title

      **sslprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SSL Profile associated with the monitor


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the monitor. The DISABLED setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to ENABLED. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-storedb"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-storedb:

      .. rst-class:: ansible-option-title

      **storedb**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-storedb" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Store the database list populated with the responses to monitor probes. Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-storefrontacctservice"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-storefrontacctservice:

      .. rst-class:: ansible-option-title

      **storefrontacctservice**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-storefrontacctservice" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-storefrontcheckbackendservices"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-storefrontcheckbackendservices:

      .. rst-class:: ansible-option-title

      **storefrontcheckbackendservices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-storefrontcheckbackendservices" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-storename"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-storename:

      .. rst-class:: ansible-option-title

      **storename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-storename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument defining storefront service store name. Applicable to STOREFRONT monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-successretries"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-successretries:

      .. rst-class:: ansible-option-title

      **successretries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-successretries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of consecutive successful probes required to transition a service's state from DOWN to UP.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-supportedvendorids"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-supportedvendorids:

      .. rst-class:: ansible-option-title

      **supportedvendorids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-supportedvendorids" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tos"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-tos:

      .. rst-class:: ansible-option-title

      **tos**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tos" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Probe the service by encoding the destination IP address in the IP TOS (6) bits.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tosid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-tosid:

      .. rst-class:: ansible-option-title

      **tosid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tosid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-transparent"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-transparent:

      .. rst-class:: ansible-option-title

      **transparent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-transparent" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trofscode"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-trofscode:

      .. rst-class:: ansible-option-title

      **trofscode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trofscode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Code expected when the server is under maintenance


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trofsstring"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-trofsstring:

      .. rst-class:: ansible-option-title

      **trofsstring**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trofsstring" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of monitor that you want to create.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"PING"`
      - :ansible-option-choices-entry:`"TCP"`
      - :ansible-option-choices-entry:`"HTTP"`
      - :ansible-option-choices-entry:`"TCP-ECV"`
      - :ansible-option-choices-entry:`"HTTP-ECV"`
      - :ansible-option-choices-entry:`"UDP-ECV"`
      - :ansible-option-choices-entry:`"DNS"`
      - :ansible-option-choices-entry:`"FTP"`
      - :ansible-option-choices-entry:`"LDNS-PING"`
      - :ansible-option-choices-entry:`"LDNS-TCP"`
      - :ansible-option-choices-entry:`"LDNS-DNS"`
      - :ansible-option-choices-entry:`"RADIUS"`
      - :ansible-option-choices-entry:`"USER"`
      - :ansible-option-choices-entry:`"HTTP-INLINE"`
      - :ansible-option-choices-entry:`"SIP-UDP"`
      - :ansible-option-choices-entry:`"SIP-TCP"`
      - :ansible-option-choices-entry:`"LOAD"`
      - :ansible-option-choices-entry:`"FTP-EXTENDED"`
      - :ansible-option-choices-entry:`"SMTP"`
      - :ansible-option-choices-entry:`"SNMP"`
      - :ansible-option-choices-entry:`"NNTP"`
      - :ansible-option-choices-entry:`"MYSQL"`
      - :ansible-option-choices-entry:`"MYSQL-ECV"`
      - :ansible-option-choices-entry:`"MSSQL-ECV"`
      - :ansible-option-choices-entry:`"ORACLE-ECV"`
      - :ansible-option-choices-entry:`"LDAP"`
      - :ansible-option-choices-entry:`"POP3"`
      - :ansible-option-choices-entry:`"CITRIX-XML-SERVICE"`
      - :ansible-option-choices-entry:`"CITRIX-WEB-INTERFACE"`
      - :ansible-option-choices-entry:`"DNS-TCP"`
      - :ansible-option-choices-entry:`"RTSP"`
      - :ansible-option-choices-entry:`"ARP"`
      - :ansible-option-choices-entry:`"CITRIX-AG"`
      - :ansible-option-choices-entry:`"CITRIX-AAC-LOGINPAGE"`
      - :ansible-option-choices-entry:`"CITRIX-AAC-LAS"`
      - :ansible-option-choices-entry:`"CITRIX-XD-DDC"`
      - :ansible-option-choices-entry:`"ND6"`
      - :ansible-option-choices-entry:`"CITRIX-WI-EXTENDED"`
      - :ansible-option-choices-entry:`"DIAMETER"`
      - :ansible-option-choices-entry:`"RADIUS\_ACCOUNTING"`
      - :ansible-option-choices-entry:`"STOREFRONT"`
      - :ansible-option-choices-entry:`"APPC"`
      - :ansible-option-choices-entry:`"SMPP"`
      - :ansible-option-choices-entry:`"CITRIX-XNC-ECV"`
      - :ansible-option-choices-entry:`"CITRIX-XDM"`
      - :ansible-option-choices-entry:`"CITRIX-STA-SERVICE"`
      - :ansible-option-choices-entry:`"CITRIX-STA-SERVICE-NHOP"`
      - :ansible-option-choices-entry:`"MQTT"`
      - :ansible-option-choices-entry:`"HTTP2"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-units1"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-units1:

      .. rst-class:: ansible-option-title

      **units1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-units1" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"SEC"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"MSEC"`
      - :ansible-option-choices-entry:`"MIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-units2"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-units2:

      .. rst-class:: ansible-option-title

      **units2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-units2" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"SEC"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"MSEC"`
      - :ansible-option-choices-entry:`"MIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-units3"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-units3:

      .. rst-class:: ansible-option-title

      **units3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-units3" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      monitor interval units


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"SEC"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"MSEC"`
      - :ansible-option-choices-entry:`"MIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-units4"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-units4:

      .. rst-class:: ansible-option-title

      **units4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-units4" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      monitor response timeout units


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"SEC"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"MSEC"`
      - :ansible-option-choices-entry:`"MIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-validate_certs:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If \ :literal:`false`\ , SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validatecred"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-validatecred:

      .. rst-class:: ansible-option-title

      **validatecred**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-validatecred" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vendorid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-vendorid:

      .. rst-class:: ansible-option-title

      **vendorid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vendorid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vendorspecificacctapplicationids"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-vendorspecificacctapplicationids:

      .. rst-class:: ansible-option-title

      **vendorspecificacctapplicationids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vendorspecificacctapplicationids" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vendorspecificauthapplicationids"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-vendorspecificauthapplicationids:

      .. rst-class:: ansible-option-title

      **vendorspecificauthapplicationids**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vendorspecificauthapplicationids" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-vendorspecificvendorid"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__parameter-vendorspecificvendorid:

      .. rst-class:: ansible-option-title

      **vendorspecificvendorid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vendorspecificvendorid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - For more information on using Ansible to manage NetScaler ADC Network devices see \ https://www.ansible.com/integrations/networks/citrixadc\ .

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__return-changed:

      .. rst-class:: ansible-option-title

      **changed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates if any change is made by the module


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`true`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-diff"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__return-diff:

      .. rst-class:: ansible-option-title

      **diff**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-diff" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Dictionary of before and after changes


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"after": {"key2": "pqr"}, "before": {"key1": "xyz"}, "prepared": "changes done"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-diff_list"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__return-diff_list:

      .. rst-class:: ansible-option-title

      **diff_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-diff_list" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of differences between the actual configured object and the configuration specified in the module


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when changed

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`["Attribute \`key1\` differs. Desired: (\<class 'str'\>) XYZ. Existing: (\<class 'str'\>) PQR"]`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-failed"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__return-failed:

      .. rst-class:: ansible-option-title

      **failed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-failed" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates if the module failed or not


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`false`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-loglines"></div>

      .. _ansible_collections.netscaler.adc.lbmonitor_module__return-loglines:

      .. rst-class:: ansible-option-title

      **loglines**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-loglines" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      list of logged messages by the module


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`["message 1", "message 2"]`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Sumanth Lingappa (@sumanth-lingappa)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="http://example.com/issue/tracker" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="http://example.com" aria-role="button" target="_blank" rel="noopener external">Homepage</a>
    <a href="http://example.com/repository" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

