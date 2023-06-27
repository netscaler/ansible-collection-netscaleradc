
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

.. _ansible_collections.netscaler.adc.sslprofile_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

netscaler.adc.sslprofile module -- Configuration for SSL profile resource.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `netscaler.adc collection <https://galaxy.ansible.com/netscaler/adc>`_ (version 2.0.0-alpha).

    To install it, use: :code:`ansible-galaxy collection install netscaler.adc`.

    To use it in a playbook, specify: :code:`netscaler.adc.sslprofile`.

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

- Configuration for SSL profile resource.


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
        <div class="ansibleOptionAnchor" id="parameter-allowextendedmastersecret"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-allowextendedmastersecret:

      .. rst-class:: ansible-option-title

      **allowextendedmastersecret**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-allowextendedmastersecret" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      When set to YES, attempt to use the TLS Extended Master Secret (EMS, as

      described in RFC 7627) when negotiating TLS 1.0, TLS 1.1 and TLS 1.2

      connection parameters. EMS must be supported by both the TLS client and server

      in order to be enabled during a handshake. This setting applies to both

      frontend and backend SSL profiles.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-alpnprotocol"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-alpnprotocol:

      .. rst-class:: ansible-option-title

      **alpnprotocol**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-alpnprotocol" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Application protocol supported by the server and used in negotiation of the protocol with the client. Possible values are \ :literal:`HTTP1.1`\ , \ :literal:`HTTP2`\  and \ :literal:`NONE`\ . Default value is \ :literal:`NONE`\  which implies application protocol is not enabled hence remain unknown to the TLS layer. This parameter is relevant only if SSL connection is handled by the virtual server of the type SSL\_TCP.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"NONE"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"HTTP1.1"`
      - :ansible-option-choices-entry:`"HTTP2"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-api_path"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-api_path:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-bearer_token:

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
        <div class="ansibleOptionAnchor" id="parameter-ciphername"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ciphername:

      .. rst-class:: ansible-option-title

      **ciphername**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ciphername" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The cipher group/alias/individual cipher configuration


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cipherpriority"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-cipherpriority:

      .. rst-class:: ansible-option-title

      **cipherpriority**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cipherpriority" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      cipher priority


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cipherredirect"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-cipherredirect:

      .. rst-class:: ansible-option-title

      **cipherredirect**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cipherredirect" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of Cipher Redirect. If this parameter is set to \ :literal:`ENABLED`\ , you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.

      This parameter is not applicable when configuring a backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cipherurl"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-cipherurl:

      .. rst-class:: ansible-option-title

      **cipherurl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cipherurl" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The redirect URL to be used with the Cipher Redirect feature.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cleartextport"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-cleartextport:

      .. rst-class:: ansible-option-title

      **cleartextport**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cleartextport" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientauth"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-clientauth:

      .. rst-class:: ansible-option-title

      **clientauth**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientauth" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate.

      This parameter is not applicable when configuring a backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientauthuseboundcachain"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-clientauthuseboundcachain:

      .. rst-class:: ansible-option-title

      **clientauthuseboundcachain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientauthuseboundcachain" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Certficates bound on the VIP are used for validating the client cert. Certficates came along with client cert are not used for validating the client cert


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-clientcert"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-clientcert:

      .. rst-class:: ansible-option-title

      **clientcert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-clientcert" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The rule for client certificate requirement in client authentication.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Mandatory"`
      - :ansible-option-choices-entry:`"Optional"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-commonname"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-commonname:

      .. rst-class:: ansible-option-title

      **commonname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-commonname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-denysslreneg"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-denysslreneg:

      .. rst-class:: ansible-option-title

      **denysslreneg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-denysslreneg" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Deny renegotiation in specified circumstances. Available settings function as follows:

      \* NO - Allow SSL renegotiation.

      \* FRONTEND\_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.

      \* FRONTEND\_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the Citrix ADC during policy-based client authentication.

      \* ALL - Deny all secure and nonsecure SSL renegotiation.

      \* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry:`"FRONTEND\_CLIENT"`
      - :ansible-option-choices-entry:`"FRONTEND\_CLIENTSERVER"`
      - :ansible-option-choices-entry-default:`"ALL"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"NONSECURE"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dh"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dh:

      .. rst-class:: ansible-option-title

      **dh**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dh" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of Diffie-Hellman (DH) key exchange.

      This parameter is not applicable when configuring a backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dhcount"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dhcount:

      .. rst-class:: ansible-option-title

      **dhcount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dhcount" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of interactions, between the client and the Citrix ADC, after which the DH private-public pair is regenerated. A value of zero (0) specifies refresh every time.

      This parameter is not applicable when configuring a backend profile. Allowed DH count values are 0 and \>= 500.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dhekeyexchangewithpsk"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dhekeyexchangewithpsk:

      .. rst-class:: ansible-option-title

      **dhekeyexchangewithpsk**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dhekeyexchangewithpsk" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether or not the SSL Virtual Server will require a DHE key exchange to occur when a PSK is accepted during a TLS 1.3 resumption handshake.

      A DHE key exchange ensures forward secrecy even in the event that ticket keys are compromised, at the expense of an additional round trip and resources required to carry out the DHE key exchange.

      If disabled, a DHE key exchange will be performed when a PSK is accepted but only if requested by the client.

      If enabled, the server will require a DHE key exchange when a PSK is accepted regardless of whether the client supports combined PSK-DHE key exchange. This setting only has an effect when resumption is enabled.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dhfile"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dhfile:

      .. rst-class:: ansible-option-title

      **dhfile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dhfile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The file name and path for the DH parameter.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dhkeyexpsizelimit"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dhkeyexpsizelimit:

      .. rst-class:: ansible-option-title

      **dhkeyexpsizelimit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dhkeyexpsizelimit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dropreqwithnohostheader"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-dropreqwithnohostheader:

      .. rst-class:: ansible-option-title

      **dropreqwithnohostheader**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dropreqwithnohostheader" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions(i.e vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived with SNI extension), the request is dropped.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-encrypttriggerpktcount"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-encrypttriggerpktcount:

      .. rst-class:: ansible-option-title

      **encrypttriggerpktcount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-encrypttriggerpktcount" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to Citrix ADC.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`45`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ersa"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ersa:

      .. rst-class:: ansible-option-title

      **ersa**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ersa" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.

      This parameter is not applicable when configuring a backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ersacount"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ersacount:

      .. rst-class:: ansible-option-title

      **ersacount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ersacount" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The  refresh  count  for the re-generation of RSA public-key and private-key pair.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hsts"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-hsts:

      .. rst-class:: ansible-option-title

      **hsts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hsts" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of HSTS protocol support for the SSL profile. Using HSTS, a server can enforce the use of an HTTPS connection for all communication with a client


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-includesubdomains"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-includesubdomains:

      .. rst-class:: ansible-option-title

      **includesubdomains**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-includesubdomains" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests for subdomains.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-insertionencoding"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-insertionencoding:

      .. rst-class:: ansible-option-title

      **insertionencoding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-insertionencoding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Encoding method used to insert the subject or issuer's name in HTTP requests to servers.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"Unicode"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"UTF-8"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_id"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-instance_id:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-instance_ip:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-instance_name:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-is_cloud:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-mas_proxy_call:

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
        <div class="ansibleOptionAnchor" id="parameter-maxage"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-maxage:

      .. rst-class:: ansible-option-title

      **maxage**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-maxage" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the maximum time, in seconds, in the strict transport security (STS) header during which the client must send only HTTPS requests to the server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-name:

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

      Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore (\_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-nitro_auth_token"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nitro_auth_token:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nitro_pass:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nitro_protocol:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nitro_timeout:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nitro_user:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-nsip:

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
        <div class="ansibleOptionAnchor" id="parameter-ocspstapling"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ocspstapling:

      .. rst-class:: ansible-option-title

      **ocspstapling**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ocspstapling" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:

      \ :literal:`ENABLED`\ : The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.

      \ :literal:`DISABLED`\ : The appliance does not check the status of the server certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-preload"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-preload:

      .. rst-class:: ansible-option-title

      **preload**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-preload" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Flag indicates the consent of the site owner to have their domain preloaded.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-prevsessionkeylifetime"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-prevsessionkeylifetime:

      .. rst-class:: ansible-option-title

      **prevsessionkeylifetime**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-prevsessionkeylifetime" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option sets the life time of symm key used to generate session tickets issued by NS in secs


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushenctrigger"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-pushenctrigger:

      .. rst-class:: ansible-option-title

      **pushenctrigger**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushenctrigger" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:

      \* ALWAYS - Any PUSH packet triggers encryption.

      \* IGNORE - \ :literal:`Ignore`\  PUSH packet for triggering encryption.

      \* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.

      \* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"Always"`
      - :ansible-option-choices-entry:`"Merge"`
      - :ansible-option-choices-entry:`"Ignore"`
      - :ansible-option-choices-entry:`"Timer"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushenctriggertimeout"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-pushenctriggertimeout:

      .. rst-class:: ansible-option-title

      **pushenctriggertimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushenctriggertimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-pushflag"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-pushflag:

      .. rst-class:: ansible-option-title

      **pushflag**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-pushflag" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:

      0 - Auto (PUSH flag is not set.)

      1 - Insert PUSH flag into every decrypted record.

      2 -Insert PUSH flag into every encrypted record.

      3 - Insert PUSH flag into every decrypted and encrypted record.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-quantumsize"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-quantumsize:

      .. rst-class:: ansible-option-title

      **quantumsize**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-quantumsize" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"4096"`
      - :ansible-option-choices-entry-default:`"8192"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"16384"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-redirectportrewrite"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-redirectportrewrite:

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

      State of the port rewrite while performing HTTPS redirect. If this parameter is set to \ :literal:`ENABLED`\ , and the URL from the server does not contain the standard port, the port is rewritten to the standard.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-save_config"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-save_config:

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
        <div class="ansibleOptionAnchor" id="parameter-sendclosenotify"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sendclosenotify:

      .. rst-class:: ansible-option-title

      **sendclosenotify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sendclosenotify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable sending SSL Close-Notify at the end of a transaction.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"True"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-serverauth"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-serverauth:

      .. rst-class:: ansible-option-title

      **serverauth**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-serverauth" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of server authentication support for the SSL Backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionkeylifetime"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessionkeylifetime:

      .. rst-class:: ansible-option-title

      **sessionkeylifetime**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionkeylifetime" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option sets the life time of symm key used to generate session tickets issued by NS in secs


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`3000`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionticket"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessionticket:

      .. rst-class:: ansible-option-title

      **sessionticket**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionticket" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option enables the use of session tickets, as per the RFC 5077


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionticketkeydata"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessionticketkeydata:

      .. rst-class:: ansible-option-title

      **sessionticketkeydata**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionticketkeydata" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Session ticket enc/dec key , admin can set it


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionticketkeyrefresh"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessionticketkeyrefresh:

      .. rst-class:: ansible-option-title

      **sessionticketkeyrefresh**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionticketkeyrefresh" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option enables the use of session tickets, as per the RFC 5077


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessionticketlifetime"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessionticketlifetime:

      .. rst-class:: ansible-option-title

      **sessionticketlifetime**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessionticketlifetime" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This option sets the life time of session tickets issued by NS in secs


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`300`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sessreuse"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sessreuse:

      .. rst-class:: ansible-option-title

      **sessreuse**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sessreuse" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the \ :literal:`ENABLED`\  setting, session key exchange is avoided for session resumption requests received from the client.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sesstimeout"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sesstimeout:

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

      The Session timeout value in seconds.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-skipclientcertpolicycheck"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-skipclientcertpolicycheck:

      .. rst-class:: ansible-option-title

      **skipclientcertpolicycheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-skipclientcertpolicycheck" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      This flag controls the processing of X509 certificate policies. If this option is Enabled, then the policy check in Client authentication will be skipped. This option can be used only when Client Authentication is Enabled and ClientCert is set to Mandatory


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snienable"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-snienable:

      .. rst-class:: ansible-option-title

      **snienable**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snienable" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, \*.sports.net can be used to secure domains such as login.sports.net and help.sports.net.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-snihttphostmatch"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-snihttphostmatch:

      .. rst-class:: ansible-option-title

      **snihttphostmatch**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-snihttphostmatch" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Controls how the HTTP 'Host' header value is validated. These checks are performed only if the session is SNI enabled (i.e when vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived with SNI extension) and HTTP request contains 'Host' header.

      Available settings function as follows:

      CERT   - Request is forwarded if the 'Host' value is covered

               by the certificate used to establish this SSL session.

               Note: 'CERT' matching mode cannot be applied in

               TLS 1.3 connections established by resuming from a

               previous TLS 1.3 session. On these connections, 'STRICT'

               matching mode will be used instead.

      STRICT - Request is forwarded only if value of 'Host' header

               in HTTP is identical to the 'Server name' value passed

               in 'Client Hello' of the SSL connection.

      NO     - No validation is performed on the HTTP 'Host'

               header value.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"False"`
      - :ansible-option-choices-entry-default:`"CERT"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"STRICT"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ssl3"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ssl3:

      .. rst-class:: ansible-option-title

      **ssl3**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ssl3" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of SSLv3 protocol support for the SSL profile.

      Note: On platforms with SSL acceleration chips, if the SSL chip does not support SSLv3, this parameter cannot be set to \ :literal:`ENABLED`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslimaxsessperserver"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslimaxsessperserver:

      .. rst-class:: ansible-option-title

      **sslimaxsessperserver**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslimaxsessperserver" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Maximum ssl session to be cached per dynamic origin server. A unique ssl session is created for each SNI received from the client on ClientHello and the matching session is used for server session reuse.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`10`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslinterception"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslinterception:

      .. rst-class:: ansible-option-title

      **sslinterception**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslinterception" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable transparent interception of SSL sessions.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ssliocspcheck"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ssliocspcheck:

      .. rst-class:: ansible-option-title

      **ssliocspcheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ssliocspcheck" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable OCSP check for origin server certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslireneg"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslireneg:

      .. rst-class:: ansible-option-title

      **sslireneg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslireneg" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or disable triggering the client renegotiation when renegotiation request is received from the origin server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ssllogprofile"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ssllogprofile:

      .. rst-class:: ansible-option-title

      **ssllogprofile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ssllogprofile" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the ssllogprofile.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_ecccurve_binding"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_ecccurve_binding:

      .. rst-class:: ansible-option-title

      **sslprofile_ecccurve_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_ecccurve_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for sslprofile\_ecccurve\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_ecccurve_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_ecccurve_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_ecccurve_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_ecccurve_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_ecccurve_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_ecccurve_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcertkey_binding"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcertkey_binding:

      .. rst-class:: ansible-option-title

      **sslprofile_sslcertkey_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcertkey_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for sslprofile\_sslcertkey\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcertkey_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcertkey_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcertkey_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcertkey_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcertkey_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcertkey_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcipher_binding"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcipher_binding:

      .. rst-class:: ansible-option-title

      **sslprofile_sslcipher_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcipher_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for sslprofile\_sslcipher\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcipher_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcipher_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcipher_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslcipher_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslcipher_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslcipher_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslciphersuite_binding"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslciphersuite_binding:

      .. rst-class:: ansible-option-title

      **sslprofile_sslciphersuite_binding**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslciphersuite_binding" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Bindings for sslprofile\_sslciphersuite\_binding resource


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslciphersuite_binding/binding_members"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslciphersuite_binding/binding_members:

      .. rst-class:: ansible-option-title

      **binding_members**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslciphersuite_binding/binding_members" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofile_sslciphersuite_binding/mode"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofile_sslciphersuite_binding/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofile_sslciphersuite_binding/mode" title="Permalink to this option"></a>

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
        <div class="ansibleOptionAnchor" id="parameter-sslprofiletype"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslprofiletype:

      .. rst-class:: ansible-option-title

      **sslprofiletype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslprofiletype" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Type of profile. Front end profiles apply to the entity that receives requests from a client. Backend profiles apply to the entity that sends client requests to a server.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"BackEnd"`
      - :ansible-option-choices-entry-default:`"FrontEnd"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"QUIC-FrontEnd"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sslredirect"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-sslredirect:

      .. rst-class:: ansible-option-title

      **sslredirect**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sslredirect" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of HTTPS redirects for the SSL service.

      For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.

      If SSL Redirect is \ :literal:`ENABLED`\ , the redirect message is automatically converted from http:// to https:// and the SSL session does not break.

      This parameter is not applicable when configuring a backend profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ssltriggertimeout"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-ssltriggertimeout:

      .. rst-class:: ansible-option-title

      **ssltriggertimeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ssltriggertimeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the Citrix ADC because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`100`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-state:

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
        <div class="ansibleOptionAnchor" id="parameter-strictcachecks"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-strictcachecks:

      .. rst-class:: ansible-option-title

      **strictcachecks**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-strictcachecks" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable strict CA certificate checks on the appliance.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"True"`
      - :ansible-option-choices-entry:`"False"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-strictsigdigestcheck"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-strictsigdigestcheck:

      .. rst-class:: ansible-option-title

      **strictsigdigestcheck**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-strictsigdigestcheck" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Parameter indicating to check whether peer entity certificate during TLS1.2 handshake is signed with one of signature-hash combination supported by Citrix ADC.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls1"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-tls1:

      .. rst-class:: ansible-option-title

      **tls1**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls1" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of TLSv1.0 protocol support for the SSL profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls11"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-tls11:

      .. rst-class:: ansible-option-title

      **tls11**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls11" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of TLSv1.1 protocol support for the SSL profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls12"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-tls12:

      .. rst-class:: ansible-option-title

      **tls12**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls12" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of TLSv1.2 protocol support for the SSL profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"ENABLED"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"DISABLED"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls13"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-tls13:

      .. rst-class:: ansible-option-title

      **tls13**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls13" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of TLSv1.3 protocol support for the SSL profile.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tls13sessionticketsperauthcontext"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-tls13sessionticketsperauthcontext:

      .. rst-class:: ansible-option-title

      **tls13sessionticketsperauthcontext**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tls13sessionticketsperauthcontext" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated, ticket-based resumption is enabled, and either (1) a handshake completes or (2) post-handhsake client auth completes.

      This value can be increased to enable clients to open multiple parallel connections using a fresh ticket for each connection.

      No tickets are sent if resumption is disabled.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`1`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-validate_certs:

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
        <div class="ansibleOptionAnchor" id="parameter-zerorttearlydata"></div>

      .. _ansible_collections.netscaler.adc.sslprofile_module__parameter-zerorttearlydata:

      .. rst-class:: ansible-option-title

      **zerorttearlydata**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zerorttearlydata" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of TLS 1.3 0-RTT early data support for the SSL Virtual Server. This setting only has an effect if resumption is enabled, as early data cannot be sent along with an initial handshake.

      Early application data has significantly different security properties - in particular there is no guarantee that the data cannot be replayed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"ENABLED"`
      - :ansible-option-choices-entry-default:`"DISABLED"` :ansible-option-choices-default-mark:`← (default)`


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

      .. _ansible_collections.netscaler.adc.sslprofile_module__return-changed:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__return-diff:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__return-diff_list:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__return-failed:

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

      .. _ansible_collections.netscaler.adc.sslprofile_module__return-loglines:

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

