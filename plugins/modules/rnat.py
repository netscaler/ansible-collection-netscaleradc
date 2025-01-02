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
module: rnat
short_description: Configuration for RNAT configured route resource.
description: Configuration for RNAT configured route resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  aclname:
    type: str
    description:
      - An extended ACL defined for the RNAT entry.
  connfailover:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Synchronize all connection-related information for the RNAT sessions with
        the secondary ADC in a high availability (HA) pair.
  name:
    type: str
    description:
      - Name for the RNAT4 rule. Must begin with a letter, number, or the underscore
        character (_), and can consist of letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the rule is created. Choose a name that
        helps identify the RNAT4 rule.
  natip:
    type: str
    description:
      - Any NetScaler-owned IPv4 address except the NSIP address. The NetScaler appliance
        replaces the source IP addresses of server-generated packets with the IP address
        specified. The IP address must be a public NetScaler-owned IP address. If
        you specify multiple addresses for this field, NATIP selection uses the round
        robin algorithm for each session. By specifying a range of IP addresses, you
        can specify all NetScaler-owned IP addresses, except the NSIP, that fall within
        the specified range.
  netmask:
    type: str
    description:
      - The subnet mask for the network address.
  network:
    type: str
    description:
      - The network address defined for the RNAT entry.
  newname:
    type: str
    description:
      - New name for the RNAT4 rule. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain       only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
  ownergroup:
    type: str
    description:
      - The owner node group in a Cluster for this rnat rule.
  redirectport:
    type: int
    description:
      - Port number to which the IPv4 packets are redirected. Applicable to TCP and
        UDP protocols.
  srcippersistency:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enables the Citrix ADC to use the same NAT IP address for all RNAT sessions
        initiated from a particular server.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  useproxyport:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable source port proxying, which enables the Citrix ADC to use the RNAT
        ips using proxied source port.
  rnat6_nsip6_binding:
    type: dict
    description: Bindings for rnat6_nsip6_binding resource
    suboptions:
      mode:
        type: str
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
  rnat_nsip_binding:
    type: dict
    description: Bindings for rnat_nsip_binding resource
    suboptions:
      mode:
        type: str
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
  rnat_retainsourceportset_binding:
    type: dict
    description: Bindings for rnat_retainsourceportset_binding resource
    suboptions:
      mode:
        type: str
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
  rnatglobal_auditsyslogpolicy_binding:
    type: dict
    description: Bindings for rnatglobal_auditsyslogpolicy_binding resource
    suboptions:
      mode:
        type: str
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
---
- name: Sample rnat playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure rnat
      delegate_to: localhost
      netscaler.adc.rnat:
        state: present
        name: RNAT_SF_Allow_USE1-A
        aclname: ACL_SF_Allow_USE1-A
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
