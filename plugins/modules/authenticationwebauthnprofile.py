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
module: authenticationwebauthnprofile
short_description: Configuration for WebAuthn Profile to hold FIDO2 information resource.
description: Configuration for WebAuthn Profile to hold FIDO2 information resource.
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
  allowedattstmtfmt:
    type: list
    choices:
      - none
      - tpm
    description:
      - 'Allowed attestation statement format, automatically derived from attestationPreference:
        ''C(none)'' allows only ''C(none)'' format; ''direct'' allows only ''C(tpm)''
        format.'
    elements: str
  attestationpreference:
    type: str
    choices:
      - none
      - direct
    description:
      - Controls the attestation conveyance preference during WebAuthn credential
        creation. NetScaler uses the AttestationConveyancePreference to specify its
        preference regarding attestation conveyance during credential registration.
      - 'C(none): NetScaler is not interested in authenticator attestation.'
      - 'C(direct): NetScaler wants to receive the attestation statement as generated
        by the authenticator, allowing verification of the device type and provenance.'
  authenticatorattachment:
    type: str
    choices:
      - platform
      - any
      - cross-platform
    description:
      - 'Authenticator attachment modality for credential creation. C(platform): require
        a C(platform) authenticator (e.g. Windows Hello, Touch ID). C(cross-platform):
        require a roaming authenticator (e.g. FIDO2 USB/NFC key). C(any): no restriction
        - omits the authenticatorAttachment field so C(any) authenticator type may
        be used.'
  fidoattribute:
    type: str
    description:
      - Active Directory attribute used to store FIDO2 device credential information
        for the authenticating user. NetScaler reads and writes this attribute during
        WebAuthn credential registration and authentication.
  name:
    type: str
    description:
      - Name for the WebAuthn Profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Cannot be changed after the profile is created.
      - "\t    CLI Users: If the name includes one or more spaces, enclose the name\
        \ in double or single quotation marks (for example, \"my webauthn profile\"\
        \ or 'my webauthn profile')."
  pubkeycredparamsalgorithms:
    type: list
    choices:
      - ES256
      - RS256
    description:
      - List of the key types and signature COSE algorithms the NetScaler, as Relying
        Party, supports to advertise, ordered from most preferred to least preferred.
        The client and authenticator make a best-effort to create a credential of
        the most preferred type possible.
    elements: str
  requesttimeout:
    type: int
    description:
      - Timeout in seconds for WebAuthn authenticator interactions (credential creation
        during registration and assertion during authentication). A value of 0 uses
        the global default of 15 seconds.
  residentkey:
    type: str
    choices:
      - discouraged
      - preferred
      - required
    description:
      - 'Resident key (discoverable credential) preference for credential creation.
        C(discouraged): prefer a server-side credential (default). C(preferred): use
        a discoverable credential if the authenticator supports it. C(required): require
        a discoverable credential; registration will fail if the authenticator cannot
        create one.'
  userverification:
    type: str
    choices:
      - preferred
      - required
      - discouraged
    description:
      - 'User verification requirement enforced by the authenticator during both credential
        creation and authentication. C(preferred): use UV if supported (default, recommended).
        C(required): UV is mandatory; the authenticator must verify the user. C(discouraged):
        skip UV even if supported (not recommended for high-assurance scenarios).'
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
