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
module: nshttpparam
short_description: Configuration for HTTP parameter resource.
description: Configuration for HTTP parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  conmultiplex:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Reuse server connections for requests from more than one client connections.
  dropinvalreqs:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Drop invalid HTTP requests or responses.
  http2serverside:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable/Disable HTTP/2 on server side
  ignoreconnectcodingscheme:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Ignore Coding scheme in CONNECT request.
  insnssrvrhdr:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable Citrix ADC server header insertion for Citrix ADC generated
        HTTP responses.
  logerrresp:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Server header value to be inserted.
  markconnreqinval:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Mark CONNECT requests as invalid.
  markhttp09inval:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Mark HTTP/0.9 requests as invalid.
  maxreusepool:
    type: raw
    description:
      - Maximum limit on the number of connections, from the Citrix ADC to a particular
        server that are kept in the reuse pool. This setting is helpful for optimal
        memory utilization and for reducing the idle connections to the server just
        after the peak time.
  nssrvrhdr:
    type: raw
    description:
      - The server header value to be inserted. If no explicit header is specified
        then NSBUILD.RELEASE is used as default server header.
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
