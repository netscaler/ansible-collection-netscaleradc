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
module: contentinspectioncallout
short_description: Configuration for Content Inspection callout resource.
description: Configuration for Content Inspection callout resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about this Content Inspection callout.
  name:
    type: str
    description:
      - Name for the Content Inspection callout. Not case sensitive. Must begin with
        an ASCII letter or underscore (_) character, and must consist only of ASCII
        alphanumeric or underscore characters. Must not begin with 're' or 'xp' or
        be a word reserved for use as an expression qualifier prefix (such as HTTP)
        or enumeration value (such as ASCII). Must not be the name of an existing
        named expression, pattern set, dataset, stringmap, or callout.
  profilename:
    type: str
    description:
      - Name of the Content Inspection profile. The type of the configured profile
        must match the type specified using -type argument.
  resultexpr:
    type: str
    description:
      - 'Expression that extracts the callout results from the response sent by the
        CI callout agent. Must be a response based expression, that is, it must begin
        with ICAP.RES. The operations in this expression must match the return type.
        For example, if you configure a return type of TEXT, the result expression
        must be a text based expression, as in the following example: icap.res.header("ISTag")'
  returntype:
    type: str
    choices:
      - BOOL
      - NUM
      - TEXT
    description:
      - Type of data that the target callout agent returns in response to the callout.
      - 'Available settings function as follows:'
      - '* C(TEXT) - Treat the returned value as a text string.'
      - '* C(NUM) - Treat the returned value as a number.'
      - '* C(BOOL) - Treat the returned value as a Boolean value.'
      - 'Note: You cannot change the return type after it is set.'
  serverip:
    type: str
    description:
      - IP address of Content Inspection server. Mutually exclusive with the server
        name parameter.
  servername:
    type: str
    description:
      - Name of the load balancing or content switching virtual server or service
        to which the Content Inspection request is issued. Mutually exclusive with
        server IP address and port parameters. The service type must be TCP or SSL_TCP.
        If there are vservers and services with the same name, then vserver is selected.
  serverport:
    type: float
    description:
      - Port of the Content Inspection server.
  type:
    type: str
    choices:
      - ICAP
    description:
      - 'Type of the Content Inspection callout. It must be one of the following:'
      - '* C(ICAP) - Sends C(ICAP) request to the configured C(ICAP) server.'
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
