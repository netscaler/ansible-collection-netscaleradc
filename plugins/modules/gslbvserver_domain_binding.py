#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: gslbvserver_domain_binding
short_description: Binding Resource definition for describing association between
  gslbvserver and domain resources
description: Binding Resource definition for describing association between gslbvserver
  and domain resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  backupip:
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
    type: str
  backupipflag:
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
    type: bool
  cookie_domain:
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
    type: str
  cookie_domainflag:
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
    type: bool
  cookietimeout:
    description:
      - Timeout, in minutes, for the GSLB site cookie.
    type: float
  domainname:
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
    type: str
  name:
    description:
      - Name of the virtual server on which to perform the binding operation.
    type: str
  order:
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
    type: float
  sitedomainttl:
    description:
      - TTL, in seconds, for all internally created site domains (created when a site
        prefix is configured on a GSLB service) that are associated with this virtual
        server.
    type: float
  ttl:
    description:
      - Time to live (TTL) for the domain.
    type: float
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
