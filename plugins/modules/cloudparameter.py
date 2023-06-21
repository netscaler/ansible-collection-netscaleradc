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
module: cloudparameter
short_description: Configuration for cloud parameter resource.
description: Configuration for cloud parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  activationcode:
    description:
      - Activation code for the NGS Connector instance
    type: str
  connectorresidence:
    description:
      - Identifies whether the connector is located Onprem, Aws or Azure
    type: str
    choices:
      - None
      - Onprem
      - Aws
      - Azure
      - Cpx
  controllerfqdn:
    description:
      - FQDN of the controller to which the Citrix ADC SDProxy Connects
    type: str
  controllerport:
    description:
      - Port number of the controller to which the Citrix ADC SDProxy connects
    type: int
  customerid:
    description:
      - Customer ID of the citrix cloud customer
    type: str
  deployment:
    description:
      - Describes if the customer is a Staging/Production or Dev Citrix Cloud customer
    type: str
    choices:
      - Production
      - Staging
      - Dev
  instanceid:
    description:
      - Instance ID of the customer provided by Trust
    type: str
  resourcelocation:
    description:
      - Resource Location of the customer provided by Trust
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
