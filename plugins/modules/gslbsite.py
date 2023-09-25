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
module: gslbsite
short_description: Configuration for GSLB site resource.
description: Configuration for GSLB site resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  backupparentlist:
    description:
      - The list of backup gslb sites configured in preferred order. Need to be parent
        gsb sites.
    type: list
    elements: str
    default: '"None"'
  clip:
    description:
      - 'Cluster IP address. Specify this parameter to connect to the remote cluster
        site for GSLB auto-sync. Note: The cluster IP address is defined when creating
        the cluster.'
    type: str
  metricexchange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'Exchange metrics with other sites. Metrics are exchanged by using Metric
        Exchange Protocol (MEP). The appliances in the GSLB setup exchange health
        information once every second. '
      - ''
      - If you disable metrics exchange, you can use only static load balancing methods
        (such as round robin, static proximity, or the hash-based methods), and if
        you disable metrics exchange when a dynamic load balancing method (such as
        least connection) is in operation, the appliance falls back to round robin.
        Also, if you disable metrics exchange, you must use a monitor to determine
        the state of GSLB services. Otherwise, the service is marked as DOWN.
    type: str
    default: ENABLED
  naptrreplacementsuffix:
    description:
      - The naptr replacement suffix configured here will be used to construct the
        naptr replacement field in NAPTR record.
    type: str
  nwmetricexchange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Exchange, with other GSLB sites, network metrics such as round-trip time (RTT),
        learned from communications with various local DNS (LDNS) servers used by
        clients. RTT information is used in the dynamic RTT load balancing method,
        and is exchanged every 5 seconds.
    type: str
    default: ENABLED
  parentsite:
    description:
      - Parent site of the GSLB site, in a parent-child topology.
    type: str
  publicclip:
    description:
      - IP address to be used to globally access the remote cluster when it is deployed
        behind a NAT. It can be same as the normal cluster IP address.
    type: str
  publicip:
    description:
      - Public IP address for the local site. Required only if the appliance is deployed
        in a private address space and the site has a public IP address hosted on
        an external firewall or a NAT device.
    type: str
  sessionexchange:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Exchange persistent session entries with other GSLB sites every five seconds.
    type: str
    default: ENABLED
  siteipaddress:
    description:
      - IP address for the GSLB site. The GSLB site uses this IP address to communicate
        with other GSLB sites. For a local site, use any IP address that is owned
        by the appliance (for example, a SNIP or MIP address, or the IP address of
        the ADNS service).
    type: str
  sitename:
    description:
      - Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my gslbsite" or ''my gslbsite'').'
    type: str
  sitetype:
    choices:
      - REMOTE
      - LOCAL
    description:
      - Type of site to create. If the type is not specified, the appliance automatically
        detects and sets the type on the basis of the IP address being assigned to
        the site. If the specified site IP address is owned by the appliance (for
        example, a MIP address or SNIP address), the site is a local site. Otherwise,
        it is a remote site.
    type: str
    default: NONE
  triggermonitor:
    choices:
      - ALWAYS
      - MEPDOWN
      - MEPDOWN_SVCDOWN
    description:
      - 'Specify the conditions under which the GSLB service must be monitored by
        a monitor, if one is bound. Available settings function as follows:'
      - '* C(ALWAYS) - Monitor the GSLB service at all times.'
      - '* C(MEPDOWN) - Monitor the GSLB service only when the exchange of metrics
        through the Metrics Exchange Protocol (MEP) is disabled.'
      - 'C(MEPDOWN_SVCDOWN) - Monitor the service in either of the following situations: '
      - '* The exchange of metrics through MEP is disabled.'
      - '* The exchange of metrics through MEP is enabled but the status of the service,
        learned through metrics exchange, is DOWN.'
    type: str
    default: ALWAYS
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
