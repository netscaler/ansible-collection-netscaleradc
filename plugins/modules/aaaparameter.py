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
module: aaaparameter
short_description: Configuration for AAA parameter resource.
description: Configuration for AAA parameter resource.
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
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  aaadloglevel:
    type: str
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
    description:
      - AAAD log level, which specifies the types of AAAD events to log in nsvpn.log.
      - 'Available values function as follows:'
      - '* C(EMERGENCY) - Events that indicate an immediate crisis on the server.'
      - '* C(ALERT) - Events that might require action.'
      - '* C(CRITICAL) - Events that indicate an imminent server crisis.'
      - '* C(ERROR) - Events that indicate some type of error.'
      - '* C(WARNING) - Events that require action in the near future.'
      - '* C(NOTICE) - Events that the administrator should know about.'
      - '* C(INFORMATIONAL) - All but low-level events.'
      - '* C(DEBUG) - All events, in extreme detail.'
  aaadnatip:
    type: str
    description:
      - Source IP address to use for traffic that is sent to the authentication server.
  aaasessionloglevel:
    type: str
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
    description:
      - Audit log level, which specifies the types of events to log for cli executed
        commands.
      - 'Available values function as follows:'
      - '* C(EMERGENCY) - Events that indicate an immediate crisis on the server.'
      - '* C(ALERT) - Events that might require action.'
      - '* C(CRITICAL) - Events that indicate an imminent server crisis.'
      - '* C(ERROR) - Events that indicate some type of error.'
      - '* C(WARNING) - Events that require action in the near future.'
      - '* C(NOTICE) - Events that the administrator should know about.'
      - '* C(INFORMATIONAL) - All but low-level events.'
      - '* C(DEBUG) - All events, in extreme detail.'
  apitokencache:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Option to enable/disable API cache feature.
  defaultauthtype:
    type: str
    choices:
      - LOCAL
      - LDAP
      - RADIUS
      - TACACS
      - CERT
    description:
      - The default authentication server type.
  defaultcspheader:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to enable/disable default CSP header
  dynaddr:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Set by the DHCP client when the IP address was fetched dynamically.
  enableenhancedauthfeedback:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enhanced auth feedback provides more information to the end user about the
        reason for an authentication failure.  The default value is set to C(NO).
  enablesessionstickiness:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enables/Disables stickiness to authentication servers
  enablestaticpagecaching:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - The default state of VPN Static Page caching. Static Page caching is enabled
        by default.
  failedlogintimeout:
    type: float
    description:
      - Number of minutes an account will be locked if user exceeds maximum permissible
        attempts
  ftmode:
    type: str
    choices:
      - 'ON'
      - HA
      - 'OFF'
    description:
      - First time user mode determines which configuration options are shown by default
        when logging in to the GUI. This setting is controlled by the GUI.
  httponlycookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to set/reset HttpOnly Flag for NSC_AAAC/NSC_TMAS cookies in nfactor
  loginencryption:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter to encrypt login information for nFactor flow
  maxaaausers:
    type: float
    description:
      - Maximum number of concurrent users allowed to log on to VPN simultaneously.
  maxkbquestions:
    type: float
    description:
      - This will set maximum number of Questions to be asked for KB Validation. Default
        value is 2, Max Value is 6
  maxloginattempts:
    type: float
    description:
      - Maximum Number of login Attempts
  maxsamldeflatesize:
    type: float
    description:
      - This will set the maximum deflate size in case of SAML Redirect binding.
  persistentloginattempts:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Persistent storage of unsuccessful user login attempts
  pwdexpirynotificationdays:
    type: float
    description:
      - This will set the threshold time in days for password expiry notification.
        Default value is 0, which means no notification is sent
  samesite:
    type: str
    choices:
      - None
      - LAX
      - STRICT
    description:
      - SameSite attribute value for Cookies generated in AAATM context. This attribute
        value will be appended only for the cookies which are specified in the builtin
        patset ns_cookies_samesite
  tokenintrospectioninterval:
    type: float
    description:
      - Frequency at which a token must be verified at the Authorization Server (AS)
        despite being found in cache.
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
