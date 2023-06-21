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
module: dnskey
short_description: Configuration for dns key resource.
description: Configuration for dns key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  algorithm:
    description:
      - Algorithm to generate for zone signing.
    type: str
    default: RSASHA1
    choices:
      - RSASHA1
      - RSASHA256
      - RSASHA512
  expires:
    description:
      - Time period for which to consider the key valid, after the key is used to
        sign a zone.
    type: int
    default: 120
  filenameprefix:
    description:
      - Common prefix for the names of the generated public and private key files
        and the Delegation Signer (DS) resource record. During key generation, the
        .key, .private, and .ds suffixes are appended automatically to the file name
        prefix to produce the names of the public key, the private key, and the DS
        record, respectively.
    type: str
  keyname:
    description:
      - Name of the public-private key pair to publish in the zone.
    type: str
  keysize:
    description:
      - Size of the key, in bits.
    type: int
    default: 512
  keytype:
    description:
      - Type of key to create.
    type: str
    default: ZSK
    choices:
      - KSK
      - KeySigningKey
      - ZSK
      - ZoneSigningKey
  notificationperiod:
    description:
      - Time at which to generate notification of key expiration, specified as number
        of days, hours, or minutes before expiry. Must be less than the expiry period.
        The notification is an SNMP trap sent to an SNMP manager. To enable the appliance
        to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.
    type: int
    default: 7
  password:
    description:
      - Passphrase for reading the encrypted public/private DNS keys
    type: str
  privatekey:
    description:
      - File name of the private key.
    type: str
  publickey:
    description:
      - File name of the public key.
    type: str
  src:
    description:
      - 'URL (protocol, host, path, and file name) from where the DNS key file will
        be imported. NOTE: The import fails if the object to be imported is on an
        HTTPS server that requires client certificate authentication for access. This
        is a mandatory argument'
    type: str
  ttl:
    description:
      - Time to Live (TTL), in seconds, for the DNSKEY resource record created in
        the zone. TTL is the time for which the record must be cached by the DNS proxies.
        If the TTL is not specified, either the DNS zone's minimum TTL or the default
        value of 3600 is used.
    type: int
    default: 3600
  units1:
    description:
      - Units for the expiry period.
    type: str
    default: DAYS
    choices:
      - MINUTES
      - HOURS
      - DAYS
  units2:
    description:
      - Units for the notification period.
    type: str
    default: DAYS
    choices:
      - MINUTES
      - HOURS
      - DAYS
  zonename:
    description:
      - Name of the zone for which to create a key.
    type: str
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
