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
module: nsconfig
short_description: Configuration for system config resource.
description: Configuration for system config resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  all:
    description:
      - Use this option to do saveconfig for all partitions
    type: bool
  changedpassword:
    description:
      - Option to list all passwords changed which would not work when downgraded
        to older releases. Takes config file as input, if no input specified, running
        configuration is considered. Command => query ns config -changedpassword /
        query ns config -changedpassword /nsconfig/ns.conf
    type: bool
  cip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - The option to control (enable or disable) the insertion of the actual client
        IP address into the HTTP header request passed from the client to one, some,
        or all servers attached to the system.
      - The passed address can then be accessed through a minor modification to the
        server.
      - l    If cipHeader is specified, it will be used as the client IP header.
      - l    If it is not specified, then the value that has been set by the set ns
        config CLI command will be used as the client IP header.
    type: str
  cipheader:
    description:
      - The text that will be used as the client IP header.
    type: str
  config:
    description:
      - configuration File to be used to find weak passwords, if not specified, running
        config is taken as input.
    type: str
  config1:
    description:
      - Location of the configurations.
    type: str
  config2:
    description:
      - Location of the configurations.
    type: str
  cookieversion:
    choices:
      - 0
      - 1
    description:
      - The version of the cookie inserted by system.
    type: str
  crportrange:
    description:
      - Port range for cache redirection services.
    type: str
  exclusivequotamaxclient:
    description:
      - The percentage of maxClient to be given to PEs
    type: float
    default: 80
  exclusivequotaspillover:
    description:
      - The percentage of max limit to be given to PEs
    type: float
    default: 80
  force:
    description:
      - Configurations will be cleared without prompting for confirmation.
    type: bool
  ftpportrange:
    description:
      - Port range configured for FTP services.
    type: str
  grantquotamaxclient:
    description:
      - The percentage of shared quota to be granted at a time for maxClient
    type: float
    default: 10
  grantquotaspillover:
    description:
      - The percentage of shared quota to be granted at a time for spillover
    type: float
    default: 10
  httpport:
    description:
      - The HTTP ports on the Web server. This allows the system to perform connection
        off-load for any client request that has a destination port matching one of
        these configured ports.
    type: list
  ifnum:
    description:
      - Interfaces of the appliances that must be bound to the NSVLAN.
    type: list
    elements: str
  ignoredevicespecific:
    description:
      - Suppress device specific differences.
    type: bool
  ipaddress:
    description:
      - IP address of the Citrix ADC. Commonly referred to as NSIP address. This parameter
        is mandatory to bring up the appliance.
    type: str
  level:
    choices:
      - basic
      - extended
      - full
    description:
      - Types of configurations to be cleared.
      - '* C(basic): Clears all configurations except the following:'
      - '  - NSIP, default route (gateway), static routes, MIPs, and SNIPs'
      - '  - Network settings (DG, VLAN, RHI and DNS settings)'
      - '  - Cluster settings'
      - '  - HA node definitions'
      - '  - Feature and mode settings'
      - '  - nsroot password'
      - '* C(extended): Clears the same configurations as the ''C(basic)'' option.
        In addition, it clears the feature and mode settings.'
      - '* C(full): Clears all configurations except NSIP, default route, and interface
        settings.'
      - 'Note: When you clear the configurations through the cluster IP address, by
        specifying the level as ''C(full)'', the cluster is deleted and all cluster
        nodes become standalone appliances. The ''C(basic)'' and ''C(extended)'' levels
        are propagated to the cluster nodes.'
    type: str
  maxconn:
    description:
      - The maximum number of connections that will be made from the system to the
        web server(s) attached to it. The value entered here is applied globally to
        all attached servers.
    type: float
  maxreq:
    description:
      - The maximum number of requests that the system can pass on a particular connection
        between the system and a server attached to it. Setting this value to 0 allows
        an unlimited number of requests to be passed.
    type: float
  netmask:
    description:
      - Netmask corresponding to the IP address. This parameter is mandatory to bring
        up the appliance.
    type: str
  nsvlan:
    description:
      - VLAN (NSVLAN) for the subnet on which the IP address resides.
    type: float
  outtype:
    choices:
      - cli
      - xml
    description:
      - Format to display the difference in configurations.
    type: str
  pmtumin:
    description:
      - The minimum Path MTU.
    type: float
    default: 576
  pmtutimeout:
    description:
      - The timeout value in minutes.
    type: float
    default: 10
  rbaconfig:
    choices:
      - 'YES'
      - 'NO'
    description:
      - RBA configurations and TACACS policies bound to system global will not be
        cleared if RBA is set to C(NO).This option is applicable only for BASIC level
        of clear configuration.Default is C(YES), which will clear rba configurations.
    type: str
    default: 'YES'
  securecookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - enable/disable secure flag for persistence cookie
    type: str
    default: ENABLED
  tagged:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Specifies that the interfaces will be added as 802.1q tagged interfaces. Packets
        sent on these interface on this VLAN will have an additional 4-byte 802.1q
        tag which identifies the VLAN.
      - To use 802.1q tagging, the switch connected to the appliance's interfaces
        must also be configured for tagging.
    type: str
    default: 'YES'
  template:
    description:
      - File that contains the commands to be compared.
    type: bool
  timezone:
    description:
      - Name of the timezone
    type: str
    default: CoordinatedUniversalTime
  weakpassword:
    description:
      - Option to list all weak passwords (not adhering to strong password requirements).
        Takes config file as input, if no input specified, running configuration is
        considered. Command => query ns config -weakpassword  / query ns config -weakpassword
        /nsconfig/ns.conf
    type: bool
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
