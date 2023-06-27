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
module: lsnip6profile
short_description: Configuration for LSN ip6 Profile resource.
description: Configuration for LSN ip6 Profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  name:
    description:
      - 'Name for the LSN ip6 profile. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the LSN ip6 profile is created. The following requirement
        applies only to the Citrix ADC CLI: If the name includes one or more spaces,
        enclose the name in double or single quotation marks (for example, "lsn ip6
        profile1" or ''lsn ip6 profile1'').'
    type: str
  natprefix:
    description:
      - IPv6 address(es) of the LSN subscriber(s) or subscriber network(s) on whose
        traffic you want the Citrix ADC to perform Large Scale NAT.
    type: str
  network6:
    description:
      - IPv6 address of the Citrix ADC AFTR device
    type: str
  type:
    choices:
      - DS-Lite
      - NAT64
    description:
      - IPv6 translation type for which to set the LSN IP6 profile parameters.
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
