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
module: snmpalarm
short_description: Configuration for alarm resource.
description: Configuration for alarm resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  logging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Logging status of the alarm. When logging is enabled, the Citrix ADC logs
        every trap message that is generated for this alarm.
  normalvalue:
    type: float
    description:
      - Value for the normal threshold. A trap message is generated if the value of
        the respective attribute falls to or below this value after exceeding the
        high threshold.
  severity:
    type: str
    choices:
      - Critical
      - Major
      - Minor
      - Warning
      - Informational
    description:
      - Severity level assigned to trap messages generated by this alarm. The severity
        levels are, in increasing order of severity, C(Informational), C(Warning),
        C(Minor), C(Major), and C(Critical).
      - This parameter is useful when you want the Citrix ADC to send trap messages
        to a trap listener on the basis of severity level. Trap messages with a severity
        level lower than the specified level (in the trap listener entry) are not
        sent.
  thresholdvalue:
    type: float
    description:
      - Value for the high threshold. The Citrix ADC generates an SNMP trap message
        when the value of the attribute associated with the alarm is greater than
        or equal to the specified high threshold value.
  time:
    type: float
    description:
      - 'Interval, in seconds, at which the Citrix ADC generates SNMP trap messages
        when the conditions specified in the SNMP alarm are met.Can be specified for
        the following alarms: SYNFLOOD, HA-VERSION-MISMATCH, HA-SYNC-FAILURE, HA-NO-HEARTBEATS,HA-BAD-SECONDARY-STATE,
        CLUSTER-NODE-HEALTH, CLUSTER-NODE-QUORUM, CLUSTER-VERSION-MISMATCH, CLUSTER-BKHB-FAILED,
        PORT-ALLOC-FAILED, COMPACT-FLASH-ERRORS, HARD-DISK-DRIVE-ERRORS and APPFW
        traps. Default trap time intervals: SYNFLOOD and APPFW traps = 1sec, PORT-ALLOC-FAILED
        = 3600sec(1 hour), PORT-ALLOC-EXCEED = 3600sec(1 hour), SYSLOG-CONNECTION-DROPPED
        = 3600sec(1 hour), Other Traps = 86400sec(1 day)'
  trapname:
    type: str
    choices:
      - CPU-USAGE
      - AVERAGE-CPU
      - MEMORY
      - MGMT-CPU-USAGE
      - SYNFLOOD
      - TCP-SYNFLOOD
      - VSERVER-REQRATE
      - SERVICE-REQRATE
      - ENTITY-RXRATE
      - ENTITY-TXRATE
      - ENTITY-SYNFLOOD
      - SERVICE-MAXCLIENTS
      - HA-STATE-CHANGE
      - ENTITY-STATE
      - CONFIG-CHANGE
      - CONFIG-SAVE
      - SERVICEGROUP-MEMBER-REQRATE
      - SERVICEGROUP-MEMBER-MAXCLIENTS
      - MONITOR-RTO-THRESHOLD
      - LOGIN-FAILURE
      - SSL-CERT-EXPIRY
      - FAN-SPEED-LOW
      - VOLTAGE-LOW
      - VOLTAGE-HIGH
      - TEMPERATURE-HIGH
      - CPU-TEMPERATURE-HIGH
      - POWER-SUPPLY-FAILURE
      - DISK-USAGE-HIGH
      - INTERFACE-THROUGHPUT-LOW
      - MON_PROBE_FAILED
      - HA-VERSION-MISMATCH
      - HA-SYNC-FAILURE
      - HA-NO-HEARTBEATS
      - HA-BAD-SECONDARY-STATE
      - INTERFACE-BW-USAGE
      - RATE-LIMIT-THRESHOLD-EXCEEDED
      - ENTITY-NAME-CHANGE
      - HA-PROP-FAILURE
      - IP-CONFLICT
      - PF-RL-RATE-THRESHOLD
      - PF-RL-PPS-THRESHOLD
      - PF-RL-RATE-PKTS-DROPPED
      - PF-RL-PPS-PKTS-DROPPED
      - APPFW-START-URL
      - APPFW-DENY-URL
      - APPFW-VIOLATIONS-TYPE
      - APPFW-REFERER-HEADER
      - APPFW-CSRF-TAG
      - APPFW-COOKIE
      - APPFW-FIELD-CONSISTENCY
      - APPFW-BUFFER-OVERFLOW
      - APPFW-FIELD-FORMAT
      - APPFW-FILE-UPLOAD-TYPE
      - APPFW-GRPC
      - APPFW-GRPC-WEB-JSON
      - APPFW-GRPC-WEB-TEXT
      - APPFW-JSON-DOS
      - APPFW-JSON-SQL
      - APPFW-JSON-XSS
      - APPFW-SAFE-COMMERCE
      - APPFW-SAFE-OBJECT
      - APPFW-SESSION-LIMIT
      - APPFW-SIGNATURE-MATCH
      - APPFW-POLICY-HIT
      - APPFW-XSS
      - APPFW-XML-XSS
      - APPFW-SQL
      - APPFW-XML-SQL
      - APPFW-XML-ATTACHMENT
      - APPFW-XML-DOS
      - APPFW-XML-VALIDATION
      - APPFW-XML-WSI
      - APPFW-XML-SCHEMA-COMPILE
      - APPFW-XML-SOAP-FAULT
      - APPFW-NEW-SIGNATURE-ADDED
      - APPFW-DEPLOY-RELAXATION-DP
      - APPFW-LEARNED-RULE-APPLIED-DYN-PROF
      - APPFW-CMD
      - APPFW-SCHEMA-ENDPOINT-NOTFOUND
      - APPFW-SCHEMA-METHOD-UNSUPPORTED
      - APPFW-SCHEMA-PARAMETER-MISSING
      - APPFW-SCHEMA-VALUE-INCORRECT
      - APPFW-SCHEMA-CONTENTTYPE-UNSUPPORTED
      - APPFW-SCHEMA-PARAMETER-INVALID
      - APPFW-SCHEMA-OTHER
      - APPFW-SCHEMA-RELAXATION-RULE
      - APPFW-POSTBODYLIMIT
      - APPFW-JSON-CMD
      - APPFW-SQL-GRAM
      - APPFW-JSON-SQL-GRAM
      - APPFW-CMD-GRAM
      - APPFW-JSON-CMD-GRAM
      - APPFW-BLOCK-KEYWORD
      - APPFW-JSON-BLOCKKEYWORD
      - APPFW-BYPASS-LIST
      - APPFW-DENY-LIST
      - DNSKEY-EXPIRY
      - HA-LICENSE-MISMATCH
      - SSL-CARD-FAILED
      - SSL-CARD-NORMAL
      - WARM-RESTART-EVENT
      - HARD-DISK-DRIVE-ERRORS
      - COMPACT-FLASH-ERRORS
      - CALLHOME-UPLOAD-EVENT
      - 1024KEY-EXCHANGE-RATE
      - 2048KEY-EXCHANGE-RATE
      - 4096KEY-EXCHANGE-RATE
      - SSL-CUR-SESSION-INUSE
      - CLUSTER-NODE-HEALTH
      - CLUSTER-NODE-QUORUM
      - CLUSTER-VERSION-MISMATCH
      - CLUSTER-CCO-CHANGE
      - CLUSTER-OVS-CHANGE
      - CLUSTER-SYNC-FAILURE
      - CLUSTER-SYNC-PARTIAL-SUCCESS
      - CLUSTER-PROP-FAILURE
      - CLUSTER-PROP-EXEC-FAILURE
      - HA-STICKY-PRIMARY
      - INBAND-PROTOCOL-VERSION-MISMATCH
      - SSL-CHIP-REINIT
      - VRID-STATE-CHANGE
      - PORT-ALLOC-FAILED
      - LLDP-REMOTE-CHANGE
      - DUPLICATE-IPV6
      - PARTITION-CONFIG-EVENT
      - PARTITION-SWITCHED
      - LSN-PORTALLOC-FAILED
      - LSN-PORTQUOTA-EXCEED
      - LSN-SESSIONQUOTA-EXCEED
      - LSN-MEM-RECOVERY-KICKEDIN
      - VSERVER-SPILLOVER
      - INCONSISTENT-CONFIGURATION-IN-PPES
      - PARTITION-RATE-LIMIT
      - POOLED-LICENSE-ONGRACE
      - POOLED-LICENSE-PARTIAL
      - CLUSTER-BACKPLANE-HB-MISSING
      - GSLB-SITE-MEP-FLAP
      - DNS-MAXNEGCACHE-USAGE
      - DNS-MAXCACHE-USAGE
      - NS-LICENSE-EXPIRY
      - PKT-RATELIMITING-ATTACK
      - GSLB-SYNC-STATUS-FLIP
      - URLFILT-DB-UPDATE-STATUS
      - URLFILT-INIT-SDK
      - POOLED-LICENSE-CHECKOUT-FAILURE
      - MIGRATION-STARTED
      - MIGRATION-COMPLETE
      - ECDHE-EXCHANGE-RATE
      - BOT-SIGNATURE-UPDATE
      - APPFW-XMLPAYLOAD-CONTENT-TYPE-MISMATCH
      - PORT-ALLOC-EXCEED
      - KEK_UPDATE_SUCCESS
      - KEK_UPDATE_FAILURE
      - ADC-ANOMALY
      - SYSLOG-CONNECTION-DROPPED
      - NSROOT_PASSWORD_EXPIRY_WARNING
      - DNSSEC-KEY-AUTOMGMT-STATUS-FAILURE
      - DNSSEC-KEY-AUTOMGMT-STATUS-SUCCESS
      - CLOUD-REST-API-FAILURE
      - SSL-ASYM-CRYPTO-UTILIZATION
      - SSL-SYM-CRYPTO-UTILIZATION
      - INTERFACE-AUTO-RECOVERY
    description:
      - Name of the SNMP alarm. This parameter is required for identifying the SNMP
        alarm and cannot be modified.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample snmpalarm playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure snmpalarm
      delegate_to: localhost
      netscaler.adc.snmpalarm:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        trapname: SYSLOG-CONNECTION-DROPPED
        time: 0
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
