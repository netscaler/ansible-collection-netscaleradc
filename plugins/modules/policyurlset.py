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
module: policyurlset
short_description: Configuration for URL set resource.
description: Configuration for URL set resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  canaryurl:
    description:
      - Add this URL to this urlset. Used for testing when contents of urlset is kept
        confidential.
    type: str
  comment:
    description:
      - Any comments to preserve information about this url set.
    type: str
  delimiter:
    description:
      - CSV file record delimiter.
    type: str
    default: 44
  imported:
    description:
      - when set, display shows all imported urlsets.
    type: bool
  interval:
    description:
      - The interval, in seconds, rounded down to the nearest 15 minutes, at which
        the update of urlset occurs.
    type: float
  matchedid:
    description:
      - An ID that would be sent to AppFlow to indicate which URLSet was the last
        one that matched the requested URL.
    type: float
    default: 1
  name:
    description:
      - Unique name of the url set. Not case sensitive. Must begin with an ASCII letter
        or underscore (_) character and must contain only alphanumeric and underscore
        characters. Must not be the name of an existing named expression, pattern
        set, dataset, string map, or HTTP callout.
    type: str
  overwrite:
    description:
      - Overwrites the existing file.
    type: bool
  privateset:
    description:
      - Prevent this urlset from being exported.
    type: bool
  rowseparator:
    description:
      - CSV file row separator.
    type: str
    default: 10
  subdomainexactmatch:
    description:
      - Force exact subdomain matching, ex. given an entry 'google.com' in the urlset,
        a request to 'news.google.com' won't match, if subdomainExactMatch is set.
    type: bool
  url:
    description:
      - 'URL (protocol, host, path and file name) from where the CSV (comma separated
        file) file will be imported or exported. Each record/line will one entry within
        the urlset. The first field contains the URL pattern, subsequent fields contains
        the metadata, if available. HTTP, HTTPS and FTP protocols are supported. NOTE:
        The operation fails if the destination HTTPS server requires client certificate
        authentication for access.'
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
