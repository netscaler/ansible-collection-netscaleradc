
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

.. _ansible_collections.netscaler.adc.vpnsessionaction_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.vpnsessionaction module -- Configuration for VPN session action resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.vpnsessionaction`.

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

- Configuration for VPN session action resource.


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
        <div class="ansibleOptionAnchor" id="parameter-advancedclientlessvpnmode"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-advancedclientlessvpnmode:

      .. rst-class:: ansible-option-title

      **advancedclientlessvpnmode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-advancedclientlessvpnmode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to enable/disable Advanced ClientlessVpnMode. Additionaly, it can be set to STRICT to block Classic ClientlessVpnMode while in AdvancedClientlessMode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"STRICT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allowedlogingroups"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-allowedlogingroups:

      .. rst-class:: ansible-option-title

      **allowedlogingroups**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allowedlogingroups" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify groups that have permission to log on to Citrix Gateway. Users who do not belong to this group or groups are denied access even if they have valid credentials.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-allprotocolproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-allprotocolproxy:

      .. rst-class:: ansible-option-title

      **allprotocolproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allprotocolproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to use for all protocols supported by Citrix Gateway.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-alwaysonprofilename"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-alwaysonprofilename:

      .. rst-class:: ansible-option-title

      **alwaysonprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-alwaysonprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the AlwaysON profile associated with the session action. The builtin profile named none can be used to explicitly disable AlwaysON for the session action.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-api_path:

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
        <div class="ansibleOptionAnchor" id="parameter-authorizationgroup"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-authorizationgroup:

      .. rst-class:: ansible-option-title

      **authorizationgroup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-authorizationgroup" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Comma-separated list of groups in which the user is placed when none of the groups that the user is a part of is configured on Citrix Gateway. The authorization policy can be bound to these groups to control access to the resources.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-autoproxyurl"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-autoproxyurl:

      .. rst-class:: ansible-option-title

      **autoproxyurl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-autoproxyurl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL to auto proxy config file


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-bearer_token"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-citrixreceiverhome"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-citrixreceiverhome:

      .. rst-class:: ansible-option-title

      **citrixreceiverhome**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-citrixreceiverhome" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Web address for the Citrix Receiver home page. Configure Citrix Gateway so that when users log on to the appliance, the Citrix Gateway Plug-in opens a web browser that allows single sign-on to the Citrix Receiver home page.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientchoices"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientchoices:

      .. rst-class:: ansible-option-title

      **clientchoices**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientchoices" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Provide users with multiple logon options. With client choices, users have the option of logging on by using the Citrix Gateway Plug-in for Windows, Citrix Gateway Plug-in for Java, the Web Interface, or clientless access from one location. Depending on how Citrix Gateway is configured, users are presented with up to three icons for logon choices. The most common are the Citrix Gateway Plug-in for Windows, Web Interface, and clientless access.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientcleanupprompt"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientcleanupprompt:

      .. rst-class:: ansible-option-title

      **clientcleanupprompt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientcleanupprompt" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Prompt for client-side cache clean-up when a client-initiated session closes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientconfiguration"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientconfiguration:

      .. rst-class:: ansible-option-title

      **clientconfiguration**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientconfiguration" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow users to change client Debug logging level in Configuration tab of the Citrix Gateway Plug-in for Windows.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"trace"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientdebug"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientdebug:

      .. rst-class:: ansible-option-title

      **clientdebug**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientdebug" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the trace level on Citrix Gateway. Technical support technicians use these debug logs for in-depth debugging and troubleshooting purposes. Available settings function as follows: 

      \* DEBUG - Detailed debug messages are collected and written into the specified file.

      \* STATS - Application audit level error messages and debug statistic counters are written into the specified file. 

      \* EVENTS - Application audit-level error messages are written into the specified file. 

      \* OFF - Only critical events are logged into the Windows Application Log.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"debug"`
      - :ansible-option-choices-entry:`"stats"`
      - :ansible-option-choices-entry:`"events"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientidletimeout"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientidletimeout:

      .. rst-class:: ansible-option-title

      **clientidletimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientidletimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time, in minutes, after which to time out the user session if Citrix Gateway does not detect mouse or keyboard activity.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientlessmodeurlencoding"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientlessmodeurlencoding:

      .. rst-class:: ansible-option-title

      **clientlessmodeurlencoding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientlessmodeurlencoding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When clientless access is enabled, you can choose to encode the addresses of internal web applications or to leave the address as clear text. Available settings function as follows: 

      \* OPAQUE - Use standard encoding mechanisms to make the domain and protocol part of the resource unclear to users. 

      \* CLEAR - Do not encode the web address and make it visible to users. 

      \* ENCRYPT - Allow the domain and protocol to be encrypted using a session key. When the web address is encrypted, the URL is different for each user session for the same web resource. If users bookmark the encoded web address, save it in the web browser and then log off, they cannot connect to the web address when they log on and use the bookmark. If users save the encrypted bookmark in the Access Interface during their session, the bookmark works each time the user logs on.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"TRANSPARENT"`
      - :ansible-option-choices-entry:`"OPAQUE"`
      - :ansible-option-choices-entry:`"ENCRYPT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientlesspersistentcookie"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientlesspersistentcookie:

      .. rst-class:: ansible-option-title

      **clientlesspersistentcookie**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientlesspersistentcookie" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of persistent cookies in clientless access mode. Persistent cookies are required for accessing certain features of SharePoint, such as opening and editing Microsoft Word, Excel, and PowerPoint documents hosted on the SharePoint server. A persistent cookie remains on the user device and is sent with each HTTP request. Citrix Gateway encrypts the persistent cookie before sending it to the plug-in on the user device, and refreshes the cookie periodically as long as the session exists. The cookie becomes stale if the session ends. Available settings function as follows: 

      \* ALLOW - Enable persistent cookies. Users can open and edit Microsoft documents stored in SharePoint. 

      \* DENY - Disable persistent cookies. Users cannot open and edit Microsoft documents stored in SharePoint. 

      \* PROMPT - Prompt users to allow or deny persistent cookies during the session. Persistent cookies are not required for clientless access if users do not connect to SharePoint.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ALLOW"`
      - :ansible-option-choices-entry:`"DENY"`
      - :ansible-option-choices-entry:`"PROMPT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientlessvpnmode"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientlessvpnmode:

      .. rst-class:: ansible-option-title

      **clientlessvpnmode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientlessvpnmode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable clientless access for web, XenApp or XenDesktop, and FileShare resources without installing the Citrix Gateway Plug-in. Available settings function as follows: 

      \* ON - Allow only clientless access. 

      \* OFF - Allow clientless access after users log on with the Citrix Gateway Plug-in. 

      \* DISABLED - Do not allow clientless access.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientoptions"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientoptions:

      .. rst-class:: ansible-option-title

      **clientoptions**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientoptions" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Display only the configured menu options when you select the "Configure Citrix Gateway" option in the Citrix Gateway Plug-in system tray icon for Windows.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"all"`
      - :ansible-option-choices-entry:`"services"`
      - :ansible-option-choices-entry:`"filetransfer"`
      - :ansible-option-choices-entry:`"configuration"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientsecurity"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientsecurity:

      .. rst-class:: ansible-option-title

      **clientsecurity**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientsecurity" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the client security check for the user device to permit a Citrix Gateway session. The web address or IP address is not included in the expression for the client security check.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientsecuritygroup"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientsecuritygroup:

      .. rst-class:: ansible-option-title

      **clientsecuritygroup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientsecuritygroup" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The client security group that will be assigned on failure of the client security check. Users can in general be organized into Groups. In this case, the Client Security Group may have a more restrictive security policy.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientsecuritylog"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientsecuritylog:

      .. rst-class:: ansible-option-title

      **clientsecuritylog**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientsecuritylog" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the logging of client security checks.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientsecuritymessage"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-clientsecuritymessage:

      .. rst-class:: ansible-option-title

      **clientsecuritymessage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientsecuritymessage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The client security message that will be displayed on failure of the client security check.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-defaultauthorizationaction"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-defaultauthorizationaction:

      .. rst-class:: ansible-option-title

      **defaultauthorizationaction**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-defaultauthorizationaction" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the network resources that users have access to when they log on to the internal network. The default setting for authorization is to deny access to all network resources. Citrix recommends using the default global setting and then creating authorization policies to define the network resources users can access. If you set the default authorization policy to DENY, you must explicitly authorize access to any network resource, which improves security.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ALLOW"`
      - :ansible-option-choices-entry:`"DENY"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dnsvservername"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-dnsvservername:

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

      Name of the DNS virtual server for the user session.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-emailhome"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-emailhome:

      .. rst-class:: ansible-option-title

      **emailhome**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-emailhome" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Web address for the web-based email, such as Outlook Web Access.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-epaclienttype"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-epaclienttype:

      .. rst-class:: ansible-option-title

      **epaclienttype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-epaclienttype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Choose between two types of End point Windows Client

      a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed

      b) Activex Control - ActiveX control run by Microsoft Internet Explorer.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AGENT"`
      - :ansible-option-choices-entry:`"PLUGIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-forcecleanup"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-forcecleanup:

      .. rst-class:: ansible-option-title

      **forcecleanup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-forcecleanup" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Force cache clean-up when the user closes a session. You can specify all, none, or any combination of the client-side items.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"none"`
      - :ansible-option-choices-entry:`"all"`
      - :ansible-option-choices-entry:`"cookie"`
      - :ansible-option-choices-entry:`"addressbar"`
      - :ansible-option-choices-entry:`"plugin"`
      - :ansible-option-choices-entry:`"filesystemapplication"`
      - :ansible-option-choices-entry:`"application"`
      - :ansible-option-choices-entry:`"applicationdata"`
      - :ansible-option-choices-entry:`"clientcertificate"`
      - :ansible-option-choices-entry:`"autocomplete"`
      - :ansible-option-choices-entry:`"cache"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-forcedtimeout"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-forcedtimeout:

      .. rst-class:: ansible-option-title

      **forcedtimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-forcedtimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Force a disconnection from the Citrix Gateway Plug-in with Citrix Gateway after a specified number of minutes. If the session closes, the user must log on again.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-forcedtimeoutwarning"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-forcedtimeoutwarning:

      .. rst-class:: ansible-option-title

      **forcedtimeoutwarning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-forcedtimeoutwarning" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of minutes to warn a user before the user session is disconnected.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-fqdnspoofedip"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-fqdnspoofedip:

      .. rst-class:: ansible-option-title

      **fqdnspoofedip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-fqdnspoofedip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Spoofed IP address range that can be used by client for FQDN based split tunneling


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ftpproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-ftpproxy:

      .. rst-class:: ansible-option-title

      **ftpproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ftpproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to be used for FTP access for all subsequent connections to the internal network.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-gopherproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-gopherproxy:

      .. rst-class:: ansible-option-title

      **gopherproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-gopherproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to be used for GOPHER access for all subsequent connections to the internal network.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-homepage"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-homepage:

      .. rst-class:: ansible-option-title

      **homepage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-homepage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Web address of the home page that appears when users log on. Otherwise, users receive the default home page for Citrix Gateway, which is the Access Interface.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httpport"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-httpport:

      .. rst-class:: ansible-option-title

      **httpport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-httpport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Destination port numbers other than port 80, added as a comma-separated list. Traffic to these ports is processed as HTTP traffic, which allows functionality, such as HTTP authorization and single sign-on to a web application to work.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-httpproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-httpproxy:

      .. rst-class:: ansible-option-title

      **httpproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-httpproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to be used for HTTP access for all subsequent connections to the internal network.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-icaproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-icaproxy:

      .. rst-class:: ansible-option-title

      **icaproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-icaproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable ICA proxy to configure secure Internet access to servers running Citrix XenApp or XenDesktop by using Citrix Receiver instead of the Citrix Gateway Plug-in.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-iconwithreceiver"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-iconwithreceiver:

      .. rst-class:: ansible-option-title

      **iconwithreceiver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-iconwithreceiver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to decide whether to show plugin icon along with receiver


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-iipdnssuffix"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-iipdnssuffix:

      .. rst-class:: ansible-option-title

      **iipdnssuffix**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-iipdnssuffix" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      An intranet IP DNS suffix. When a user logs on to Citrix Gateway and is assigned an IP address, a DNS record for the user name and IP address combination is added to the Citrix Gateway DNS cache. You can configure a DNS suffix to append to the user name when the DNS record is added to the cache. You can reach to the host from where the user is logged on by using the user's name, which can be easier to remember than an IP address. When the user logs off from Citrix Gateway, the record is removed from the DNS cache.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-instance_name:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-is_cloud:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-kcdaccount:

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

      The kcd account details to be used in SSO


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-killconnections"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-killconnections:

      .. rst-class:: ansible-option-title

      **killconnections**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-killconnections" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify whether the Citrix Gateway Plug-in should disconnect all preexisting connections, such as the connections existing before the user logged on to Citrix Gateway, and prevent new incoming connections on the Citrix Gateway Plug-in for Windows and MAC when the user is connected to Citrix Gateway and split tunneling is disabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-linuxpluginupgrade"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-linuxpluginupgrade:

      .. rst-class:: ansible-option-title

      **linuxpluginupgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-linuxpluginupgrade" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to set plugin upgrade behaviour for Linux


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Always"`
      - :ansible-option-choices-entry:`"Essential"`
      - :ansible-option-choices-entry:`"Never"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-locallanaccess"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-locallanaccess:

      .. rst-class:: ansible-option-title

      **locallanaccess**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-locallanaccess" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set local LAN access. If split tunneling is OFF, and you set local LAN access to ON, the local client can route traffic to its local interface. When the local area network switch is specified, this combination of switches is useful. The client can allow local LAN access to devices that commonly have non-routable addresses, such as local printers or local file servers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"FORCED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-loginscript"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-loginscript:

      .. rst-class:: ansible-option-title

      **loginscript**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-loginscript" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to the logon script that is run when a session is established. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logoutscript"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-logoutscript:

      .. rst-class:: ansible-option-title

      **logoutscript**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logoutscript" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to the logout script. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-macpluginupgrade"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-macpluginupgrade:

      .. rst-class:: ansible-option-title

      **macpluginupgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-macpluginupgrade" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to set plugin upgrade behaviour for Mac


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Always"`
      - :ansible-option-choices-entry:`"Essential"`
      - :ansible-option-choices-entry:`"Never"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mas_proxy_call"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-mas_proxy_call:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-name:

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

      Name for the Citrix Gateway profile (action). Must begin with an ASCII alphabetic or underscore (\_) character, and must consist only of ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.

      

      The following requirement applies only to the Citrix ADC CLI:

      If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-netmask"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-netmask:

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

      The netmask for the spoofed ip address


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-ntdomain"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-ntdomain:

      .. rst-class:: ansible-option-title

      **ntdomain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ntdomain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Single sign-on domain to use for single sign-on to applications in the internal network. This setting can be overwritten by the domain that users specify at the time of logon or by the domain that the authentication server returns.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pcoipprofilename"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-pcoipprofilename:

      .. rst-class:: ansible-option-title

      **pcoipprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pcoipprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the PCOIP profile associated with the session action. The builtin profile named none can be used to explicitly disable PCOIP for the session action.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-proxy:

      .. rst-class:: ansible-option-title

      **proxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set options to apply proxy for accessing the internal resources. Available settings function as follows:

      \* BROWSER - Proxy settings are configured only in Internet Explorer and Firefox browsers.

      \* NS - Proxy settings are configured on the Citrix ADC.

      \* OFF - Proxy settings are not configured.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"BROWSER"`
      - :ansible-option-choices-entry:`"NS"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxyexception"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-proxyexception:

      .. rst-class:: ansible-option-title

      **proxyexception**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxyexception" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Proxy exception string that will be configured in the browser for bypassing the previously configured proxies. Allowed only if proxy type is Browser.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxylocalbypass"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-proxylocalbypass:

      .. rst-class:: ansible-option-title

      **proxylocalbypass**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxylocalbypass" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bypass proxy server for local addresses option in Internet Explorer and Firefox proxy server settings.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rdpclientprofilename"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-rdpclientprofilename:

      .. rst-class:: ansible-option-title

      **rdpclientprofilename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rdpclientprofilename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the RDP profile associated with the vserver.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rfc1918"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-rfc1918:

      .. rst-class:: ansible-option-title

      **rfc1918**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rfc1918" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      As defined in the local area network, allow only the following local area network addresses to bypass the VPN tunnel when the local LAN access feature is enabled:

      \* 10.\*.\*.\*,

      \* 172.16.\*.\*,

      \* 192.168.\*.\*


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-securebrowse"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-securebrowse:

      .. rst-class:: ansible-option-title

      **securebrowse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-securebrowse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow users to connect through Citrix Gateway to network resources from iOS and Android mobile devices with Citrix Receiver. Users do not need to establish a full VPN tunnel to access resources in the secure network.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sesstimeout"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-sesstimeout:

      .. rst-class:: ansible-option-title

      **sesstimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sesstimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of minutes after which the session times out.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sfgatewayauthtype"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-sfgatewayauthtype:

      .. rst-class:: ansible-option-title

      **sfgatewayauthtype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sfgatewayauthtype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The authentication type configured for the Citrix Gateway on StoreFront.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"domain"`
      - :ansible-option-choices-entry:`"RSA"`
      - :ansible-option-choices-entry:`"domainAndRSA"`
      - :ansible-option-choices-entry:`"SMS"`
      - :ansible-option-choices-entry:`"smartCard"`
      - :ansible-option-choices-entry:`"sfAuth"`
      - :ansible-option-choices-entry:`"sfAuthAndRSA"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smartgroup"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-smartgroup:

      .. rst-class:: ansible-option-title

      **smartgroup**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smartgroup" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This is the default group that is chosen when the authentication succeeds in addition to extracted groups.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-socksproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-socksproxy:

      .. rst-class:: ansible-option-title

      **socksproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-socksproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to be used for SOCKS access for all subsequent connections to the internal network.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-splitdns"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-splitdns:

      .. rst-class:: ansible-option-title

      **splitdns**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-splitdns" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Route the DNS requests to the local DNS server configured on the user device, or Citrix Gateway (remote), or both.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"LOCAL"`
      - :ansible-option-choices-entry:`"REMOTE"`
      - :ansible-option-choices-entry:`"BOTH"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-splittunnel"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-splittunnel:

      .. rst-class:: ansible-option-title

      **splittunnel**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-splittunnel" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Send, through the tunnel, traffic only for intranet applications that are defined in Citrix Gateway. Route all other traffic directly to the Internet. The OFF setting routes all traffic through Citrix Gateway. With the REVERSE setting, intranet applications define the network traffic that is not intercepted. All network traffic directed to internal IP addresses bypasses the VPN tunnel, while other traffic goes through Citrix Gateway. Reverse split tunneling can be used to log all non-local LAN traffic. For example, if users have a home network and are logged on through the Citrix Gateway Plug-in, network traffic destined to a printer or another device within the home network is not intercepted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"REVERSE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-spoofiip"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-spoofiip:

      .. rst-class:: ansible-option-title

      **spoofiip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-spoofiip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address that the intranet application uses to route the connection through the virtual adapter.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslproxy"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-sslproxy:

      .. rst-class:: ansible-option-title

      **sslproxy**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslproxy" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      IP address of the proxy server to be used for SSL access for all subsequent connections to the internal network.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sso"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-sso:

      .. rst-class:: ansible-option-title

      **sso**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sso" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set single sign-on (SSO) for the session. When the user accesses a server, the user's logon credentials are passed to the server for authentication.

      	    NOTE : This configuration does not honor the following authentication types for security reason. BASIC, DIGEST, and NTLM (without Negotiate NTLM2 Key or Negotiate Sign Flag). Use VPN TrafficAction to configure SSO for these authentication types.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ssocredential"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-ssocredential:

      .. rst-class:: ansible-option-title

      **ssocredential**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ssocredential" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify whether to use the primary or secondary authentication credentials for single sign-on to the server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"PRIMARY"`
      - :ansible-option-choices-entry:`"SECONDARY"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-storefronturl"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-storefronturl:

      .. rst-class:: ansible-option-title

      **storefronturl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-storefronturl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Web address for StoreFront to be used in this session for enumeration of resources from XenApp or XenDesktop.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-transparentinterception"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-transparentinterception:

      .. rst-class:: ansible-option-title

      **transparentinterception**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-transparentinterception" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Allow access to network resources by using a single IP address and subnet mask or a range of IP addresses. The OFF setting sets the mode to proxy, in which you configure destination and source IP addresses and port numbers. If you are using the Citrix Gateway Plug-in for Windows, set this parameter to ON, in which the mode is set to transparent. If you are using the Citrix Gateway Plug-in for Java, set this parameter to OFF.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-useiip"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-useiip:

      .. rst-class:: ansible-option-title

      **useiip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-useiip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define IP address pool options. Available settings function as follows: 

      \* SPILLOVER - When an address pool is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned. 

      \* NOSPILLOVER - When intranet IP addresses are enabled and the mapped IP address is not used, the Transfer Login page appears for users who have used all available intranet IP addresses. 

      \* OFF - Address pool is not configured.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NOSPILLOVER"`
      - :ansible-option-choices-entry:`"SPILLOVER"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-usemip"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-usemip:

      .. rst-class:: ansible-option-title

      **usemip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-usemip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable the use of a unique IP address alias, or a mapped IP address, as the client IP address for each client session. Allow Citrix Gateway to use the mapped IP address as an intranet IP address when all other IP addresses are not available. 

      When IP pooling is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NS"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-useraccounting"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-useraccounting:

      .. rst-class:: ansible-option-title

      **useraccounting**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-useraccounting" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the radiusPolicy to use for RADIUS user accounting info on the session.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-validate_certs:

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
        <div class="ansibleOptionAnchor" id="parameter-wihome"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-wihome:

      .. rst-class:: ansible-option-title

      **wihome**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wihome" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Web address of the Web Interface server, such as http://\<ipAddress\>/Citrix/XenApp, or Receiver for Web, which enumerates the virtualized resources, such as XenApp, XenDesktop, and cloud applications. This web address is used as the home page in ICA proxy mode. 

      If Client Choices is ON, you must configure this setting. Because the user can choose between FullClient and ICAProxy, the user may see a different home page. An Internet web site may appear if the user gets the FullClient option, or a Web Interface site if the user gets the ICAProxy option. If the setting is not configured, the XenApp option does not appear as a client choice.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wihomeaddresstype"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-wihomeaddresstype:

      .. rst-class:: ansible-option-title

      **wihomeaddresstype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wihomeaddresstype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of the wihome address(IPV4/V6)


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"IPV4"`
      - :ansible-option-choices-entry:`"IPV6"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-windowsautologon"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-windowsautologon:

      .. rst-class:: ansible-option-title

      **windowsautologon**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-windowsautologon" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable the Windows Auto Logon for the session. If a VPN session is established after this setting is enabled, the user is automatically logged on by using Windows credentials after the system is restarted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-windowsclienttype"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-windowsclienttype:

      .. rst-class:: ansible-option-title

      **windowsclienttype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-windowsclienttype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Choose between two types of Windows Client\\

      a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed\\

      b) Activex Control - ActiveX control run by Microsoft Internet Explorer.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AGENT"`
      - :ansible-option-choices-entry:`"PLUGIN"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-windowspluginupgrade"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-windowspluginupgrade:

      .. rst-class:: ansible-option-title

      **windowspluginupgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-windowspluginupgrade" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Option to set plugin upgrade behaviour for Win


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Always"`
      - :ansible-option-choices-entry:`"Essential"`
      - :ansible-option-choices-entry:`"Never"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-winsip"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-winsip:

      .. rst-class:: ansible-option-title

      **winsip**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-winsip" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      WINS server IP address to add to Citrix Gateway for name resolution.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-wiportalmode"></div>

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__parameter-wiportalmode:

      .. rst-class:: ansible-option-title

      **wiportalmode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-wiportalmode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Layout on the Access Interface. The COMPACT value indicates the use of small icons.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"NORMAL"`
      - :ansible-option-choices-entry:`"COMPACT"`


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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.vpnsessionaction_module__return-loglines:

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

