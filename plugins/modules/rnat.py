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
module: rnat
short_description: Configuration for RNAT configured route resource.
description: Configuration for RNAT configured route resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aclname:
    description:
      - An extended ACL defined for the RNAT entry.
    type: str
  connfailover:
    description:
      - Synchronize all connection-related information for the RNAT sessions with
        the secondary ADC in a high availability (HA) pair.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  name:
    description:
      - Name for the RNAT4 rule. Must begin with a letter, number, or the underscore
        character (_), and can consist of letters, numbers, and the hyphen (-), period
        (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore
        characters. Cannot be changed after the rule is created. Choose a name that
        helps identify the RNAT4 rule.
    type: str
  natip:
    description:
      - Any NetScaler-owned IPv4 address except the NSIP address. The NetScaler appliance
        replaces the source IP addresses of server-generated packets with the IP address
        specified. The IP address must be a public NetScaler-owned IP address. If
        you specify multiple addresses for this field, NATIP selection uses the round
        robin algorithm for each session. By specifying a range of IP addresses, you
        can specify all NetScaler-owned IP addresses, except the NSIP, that fall within
        the specified range.
    type: str
  netmask:
    description:
      - The subnet mask for the network address.
    type: str
  network:
    description:
      - The network address defined for the RNAT entry.
    type: str
  newname:
    description:
      - New name for the RNAT4 rule. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain       only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
    type: str
  ownergroup:
    description:
      - The owner node group in a Cluster for this rnat rule.
    type: str
    default: DEFAULT_NG
  redirectport:
    description:
      - Port number to which the IPv4 packets are redirected. Applicable to TCP and
        UDP protocols.
    type: int
  srcippersistency:
    description:
      - Enables the Citrix ADC to use the same NAT IP address for all RNAT sessions
        initiated from a particular server.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  useproxyport:
    description:
      - Enable source port proxying, which enables the Citrix ADC to use the RNAT
        ips using proxied source port.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
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
