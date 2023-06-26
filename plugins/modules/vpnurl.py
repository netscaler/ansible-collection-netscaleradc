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
module: vpnurl
short_description: Configuration for VPN URL resource.
description: Configuration for VPN URL resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  actualurl:
    description:
      - Web address for the bookmark link.
    type: str
  appjson:
    description:
      - To store the template details in the json format.
    type: str
  applicationtype:
    description:
      - The type of application this VPN URL represents. Possible values are CVPN/SaaS/VPN
    type: str
    choices:
      - CVPN
      - VPN
      - SaaS
  clientlessaccess:
    description:
      - If clientless access to the resource hosting the link is allowed, also use
        clientless access for the bookmarked web address in the Secure Client Access
        based session. Allows single sign-on and other HTTP processing on Citrix Gateway
        for HTTPS resources.
    type: str
    choices:
      - true
      - false
  comment:
    description:
      - Any comments associated with the bookmark link.
    type: str
  iconurl:
    description:
      - URL to fetch icon file for displaying this resource.
    type: str
  linkname:
    description:
      - Description of the bookmark link. The description appears in the Access Interface.
    type: str
  samlssoprofile:
    description:
      - Profile to be used for doing SAML SSO
    type: str
  ssotype:
    description:
      - Single sign on type for unified gateway
    type: str
    choices:
      - unifiedgateway
      - selfauth
      - samlauth
  urlname:
    description:
      - Name of the bookmark link.
    type: str
  vservername:
    description:
      - Name of the associated LB/CS vserver
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