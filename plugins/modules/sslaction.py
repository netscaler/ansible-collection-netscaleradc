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
module: sslaction
short_description: Configuration for SSL action resource.
description: Configuration for SSL action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  cacertgrpname:
    type: str
    description:
      - This action will allow to pick CA(s) from the specific CA group, to verify
        the client certificate.
  certfingerprintdigest:
    type: str
    choices:
      - SHA1
      - SHA224
      - SHA256
      - SHA384
      - SHA512
    description:
      - Digest algorithm used to compute the fingerprint of the client certificate.
  certfingerprintheader:
    type: str
    description:
      - Name of the header into which to insert the client certificate fingerprint.
  certhashheader:
    type: str
    description:
      - Name of the header into which to insert the client certificate signature (hash).
  certheader:
    type: str
    description:
      - Name of the header into which to insert the client certificate.
  certissuerheader:
    type: str
    description:
      - Name of the header into which to insert the client certificate issuer details.
  certnotafterheader:
    type: str
    description:
      - Name of the header into which to insert the certificate's expiry date.
  certnotbeforeheader:
    type: str
    description:
      - Name of the header into which to insert the date and time from which the certificate
        is valid.
  certserialheader:
    type: str
    description:
      - Name of the header into which to insert the client serial number.
  certsubjectheader:
    type: str
    description:
      - Name of the header into which to insert the client certificate subject.
  cipher:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Insert the cipher suite that the client and the Citrix ADC negotiated for
        the SSL session into the HTTP header of the request being sent to the web
        server. The appliance inserts the cipher-suite name, SSL protocol, export
        or non-export string, and cipher strength bit, depending on the type of browser
        connecting to the SSL virtual server or service (for example, Cipher-Suite:
        RC4- MD5 SSLv3 Non-Export 128-bit).'
  cipherheader:
    type: str
    description:
      - Name of the header into which to insert the name of the cipher suite.
  clientauth:
    type: str
    choices:
      - DOCLIENTAUTH
      - NOCLIENTAUTH
    description:
      - Perform client certificate authentication.
  clientcert:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the entire client certificate into the HTTP header of the request being
        sent to the web server. The certificate is inserted in ASCII (PEM) format.
  clientcertfingerprint:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the certificate's fingerprint into the HTTP header of the request being
        sent to the web server. The fingerprint is derived by computing the specified
        hash value (SHA256, for example) of the DER-encoding of the client certificate.
  clientcerthash:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the certificate's signature into the HTTP header of the request being
        sent to the web server. The signature is the value extracted directly from
        the X.509 certificate signature field. All X.509 certificates contain a signature
        field.
  clientcertissuer:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the certificate issuer details into the HTTP header of the request
        being sent to the web server.
  clientcertnotafter:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the date of expiry of the certificate into the HTTP header of the request
        being sent to the web server. Every certificate is configured with the date
        and time at which the certificate expires.
  clientcertnotbefore:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the date from which the certificate is valid into the HTTP header of
        the request being sent to the web server. Every certificate is configured
        with the date and time from which it is valid.
  clientcertserialnumber:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the entire client serial number into the HTTP header of the request
        being sent to the web server.
  clientcertsubject:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the client certificate subject, also known as the distinguished name
        (DN), into the HTTP header of the request being sent to the web server.
  clientcertverification:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - Client certificate verification is mandatory or optional.
  forward:
    type: str
    description:
      - This action takes an argument a vserver name, to this vserver one will be
        able to forward all the packets.
  name:
    type: str
    description:
      - Name for the SSL action. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  owasupport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'If the appliance is in front of an Outlook Web Access (OWA) server, insert
        a special header field, FRONT-END-HTTPS: ON, into the HTTP requests going
        to the OWA server. This header communicates to the server that the transaction
        is HTTPS and not HTTP.'
  sessionid:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the SSL session ID into the HTTP header of the request being sent to
        the web server. Every SSL connection that the client and the Citrix ADC share
        has a unique ID that identifies the specific connection.
  sessionidheader:
    type: str
    description:
      - Name of the header into which to insert the Session ID.
  ssllogprofile:
    type: str
    description:
      - The name of the ssllogprofile.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslaction
      delegate_to: localhost
      netscaler.adc.sslaction:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: _XM_MDM_titan.dnpg-blr.com_ACTION
        clientcert: ENABLED
        certheader: NSClientCert
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
