#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: botprofile
short_description: Configuration for Bot profile resource.
description: Configuration for Bot profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bot_enable_black_list:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable black-list bot detection.
    type: str
    default: 'OFF'
  bot_enable_ip_reputation:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable IP-reputation bot detection.
    type: str
    default: 'OFF'
  bot_enable_rate_limit:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable rate-limit bot detection.
    type: str
    default: 'OFF'
  bot_enable_tps:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable TPS.
    type: str
    default: 'OFF'
  bot_enable_white_list:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable white-list bot detection.
    type: str
    default: 'OFF'
  clientipexpression:
    description:
      - Expression to get the client IP.
    type: str
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  devicefingerprint:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable device-fingerprint bot detection
    type: str
    default: 'OFF'
  devicefingerprintaction:
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - MITIGATION
    description:
      - Action to be taken for device-fingerprint based bot detection.
    type: list
    elements: str
    default: NONE
  devicefingerprintmobile:
    choices:
      - NONE
      - Android
      - iOS
    description:
      - Enabling bot device fingerprint protection for mobile clients
    type: list
    elements: str
    default: NONE
  errorurl:
    description:
      - URL that Bot protection uses as the Error URL.
    type: str
  headlessbrowserdetection:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable Headless Browser detection.
    type: str
    default: 'OFF'
  kmdetection:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable keyboard-mouse based bot detection.
    type: str
    default: 'OFF'
  kmeventspostbodylimit:
    description:
      - Size of the KM data send by the browser, needs to be processed on ADC
    type: float
  kmjavascriptname:
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
    type: str
  name:
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
    type: str
  signature:
    description:
      - Name of object containing bot static signature details.
    type: str
  signaturemultipleuseragentheaderaction:
    choices:
      - CHECKLAST
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken if multiple User-Agent headers are seen in a request (Applicable
        if Signature check is enabled). Log action should be combined with other actions
    type: list
    elements: str
    default: CHECKLAST
  signaturenouseragentheaderaction:
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken if no User-Agent header in the request (Applicable if
        Signature check is enabled).
    type: list
    elements: str
    default: DROP
  spoofedreqaction:
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Actions to be taken on a spoofed request (A request spoofing good bot user
        agent string).
    type: list
    elements: str
    default: LOG
  trap:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable trap bot detection.
    type: str
    default: 'OFF'
  trapaction:
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
    description:
      - Action to be taken for bot trap based bot detection.
    type: list
    elements: str
    default: NONE
  trapurl:
    description:
      - URL that Bot protection uses as the Trap URL.
    type: str
  verboseloglevel:
    choices:
      - NONE
      - HTTP_FULL_HEADER
    description:
      - Bot verbose Logging. Based on the log level, ADC will log additional information
        whenever client is detected as a bot.
    type: str
    default: NONE
  botprofile_blacklist_binding:
    type: dict
    description: Bindings for botprofile_blacklist_binding resource
    suboptions:
      mode:
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
