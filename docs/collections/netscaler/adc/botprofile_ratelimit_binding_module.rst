
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

.. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.botprofile_ratelimit_binding module -- Binding Resource definition for describing association between botprofile and ratelimit resources
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.botprofile_ratelimit_binding`.

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

- Binding Resource definition for describing association between botprofile and ratelimit resources


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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-api_path:

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
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-bot_bind_comment"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_bind_comment:

      .. rst-class:: ansible-option-title

      **bot_bind_comment**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_bind_comment" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Any comments about this binding.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bot_rate_limit_action"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_rate_limit_action:

      .. rst-class:: ansible-option-title

      **bot_rate_limit_action**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_rate_limit_action" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      One or more actions to be taken when the current rate becomes more than the configured rate. Only \ :literal:`LOG`\  action can be combined with \ :literal:`DROP`\ , \ :literal:`REDIRECT`\  or \ :literal:`RESET`\  action.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"NONE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"LOG"`
      - :ansible-option-choices-entry:`"DROP"`
      - :ansible-option-choices-entry:`"REDIRECT"`
      - :ansible-option-choices-entry:`"RESET"`


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`["NONE"]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bot_rate_limit_enabled"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_rate_limit_enabled:

      .. rst-class:: ansible-option-title

      **bot_rate_limit_enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_rate_limit_enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable rate-limit binding.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bot_rate_limit_type"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_rate_limit_type:

      .. rst-class:: ansible-option-title

      **bot_rate_limit_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_rate_limit_type" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rate-limiting type Following rate-limiting types are allowed:

      \*\ :literal:`SOURCE\_IP`\  - Rate-limiting based on the client IP.

      \*\ :literal:`SESSION`\  - Rate-limiting based on the configured cookie name.

      \*\ :literal:`URL`\  - Rate-limiting based on the configured \ :literal:`URL`\ .

      \*\ :literal:`GEOLOCATION`\  - Rate-limiting based on the configured country name.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"SESSION"`
      - :ansible-option-choices-entry:`"SOURCE\_IP"`
      - :ansible-option-choices-entry:`"URL"`
      - :ansible-option-choices-entry:`"GEOLOCATION"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bot_rate_limit_url"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_rate_limit_url:

      .. rst-class:: ansible-option-title

      **bot_rate_limit_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_rate_limit_url" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL for the resource based rate-limiting.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bot_ratelimit"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-bot_ratelimit:

      .. rst-class:: ansible-option-title

      **bot_ratelimit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-bot_ratelimit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Rate-limit binding. Maximum 30 bindings can be configured per profile for rate-limit detection. For SOURCE\_IP type, only one binding can be configured, and for URL type, only one binding is allowed per URL, and for SESSION type, only one binding is allowed for a cookie name. To update the values of an existing binding, user has to first unbind that binding, and then needs to bind again with new values.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cookiename"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-cookiename:

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

      Cookie name which is used to identify the session for session rate-limiting.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-countrycode"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-countrycode:

      .. rst-class:: ansible-option-title

      **countrycode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-countrycode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Country name which is used for geolocation rate-limiting.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AF"`
      - :ansible-option-choices-entry:`"AX"`
      - :ansible-option-choices-entry:`"AL"`
      - :ansible-option-choices-entry:`"DZ"`
      - :ansible-option-choices-entry:`"AS"`
      - :ansible-option-choices-entry:`"AD"`
      - :ansible-option-choices-entry:`"AO"`
      - :ansible-option-choices-entry:`"AI"`
      - :ansible-option-choices-entry:`"AQ"`
      - :ansible-option-choices-entry:`"AG"`
      - :ansible-option-choices-entry:`"AR"`
      - :ansible-option-choices-entry:`"AM"`
      - :ansible-option-choices-entry:`"AW"`
      - :ansible-option-choices-entry:`"AU"`
      - :ansible-option-choices-entry:`"AT"`
      - :ansible-option-choices-entry:`"AZ"`
      - :ansible-option-choices-entry:`"BS"`
      - :ansible-option-choices-entry:`"BH"`
      - :ansible-option-choices-entry:`"BD"`
      - :ansible-option-choices-entry:`"BB"`
      - :ansible-option-choices-entry:`"BY"`
      - :ansible-option-choices-entry:`"BE"`
      - :ansible-option-choices-entry:`"BZ"`
      - :ansible-option-choices-entry:`"BJ"`
      - :ansible-option-choices-entry:`"BM"`
      - :ansible-option-choices-entry:`"BT"`
      - :ansible-option-choices-entry:`"BO"`
      - :ansible-option-choices-entry:`"BQ"`
      - :ansible-option-choices-entry:`"BA"`
      - :ansible-option-choices-entry:`"BW"`
      - :ansible-option-choices-entry:`"BR"`
      - :ansible-option-choices-entry:`"IO"`
      - :ansible-option-choices-entry:`"BN"`
      - :ansible-option-choices-entry:`"BG"`
      - :ansible-option-choices-entry:`"BF"`
      - :ansible-option-choices-entry:`"BI"`
      - :ansible-option-choices-entry:`"KH"`
      - :ansible-option-choices-entry:`"CM"`
      - :ansible-option-choices-entry:`"CA"`
      - :ansible-option-choices-entry:`"CV"`
      - :ansible-option-choices-entry:`"KY"`
      - :ansible-option-choices-entry:`"CF"`
      - :ansible-option-choices-entry:`"TD"`
      - :ansible-option-choices-entry:`"CL"`
      - :ansible-option-choices-entry:`"CN"`
      - :ansible-option-choices-entry:`"CX"`
      - :ansible-option-choices-entry:`"CC"`
      - :ansible-option-choices-entry:`"CO"`
      - :ansible-option-choices-entry:`"KM"`
      - :ansible-option-choices-entry:`"CG"`
      - :ansible-option-choices-entry:`"CD"`
      - :ansible-option-choices-entry:`"CK"`
      - :ansible-option-choices-entry:`"CR"`
      - :ansible-option-choices-entry:`"CI"`
      - :ansible-option-choices-entry:`"HR"`
      - :ansible-option-choices-entry:`"CU"`
      - :ansible-option-choices-entry:`"CW"`
      - :ansible-option-choices-entry:`"CY"`
      - :ansible-option-choices-entry:`"CZ"`
      - :ansible-option-choices-entry:`"DK"`
      - :ansible-option-choices-entry:`"DJ"`
      - :ansible-option-choices-entry:`"DM"`
      - :ansible-option-choices-entry:`"DO"`
      - :ansible-option-choices-entry:`"EC"`
      - :ansible-option-choices-entry:`"EG"`
      - :ansible-option-choices-entry:`"SV"`
      - :ansible-option-choices-entry:`"GQ"`
      - :ansible-option-choices-entry:`"ER"`
      - :ansible-option-choices-entry:`"EE"`
      - :ansible-option-choices-entry:`"ET"`
      - :ansible-option-choices-entry:`"FK"`
      - :ansible-option-choices-entry:`"FO"`
      - :ansible-option-choices-entry:`"FJ"`
      - :ansible-option-choices-entry:`"FI"`
      - :ansible-option-choices-entry:`"FR"`
      - :ansible-option-choices-entry:`"GF"`
      - :ansible-option-choices-entry:`"PF"`
      - :ansible-option-choices-entry:`"TF"`
      - :ansible-option-choices-entry:`"GA"`
      - :ansible-option-choices-entry:`"GM"`
      - :ansible-option-choices-entry:`"GE"`
      - :ansible-option-choices-entry:`"DE"`
      - :ansible-option-choices-entry:`"GH"`
      - :ansible-option-choices-entry:`"GI"`
      - :ansible-option-choices-entry:`"GR"`
      - :ansible-option-choices-entry:`"GL"`
      - :ansible-option-choices-entry:`"GD"`
      - :ansible-option-choices-entry:`"GP"`
      - :ansible-option-choices-entry:`"GU"`
      - :ansible-option-choices-entry:`"GT"`
      - :ansible-option-choices-entry:`"GG"`
      - :ansible-option-choices-entry:`"GN"`
      - :ansible-option-choices-entry:`"GW"`
      - :ansible-option-choices-entry:`"GY"`
      - :ansible-option-choices-entry:`"HT"`
      - :ansible-option-choices-entry:`"HM"`
      - :ansible-option-choices-entry:`"VA"`
      - :ansible-option-choices-entry:`"HN"`
      - :ansible-option-choices-entry:`"HK"`
      - :ansible-option-choices-entry:`"HU"`
      - :ansible-option-choices-entry:`"IS"`
      - :ansible-option-choices-entry:`"IN"`
      - :ansible-option-choices-entry:`"ID"`
      - :ansible-option-choices-entry:`"IR"`
      - :ansible-option-choices-entry:`"IQ"`
      - :ansible-option-choices-entry:`"IE"`
      - :ansible-option-choices-entry:`"IM"`
      - :ansible-option-choices-entry:`"IL"`
      - :ansible-option-choices-entry:`"IT"`
      - :ansible-option-choices-entry:`"JM"`
      - :ansible-option-choices-entry:`"JP"`
      - :ansible-option-choices-entry:`"JE"`
      - :ansible-option-choices-entry:`"JO"`
      - :ansible-option-choices-entry:`"KZ"`
      - :ansible-option-choices-entry:`"KE"`
      - :ansible-option-choices-entry:`"KI"`
      - :ansible-option-choices-entry:`"XK"`
      - :ansible-option-choices-entry:`"KW"`
      - :ansible-option-choices-entry:`"KG"`
      - :ansible-option-choices-entry:`"LA"`
      - :ansible-option-choices-entry:`"LV"`
      - :ansible-option-choices-entry:`"LB"`
      - :ansible-option-choices-entry:`"LS"`
      - :ansible-option-choices-entry:`"LR"`
      - :ansible-option-choices-entry:`"LY"`
      - :ansible-option-choices-entry:`"LI"`
      - :ansible-option-choices-entry:`"LT"`
      - :ansible-option-choices-entry:`"LU"`
      - :ansible-option-choices-entry:`"MO"`
      - :ansible-option-choices-entry:`"MK"`
      - :ansible-option-choices-entry:`"MG"`
      - :ansible-option-choices-entry:`"MW"`
      - :ansible-option-choices-entry:`"MY"`
      - :ansible-option-choices-entry:`"MV"`
      - :ansible-option-choices-entry:`"ML"`
      - :ansible-option-choices-entry:`"MT"`
      - :ansible-option-choices-entry:`"MH"`
      - :ansible-option-choices-entry:`"MQ"`
      - :ansible-option-choices-entry:`"MR"`
      - :ansible-option-choices-entry:`"MU"`
      - :ansible-option-choices-entry:`"YT"`
      - :ansible-option-choices-entry:`"MX"`
      - :ansible-option-choices-entry:`"FM"`
      - :ansible-option-choices-entry:`"MD"`
      - :ansible-option-choices-entry:`"MC"`
      - :ansible-option-choices-entry:`"MN"`
      - :ansible-option-choices-entry:`"ME"`
      - :ansible-option-choices-entry:`"MS"`
      - :ansible-option-choices-entry:`"MA"`
      - :ansible-option-choices-entry:`"MZ"`
      - :ansible-option-choices-entry:`"MM"`
      - :ansible-option-choices-entry:`"NA"`
      - :ansible-option-choices-entry:`"NR"`
      - :ansible-option-choices-entry:`"NP"`
      - :ansible-option-choices-entry:`"NL"`
      - :ansible-option-choices-entry:`"NC"`
      - :ansible-option-choices-entry:`"NZ"`
      - :ansible-option-choices-entry:`"NI"`
      - :ansible-option-choices-entry:`"NE"`
      - :ansible-option-choices-entry:`"NG"`
      - :ansible-option-choices-entry:`"NU"`
      - :ansible-option-choices-entry:`"NF"`
      - :ansible-option-choices-entry:`"KP"`
      - :ansible-option-choices-entry:`"MP"`
      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"OM"`
      - :ansible-option-choices-entry:`"PK"`
      - :ansible-option-choices-entry:`"PW"`
      - :ansible-option-choices-entry:`"PS"`
      - :ansible-option-choices-entry:`"PA"`
      - :ansible-option-choices-entry:`"PG"`
      - :ansible-option-choices-entry:`"PY"`
      - :ansible-option-choices-entry:`"PE"`
      - :ansible-option-choices-entry:`"PH"`
      - :ansible-option-choices-entry:`"PN"`
      - :ansible-option-choices-entry:`"PL"`
      - :ansible-option-choices-entry:`"PT"`
      - :ansible-option-choices-entry:`"PR"`
      - :ansible-option-choices-entry:`"QA"`
      - :ansible-option-choices-entry:`"RE"`
      - :ansible-option-choices-entry:`"RO"`
      - :ansible-option-choices-entry:`"RU"`
      - :ansible-option-choices-entry:`"RW"`
      - :ansible-option-choices-entry:`"BL"`
      - :ansible-option-choices-entry:`"SH"`
      - :ansible-option-choices-entry:`"KN"`
      - :ansible-option-choices-entry:`"LC"`
      - :ansible-option-choices-entry:`"MF"`
      - :ansible-option-choices-entry:`"PM"`
      - :ansible-option-choices-entry:`"VC"`
      - :ansible-option-choices-entry:`"WS"`
      - :ansible-option-choices-entry:`"SM"`
      - :ansible-option-choices-entry:`"ST"`
      - :ansible-option-choices-entry:`"SA"`
      - :ansible-option-choices-entry:`"SN"`
      - :ansible-option-choices-entry:`"RS"`
      - :ansible-option-choices-entry:`"SC"`
      - :ansible-option-choices-entry:`"SL"`
      - :ansible-option-choices-entry:`"SG"`
      - :ansible-option-choices-entry:`"SX"`
      - :ansible-option-choices-entry:`"SK"`
      - :ansible-option-choices-entry:`"SI"`
      - :ansible-option-choices-entry:`"SB"`
      - :ansible-option-choices-entry:`"SO"`
      - :ansible-option-choices-entry:`"SZA"`
      - :ansible-option-choices-entry:`"GS"`
      - :ansible-option-choices-entry:`"KR"`
      - :ansible-option-choices-entry:`"SS"`
      - :ansible-option-choices-entry:`"ES"`
      - :ansible-option-choices-entry:`"LK"`
      - :ansible-option-choices-entry:`"SD"`
      - :ansible-option-choices-entry:`"SR"`
      - :ansible-option-choices-entry:`"SJ"`
      - :ansible-option-choices-entry:`"SZ"`
      - :ansible-option-choices-entry:`"SE"`
      - :ansible-option-choices-entry:`"CH"`
      - :ansible-option-choices-entry:`"SY"`
      - :ansible-option-choices-entry:`"TW"`
      - :ansible-option-choices-entry:`"TJ"`
      - :ansible-option-choices-entry:`"TZ"`
      - :ansible-option-choices-entry:`"TH"`
      - :ansible-option-choices-entry:`"TL"`
      - :ansible-option-choices-entry:`"TG"`
      - :ansible-option-choices-entry:`"TK"`
      - :ansible-option-choices-entry:`"TO"`
      - :ansible-option-choices-entry:`"TT"`
      - :ansible-option-choices-entry:`"TN"`
      - :ansible-option-choices-entry:`"TR"`
      - :ansible-option-choices-entry:`"TM"`
      - :ansible-option-choices-entry:`"TC"`
      - :ansible-option-choices-entry:`"TV"`
      - :ansible-option-choices-entry:`"UG"`
      - :ansible-option-choices-entry:`"UA"`
      - :ansible-option-choices-entry:`"AE"`
      - :ansible-option-choices-entry:`"GB"`
      - :ansible-option-choices-entry:`"US"`
      - :ansible-option-choices-entry:`"UM"`
      - :ansible-option-choices-entry:`"UY"`
      - :ansible-option-choices-entry:`"UZ"`
      - :ansible-option-choices-entry:`"VU"`
      - :ansible-option-choices-entry:`"VE"`
      - :ansible-option-choices-entry:`"VN"`
      - :ansible-option-choices-entry:`"VG"`
      - :ansible-option-choices-entry:`"VI"`
      - :ansible-option-choices-entry:`"WF"`
      - :ansible-option-choices-entry:`"EH"`
      - :ansible-option-choices-entry:`"YE"`
      - :ansible-option-choices-entry:`"ZM"`
      - :ansible-option-choices-entry:`"ZW"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-instance_name:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-is_cloud:

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
        <div class="ansibleOptionAnchor" id="parameter-logmessage"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-logmessage:

      .. rst-class:: ansible-option-title

      **logmessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logmessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Message to be logged for this binding.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-mas_proxy_call:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-name:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-rate"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-rate:

      .. rst-class:: ansible-option-title

      **rate**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rate" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum number of requests that are allowed in this session in the given period time.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-timeslice"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-timeslice:

      .. rst-class:: ansible-option-title

      **timeslice**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-timeslice" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time interval during which requests are tracked to check if they cross the given rate.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__parameter-validate_certs:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.botprofile_ratelimit_binding_module__return-loglines:

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

