#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: sslcertkey
short_description: Configuration for certificate key resource.
description: Configuration for certificate key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bundle:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Parse the certificate chain as a single file after linking the server certificate
        to its issuer's certificate within the file.
    type: str
    default: 'NO'
  cert:
    description:
      - Name of and, optionally, path to the X509 certificate file that is used to
        form the certificate-key pair. The certificate file should be present on the
        appliance's hard-disk drive or solid-state drive. Storing a certificate in
        any location other than the default might cause inconsistency in a high availability
        setup. /nsconfig/ssl/ is the default path.
    type: str
  certkey:
    description:
      - Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the certificate-key pair is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cert" or 'my cert').
    type: str
  deletefromdevice:
    description:
      - Delete cert/key file from file system.
    type: bool
  expirymonitor:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Issue an alert when the certificate is about to expire.
    type: str
  fipskey:
    description:
      - Name of the FIPS key that was created inside the Hardware Security Module
        (HSM) of a FIPS appliance, or a key that was imported into the HSM.
    type: str
  hsmkey:
    description:
      - Name of the HSM key that was created in the External Hardware Security Module
        (HSM) of a FIPS appliance.
    type: str
  inform:
    choices:
      - DER
      - PEM
      - PFX
    description:
      - 'Input format of the certificate and the private-key files. The three formats
        supported by the appliance are:'
      - C(PEM) - Privacy Enhanced Mail
      - C(DER) - Distinguished Encoding Rule
      - C(PFX) - Personal Information Exchange
    type: str
    default: PEM
  key:
    description:
      - Name of and, optionally, path to the private-key file that is used to form
        the certificate-key pair. The certificate file should be present on the appliance's
        hard-disk drive or solid-state drive. Storing a certificate in any location
        other than the default might cause inconsistency in a high availability setup.
        /nsconfig/ssl/ is the default path.
    type: str
  linkcertkeyname:
    description:
      - Name of the Certificate Authority certificate-key pair to which to link a
        certificate-key pair.
    type: str
  nodomaincheck:
    description:
      - Override the check for matching domain names during a certificate update operation.
    type: bool
  notificationperiod:
    description:
      - Time, in number of days, before certificate expiration, at which to generate
        an alert that the certificate is about to expire.
    type: float
  ocspstaplingcache:
    description:
      - Clear cached ocspStapling response in certkey.
    type: bool
  passplain:
    description:
      - Pass phrase used to encrypt the private-key. Required when adding an encrypted
        private-key in PEM format.
    type: str
  password:
    description:
      - Passphrase that was used to encrypt the private-key. Use this option to load
        encrypted private-keys in PEM format.
    type: bool
  sslcertkey_sslocspresponder_binding:
    type: dict
    description: Bindings for sslcertkey_sslocspresponder_binding resource
    suboptions:
      mode:
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
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | sslcertKey
      delegate_to: localhost
      netscaler.adc.sslcertkey:
        state: present
        certkey: ns-server-certificate
        cert: ns-server.cert
        key: ns-server.key
        password: false

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
