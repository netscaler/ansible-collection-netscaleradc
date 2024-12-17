#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
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
module: sslvserver
short_description: Configuration for SSL virtual server resource.
description: Configuration for SSL virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  cipherredirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of Cipher Redirect. If cipher redirect is enabled, you can configure
        an SSL virtual server or service to display meaningful error messages if the
        SSL handshake fails because of a cipher mismatch between the virtual server
        or service and the client.
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
      - State of client authentication. If client authentication is enabled, the virtual
        server terminates the SSL handshake if the SSL client does not provide a valid
        certificate.
  clientcert:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - Type of client authentication. If this parameter is set to MANDATORY, the
        appliance terminates the SSL handshake if the SSL client does not provide
        a valid certificate. With the OPTIONAL setting, the appliance requests a certificate
        from the SSL clients but proceeds with the SSL transaction even if the client
        presents an invalid certificate.
      - 'Caution: Define proper access control policies before changing this setting
        to C(Optional).'
  defaultsni:
    type: str
    description:
      - Default domain name supported by the SSL virtual server. The parameter is
        effective, when zero touch certificate management is active for the SSL virtual
        server i.e. no manual SNI cert or default server cert is bound to the v-server.
      - For SSL transactions, when SNI is not presented by the client, server-certificate
        corresponding to the default SNI, if available in the cert-store, is selected
        else connection is terminated.
  dh:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of Diffie-Hellman (DH) key exchange.
  dhcount:
    type: float
    description:
      - Number of interactions, between the client and the Citrix ADC, after which
        the DH private-public pair is regenerated. A value of zero (0) specifies refresh
        every time.
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
      - Name of and, optionally, path to the DH parameter file, in PEM format, to
        be installed. /nsconfig/ssl/ is the default path.
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
  dtls1:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of DTLSv1.0 protocol support for the SSL Virtual Server.
  dtls12:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of DTLSv1.2 protocol support for the SSL Virtual Server.
  dtlsprofilename:
    type: str
    description:
      - Name of the DTLS profile whose settings are to be applied to the virtual server.
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
  ersacount:
    type: float
    description:
      - Refresh count for regeneration of the RSA public-key and private-key pair.
        Zero (0) specifies infinite usage (no refresh).
  hsts:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of HSTS protocol support for the SSL Virtual Server. Using HSTS, a server
        can enforce the use of an HTTPS connection for all communication with a client
  includesubdomains:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests
        for subdomains.
  maxage:
    type: float
    description:
      - Set the maximum time, in seconds, in the strict transport security (STS) header
        during which the client must send only HTTPS requests to the server
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
  redirectportrewrite:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the port rewrite while performing HTTPS redirect. If this parameter
        is C(ENABLED) and the URL from the server does not contain the standard port,
        the port is rewritten to the standard.
  sendclosenotify:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable sending SSL Close-Notify at the end of a transaction
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
    type: float
    description:
      - Time, in seconds, for which to keep the session active. Any session resumption
        request received after the timeout period will require a fresh SSL handshake
        and establishment of a new SSL session.
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
  ssl2:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of SSLv2 protocol support for the SSL Virtual Server.
  ssl3:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of SSLv3 protocol support for the SSL Virtual Server.
      - 'Note: On platforms with SSL acceleration chips, if the SSL chip does not
        support SSLv3, this parameter cannot be set to C(ENABLED).'
  sslprofile:
    type: str
    description:
      - Name of the SSL profile that contains SSL settings for the virtual server.
  sslredirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of HTTPS redirects for the SSL virtual server.
      - ''
      - For an SSL session, if the client browser receives a redirect message, the
        browser tries to connect to the new location. However, the secure SSL session
        breaks if the object has moved from a secure site (https://) to an unsecure
        site (http://). Typically, a warning message appears on the screen, prompting
        the user to continue or disconnect.
      - If SSL Redirect is C(ENABLED), the redirect message is automatically converted
        from http:// to https:// and the SSL session does not break.
  sslv2redirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of SSLv2 Redirect. If SSLv2 redirect is enabled, you can configure an
        SSL virtual server or service to display meaningful error messages if the
        SSL handshake fails because of a protocol version mismatch between the virtual
        server or service and the client.
  sslv2url:
    type: str
    description:
      - URL of the page to which to redirect the client in case of a protocol version
        mismatch. Typically, this page has a clear explanation of the error or an
        alternative location that the transaction can continue from.
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
      - State of TLSv1.0 protocol support for the SSL Virtual Server.
  tls11:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.1 protocol support for the SSL Virtual Server.
  tls12:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.2 protocol support for the SSL Virtual Server.
  tls13:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.3 protocol support for the SSL Virtual Server.
  tls13sessionticketsperauthcontext:
    type: float
    description:
      - Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated,
        ticket-based resumption is enabled, and either (1) a handshake completes or
        (2) post-handhsake client auth completes.
      - This value can be increased to enable clients to open multiple parallel connections
        using a fresh ticket for each connection.
      - No tickets are sent if resumption is disabled.
  vservername:
    type: str
    description:
      - Name of the SSL virtual server for which to set advanced configuration.
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
  sslvserver_appfwpolicy_binding:
    type: dict
    description: Bindings for sslvserver_appfwpolicy_binding resource
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
  sslvserver_auditnslogpolicy_binding:
    type: dict
    description: Bindings for sslvserver_auditnslogpolicy_binding resource
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
  sslvserver_auditsyslogpolicy_binding:
    type: dict
    description: Bindings for sslvserver_auditsyslogpolicy_binding resource
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
  sslvserver_authorizationpolicy_binding:
    type: dict
    description: Bindings for sslvserver_authorizationpolicy_binding resource
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
  sslvserver_cachepolicy_binding:
    type: dict
    description: Bindings for sslvserver_cachepolicy_binding resource
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
  sslvserver_cmppolicy_binding:
    type: dict
    description: Bindings for sslvserver_cmppolicy_binding resource
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
  sslvserver_ecccurve_binding:
    type: dict
    description: Bindings for sslvserver_ecccurve_binding resource
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
  sslvserver_responderpolicy_binding:
    type: dict
    description: Bindings for sslvserver_responderpolicy_binding resource
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
  sslvserver_rewritepolicy_binding:
    type: dict
    description: Bindings for sslvserver_rewritepolicy_binding resource
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
  sslvserver_sslcacertbundle_binding:
    type: dict
    description: Bindings for sslvserver_sslcacertbundle_binding resource
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
  sslvserver_sslcertkey_binding:
    type: dict
    description: Bindings for sslvserver_sslcertkey_binding resource
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
  sslvserver_sslcertkeybundle_binding:
    type: dict
    description: Bindings for sslvserver_sslcertkeybundle_binding resource
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
  sslvserver_sslcipher_binding:
    type: dict
    description: Bindings for sslvserver_sslcipher_binding resource
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
  sslvserver_sslciphersuite_binding:
    type: dict
    description: Bindings for sslvserver_sslciphersuite_binding resource
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
  sslvserver_sslpolicy_binding:
    type: dict
    description: Bindings for sslvserver_sslpolicy_binding resource
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
- name: Sample sslvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslvserver
      delegate_to: localhost
      netscaler.adc.sslvserver:

        state: present
        vservername: backup_gslb_portal.bx.com
        sslprofile: ns_default_ssl_profile_frontend
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
