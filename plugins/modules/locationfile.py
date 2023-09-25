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
module: locationfile
short_description: Configuration for location file resource.
description: Configuration for location file resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  Locationfile:
    description:
      - Name of the location file, with or without absolute path. If the path is not
        included, the default path (/var/netscaler/locdb) is assumed. In a high availability
        setup, the static database must be stored in the same location on both Citrix
        ADCs.
    type: str
  format:
    choices:
      - netscaler
      - ip-country
      - ip-country-isp
      - ip-country-region-city
      - ip-country-region-city-isp
      - geoip-country
      - geoip-region
      - geoip-city
      - geoip-country-org
      - geoip-country-isp
      - geoip-city-isp-org
    description:
      - Format of the location file. Required for the Citrix ADC to identify how to
        read the location file.
    type: str
    default: netscaler
  src:
    description:
      - URL \(protocol, host, path, and file name\) from where the location file will
        be imported.
      - '            NOTE: The import fails if the object to be imported is on an
        HTTPS server that requires client certificate authentication for access.'
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
