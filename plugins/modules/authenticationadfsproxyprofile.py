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
module: authenticationadfsproxyprofile
short_description: Configuration for ADFSProxy Profile resource.
description: Configuration for ADFSProxy Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  certkeyname:
    description:
      - SSL certificate of the proxy that is registered at adfs server for trust.
    type: str
  name:
    description:
      - Name for the adfs proxy profile. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Cannot be changed after the profile is created.
      - "\t    CLI Users: If the name includes one or more spaces, enclose the name\
        \ in double or single quotation marks (for example, \"my push service\" or\
        \ 'my push service')."
    type: str
  password:
    description:
      - This is the password of an account in directory that would be used to authenticate
        trust request from ADC acting as a proxy.
    type: str
  serverurl:
    description:
      - Fully qualified url of the adfs server.
    type: str
  username:
    description:
      - This is the name of an account in directory that would be used to authenticate
        trust request from ADC acting as a proxy.
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
