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
module: dnspolicy
short_description: Configuration for DNS policy resource.
description: Configuration for DNS policy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  actionname:
    description:
      - 'Name of the DNS action to perform when the rule evaluates to TRUE. The built
        in actions function as follows:'
      - '* dns_default_act_Drop. Drop the DNS request.'
      - '* dns_default_act_Cachebypass. Bypass the DNS cache and forward the request
        to the name server.'
      - You can create custom actions by using the add dns action command in the CLI
        or the DNS > Actions > Create DNS Action dialog box in the Citrix ADC configuration
        utility.
    type: str
  cachebypass:
    choices:
      - true
      - false
    description:
      - By pass dns cache for this.
    type: str
  drop:
    choices:
      - true
      - false
    description:
      - The dns packet must be dropped.
    type: str
  logaction:
    description:
      - Name of the messagelog action to use for requests that match this policy.
    type: str
  name:
    description:
      - Name for the DNS policy.
    type: str
  preferredlocation:
    description:
      - The location used for the given policy. This is deprecated attribute. Please
        use -prefLocList
    type: str
  preferredloclist:
    description:
      - The location list in priority order used for the given policy.
    type: list
    elements: str
  rule:
    description:
      - Expression against which DNS traffic is evaluated.
      - 'Note:'
      - '* On the command line interface, if the expression includes blank spaces,
        the entire expression must be enclosed in double quotation marks.'
      - '* If the expression itself includes double quotation marks, you must escape
        the quotations by using the  character. '
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks. '
      - 'Example: CLIENT.UDP.DNS.DOMAIN.EQ("domainname")'
    type: str
  viewname:
    description:
      - The view name that must be used for the given policy.
    type: str
  dnspolicylabel_dnspolicy_binding:
    type: dict
    description: Bindings for dnspolicylabel_dnspolicy_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
