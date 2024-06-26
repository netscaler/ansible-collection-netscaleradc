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
module: streamidentifier
short_description: Configuration for identifier resource.
description: Configuration for identifier resource.
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
  acceptancethreshold:
    type: raw
    description:
      - Non-Breaching transactions to Total transactions threshold expressed in percent.
      - Maximum of 6 decimal places is supported.
  appflowlog:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable Appflow logging for stream identifier
  breachthreshold:
    type: raw
    description:
      - Breaching transactions threshold calculated over interval.
  interval:
    type: raw
    description:
      - Number of minutes of data to use when calculating session statistics (number
        of requests, bandwidth, and response times). The interval is a moving window
        that keeps the most recently collected data. Older data is discarded at regular
        intervals.
  maxtransactionthreshold:
    type: raw
    description:
      - Maximum per transcation value of metric. Metric to be tracked is specified
        by tracktransactions attribute.
  mintransactionthreshold:
    type: raw
    description:
      - Minimum per transcation value of metric. Metric to be tracked is specified
        by tracktransactions attribute.
  name:
    type: raw
    description:
      - The name of stream identifier.
  samplecount:
    type: raw
    description:
      - Size of the sample from which to select a request for evaluation. The smaller
        the sample count, the more accurate is the statistical data. To evaluate all
        requests, set the sample count to 1. However, such a low setting can result
        in excessive consumption of memory and processing resources.
  selectorname:
    type: raw
    description:
      - Name of the selector to use with the stream identifier.
  snmptrap:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable SNMP trap for stream identifier
  sort:
    type: raw
    choices:
      - REQUESTS
      - CONNECTIONS
      - RESPTIME
      - BANDWIDTH
      - RESPTIME_BREACHES
      - NONE
    description:
      - Sort stored records by the specified statistics column, in descending order.
        Performed during data collection, the sorting enables real-time data evaluation
        through Citrix ADC policies (for example, compression and caching policies)
        that use functions such as IS_TOP(n).
  trackackonlypackets:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Track ack only packets as well. This setting is applicable only when packet
        rate limiting is being used.
  tracktransactions:
    type: raw
    choices:
      - RESPTIME
      - NONE
    description:
      - 'Track transactions exceeding configured threshold. Transaction tracking can
        be enabled for following metric: ResponseTime.'
      - By default transaction tracking is disabled
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
