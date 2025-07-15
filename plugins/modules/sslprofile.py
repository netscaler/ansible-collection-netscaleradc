#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: sslprofile
short_description: Configuration for SSL profile resource.
description: Configuration for SSL profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  allowextendedmastersecret:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - When set to C(YES), attempt to use the TLS Extended Master Secret (EMS, as
      - described in RFC 7627) when negotiating TLS 1.0, TLS 1.1 and TLS 1.2
      - connection parameters. EMS must be supported by both the TLS client and server
      - in order to be enabled during a handshake. This setting applies to both
      - frontend and backend SSL profiles.
  allowunknownsni:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Controls how the handshake is handled when the server name extension does
        not match any of the bound certificates. These checks are performed only if
        the session is SNI enabled (i.e. when profile bound to vserver has SNIEnable
        and Client Hello arrived with SNI extension). Available settings function
        as follows :'
      - C(ENABLED)   - handshakes with an unknown SNI are allowed to continue, if
        a default cert is bound.
      - DISLABED  - handshakes with an unknown SNI are not allowed to continue.
  alpnprotocol:
    type: str
    choices:
      - NONE
      - HTTP1.1
      - HTTP2
    description:
      - Application protocol supported by the server and used in negotiation of the
        protocol with the client. Possible values are C(HTTP1.1), C(HTTP2) and C(NONE).
        Default value is C(NONE) which implies application protocol is not enabled
        hence remain unknown to the TLS layer. This parameter is relevant only if
        SSL connection is handled by the virtual server of the type SSL_TCP.
  ciphername:
    type: str
    description:
      - The cipher group/alias/individual cipher configuration
  cipherpriority:
    type: int
    description:
      - cipher priority
  cipherredirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of Cipher Redirect. If this parameter is set to C(ENABLED), you can
        configure an SSL virtual server or service to display meaningful error messages
        if the SSL handshake fails because of a cipher mismatch between the virtual
        server or service and the client.
      - This parameter is not applicable when configuring a backend profile.
  cipherurl:
    type: str
    description:
      - The redirect URL to be used with the Cipher Redirect feature.
  cleartextport:
    type: int
    description:
      - Port on which clear-text data is sent by the appliance to the server. Do not
        specify this parameter for SSL offloading with end-to-end encryption.
  clientauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of client authentication. In service-based SSL offload, the service
        terminates the SSL handshake if the SSL client does not provide a valid certificate.
      - This parameter is not applicable when configuring a backend profile.
  clientauthuseboundcachain:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Certficates bound on the VIP are used for validating the client cert. Certficates
        came along with client cert are not used for validating the client cert
  clientcert:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The rule for client certificate requirement in client authentication.
  commonname:
    type: str
    description:
      - Name to be checked against the CommonName (CN) field in the server certificate
        bound to the SSL server.
  defaultsni:
    type: str
    description:
      - Default domain name supported by the SSL virtual server. The parameter is
        effective, when zero touch certificate management is active for the SSL virtual
        server i.e. no manual SNI cert or default server cert is bound to the v-server.
        For SSL transactions, when SNI is not presented by the client, server-certificate
        corresponding to the default SNI, if available in the cert-store, is selected
        else connection is terminated.
  denysslreneg:
    type: str
    choices:
      - 'NO'
      - FRONTEND_CLIENT
      - FRONTEND_CLIENTSERVER
      - ALL
      - NONSECURE
    description:
      - 'Deny renegotiation in specified circumstances. Available settings function
        as follows:'
      - '* C(NO) - Allow SSL renegotiation.'
      - '* C(FRONTEND_CLIENT) - Deny secure and nonsecure SSL renegotiation initiated
        by the client.'
      - '* C(FRONTEND_CLIENTSERVER) - Deny secure and nonsecure SSL renegotiation
        initiated by the client or the Citrix ADC during policy-based client authentication.'
      - '* C(ALL) - Deny all secure and nonsecure SSL renegotiation.'
      - '* C(NONSECURE) - Deny nonsecure SSL renegotiation. Allows only clients that
        support RFC 5746.'
  dh:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of Diffie-Hellman (DH) key exchange.
      - This parameter is not applicable when configuring a backend profile.
  dhcount:
    type: int
    description:
      - Number of interactions, between the client and the Citrix ADC, after which
        the DH private-public pair is regenerated. A value of zero (0) specifies refresh
        every time.
      - This parameter is not applicable when configuring a backend profile. Allowed
        DH count values are 0 and >= 500.
  dhekeyexchangewithpsk:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Whether or not the SSL Virtual Server will require a DHE key exchange to occur
        when a PSK is accepted during a TLS 1.3 resumption handshake.
      - A DHE key exchange ensures forward secrecy even in the event that ticket keys
        are compromised, at the expense of an additional round trip and resources
        required to carry out the DHE key exchange.
      - If disabled, a DHE key exchange will be performed when a PSK is accepted but
        only if requested by the client.
      - If enabled, the server will require a DHE key exchange when a PSK is accepted
        regardless of whether the client supports combined PSK-DHE key exchange. This
        setting only has an effect when resumption is enabled.
  dhfile:
    type: str
    description:
      - The file name and path for the DH parameter.
  dhkeyexpsizelimit:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option enables the use of NIST recommended (NIST Special Publication
        800-56A) bit size for private-key size. For example, for DH params of size
        2048bit, the private-key size recommended is 224bits. This is rounded-up to
        256bits.
  dropreqwithnohostheader:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Host header check for SNI enabled sessions. If this check is enabled and the
        HTTP request does not contain the host header for SNI enabled sessions(i.e
        vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived
        with SNI extension), the request is dropped.
  encryptedclienthello:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLS 1.3 Encrypted Client Hello Support
  encrypttriggerpktcount:
    type: int
    description:
      - Maximum number of queued packets after which encryption is triggered. Use
        this setting for SSL transactions that send small packets from server to Citrix
        ADC.
  ersa:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that
        support only export ciphers to communicate with the secure server even if
        the server certificate does not support export clients. The ephemeral RSA
        key is automatically generated when you bind an export cipher to an SSL or
        TCP-based SSL virtual server or service. When you remove the export cipher,
        the eRSA key is not deleted. It is reused at a later date when another export
        cipher is bound to an SSL or TCP-based SSL virtual server or service. The
        eRSA key is deleted when the appliance restarts.
      - This parameter is not applicable when configuring a backend profile.
  ersacount:
    type: int
    description:
      - The  refresh  count  for the re-generation of RSA public-key and private-key
        pair.
  hsts:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of HSTS protocol support for the SSL profile. Using HSTS, a server can
        enforce the use of an HTTPS connection for all communication with a client
  includesubdomains:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests
        for subdomains.
  insertionencoding:
    type: str
    choices:
      - Unicode
      - UTF-8
    description:
      - Encoding method used to insert the subject or issuer's name in HTTP requests
        to servers.
  maxage:
    type: int
    description:
      - Set the maximum time, in seconds, in the strict transport security (STS) header
        during which the client must send only HTTPS requests to the server
  maxrenegrate:
    type: int
    description:
      - Maximum number of renegotiation requests allowed, in one second, to each SSL
        entity to which this profile is bound. When set to 0, an unlimited number
        of renegotiation requests are allowed. Applicable only when Deny SSL renegotiation
        is set to a value other than ALL.
  name:
    type: str
    description:
      - Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the profile is created.
  ocspstapling:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'State of OCSP stapling support on the SSL virtual server. Supported only
        if the protocol used is higher than SSLv3. Possible values:'
      - 'C(ENABLED): The appliance sends a request to the OCSP responder to check
        the status of the server certificate and caches the response for the specified
        time. If the response is valid at the time of SSL handshake with the client,
        the OCSP-based server certificate status is sent to the client during the
        handshake.'
      - 'C(DISABLED): The appliance does not check the status of the server certificate.'
  preload:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Flag indicates the consent of the site owner to have their domain preloaded.
  prevsessionkeylifetime:
    type: int
    description:
      - This option sets the life time of symm key used to generate session tickets
        issued by NS in secs
  pushenctrigger:
    type: str
    choices:
      - Always
      - Merge
      - Ignore
      - Timer
    description:
      - 'Trigger encryption on the basis of the PUSH flag value. Available settings
        function as follows:'
      - '* ALWAYS - Any PUSH packet triggers encryption.'
      - '* IGNORE - C(Ignore) PUSH packet for triggering encryption.'
      - '* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet
        triggers encryption.'
      - '* TIMER - PUSH packet triggering encryption is delayed by the time defined
        in the set ssl parameter command or in the Change Advanced SSL Settings dialog
        box.'
  pushenctriggertimeout:
    type: int
    description:
      - PUSH encryption trigger timeout value. The timeout value is applied only if
        you set the Push Encryption Trigger parameter to Timer in the SSL virtual
        server settings.
  pushflag:
    type: int
    description:
      - 'Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag
        is set to a value other than 0, the buffered records are forwarded on the
        basis of the value of the PUSH flag. Available settings function as follows:'
      - 0 - Auto (PUSH flag is not set.)
      - 1 - Insert PUSH flag into every decrypted record.
      - 2 -Insert PUSH flag into every encrypted record.
      - 3 - Insert PUSH flag into every decrypted and encrypted record.
  quantumsize:
    type: str
    choices:
      - '4096'
      - '8192'
      - '16384'
    description:
      - Amount of data to collect before the data is pushed to the crypto hardware
        for encryption. For large downloads, a larger quantum size better utilizes
        the crypto resources.
  redirectportrewrite:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the port rewrite while performing HTTPS redirect. If this parameter
        is set to C(ENABLED), and the URL from the server does not contain the standard
        port, the port is rewritten to the standard.
  sendclosenotify:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable sending SSL Close-Notify at the end of a transaction.
  serverauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of server authentication support for the SSL Backend profile.
  sessionkeylifetime:
    type: int
    description:
      - This option sets the life time of symm key used to generate session tickets
        issued by NS in secs
  sessionticket:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option enables the use of session tickets, as per the RFC 5077
  sessionticketkeydata:
    type: str
    description:
      - Session ticket enc/dec key , admin can set it
  sessionticketkeyrefresh:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option enables the use of session tickets, as per the RFC 5077
  sessionticketlifetime:
    type: int
    description:
      - This option sets the life time of session tickets issued by NS in secs
  sessreuse:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of session reuse. Establishing the initial handshake requires CPU-intensive
        public key encryption operations. With the C(ENABLED) setting, session key
        exchange is avoided for session resumption requests received from the client.
  sesstimeout:
    type: int
    description:
      - The Session timeout value in seconds.
  skipclientcertpolicycheck:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This flag controls the processing of X509 certificate policies. If this option
        is Enabled, then the policy check in Client authentication will be skipped.
        This option can be used only when Client Authentication is Enabled and ClientCert
        is set to Mandatory
  snienable:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the Server Name Indication (SNI) feature on the virtual server and
        service-based offload. SNI helps to enable SSL encryption on multiple domains
        on a single virtual server or service if the domains are controlled by the
        same organization and share the same second-level domain name. For example,
        *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.
  snihttphostmatch:
    type: str
    choices:
      - 'NO'
      - CERT
      - STRICT
    description:
      - Controls how the HTTP 'Host' header value is validated. These checks are performed
        only if the session is SNI enabled (i.e when vserver or profile bound to vserver
        has SNI enabled and 'Client Hello' arrived with SNI extension) and HTTP request
        contains 'Host' header.
      - 'Available settings function as follows:'
      - C(CERT)   - Request is forwarded if the 'Host' value is covered
      - '         by the certificate used to establish this SSL session.'
      - '         Note: ''C(CERT)'' matching mode cannot be applied in'
      - '         TLS 1.3 connections established by resuming from a'
      - '         previous TLS 1.3 session. On these connections, ''C(STRICT)'''
      - '         matching mode will be used instead.'
      - C(STRICT) - Request is forwarded only if value of 'Host' header
      - '         in HTTP is identical to the ''Server name'' value passed'
      - '         in ''Client Hello'' of the SSL connection.'
      - C(NO)     - No validation is performed on the HTTP 'Host'
      - '         header value.'
  ssl3:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of SSLv3 protocol support for the SSL profile.
      - 'Note: On platforms with SSL acceleration chips, if the SSL chip does not
        support SSLv3, this parameter cannot be set to C(ENABLED).'
  sslclientlogs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When enabled, NetScaler will log the session ID and SNI name during SSL handshakes
        on both the external and internal interfaces.
  sslimaxsessperserver:
    type: int
    description:
      - Maximum ssl session to be cached per dynamic origin server. A unique ssl session
        is created for each SNI received from the client on ClientHello and the matching
        session is used for server session reuse.
  sslinterception:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable transparent interception of SSL sessions.
  ssliocspcheck:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable OCSP check for origin server certificate.
  sslireneg:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable triggering the client renegotiation when renegotiation request
        is received from the origin server.
  ssllogprofile:
    type: str
    description:
      - The name of the ssllogprofile.
  sslprofiletype:
    type: str
    choices:
      - BackEnd
      - FrontEnd
      - QUIC-FrontEnd
      - QUIC-BackEnd
    description:
      - Type of profile. Front end profiles apply to the entity that receives requests
        from a client. Backend profiles apply to the entity that sends client requests
        to a server.
  sslredirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of HTTPS redirects for the SSL service.
      - For an SSL session, if the client browser receives a redirect message, the
        browser tries to connect to the new location. However, the secure SSL session
        breaks if the object has moved from a secure site (https://) to an unsecure
        site (http://). Typically, a warning message appears on the screen, prompting
        the user to continue or disconnect.
      - If SSL Redirect is C(ENABLED), the redirect message is automatically converted
        from http:// to https:// and the SSL session does not break.
      - This parameter is not applicable when configuring a backend profile.
  ssltriggertimeout:
    type: int
    description:
      - Time, in milliseconds, after which encryption is triggered for transactions
        that are not tracked on the Citrix ADC because their length is not known.
        There can be a delay of up to 10ms from the specified timeout value before
        the packet is pushed into the queue.
  strictcachecks:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable strict CA certificate checks on the appliance.
  strictsigdigestcheck:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter indicating to check whether peer entity certificate during TLS1.2
        handshake is signed with one of signature-hash combination supported by Citrix
        ADC.
  tls1:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.0 protocol support for the SSL profile.
  tls11:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.1 protocol support for the SSL profile.
  tls12:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.2 protocol support for the SSL profile.
  tls13:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.3 protocol support for the SSL profile.
  tls13sessionticketsperauthcontext:
    type: int
    description:
      - Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated,
        ticket-based resumption is enabled, and either (1) a handshake completes or
        (2) post-handhsake client auth completes.
      - This value can be increased to enable clients to open multiple parallel connections
        using a fresh ticket for each connection.
      - No tickets are sent if resumption is disabled.
  zerorttearlydata:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLS 1.3 0-RTT early data support for the SSL Virtual Server. This
        setting only has an effect if resumption is enabled, as early data cannot
        be sent along with an initial handshake.
      - Early application data has significantly different security properties - in
        particular there is no guarantee that the data cannot be replayed.
  sslprofile_ecccurve_binding:
    type: dict
    description: Bindings for sslprofile_ecccurve_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  sslprofile_sslcertkey_binding:
    type: dict
    description: Bindings for sslprofile_sslcertkey_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  sslprofile_sslcipher_binding:
    type: dict
    description: Bindings for sslprofile_sslcipher_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  sslprofile_sslciphersuite_binding:
    type: dict
    description: Bindings for sslprofile_sslciphersuite_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  sslprofile_sslechconfig_binding:
    type: dict
    description: Bindings for sslprofile_sslechconfig_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslprofile
      delegate_to: localhost
      netscaler.adc.sslprofile:
        state: present
        name: front_1
        sslprofiletype: FrontEnd
        dhcount: '0'
        dh: ENABLED
        dhfile: certs/dh/dh1024.pem
        ersa: ENABLED
        ersacount: '0'
        sessreuse: ENABLED
        sesstimeout: '120'
        cipherredirect: ENABLED
        cipherurl: https://www.abc.com
        clientauth: ENABLED
        clientcert: Mandatory
        sslredirect: ENABLED
        redirectportrewrite: ENABLED
        ssl3: ENABLED
        tls1: ENABLED
        tls11: ENABLED
        tls12: ENABLED
        snienable: ENABLED
        pushenctrigger: Always
        sendclosenotify: 'YES'
        insertionencoding: UTF-8
        denysslreneg: ALL
        quantumsize: '4096'
        strictcachecks: 'YES'
        encrypttriggerpktcount: '10'
        pushflag: '1'
        dropreqwithnohostheader: 'YES'
        pushenctriggertimeout: '10'
        ssltriggertimeout: '10'
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
failed:
  description: Indicates if the module failed or not
  returned: always
  type: bool
  sample: false
loglines:
  description: list of logged messages by the module
  returned: always
  type: list
  sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
