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
module: dnskey
short_description: Configuration for dns key resource.
description: Configuration for dns key resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
      - created
      - imported
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(created), the `create` operation will be applied on the resource.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  algorithm:
    type: str
    choices:
      - RSASHA1
      - RSASHA256
      - RSASHA512
    description:
      - Algorithm to generate for zone signing.
  expires:
    type: raw
    description:
      - Time period for which to consider the key valid, after the key is used to
        sign a zone.
  filenameprefix:
    type: str
    description:
      - Common prefix for the names of the generated public and private key files
        and the Delegation Signer (DS) resource record. During key generation, the
        .key, .private, and .ds suffixes are appended automatically to the file name
        prefix to produce the names of the public key, the private key, and the DS
        record, respectively.
  keyname:
    type: raw
    description:
      - Name of the public-private key pair to publish in the zone.
  keysize:
    type: float
    description:
      - Size of the key, in bits.
  keytype:
    type: str
    choices:
      - KSK
      - KeySigningKey
      - ZSK
      - ZoneSigningKey
    description:
      - Type of key to create.
  notificationperiod:
    type: raw
    description:
      - Time at which to generate notification of key expiration, specified as number
        of days, hours, or minutes before expiry. Must be less than the expiry period.
        The notification is an SNMP trap sent to an SNMP manager. To enable the appliance
        to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.
  password:
    type: str
    description:
      - Passphrase for reading the encrypted public/private DNS keys
  privatekey:
    type: str
    description:
      - File name of the private key.
  publickey:
    type: str
    description:
      - File name of the public key.
  src:
    type: str
    description:
      - 'URL (protocol, host, path, and file name) from where the DNS key file will
        be imported. NOTE: The import fails if the object to be imported is on an
        HTTPS server that requires client certificate authentication for access. This
        is a mandatory argument'
  ttl:
    type: raw
    description:
      - Time to Live (TTL), in seconds, for the DNSKEY resource record created in
        the zone. TTL is the time for which the record must be cached by the DNS proxies.
        If the TTL is not specified, either the DNS zone's minimum TTL or the default
        value of 3600 is used.
  units1:
    type: raw
    choices:
      - MINUTES
      - HOURS
      - DAYS
    description:
      - Units for the expiry period.
  units2:
    type: raw
    choices:
      - MINUTES
      - HOURS
      - DAYS
    description:
      - Units for the notification period.
  zonename:
    type: str
    description:
      - Name of the zone for which to create a key.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
