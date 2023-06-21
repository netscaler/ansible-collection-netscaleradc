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
module: cspolicylabel
short_description: Configuration for CS policy label resource.
description: Configuration for CS policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  cspolicylabeltype:
    description:
      - 'Protocol supported by the policy label. All policies bound to the policy
        label must either match the specified protocol or be a subtype of that protocol.
        Available settings function as follows:'
      - '* HTTP - Supports policies that process HTTP traffic. Used to access unencrypted
        Web sites. (The default.)'
      - '* SSL - Supports policies that process HTTPS/SSL encrypted traffic. Used
        to access encrypted Web sites.'
      - '* TCP - Supports policies that process any type of TCP traffic, including
        HTTP.'
      - '* SSL_TCP - Supports policies that process SSL-encrypted TCP traffic, including
        SSL.'
      - '* UDP - Supports policies that process any type of UDP-based traffic, including
        DNS.'
      - '* DNS - Supports policies that process DNS traffic.'
      - '* ANY - Supports all types of policies except HTTP, SSL, and TCP.             '
      - '* SIP_UDP - Supports policies that process UDP based Session Initiation Protocol
        (SIP) traffic. SIP initiates, manages, and terminates multimedia communications
        sessions, and has emerged as the standard for Internet telephony (VoIP).'
      - '* RTSP - Supports policies that process Real Time Streaming Protocol (RTSP)
        traffic. RTSP provides delivery of multimedia and other streaming data, such
        as audio, video, and other types of streamed media.'
      - '* RADIUS - Supports policies that process Remote Authentication Dial In User
        Service (RADIUS) traffic. RADIUS supports combined authentication, authorization,
        and auditing services for network management.'
      - '* MYSQL - Supports policies that process MYSQL traffic.'
      - '* MSSQL - Supports policies that process Microsoft SQL traffic.'
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
  labelname:
    description:
      - 'Name for the policy label. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. '
      - The label name must be unique within the list of policy labels for content
        switching.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policylabel" or 'my policylabel').
    type: str
  newname:
    description:
      - The new name of the content switching policylabel.
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
