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
module: sslcertkey
short_description: Configuration for certificate key resource.
description: Configuration for certificate key resource.
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
  bundle:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Parse the certificate chain as a single file after linking the server certificate
        to its issuer's certificate within the file.
  cert:
    type: str
    description:
      - Name of and, optionally, path to the X509 certificate file that is used to
        form the certificate-key pair. The certificate file should be present on the
        appliance's hard-disk drive or solid-state drive. Storing a certificate in
        any location other than the default might cause inconsistency in a high availability
        setup. /nsconfig/ssl/ is the default path.
  certkey:
    type: str
    description:
      - Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the certificate-key pair is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cert" or 'my cert').
  deletecertkeyfilesonremoval:
    type: str
    choices:
      - 'NO'
      - ALWAYS
      - IF_EXPIRED
    description:
      - This option is used to automatically delete certificate/key files from physical
        device when the added certkey is removed. When deleteCertKeyFilesOnRemoval
        option is used at rm certkey command, it overwrites the deleteCertKeyFilesOnRemoval
        setting used at add/set certkey command
  deletefromdevice:
    type: bool
    description:
      - Delete cert/key file from file system.
  expirymonitor:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Issue an alert when the certificate is about to expire.
  fipskey:
    type: str
    description:
      - Name of the FIPS key that was created inside the Hardware Security Module
        (HSM) of a FIPS appliance, or a key that was imported into the HSM.
  hsmkey:
    type: str
    description:
      - Name of the HSM key that was created in the External Hardware Security Module
        (HSM) of a FIPS appliance.
  inform:
    type: str
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
  key:
    type: str
    description:
      - Name of and, optionally, path to the private-key file that is used to form
        the certificate-key pair. The certificate file should be present on the appliance's
        hard-disk drive or solid-state drive. Storing a certificate in any location
        other than the default might cause inconsistency in a high availability setup.
        /nsconfig/ssl/ is the default path.
  linkcertkeyname:
    type: str
    description:
      - Name of the Certificate Authority certificate-key pair to which to link a
        certificate-key pair.
  nodomaincheck:
    type: bool
    description:
      - Override the check for matching domain names during a certificate update operation.
  notificationperiod:
    type: int
    description:
      - Time, in number of days, before certificate expiration, at which to generate
        an alert that the certificate is about to expire.
  ocspstaplingcache:
    type: bool
    description:
      - Clear cached ocspStapling response in certkey.
  passplain:
    type: str
    description:
      - Pass phrase used to encrypt the private-key. Required when adding an encrypted
        private-key in PEM format.
  password:
    type: bool
    description:
      - Passphrase that was used to encrypt the private-key. Use this option to load
        encrypted private-keys in PEM format.
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
- name: Sample sslcertkey playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslcertkey
      delegate_to: localhost
      netscaler.adc.sslcertkey:
        state: present
        certkey: samlssokp1
        cert: ns-root.cert
        inform: PEM
        expirymonitor: ENABLED
        notificationperiod: '30'
        bundle: 'NO'
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
