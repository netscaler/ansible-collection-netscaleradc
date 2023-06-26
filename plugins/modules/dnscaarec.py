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
module: dnscaarec
short_description: Configuration for CAA record resource.
description: Configuration for CAA record resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  domain:
    description:
      - Domain name of the CAA record.
    type: str
  ecssubnet:
    description:
      - Subnet for which the cached CAA record need to be removed.
    type: str
  flag:
    description:
      - Flag associated with the CAA record.
    type: str
    default: 5
    choices:
      - NONE
      - CRITICAL
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: int
  recordid:
    description:
      - Unique, internally generated record ID. View the details of the CAA record
        to obtain its record ID. Records can be removedby either specifying the domain
        name and record id OR by specifying domain name and all other CAA record attributes
        as was supplied during the add command.
    type: int
  tag:
    description:
      - String that represents the identifier of the property represented by the CAA
        record. The RFC currently defines three available tags - issue, issuwild and
        iodef.
    type: str
    default: '"issue"'
  ttl:
    description:
      - Time to Live (TTL), in seconds, for the record. TTL is the time for which
        the record must be cached by DNS proxies. The specified TTL is applied to
        all the resource records that are of the same record type and belong to the
        specified domain name. For example, if you add an address record, with a TTL
        of 36000, to the domain name example.com, the TTLs of all the address records
        of example.com are changed to 36000. If the TTL is not specified, the Citrix
        ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available
        on the appliance, the default value of 3600.
    type: int
    default: 3600
  type:
    description:
      - 'Type of records to display. Available settings function as follows:'
      - '* ADNS - Display all authoritative address records.'
      - '* PROXY - Display all proxy address records.'
      - '* ALL - Display all address records.'
    type: str
    default: ADNS
    choices:
      - ALL
      - ADNS
      - PROXY
  valuestring:
    description:
      - Value associated with the chosen property tag in the CAA resource record.
        Enclose the string in single or double quotation marks.
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