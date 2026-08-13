#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: mcpprofile
short_description: Configuration for mcpProfile resource.
description: Configuration for mcpProfile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  comment:
    type: str
    description:
      - Any information about the MCP profile.
  hostreplacement:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Whether the Host header should be replaced with the backend MCP server FQDN
        in FORWARD proxy mode. If mcpProxyMode is FORWARD, this parameter is C(ENABLED)
        bydefault. If mcpProxyMode is REVERSE, this parameter is C(DISABLED) and cannot
        be C(ENABLED).
  insertheaderinclientrequest:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Whether mcp_token_or_api configuration will be used for MCP requests coming
        from client.
  name:
    type: str
    description:
      - Name for the mcp profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my mcp profile").
  newname:
    type: str
    description:
      - New name for the mcpProfile. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
  profiletype:
    type: str
    choices:
      - BACKEND
      - FRONTEND
    description:
      - Type of MCP profile. Frontend profiles apply to the entity that receives requests
        from a client. Backend profiles apply to the entity that sends client requests
        to a server.
  protocolversion:
    type: str
    description:
      - MCP protocol version to advertise during monitoring of a mcp server.
  proxymode:
    type: str
    choices:
      - FORWARD
      - REVERSE
    description:
      - Proxy mode for the MCP profile. C(FORWARD) mode replaces Host and URL in backend
        requests. C(REVERSE) mode passes requests as-is.
  tokenorapi:
    type: str
    description:
      - If you like to insert Bearer or API token, configure this parameter with full
        header.
  urlreplacement:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Whether the URL should be replaced with the backend MCP server URL in FORWARD
        proxy mode. If mcpProxyMode is FORWARD, this parameter is C(ENABLED) bydefault.
        If mcpProxyMode is REVERSE, this parameter is C(DISABLED) and cannot be C(ENABLED).
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
