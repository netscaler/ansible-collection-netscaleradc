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
module: rnat6
short_description: Configuration for IPv6 RNAT configured route resource.
description: Configuration for IPv6 RNAT configured route resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  acl6name:
    description:
      - Name of any configured ACL6 whose action is ALLOW. The rule of the ACL6 is
        used as an RNAT6 rule.
    type: str
  name:
    description:
      - Name for the RNAT6 rule. Must begin with a letter, number, or the underscore
        character (_), and can consist of letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the rule is created. Choose a name that
        helps identify the RNAT6 rule.
    type: str
  network:
    description:
      - IPv6 address of the network on whose traffic you want the Citrix ADC to do
        RNAT processing.
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for this rnat rule.
    type: str
    default: DEFAULT_NG
  redirectport:
    description:
      - Port number to which the IPv6 packets are redirected. Applicable to TCP and
        UDP protocols.
    type: int
  srcippersistency:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable source ip persistency, which enables the Citrix ADC to use the RNAT
        ips using source ip.
    type: str
    default: DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  rnat6_nsip6_binding:
    type: dict
    description: Bindings for rnat6_nsip6_binding resource
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
