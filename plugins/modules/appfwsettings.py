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
module: appfwsettings
short_description: Configuration for AS settings resource.
description: Configuration for AS settings resource.
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
  ceflogging:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable CEF format logs.
  centralizedlearning:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Flag used to enable/disable ADM centralized learning
  clientiploggingheader:
    type: str
    description:
      - Name of an HTTP header that contains the IP address that the client used to
        connect to the protected web site or service.
  cookiepostencryptprefix:
    type: str
    description:
      - String that is prepended to all encrypted cookie values.
  defaultprofile:
    type: str
    description:
      - Profile to use when a connection does not match any policy. Default setting
        is APPFW_BYPASS, which sends unmatched connections back to the Citrix ADC
        without attempting to filter them further.
  entitydecoding:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Transform multibyte (double- or half-width) characters to single width characters.
  geolocationlogging:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable Geo-Location Logging in CEF format logs.
  importsizelimit:
    type: float
    description:
      - Cumulative total maximum number of bytes in web forms imported to a protected
        web site. If a user attempts to upload files with a total byte count higher
        than the specified limit, the application firewall blocks the request.
  learnratelimit:
    type: float
    description:
      - Maximum number of connections per second that the application firewall learning
        engine examines to generate new relaxations for learning-enabled security
        checks. The application firewall drops any connections above this limit from
        the list of connections used by the learning engine.
  logmalformedreq:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Log requests that are so malformed that application firewall parsing doesn't
        occur.
  malformedreqaction:
    type: list
    choices:
      - none
      - block
      - log
      - stats
    description:
      - flag to define action on malformed requests that application firewall cannot
        parse
    elements: str
  proxypassword:
    type: str
    description:
      - Password with which proxy user logs on.
  proxyport:
    type: int
    description:
      - Proxy Server Port to get updated signatures from AWS.
  proxyserver:
    type: str
    description:
      - Proxy Server IP to get updated signatures from AWS.
  proxyusername:
    type: str
    description:
      - Proxy Username
  sessioncookiename:
    type: str
    description:
      - Name of the session cookie that the application firewall uses to track user
        sessions.
      - Must begin with a letter or number, and can consist of from 1 to 31 letters,
        numbers, and the hyphen (-) and underscore (_) symbols.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cookie name" or 'my cookie name').
  sessionlifetime:
    type: float
    description:
      - Maximum amount of time (in seconds) that the application firewall allows a
        user session to remain active, regardless of user activity. After this time,
        the user session is terminated. Before continuing to use the protected web
        site, the user must establish a new session by opening a designated start
        URL.
  sessionlimit:
    type: float
    description:
      - Maximum number of sessions that the application firewall allows to be active,
        regardless of user activity. After the max_limit reaches, No more user session
        will be created .
  sessiontimeout:
    type: float
    description:
      - Timeout, in seconds, after which a user session is terminated. Before continuing
        to use the protected web site, the user must establish a new session by opening
        a designated start URL.
  signatureautoupdate:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Flag used to enable/disable auto update signatures
  signatureurl:
    type: str
    description:
      - URL to download the mapping file from server
  undefaction:
    type: str
    description:
      - Profile to use when an application firewall policy evaluates to undefined
        (UNDEF).
      - An UNDEF event indicates an internal error condition. The APPFW_BLOCK built-in
        profile is the default setting. You can specify a different built-in or user-created
        profile as the UNDEF profile.
  useconfigurablesecretkey:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use configurable secret key in AppFw operations
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
