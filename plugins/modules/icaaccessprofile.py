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
module: icaaccessprofile
short_description: Configuration for ica accessprofile resource.
description: Configuration for ica accessprofile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  clientaudioredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable applications hosted on the server to play sounds
        through a sound device installed on the client computer, also allows or prevents
        users to record audio input
  clientclipboardredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable the clipboard on the client device to be mapped
        to the clipboard on the server
  clientcomportredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable COM port redirection to and from the client
  clientdriveredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disables drive redirection to and from the client
  clientprinterredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable client printers to be mapped to a server when
        a user logs on to a session
  clientusbdriveredirection:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable the redirection of USB devices to and from the
        client
  connectclientlptports:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable automatic connection of LPT ports from the client
        when the user logs on
  localremotedatasharing:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable file/data sharing via the Receiver for HTML5
  multistream:
    type: raw
    choices:
      - DEFAULT
      - DISABLED
    description:
      - Allow Default access/Disable the multistream feature for the specified users
  name:
    type: raw
    description:
      - Name for the ICA accessprofile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and
      - the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters. Cannot be changed after the ICA accessprofile
        is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my ica accessprofile" or 'my ica accessprofile').
      - ''
      - Each of the features can be configured as DEFAULT/DISABLED.
      - Here, DISABLED means that the policy settings on the backend XenApp/XenDesktop
        server are overridden and the Citrix ADC makes the decision to deny access.
        Whereas DEFAULT means that the Citrix ADC allows the request to reach the
        XenApp/XenDesktop that takes the decision to allow/deny access based on the
        policy configured on it. For example, if ClientAudioRedirection is enabled
        on the backend XenApp/XenDesktop server, and the configured profile has ClientAudioRedirection
        as DISABLED, the Citrix ADC makes the decision to deny the request irrespective
        of the configuration on the backend. If the configured profile has ClientAudioRedirection
        as DEFAULT, then the Citrix ADC forwards the requests to the backend XenApp/XenDesktop
        server.It then makes the decision to allow/deny access based on the policy
        configured on it.
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
