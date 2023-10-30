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
module: vpnclientlessaccessprofile
short_description: Configuration for Clientless VPN rewrite profile resource.
description: Configuration for Clientless VPN rewrite profile resource.
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
  clientconsumedcookies:
    type: str
    description:
      - Specify the name of the pattern set containing the names of the cookies, which
        are allowed between the client and the server. If a pattern set is not specified,
        Citrix Gateway does not allow any cookies between the client and the server.
        A cookie that is not specified in the pattern set is handled by Citrix Gateway
        on behalf of the client.
  javascriptrewritepolicylabel:
    type: str
    description:
      - Name of the configured JavaScript rewrite policy label.  If you do not specify
        a policy label name, then JAVA scripts are not rewritten.
  profilename:
    type: str
    description:
      - Name for the Citrix Gateway clientless access profile. Must begin with an
        ASCII alphabetic or underscore (_) character, and must consist only of ASCII
        alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),
        equals (=), and hyphen (-) characters. Cannot be changed after the profile
        is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
  regexforfindingcustomurls:
    type: str
    description:
      - Name of the pattern set that contains the regular expressions, which match
        the URLs in the custom content type other than HTML, CSS, XML, XCOMP, and
        JavaScript. The custom content type should be included in the patset ns_cvpn_custom_content_types.
  regexforfindingurlincss:
    type: str
    description:
      - Name of the pattern set that contains the regular expressions, which match
        the URL in the CSS.
  regexforfindingurlinjavascript:
    type: str
    description:
      - Name of the pattern set that contains the regular expressions, which match
        the URL in Java script.
  regexforfindingurlinxcomponent:
    type: str
    description:
      - Name of the pattern set that contains the regular expressions, which match
        the URL in X Component.
  regexforfindingurlinxml:
    type: str
    description:
      - Name of the pattern set that contains the regular expressions, which match
        the URL in XML.
  reqhdrrewritepolicylabel:
    type: str
    description:
      - Name of the configured Request rewrite policy label.  If you do not specify
        a policy label name, then requests are not rewritten.
  requirepersistentcookie:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Specify whether a persistent session cookie is set and accepted for clientless
        access. If this parameter is set to C(ON), COM objects, such as MSOffice,
        which are invoked by the browser can access the files using clientless access.
        Use caution because the persistent cookie is stored on the disk.
    default: 'OFF'
  reshdrrewritepolicylabel:
    type: str
    description:
      - Name of the configured Response rewrite policy label.
  urlrewritepolicylabel:
    type: str
    description:
      - Name of the configured URL rewrite policy label. If you do not specify a policy
        label name, then URLs are not rewritten.
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
