
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

.. _ansible_collections.netscaler.adc.crvserver_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.crvserver module -- Configuration for CR virtual server resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.crvserver`.

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

- Configuration for CR virtual server resource.


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
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-api_path:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-appflowlog:

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

      Enable logging of AppFlow information.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-arp"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-arp:

      .. rst-class:: ansible-option-title

      **arp**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-arp" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use ARP to determine the destination MAC address.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-backendssl"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-backendssl:

      .. rst-class:: ansible-option-title

      **backendssl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-backendssl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Decides whether the backend connection made by Citrix ADC to the origin server will be HTTP or SSL. Applicable only for SSL type CR Forward proxy vserver.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-backupvserver"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-backupvserver:

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

      Name of the backup virtual server to which traffic is forwarded if the active server becomes unavailable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-cachetype"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-cachetype:

      .. rst-class:: ansible-option-title

      **cachetype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cachetype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mode of operation for the cache redirection virtual server. Available settings function as follows:

      \* \ :literal:`TRANSPARENT`\  - Intercept all traffic flowing to the appliance and apply cache redirection policies to determine whether content should be served from the cache or from the origin server.

      \* \ :literal:`FORWARD`\  - Resolve the hostname of the incoming request, by using a DNS server, and forward requests for non-cacheable content to the resolved origin servers. Cacheable requests are sent to the configured cache servers.

      \* \ :literal:`REVERSE`\  - Configure reverse proxy caches for specific origin servers. Incoming traffic directed to the reverse proxy can either be served from a cache server or be sent to the origin server with or without modification to the URL.

      The default value for cache type is \ :literal:`TRANSPARENT`\  if service is HTTP or SSL whereas the default cache type is \ :literal:`FORWARD`\  if the service is HDX.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"TRANSPARENT"`
      - :ansible-option-choices-entry:`"REVERSE"`
      - :ansible-option-choices-entry:`"FORWARD"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cachevserver"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-cachevserver:

      .. rst-class:: ansible-option-title

      **cachevserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cachevserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the default cache virtual server to which to redirect requests (the default target of the cache redirection virtual server).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clttimeout"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-clttimeout:

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

      Time-out value, in seconds, after which to terminate an idle client connection.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-comment"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-comment:

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

      Comments associated with this virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_analyticsprofile_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_analyticsprofile_binding:

      .. rst-class:: ansible-option-title

      **crvserver_analyticsprofile_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_analyticsprofile_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_analyticsprofile\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_analyticsprofile_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_analyticsprofile_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_analyticsprofile_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_analyticsprofile_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_analyticsprofile_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_analyticsprofile_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appflowpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appflowpolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_appflowpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appflowpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_appflowpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appflowpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appflowpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appflowpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appflowpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appflowpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appflowpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appfwpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appfwpolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_appfwpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appfwpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_appfwpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appfwpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appfwpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appfwpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appfwpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appfwpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appfwpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appqoepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appqoepolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_appqoepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appqoepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_appqoepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appqoepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appqoepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appqoepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_appqoepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_appqoepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_appqoepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cachepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cachepolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_cachepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cachepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_cachepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cachepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cachepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cachepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cachepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cachepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cachepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cmppolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cmppolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_cmppolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cmppolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_cmppolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cmppolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cmppolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cmppolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cmppolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cmppolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cmppolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_crpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_crpolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_crpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_crpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_crpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_crpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_crpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_crpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_crpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_crpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_crpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cspolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cspolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_cspolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cspolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_cspolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cspolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cspolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cspolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_cspolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_cspolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_cspolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_feopolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_feopolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_feopolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_feopolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_feopolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_feopolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_feopolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_feopolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_feopolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_feopolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_feopolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_icapolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_icapolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_icapolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_icapolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_icapolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_icapolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_icapolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_icapolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_icapolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_icapolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_icapolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_lbvserver_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_lbvserver_binding:

      .. rst-class:: ansible-option-title

      **crvserver_lbvserver_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_lbvserver_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_lbvserver\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_lbvserver_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_lbvserver_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_lbvserver_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_lbvserver_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_lbvserver_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_lbvserver_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_policymap_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_policymap_binding:

      .. rst-class:: ansible-option-title

      **crvserver_policymap_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_policymap_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_policymap\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_policymap_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_policymap_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_policymap_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_policymap_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_policymap_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_policymap_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_responderpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_responderpolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_responderpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_responderpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_responderpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_responderpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_responderpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_responderpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_responderpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_responderpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_responderpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_rewritepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_rewritepolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_rewritepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_rewritepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_rewritepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_rewritepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_rewritepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_rewritepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_rewritepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_rewritepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_rewritepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_spilloverpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_spilloverpolicy_binding:

      .. rst-class:: ansible-option-title

      **crvserver_spilloverpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_spilloverpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for crvserver\_spilloverpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crvserver_spilloverpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_spilloverpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_spilloverpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-crvserver_spilloverpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-crvserver_spilloverpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crvserver_spilloverpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-destinationvserver"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-destinationvserver:

      .. rst-class:: ansible-option-title

      **destinationvserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-destinationvserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Destination virtual server for a transparent or forward proxy cache redirection virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disableprimaryondown"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-disableprimaryondown:

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

      Continue sending traffic to a backup virtual server even after the primary virtual server comes UP from the DOWN state.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disallowserviceaccess"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-disallowserviceaccess:

      .. rst-class:: ansible-option-title

      **disallowserviceaccess**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disallowserviceaccess" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This is effective when a FORWARD type cr vserver is added. By default, this parameter is \ :literal:`DISABLED`\ . When it is \ :literal:`ENABLED`\ , backend services cannot be accessed through a FORWARD type cr vserver.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnsvservername"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-dnsvservername:

      .. rst-class:: ansible-option-title

      **dnsvservername**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dnsvservername" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the DNS virtual server that resolves domain names arriving at the forward proxy virtual server.

      Note: This parameter applies only to forward proxy virtual servers, not reverse or transparent.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-domain"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-domain:

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

      Default domain for reverse proxies. Domains are configured to direct an incoming request from a specified source domain to a specified target domain. There can be several configured pairs of source and target domains. You can select one pair to be the default. If the host header or URL of an incoming request does not include a source domain, this option sends the request to the specified target domain.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-downstateflush"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-downstateflush:

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

      Perform delayed cleanup of connections to this virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-format"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-format:

      .. rst-class:: ansible-option-title

      **format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      0


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ghost"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-ghost:

      .. rst-class:: ansible-option-title

      **ghost**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ghost" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      0


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httpprofilename"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-httpprofilename:

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

      Name of the profile containing HTTP configuration information for cache redirection virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icmpvsrresponse"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-icmpvsrresponse:

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

      Criterion for responding to PING requests sent to this virtual server. If \ :literal:`ACTIVE`\ , respond only if the virtual server is available. If \ :literal:`PASSIVE`\ , respond even if the virtual server is not available.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"PASSIVE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ACTIVE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-instance_name:

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
        <div class="ansibleOptionAnchor" id="parameter-ipset"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-ipset:

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

      The list of IPv4/IPv6 addresses bound to ipset would form a part of listening service on the current cr vserver


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ipv46"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-ipv46:

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

      IPv4 or IPv6 address of the cache redirection virtual server. Usually a public IP address. Clients send connection requests to this IP address.

      Note: For a transparent cache redirection virtual server, use an asterisk (\*) to specify a wildcard virtual server address.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-is_cloud:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-l2conn:

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

      Use L2 parameters, such as MAC, VLAN, and channel to identify a connection.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-listenpolicy"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-listenpolicy:

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

      String specifying the listen policy for the cache redirection virtual server. Can be either an in-line expression or the name of a named expression.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"\\"NONE\\""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-listenpriority"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-listenpriority:

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

      Priority of the listen policy specified by the Listen Policy parameter. The lower the number, higher the priority.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`101`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-map"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-map:

      .. rst-class:: ansible-option-title

      **map**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-map" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Obsolete.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-mas_proxy_call:

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
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-name:

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

      Name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the cache redirection virtual server is created.

      The following requirement applies only to the Citrix ADC CLI:  

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my server" or 'my server').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netprofile"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-netprofile:

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

      Name of the network profile containing network configurations for the cache redirection virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newname"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-newname:

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

      New name for the cache redirection virtual server. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my name" or 'my name').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-onpolicymatch"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-onpolicymatch:

      .. rst-class:: ansible-option-title

      **onpolicymatch**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-onpolicymatch" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Redirect requests that match the policy to either the cache or the origin server, as specified.

      Note: For this option to work, you must set the cache redirection type to POLICY.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CACHE"`
      - :ansible-option-choices-entry-default:`"ORIGIN"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-originusip"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-originusip:

      .. rst-class:: ansible-option-title

      **originusip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-originusip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use the client's IP address as the source IP address in requests sent to the origin server.  

      Note: You can enable this parameter to implement fully transparent CR deployment.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-port"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-port:

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

      Port number of the virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`80`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-precedence"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-precedence:

      .. rst-class:: ansible-option-title

      **precedence**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-precedence" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of policy (\ :literal:`URL`\  or \ :literal:`RULE`\ ) that takes precedence on the cache redirection virtual server. Applies only to cache redirection virtual servers that have both \ :literal:`URL`\  and \ :literal:`RULE`\  based policies. If you specify \ :literal:`URL`\ , \ :literal:`URL`\  based policies are applied first, in the following order:

      1.   Domain and exact \ :literal:`URL`\ 

      2.   Domain, prefix and suffix

      3.   Domain and suffix

      4.   Domain and prefix

      5.   Domain only

      6.   Exact \ :literal:`URL`\ 

      7.   Prefix and suffix

      8.   Suffix only

      9.   Prefix only

      10.  Default

      If you specify \ :literal:`RULE`\ , the rule based policies are applied before \ :literal:`URL`\  based policies are applied.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"RULE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"URL"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-probeport"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-probeport:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-probeprotocol:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-probesuccessresponsecode:

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
        <div class="ansibleOptionAnchor" id="parameter-range"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-range:

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

      Number of consecutive IP addresses, starting with the address specified by the IPAddress parameter, to include in a range of addresses assigned to this virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirect"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-redirect:

      .. rst-class:: ansible-option-title

      **redirect**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirect" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of cache server to which to redirect HTTP requests. Available settings function as follows:

      \* \ :literal:`CACHE`\  - Direct all requests to the cache.

      \* \ :literal:`POLICY`\  - Apply the cache redirection policy to determine whether the request should be directed to the cache or to the origin.

      \* \ :literal:`ORIGIN`\  - Direct all requests to the origin server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CACHE"`
      - :ansible-option-choices-entry-default:`"POLICY"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ORIGIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirecturl"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-redirecturl:

      .. rst-class:: ansible-option-title

      **redirecturl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-redirecturl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL of the server to which to redirect traffic if the cache redirection virtual server configured on the Citrix ADC becomes unavailable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reuse"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-reuse:

      .. rst-class:: ansible-option-title

      **reuse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reuse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reuse TCP connections to the origin server across client connections. Do not set this parameter unless the Service Type parameter is set to HTTP. If you set this parameter to OFF, the possible settings of the Redirect parameter function as follows:

      \* CACHE - TCP connections to the cache servers are not reused.

      \* ORIGIN - TCP connections to the origin servers are not reused. 

      \* POLICY - TCP connections to the origin servers are not reused.

      If you set the Reuse parameter to ON, connections to origin servers and connections to cache servers are reused.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rhistate"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-rhistate:

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

      A host route is injected according to the setting on the virtual servers

                  \* If set to \ :literal:`PASSIVE`\  on all the virtual servers that share the IP address, the appliance always injects the hostroute.

                  \* If set to \ :literal:`ACTIVE`\  on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.

                  \* If set to \ :literal:`ACTIVE`\  on some virtual servers and \ :literal:`PASSIVE`\  on the others, the appliance, injects even if one virtual server set to \ :literal:`ACTIVE`\  is UP.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"PASSIVE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ACTIVE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-servicetype"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-servicetype:

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

      Protocol (type of service) handled by the virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"HTTP"`
      - :ansible-option-choices-entry:`"SSL"`
      - :ansible-option-choices-entry:`"NNTP"`
      - :ansible-option-choices-entry:`"HDX"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sopersistencetimeout"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-sopersistencetimeout:

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

      Time-out, in minutes, for spillover persistence.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sothreshold"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-sothreshold:

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

      For CONNECTION (or) DYNAMICCONNECTION spillover, the number of connections above which the virtual server enters spillover mode. For BANDWIDTH spillover, the amount of incoming and outgoing traffic (in Kbps) before spillover. For HEALTH spillover, the percentage of active services (by weight) below which spillover occurs.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-srcipexpr"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-srcipexpr:

      .. rst-class:: ansible-option-title

      **srcipexpr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-srcipexpr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression used to extract the source IP addresses from the requests originating from the cache. Can be either an in-line expression or the name of a named expression.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-state:

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

      Initial state of the cache redirection virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tcpprobeport"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-tcpprobeport:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-tcpprofilename:

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

      Name of the profile containing TCP configuration information for the cache redirection virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-td"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-td:

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
        <div class="ansibleOptionAnchor" id="parameter-useoriginipportforcache"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-useoriginipportforcache:

      .. rst-class:: ansible-option-title

      **useoriginipportforcache**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-useoriginipportforcache" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use origin ip/port while forwarding request to the cache. Change the destination IP, destination port of the request came to CR vserver to Origin IP and Origin Port and forward it to Cache


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-useportrange"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-useportrange:

      .. rst-class:: ansible-option-title

      **useportrange**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-useportrange" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use a port number from the port range (set by using the set ns param command, or in the Create Virtual Server (Cache Redirection) dialog box) as the source port in the requests sent to the origin server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-validate_certs:

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
        <div class="ansibleOptionAnchor" id="parameter-via"></div>

      .. _ansible_collections.netscaler.adc.crvserver_module__parameter-via:

      .. rst-class:: ansible-option-title

      **via**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-via" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Insert a via header in each HTTP request. In the case of a cache miss, the request is redirected from the cache server to the origin server. This header indicates whether the request is being sent from a cache server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


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

      .. _ansible_collections.netscaler.adc.crvserver_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.crvserver_module__return-loglines:

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

