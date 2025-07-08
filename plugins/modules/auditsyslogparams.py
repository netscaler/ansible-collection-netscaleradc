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
module: auditsyslogparams
short_description: Configuration for system log parameters resource.
description: Configuration for system log parameters resource.
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
  acl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log access control list (ACL) messages.
  alg:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log the ALG messages
  appflowexport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Export log messages to AppFlow collectors.
      - Appflow collectors are entities to which log messages can be sent so that
        some action can be performed on them.
  contentinspectionlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log Content Inspection event ifnormation
  dateformat:
    type: str
    choices:
      - MMDDYYYY
      - DDMMYYYY
      - YYYYMMDD
    description:
      - Format of dates in the logs.
      - 'Supported formats are:'
      - '* C(MMDDYYYY) - U.S. style month/date/year format.'
      - '* C(DDMMYYYY). European style  -date/month/year format.'
      - '* C(YYYYMMDD) - ISO style year/month/date format.'
  dns:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log DNS related syslog messages
  logfacility:
    type: str
    choices:
      - LOCAL0
      - LOCAL1
      - LOCAL2
      - LOCAL3
      - LOCAL4
      - LOCAL5
      - LOCAL6
      - LOCAL7
    description:
      - Facility value, as defined in RFC 3164, assigned to the log message.
      - Log facility values are numbers 0 to 7 (C(LOCAL0) through C(LOCAL7)). Each
        number indicates where a specific message originated from, such as the Citrix
        ADC itself, the VPN, or external.
  loglevel:
    type: list
    choices:
      - ALL
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - NONE
    description:
      - Types of information to be logged.
      - 'Available settings function as follows:'
      - '* C(ALL) - All events.'
      - '* C(EMERGENCY) - Events that indicate an immediate crisis on the server.'
      - '* C(ALERT) - Events that might require action.'
      - '* C(CRITICAL) - Events that indicate an imminent server crisis.'
      - '* C(ERROR) - Events that indicate some type of error.'
      - '* C(WARNING) - Events that require action in the near future.'
      - '* C(NOTICE) - Events that the administrator should know about.'
      - '* C(INFORMATIONAL) - All but low-level events.'
      - '* C(NONE) - No events.'
    elements: str
  lsn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log the LSN messages
  protocolviolations:
    type: str
    choices:
      - ALL
      - NONE
    description:
      - Log protocol violations
  serverip:
    type: str
    description:
      - IP address of the syslog server.
  serverport:
    type: int
    description:
      - Port on which the syslog server accepts connections.
  sslinterception:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log SSL Interceptionn event information
  streamanalytics:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Export log stream analytics statistics to syslog server
  subscriberlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log subscriber session event information
  tcp:
    type: str
    choices:
      - NONE
      - ALL
    description:
      - Log TCP messages.
  timezone:
    type: str
    choices:
      - GMT_TIME
      - LOCAL_TIME
    description:
      - Time zone used for date and timestamps in the logs.
      - 'Available settings function as follows:'
      - '* C(GMT_TIME) - Coordinated Universal Time.'
      - '* C(LOCAL_TIME)  Use the server''s timezone setting.'
  urlfiltering:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log URL filtering event information
  userdefinedauditlog:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Log user-configurable log messages to syslog.
      - Setting this parameter to C(NO) causes audit to ignore all user-configured
        message actions. Setting this parameter to C(YES) causes audit to log user-configured
        message actions that meet the other logging criteria.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample auditsyslogparams playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure auditsyslogparams
      delegate_to: localhost
      netscaler.adc.auditsyslogparams:
        state: present
        loglevel:
          - ALL
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
