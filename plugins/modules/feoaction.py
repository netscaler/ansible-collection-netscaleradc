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
module: feoaction
short_description: Configuration for Front end optimization action resource.
description: Configuration for Front end optimization action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  cachemaxage:
    description:
      - Maxage for cache extension.
    type: float
    default: 30
  clientsidemeasurements:
    description:
      - Send AppFlow records about the web pages optimized by this action. The records
        provide FEO statistics, such as the number of HTTP requests that have been
        reduced for this page. You must enable the Appflow feature before enabling
        this parameter.
    type: bool
  convertimporttolink:
    description:
      - Convert CSS import statements to HTML link tags.
    type: bool
  csscombine:
    description:
      - Combine one or more CSS files into one file.
    type: bool
  cssimginline:
    description:
      - Inline small images (less than 2KB) referred within CSS files as background-URLs
    type: bool
  cssinline:
    description:
      - Inline CSS files, whose size is less than 2KB, within the main page.
    type: bool
  cssminify:
    description:
      - Remove comments and whitespaces from CSSs.
    type: bool
  cssmovetohead:
    description:
      - Move any CSS file present within the body tag of an HTML page to the head
        tag.
    type: bool
  dnsshards:
    description:
      - Set of domain names that replaces the parent domain.
    type: list
    elements: str
  domainsharding:
    description:
      - Domain name of the server
    type: str
  htmlminify:
    description:
      - Remove comments and whitespaces from an HTML page.
    type: bool
  imggiftopng:
    description:
      - Convert GIF image formats to PNG formats.
    type: bool
  imginline:
    description:
      - Inline images whose size is less than 2KB.
    type: bool
  imglazyload:
    description:
      - Download images, only when the user scrolls the page to view them.
    type: bool
  imgshrinktoattrib:
    description:
      - Shrink image dimensions as per the height and width attributes specified in
        the <img> tag.
    type: bool
  imgtojpegxr:
    description:
      - Convert JPEG, GIF, PNG image formats to JXR format.
    type: bool
  imgtowebp:
    description:
      - Convert JPEG, GIF, PNG image formats to WEBP format.
    type: bool
  jpgoptimize:
    description:
      - Remove non-image data such as comments from JPEG images.
    type: bool
  jsinline:
    description:
      - Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
    type: bool
  jsminify:
    description:
      - Remove comments and whitespaces from JavaScript.
    type: bool
  jsmovetoend:
    description:
      - Move any JavaScript present in the body tag to the end of the body tag.
    type: bool
  name:
    description:
      - The name of the front end optimization action.
    type: str
  pageextendcache:
    description:
      - Extend the time period during which the browser can use the cached resource.
    type: bool
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
