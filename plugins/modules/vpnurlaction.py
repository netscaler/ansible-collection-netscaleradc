#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: vpnurlaction
short_description: Configuration for VPN url action resource.
description: Configuration for VPN url action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  actualurl:
    description:
      - Web address for the bookmark link.
    type: str
  applicationtype:
    choices:
      - CVPN
      - VPN
      - SaaS
    description:
      - The type of application this C(VPN) URL represents. Possible values are C(CVPN)/C(SaaS)/C(VPN)
    type: str
  clientlessaccess:
    choices:
      - true
      - false
    description:
      - If clientless access to the resource hosting the link is allowed, also use
        clientless access for the bookmarked web address in the Secure Client Access
        based session. Allows single sign-on and other HTTP processing on NetScaler
        Gateway for HTTPS resources.
    type: str
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
  name:
    description:
      - Name of the bookmark link.
    type: str
  newname:
    description:
      - New name for the vpn urlAction.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the NetScaler CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my vpnurl action" or 'my vpnurl action').
    type: str
  samlssoprofile:
    description:
      - Profile to be used for doing SAML SSO
    type: str
  ssotype:
    choices:
      - unifiedgateway
      - selfauth
      - samlauth
    description:
      - Single sign on type for unified gateway
    type: str
  vservername:
    description:
      - Name of the associated vserver to handle selfAuth SSO
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
