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
module: nsappflowparam
short_description: Configuration for appflowParam resource.
description: Configuration for appflowParam resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  clienttrafficonly:
    choices:
      - true
      - false
    description:
      - Control whether AppFlow records should be generated only for client-side traffic.
    type: str
  httpcookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP cookie logging.
    type: str
    default: DISABLED
  httphost:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP host logging.
    type: str
    default: DISABLED
  httpmethod:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP method logging.
    type: str
    default: DISABLED
  httpreferer:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP referer logging.
    type: str
    default: DISABLED
  httpurl:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP URL logging.
    type: str
    default: DISABLED
  httpuseragent:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow HTTP user-agent logging.
    type: str
    default: DISABLED
  templaterefresh:
    description:
      - IPFIX template refresh interval (in seconds).
    type: int
    default: 600
  udppmtu:
    description:
      - MTU to be used for IPFIX UDP packets.
    type: int
    default: 1472
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
