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
module: cspolicylabel
short_description: Configuration for CS policy label resource.
description: Configuration for CS policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  cspolicylabeltype:
    type: str
    choices:
      - HTTP
      - TCP
      - RTSP
      - SSL
      - SSL_TCP
      - UDP
      - DNS
      - SIP_UDP
      - SIP_TCP
      - ANY
      - RADIUS
      - RDP
      - MYSQL
      - MSSQL
      - ORACLE
      - DIAMETER
      - SSL_DIAMETER
      - FTP
      - DNS_TCP
      - SMPP
      - MQTT
      - MQTT_TLS
      - HTTP_QUIC
    description:
      - 'Protocol supported by the policy label. All policies bound to the policy
        label must either match the specified protocol or be a subtype of that protocol.
        Available settings function as follows:'
      - '* C(HTTP) - Supports policies that process C(HTTP) traffic. Used to access
        unencrypted Web sites. (The default.)'
      - '* C(SSL) - Supports policies that process HTTPS/C(SSL) encrypted traffic.
        Used to access encrypted Web sites.'
      - '* C(TCP) - Supports policies that process any type of C(TCP) traffic, including
        C(HTTP).'
      - '* C(SSL_TCP) - Supports policies that process C(SSL)-encrypted C(TCP) traffic,
        including C(SSL).'
      - '* C(UDP) - Supports policies that process any type of C(UDP)-based traffic,
        including C(DNS).'
      - '* C(DNS) - Supports policies that process C(DNS) traffic.'
      - '* C(ANY) - Supports all types of policies except C(HTTP), C(SSL), and C(TCP).'
      - '* C(SIP_UDP) - Supports policies that process C(UDP) based Session Initiation
        Protocol (SIP) traffic. SIP initiates, manages, and terminates multimedia
        communications sessions, and has emerged as the standard for Internet telephony
        (VoIP).'
      - '* C(RTSP) - Supports policies that process Real Time Streaming Protocol (C(RTSP))
        traffic. C(RTSP) provides delivery of multimedia and other streaming data,
        such as audio, video, and other types of streamed media.'
      - '* C(RADIUS) - Supports policies that process Remote Authentication Dial In
        User Service (C(RADIUS)) traffic. C(RADIUS) supports combined authentication,
        authorization, and auditing services for network management.'
      - '* C(MYSQL) - Supports policies that process C(MYSQL) traffic.'
      - '* C(MSSQL) - Supports policies that process Microsoft SQL traffic.'
  labelname:
    type: str
    description:
      - Name for the policy label. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters.
      - The label name must be unique within the list of policy labels for content
        switching.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policylabel" or 'my policylabel').
  newname:
    type: str
    description:
      - The new name of the content switching policylabel.
  cspolicylabel_cspolicy_binding:
    type: dict
    description: Bindings for cspolicylabel_cspolicy_binding resource
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
---
- name: Sample cspolicylabel playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cspolicylabel
      delegate_to: localhost
      netscaler.adc.cspolicylabel:
        state: present
        labelname: plab1
        newname: plab1_new
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
