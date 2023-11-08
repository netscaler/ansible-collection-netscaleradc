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
module: systementitydata
short_description: Configuration for entity data resource.
description: Configuration for entity data resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  alldeleted:
    type: bool
    description:
      - Specify this if you would like to delete information about all deleted entities
        from the database.
  allinactive:
    type: bool
    description:
      - Specify this if you would like to delete information about all inactive entities
        from the database.
  core:
    type: int
    description:
      - Specify core ID of the PE in nCore.
  counters:
    type: str
    description:
      - Specify the counters to be collected.
  datasource:
    type: str
    description:
      - Specifies the source which contains all the stored counter values.
  endtime:
    type: str
    description:
      - Specify end time in mmddyyyyhhmm upto which values have to be collected.
  last:
    type: int
    description:
      - 'Last is literal way of saying a certain time period from the current moment.
        Example: -last 1 hour, -last 1 day, et cetera.'
    default: 1
  name:
    type: str
    description:
      - Specify the entity name.
  starttime:
    type: str
    description:
      - Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.
  type:
    type: str
    description:
      - Specify the entity type.
  unit:
    type: str
    choices:
      - HOURS
      - DAYS
      - MONTHS
    description:
      - Specify the time period from current moment. Example 1 x where x = hours/
        days/ years.
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
