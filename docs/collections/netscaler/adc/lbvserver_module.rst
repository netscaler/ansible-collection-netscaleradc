
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

.. _ansible_collections.netscaler.adc.lbvserver_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.lbvserver module -- Configuration for Load Balancing Virtual Server resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.lbvserver`.

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

- Configuration for Load Balancing Virtual Server resource.


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
        <div class="ansibleOptionAnchor" id="parameter-adfsproxyprofile"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-adfsproxyprofile:

      .. rst-class:: ansible-option-title

      **adfsproxyprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-adfsproxyprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the adfsProxy profile to be used to support ADFSPIP protocol for ADFS servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-api_path:

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
        <div class="ansibleOptionAnchor" id="parameter-appflowlog"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-appflowlog:

      .. rst-class:: ansible-option-title

      **appflowlog**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appflowlog" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Apply AppFlow logging to the virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authentication"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-authentication:

      .. rst-class:: ansible-option-title

      **authentication**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authentication" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable user authentication.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationhost"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-authenticationhost:

      .. rst-class:: ansible-option-title

      **authenticationhost**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationhost" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be redirected for authentication. Make sure that the Authentication parameter is set to ENABLED.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authn401"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-authn401:

      .. rst-class:: ansible-option-title

      **authn401**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authn401" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable user authentication with HTTP 401 responses.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authnprofile"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-authnprofile:

      .. rst-class:: ansible-option-title

      **authnprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authnprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the authentication profile to be used when authentication is turned on.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authnvsname"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-authnvsname:

      .. rst-class:: ansible-option-title

      **authnvsname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authnvsname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of an authentication virtual server with which to authenticate users.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-backuplbmethod"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-backuplbmethod:

      .. rst-class:: ansible-option-title

      **backuplbmethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-backuplbmethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Backup load balancing method. Becomes operational if the primary load balancing me

      thod fails or cannot be used.

                             Valid only if the primary method is based on static proximity.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ROUNDROBIN"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"LEASTCONNECTION"`
      - :ansible-option-choices-entry:`"LEASTRESPONSETIME"`
      - :ansible-option-choices-entry:`"SOURCEIPHASH"`
      - :ansible-option-choices-entry:`"LEASTBANDWIDTH"`
      - :ansible-option-choices-entry:`"LEASTPACKETS"`
      - :ansible-option-choices-entry:`"CUSTOMLOAD"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-backuppersistencetimeout"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-backuppersistencetimeout:

      .. rst-class:: ansible-option-title

      **backuppersistencetimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-backuppersistencetimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time period for which backup persistence is in effect.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-backupvserver"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-backupvserver:

      .. rst-class:: ansible-option-title

      **backupvserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-backupvserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the backup virtual server to which to forward requests if the primary virtual server goes DOWN or reaches its spillover threshold.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-bypassaaaa"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-bypassaaaa:

      .. rst-class:: ansible-option-title

      **bypassaaaa**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bypassaaaa" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns server


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cacheable"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-cacheable:

      .. rst-class:: ansible-option-title

      **cacheable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cacheable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can forward requests only to a transparent cache redirection virtual server that has an IP address and port combination of \*:80, so such a cache redirection virtual server must be configured on the appliance.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clttimeout"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-clttimeout:

      .. rst-class:: ansible-option-title

      **clttimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clttimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Idle time, in seconds, after which a client connection is terminated.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-comment"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-comment:

      .. rst-class:: ansible-option-title

      **comment**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-comment" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Any comments that you might want to associate with the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-connfailover"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-connfailover:

      .. rst-class:: ansible-option-title

      **connfailover**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-connfailover" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mode in which the connection failover feature must operate for the virtual server. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients remain connected to the same servers. Available settings function as follows:

      \* \ :literal:`STATEFUL`\  - The primary appliance shares state information with the secondary appliance, in real time, resulting in some runtime processing overhead. 

      \* \ :literal:`STATELESS`\  - State information is not shared, and the new primary appliance tries to re-create the packet flow on the basis of the information contained in the packets it receives. 

      \* \ :literal:`DISABLED`\  - Connection failover does not occur.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"STATEFUL"`
      - :ansible-option-choices-entry:`"STATELESS"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookiename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-cookiename:

      .. rst-class:: ansible-option-title

      **cookiename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookiename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-datalength"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-datalength:

      .. rst-class:: ansible-option-title

      **datalength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-datalength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Length of the token to be extracted from the data segment of an incoming packet, for use in the token method of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. Applicable to virtual servers of type TCP.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dataoffset"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-dataoffset:

      .. rst-class:: ansible-option-title

      **dataoffset**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dataoffset" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP payload.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dbprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-dbprofilename:

      .. rst-class:: ansible-option-title

      **dbprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dbprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the DB profile whose settings are to be applied to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dbslb"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-dbslb:

      .. rst-class:: ansible-option-title

      **dbslb**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dbslb" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable database specific load balancing for MySQL and MSSQL service types.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disableprimaryondown"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-disableprimaryondown:

      .. rst-class:: ansible-option-title

      **disableprimaryondown**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disableprimaryondown" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If the primary virtual server goes down, do not allow it to return to primary status until manually enabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dns64"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-dns64:

      .. rst-class:: ansible-option-title

      **dns64**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dns64" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This argument is for enabling/disabling the dns64 on lbvserver


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnsprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-dnsprofilename:

      .. rst-class:: ansible-option-title

      **dnsprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnsprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-downstateflush"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-downstateflush:

      .. rst-class:: ansible-option-title

      **downstateflush**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-downstateflush" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hashlength"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-hashlength:

      .. rst-class:: ansible-option-title

      **hashlength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hashlength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing methods.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`80`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-healththreshold"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-healththreshold:

      .. rst-class:: ansible-option-title

      **healththreshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-healththreshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Threshold in percent of active services below which vserver state is made down. If this threshold is 0, vserver state will be up even if one bound service is up.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httpprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-httpprofilename:

      .. rst-class:: ansible-option-title

      **httpprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-httpprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the HTTP profile whose settings are to be applied to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httpsredirecturl"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-httpsredirecturl:

      .. rst-class:: ansible-option-title

      **httpsredirecturl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-httpsredirecturl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL to which all HTTP traffic received on the port specified in the -redirectFromPort parameter is redirected.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icmpvsrresponse"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-icmpvsrresponse:

      .. rst-class:: ansible-option-title

      **icmpvsrresponse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icmpvsrresponse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      How the Citrix ADC responds to ping requests received for an IP address that is common to one or more virtual servers. Available settings function as follows:

      \* If set to \ :literal:`PASSIVE`\  on all the virtual servers that share the IP address, the appliance always responds to the ping requests.

      \* If set to \ :literal:`ACTIVE`\  on all the virtual servers that share the IP address, the appliance responds to the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not respond.

      \* If set to \ :literal:`ACTIVE`\  on some virtual servers and \ :literal:`PASSIVE`\  on the others, the appliance responds if at least one virtual server with the \ :literal:`ACTIVE`\  setting is UP. Otherwise, the appliance does not respond.

      Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip command in the CLI or the Create IP dialog box in the GUI.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"PASSIVE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ACTIVE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-insertvserveripport"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-insertvserveripport:

      .. rst-class:: ansible-option-title

      **insertvserveripport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-insertvserveripport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Insert an HTTP header, whose value is the IP address and port number of the virtual server, before forwarding a request to the server. The format of the header is \<vipHeader\>: \<virtual server IP address\>\_\<port number \>, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter determines which IP address is inserted in the header, as follows:

      \* VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.

      \* V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a mapped IPv4 address is not configured, insert the IPv6 address.

      \* OFF - Disable header insertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"VIPADDR"`
      - :ansible-option-choices-entry:`"V6TOV4MAPPING"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-instance_name:

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
        <div class="ansibleOptionAnchor" id="parameter-ipmask"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-ipmask:

      .. rst-class:: ansible-option-title

      **ipmask**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipmask" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ippattern"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-ippattern:

      .. rst-class:: ansible-option-title

      **ippattern**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ippattern" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern.  Mutually exclusive with the IP Address parameter. 

      For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254.  You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).

      If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2 have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipset"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-ipset:

      .. rst-class:: ansible-option-title

      **ipset**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipset" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current lb vserver


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipv46"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-ipv46:

      .. rst-class:: ansible-option-title

      **ipv46**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ipv46" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IPv4 or IPv6 address to assign to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-is_cloud:

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
        <div class="ansibleOptionAnchor" id="parameter-l2conn"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-l2conn:

      .. rst-class:: ansible-option-title

      **l2conn**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-l2conn" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (\<source IP\>:\<source port\>::\<destination IP\>:\<destination port\>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the Citrix ADC.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbmethod"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbmethod:

      .. rst-class:: ansible-option-title

      **lbmethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbmethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Load balancing method.  The available settings function as follows:

      \* \ :literal:`ROUNDROBIN`\  - Distribute requests in rotation, regardless of the load. Weights can be assigned to services to enforce weighted round robin distribution.

      \* \ :literal:`LEASTCONNECTION`\  (default) - Select the service with the fewest connections. 

      \* \ :literal:`LEASTRESPONSETIME`\  - Select the service with the lowest average response time. 

      \* \ :literal:`LEASTBANDWIDTH`\  - Select the service currently handling the least traffic.

      \* \ :literal:`LEASTPACKETS`\  - Select the service currently serving the lowest number of packets per second.

      \* \ :literal:`CUSTOMLOAD`\  - Base service selection on the SNMP metrics obtained by custom load monitors.

      \* \ :literal:`LRTM`\  - Select the service with the lowest response time. Response times are learned through monitoring probes. This method also takes the number of active connections into account.

      Also available are a number of hashing methods, in which the appliance extracts a predetermined portion of the request, creates a hash of the portion, and then checks whether any previous requests had the same hash value. If it finds a match, it forwards the request to the service that served those previous requests. Following are the hashing methods: 

      \* \ :literal:`URLHASH`\  - Create a hash of the request URL (or part of the URL).

      \* \ :literal:`DOMAINHASH`\  - Create a hash of the domain name in the request (or part of the domain name). The domain name is taken from either the URL or the Host header. If the domain name appears in both locations, the URL is preferred. If the request does not contain a domain name, the load balancing method defaults to \ :literal:`LEASTCONNECTION`\ .

      \* \ :literal:`DESTINATIONIPHASH`\  - Create a hash of the destination IP address in the IP header. 

      \* \ :literal:`SOURCEIPHASH`\  - Create a hash of the source IP address in the IP header.  

      \* \ :literal:`TOKEN`\  - Extract a token from the request, create a hash of the token, and then select the service to which any previous requests with the same token hash value were sent. 

      \* \ :literal:`SRCIPDESTIPHASH`\  - Create a hash of the string obtained by concatenating the source IP address and destination IP address in the IP header.  

      \* \ :literal:`SRCIPSRCPORTHASH`\  - Create a hash of the source IP address and source port in the IP header.  

      \* \ :literal:`CALLIDHASH`\  - Create a hash of the SIP Call-ID header.

      \* \ :literal:`USER\_TOKEN`\  - Same as \ :literal:`TOKEN`\  LB method but token needs to be provided from an extension.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ROUNDROBIN"`
      - :ansible-option-choices-entry-default:`"LEASTCONNECTION"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"LEASTRESPONSETIME"`
      - :ansible-option-choices-entry:`"URLHASH"`
      - :ansible-option-choices-entry:`"DOMAINHASH"`
      - :ansible-option-choices-entry:`"DESTINATIONIPHASH"`
      - :ansible-option-choices-entry:`"SOURCEIPHASH"`
      - :ansible-option-choices-entry:`"SRCIPDESTIPHASH"`
      - :ansible-option-choices-entry:`"LEASTBANDWIDTH"`
      - :ansible-option-choices-entry:`"LEASTPACKETS"`
      - :ansible-option-choices-entry:`"TOKEN"`
      - :ansible-option-choices-entry:`"SRCIPSRCPORTHASH"`
      - :ansible-option-choices-entry:`"LRTM"`
      - :ansible-option-choices-entry:`"CALLIDHASH"`
      - :ansible-option-choices-entry:`"CUSTOMLOAD"`
      - :ansible-option-choices-entry:`"LEASTREQUEST"`
      - :ansible-option-choices-entry:`"AUDITLOGHASH"`
      - :ansible-option-choices-entry:`"STATICPROXIMITY"`
      - :ansible-option-choices-entry:`"USER\_TOKEN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbprofilename:

      .. rst-class:: ansible-option-title

      **lbprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the LB profile which is associated to the vserver


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_analyticsprofile_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_analyticsprofile_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_analyticsprofile_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_analyticsprofile_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_analyticsprofile\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_analyticsprofile_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_analyticsprofile_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_analyticsprofile_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_analyticsprofile_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_analyticsprofile_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_analyticsprofile_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appflowpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appflowpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_appflowpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appflowpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_appflowpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appflowpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appflowpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appflowpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appflowpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appflowpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appflowpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appfwpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appfwpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_appfwpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appfwpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_appfwpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appfwpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appfwpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appfwpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appfwpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appfwpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appfwpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appqoepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appqoepolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_appqoepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appqoepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_appqoepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appqoepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appqoepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appqoepolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_appqoepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_appqoepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_appqoepolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditnslogpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditnslogpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_auditnslogpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditnslogpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_auditnslogpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditnslogpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditnslogpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditnslogpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditnslogpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditnslogpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditnslogpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditsyslogpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditsyslogpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_auditsyslogpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditsyslogpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_auditsyslogpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditsyslogpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditsyslogpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditsyslogpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_auditsyslogpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_auditsyslogpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_auditsyslogpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_authorizationpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_authorizationpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_authorizationpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_authorizationpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_authorizationpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_authorizationpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_authorizationpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_authorizationpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_authorizationpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_authorizationpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_authorizationpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_botpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_botpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_botpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_botpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_botpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_botpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_botpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_botpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_botpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_botpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_botpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cachepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cachepolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_cachepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cachepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_cachepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cachepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cachepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cachepolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cachepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cachepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cachepolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cmppolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cmppolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_cmppolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cmppolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_cmppolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cmppolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cmppolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cmppolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_cmppolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_cmppolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_cmppolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_contentinspectionpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_contentinspectionpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_contentinspectionpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_contentinspectionpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_contentinspectionpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_contentinspectionpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_contentinspectionpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_contentinspectionpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_contentinspectionpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_contentinspectionpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_contentinspectionpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_dnspolicy64_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_dnspolicy64_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_dnspolicy64_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_dnspolicy64_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_dnspolicy64\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_dnspolicy64_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_dnspolicy64_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_dnspolicy64_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_dnspolicy64_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_dnspolicy64_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_dnspolicy64_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_feopolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_feopolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_feopolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_feopolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_feopolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_feopolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_feopolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_feopolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_feopolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_feopolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_feopolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_lbpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_lbpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_lbpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_lbpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_lbpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_lbpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_lbpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_lbpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_lbpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_lbpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_lbpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_responderpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_responderpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_responderpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_responderpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_responderpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_responderpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_responderpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_responderpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_responderpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_responderpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_responderpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_rewritepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_rewritepolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_rewritepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_rewritepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_rewritepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_rewritepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_rewritepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_rewritepolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_rewritepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_rewritepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_rewritepolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_service_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_service_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_service_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_service_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_service\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_service_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_service_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_service_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_service_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_service_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_service_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_servicegroup_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_servicegroup_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_servicegroup_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_servicegroup_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_servicegroup\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_servicegroup_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_servicegroup_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_servicegroup_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_servicegroup_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_servicegroup_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_servicegroup_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_spilloverpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_spilloverpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_spilloverpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_spilloverpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_spilloverpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_spilloverpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_spilloverpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_spilloverpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_spilloverpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_spilloverpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_spilloverpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_tmtrafficpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_tmtrafficpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_tmtrafficpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_tmtrafficpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_tmtrafficpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_tmtrafficpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_tmtrafficpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_tmtrafficpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_tmtrafficpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_tmtrafficpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_tmtrafficpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_transformpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_transformpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_transformpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_transformpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_transformpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_transformpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_transformpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_transformpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_transformpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_transformpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_transformpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationdetectionpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationdetectionpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_videooptimizationdetectionpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationdetectionpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_videooptimizationdetectionpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationdetectionpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationdetectionpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationdetectionpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationdetectionpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationdetectionpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationdetectionpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationpacingpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationpacingpolicy_binding:

      .. rst-class:: ansible-option-title

      **lbvserver_videooptimizationpacingpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationpacingpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for lbvserver\_videooptimizationpacingpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationpacingpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationpacingpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationpacingpolicy_binding/binding_members" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of binding members


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-lbvserver_videooptimizationpacingpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-lbvserver_videooptimizationpacingpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-lbvserver_videooptimizationpacingpolicy_binding/mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mode in which to configure the bindings.

      If mode is set to \ :literal:`desired`\ , the bindings will be added or removed from the target NetScaler ADCs as necessary to match the bindings specified in the state.

      If mode is set to \ :literal:`bind`\ , the specified bindings will be added to the resource. The existing bindings in the target ADCs will not be modified.

      If mode is set to \ :literal:`unbind`\ , the specified bindings will be removed from the resource. The existing bindings in the target ADCs will not be modified.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"desired"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"bind"`
      - :ansible-option-choices-entry:`"unbind"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-listenpolicy"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-listenpolicy:

      .. rst-class:: ansible-option-title

      **listenpolicy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-listenpolicy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression identifying traffic accepted by the virtual server. Can be either an expression (for example, CLIENT.IP.DST.IN\_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the virtual server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"NONE\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-listenpriority"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-listenpriority:

      .. rst-class:: ansible-option-title

      **listenpriority**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-listenpriority" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`101`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-m"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-m:

      .. rst-class:: ansible-option-title

      **m**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-m" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Redirection mode for load balancing. Available settings function as follows:

      \* \ :literal:`IP`\  - Before forwarding a request to a server, change the destination \ :literal:`IP`\  address to the server's \ :literal:`IP`\  address. 

      \* \ :literal:`MAC`\  - Before forwarding a request to a server, change the destination \ :literal:`MAC`\  address to the server's \ :literal:`MAC`\  address.  The destination \ :literal:`IP`\  address is not changed. \ :literal:`MAC`\ -based redirection mode is used mostly in firewall load balancing deployments. 

      \* \ :literal:`IPTUNNEL`\  - Perform \ :literal:`IP`\ -in-\ :literal:`IP`\  encapsulation for client \ :literal:`IP`\  packets. In the outer \ :literal:`IP`\  headers, set the destination \ :literal:`IP`\  address to the \ :literal:`IP`\  address of the server and the source \ :literal:`IP`\  address to the subnet \ :literal:`IP`\  (SNIP). The client \ :literal:`IP`\  packets are not modified. Applicable to both IPv4 and IPv6 packets. 

      \* \ :literal:`TOS`\  - Encode the virtual server's \ :literal:`TOS`\  ID in the \ :literal:`TOS`\  field of the \ :literal:`IP`\  header. 

      You can use either the \ :literal:`IPTUNNEL`\  or the \ :literal:`TOS`\  option to implement Direct Server Return (DSR).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"IP"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"MAC"`
      - :ansible-option-choices-entry:`"IPTUNNEL"`
      - :ansible-option-choices-entry:`"TOS"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macmoderetainvlan"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-macmoderetainvlan:

      .. rst-class:: ansible-option-title

      **macmoderetainvlan**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-macmoderetainvlan" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option is used to retain vlan information of incoming packet when macmode is enabled


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mas_proxy_call:

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
        <div class="ansibleOptionAnchor" id="parameter-maxautoscalemembers"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-maxautoscalemembers:

      .. rst-class:: ansible-option-title

      **maxautoscalemembers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maxautoscalemembers" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum number of members expected to be present when vserver is used in Autoscale.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-minautoscalemembers"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-minautoscalemembers:

      .. rst-class:: ansible-option-title

      **minautoscalemembers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-minautoscalemembers" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Minimum number of members expected to be present when vserver is used in Autoscale.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mssqlserverversion"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mssqlserverversion:

      .. rst-class:: ansible-option-title

      **mssqlserverversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mssqlserverversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this parameter if you expect some clients to run a version different from the version of the database. This setting provides compatibility between the client-side and server-side connections by ensuring that all communication conforms to the server's version.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"70"`
      - :ansible-option-choices-entry:`"2000"`
      - :ansible-option-choices-entry:`"2000SP1"`
      - :ansible-option-choices-entry:`"2005"`
      - :ansible-option-choices-entry:`"2008"`
      - :ansible-option-choices-entry-default:`"2008R2"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"2012"`
      - :ansible-option-choices-entry:`"2014"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mysqlcharacterset"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mysqlcharacterset:

      .. rst-class:: ansible-option-title

      **mysqlcharacterset**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mysqlcharacterset" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Character set that the virtual server advertises to clients.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mysqlprotocolversion"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mysqlprotocolversion:

      .. rst-class:: ansible-option-title

      **mysqlprotocolversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mysqlprotocolversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      MySQL protocol version that the virtual server advertises to clients.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mysqlservercapabilities"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mysqlservercapabilities:

      .. rst-class:: ansible-option-title

      **mysqlservercapabilities**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mysqlservercapabilities" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Server capabilities that the virtual server advertises to clients.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mysqlserverversion"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-mysqlserverversion:

      .. rst-class:: ansible-option-title

      **mysqlserverversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mysqlserverversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      MySQL server version string that the virtual server advertises to clients.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.

      

      CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netmask"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-netmask:

      .. rst-class:: ansible-option-title

      **netmask**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-netmask" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing method is DESTINATIONIPHASH or SOURCEIPHASH.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netprofile"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-netprofile:

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

      Name of the network profile to associate with the virtual server. If you set this parameter, the virtual server uses only the IP addresses in the network profile as source IP addresses when initiating connections with servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newname"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-newname:

      .. rst-class:: ansible-option-title

      **newname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-newname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      New name for the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newservicerequest"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-newservicerequest:

      .. rst-class:: ansible-option-title

      **newservicerequest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-newservicerequest" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of requests, or percentage of the load on existing services, by which to increase the load on a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is applicable. A zero value indicates that the global RR startup parameter is applied. Changing the value to zero will cause services currently in slow start to take the full traffic as determined by the LB method. Subsequently, any new services added will use the global RR factor.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newservicerequestincrementinterval"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-newservicerequestincrementinterval:

      .. rst-class:: ansible-option-title

      **newservicerequestincrementinterval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-newservicerequestincrementinterval" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Interval, in seconds, between successive increments in the load on a new service or a service whose state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newservicerequestunit"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-newservicerequestunit:

      .. rst-class:: ansible-option-title

      **newservicerequestunit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-newservicerequestunit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Units in which to increment load at each interval in slow-start mode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"PER\_SECOND"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"PERCENT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-oracleserverversion"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-oracleserverversion:

      .. rst-class:: ansible-option-title

      **oracleserverversion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-oracleserverversion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Oracle server version


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"10G"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"11G"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-order"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-order:

      .. rst-class:: ansible-option-title

      **order**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-order" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Order number to be assigned to the service when it is bound to the lb vserver.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-orderthreshold"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-orderthreshold:

      .. rst-class:: ansible-option-title

      **orderthreshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-orderthreshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option is used to to specify the threshold of minimum number of services to be UP in an order, for it to be considered in Lb decision.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-persistavpno"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-persistavpno:

      .. rst-class:: ansible-option-title

      **persistavpno**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-persistavpno" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Persist AVP number for Diameter Persistency. 

                  In case this AVP is not defined in Base RFC 3588 and it is nested inside a Grouped AVP, 

                  define a sequence of AVP numbers (max 3) in order of parent to child. So say persist AVP number X 

                  is nested inside AVP Y which is nested in Z, then define the list as  Z Y X


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-persistencebackup"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-persistencebackup:

      .. rst-class:: ansible-option-title

      **persistencebackup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-persistencebackup" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SOURCEIP"`
      - :ansible-option-choices-entry:`"NONE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-persistencetype"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-persistencetype:

      .. rst-class:: ansible-option-title

      **persistencetype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-persistencetype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of persistence for the virtual server. Available settings function as follows:

      \* \ :literal:`SOURCEIP`\  - Connections from the same client IP address belong to the same persistence session.

      \* \ :literal:`COOKIEINSERT`\  - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session. 

      \* \ :literal:`SSLSESSION`\  - Connections that have the same SSL Session ID belong to the same persistence session.

      \* \ :literal:`CUSTOMSERVERID`\  - Connections with the same server ID form part of the same session. For this persistence type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter to identify the server ID in a request.

      \* \ :literal:`RULE`\  - All connections that match a user defined rule belong to the same persistence session. 

      \* \ :literal:`URLPASSIVE`\  - Requests that have the same server ID in the URL query belong to the same persistence session. The server ID is the hexadecimal representation of the IP address and port of the service to which the request must be forwarded. This persistence type requires a rule to identify the server ID in the request. 

      \* \ :literal:`DESTIP`\  - Connections to the same destination IP address belong to the same persistence session.

      \* \ :literal:`SRCIPDESTIP`\  - Connections that have the same source IP address and destination IP address belong to the same persistence session.

      \* \ :literal:`CALLID`\  - Connections that have the same CALL-ID SIP header belong to the same persistence session.

      \* \ :literal:`RTSPSID`\  - Connections that have the same RTSP Session ID belong to the same persistence session.

      \* \ :literal:`FIXSESSION`\  - Connections that have the same SenderCompID and TargetCompID values belong to the same persistence session.

      \* \ :literal:`USERSESSION`\  - Persistence session is created based on the persistence parameter value provided from an extension.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SOURCEIP"`
      - :ansible-option-choices-entry:`"COOKIEINSERT"`
      - :ansible-option-choices-entry:`"SSLSESSION"`
      - :ansible-option-choices-entry:`"RULE"`
      - :ansible-option-choices-entry:`"URLPASSIVE"`
      - :ansible-option-choices-entry:`"CUSTOMSERVERID"`
      - :ansible-option-choices-entry:`"DESTIP"`
      - :ansible-option-choices-entry:`"SRCIPDESTIP"`
      - :ansible-option-choices-entry:`"CALLID"`
      - :ansible-option-choices-entry:`"RTSPSID"`
      - :ansible-option-choices-entry:`"DIAMETER"`
      - :ansible-option-choices-entry:`"FIXSESSION"`
      - :ansible-option-choices-entry:`"USERSESSION"`
      - :ansible-option-choices-entry:`"NONE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-persistmask"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-persistmask:

      .. rst-class:: ansible-option-title

      **persistmask**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-persistmask" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Persistence mask for IP based persistence types, for IPv4 virtual servers.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-port"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-port:

      .. rst-class:: ansible-option-title

      **port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number for the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-probeport"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-probeport:

      .. rst-class:: ansible-option-title

      **probeport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-probeport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Citrix ADC provides support for external health check of the vserver status. Select port for HTTP/TCP monitring


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-probeprotocol"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-probeprotocol:

      .. rst-class:: ansible-option-title

      **probeprotocol**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-probeprotocol" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Citrix ADC provides support for external health check of the vserver status. Select \ :literal:`HTTP`\  or \ :literal:`TCP`\  probes for healthcheck


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"TCP"`
      - :ansible-option-choices-entry:`"HTTP"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-probesuccessresponsecode"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-probesuccessresponsecode:

      .. rst-class:: ansible-option-title

      **probesuccessresponsecode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-probesuccessresponsecode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      HTTP code to return in SUCCESS case.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"200 OK\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-processlocal"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-processlocal:

      .. rst-class:: ansible-option-title

      **processlocal**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-processlocal" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-push"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-push:

      .. rst-class:: ansible-option-title

      **push**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-push" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Process traffic with the push virtual server that is bound to this load balancing virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushlabel"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-pushlabel:

      .. rst-class:: ansible-option-title

      **pushlabel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushlabel" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression for extracting a label from the server's response. Can be either an expression or the name of a named expression.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"none\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushmulticlients"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-pushmulticlients:

      .. rst-class:: ansible-option-title

      **pushmulticlients**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushmulticlients" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushvserver"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-pushvserver:

      .. rst-class:: ansible-option-title

      **pushvserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushvserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the load balancing virtual server, of type PUSH or SSL\_PUSH, to which the server pushes updates received on the load balancing virtual server that you are configuring.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quicbridgeprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-quicbridgeprofilename:

      .. rst-class:: ansible-option-title

      **quicbridgeprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quicbridgeprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the QUIC Bridge profile whose settings are to be applied to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quicprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-quicprofilename:

      .. rst-class:: ansible-option-title

      **quicprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quicprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of QUIC profile which will be attached to the VServer.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-range"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-range:

      .. rst-class:: ansible-option-title

      **range**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-range" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual server then functions as a network virtual server, accepting traffic on any of the generated IP addresses. The IP addresses are generated automatically, as follows: 

      \* For a range of n, the last octet of the address specified by the IP Address parameter increments n-1 times. 

      \* If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.

      Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name parameters to specify the range. For example:

      add lb vserver my\_vserver[1-3] HTTP 192.0.2.[1-3] 80


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recursionavailable"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-recursionavailable:

      .. rst-class:: ansible-option-title

      **recursionavailable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recursionavailable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport recursive queries.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirectfromport"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-redirectfromport:

      .. rst-class:: ansible-option-title

      **redirectfromport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirectfromport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number for the virtual server, from which we absorb the traffic for http redirect


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirectportrewrite"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-redirectportrewrite:

      .. rst-class:: ansible-option-title

      **redirectportrewrite**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirectportrewrite" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rewrite the port and change the protocol to ensure successful HTTP redirects from services.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirurl"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-redirurl:

      .. rst-class:: ansible-option-title

      **redirurl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirurl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL to which to redirect traffic if the virtual server becomes unavailable. 

      WARNING! Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirurlflags"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-redirurlflags:

      .. rst-class:: ansible-option-title

      **redirurlflags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirurlflags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The redirect URL to be unset.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-resrule"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-resrule:

      .. rst-class:: ansible-option-title

      **resrule**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-resrule" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression specifying which part of a server's response to use for creating rule based persistence sessions (persistence type RULE). Can be either an expression or the name of a named expression.

      Example:

      HTTP.RES.HEADER("setcookie").VALUE(0).TYPECAST\_NVLIST\_T('=',';').VALUE("server1").


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"none\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-retainconnectionsoncluster"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-retainconnectionsoncluster:

      .. rst-class:: ansible-option-title

      **retainconnectionsoncluster**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-retainconnectionsoncluster" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option enables you to retain existing connections on a node joining a Cluster system or when a node is being configured for passive timeout. By default, this option is disabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rhistate"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-rhistate:

      .. rst-class:: ansible-option-title

      **rhistate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rhistate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to VSVR\_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:

      \* If you set RHI STATE to \ :literal:`PASSIVE`\  on all virtual servers, the Citrix ADC always advertises the route for the VIP address.

      \* If you set RHI STATE to \ :literal:`ACTIVE`\  on all virtual servers, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.

      \* If you set RHI STATE to \ :literal:`ACTIVE`\  on some and \ :literal:`PASSIVE`\  on others, the Citrix ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to \ :literal:`ACTIVE`\ , is in UP state.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"PASSIVE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ACTIVE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rtspnat"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-rtspnat:

      .. rst-class:: ansible-option-title

      **rtspnat**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rtspnat" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use network address translation (NAT) for RTSP data connections.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rule"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-rule:

      .. rst-class:: ansible-option-title

      **rule**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rule" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression, or name of a named expression, against which traffic is evaluated.

      The following requirements apply only to the Citrix ADC CLI:

      \* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.

      \* If the expression itself includes double quotation marks, escape the quotations by using the \\ character. 

      \* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"none\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-servicename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-servicename:

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

      Service to bind to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-servicetype"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-servicetype:

      .. rst-class:: ansible-option-title

      **servicetype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-servicetype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Protocol used by the service (also called the service type).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"HTTP"`
      - :ansible-option-choices-entry:`"FTP"`
      - :ansible-option-choices-entry:`"TCP"`
      - :ansible-option-choices-entry:`"UDP"`
      - :ansible-option-choices-entry:`"SSL"`
      - :ansible-option-choices-entry:`"SSL\_BRIDGE"`
      - :ansible-option-choices-entry:`"SSL\_TCP"`
      - :ansible-option-choices-entry:`"DTLS"`
      - :ansible-option-choices-entry:`"NNTP"`
      - :ansible-option-choices-entry:`"DNS"`
      - :ansible-option-choices-entry:`"DHCPRA"`
      - :ansible-option-choices-entry:`"ANY"`
      - :ansible-option-choices-entry:`"SIP\_UDP"`
      - :ansible-option-choices-entry:`"SIP\_TCP"`
      - :ansible-option-choices-entry:`"SIP\_SSL"`
      - :ansible-option-choices-entry:`"DNS\_TCP"`
      - :ansible-option-choices-entry:`"RTSP"`
      - :ansible-option-choices-entry:`"PUSH"`
      - :ansible-option-choices-entry:`"SSL\_PUSH"`
      - :ansible-option-choices-entry:`"RADIUS"`
      - :ansible-option-choices-entry:`"RDP"`
      - :ansible-option-choices-entry:`"MYSQL"`
      - :ansible-option-choices-entry:`"MSSQL"`
      - :ansible-option-choices-entry:`"DIAMETER"`
      - :ansible-option-choices-entry:`"SSL\_DIAMETER"`
      - :ansible-option-choices-entry:`"TFTP"`
      - :ansible-option-choices-entry:`"ORACLE"`
      - :ansible-option-choices-entry:`"SMPP"`
      - :ansible-option-choices-entry:`"SYSLOGTCP"`
      - :ansible-option-choices-entry:`"SYSLOGUDP"`
      - :ansible-option-choices-entry:`"FIX"`
      - :ansible-option-choices-entry:`"SSL\_FIX"`
      - :ansible-option-choices-entry:`"PROXY"`
      - :ansible-option-choices-entry:`"USER\_TCP"`
      - :ansible-option-choices-entry:`"USER\_SSL\_TCP"`
      - :ansible-option-choices-entry:`"QUIC"`
      - :ansible-option-choices-entry:`"IPFIX"`
      - :ansible-option-choices-entry:`"LOGSTREAM"`
      - :ansible-option-choices-entry:`"MONGO"`
      - :ansible-option-choices-entry:`"MONGO\_TLS"`
      - :ansible-option-choices-entry:`"MQTT"`
      - :ansible-option-choices-entry:`"MQTT\_TLS"`
      - :ansible-option-choices-entry:`"QUIC\_BRIDGE"`
      - :ansible-option-choices-entry:`"HTTP\_QUIC"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionless"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-sessionless:

      .. rst-class:: ansible-option-title

      **sessionless**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionless" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load balancing of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where session information is unnecessary.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-skippersistency"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-skippersistency:

      .. rst-class:: ansible-option-title

      **skippersistency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-skippersistency" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This argument decides the behavior incase the service which is selected from an existing persistence session has reached threshold.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Bypass"`
      - :ansible-option-choices-entry:`"ReLb"`
      - :ansible-option-choices-entry-default:`"None"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sobackupaction"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-sobackupaction:

      .. rst-class:: ansible-option-title

      **sobackupaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sobackupaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"DROP"`
      - :ansible-option-choices-entry:`"ACCEPT"`
      - :ansible-option-choices-entry:`"REDIRECT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-somethod"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-somethod:

      .. rst-class:: ansible-option-title

      **somethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-somethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:

      \* \ :literal:`CONNECTION`\  - Spillover occurs when the number of client connections exceeds the threshold.

      \* \ :literal:`DYNAMICCONNECTION`\  - Spillover occurs when the number of client connections at the virtual server exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of bound services.

      \* \ :literal:`BANDWIDTH`\  - Spillover occurs when the bandwidth consumed by the virtual server's incoming and outgoing traffic exceeds the threshold. 

      \* \ :literal:`HEALTH`\  - Spillover occurs when the percentage of weights of the services that are UP drops below the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 transition to DOWN. 

      \* \ :literal:`NONE`\  - Spillover does not occur.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CONNECTION"`
      - :ansible-option-choices-entry:`"DYNAMICCONNECTION"`
      - :ansible-option-choices-entry:`"BANDWIDTH"`
      - :ansible-option-choices-entry:`"HEALTH"`
      - :ansible-option-choices-entry:`"NONE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sopersistence"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-sopersistence:

      .. rst-class:: ansible-option-title

      **sopersistence**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sopersistence" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If spillover occurs, maintain source IP address based persistence for both primary and backup virtual servers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sopersistencetimeout"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-sopersistencetimeout:

      .. rst-class:: ansible-option-title

      **sopersistencetimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sopersistencetimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Timeout for spillover persistence, in minutes.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sothreshold"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-sothreshold:

      .. rst-class:: ansible-option-title

      **sothreshold**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sothreshold" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-state:

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

      State of the load balancing virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tcpprobeport"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-tcpprobeport:

      .. rst-class:: ansible-option-title

      **tcpprobeport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tcpprobeport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number for external TCP probe. NetScaler provides support for external TCP health check of the vserver status over the selected port. This option is only supported for vservers assigned with an IPAddress or ipset.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tcpprofilename"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-tcpprofilename:

      .. rst-class:: ansible-option-title

      **tcpprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tcpprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the TCP profile whose settings are to be applied to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-td"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-td:

      .. rst-class:: ansible-option-title

      **td**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-td" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-timeout"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-timeout:

      .. rst-class:: ansible-option-title

      **timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time period for which a persistence session is in effect.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-toggleorder"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-toggleorder:

      .. rst-class:: ansible-option-title

      **toggleorder**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-toggleorder" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configure this option to toggle order preference


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ASCENDING"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DESCENDING"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tosid"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-tosid:

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

      TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trofspersistence"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-trofspersistence:

      .. rst-class:: ansible-option-title

      **trofspersistence**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trofspersistence" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When value is \ :literal:`ENABLED`\ , Trofs persistence is honored. When value is \ :literal:`DISABLED`\ , Trofs persistence is not honored.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-v6netmasklen"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-v6netmasklen:

      .. rst-class:: ansible-option-title

      **v6netmasklen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-v6netmasklen" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is required by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`128`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-v6persistmasklen"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-v6persistmasklen:

      .. rst-class:: ansible-option-title

      **v6persistmasklen**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-v6persistmasklen" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Persistence mask for IP based persistence types, for IPv6 virtual servers.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`128`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-validate_certs:

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
        <div class="ansibleOptionAnchor" id="parameter-vipheader"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-vipheader:

      .. rst-class:: ansible-option-title

      **vipheader**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-vipheader" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name for the inserted header. The default name is vip-header.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-weight"></div>

      .. _ansible_collections.netscaler.adc.lbvserver_module__parameter-weight:

      .. rst-class:: ansible-option-title

      **weight**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-weight" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Weight to assign to the specified service.


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

      .. _ansible_collections.netscaler.adc.lbvserver_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.lbvserver_module__return-loglines:

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

