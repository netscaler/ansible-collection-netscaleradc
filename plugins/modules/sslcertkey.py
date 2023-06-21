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
module: sslcertkey
short_description: Configuration for certificate key resource.
description: Configuration for certificate key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bundle:
    description:
      - Parse the certificate chain as a single file after linking the server certificate
        to its issuer's certificate within the file.
    type: str
    choices:
      - true
      - false
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
    description:
      - Issue an alert when the certificate is about to expire.
    type: str
    choices:
      - ENABLED
      - DISABLED
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
    description:
      - 'Input format of the certificate and the private-key files. The three formats
        supported by the appliance are:'
      - PEM - Privacy Enhanced Mail
      - DER - Distinguished Encoding Rule
      - PFX - Personal Information Exchange
    type: str
    default: PEM
    choices:
      - DER
      - PEM
      - PFX
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
    type: int
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
