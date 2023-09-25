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
module: reportingconfig
short_description: Configuration for reporting config resource.
description: Configuration for reporting config resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  entitytypes:
    choices:
      - appfwpolicy
      - appfwpolicylabel
      - appfwprofile
      - appqoepolicy
      - authenticationloginschemapolicy
      - authenticationoauthidppolicy
      - authenticationpolicy
      - authenticationpolicylabel
      - authenticationsamlidppolicy
      - authenticationvserver
      - authorizationpolicylabel
      - botpolicy
      - botpolicylabel
      - botprofile
      - cachecontentgroup
      - cachepolicy
      - cachepolicylabel
      - cmppolicy
      - cmppolicylabel
      - contentinspectionpolicy
      - contentinspectionpolicylabel
      - crvserver
      - csvserver
      - dnspolicylabel
      - dnsrecords
      - dospolicy
      - gslbdomain
      - gslbservice
      - gslbservicegroup
      - gslbservicegroupmember
      - gslbsite
      - gslbvserver
      - inat
      - inatsession
      - lbvserver
      - lldp
      - nsacl
      - nsacl6
      - nslimitidentifier
      - nsmemory
      - nspbr
      - nspbr6
      - pcpserver
      - responderpolicy
      - responderpolicylabel
      - rewritepolicy
      - rewritepolicylabel
      - rnatip
      - service
      - servicegroup
      - servicegroupmember
      - spilloverpolicy
      - sslvserver
      - tmsessionpolicy
      - tmtrafficpolicy
      - tunnelip
      - tunnelip6
      - uservserver
      - videooptimizationdetectionpolicy
      - videooptimizationdetectionpolicylabel
      - videooptimizationpacingpolicy
      - videooptimizationpacingpolicylabel
      - vlan
      - vxlan
    description:
      - Object type of the entity
    type: str
  name:
    description:
      - Name of the entity
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
