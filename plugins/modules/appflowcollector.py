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
module: appflowcollector
short_description: Configuration for AppFlow collector resource.
description: Configuration for AppFlow collector resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  ipaddress:
    description:
      - IPv4 address of the collector.
    type: str
  name:
    description:
      - Name for the collector. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at
      - (@), equals (=), and hyphen (-) characters.
      - ' Only four collectors can be configured. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow collector" or 'my appflow collector').
    type: str
  netprofile:
    description:
      - Netprofile to associate with the collector. The IP address defined in the
        profile is used as the source IP address for AppFlow traffic for this collector.  If
        you do not set this parameter, the Citrix ADC IP (NSIP) address is used as
        the source IP address.
    type: str
  newname:
    description:
      - New name for the collector. Must begin with an ASCII alphabetic or underscore
        (_) character, and must
      - 'contain only ASCII alphanumeric, underscore, hash (#), period (.), space,
        colon (:), at(@), equals (=), and hyphen (-) characters. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow coll" or 'my appflow coll').
    type: str
  port:
    description:
      - Port on which the collector listens.
    type: int
  transport:
    description:
      - 'Type of collector: either logstream or ipfix or rest.'
    type: str
    default: ipfix
    choices:
      - ipfix
      - logstream
      - rest
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
