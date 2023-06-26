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
module: netprofile
short_description: Configuration for Network profile resource.
description: Configuration for Network profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  mbf:
    description:
      - Response will be sent using learnt info if enabled. When creating a netprofile,
        if you do not set this parameter, the netprofile inherits the global MBF setting
        (available in the enable ns mode and disable ns mode CLI commands, or in the
        System > Settings > Configure modes > Configure Modes dialog box). However,
        you can override this setting after you create the netprofile
    type: str
    choices:
      - ENABLED
      - DISABLED
  name:
    description:
      - Name for the net profile. Must begin with a letter, number, or the underscore
        character (_), and can consist of letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the profile is created. Choose a name
        that helps identify the net profile.
    type: str
  overridelsn:
    description:
      - USNIP/USIP settings override LSN settings for configured
      - '              service/virtual server traffic..'
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  proxyprotocol:
    description:
      - Proxy Protocol Action (Enabled/Disabled)
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  proxyprotocolaftertlshandshake:
    description:
      - ADC doesnt look for proxy header before TLS handshake, if enabled. Proxy protocol
        parsed after TLS handshake
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  proxyprotocoltxversion:
    description:
      - Proxy Protocol Version (V1/V2)
    type: str
    default: V1
    choices:
      - V1
      - V2
  srcip:
    description:
      - IP address or the name of an IP set.
    type: str
  srcippersistency:
    description:
      - When the net profile is associated with a virtual server or its bound services,
        this option enables the Citrix ADC to use the same  address, specified in
        the net profile, to communicate to servers for all sessions initiated from
        a particular client to the virtual server.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
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