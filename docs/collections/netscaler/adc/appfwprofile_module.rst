
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

.. _ansible_collections.netscaler.adc.appfwprofile_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.appfwprofile module -- Configuration for application firewall profile resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.appfwprofile`.

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

- Configuration for application firewall profile resource.


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
        <div class="ansibleOptionAnchor" id="parameter-addcookieflags"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-addcookieflags:

      .. rst-class:: ansible-option-title

      **addcookieflags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-addcookieflags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Add the specified flags to cookies. Available settings function as follows:

      \* None - Do not add flags to cookies.

      \* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from accessing cookies.

      \* Secure - Add Secure flag to cookies.

      \* All - Add both HTTPOnly and Secure flags to cookies.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"httpOnly"`
      - :ansible-option-choices-entry:`"secure"`
      - :ansible-option-choices-entry:`"all"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-api_path:

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_appfwconfidfield_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_appfwconfidfield_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_appfwconfidfield_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_appfwconfidfield_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_appfwconfidfield\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_appfwconfidfield_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_appfwconfidfield_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_appfwconfidfield_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_appfwconfidfield_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_appfwconfidfield_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_appfwconfidfield_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_blockkeyword_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_blockkeyword_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_blockkeyword_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_blockkeyword_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_blockkeyword\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_blockkeyword_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_blockkeyword_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_blockkeyword_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_blockkeyword_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_blockkeyword_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_blockkeyword_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_bypasslist_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_bypasslist_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_bypasslist_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_bypasslist_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_bypasslist\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_bypasslist_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_bypasslist_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_bypasslist_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_bypasslist_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_bypasslist_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_bypasslist_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cmdinjection_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cmdinjection_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_cmdinjection_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cmdinjection_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_cmdinjection\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cmdinjection_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cmdinjection_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cmdinjection_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cmdinjection_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cmdinjection_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cmdinjection_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_contenttype_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_contenttype_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_contenttype_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_contenttype_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_contenttype\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_contenttype_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_contenttype_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_contenttype_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_contenttype_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_contenttype_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_contenttype_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cookieconsistency_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cookieconsistency_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_cookieconsistency_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cookieconsistency_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_cookieconsistency\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cookieconsistency_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cookieconsistency_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cookieconsistency_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_cookieconsistency_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_cookieconsistency_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_cookieconsistency_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_creditcardnumber_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_creditcardnumber_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_creditcardnumber_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_creditcardnumber_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_creditcardnumber\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_creditcardnumber_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_creditcardnumber_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_creditcardnumber_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_creditcardnumber_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_creditcardnumber_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_creditcardnumber_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_crosssitescripting_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_crosssitescripting_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_crosssitescripting_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_crosssitescripting_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_crosssitescripting\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_crosssitescripting_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_crosssitescripting_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_crosssitescripting_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_crosssitescripting_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_crosssitescripting_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_crosssitescripting_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_csrftag_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_csrftag_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_csrftag_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_csrftag_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_csrftag\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_csrftag_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_csrftag_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_csrftag_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_csrftag_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_csrftag_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_csrftag_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denylist_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denylist_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_denylist_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denylist_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_denylist\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denylist_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denylist_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denylist_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denylist_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denylist_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denylist_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denyurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denyurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_denyurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denyurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_denyurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denyurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denyurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denyurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_denyurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_denyurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_denyurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_excluderescontenttype_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_excluderescontenttype_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_excluderescontenttype_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_excluderescontenttype_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_excluderescontenttype\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_excluderescontenttype_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_excluderescontenttype_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_excluderescontenttype_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_excluderescontenttype_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_excluderescontenttype_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_excluderescontenttype_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fakeaccount_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fakeaccount_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_fakeaccount_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fakeaccount_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_fakeaccount\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fakeaccount_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fakeaccount_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fakeaccount_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fakeaccount_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fakeaccount_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fakeaccount_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldconsistency_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldconsistency_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_fieldconsistency_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldconsistency_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_fieldconsistency\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldconsistency_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldconsistency_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldconsistency_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldconsistency_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldconsistency_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldconsistency_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldformat_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldformat_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_fieldformat_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldformat_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_fieldformat\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldformat_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldformat_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldformat_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fieldformat_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fieldformat_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fieldformat_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fileuploadtype_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fileuploadtype_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_fileuploadtype_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fileuploadtype_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_fileuploadtype\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fileuploadtype_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fileuploadtype_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fileuploadtype_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_fileuploadtype_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_fileuploadtype_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_fileuploadtype_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonblockkeyword_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonblockkeyword_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_jsonblockkeyword_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonblockkeyword_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_jsonblockkeyword\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonblockkeyword_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonblockkeyword_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonblockkeyword_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonblockkeyword_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonblockkeyword_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonblockkeyword_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsoncmdurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsoncmdurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_jsoncmdurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsoncmdurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_jsoncmdurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsoncmdurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsoncmdurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsoncmdurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsoncmdurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsoncmdurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsoncmdurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsondosurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsondosurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_jsondosurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsondosurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_jsondosurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsondosurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsondosurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsondosurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsondosurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsondosurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsondosurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonsqlurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonsqlurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_jsonsqlurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonsqlurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_jsonsqlurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonsqlurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonsqlurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonsqlurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonsqlurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonsqlurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonsqlurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonxssurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonxssurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_jsonxssurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonxssurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_jsonxssurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonxssurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonxssurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonxssurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_jsonxssurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_jsonxssurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_jsonxssurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_logexpression_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_logexpression_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_logexpression_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_logexpression_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_logexpression\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_logexpression_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_logexpression_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_logexpression_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_logexpression_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_logexpression_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_logexpression_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_safeobject_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_safeobject_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_safeobject_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_safeobject_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_safeobject\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_safeobject_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_safeobject_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_safeobject_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_safeobject_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_safeobject_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_safeobject_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_sqlinjection_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_sqlinjection_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_sqlinjection_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_sqlinjection_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_sqlinjection\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_sqlinjection_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_sqlinjection_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_sqlinjection_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_sqlinjection_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_sqlinjection_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_sqlinjection_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_starturl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_starturl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_starturl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_starturl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_starturl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_starturl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_starturl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_starturl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_starturl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_starturl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_starturl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_trustedlearningclients_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_trustedlearningclients_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_trustedlearningclients_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_trustedlearningclients_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_trustedlearningclients\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_trustedlearningclients_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_trustedlearningclients_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_trustedlearningclients_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_trustedlearningclients_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_trustedlearningclients_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_trustedlearningclients_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlattachmenturl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlattachmenturl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmlattachmenturl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlattachmenturl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmlattachmenturl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlattachmenturl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlattachmenturl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlattachmenturl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlattachmenturl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlattachmenturl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlattachmenturl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmldosurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmldosurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmldosurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmldosurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmldosurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmldosurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmldosurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmldosurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmldosurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmldosurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmldosurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlsqlinjection_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlsqlinjection_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmlsqlinjection_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlsqlinjection_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmlsqlinjection\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlsqlinjection_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlsqlinjection_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlsqlinjection_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlsqlinjection_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlsqlinjection_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlsqlinjection_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlvalidationurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlvalidationurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmlvalidationurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlvalidationurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmlvalidationurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlvalidationurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlvalidationurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlvalidationurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlvalidationurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlvalidationurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlvalidationurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlwsiurl_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlwsiurl_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmlwsiurl_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlwsiurl_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmlwsiurl\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlwsiurl_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlwsiurl_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlwsiurl_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlwsiurl_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlwsiurl_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlwsiurl_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlxss_binding"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlxss_binding:

      .. rst-class:: ansible-option-title

      **appfwprofile_xmlxss_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlxss_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for appfwprofile\_xmlxss\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlxss_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlxss_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlxss_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-appfwprofile_xmlxss_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-appfwprofile_xmlxss_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appfwprofile_xmlxss_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-archivename"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-archivename:

      .. rst-class:: ansible-option-title

      **archivename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-archivename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Source for tar archive.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-augment"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-augment:

      .. rst-class:: ansible-option-title

      **augment**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-augment" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Augment Relaxation Rules during import


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-blockkeywordaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-blockkeywordaction:

      .. rst-class:: ansible-option-title

      **blockkeywordaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-blockkeywordaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Block Keyword action. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -blockKeywordAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -blockKeywordAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowaction:

      .. rst-class:: ansible-option-title

      **bufferoverflowaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Buffer Overflow actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -bufferOverflowAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowmaxcookielength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowmaxcookielength:

      .. rst-class:: ansible-option-title

      **bufferoverflowmaxcookielength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowmaxcookielength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in characters, for cookies sent to your protected web sites. Requests with longer cookies are blocked.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4096`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowmaxheaderlength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowmaxheaderlength:

      .. rst-class:: ansible-option-title

      **bufferoverflowmaxheaderlength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowmaxheaderlength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in characters, for HTTP headers in requests sent to your protected web sites. Requests with longer headers are blocked.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4096`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowmaxquerylength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowmaxquerylength:

      .. rst-class:: ansible-option-title

      **bufferoverflowmaxquerylength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowmaxquerylength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in bytes, for query string sent to your protected web sites. Requests with longer query strings are blocked.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`65535`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowmaxtotalheaderlength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowmaxtotalheaderlength:

      .. rst-class:: ansible-option-title

      **bufferoverflowmaxtotalheaderlength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowmaxtotalheaderlength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in bytes, for the total HTTP header length in requests sent to your protected web sites. The minimum value of this and maxHeaderLen in httpProfile will be used. Requests with longer length are blocked.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`65535`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bufferoverflowmaxurllength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-bufferoverflowmaxurllength:

      .. rst-class:: ansible-option-title

      **bufferoverflowmaxurllength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bufferoverflowmaxurllength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in characters, for URLs on your protected web sites. Requests with longer URLs are blocked.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1024`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-canonicalizehtmlresponse"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-canonicalizehtmlresponse:

      .. rst-class:: ansible-option-title

      **canonicalizehtmlresponse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-canonicalizehtmlresponse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Perform HTML entity encoding for any special characters in responses sent by your protected web sites.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ceflogging"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-ceflogging:

      .. rst-class:: ansible-option-title

      **ceflogging**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ceflogging" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable CEF format logs for the profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-checkrequestheaders"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-checkrequestheaders:

      .. rst-class:: ansible-option-title

      **checkrequestheaders**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-checkrequestheaders" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check request headers as well as web forms for injected SQL and cross-site scripts.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientipexpression"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-clientipexpression:

      .. rst-class:: ansible-option-title

      **clientipexpression**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientipexpression" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression to get the client IP.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cmdinjectionaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cmdinjectionaction:

      .. rst-class:: ansible-option-title

      **cmdinjectionaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cmdinjectionaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Command injection action. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -cmdInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -cmdInjectionAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cmdinjectiongrammar"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cmdinjectiongrammar:

      .. rst-class:: ansible-option-title

      **cmdinjectiongrammar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cmdinjectiongrammar" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for CMD injection using CMD grammar


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cmdinjectiontype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cmdinjectiontype:

      .. rst-class:: ansible-option-title

      **cmdinjectiontype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cmdinjectiontype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Available CMD injection types. 

      -\ :literal:`CMDSplChar`\               : Checks for CMD Special Chars

      -\ :literal:`CMDKeyword`\               : Checks for CMD Keywords

      -\ :literal:`CMDSplCharANDKeyword`\     : Checks for both and blocks if both are found

      -\ :literal:`CMDSplCharORKeyword`\      : Checks for both and blocks if anyone is found,

      -\ :literal:`None`\                     : Disables checking using both CMD Special Char and Keyword


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CMDSplChar"`
      - :ansible-option-choices-entry:`"CMDKeyword"`
      - :ansible-option-choices-entry:`"CMDSplCharORKeyword"`
      - :ansible-option-choices-entry-default:`"CMDSplCharANDKeyword"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"None"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-comment"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-comment:

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

      Any comments about the purpose of profile, or other useful information about the profile.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-contenttypeaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-contenttypeaction:

      .. rst-class:: ansible-option-title

      **contenttypeaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-contenttypeaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Content-type actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -contentTypeaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -contentTypeaction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookieconsistencyaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookieconsistencyaction:

      .. rst-class:: ansible-option-title

      **cookieconsistencyaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookieconsistencyaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Cookie Consistency actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -cookieConsistencyAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -cookieConsistencyAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookieencryption"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookieencryption:

      .. rst-class:: ansible-option-title

      **cookieencryption**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookieencryption" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of cookie encryption. Available settings function as follows:

      \* None - Do not encrypt cookies.

      \* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.

      \* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.

      \* Encrypt All - Encrypt all cookies.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"decryptOnly"`
      - :ansible-option-choices-entry:`"encryptSessionOnly"`
      - :ansible-option-choices-entry:`"encryptAll"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookiehijackingaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookiehijackingaction:

      .. rst-class:: ansible-option-title

      **cookiehijackingaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookiehijackingaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more actions to prevent cookie hijacking. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      NOTE: Cookie Hijacking feature is not supported for TLSv1.3

      

      CLI users: To enable one or more actions, type "set appfw profile -cookieHijackingAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -cookieHijackingAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookieproxying"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookieproxying:

      .. rst-class:: ansible-option-title

      **cookieproxying**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookieproxying" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cookie proxy setting. Available settings function as follows:

      \* None - Do not proxy cookies.

      \* Session Only - Proxy session cookies by using the Citrix ADC session ID, but do not proxy permanent cookies.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"sessionOnly"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookiesamesiteattribute"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookiesamesiteattribute:

      .. rst-class:: ansible-option-title

      **cookiesamesiteattribute**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookiesamesiteattribute" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Cookie Samesite attribute added to support adding cookie SameSite attribute for all set-cookies including appfw session cookies. Default value will be "SameSite=Lax".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"None"`
      - :ansible-option-choices-entry-default:`"LAX"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"STRICT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookietransforms"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-cookietransforms:

      .. rst-class:: ansible-option-title

      **cookietransforms**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cookietransforms" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Perform the specified type of cookie transformation. 

      Available settings function as follows: 

      \* Encryption - Encrypt cookies.

      \* Proxying - Mask contents of server cookies by sending proxy cookie to users.

      \* Cookie flags - Flag cookies as HTTP only to prevent scripts on user's browser from accessing and possibly modifying them.

      CAUTION: Make sure that this parameter is set to ON if you are configuring any cookie transformations. If it is set to OFF, no cookie transformations are performed regardless of any other settings.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-creditcard"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-creditcard:

      .. rst-class:: ansible-option-title

      **creditcard**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-creditcard" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Credit card types that the application firewall should protect.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"visa"`
      - :ansible-option-choices-entry:`"mastercard"`
      - :ansible-option-choices-entry:`"discover"`
      - :ansible-option-choices-entry:`"amex"`
      - :ansible-option-choices-entry:`"jcb"`
      - :ansible-option-choices-entry:`"dinersclub"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-creditcardaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-creditcardaction:

      .. rst-class:: ansible-option-title

      **creditcardaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-creditcardaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Credit Card actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -creditCardAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -creditCardAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-creditcardmaxallowed"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-creditcardmaxallowed:

      .. rst-class:: ansible-option-title

      **creditcardmaxallowed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-creditcardmaxallowed" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This parameter value is used by the block action. It represents the maximum number of credit card numbers that can appear on a web page served by your protected web sites. Pages that contain more credit card numbers are blocked.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-creditcardxout"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-creditcardxout:

      .. rst-class:: ansible-option-title

      **creditcardxout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-creditcardxout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Mask any credit card number detected in a response by replacing each digit, except the digits in the final group, with the letter "X."


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crosssitescriptingaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-crosssitescriptingaction:

      .. rst-class:: ansible-option-title

      **crosssitescriptingaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crosssitescriptingaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Cross-Site Scripting (XSS) actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -crossSiteScriptingAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -crossSiteScriptingAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crosssitescriptingcheckcompleteurls"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-crosssitescriptingcheckcompleteurls:

      .. rst-class:: ansible-option-title

      **crosssitescriptingcheckcompleteurls**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crosssitescriptingcheckcompleteurls" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check complete URLs for cross-site scripts, instead of just the query portions of URLs.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-crosssitescriptingtransformunsafehtml"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-crosssitescriptingtransformunsafehtml:

      .. rst-class:: ansible-option-title

      **crosssitescriptingtransformunsafehtml**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-crosssitescriptingtransformunsafehtml" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Transform cross-site scripts. This setting configures the application firewall to disable dangerous HTML instead of blocking the request. 

      CAUTION: Make sure that this parameter is set to ON if you are configuring any cross-site scripting transformations. If it is set to OFF, no cross-site scripting transformations are performed regardless of any other settings.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-csrftagaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-csrftagaction:

      .. rst-class:: ansible-option-title

      **csrftagaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-csrftagaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -CSRFTagAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -CSRFTagAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-customsettings"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-customsettings:

      .. rst-class:: ansible-option-title

      **customsettings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-customsettings" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Object name for custom settings.

      This check is applicable to Profile Type: HTML, XML.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultcharset"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-defaultcharset:

      .. rst-class:: ansible-option-title

      **defaultcharset**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultcharset" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default character set for protected web pages. Web pages sent by your protected web sites in response to user requests are assigned this character set if the page does not already specify a character set. The character sets supported by the application firewall are: 

      \* iso-8859-1 (English US)

      \* big5 (Chinese Traditional)

      \* gb2312 (Chinese Simplified)

      \* sjis (Japanese Shift-JIS)

      \* euc-jp (Japanese EUC-JP)

      \* iso-8859-9 (Turkish)

      \* utf-8 (Unicode)

      \* euc-kr (Korean)


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultfieldformatmaxlength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-defaultfieldformatmaxlength:

      .. rst-class:: ansible-option-title

      **defaultfieldformatmaxlength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultfieldformatmaxlength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum length, in characters, for data entered into a field that is assigned the default field type.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`65535`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultfieldformatminlength"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-defaultfieldformatminlength:

      .. rst-class:: ansible-option-title

      **defaultfieldformatminlength**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultfieldformatminlength" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Minimum length, in characters, for data entered into a field that is assigned the default field type. 

      To disable the minimum and maximum length settings and allow data of any length to be entered into the field, set this parameter to zero (0).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultfieldformattype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-defaultfieldformattype:

      .. rst-class:: ansible-option-title

      **defaultfieldformattype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultfieldformattype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Designate a default field type to be applied to web form fields that do not have a field type explicitly assigned to them.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaults"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-defaults:

      .. rst-class:: ansible-option-title

      **defaults**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaults" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default configuration to apply to the profile. Basic defaults are intended for standard content that requires little further configuration, such as static web site content. Advanced defaults are intended for specialized content that requires significant specialized configuration, such as heavily scripted or dynamic content.

      

      CLI users: When adding an application firewall profile, you can set either the defaults or the type, but not both. To set both options, create the profile by using the add appfw profile command, and then use the set appfw profile command to configure the other option.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"basic"`
      - :ansible-option-choices-entry:`"advanced"`
      - :ansible-option-choices-entry:`"core"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-denyurlaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-denyurlaction:

      .. rst-class:: ansible-option-title

      **denyurlaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-denyurlaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Deny URL actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      NOTE: The Deny URL check takes precedence over the Start URL check. If you enable blocking for the Deny URL check, the application firewall blocks any URL that is explicitly blocked by a Deny URL, even if the same URL would otherwise be allowed by the Start URL check.

      

      CLI users: To enable one or more actions, type "set appfw profile -denyURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -denyURLaction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dosecurecreditcardlogging"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-dosecurecreditcardlogging:

      .. rst-class:: ansible-option-title

      **dosecurecreditcardlogging**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dosecurecreditcardlogging" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Setting this option logs credit card numbers in the response when the match is found.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dynamiclearning"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-dynamiclearning:

      .. rst-class:: ansible-option-title

      **dynamiclearning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dynamiclearning" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more security checks. Available options are as follows:

      \* \ :literal:`SQLInjection`\  - Enable dynamic learning for \ :literal:`SQLInjection`\  security check.

      \* \ :literal:`CrossSiteScripting`\  - Enable dynamic learning for \ :literal:`CrossSiteScripting`\  security check.

      \* \ :literal:`fieldFormat`\  - Enable dynamic learning for  \ :literal:`fieldFormat`\  security check.

      \* None - Disable security checks for all security checks.

      

      CLI users: To enable dynamic learning on one or more security checks, type "set appfw profile -dynamicLearning" followed by the security checks to be enabled. To turn off dynamic learning on all security checks, type "set appfw profile -dynamicLearning \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"SQLInjection"`
      - :ansible-option-choices-entry:`"CrossSiteScripting"`
      - :ansible-option-choices-entry:`"fieldFormat"`
      - :ansible-option-choices-entry:`"startURL"`
      - :ansible-option-choices-entry:`"cookieConsistency"`
      - :ansible-option-choices-entry:`"fieldConsistency"`
      - :ansible-option-choices-entry:`"CSRFtag"`
      - :ansible-option-choices-entry:`"ContentType"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enableformtagging"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-enableformtagging:

      .. rst-class:: ansible-option-title

      **enableformtagging**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enableformtagging" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable tagging of web form fields for use by the Form Field Consistency and CSRF Form Tagging checks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-errorurl"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-errorurl:

      .. rst-class:: ansible-option-title

      **errorurl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-errorurl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL that application firewall uses as the Error URL.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-excludefileuploadfromchecks"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-excludefileuploadfromchecks:

      .. rst-class:: ansible-option-title

      **excludefileuploadfromchecks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-excludefileuploadfromchecks" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Exclude uploaded files from Form checks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-exemptclosureurlsfromsecuritychecks"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-exemptclosureurlsfromsecuritychecks:

      .. rst-class:: ansible-option-title

      **exemptclosureurlsfromsecuritychecks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-exemptclosureurlsfromsecuritychecks" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Exempt URLs that pass the Start URL closure check from SQL injection, cross-site script, field format and field consistency security checks at locations other than headers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fakeaccountdetection"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-fakeaccountdetection:

      .. rst-class:: ansible-option-title

      **fakeaccountdetection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fakeaccountdetection" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Fake account detection flag : ON/OFF. If set to ON fake account detection in enabled on ADC, if set to OFF fake account detection is disabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fieldconsistencyaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-fieldconsistencyaction:

      .. rst-class:: ansible-option-title

      **fieldconsistencyaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fieldconsistencyaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Form Field Consistency actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -fieldConsistencyaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldConsistencyAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fieldformataction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-fieldformataction:

      .. rst-class:: ansible-option-title

      **fieldformataction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fieldformataction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Field Format actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of suggested web form fields and field format assignments.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -fieldFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fieldFormatAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fileuploadmaxnum"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-fileuploadmaxnum:

      .. rst-class:: ansible-option-title

      **fileuploadmaxnum**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fileuploadmaxnum" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum allowed number of file uploads per form-submission request. The maximum setting (65535) allows an unlimited number of uploads.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`65535`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fileuploadtypesaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-fileuploadtypesaction:

      .. rst-class:: ansible-option-title

      **fileuploadtypesaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fileuploadtypesaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more file upload types actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -fileUploadTypeAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -fileUploadTypeAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-geolocationlogging"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-geolocationlogging:

      .. rst-class:: ansible-option-title

      **geolocationlogging**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-geolocationlogging" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable Geo-Location Logging in CEF format logs for the profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-grpcaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-grpcaction:

      .. rst-class:: ansible-option-title

      **grpcaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-grpcaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      gRPC validation


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-htmlerrorobject"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-htmlerrorobject:

      .. rst-class:: ansible-option-title

      **htmlerrorobject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-htmlerrorobject" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name to assign to the HTML Error Object. 

      Must begin with a letter, number, or the underscore character \\(\_\\), and must contain only letters, numbers, and the hyphen \\(-\\), period \\(.\\) pound \\(\\#\\), space \\( \\), at (@), equals \\(=\\), colon \\(:\\), and underscore characters. Cannot be changed after the HTML error object is added.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks \\(for example, "my HTML error object" or 'my HTML error object'\\).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-htmlerrorstatuscode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-htmlerrorstatuscode:

      .. rst-class:: ansible-option-title

      **htmlerrorstatuscode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-htmlerrorstatuscode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status code associated with HTML error page. Non-empty HTML error object must be imported to the application firewall profile for the status code.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-htmlerrorstatusmessage"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-htmlerrorstatusmessage:

      .. rst-class:: ansible-option-title

      **htmlerrorstatusmessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-htmlerrorstatusmessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status message associated with HTML error page


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-importprofilename"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-importprofilename:

      .. rst-class:: ansible-option-title

      **importprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-importprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the profile which will be created/updated to associate the relaxation rules


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-infercontenttypexmlpayloadaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-infercontenttypexmlpayloadaction:

      .. rst-class:: ansible-option-title

      **infercontenttypexmlpayloadaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-infercontenttypexmlpayloadaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more infer content type payload actions. Available settings function as follows:

      \* Block - Block connections that have mismatch in content-type header and payload.

      \* Log - Log connections that have mismatch in content-type header and payload. The mismatched content-type in HTTP request header will be logged for the request.

      \* Stats - Generate statistics when there is mismatch in content-type header and payload.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -inferContentTypeXMLPayloadAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -inferContentTypeXMLPayloadAction \ :literal:`none`\ ". Please note "\ :literal:`none`\ " action cannot be used with any other action type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`
      - :ansible-option-choices-entry:`"none"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-insertcookiesamesiteattribute"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-insertcookiesamesiteattribute:

      .. rst-class:: ansible-option-title

      **insertcookiesamesiteattribute**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-insertcookiesamesiteattribute" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configure whether application firewall should add samesite attribute for set-cookies


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-inspectcontenttypes"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-inspectcontenttypes:

      .. rst-class:: ansible-option-title

      **inspectcontenttypes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-inspectcontenttypes" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more InspectContentType lists. 

      \* \ :literal:`application/x-www-form-urlencoded`\ 

      \* \ :literal:`multipart/form-data`\ 

      \* \ :literal:`text/x-gwt-rpc`\ 

      

      CLI users: To enable, type "set appfw profile -InspectContentTypes" followed by the content types to be inspected.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"application/x-www-form-urlencoded"`
      - :ansible-option-choices-entry:`"multipart/form-data"`
      - :ansible-option-choices-entry:`"text/x-gwt-rpc"`
      - :ansible-option-choices-entry:`"application/grpc"`
      - :ansible-option-choices-entry:`"application/grpc-web-text"`
      - :ansible-option-choices-entry:`"application/grpc-web+json"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-inspectquerycontenttypes"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-inspectquerycontenttypes:

      .. rst-class:: ansible-option-title

      **inspectquerycontenttypes**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-inspectquerycontenttypes" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Inspect request query as well as web forms for injected SQL and cross-site scripts for following content types.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"HTML"`
      - :ansible-option-choices-entry:`"XML"`
      - :ansible-option-choices-entry:`"JSON"`
      - :ansible-option-choices-entry:`"OTHER"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-instance_name:

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
        <div class="ansibleOptionAnchor" id="parameter-invalidpercenthandling"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-invalidpercenthandling:

      .. rst-class:: ansible-option-title

      **invalidpercenthandling**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-invalidpercenthandling" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configure the method that the application firewall uses to handle percent-encoded names and values. Available settings function as follows: 

      \* \ :literal:`apache\_mode`\  - Apache format.

      \* \ :literal:`asp\_mode`\  - Microsoft ASP format.

      \* \ :literal:`secure\_mode`\  - Secure format.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"apache\_mode"`
      - :ansible-option-choices-entry:`"asp\_mode"`
      - :ansible-option-choices-entry-default:`"secure\_mode"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-is_cloud:

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
        <div class="ansibleOptionAnchor" id="parameter-jsonblockkeywordaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonblockkeywordaction:

      .. rst-class:: ansible-option-title

      **jsonblockkeywordaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonblockkeywordaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      JSON Block Keyword action. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -JSONBlockKeywordAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -JSONBlockKeywordAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["none"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsoncmdinjectionaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsoncmdinjectionaction:

      .. rst-class:: ansible-option-title

      **jsoncmdinjectionaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsoncmdinjectionaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more JSON CMD Injection actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -JSONCMDInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -JSONCMDInjectionAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsoncmdinjectiongrammar"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsoncmdinjectiongrammar:

      .. rst-class:: ansible-option-title

      **jsoncmdinjectiongrammar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsoncmdinjectiongrammar" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for CMD injection using CMD grammar in JSON


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsoncmdinjectiontype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsoncmdinjectiontype:

      .. rst-class:: ansible-option-title

      **jsoncmdinjectiontype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsoncmdinjectiontype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Available CMD injection types.

      -\ :literal:`CMDSplChar`\               : Checks for CMD Special Chars

      -\ :literal:`CMDKeyword`\               : Checks for CMD Keywords

      -\ :literal:`CMDSplCharANDKeyword`\     : Checks for both and blocks if both are found

      -\ :literal:`CMDSplCharORKeyword`\      : Checks for both and blocks if anyone is found,

      -\ :literal:`None`\                     : Disables checking using both SQL Special Char and Keyword


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"CMDSplChar"`
      - :ansible-option-choices-entry:`"CMDKeyword"`
      - :ansible-option-choices-entry:`"CMDSplCharORKeyword"`
      - :ansible-option-choices-entry-default:`"CMDSplCharANDKeyword"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"None"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsondosaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsondosaction:

      .. rst-class:: ansible-option-title

      **jsondosaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsondosaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more JSON Denial-of-Service (JsonDoS) actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -JSONDoSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -JSONDoSAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonerrorobject"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonerrorobject:

      .. rst-class:: ansible-option-title

      **jsonerrorobject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonerrorobject" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name to the imported JSON Error Object to be set on application firewall profile.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks \\(for example, "my JSON error object" or 'my JSON error object'\\).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonerrorstatuscode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonerrorstatuscode:

      .. rst-class:: ansible-option-title

      **jsonerrorstatuscode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonerrorstatuscode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status code associated with JSON error page. Non-empty JSON error object must be imported to the application firewall profile for the status code.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonerrorstatusmessage"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonerrorstatusmessage:

      .. rst-class:: ansible-option-title

      **jsonerrorstatusmessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonerrorstatusmessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status message associated with JSON error page


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonsqlinjectionaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonsqlinjectionaction:

      .. rst-class:: ansible-option-title

      **jsonsqlinjectionaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonsqlinjectionaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more JSON SQL Injection actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -JSONSQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -JSONSQLInjectionAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonsqlinjectiongrammar"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonsqlinjectiongrammar:

      .. rst-class:: ansible-option-title

      **jsonsqlinjectiongrammar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonsqlinjectiongrammar" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for SQL injection using SQL grammar in JSON


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonsqlinjectiontype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonsqlinjectiontype:

      .. rst-class:: ansible-option-title

      **jsonsqlinjectiontype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonsqlinjectiontype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Available SQL injection types.

      -\ :literal:`SQLSplChar`\               : Checks for SQL Special Chars

      -\ :literal:`SQLKeyword`\               : Checks for SQL Keywords

      -\ :literal:`SQLSplCharANDKeyword`\     : Checks for both and blocks if both are found

      -\ :literal:`SQLSplCharORKeyword`\      : Checks for both and blocks if anyone is found,

      -\ :literal:`None`\                     : Disables checking using both SQL Special Char and Keyword


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SQLSplChar"`
      - :ansible-option-choices-entry:`"SQLKeyword"`
      - :ansible-option-choices-entry:`"SQLSplCharORKeyword"`
      - :ansible-option-choices-entry-default:`"SQLSplCharANDKeyword"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"None"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-jsonxssaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-jsonxssaction:

      .. rst-class:: ansible-option-title

      **jsonxssaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-jsonxssaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more JSON Cross-Site Scripting actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -JSONXssAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -JSONXssAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logeverypolicyhit"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-logeverypolicyhit:

      .. rst-class:: ansible-option-title

      **logeverypolicyhit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logeverypolicyhit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Log every profile match, regardless of security checks results.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-mas_proxy_call:

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
        <div class="ansibleOptionAnchor" id="parameter-matchurlstring"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-matchurlstring:

      .. rst-class:: ansible-option-title

      **matchurlstring**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-matchurlstring" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Match this action url in archived Relaxation Rules to replace.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-multipleheaderaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-multipleheaderaction:

      .. rst-class:: ansible-option-title

      **multipleheaderaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-multipleheaderaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more multiple header actions. Available settings function as follows:

      \* Block - Block connections that have multiple headers.

      \* Log - Log connections that have multiple headers.

      \* KeepLast - Keep only last header when multiple headers are present.

      

      CLI users: To enable one or more actions, type "set appfw profile -multipleHeaderAction" followed by the actions to be enabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"keepLast"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"none"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-name:

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

      Name for the profile. Must begin with a letter, number, or the underscore character (\_), and must contain only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore (\_) characters. Cannot be changed after the profile is added.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-optimizepartialreqs"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-optimizepartialreqs:

      .. rst-class:: ansible-option-title

      **optimizepartialreqs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-optimizepartialreqs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Optimize handle of HTTP partial requests i.e. those with range headers.

      Available settings are as follows: 

      \* ON  - Partial requests by the client result in partial requests to the backend server in most cases.

      \* OFF - Partial requests by the client are changed to full requests to the backend server


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-overwrite"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-overwrite:

      .. rst-class:: ansible-option-title

      **overwrite**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-overwrite" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Purge existing Relaxation Rules and replace during import


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-percentdecoderecursively"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-percentdecoderecursively:

      .. rst-class:: ansible-option-title

      **percentdecoderecursively**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-percentdecoderecursively" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configure whether the application firewall should use percentage recursive decoding


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postbodylimit"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-postbodylimit:

      .. rst-class:: ansible-option-title

      **postbodylimit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postbodylimit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum allowed HTTP post body size, in bytes. Maximum supported value is 10GB. Citrix recommends enabling streaming option for large values of post body limit (\>20MB).


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`20000000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postbodylimitaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-postbodylimitaction:

      .. rst-class:: ansible-option-title

      **postbodylimitaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postbodylimitaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Post Body Limit actions. Available settings function as follows:

      \* Block - Block connections that violate this security check. Must always be set.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -PostBodyLimitAction \ :literal:`block`\ " followed by the other actions to be enabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-postbodylimitsignature"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-postbodylimitsignature:

      .. rst-class:: ansible-option-title

      **postbodylimitsignature**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-postbodylimitsignature" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum allowed HTTP post body size for signature inspection for location HTTP\_POST\_BODY in the signatures, in bytes. Note that the changes in value could impact CPU and latency profile.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2048`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-protofileobject"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-protofileobject:

      .. rst-class:: ansible-option-title

      **protofileobject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-protofileobject" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the imported proto file.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refererheadercheck"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-refererheadercheck:

      .. rst-class:: ansible-option-title

      **refererheadercheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refererheadercheck" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable validation of Referer headers. 

      Referer validation ensures that a web form that a user sends to your web site originally came from your web site, not an outside attacker. 

      Although this parameter is part of the Start URL check, referer validation protects against cross-site request forgery (CSRF) attacks, not Start URL attacks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"if\_present"`
      - :ansible-option-choices-entry:`"AlwaysExceptStartURLs"`
      - :ansible-option-choices-entry:`"AlwaysExceptFirstRequest"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-relaxationrules"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-relaxationrules:

      .. rst-class:: ansible-option-title

      **relaxationrules**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-relaxationrules" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Import all appfw relaxation rules


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-replaceurlstring"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-replaceurlstring:

      .. rst-class:: ansible-option-title

      **replaceurlstring**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-replaceurlstring" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Replace matched url string with this action url string while restoring Relaxation Rules


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-requestcontenttype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-requestcontenttype:

      .. rst-class:: ansible-option-title

      **requestcontenttype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-requestcontenttype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default Content-Type header for requests. 

      A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (\_) characters.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-responsecontenttype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-responsecontenttype:

      .. rst-class:: ansible-option-title

      **responsecontenttype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-responsecontenttype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Default Content-Type header for responses. 

      A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (\_) characters.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rfcprofile"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-rfcprofile:

      .. rst-class:: ansible-option-title

      **rfcprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rfcprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Object name of the rfc profile.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-semicolonfieldseparator"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-semicolonfieldseparator:

      .. rst-class:: ansible-option-title

      **semicolonfieldseparator**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-semicolonfieldseparator" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow ';' as a form field separator in URL queries and POST form bodies.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionlessfieldconsistency"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sessionlessfieldconsistency:

      .. rst-class:: ansible-option-title

      **sessionlessfieldconsistency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionlessfieldconsistency" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Perform sessionless Field Consistency Checks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"postOnly"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionlessurlclosure"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sessionlessurlclosure:

      .. rst-class:: ansible-option-title

      **sessionlessurlclosure**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionlessurlclosure" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable session less URL Closure Checks.

      This check is applicable to Profile Type: HTML.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-signatures"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-signatures:

      .. rst-class:: ansible-option-title

      **signatures**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-signatures" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Object name for signatures.

      This check is applicable to Profile Type: HTML, XML.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectionaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectionaction:

      .. rst-class:: ansible-option-title

      **sqlinjectionaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectionaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more HTML SQL Injection actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -SQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -SQLInjectionAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectionchecksqlwildchars"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectionchecksqlwildchars:

      .. rst-class:: ansible-option-title

      **sqlinjectionchecksqlwildchars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectionchecksqlwildchars" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for form fields that contain SQL wild chars .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectiongrammar"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectiongrammar:

      .. rst-class:: ansible-option-title

      **sqlinjectiongrammar**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectiongrammar" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for SQL injection using SQL grammar


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectiononlycheckfieldswithsqlchars"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectiononlycheckfieldswithsqlchars:

      .. rst-class:: ansible-option-title

      **sqlinjectiononlycheckfieldswithsqlchars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectiononlycheckfieldswithsqlchars" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check only form fields that contain SQL special strings (characters) for injected SQL code.

      Most SQL servers require a special string to activate an SQL request, so SQL code without a special string is harmless to most SQL servers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectionparsecomments"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectionparsecomments:

      .. rst-class:: ansible-option-title

      **sqlinjectionparsecomments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectionparsecomments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Parse HTML comments and exempt them from the HTML SQL Injection check. You must specify the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:

      \* Check all - Check all content.

      \* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 

      \* Nested - Exempt content that is part of a \ :literal:`nested`\  (Microsoft-style) comment.

      \* ANSI Nested - Exempt content that is part of any type of comment.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"checkall"`
      - :ansible-option-choices-entry:`"ansi"`
      - :ansible-option-choices-entry:`"nested"`
      - :ansible-option-choices-entry:`"ansinested"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectionruletype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectionruletype:

      .. rst-class:: ansible-option-title

      **sqlinjectionruletype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectionruletype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies SQL Injection rule type: \ :literal:`ALLOW`\ /\ :literal:`DENY`\ . If \ :literal:`ALLOW`\  rule type is configured then allow list rules are used, if \ :literal:`DENY`\  rule type is configured then deny rules are used.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ALLOW"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DENY"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectiontransformspecialchars"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectiontransformspecialchars:

      .. rst-class:: ansible-option-title

      **sqlinjectiontransformspecialchars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectiontransformspecialchars" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Transform injected SQL code. This setting configures the application firewall to disable SQL special strings instead of blocking the request. Since most SQL servers require a special string to activate an SQL keyword, in most cases a request that contains injected SQL code is safe if special strings are disabled.

      CAUTION: Make sure that this parameter is set to ON if you are configuring any SQL injection transformations. If it is set to OFF, no SQL injection transformations are performed regardless of any other settings.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sqlinjectiontype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-sqlinjectiontype:

      .. rst-class:: ansible-option-title

      **sqlinjectiontype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sqlinjectiontype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Available SQL injection types. 

      -\ :literal:`SQLSplChar`\               : Checks for SQL Special Chars

      -\ :literal:`SQLKeyword`\ 		 : Checks for SQL Keywords

      -\ :literal:`SQLSplCharANDKeyword`\     : Checks for both and blocks if both are found

      -\ :literal:`SQLSplCharORKeyword`\      : Checks for both and blocks if anyone is found

      -\ :literal:`None`\                     : Disables checking using both SQL Special Char and Keyword


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SQLSplChar"`
      - :ansible-option-choices-entry:`"SQLKeyword"`
      - :ansible-option-choices-entry:`"SQLSplCharORKeyword"`
      - :ansible-option-choices-entry-default:`"SQLSplCharANDKeyword"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"None"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-starturlaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-starturlaction:

      .. rst-class:: ansible-option-title

      **starturlaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-starturlaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Start URL actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -startURLaction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -startURLaction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-starturlclosure"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-starturlclosure:

      .. rst-class:: ansible-option-title

      **starturlclosure**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-starturlclosure" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle  the state of Start URL Closure.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-state:

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

      The state of the resource being configured by the module on the NetScaler ADC node.

      \ :literal:`enabled`\  and \ :literal:`disabled`\  are only valid for resources that can be enabled or disabled.

      When \ :literal:`present`\  the resource will be created if needed and configured according to the module's parameters.

      When \ :literal:`absent`\  the resource will be deleted from the NetScaler ADC node.

      When \ :literal:`enabled`\  the resource will be enabled on the NetScaler ADC node.

      When \ :literal:`disabled`\  the resource will be disabled on the NetScaler ADC node.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"enabled"`
      - :ansible-option-choices-entry:`"disabled"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-streaming"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-streaming:

      .. rst-class:: ansible-option-title

      **streaming**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-streaming" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Setting this option converts content-length form submission requests (requests with content-type "application/x-www-form-urlencoded" or "multipart/form-data") to chunked requests when atleast one of the following protections : Signatures, SQL injection protection, XSS protection, form field consistency protection, starturl closure, CSRF tagging, JSON SQL, JSON XSS, JSON DOS is enabled. Please make sure that the backend server accepts chunked requests before enabling this option. Citrix recommends enabling this option for large request sizes(\>20MB).


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-stripcomments"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-stripcomments:

      .. rst-class:: ansible-option-title

      **stripcomments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-stripcomments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Strip HTML comments.

      This check is applicable to Profile Type: HTML.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-striphtmlcomments"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-striphtmlcomments:

      .. rst-class:: ansible-option-title

      **striphtmlcomments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-striphtmlcomments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Strip HTML comments before forwarding a web page sent by a protected web site in response to a user request.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"all"`
      - :ansible-option-choices-entry:`"exclude\_script\_tag"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-stripxmlcomments"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-stripxmlcomments:

      .. rst-class:: ansible-option-title

      **stripxmlcomments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-stripxmlcomments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Strip XML comments before forwarding a web page sent by a protected web site in response to a user request.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"none"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"all"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-trace"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-trace:

      .. rst-class:: ansible-option-title

      **trace**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-trace" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle  the state of trace


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Application firewall profile type, which controls which security checks and settings are applied to content that is filtered with the profile. Available settings function as follows:

      \* \ :literal:`HTML`\  - \ :literal:`HTML`\ -based web sites.

      \* \ :literal:`XML`\  -  \ :literal:`XML`\ -based web sites and services.

      \* \ :literal:`JSON`\  - \ :literal:`JSON`\ -based web sites and services.

      \* \ :literal:`HTML`\  \ :literal:`XML`\  (Web 2.0) - Sites that contain both \ :literal:`HTML`\  and \ :literal:`XML`\  content, such as ATOM feeds, blogs, and RSS feeds.

      \* \ :literal:`HTML`\  \ :literal:`JSON`\   - Sites that contain both \ :literal:`HTML`\  and \ :literal:`JSON`\  content.

      \* \ :literal:`XML`\  \ :literal:`JSON`\    - Sites that contain both \ :literal:`XML`\  and \ :literal:`JSON`\  content.

      \* \ :literal:`HTML`\  \ :literal:`XML`\  \ :literal:`JSON`\    - Sites that contain \ :literal:`HTML`\ , \ :literal:`XML`\  and \ :literal:`JSON`\  content.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"HTML"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"XML"`
      - :ansible-option-choices-entry:`"JSON"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["HTML"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-urldecoderequestcookies"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-urldecoderequestcookies:

      .. rst-class:: ansible-option-title

      **urldecoderequestcookies**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-urldecoderequestcookies" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL Decode request cookies before subjecting them to SQL and cross-site scripting checks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usehtmlerrorobject"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-usehtmlerrorobject:

      .. rst-class:: ansible-option-title

      **usehtmlerrorobject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usehtmlerrorobject" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Send an imported HTML Error object to a user when a request is blocked, instead of redirecting the user to the designated Error URL.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-validate_certs:

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
        <div class="ansibleOptionAnchor" id="parameter-verboseloglevel"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-verboseloglevel:

      .. rst-class:: ansible-option-title

      **verboseloglevel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-verboseloglevel" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Detailed Logging Verbose Log Level.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"pattern"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"patternPayload"`
      - :ansible-option-choices-entry:`"patternPayloadHeader"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlattachmentaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlattachmentaction:

      .. rst-class:: ansible-option-title

      **xmlattachmentaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlattachmentaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML Attachment actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLAttachmentAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLAttachmentAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmldosaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmldosaction:

      .. rst-class:: ansible-option-title

      **xmldosaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmldosaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML Denial-of-Service (XDoS) actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLDoSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLDoSAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlerrorobject"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlerrorobject:

      .. rst-class:: ansible-option-title

      **xmlerrorobject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlerrorobject" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name to assign to the XML Error Object, which the application firewall displays when a user request is blocked.

      Must begin with a letter, number, or the underscore character \\(\_\\), and must contain only letters, numbers, and the hyphen \\(-\\), period \\(.\\) pound \\(\\#\\), space \\( \\), at (@), equals \\(=\\), colon \\(:\\), and underscore characters. Cannot be changed after the XML error object is added.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks \\(for example, "my XML error object" or 'my XML error object'\\).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlerrorstatuscode"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlerrorstatuscode:

      .. rst-class:: ansible-option-title

      **xmlerrorstatuscode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlerrorstatuscode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status code associated with XML error page. Non-empty XML error object must be imported to the application firewall profile for the status code.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`200`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlerrorstatusmessage"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlerrorstatusmessage:

      .. rst-class:: ansible-option-title

      **xmlerrorstatusmessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlerrorstatusmessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Response status message associated with XML error page


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlformataction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlformataction:

      .. rst-class:: ansible-option-title

      **xmlformataction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlformataction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML Format actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLFormatAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsoapfaultaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsoapfaultaction:

      .. rst-class:: ansible-option-title

      **xmlsoapfaultaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsoapfaultaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML SOAP Fault Filtering actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      \* Remove - Remove all violations for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLSOAPFaultAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSOAPFaultAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"remove"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsqlinjectionaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsqlinjectionaction:

      .. rst-class:: ansible-option-title

      **xmlsqlinjectionaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsqlinjectionaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML SQL Injection actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLSQLInjectionAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsqlinjectionchecksqlwildchars"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsqlinjectionchecksqlwildchars:

      .. rst-class:: ansible-option-title

      **xmlsqlinjectionchecksqlwildchars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsqlinjectionchecksqlwildchars" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check for form fields that contain SQL wild chars .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsqlinjectiononlycheckfieldswithsqlchars"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsqlinjectiononlycheckfieldswithsqlchars:

      .. rst-class:: ansible-option-title

      **xmlsqlinjectiononlycheckfieldswithsqlchars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsqlinjectiononlycheckfieldswithsqlchars" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Check only form fields that contain SQL special characters, which most SQL servers require before accepting an SQL command, for injected SQL.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsqlinjectionparsecomments"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsqlinjectionparsecomments:

      .. rst-class:: ansible-option-title

      **xmlsqlinjectionparsecomments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsqlinjectionparsecomments" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Parse comments in XML Data and exempt those sections of the request that are from the XML SQL Injection check. You must configure the type of comments that the application firewall is to detect and exempt from this security check. Available settings function as follows:

      \* Check all - Check all content.

      \* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. 

      \* Nested - Exempt content that is part of a \ :literal:`nested`\  (Microsoft-style) comment.

      \* ANSI Nested - Exempt content that is part of any type of comment.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"checkall"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"ansi"`
      - :ansible-option-choices-entry:`"nested"`
      - :ansible-option-choices-entry:`"ansinested"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlsqlinjectiontype"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlsqlinjectiontype:

      .. rst-class:: ansible-option-title

      **xmlsqlinjectiontype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlsqlinjectiontype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Available SQL injection types.

      -\ :literal:`SQLSplChar`\               : Checks for SQL Special Chars

      -\ :literal:`SQLKeyword`\               : Checks for SQL Keywords

      -\ :literal:`SQLSplCharANDKeyword`\     : Checks for both and blocks if both are found

      -\ :literal:`SQLSplCharORKeyword`\      : Checks for both and blocks if anyone is found


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SQLSplChar"`
      - :ansible-option-choices-entry:`"SQLKeyword"`
      - :ansible-option-choices-entry:`"SQLSplCharORKeyword"`
      - :ansible-option-choices-entry-default:`"SQLSplCharANDKeyword"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"None"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlvalidationaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlvalidationaction:

      .. rst-class:: ansible-option-title

      **xmlvalidationaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlvalidationaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML Validation actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check. 

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLValidationAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlwsiaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlwsiaction:

      .. rst-class:: ansible-option-title

      **xmlwsiaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlwsiaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more Web Services Interoperability (WSI) actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Learn - Use the learning engine to generate a list of exceptions to this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLWSIAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLWSIAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-xmlxssaction"></div>

      .. _ansible_collections.netscaler.adc.appfwprofile_module__parameter-xmlxssaction:

      .. rst-class:: ansible-option-title

      **xmlxssaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-xmlxssaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more XML Cross-Site Scripting actions. Available settings function as follows:

      \* Block - Block connections that violate this security check.

      \* Log - Log violations of this security check.

      \* Stats - Generate statistics for this security check.

      \* None - Disable all actions for this security check.

      

      CLI users: To enable one or more actions, type "set appfw profile -XMLXSSAction" followed by the actions to be enabled. To turn off all actions, type "set appfw profile -XMLXSSAction \ :literal:`none`\ ".


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"block"`
      - :ansible-option-choices-entry:`"learn"`
      - :ansible-option-choices-entry:`"log"`
      - :ansible-option-choices-entry:`"stats"`


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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.appfwprofile_module__return-loglines:

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

