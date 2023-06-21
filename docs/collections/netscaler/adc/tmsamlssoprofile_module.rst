
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

.. _ansible_collections.netscaler.adc.tmsamlssoprofile_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.tmsamlssoprofile module -- Configuration for SAML sso action resource.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.tmsamlssoprofile`.

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

- Configuration for SAML sso action resource.


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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-api_path:

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
        <div class="ansibleOptionAnchor" id="parameter-assertionconsumerserviceurl"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-assertionconsumerserviceurl:

      .. rst-class:: ansible-option-title

      **assertionconsumerserviceurl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-assertionconsumerserviceurl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL to which the assertion is to be sent.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute1"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute1:

      .. rst-class:: ansible-option-title

      **attribute1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute1" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute1 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute10"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute10:

      .. rst-class:: ansible-option-title

      **attribute10**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute10" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute10 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute10expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute10expr:

      .. rst-class:: ansible-option-title

      **attribute10expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute10expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute10's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute10format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute10format:

      .. rst-class:: ansible-option-title

      **attribute10format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute10format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute10 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute10friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute10friendlyname:

      .. rst-class:: ansible-option-title

      **attribute10friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute10friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute10 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute11"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute11:

      .. rst-class:: ansible-option-title

      **attribute11**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute11" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute11 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute11expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute11expr:

      .. rst-class:: ansible-option-title

      **attribute11expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute11expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute11's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute11format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute11format:

      .. rst-class:: ansible-option-title

      **attribute11format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute11format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute11 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute11friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute11friendlyname:

      .. rst-class:: ansible-option-title

      **attribute11friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute11friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute11 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute12"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute12:

      .. rst-class:: ansible-option-title

      **attribute12**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute12" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute12 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute12expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute12expr:

      .. rst-class:: ansible-option-title

      **attribute12expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute12expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute12's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute12format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute12format:

      .. rst-class:: ansible-option-title

      **attribute12format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute12format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute12 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute12friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute12friendlyname:

      .. rst-class:: ansible-option-title

      **attribute12friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute12friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute12 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute13"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute13:

      .. rst-class:: ansible-option-title

      **attribute13**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute13" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute13 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute13expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute13expr:

      .. rst-class:: ansible-option-title

      **attribute13expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute13expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute13's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute13format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute13format:

      .. rst-class:: ansible-option-title

      **attribute13format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute13format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute13 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute13friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute13friendlyname:

      .. rst-class:: ansible-option-title

      **attribute13friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute13friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute13 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute14"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute14:

      .. rst-class:: ansible-option-title

      **attribute14**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute14" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute14 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute14expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute14expr:

      .. rst-class:: ansible-option-title

      **attribute14expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute14expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute14's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute14format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute14format:

      .. rst-class:: ansible-option-title

      **attribute14format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute14format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute14 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute14friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute14friendlyname:

      .. rst-class:: ansible-option-title

      **attribute14friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute14friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute14 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute15"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute15:

      .. rst-class:: ansible-option-title

      **attribute15**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute15" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute15 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute15expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute15expr:

      .. rst-class:: ansible-option-title

      **attribute15expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute15expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute15's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute15format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute15format:

      .. rst-class:: ansible-option-title

      **attribute15format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute15format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute15 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute15friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute15friendlyname:

      .. rst-class:: ansible-option-title

      **attribute15friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute15friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute15 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute16"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute16:

      .. rst-class:: ansible-option-title

      **attribute16**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute16" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute16 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute16expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute16expr:

      .. rst-class:: ansible-option-title

      **attribute16expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute16expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute16's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute16format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute16format:

      .. rst-class:: ansible-option-title

      **attribute16format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute16format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute16 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute16friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute16friendlyname:

      .. rst-class:: ansible-option-title

      **attribute16friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute16friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute16 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute1expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute1expr:

      .. rst-class:: ansible-option-title

      **attribute1expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute1expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute1's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute1format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute1format:

      .. rst-class:: ansible-option-title

      **attribute1format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute1format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute1 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute1friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute1friendlyname:

      .. rst-class:: ansible-option-title

      **attribute1friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute1friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute1 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute2"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute2:

      .. rst-class:: ansible-option-title

      **attribute2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute2" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute2 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute2expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute2expr:

      .. rst-class:: ansible-option-title

      **attribute2expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute2expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute2's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute2format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute2format:

      .. rst-class:: ansible-option-title

      **attribute2format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute2format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute2 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute2friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute2friendlyname:

      .. rst-class:: ansible-option-title

      **attribute2friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute2friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute2 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute3"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute3:

      .. rst-class:: ansible-option-title

      **attribute3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute3" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute3 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute3expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute3expr:

      .. rst-class:: ansible-option-title

      **attribute3expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute3expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute3's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute3format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute3format:

      .. rst-class:: ansible-option-title

      **attribute3format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute3format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute3 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute3friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute3friendlyname:

      .. rst-class:: ansible-option-title

      **attribute3friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute3friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute3 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute4"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute4:

      .. rst-class:: ansible-option-title

      **attribute4**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute4" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute4 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute4expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute4expr:

      .. rst-class:: ansible-option-title

      **attribute4expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute4expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute4's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute4format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute4format:

      .. rst-class:: ansible-option-title

      **attribute4format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute4format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute4 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute4friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute4friendlyname:

      .. rst-class:: ansible-option-title

      **attribute4friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute4friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute4 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute5"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute5:

      .. rst-class:: ansible-option-title

      **attribute5**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute5" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute5 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute5expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute5expr:

      .. rst-class:: ansible-option-title

      **attribute5expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute5expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute5's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute5format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute5format:

      .. rst-class:: ansible-option-title

      **attribute5format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute5format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute5 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute5friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute5friendlyname:

      .. rst-class:: ansible-option-title

      **attribute5friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute5friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute5 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute6"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute6:

      .. rst-class:: ansible-option-title

      **attribute6**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute6" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute6 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute6expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute6expr:

      .. rst-class:: ansible-option-title

      **attribute6expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute6expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute6's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute6format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute6format:

      .. rst-class:: ansible-option-title

      **attribute6format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute6format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute6 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute6friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute6friendlyname:

      .. rst-class:: ansible-option-title

      **attribute6friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute6friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute6 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute7"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute7:

      .. rst-class:: ansible-option-title

      **attribute7**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute7" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute7 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute7expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute7expr:

      .. rst-class:: ansible-option-title

      **attribute7expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute7expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute7's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute7format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute7format:

      .. rst-class:: ansible-option-title

      **attribute7format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute7format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute7 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute7friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute7friendlyname:

      .. rst-class:: ansible-option-title

      **attribute7friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute7friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute7 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute8"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute8:

      .. rst-class:: ansible-option-title

      **attribute8**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute8" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute8 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute8expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute8expr:

      .. rst-class:: ansible-option-title

      **attribute8expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute8expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute8's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute8format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute8format:

      .. rst-class:: ansible-option-title

      **attribute8format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute8format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute8 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute8friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute8friendlyname:

      .. rst-class:: ansible-option-title

      **attribute8friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute8friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute8 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute9"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute9:

      .. rst-class:: ansible-option-title

      **attribute9**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute9" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of attribute9 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute9expr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute9expr:

      .. rst-class:: ansible-option-title

      **attribute9expr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute9expr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain attribute9's value to be sent in Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute9format"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute9format:

      .. rst-class:: ansible-option-title

      **attribute9format**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute9format" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Attribute9 to be sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"URI"`
      - :ansible-option-choices-entry:`"Basic"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-attribute9friendlyname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-attribute9friendlyname:

      .. rst-class:: ansible-option-title

      **attribute9friendlyname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-attribute9friendlyname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User-Friendly Name of attribute9 that needs to be sent in SAML Assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-audience"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-audience:

      .. rst-class:: ansible-option-title

      **audience**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-audience" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Audience for which assertion sent by IdP is applicable. This is typically entity name or url that represents ServiceProvider


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-digestmethod"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-digestmethod:

      .. rst-class:: ansible-option-title

      **digestmethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-digestmethod" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Algorithm to be used to compute/verify digest for SAML transactions


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SHA1"`
      - :ansible-option-choices-entry-default:`"SHA256"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-encryptassertion"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-encryptassertion:

      .. rst-class:: ansible-option-title

      **encryptassertion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-encryptassertion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to encrypt assertion when Citrix ADC sends one.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-encryptionalgorithm"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-encryptionalgorithm:

      .. rst-class:: ansible-option-title

      **encryptionalgorithm**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-encryptionalgorithm" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Algorithm to be used to encrypt SAML assertion


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"DES3"`
      - :ansible-option-choices-entry:`"AES128"`
      - :ansible-option-choices-entry:`"AES192"`
      - :ansible-option-choices-entry-default:`"AES256"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-instance_name:

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
        <div class="ansibleOptionAnchor" id="parameter-is_cloud"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-is_cloud:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-mas_proxy_call:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-name:

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

      Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an SSO action is created.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nameidexpr"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nameidexpr:

      .. rst-class:: ansible-option-title

      **nameidexpr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nameidexpr" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression that will be evaluated to obtain NameIdentifier to be sent in assertion


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nameidformat"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nameidformat:

      .. rst-class:: ansible-option-title

      **nameidformat**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-nameidformat" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Format of Name Identifier sent in Assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Unspecified"`
      - :ansible-option-choices-entry:`"emailAddress"`
      - :ansible-option-choices-entry:`"X509SubjectName"`
      - :ansible-option-choices-entry:`"WindowsDomainQualifiedName"`
      - :ansible-option-choices-entry:`"kerberos"`
      - :ansible-option-choices-entry:`"entity"`
      - :ansible-option-choices-entry:`"persistent"`
      - :ansible-option-choices-entry-default:`"transient"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-relaystaterule"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-relaystaterule:

      .. rst-class:: ansible-option-title

      **relaystaterule**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-relaystaterule" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expression to extract relaystate to be sent along with assertion. Evaluation of this expression should return TEXT content. This is typically a targ

      et url to which user is redirected after the recipient validates SAML token


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-samlissuername"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-samlissuername:

      .. rst-class:: ansible-option-title

      **samlissuername**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-samlissuername" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name to be used in requests sent from	Citrix ADC to IdP to uniquely identify Citrix ADC.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-samlsigningcertname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-samlsigningcertname:

      .. rst-class:: ansible-option-title

      **samlsigningcertname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-samlsigningcertname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the SSL certificate that is used to Sign Assertion.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-samlspcertname"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-samlspcertname:

      .. rst-class:: ansible-option-title

      **samlspcertname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-samlspcertname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the SSL certificate of peer/receving party using which Assertion is encrypted.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-sendpassword"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-sendpassword:

      .. rst-class:: ansible-option-title

      **sendpassword**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sendpassword" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to send password in assertion.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-signassertion"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-signassertion:

      .. rst-class:: ansible-option-title

      **signassertion**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-signassertion" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to sign portions of assertion when Citrix ADC IDP sends one. Based on the user selection, either Assertion or Response or Both or none can be signed


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NONE"`
      - :ansible-option-choices-entry-default:`"ASSERTION"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"RESPONSE"`
      - :ansible-option-choices-entry:`"BOTH"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-signaturealg"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-signaturealg:

      .. rst-class:: ansible-option-title

      **signaturealg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-signaturealg" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Algorithm to be used to sign/verify SAML transactions


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"RSA-SHA1"`
      - :ansible-option-choices-entry-default:`"RSA-SHA256"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-skewtime"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-skewtime:

      .. rst-class:: ansible-option-title

      **skewtime**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-skewtime" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option specifies the number of minutes on either side of current time that the assertion would be valid. For example, if skewTime is 10, then assertion would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`5`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__parameter-validate_certs:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.tmsamlssoprofile_module__return-loglines:

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

