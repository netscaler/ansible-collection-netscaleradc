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
module: sslcertkeybundle
short_description: Configuration for certkey bundle resource.
description: Configuration for certkey bundle resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - changed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(changed), the resource will be changed(?action=update) on the NetScaler
        ADC node.
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
  bundlefile:
    type: str
    description:
      - Name of and, optionally, path to the X509 certificate bundle file that is
        used to form the certificate-key bundle. The certificate bundle file should
        be present on the appliance's hard-disk drive or solid-state drive. /nsconfig/ssl/
        is the default path. The certificate bundle file consists of list of certificates
        and one key in PEM format.
  certkeybundlename:
    type: str
    description:
      - 'Name given to the cerKeyBundle. The name will be used to bind/unbind certkey
        bundle to vip. Must begin with an ASCII alphanumeric or underscore (_) character,
        and must contain only ASCII alphanumeric, underscore, hash (#), period (.),
        space, colon (:), at (@), equals (=), and hyphen (-) characters. The following
        requirement applies only to the Citrix ADC CLI: If the name includes one or
        more spaces, enclose the name in double or single quotation marks (for example,
        "my file" or ''my file'').'
  passplain:
    type: str
    description:
      - Pass phrase used to encrypt the private-key. Required when certificate bundle
        file contains encrypted private-key in PEM format.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslcertkeybundle playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslcertkeybundle
      delegate_to: localhost
      netscaler.adc.sslcertkeybundle:
        state: present
        certkeybundlename: tc11
        bundlefile: bundle_files/enc_cert.pem
        passplain: '123456'
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
