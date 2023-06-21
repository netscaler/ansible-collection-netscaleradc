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
module: aaaparameter
short_description: Configuration for AAA parameter resource.
description: Configuration for AAA parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aaadloglevel:
    description:
      - 'AAAD log level, which specifies the types of AAAD events to log in nsvpn.log. '
      - 'Available values function as follows: '
      - '* EMERGENCY - Events that indicate an immediate crisis on the server.'
      - '* ALERT - Events that might require action.'
      - '* CRITICAL - Events that indicate an imminent server crisis.'
      - '* ERROR - Events that indicate some type of error.'
      - '* WARNING - Events that require action in the near future.'
      - '* NOTICE - Events that the administrator should know about.'
      - '* INFORMATIONAL - All but low-level events.'
      - '* DEBUG - All events, in extreme detail.'
    type: str
    default: INFORMATIONAL
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
  aaadnatip:
    description:
      - Source IP address to use for traffic that is sent to the authentication server.
    type: str
  aaasessionloglevel:
    description:
      - 'Audit log level, which specifies the types of events to log for cli executed
        commands. '
      - 'Available values function as follows: '
      - '* EMERGENCY - Events that indicate an immediate crisis on the server.'
      - '* ALERT - Events that might require action.'
      - '* CRITICAL - Events that indicate an imminent server crisis.'
      - '* ERROR - Events that indicate some type of error.'
      - '* WARNING - Events that require action in the near future.'
      - '* NOTICE - Events that the administrator should know about.'
      - '* INFORMATIONAL - All but low-level events.'
      - '* DEBUG - All events, in extreme detail.'
    type: str
    default: DEFAULT_LOGLEVEL_AAA
    choices:
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
  apitokencache:
    description:
      - Option to enable/disable API cache feature.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  defaultauthtype:
    description:
      - The default authentication server type.
    type: str
    default: LOCAL
    choices:
      - LOCAL
      - LDAP
      - RADIUS
      - TACACS
      - CERT
  defaultcspheader:
    description:
      - Parameter to enable/disable default CSP header
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dynaddr:
    description:
      - Set by the DHCP client when the IP address was fetched dynamically.
    type: str
    choices:
      - true
      - false
  enableenhancedauthfeedback:
    description:
      - Enhanced auth feedback provides more information to the end user about the
        reason for an authentication failure.  The default value is set to NO.
    type: str
    choices:
      - true
      - false
  enablesessionstickiness:
    description:
      - Enables/Disables stickiness to authentication servers
    type: str
    choices:
      - true
      - false
  enablestaticpagecaching:
    description:
      - The default state of VPN Static Page caching. Static Page caching is enabled
        by default.
    type: str
    default: true
    choices:
      - true
      - false
  failedlogintimeout:
    description:
      - Number of minutes an account will be locked if user exceeds maximum permissible
        attempts
    type: int
  ftmode:
    description:
      - First time user mode determines which configuration options are shown by default
        when logging in to the GUI. This setting is controlled by the GUI.
    type: str
    default: true
    choices:
      - true
      - HA
      - false
  loginencryption:
    description:
      - Parameter to encrypt login information for nFactor flow
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  maxaaausers:
    description:
      - Maximum number of concurrent users allowed to log on to VPN simultaneously.
    type: int
  maxkbquestions:
    description:
      - This will set maximum number of Questions to be asked for KB Validation. Default
        value is 2, Max Value is 6
    type: int
  maxloginattempts:
    description:
      - Maximum Number of login Attempts
    type: int
  maxsamldeflatesize:
    description:
      - This will set the maximum deflate size in case of SAML Redirect binding.
    type: int
  persistentloginattempts:
    description:
      - Persistent storage of unsuccessful user login attempts
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  pwdexpirynotificationdays:
    description:
      - This will set the threshold time in days for password expiry notification.
        Default value is 0, which means no notification is sent
    type: int
  samesite:
    description:
      - SameSite attribute value for Cookies generated in AAATM context. This attribute
        value will be appended only for the cookies which are specified in the builtin
        patset ns_cookies_samesite
    type: str
    choices:
      - None
      - LAX
      - STRICT
  tokenintrospectioninterval:
    description:
      - Frequency at which a token must be verified at the Authorization Server (AS)
        despite being found in cache.
    type: int
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
