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
---
module: systemparameter
short_description: Configuration for system parameter resource.
description: Configuration for system parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  basicauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable basic authentication for Nitro API.
  cliloglevel:
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
  daystoexpire:
    type: int
    description:
      - Password expiry days for all the system users. The daystoexpire value ranges
        from 30 to 255.
  doppler:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Doppler
  fipsusermode:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use this option to set the FIPS mode for key user-land processes. When enabled,
        these user-land processes will operate in FIPS mode. In this mode, these processes
        will use FIPS 140-2 certified crypto algorithms.
      - With a FIPS license, it is enabled by default and cannot be disabled.
      - Without a FIPS license, it is disabled by default, wherein these user-land
        processes will not operate in FIPS mode.
  forcepasswordchange:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable force password change for nsroot user
  googleanalytics:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Google analytics
  localauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When enabled, local users can access Citrix ADC even when external authentication
        is configured. When disabled, local users are not allowed to access the Citrix
        ADC, Local users can access the Citrix ADC only when the configured external
        authentication servers are unavailable. This parameter is not applicable to
        SSH Key-based authentication
  maxsessionperuser:
    type: int
    description:
      - Maximum number of client connection allowed per user.The maxsessionperuser
        value ranges from 1 to 40
  minpasswordlen:
    type: int
    description:
      - Minimum length of system user password. When strong password is enabled default
        minimum length is 8. User entered value can be greater than or equal to 8.
        Default mininum value is 1 when strong password is disabled. Maximum value
        is 127 in both cases.
  natpcbforceflushlimit:
    type: int
    description:
      - Flush the system if the number of Network Address Translation Protocol Control
        Blocks (NATPCBs) exceeds this value.
  natpcbrstontimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send a reset signal to client and server connections when their NATPCBs time
        out. Avoids the buildup of idle TCP connections on both the sides.
  passwordhistorycontrol:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enables or disable password expiry feature for system users.
      - If the feature is C(ENABLED), by default the last 6 passwords of users will
        be maintained and will not be allowed to reuse same.
      - When the feature is enabled the daystoexpire, warnpriorndays and pwdhistoryCount
        will be set with default values. The values can only be set in system
      - for system parameter. It cannot be unset. It is possible to set and unset
        the values for daytoexpire and warnpriorndays in system groups.
      - 'Default values if feature is C(ENABLED):'
      - 'daystoexpire: 30'
      - 'warnpriorndays: 5'
      - 'pwdhistoryCount: 6'
      - If the feature is C(DISABLED) the values cannot be set or unset in system
        parameter and system groups
  promptstring:
    type: str
    description:
      - 'String to display at the command-line prompt. Can consist of letters, numbers,
        hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:),
        underscore (_), and the following variables:'
      - '* %u - Will be replaced by the user name.'
      - '* %h - Will be replaced by the hostname of the Citrix ADC.'
      - '* %t - Will be replaced by the current time in 12-hour format.'
      - '* %T - Will be replaced by the current time in 24-hour format.'
      - '* %d - Will be replaced by the current date.'
      - '* %s - Will be replaced by the state of the Citrix ADC.'
      - ''
      - 'Note: The 63-character limit for the length of the string does not apply
        to the characters that replace the variables.'
  pwdhistorycount:
    type: int
    description:
      - Number of passwords to be maintained as history for system users. The pwdhistorycount
        value ranges from 1 to 10.
  rbaonresponse:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable Role-Based Authentication (RBA) on responses.
  reauthonauthparamchange:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable External user reauthentication when authentication parameter
        changes
  removesensitivefiles:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use this option to remove the sensitive files from the system like authorise
        keys, public keys etc. The commands which will remove sensitive files when
        this system paramter is enabled are rm cluster instance, rm cluster node,
        rm ha node, clear config full, join cluster and add cluster instance.
  restrictedtimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot
        be configured beyond admin configured timeout  and also it will have the [minimum
        - maximum] range check. When disabled, timeout will have the old behaviour.
        By default the value is disabled
  strongpassword:
    type: str
    choices:
      - enableall
      - enablelocal
      - disabled
    description:
      - 'After enabling strong password (C(enableall) / C(enablelocal) - not included
        in exclude list), all the passwords / sensitive information must have - Atleast
        1 Lower case character, Atleast 1 Upper case character, Atleast 1 numeric
        character, Atleast 1 special character ( ~, `, !, @, #, $, %, ^, &, *, -,
        _, =, +, {, }, [, ], |, \, :, <, >, /, ., ,, " "). Exclude list in case of
        C(enablelocal) is - NS_FIPS, NS_CRL, NS_RSAKEY, NS_PKCS12, NS_PKCS8, NS_LDAP,
        NS_TACACS, NS_TACACSACTION, NS_RADIUS, NS_RADIUSACTION, NS_ENCRYPTION_PARAMS.
        So no Strong Password checks will be performed on these ObjectType commands
        for C(enablelocal) case.'
  timeout:
    type: int
    description:
      - CLI session inactivity timeout, in seconds. If Restrictedtimeout argument
        is enabled, Timeout can have values in the range [300-86400] seconds.
      - If Restrictedtimeout argument is disabled, Timeout can have values in the
        range [0, 10-100000000] seconds. Default value is 900 seconds.
  totalauthtimeout:
    type: int
    description:
      - Total time a request can take for authentication/authorization
  wafprotection:
    type: list
    choices:
      - DEFAULT
      - DISABLED
      - GUI
    description:
      - 'Configure WAF protection for endpoints used by NetScaler management interfaces.
        The available options are:'
      - '* C(DEFAULT) - NetScaler decides which endpoints have WAF protection enabled.'
      - '* C(GUI) - Endpoints used by the Management C(GUI) Interface are WAF protected.'
      - '* C(DISABLED) - WAF protection is disabled.'
    elements: str
  warnpriorndays:
    type: int
    description:
      - Number of days before which password expiration warning would be thrown with
        respect to daystoexpire. The warnpriorndays value ranges from 5 to 40.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample systemparameter playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure systemparameter
      delegate_to: localhost
      netscaler.adc.systemparameter:
        state: present
        maxclient: '40'
        forcepasswordchange: ENABLED
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
