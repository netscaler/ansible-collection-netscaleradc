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
module: dnsaction
short_description: Configuration for DNS action resource.
description: Configuration for DNS action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  actionname:
    description:
      - Name of the dns action.
    type: str
  actiontype:
    description:
      - The type of DNS action that is being configured.
    type: str
    choices:
      - ViewName
      - GslbPrefLoc
      - noop
      - Drop
      - Cache_Bypass
      - Rewrite_Response
  dnsprofilename:
    description:
      - Name of the DNS profile to be associated with the transaction for which the
        action is chosen
    type: str
  ipaddress:
    description:
      - List of IP address to be returned in case of rewrite_response actiontype.
        They can be of IPV4 or IPV6 type.
      - "\t    In case of set command We will remove all the IP address previously\
        \ present in the action and will add new once given in set dns action command."
    type: list
    elements: str
  preferredloclist:
    description:
      - The location list in priority order used for the given action.
    type: list
    elements: str
  ttl:
    description:
      - Time to live, in seconds.
    type: int
    default: 3600
  viewname:
    description:
      - The view name that must be used for the given action.
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
