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
module: tmtrafficaction
short_description: Configuration for TM traffic action resource.
description: Configuration for TM traffic action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  apptimeout:
    description:
      - Time interval, in minutes, of user inactivity after which the connection is
        closed.
    type: int
  forcedtimeout:
    description:
      - Setting to start, stop or reset TM session force timer
    type: str
    choices:
      - START
      - STOP
      - RESET
  forcedtimeoutval:
    description:
      - Time interval, in minutes, for which force timer should be set.
    type: int
  formssoaction:
    description:
      - Name of the configured form-based single sign-on profile.
    type: str
  initiatelogout:
    description:
      - Initiate logout for the traffic management (TM) session if the policy evaluates
        to true. The session is then terminated after two minutes.
    type: str
    choices:
      - true
      - false
  kcdaccount:
    description:
      - Kerberos constrained delegation account name
    type: str
    default: '"None"'
  name:
    description:
      - Name for the traffic action. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after a traffic action is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
    type: str
  passwdexpression:
    description:
      - expression that will be evaluated to obtain password for SingleSignOn
    type: str
  persistentcookie:
    description:
      - Use persistent cookies for the traffic session. A persistent cookie remains
        on the user device and is sent with each HTTP request. The cookie becomes
        stale if the session ends.
    type: str
    choices:
      - true
      - false
  samlssoprofile:
    description:
      - Profile to be used for doing SAML SSO to remote relying party
    type: str
  sso:
    description:
      - Use single sign-on for the resource that the user is accessing now.
    type: str
    choices:
      - true
      - false
  userexpression:
    description:
      - expression that will be evaluated to obtain username for SingleSignOn
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
