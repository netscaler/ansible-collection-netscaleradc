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
module: location
short_description: Configuration for location resource.
description: Configuration for location resource.
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
  ipfrom:
    type: str
    description:
      - First IP address in the range, in dotted decimal notation.
  ipto:
    type: str
    description:
      - Last IP address in the range, in dotted decimal notation.
  latitude:
    type: int
    description:
      - Numerical value, in degrees, specifying the latitude of the geographical location
        of the IP address-range.
      - 'Note: Longitude and latitude parameters are used for selecting a service
        with the static proximity GSLB method. If they are not specified, selection
        is based on the qualifiers specified for the location.'
  longitude:
    type: int
    description:
      - Numerical value, in degrees, specifying the longitude of the geographical
        location of the IP address-range.
      - 'Note: Longitude and latitude parameters are used for selecting a service
        with the static proximity GSLB method. If they are not specified, selection
        is based on the qualifiers specified for the location.'
  preferredlocation:
    type: str
    description:
      - String of qualifiers, in dotted notation, describing the geographical location
        of the IP address range. Each qualifier is more specific than the one that
        precedes it, as in continent.country.region.city.isp.organization. For example,
        "NA.US.CA.San Jose.ATT.citrix".
      - 'Note: A qualifier that includes a dot (.) or space ( ) must be enclosed in
        double quotation marks.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample location playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure location
      delegate_to: localhost
      netscaler.adc.location:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        ipfrom: 1.1.1.1
        ipto: 2.2.2.2
        preferredlocation: '*.US.*'
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
