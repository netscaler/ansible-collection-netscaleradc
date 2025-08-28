#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: gslbvserver_domain_binding
short_description: Binding Resource definition for describing association between
  gslbvserver and domain resources
description: Binding Resource definition for describing association between gslbvserver
  and domain resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  backupip:
    type: str
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
  backupipflag:
    type: bool
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
  cookie_domain:
    type: str
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
  cookie_domainflag:
    type: bool
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
  cookietimeout:
    type: int
    description:
      - Timeout, in minutes, for the GSLB site cookie.
  domainname:
    type: str
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
  name:
    type: str
    description:
      - Name of the virtual server on which to perform the binding operation.
  order:
    type: int
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
  sitedomainttl:
    type: int
    description:
      - TTL, in seconds, for all internally created site domains (created when a site
        prefix is configured on a GSLB service) that are associated with this virtual
        server.
  ttl:
    type: int
    description:
      - Time to live (TTL) for the domain.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample gslbvserver_domain_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure gslbvserver_domain_binding
      delegate_to: localhost
      netscaler.adc.gslbvserver_domain_binding:
        state: present
        name: LB_ia_gslbv3
        domainname: www.abc.com
        ttl: 5
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
