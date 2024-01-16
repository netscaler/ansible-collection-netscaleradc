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
module: nsicapprofile
short_description: Configuration for ICAP profile resource.
description: Configuration for ICAP profile resource.
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
  allow204:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Enable or Disable sending Allow: 204 header in ICAP request.'
  connectionkeepalive:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, Citrix ADC keeps the ICAP connection alive after a transaction
        to reuse it to send next ICAP request.
  hostheader:
    type: str
    description:
      - ICAP Host Header
  inserthttprequest:
    type: str
    description:
      - Exact HTTP request, in the form of an expression, which the Citrix ADC encapsulates
        and sends to the ICAP server. If you set this parameter, the ICAP request
        is sent using only this header. This can be used when the HTTP header is not
        available to send or ICAP server only needs part of the incoming HTTP request.
        The request expression is constrained by the feature for which it is used.
      - The Citrix ADC does not check the validity of this request. You must manually
        validate the request.
  inserticapheaders:
    type: str
    description:
      - 'Insert custom ICAP headers in the ICAP request to send to ICAP server. The
        headers can be static or can be dynamically constructed using PI Policy Expression.
        For example, to send static user agent and Client''s IP address, the expression
        can be specified as "User-Agent: NS-ICAP-Client/V1.0\r\nX-Client-IP: "+CLIENT.IP.SRC+"\r\n".'
      - The Citrix ADC does not check the validity of the specified header name-value.
        You must manually validate the specified header syntax.
  logaction:
    type: str
    description:
      - Name of the audit message action which would be evaluated on receiving the
        ICAP response to emit the logs.
  mode:
    type: str
    choices:
      - REQMOD
      - RESPMOD
    description:
      - ICAP Mode of operation. It is a mandatory argument while creating an icapprofile.
  name:
    type: str
    description:
      - Name for an ICAP profile. Must begin with a letter, number, or the underscore
        \(_\) character. Other characters allowed, after the first character, are
        the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon
        \(:\), and equal \(=\) characters. The name of a ICAP profile cannot be changed
        after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my icap profile" or ''my icap profile''\).'
  preview:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or Disable preview header with ICAP request. This feature allows an
        ICAP server to see the beginning of a transaction, then decide if it wants
        to opt-out of the transaction early instead of receiving the remainder of
        the request message.
  previewlength:
    type: float
    description:
      - Value of Preview Header field. Citrix ADC uses the minimum of this set value
        and the preview size received on OPTIONS response.
  queryparams:
    type: str
    description:
      - 'Query parameters to be included with ICAP request URI. Entered values should
        be in arg=value format. For more than one parameters, add & separated values.
        e.g.: arg1=val1&arg2=val2.'
  reqtimeout:
    type: float
    description:
      - Time, in seconds, within which the remote server should respond to the ICAP-request.
        If the Netscaler does not receive full response with this time, the specified
        request timeout action is performed. Zero value disables this timeout functionality.
  reqtimeoutaction:
    type: str
    choices:
      - BYPASS
      - DROP
      - RESET
    description:
      - Name of the action to perform if the Vserver/Server representing the remote
        service does not respond with any response within the timeout value configured.
        The Supported actions are
      - '* C(BYPASS) - This Ignores the remote server response and sends the request/response
        to Client/Server.'
      - '           * If the ICAP response with Encapsulated headers is not received
        within the request-timeout value configured, this Ignores the remote ICAP
        server response and sends the Full request/response to Server/Client.'
      - '* C(RESET) - Reset the client connection by closing it. The client program,
        such as a browser, will handle this and may inform the user. The client may
        then resend the request if desired.'
      - '* C(DROP) - Drop the request without sending a response to the user.'
  uri:
    type: str
    description:
      - URI representing icap service. It is a mandatory argument while creating an
        icapprofile.
  useragent:
    type: str
    description:
      - ICAP User Agent Header String
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
