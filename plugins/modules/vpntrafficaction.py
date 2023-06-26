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
module: vpntrafficaction
short_description: Configuration for VPN traffic action resource.
description: Configuration for VPN traffic action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  apptimeout:
    description:
      - Maximum amount of time, in minutes, a user can stay logged on to the web application.
    type: int
  formssoaction:
    description:
      - Name of the form-based single sign-on profile. Form-based single sign-on allows
        users to log on one time to all protected applications in your network, instead
        of requiring them to log on separately to access each one.
    type: str
  fta:
    description:
      - Specify file type association, which is a list of file extensions that users
        are allowed to open.
    type: str
    choices:
      - true
      - false
  hdx:
    description:
      - Provide hdx proxy to the ICA traffic
    type: str
    choices:
      - true
      - false
  kcdaccount:
    description:
      - Kerberos constrained delegation account name
    type: str
    default: '"Default"'
  name:
    description:
      - Name for the traffic action. Must begin with an ASCII alphabetic or underscore
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
  proxy:
    description:
      - IP address and Port of the proxy server to be used for HTTP access for this
        request.
    type: str
  qual:
    description:
      - Protocol, either HTTP or TCP, to be used with the action.
    type: str
    choices:
      - http
      - tcp
  samlssoprofile:
    description:
      - Profile to be used for doing SAML SSO to remote relying party
    type: str
  sso:
    description:
      - Provide single sign-on to the web application.
      - "\t    NOTE : Authentication mechanisms like Basic-authentication  require\
        \ the user credentials to be sent in plaintext which is not secure if the\
        \ server is running on HTTP (instead of HTTPS)."
    type: str
    choices:
      - true
      - false
  userexpression:
    description:
      - expression that will be evaluated to obtain username for SingleSignOn
    type: str
  wanscaler:
    description:
      - Use the Repeater Plug-in to optimize network traffic.
    type: str
    choices:
      - true
      - false
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