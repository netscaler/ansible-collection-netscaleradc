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
module: uservserver
short_description: Configuration for virtual server resource.
description: Configuration for virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  Params:
    description:
      - Any comments associated with the protocol.
    type: str
  comment:
    description:
      - Any comments that you might want to associate with the virtual server.
    type: str
  defaultlb:
    description:
      - Name of the default Load Balancing virtual server used for load balancing
        of services. The protocol type of default Load Balancing virtual server should
        be a user type.
    type: str
  ipaddress:
    description:
      - IPv4 or IPv6 address to assign to the virtual server.
    type: str
  name:
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
    type: str
  port:
    description:
      - Port number for the virtual server.
    type: int
  state:
    description:
      - Initial state of the user vserver.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  userprotocol:
    description:
      - User protocol uesd by the service.
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
