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
module: nscentralmanagementserver
short_description: Configuration for centralmanagementserver resource.
description: Configuration for centralmanagementserver resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  activationcode:
    description:
      - Activation code is used to register to ADM service
    type: str
  adcpassword:
    description:
      - ADC password used to create device profile on ADM
    type: str
  adcusername:
    description:
      - ADC username used to create device profile on ADM
    type: str
  deviceprofilename:
    description:
      - Device profile is created on ADM and contains the user name and password of
        the instance(s).
    type: str
  ipaddress:
    description:
      - Ip Address of central management server.
    type: str
  password:
    description:
      - Password for access to central management server. Required for any user account.
    type: str
  servername:
    description:
      - Fully qualified domain name of the central management server or service-url
        to locate ADM service.
    type: str
  type:
    choices:
      - CLOUD
      - ONPREM
    description:
      - Type of the central management server. Must be either C(CLOUD) or C(ONPREM)
        depending on whether the server is on the cloud or on premise.
    type: str
  username:
    description:
      - Username for access to central management server. Must begin with a letter,
        number, or the underscore character (_), and must contain only letters, numbers,
        and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or
      - single quotation marks (for example, "my ns centralmgmtserver" or "my ns centralmgmtserver").
    type: str
  validatecert:
    choices:
      - 'YES'
      - 'NO'
    description:
      - validate the server certificate for secure SSL connections.
    type: str
    default: 'YES'
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
