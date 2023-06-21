#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: sslprofile
short_description: Configuration for SSL profile resource.
description: Configuration for SSL profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  allowextendedmastersecret:
    description:
      - When set to YES, attempt to use the TLS Extended Master Secret (EMS, as
      - described in RFC 7627) when negotiating TLS 1.0, TLS 1.1 and TLS 1.2
      - connection parameters. EMS must be supported by both the TLS client and server
      - in order to be enabled during a handshake. This setting applies to both
      - frontend and backend SSL profiles.
    type: str
    choices:
      - true
      - false
  alpnprotocol:
    description:
      - Application protocol supported by the server and used in negotiation of the
        protocol with the client. Possible values are HTTP1.1, HTTP2 and NONE. Default
        value is NONE which implies application protocol is not enabled hence remain
        unknown to the TLS layer. This parameter is relevant only if SSL connection
        is handled by the virtual server of the type SSL_TCP.
    type: str
    default: NONE
    choices:
      - NONE
      - HTTP1.1
      - HTTP2
  ciphername:
    description:
      - The cipher group/alias/individual cipher configuration
    type: str
  cipherpriority:
    description:
      - cipher priority
    type: int
  cipherredirect:
    description:
      - State of Cipher Redirect. If this parameter is set to ENABLED, you can configure
        an SSL virtual server or service to display meaningful error messages if the
        SSL handshake fails because of a cipher mismatch between the virtual server
        or service and the client.
      - This parameter is not applicable when configuring a backend profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  cipherurl:
    description:
      - The redirect URL to be used with the Cipher Redirect feature.
    type: str
  cleartextport:
    description:
      - Port on which clear-text data is sent by the appliance to the server. Do not
        specify this parameter for SSL offloading with end-to-end encryption.
    type: int
  clientauth:
    description:
      - State of client authentication. In service-based SSL offload, the service
        terminates the SSL handshake if the SSL client does not provide a valid certificate.
      - This parameter is not applicable when configuring a backend profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  clientauthuseboundcachain:
    description:
      - Certficates bound on the VIP are used for validating the client cert. Certficates
        came along with client cert are not used for validating the client cert
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  clientcert:
    description:
      - The rule for client certificate requirement in client authentication.
    type: str
    choices:
      - Mandatory
      - Optional
  commonname:
    description:
      - Name to be checked against the CommonName (CN) field in the server certificate
        bound to the SSL server.
    type: str
  denysslreneg:
    description:
      - 'Deny renegotiation in specified circumstances. Available settings function
        as follows:'
      - '* NO - Allow SSL renegotiation.'
      - '* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated
        by the client.'
      - '* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated
        by the client or the Citrix ADC during policy-based client authentication.'
      - '* ALL - Deny all secure and nonsecure SSL renegotiation.'
      - '* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that
        support RFC 5746.'
    type: str
    default: ALL
    choices:
      - false
      - FRONTEND_CLIENT
      - FRONTEND_CLIENTSERVER
      - ALL
      - NONSECURE
  dh:
    description:
      - State of Diffie-Hellman (DH) key exchange.
      - This parameter is not applicable when configuring a backend profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dhcount:
    description:
      - Number of interactions, between the client and the Citrix ADC, after which
        the DH private-public pair is regenerated. A value of zero (0) specifies refresh
        every time.
      - This parameter is not applicable when configuring a backend profile. Allowed
        DH count values are 0 and >= 500.
    type: int
  dhekeyexchangewithpsk:
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
    type: str
    choices:
      - true
      - false
  dhfile:
    description:
      - The file name and path for the DH parameter.
    type: str
  dhkeyexpsizelimit:
    description:
      - This option enables the use of NIST recommended (NIST Special Publication
        800-56A) bit size for private-key size. For example, for DH params of size
        2048bit, the private-key size recommended is 224bits. This is rounded-up to
        256bits.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dropreqwithnohostheader:
    description:
      - Host header check for SNI enabled sessions. If this check is enabled and the
        HTTP request does not contain the host header for SNI enabled sessions(i.e
        vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived
        with SNI extension), the request is dropped.
    type: str
    choices:
      - true
      - false
  encrypttriggerpktcount:
    description:
      - Maximum number of queued packets after which encryption is triggered. Use
        this setting for SSL transactions that send small packets from server to Citrix
        ADC.
    type: int
    default: 45
  ersa:
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
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  ersacount:
    description:
      - The  refresh  count  for the re-generation of RSA public-key and private-key
        pair.
    type: int
  hsts:
    description:
      - State of HSTS protocol support for the SSL profile. Using HSTS, a server can
        enforce the use of an HTTPS connection for all communication with a client
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  includesubdomains:
    description:
      - Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests
        for subdomains.
    type: str
    choices:
      - true
      - false
  insertionencoding:
    description:
      - Encoding method used to insert the subject or issuer's name in HTTP requests
        to servers.
    type: str
    default: Unicode
    choices:
      - Unicode
      - UTF-8
  maxage:
    description:
      - Set the maximum time, in seconds, in the strict transport security (STS) header
        during which the client must send only HTTPS requests to the server
    type: int
  name:
    description:
      - Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the profile is created.
    type: str
  ocspstapling:
    description:
      - 'State of OCSP stapling support on the SSL virtual server. Supported only
        if the protocol used is higher than SSLv3. Possible values:'
      - 'ENABLED: The appliance sends a request to the OCSP responder to check the
        status of the server certificate and caches the response for the specified
        time. If the response is valid at the time of SSL handshake with the client,
        the OCSP-based server certificate status is sent to the client during the
        handshake.'
      - 'DISABLED: The appliance does not check the status of the server certificate.'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  preload:
    description:
      - Flag indicates the consent of the site owner to have their domain preloaded.
    type: str
    choices:
      - true
      - false
  prevsessionkeylifetime:
    description:
      - This option sets the life time of symm key used to generate session tickets
        issued by NS in secs
    type: int
  pushenctrigger:
    description:
      - 'Trigger encryption on the basis of the PUSH flag value. Available settings
        function as follows:'
      - '* ALWAYS - Any PUSH packet triggers encryption.'
      - '* IGNORE - Ignore PUSH packet for triggering encryption.'
      - '* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet
        triggers encryption.'
      - '* TIMER - PUSH packet triggering encryption is delayed by the time defined
        in the set ssl parameter command or in the Change Advanced SSL Settings dialog
        box.'
    type: str
    choices:
      - Always
      - Merge
      - Ignore
      - Timer
  pushenctriggertimeout:
    description:
      - PUSH encryption trigger timeout value. The timeout value is applied only if
        you set the Push Encryption Trigger parameter to Timer in the SSL virtual
        server settings.
    type: int
    default: 1
  pushflag:
    description:
      - 'Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag
        is set to a value other than 0, the buffered records are forwarded on the
        basis of the value of the PUSH flag. Available settings function as follows:'
      - 0 - Auto (PUSH flag is not set.)
      - 1 - Insert PUSH flag into every decrypted record.
      - 2 -Insert PUSH flag into every encrypted record.
      - 3 - Insert PUSH flag into every decrypted and encrypted record.
    type: int
  quantumsize:
    description:
      - Amount of data to collect before the data is pushed to the crypto hardware
        for encryption. For large downloads, a larger quantum size better utilizes
        the crypto resources.
    type: str
    default: 8192
    choices:
      - 4096
      - 8192
      - 16384
  redirectportrewrite:
    description:
      - State of the port rewrite while performing HTTPS redirect. If this parameter
        is set to ENABLED, and the URL from the server does not contain the standard
        port, the port is rewritten to the standard.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sendclosenotify:
    description:
      - Enable sending SSL Close-Notify at the end of a transaction.
    type: str
    default: true
    choices:
      - true
      - false
  serverauth:
    description:
      - State of server authentication support for the SSL Backend profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sessionkeylifetime:
    description:
      - This option sets the life time of symm key used to generate session tickets
        issued by NS in secs
    type: int
    default: 3000
  sessionticket:
    description:
      - This option enables the use of session tickets, as per the RFC 5077
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sessionticketkeydata:
    description:
      - Session ticket enc/dec key , admin can set it
    type: str
  sessionticketkeyrefresh:
    description:
      - This option enables the use of session tickets, as per the RFC 5077
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  sessionticketlifetime:
    description:
      - This option sets the life time of session tickets issued by NS in secs
    type: int
    default: 300
  sessreuse:
    description:
      - State of session reuse. Establishing the initial handshake requires CPU-intensive
        public key encryption operations. With the ENABLED setting, session key exchange
        is avoided for session resumption requests received from the client.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  sesstimeout:
    description:
      - The Session timeout value in seconds.
    type: int
  skipclientcertpolicycheck:
    description:
      - This flag controls the processing of X509 certificate policies. If this option
        is Enabled, then the policy check in Client authentication will be skipped.
        This option can be used only when Client Authentication is Enabled and ClientCert
        is set to Mandatory
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  snienable:
    description:
      - State of the Server Name Indication (SNI) feature on the virtual server and
        service-based offload. SNI helps to enable SSL encryption on multiple domains
        on a single virtual server or service if the domains are controlled by the
        same organization and share the same second-level domain name. For example,
        *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  snihttphostmatch:
    description:
      - Controls how the HTTP 'Host' header value is validated. These checks are performed
        only if the session is SNI enabled (i.e when vserver or profile bound to vserver
        has SNI enabled and 'Client Hello' arrived with SNI extension) and HTTP request
        contains 'Host' header.
      - 'Available settings function as follows:'
      - CERT   - Request is forwarded if the 'Host' value is covered
      - '         by the certificate used to establish this SSL session.'
      - '         Note: ''CERT'' matching mode cannot be applied in'
      - '         TLS 1.3 connections established by resuming from a'
      - '         previous TLS 1.3 session. On these connections, ''STRICT'''
      - '         matching mode will be used instead.'
      - STRICT - Request is forwarded only if value of 'Host' header
      - '         in HTTP is identical to the ''Server name'' value passed'
      - '         in ''Client Hello'' of the SSL connection.'
      - NO     - No validation is performed on the HTTP 'Host'
      - '         header value.'
    type: str
    default: CERT
    choices:
      - false
      - CERT
      - STRICT
  ssl3:
    description:
      - State of SSLv3 protocol support for the SSL profile.
      - 'Note: On platforms with SSL acceleration chips, if the SSL chip does not
        support SSLv3, this parameter cannot be set to ENABLED.'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sslimaxsessperserver:
    description:
      - Maximum ssl session to be cached per dynamic origin server. A unique ssl session
        is created for each SNI received from the client on ClientHello and the matching
        session is used for server session reuse.
    type: int
    default: 10
  sslinterception:
    description:
      - Enable or disable transparent interception of SSL sessions.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ssliocspcheck:
    description:
      - Enable or disable OCSP check for origin server certificate.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  sslireneg:
    description:
      - Enable or disable triggering the client renegotiation when renegotiation request
        is received from the origin server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  ssllogprofile:
    description:
      - The name of the ssllogprofile.
    type: str
  sslprofiletype:
    description:
      - Type of profile. Front end profiles apply to the entity that receives requests
        from a client. Backend profiles apply to the entity that sends client requests
        to a server.
    type: str
    default: FrontEnd
    choices:
      - BackEnd
      - FrontEnd
      - QUIC-FrontEnd
  sslredirect:
    description:
      - State of HTTPS redirects for the SSL service.
      - For an SSL session, if the client browser receives a redirect message, the
        browser tries to connect to the new location. However, the secure SSL session
        breaks if the object has moved from a secure site (https://) to an unsecure
        site (http://). Typically, a warning message appears on the screen, prompting
        the user to continue or disconnect.
      - If SSL Redirect is ENABLED, the redirect message is automatically converted
        from http:// to https:// and the SSL session does not break.
      - This parameter is not applicable when configuring a backend profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ssltriggertimeout:
    description:
      - Time, in milliseconds, after which encryption is triggered for transactions
        that are not tracked on the Citrix ADC because their length is not known.
        There can be a delay of up to 10ms from the specified timeout value before
        the packet is pushed into the queue.
    type: int
    default: 100
  strictcachecks:
    description:
      - Enable strict CA certificate checks on the appliance.
    type: str
    choices:
      - true
      - false
  strictsigdigestcheck:
    description:
      - Parameter indicating to check whether peer entity certificate during TLS1.2
        handshake is signed with one of signature-hash combination supported by Citrix
        ADC.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  tls1:
    description:
      - State of TLSv1.0 protocol support for the SSL profile.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tls11:
    description:
      - State of TLSv1.1 protocol support for the SSL profile.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tls12:
    description:
      - State of TLSv1.2 protocol support for the SSL profile.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tls13:
    description:
      - State of TLSv1.3 protocol support for the SSL profile.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  tls13sessionticketsperauthcontext:
    description:
      - Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated,
        ticket-based resumption is enabled, and either (1) a handshake completes or
        (2) post-handhsake client auth completes.
      - This value can be increased to enable clients to open multiple parallel connections
        using a fresh ticket for each connection.
      - No tickets are sent if resumption is disabled.
    type: int
    default: 1
  zerorttearlydata:
    description:
      - State of TLS 1.3 0-RTT early data support for the SSL Virtual Server. This
        setting only has an effect if resumption is enabled, as early data cannot
        be sent along with an initial handshake.
      - Early application data has significantly different security properties - in
        particular there is no guarantee that the data cannot be replayed.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
