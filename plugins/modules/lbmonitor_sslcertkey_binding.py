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
module: lbmonitor_sslcertkey_binding
short_description: Binding Resource definition for describing association between
  lbmonitor and sslcertkey resources
description: Binding Resource definition for describing association between lbmonitor
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
      - The rule for use of CRL corresponding to this CA certificate during client
        authentication. If crlCheck is set to Mandatory, the system will deny all
        SSL clients if the CRL is missing, expired - NextUpdate date is in the past,
        or is incomplete with remote CRL refresh enabled. If crlCheck is set to optional,
        the system will allow SSL clients in the above error cases.However, in any
        case if the client certificate is revoked in the CRL, the SSL client will
        be denied access.
  certkeyname:
    type: str
    description:
      - The name of the certificate bound to the monitor.
  crlcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the CRL check parameter. (C(Mandatory)/C(Optional))
  monitorname:
    type: str
    description:
      - Name of the monitor.
  ocspcheck:
    type: str
    choices:
      - Mandatory
      - Optional
    description:
      - The state of the OCSP check parameter. (C(Mandatory)/C(Optional))
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lbmonitor_sslcertkey_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lbmonitor_sslcertkey_binding
      delegate_to: localhost
      netscaler.adc.lbmonitor_sslcertkey_binding:
        state: present
        monitorname: https
        certkeyname: myclient
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
