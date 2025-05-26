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
module: sslcert
short_description: Configuration for cerificate resource.
description: Configuration for cerificate resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - created
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(created), the `create` operation will be applied on the resource.
    type: str
  cacert:
    type: str
    description:
      - Name of the CA certificate file that issues and signs the Intermediate-CA
        certificate or the end-user client and server certificates.
  cacertform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format of the CA certificate.
  cakey:
    type: str
    description:
      - Private key, associated with the CA certificate that is used to sign the Intermediate-CA
        certificate or the end-user client and server certificate. If the CA key file
        is password protected, the user is prompted to enter the pass phrase that
        was used to encrypt the key.
  cakeyform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format for the CA certificate.
  caserial:
    type: str
    description:
      - Serial number file maintained for the CA certificate. This file contains the
        serial number of the next certificate to be issued or signed by the CA. If
        the specified file does not exist, a new file is created, with /nsconfig/ssl/
        as the default path. If you do not specify a proper path for the existing
        serial file, a new serial file is created. This might change the certificate
        serial numbers assigned by the CA certificate to each of the certificates
        it signs.
  certfile:
    type: str
    description:
      - Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/
        is the default path.
  certform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format in which the certificate is stored on the appliance.
  certtype:
    type: str
    choices:
      - ROOT_CERT
      - INTM_CERT
      - CLNT_CERT
      - SRVR_CERT
    description:
      - 'Type of certificate to generate. Specify one of the following:'
      - '* C(ROOT_CERT) - Self-signed Root-CA certificate. You must specify the key
        file name. The generated Root-CA certificate can be used for signing end-user
        client or server certificates or to create Intermediate-CA certificates.'
      - '* C(INTM_CERT) - Intermediate-CA certificate.'
      - '* C(CLNT_CERT) - End-user client certificate used for client authentication.'
      - '* C(SRVR_CERT) - SSL server certificate used on SSL servers for end-to-end
        encryption.'
  days:
    type: float
    description:
      - Number of days for which the certificate will be valid, beginning with the
        time and day (system time) of creation.
  keyfile:
    type: str
    description:
      - Name for and, optionally, path to the private key. You can either use an existing
        RSA or DSA key that you own or create a new private key on the Citrix ADC.
        This file is required only when creating a self-signed Root-CA certificate.
        The key file is stored in the /nsconfig/ssl directory by default.
      - If the input key specified is an encrypted key, you are prompted to enter
        the PEM pass phrase that was used for encrypting the key.
  keyform:
    type: str
    choices:
      - DER
      - PEM
    description:
      - Format in which the key is stored on the appliance.
  pempassphrase:
    type: str
    description:
      - '0'
  reqfile:
    type: str
    description:
      - Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/
        is the default path.
  subjectaltname:
    type: str
    description:
      - 'Subject Alternative Name (SAN) is an extension to X.509 that allows various
        values to be associated with a security certificate using a subjectAltName
        field. These values are called "Subject Alternative Names" (SAN). Names include:'
      - '      1. Email addresses'
      - '      2. IP addresses'
      - '      3. URIs'
      - '      4. DNS names (This is usually also provided as the Common Name RDN
        within the Subject field of the main certificate.)'
      - '      5. directory names (alternative Distinguished Names to that given in
        the Subject)'
  sslcertkey_sslocspresponder_binding:
    type: dict
    description: Bindings for sslcertkey_sslocspresponder_binding resource
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
- name: Sample sslcert playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslcert
      delegate_to: localhost
      netscaler.adc.sslcert:
        state: present
        certfile: ssl_rsa_der_cert
        reqfile: ssl_rsa_der_csr
        certtype: ROOT_CERT
        keyfile: ssl_rsa_der_key
        keyform: DER
        days: '3650'
        certform: DER
        cacertform: PEM
        cakeyform: PEM
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
