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
module: sslvserver_sslcertkey_binding
short_description: Binding Resource definition for describing association between
  sslvserver and sslcertkey resources
description: Binding Resource definition for describing association between sslvserver
  and sslcertkey resources
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
  ca:
    type: bool
    description:
      - CA certificate.
  certkeyname:
    type: str
    description:
      - The name of the certificate key pair binding.
  crlcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the CRL check parameter. (C(Mandatory)/C(Optional))
  ocspcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the OCSP check parameter. (C(Mandatory)/C(Optional))
  skipcaname:
    type: bool
    description:
      - The flag is used to indicate whether this particular CA certificate's CA_Name
        needs to be sent to the SSL client while requesting for client certificate
        in a SSL handshake
  snicert:
    type: bool
    description:
      - The name of the CertKey. Use this option to bind Certkey(s) which will be
        used in SNI processing.
  vservername:
    type: str
    description:
      - Name of the SSL virtual server.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample sslvserver_sslcertkey_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure sslvserver_sslcertkey_binding
      delegate_to: localhost
      netscaler.adc.sslvserver_sslcertkey_binding:

        state: present
        vservername: CitrixAccessCallback
        certkeyname: callback.blackstone.com
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
