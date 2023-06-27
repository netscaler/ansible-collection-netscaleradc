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
module: servicegroup_lbmonitor_binding
short_description: Binding Resource definition for describing association between
  servicegroup and lbmonitor resources
description: Binding Resource definition for describing association between servicegroup
  and lbmonitor resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  customserverid:
    description:
      - Unique service identifier. Used when the persistency type for the virtual
        server is set to Custom Server ID.
    type: str
    default: '"None"'
  dbsttl:
    description:
      - Specify the TTL for DNS record for domain based service.The default value
        of ttl is 0 which indicates to use the TTL received in DNS response for monitors
    type: int
  hashid:
    description:
      - Unique numerical identifier used by hash based load balancing methods to identify
        a service.
    type: int
  monitor_name:
    description:
      - Monitor name.
    type: str
  monstate:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Monitor state.
    type: str
  nameserver:
    description:
      - Specify the nameserver to which the query for bound domain needs to be sent.
        If not specified, use the global nameserver
    type: str
  order:
    description:
      - Order number to be assigned to the servicegroup member
    type: int
  passive:
    description:
      - Indicates if load monitor is passive. A passive load monitor does not remove
        service from LB decision when threshold is breached.
    type: bool
  port:
    description:
      - Port number of the service. Each service must have a unique port number.
    type: int
  serverid:
    description:
      - The  identifier for the service. This is used when the persistency type is
        set to Custom Server ID.
    type: int
  servicegroupname:
    description:
      - Name of the service group.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Initial state of the service after binding.
    type: str
    default: ENABLED
  weight:
    description:
      - Weight to assign to the servers in the service group. Specifies the capacity
        of the servers relative to the other servers in the load balancing configuration.
        The higher the weight, the higher the percentage of requests sent to the service.
    type: int
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
