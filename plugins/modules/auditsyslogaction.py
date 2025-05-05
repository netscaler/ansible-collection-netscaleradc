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
module: auditsyslogaction
short_description: Configuration for system log action resource.
description: Configuration for system log action resource.
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
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
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
      - Log alg info
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
      - Log Content Inspection event information
  dateformat:
    type: str
    choices:
      - MMDDYYYY
      - DDMMYYYY
      - YYYYMMDD
    description:
      - Format of dates in the logs.
      - 'Supported formats are:'
      - '* C(MMDDYYYY). -U.S. style month/date/year format.'
      - '* C(DDMMYYYY) - European style date/month/year format.'
      - '* C(YYYYMMDD) - ISO style year/month/date format.'
  dns:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log DNS related syslog messages
  domainresolvenow:
    type: bool
    description:
      - Immediately send a DNS query to resolve the server's domain name.
  domainresolveretry:
    type: int
    description:
      - Time, in seconds, for which the Citrix ADC waits before sending another DNS
        query to resolve the host name of the syslog server if the last query failed.
  lbvservername:
    type: str
    description:
      - Name of the LB vserver. Mutually exclusive with syslog serverIP/serverName
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
      - DEBUG
      - NONE
    description:
      - Audit log level, which specifies the types of events to log.
      - 'Available values function as follows:'
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
    elements: str
  lsn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log lsn info
  managementlog:
    type: list
    choices:
      - ALL
      - SHELL
      - ACCESS
      - NSMGMT
      - NONE
    description:
      - Management log specifies the categories of log files to be exported.
      - It use destination and transport from PE params.
      - 'Available values function as follows:'
      - '* C(ALL) - All categories (C(SHELL), C(NSMGMT) and C(ACCESS)).'
      - '* C(SHELL) -  bash.log, and sh.log.'
      - '* C(ACCESS) - auth.log, nsvpn.log, vpndebug.log, httpaccess.log, httperror.log,
        httpaccess-vpn.log and httperror-vpn.log.'
      - '* C(NSMGMT) - notice.log and ns.log.'
      - '* C(NONE) - No logs.'
    elements: str
  maxlogdatasizetohold:
    type: float
    description:
      - Max size of log data that can be held in NSB chain of server info.
  mgmtloglevel:
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
      - DEBUG
      - NONE
    description:
      - Management log level, which specifies the types of events to log.
      - 'Available values function as follows:'
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
    elements: str
  name:
    type: str
    description:
      - Name of the syslog action. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the syslog action is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my syslog action" or 'my syslog action').
  netprofile:
    type: str
    description:
      - Name of the network profile.
      - The SNIP configured in the network profile will be used as source IP while
        sending log messages.
  serverdomainname:
    type: str
    description:
      - SYSLOG server name as a FQDN.  Mutually exclusive with serverIP/lbVserverName
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
      - Log SSL Interception event information
  streamanalytics:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Export log stream analytics statistics to syslog server.
  subscriberlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log subscriber session event information
  syslogcompliance:
    type: str
    choices:
      - RFC5424
    description:
      - Setting this parameter ensures that all the Audit Logs generated for this
        Syslog Action comply with an RFC. For example, set it to C(RFC5424) to ensure
        RFC 5424 compliance
  tcp:
    type: str
    choices:
      - NONE
      - ALL
    description:
      - Log TCP messages.
  tcpprofilename:
    type: str
    description:
      - Name of the TCP profile whose settings are to be applied to the audit server
        info to tune the TCP connection parameters.
  timezone:
    type: str
    choices:
      - GMT_TIME
      - LOCAL_TIME
    description:
      - Time zone used for date and timestamps in the logs.
      - 'Supported settings are:'
      - '* C(GMT_TIME). Coordinated Universal time.'
      - '* C(LOCAL_TIME). Use the server''s timezone setting.'
  transport:
    type: str
    choices:
      - TCP
      - UDP
    description:
      - Transport type used to send auditlogs to syslog server. Default type is C(UDP).
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
      - Setting this parameter to C(NO) causes auditing to ignore all user-configured
        message actions. Setting this parameter to C(YES) causes auditing to log user-configured
        message actions that meet the other logging criteria.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample auditsyslogaction playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure auditsyslogaction
      delegate_to: localhost
      netscaler.adc.auditsyslogaction:
        state: present
        name: act1121
        lbvservername: lb511
        loglevel:
          - ALL
        lsn: ENABLED
        transport: TCP
        maxlogdatasizetohold: '1000'
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
