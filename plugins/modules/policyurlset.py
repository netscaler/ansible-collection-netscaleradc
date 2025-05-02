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
---
module: policyurlset
short_description: Configuration for URL set resource.
description: Configuration for URL set resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - imported
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(imported), the resource will be imported on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  canaryurl:
    type: str
    description:
      - Add this URL to this urlset. Used for testing when contents of urlset is kept
        confidential.
  comment:
    type: str
    description:
      - Any comments to preserve information about this url set.
  delimiter:
    type: str
    description:
      - CSV file record delimiter.
  imported:
    type: bool
    description:
      - when set, display shows all imported urlsets.
  interval:
    type: float
    description:
      - The interval, in seconds, rounded down to the nearest 15 minutes, at which
        the update of urlset occurs.
  matchedid:
    type: float
    description:
      - An ID that would be sent to AppFlow to indicate which URLSet was the last
        one that matched the requested URL.
  name:
    type: str
    description:
      - Unique name of the url set. Not case sensitive. Must begin with an ASCII letter
        or underscore (_) character and must contain only alphanumeric and underscore
        characters. Must not be the name of an existing named expression, pattern
        set, dataset, string map, or HTTP callout.
  overwrite:
    type: bool
    description:
      - Overwrites the existing file.
  privateset:
    type: bool
    description:
      - Prevent this urlset from being exported.
  rowseparator:
    type: str
    description:
      - CSV file row separator.
  subdomainexactmatch:
    type: bool
    description:
      - Force exact subdomain matching, ex. given an entry 'google.com' in the urlset,
        a request to 'news.google.com' won't match, if subdomainExactMatch is set.
  url:
    type: str
    description:
      - 'URL (protocol, host, path and file name) from where the CSV (comma separated
        file) file will be imported or exported. Each record/line will one entry within
        the urlset. The first field contains the URL pattern, subsequent fields contains
        the metadata, if available. HTTP, HTTPS and FTP protocols are supported. NOTE:
        The operation fails if the destination HTTPS server requires client certificate
        authentication for access.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample policyurlset playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure policyurlset
      delegate_to: localhost
      netscaler.adc.policyurlset:
        state: present
        name: top10k
        imported: false
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
