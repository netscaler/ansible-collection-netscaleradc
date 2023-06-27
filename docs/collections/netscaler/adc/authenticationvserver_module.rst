
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

.. _ansible_collections.netscaler.adc.authenticationvserver_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.authenticationvserver module -- Configuration for authentication virtual server resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.authenticationvserver`.

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

- Configuration for authentication virtual server resource.


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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-api_path:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-appflowlog:

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

      Log AppFlow flow information.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authentication"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authentication:

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

      Require users to be authenticated before sending traffic through this virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationdomain"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationdomain:

      .. rst-class:: ansible-option-title

      **authenticationdomain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationdomain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The domain of the authentication cookie set by Authentication vserver


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditnslogpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditnslogpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_auditnslogpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditnslogpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_auditnslogpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditnslogpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditnslogpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditnslogpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditnslogpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditnslogpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditnslogpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditsyslogpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditsyslogpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_auditsyslogpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditsyslogpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_auditsyslogpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditsyslogpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditsyslogpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditsyslogpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_auditsyslogpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_auditsyslogpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_auditsyslogpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationcertpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationcertpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationcertpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationcertpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationcertpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationcertpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationcertpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationcertpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationcertpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationcertpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationcertpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationldappolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationldappolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationldappolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationldappolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationldappolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationldappolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationldappolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationldappolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationldappolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationldappolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationldappolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationlocalpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationlocalpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationlocalpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationlocalpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationlocalpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationlocalpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationlocalpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationlocalpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationlocalpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationlocalpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationlocalpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationloginschemapolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationloginschemapolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationloginschemapolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationloginschemapolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationloginschemapolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationloginschemapolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationloginschemapolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationloginschemapolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationloginschemapolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationloginschemapolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationloginschemapolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationnegotiatepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationnegotiatepolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationnegotiatepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationnegotiatepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationnegotiatepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationnegotiatepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationnegotiatepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationnegotiatepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationnegotiatepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationnegotiatepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationnegotiatepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationoauthidppolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationoauthidppolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationoauthidppolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationoauthidppolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationoauthidppolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationoauthidppolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationoauthidppolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationoauthidppolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationoauthidppolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationoauthidppolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationoauthidppolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationradiuspolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationradiuspolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationradiuspolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationradiuspolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationradiuspolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationradiuspolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationradiuspolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationradiuspolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationradiuspolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationradiuspolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationradiuspolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlidppolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlidppolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationsamlidppolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlidppolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationsamlidppolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlidppolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlidppolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlidppolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlidppolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlidppolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlidppolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationsamlpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationsamlpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsamlpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsamlpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsamlpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsmartaccesspolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsmartaccesspolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationsmartaccesspolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsmartaccesspolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationsmartaccesspolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationsmartaccesspolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationtacacspolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationtacacspolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationtacacspolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationtacacspolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationtacacspolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationtacacspolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationtacacspolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationtacacspolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationtacacspolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationtacacspolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationtacacspolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationwebauthpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationwebauthpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_authenticationwebauthpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationwebauthpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_authenticationwebauthpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationwebauthpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationwebauthpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationwebauthpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_authenticationwebauthpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_authenticationwebauthpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_authenticationwebauthpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cachepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cachepolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_cachepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cachepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_cachepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cachepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cachepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cachepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cachepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cachepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cachepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cspolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cspolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_cspolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cspolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_cspolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cspolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cspolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cspolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_cspolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_cspolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_cspolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_responderpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_responderpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_responderpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_responderpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_responderpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_responderpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_responderpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_responderpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_responderpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_responderpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_responderpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_rewritepolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_rewritepolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_rewritepolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_rewritepolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_rewritepolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_rewritepolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_rewritepolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_rewritepolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_rewritepolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_rewritepolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_rewritepolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_tmsessionpolicy_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_tmsessionpolicy_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_tmsessionpolicy_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_tmsessionpolicy_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_tmsessionpolicy\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_tmsessionpolicy_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_tmsessionpolicy_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_tmsessionpolicy_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_tmsessionpolicy_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_tmsessionpolicy_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_tmsessionpolicy_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_vpnportaltheme_binding"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_vpnportaltheme_binding:

      .. rst-class:: ansible-option-title

      **authenticationvserver_vpnportaltheme_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_vpnportaltheme_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for authenticationvserver\_vpnportaltheme\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_vpnportaltheme_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_vpnportaltheme_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_vpnportaltheme_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-authenticationvserver_vpnportaltheme_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-authenticationvserver_vpnportaltheme_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authenticationvserver_vpnportaltheme_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-certkeynames"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-certkeynames:

      .. rst-class:: ansible-option-title

      **certkeynames**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-certkeynames" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the certificate key that was bound to the corresponding SSL virtual server as the Certificate Authority for the device certificate


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-comment"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-comment:

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

      Any comments associated with this virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-failedlogintimeout"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-failedlogintimeout:

      .. rst-class:: ansible-option-title

      **failedlogintimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-failedlogintimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of minutes an account will be locked if user exceeds maximum permissible attempts


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-instance_name:

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
        <div class="ansibleOptionAnchor" id="parameter-ipv46"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-ipv46:

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

      IP address of the authentication virtual server, if a single IP address is assigned to the virtual server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-is_cloud:

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
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-mas_proxy_call:

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
        <div class="ansibleOptionAnchor" id="parameter-maxloginattempts"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-maxloginattempts:

      .. rst-class:: ansible-option-title

      **maxloginattempts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maxloginattempts" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum Number of login Attempts


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-name:

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

      Name for the new authentication virtual server. 

      Must begin with a letter, number, or the underscore character (\_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the authentication virtual server is added by using the rename authentication vserver command.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-newname"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-newname:

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

      New name of the authentication virtual server. 

      Must begin with a letter, number, or the underscore character (\_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, 'my authentication policy' or "my authentication policy").


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-port"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-port:

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

      TCP port on which the virtual server accepts connections.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-range"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-range:

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

      If you are creating a series of virtual servers with a range of IP addresses assigned to them, the length of the range. 

      The new range of authentication virtual servers will have IP addresses consecutively numbered, starting with the primary address specified with the IP Address parameter.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-samesite"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-samesite:

      .. rst-class:: ansible-option-title

      **samesite**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-samesite" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      SameSite attribute value for Cookies generated in AAATM context. This attribute value will be appended only for the cookies which are specified in the builtin patset ns\_cookies\_samesite


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"None"`
      - :ansible-option-choices-entry:`"LAX"`
      - :ansible-option-choices-entry:`"STRICT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-save_config:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-servicetype:

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

      Protocol type of the authentication virtual server. Always \ :literal:`SSL`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"SSL"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-state:

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

      Initial state of the new virtual server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-td"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-td:

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
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__parameter-validate_certs:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.authenticationvserver_module__return-loglines:

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

