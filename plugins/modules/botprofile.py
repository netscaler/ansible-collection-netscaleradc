#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: botprofile
short_description: Configuration for Bot profile resource.
description: Configuration for Bot profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
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
  addcookieflags:
    type: str
    choices:
      - none
      - httpOnly
      - secure
      - all
    description:
      - 'Add the specified flags to bot session cookies. Available settings function
        as follows:'
      - '* None - Do not add flags to cookies.'
      - '* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from
        accessing cookies.'
      - '* Secure - Add Secure flag to cookies.'
      - '* All - Add both HTTPOnly and Secure flags to cookies.'
  bot_enable_black_list:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable black-list bot detection.
  bot_enable_ip_reputation:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable IP-reputation bot detection.
  bot_enable_rate_limit:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable rate-limit bot detection.
  bot_enable_tps:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable TPS.
  bot_enable_white_list:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable white-list bot detection.
  clientipexpression:
    type: str
    description:
      - Expression to get the client IP.
  comment:
    type: str
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
  devicefingerprint:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable device-fingerprint bot detection
  devicefingerprintaction:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - MITIGATION
    description:
      - Action to be taken for device-fingerprint based bot detection.
    elements: str
  devicefingerprintmobile:
    type: list
    choices:
      - NONE
      - Android
      - iOS
    description:
      - Enabling bot device fingerprint protection for mobile clients
    elements: str
  dfprequestlimit:
    type: float
    description:
      - Number of requests to allow without bot session cookie if device fingerprint
        is enabled
  errorurl:
    type: str
    description:
      - URL that Bot protection uses as the Error URL.
  headlessbrowserdetection:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable Headless Browser detection.
  kmdetection:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable keyboard-mouse based bot detection.
  kmeventspostbodylimit:
    type: float
    description:
      - Size of the KM data send by the browser, needs to be processed on ADC
  kmjavascriptname:
    type: str
    description:
      - Name of the JavaScript file that the Bot Management feature will insert in
        the response for keyboard-mouse based detection.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my javascript file name" or 'my javascript
        file name').
  name:
    type: str
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
  sessioncookiename:
    type: str
    description:
      - Name of the SessionCookie that the Bot Management feature uses for tracking.
      - Must begin with a letter or number, and can consist of from 1 to 31 letters,
        numbers, and the hyphen (-) and underscore (_) symbols.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my cookie name" or 'my cookie name').
  sessiontimeout:
    type: float
    description:
      - Timeout, in seconds, after which a user session is terminated.
  signature:
    type: str
    description:
      - Name of object containing bot static signature details.
  signaturemultipleuseragentheaderaction:
    type: list
    choices:
      - CHECKLAST
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken if multiple User-Agent headers are seen in a request (Applicable
        if Signature check is enabled). Log action should be combined with other actions
    elements: str
  signaturenouseragentheaderaction:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken if no User-Agent header in the request (Applicable if
        Signature check is enabled).
    elements: str
  spoofedreqaction:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken on a spoofed request (A request spoofing good bot user
        agent string).
    elements: str
  trap:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable trap bot detection.
  trapaction:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Action to be taken for bot trap based bot detection.
    elements: str
  trapurl:
    type: str
    description:
      - URL that Bot protection uses as the Trap URL.
  verboseloglevel:
    type: str
    choices:
      - NONE
      - HTTP_FULL_HEADER
    description:
      - Bot verbose Logging. Based on the log level, ADC will log additional information
        whenever client is detected as a bot.
  botprofile_blacklist_binding:
    type: dict
    description: Bindings for botprofile_blacklist_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_captcha_binding:
    type: dict
    description: Bindings for botprofile_captcha_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_ipreputation_binding:
    type: dict
    description: Bindings for botprofile_ipreputation_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_kmdetectionexpr_binding:
    type: dict
    description: Bindings for botprofile_kmdetectionexpr_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_logexpression_binding:
    type: dict
    description: Bindings for botprofile_logexpression_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_ratelimit_binding:
    type: dict
    description: Bindings for botprofile_ratelimit_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_tps_binding:
    type: dict
    description: Bindings for botprofile_tps_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_trapinsertionurl_binding:
    type: dict
    description: Bindings for botprofile_trapinsertionurl_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  botprofile_whitelist_binding:
    type: dict
    description: Bindings for botprofile_whitelist_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
