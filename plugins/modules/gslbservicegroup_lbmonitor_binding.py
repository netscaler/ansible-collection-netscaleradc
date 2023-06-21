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
module: gslbservicegroup_lbmonitor_binding
short_description: Binding Resource definition for describing association between
  gslbservicegroup and lbmonitor resources
description: Binding Resource definition for describing association between gslbservicegroup
  and lbmonitor resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
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
    description:
      - Monitor state.
    type: str
    choices:
      - ENABLED
      - DISABLED
  order:
    description:
      - Order number to be assigned to the gslb servicegroup member
    type: int
  passive:
    description:
      - Indicates if load monitor is passive. A passive load monitor does not remove
        service from LB decision when threshold is breached.
    type: bool
  port:
    description:
      - Port number of the GSLB service. Each service must have a unique port number.
    type: int
  publicip:
    description:
      - The public IP address that a NAT device translates to the GSLB service's private
        IP address. Optional.
    type: str
  publicport:
    description:
      - The public port associated with the GSLB service's public IP address. The
        port is mapped to the service's private port number. Applicable to the local
        GSLB service. Optional.
    type: int
  servicegroupname:
    description:
      - Name of the GSLB service group.
    type: str
  siteprefix:
    description:
      - The site's prefix string. When the GSLB service group is bound to a GSLB virtual
        server, a GSLB site domain is generated internally for each bound serviceitem-domain
        pair by concatenating the site prefix of the service item and the name of
        the domain. If the special string NONE is specified, the site-prefix string
        is unset. When implementing HTTP redirect site persistence, the Citrix ADC
        redirects GSLB requests to GSLB services by using their site domains.
    type: str
  state:
    description:
      - Initial state of the service after binding.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
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
