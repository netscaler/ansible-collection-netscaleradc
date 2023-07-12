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
module: auditnslogparams
short_description: Configuration for ns log parameters resource.
description: Configuration for ns log parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  acl:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Configure auditing to log access control list (ACL) messages.
    type: str
  alg:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log the ALG messages
    type: str
  appflowexport:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Export log messages to AppFlow collectors.
      - Appflow collectors are entities to which log messages can be sent so that
        some action can be performed on them.
    type: str
  contentinspectionlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log Content Inspection event information
    type: str
  dateformat:
    choices:
      - MMDDYYYY
      - DDMMYYYY
      - YYYYMMDD
    description:
      - Format of dates in the logs.
      - 'Supported formats are: '
      - '* C(MMDDYYYY) - U.S. style month/date/year format.'
      - '* C(DDMMYYYY) - European style date/month/year format.'
      - '* C(YYYYMMDD) - ISO style year/month/date format.'
    type: str
  logfacility:
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
      - 'Facility value, as defined in RFC 3164, assigned to the log message. '
      - Log facility values are numbers 0 to 7 (C(LOCAL0) through C(LOCAL7)). Each
        number indicates where a specific message originated from, such as the Citrix
        ADC itself, the VPN, or external.
    type: str
  loglevel:
    choices:
      - ALL
      - EMERGENCY
      - ALERT
      - CRITICAL
      - ERROR
      - WARNING
      - NOTICE
      - INFORMATIONAL
      - DEBUG
      - NONE
    description:
      - 'Types of information to be logged. '
      - 'Available settings function as follows: '
      - '* C(ALL) - All events.'
      - '* C(EMERGENCY) - Events that indicate an immediate crisis on the server.'
      - '* C(ALERT) - Events that might require action.'
      - '* C(CRITICAL) - Events that indicate an imminent server crisis.'
      - '* C(ERROR) - Events that indicate some type of error.'
      - '* C(WARNING) - Events that require action in the near future.'
      - '* C(NOTICE) - Events that the administrator should know about.'
      - '* C(INFORMATIONAL) - All but low-level events.'
      - '* C(DEBUG) - All events, in extreme detail.'
      - '* C(NONE) - No events.'
    type: list
    elements: str
  lsn:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log the LSN messages
    type: str
  serverip:
    description:
      - IP address of the nslog server.
    type: str
  serverport:
    description:
      - Port on which the nslog server accepts connections.
    type: int
  sslinterception:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log SSL Interception event information
    type: str
  subscriberlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log subscriber session event information
    type: str
  tcp:
    choices:
      - NONE
      - ALL
    description:
      - Configure auditing to log TCP messages.
    type: str
  timezone:
    choices:
      - GMT_TIME
      - LOCAL_TIME
    description:
      - 'Time zone used for date and timestamps in the logs. '
      - 'Supported settings are: '
      - '* C(GMT_TIME) - Coordinated Universal Time.'
      - '* C(LOCAL_TIME) - Use the server''s timezone setting.'
    type: str
  urlfiltering:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log URL filtering event information
    type: str
  userdefinedauditlog:
    choices:
      - true
      - false
    description:
      - Log user-configurable log messages to nslog.
      - Setting this parameter to NO causes auditing to ignore all user-configured
        message actions. Setting this parameter to YES causes auditing to log user-configured
        message actions that meet the other logging criteria.
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