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
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  cachemaxage:
    type: float
    description:
      - Maxage for cache extension.
  clientsidemeasurements:
    type: raw
    description:
      - Send AppFlow records about the web pages optimized by this action. The records
        provide FEO statistics, such as the number of HTTP requests that have been
        reduced for this page. You must enable the Appflow feature before enabling
        this parameter.
  convertimporttolink:
    type: raw
    description:
      - Convert CSS import statements to HTML link tags.
  csscombine:
    type: raw
    description:
      - Combine one or more CSS files into one file.
  cssimginline:
    type: raw
    description:
      - Inline small images (less than 2KB) referred within CSS files as background-URLs
  cssinline:
    type: raw
    description:
      - Inline CSS files, whose size is less than 2KB, within the main page.
  cssminify:
    type: raw
    description:
      - Remove comments and whitespaces from CSSs.
  cssmovetohead:
    type: raw
    description:
      - Move any CSS file present within the body tag of an HTML page to the head
        tag.
  dnsshards:
    type: list
    description:
      - Set of domain names that replaces the parent domain.
    elements: str
  domainsharding:
    type: raw
    description:
      - Domain name of the server
  htmlminify:
    type: raw
    description:
      - Remove comments and whitespaces from an HTML page.
  imggiftopng:
    type: raw
    description:
      - Convert GIF image formats to PNG formats.
  imginline:
    type: raw
    description:
      - Inline images whose size is less than 2KB.
  imglazyload:
    type: raw
    description:
      - Download images, only when the user scrolls the page to view them.
  imgshrinktoattrib:
    type: raw
    description:
      - Shrink image dimensions as per the height and width attributes specified in
        the <img> tag.
  imgtojpegxr:
    type: raw
    description:
      - Convert JPEG, GIF, PNG image formats to JXR format.
  imgtowebp:
    type: raw
    description:
      - Convert JPEG, GIF, PNG image formats to WEBP format.
  jpgoptimize:
    type: raw
    description:
      - Remove non-image data such as comments from JPEG images.
  jsinline:
    type: raw
    description:
      - Convert linked JavaScript files (less than 2KB) to inline JavaScript files.
  jsminify:
    type: raw
    description:
      - Remove comments and whitespaces from JavaScript.
  jsmovetoend:
    type: raw
    description:
      - Move any JavaScript present in the body tag to the end of the body tag.
  name:
    type: raw
    description:
      - The name of the front end optimization action.
  pageextendcache:
    type: raw
    description:
      - Extend the time period during which the browser can use the cached resource.
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
