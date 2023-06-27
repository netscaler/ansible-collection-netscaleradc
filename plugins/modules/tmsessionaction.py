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
module: tmsessionaction
short_description: Configuration for TM session action resource.
description: Configuration for TM session action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  defaultauthorizationaction:
    choices:
      - ALLOW
      - DENY
    description:
      - Allow or deny access to content for which there is no specific authorization
        policy.
    type: str
  homepage:
    description:
      - Web address of the home page that a user is displayed when authentication
        vserver is bookmarked and used to login.
    type: str
  httponlycookie:
    choices:
      - true
      - false
    description:
      - Allow only an HTTP session cookie, in which case the cookie cannot be accessed
        by scripts.
    type: str
    default: true
  kcdaccount:
    description:
      - Kerberos constrained delegation account name
    type: str
  name:
    description:
      - Name for the session action. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after a session action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
    type: str
  persistentcookie:
    choices:
      - true
      - false
    description:
      - 'Enable or disable persistent SSO cookies for the traffic management (TM)
        session. A persistent cookie remains on the user device and is sent with each
        HTTP request. The cookie becomes stale if the session ends. This setting is
        overwritten if a traffic action sets persistent cookie to OFF. '
      - 'Note: If persistent cookie is enabled, make sure you set the persistent cookie
        validity.'
    type: str
  persistentcookievalidity:
    description:
      - Integer specifying the number of minutes for which the persistent cookie remains
        valid. Can be set only if the persistent cookie setting is enabled.
    type: int
  sesstimeout:
    description:
      - Session timeout, in minutes. If there is no traffic during the timeout period,
        the user is disconnected and must reauthenticate to access intranet resources.
    type: int
  sso:
    choices:
      - true
      - false
    description:
      - Use single sign-on (SSO) to log users on to all web applications automatically
        after they authenticate, or pass users to the web application logon page to
        authenticate to each application individually. Note that this configuration
        does not honor the following authentication types for security reason. BASIC,
        DIGEST, and NTLM (without Negotiate NTLM2 Key or Negotiate Sign Flag). Use
        TM TrafficAction to configure SSO for these authentication types.
    type: str
  ssocredential:
    choices:
      - PRIMARY
      - SECONDARY
    description:
      - Use the primary or secondary authentication credentials for single sign-on
        (SSO).
    type: str
  ssodomain:
    description:
      - Domain to use for single sign-on (SSO).
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
