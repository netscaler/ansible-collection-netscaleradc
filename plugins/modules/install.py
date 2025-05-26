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
module: install
short_description: Configuration for install resource.
description: Configuration for install resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - installed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(Install), the resource will be installed on the NetScaler ADC node.
    type: str
  async:
    type: bool
    description:
      - Use this flag to return the install id when the nitro api request is sent.
      - The id can be used later to track the installation progress via show ns job
        <id> command.
      - For the cli request of install the flag is by default set as false as the
        installation progress details can be tracked via cli
  a:
    type: bool
    description:
      - Use this flag to enable Citrix ADM Service Connect. This feature helps you
        discover your Citrix ADC instances effortlessly on Citrix ADM service and
        get insights and curated machine learning based recommendations for applications
        and Citrix ADC infrastructure. This feature lets the Citrix ADC instance automatically
        send system, usage and telemetry data to Citrix ADM service. View here [https://docs.citrix.com/en-us/citrix-adc/13/data-governance.html]
        to learn more about this feature. Use of this feature is subject to the Citrix
        End User ServiceAgreement. View here [https://www.citrix.com/buy/licensing/agreements.html].
  enhancedupgrade:
    type: bool
    description:
      - Use this flag for upgrading from/to enhancement mode.
  l:
    type: bool
    description:
      - Use this flag to enable callhome.
  resizeswapvar:
    type: bool
    description:
      - Use this flag to change swap size on ONLY 64bit nCore/MCNS/VMPE systems NON-VPX
        systems.
  url:
    type: str
    description:
      - 'Url for the build file. Must be in the following formats:'
      - http://[user]:[password]@host/path/to/file
      - https://[user]:[password]@host/path/to/file
      - sftp://[user]:[password]@host/path/to/file
      - scp://[user]:[password]@host/path/to/file
      - ftp://[user]:[password]@host/path/to/file
      - file://path/to/file
  y:
    type: bool
    description:
      - Do not prompt for yes/no before rebooting.
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
