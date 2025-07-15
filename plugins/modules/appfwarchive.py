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
module: appfwarchive
short_description: Configuration for archive resource.
description: Configuration for archive resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - absent
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
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
      - Comments associated with this archive.
  name:
    type: str
    description:
      - Name of tar archive
  src:
    type: str
    description:
      - Indicates the source of the tar archive file as a URL
      - of the form
      - ''
      - '    <protocol>://<host>[:<port>][/<path>]'
      - ''
      - <protocol> is http or https.
      - <host> is the DNS name or IP address of the http or https server.
      - <port> is the port number of the server. If omitted, the
      - default port for http or https will be used.
      - <path> is the path of the file on the server.
      - ''
      - Import will fail if an https server requires client
      - certificate authentication.
  target:
    type: str
    description:
      - Path to the file to be exported
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
