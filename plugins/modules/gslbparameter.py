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
module: gslbparameter
short_description: Configuration for GSLB parameter resource.
description: Configuration for GSLB parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  automaticconfigsync:
    choices:
      - ENABLED
      - DISABLED
    description:
      - GSLB configuration will be synced automatically to remote gslb sites if enabled.
    type: str
    default: DISABLED
  dropldnsreq:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop LDNS requests if round-trip time (RTT) information is not available.
    type: str
    default: DISABLED
  gslbconfigsyncmonitor:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, remote gslb site's rsync port will be monitored and site is considered
        for configuration sync only when the monitor is successful.
    type: str
    default: DISABLED
  gslbsvcstatedelaytime:
    description:
      - Amount of delay in updating the state of GSLB service to DOWN when MEP goes
        down.
      - "\t\t\tThis parameter is applicable only if monitors are not bound to GSLB\
        \ services"
    type: int
  gslbsyncinterval:
    description:
      - Time duartion (in seconds) for which the gslb sync process will wait before
        checking for config changes.
    type: int
    default: 10
  gslbsynclocfiles:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If disabled, Location files will not be synced to the remote sites as part
        of automatic sync.
    type: str
    default: ENABLED
  gslbsyncmode:
    choices:
      - IncrementalSync
      - FullSync
    description:
      - Mode in which configuration will be synced from master site to remote sites.
    type: str
    default: IncrementalSync
  gslbsyncsaveconfigcommand:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, 'save ns config' command will be treated as other GSLB commands
        and synced to GSLB nodes when auto gslb sync option is enabled.
    type: str
    default: DISABLED
  ldnsentrytimeout:
    description:
      - Time, in seconds, after which an inactive LDNS entry is removed.
    type: int
    default: 180
  ldnsmask:
    description:
      - The IPv4 network mask with which to create LDNS entries.
    type: str
  ldnsprobeorder:
    choices:
      - PING
      - DNS
      - TCP
    description:
      - Order in which monitors should be initiated to calculate RTT.
    type: list
    elements: str
  mepkeepalivetimeout:
    description:
      - Time duartion (in seconds) during which if no new packets received by Local
        gslb site from Remote gslb site then mark the MEP connection DOWN
    type: int
    default: 10
  rtttolerance:
    description:
      - Tolerance, in milliseconds, for newly learned round-trip time (RTT) values.
        If the difference between the old RTT value and the newly computed RTT value
        is less than or equal to the specified tolerance value, the LDNS entry in
        the network metric table is not updated with the new RTT value. Prevents the
        exchange of metrics when variations in RTT values are negligible.
    type: int
    default: 5
  svcstatelearningtime:
    description:
      - Time (in seconds) within which local or child site services remain in learning
        phase. GSLB site will enter the learning phase after reboot, HA failover,
        Cluster GSLB owner node changes or MEP being enabled on local node.  Backup
        parent (if configured) will selectively move the adopted children's GSLB services
        to learning phase when primary parent goes down. While a service is in learning
        period, remote site will not honour the state and stats got through MEP for
        that service. State can be learnt from health monitor if bound explicitly.
    type: int
  undefaction:
    description:
      - 'Action to perform when policy evaluation creates an UNDEF condition. Available
        settings function as follows:'
      - '* NOLBACTION - Does not consider LB action in making LB decision.'
      - '* RESET - Reset the request and notify the user, so that the user can resend
        the request.'
      - '* DROP - Drop the request without sending a response to the user.'
    type: str
    default: '"NOLBACTION"'
  v6ldnsmasklen:
    description:
      - Mask for creating LDNS entries for IPv6 source addresses. The mask is defined
        as the number of leading bits to consider, in the source IP address, when
        creating an LDNS entry.
    type: int
    default: 128
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
