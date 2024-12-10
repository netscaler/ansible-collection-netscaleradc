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
module: nscentralmanagementserver
short_description: Configuration for centralmanagementserver resource.
description: Configuration for centralmanagementserver resource.
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
  activationcode:
    type: str
    description:
      - Activation code is used to register to ADM service
  adcpassword:
    type: str
    description:
      - ADC password used to create device profile on ADM
  adcusername:
    type: str
    description:
      - ADC username used to create device profile on ADM
  deviceprofilename:
    type: str
    description:
      - Device profile is created on ADM and contains the user name and password of
        the instance(s).
  ipaddress:
    type: str
    description:
      - Ip Address of central management server.
  password:
    type: str
    description:
      - Password for access to central management server. Required for any user account.
  servername:
    type: str
    description:
      - Fully qualified domain name of the central management server or service-url
        to locate ADM service.
  type:
    type: str
    choices:
      - CLOUD
      - ONPREM
    description:
      - Type of the central management server. Must be either C(CLOUD) or C(ONPREM)
        depending on whether the server is on the cloud or on premise.
  username:
    type: str
    description:
      - Username for access to central management server. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or
      - single quotation marks (for example, "my ns centralmgmtserver" or "my ns centralmgmtserver").
  validatecert:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - validate the server certificate for secure SSL connections.
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
