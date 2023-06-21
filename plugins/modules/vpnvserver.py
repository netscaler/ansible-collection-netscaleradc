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
module: vpnvserver
short_description: Configuration for VPN virtual server resource.
description: Configuration for VPN virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  advancedepa:
    description:
      - This option tells whether advanced EPA is enabled on this virtual server
    type: str
    choices:
      - true
      - false
  appflowlog:
    description:
      - Log AppFlow records that contain standard NetFlow or IPFIX information, such
        as time stamps for the beginning and end of a flow, packet count, and byte
        count. Also log records that contain application-level information, such as
        HTTP web addresses, HTTP request methods and response status codes, server
        response time, and latency.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  authentication:
    description:
      - Require authentication for users connecting to Citrix Gateway.
    type: str
    default: true
    choices:
      - true
      - false
  authnprofile:
    description:
      - Authentication Profile entity on virtual server. This entity can be used to
        offload authentication to AAA vserver for multi-factor(nFactor) authentication
    type: str
  certkeynames:
    description:
      - Name of the certificate key that was bound to the corresponding SSL virtual
        server as the Certificate Authority for the device certificate
    type: str
  cginfrahomepageredirect:
    description:
      - When client requests ShareFile resources and Citrix Gateway detects that the
        user is unauthenticated or the user session has expired, disabling this option
        takes the user to the originally requested ShareFile resource after authentication
        (instead of taking the user to the default VPN home page)
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  comment:
    description:
      - Any comments associated with the virtual server.
    type: str
  deploymenttype:
    description:
      - '0'
    type: str
    default: 5
    choices:
      - NONE
      - ICA_WEBINTERFACE
      - ICA_STOREFRONT
      - MOBILITY
  devicecert:
    description:
      - Indicates whether device certificate check as a part of EPA is on or off.
    type: str
    choices:
      - true
      - false
  doublehop:
    description:
      - Use the Citrix Gateway appliance in a double-hop configuration. A double-hop
        deployment provides an extra layer of security for the internal network by
        using three firewalls to divide the DMZ into two stages. Such a deployment
        can have one appliance in the DMZ and one appliance in the secure network.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  downstateflush:
    description:
      - Close existing connections when the virtual server is marked DOWN, which means
        the server might have timed out. Disconnecting existing connections frees
        resources and in certain cases speeds recovery of overloaded load balancing
        setups. Enable this setting on servers in which the connections can safely
        be closed when they are marked DOWN.  Do not enable DOWN state flush on servers
        that must complete their transactions.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  dtls:
    description:
      - This option starts/stops the turn service on the vserver
    type: str
    default: true
    choices:
      - true
      - false
  failedlogintimeout:
    description:
      - Number of minutes an account will be locked if user exceeds maximum permissible
        attempts
    type: int
  httpprofilename:
    description:
      - Name of the HTTP profile to assign to this virtual server.
    type: str
    default: '"nshttp_default_strict_validation"'
  icaonly:
    description:
      - '- When set to ON, it implies Basic mode where the user can log on using either
        Citrix Receiver or a browser and get access to the published apps configured
        at the XenApp/XenDEsktop environment pointed out by the WIHome parameter.
        Users are not allowed to connect using the Citrix Gateway Plug-in and end
        point scans cannot be configured. Number of users that can log in and access
        the apps are not limited by the license in this mode.'
      - ' '
      - '- When set to OFF, it implies Smart Access mode where the user can log on
        using either Citrix Receiver or a browser or a Citrix Gateway Plug-in. The
        admin can configure end point scans to be run on the client systems and then
        use the results to control access to the published apps. In this mode, the
        client can connect to the gateway in other client modes namely VPN and CVPN.
        Number of users that can log in and access the resources are limited by the
        CCU licenses in this mode.'
    type: str
    choices:
      - true
      - false
  icaproxysessionmigration:
    description:
      - This option determines if an existing ICA Proxy session is transferred when
        the user logs on from another device.
    type: str
    choices:
      - true
      - false
  icmpvsrresponse:
    description:
      - Criterion for responding to PING requests sent to this virtual server. If
        this parameter is set to ACTIVE, respond only if the virtual server is available.
        With the PASSIVE setting, respond even if the virtual server is not available.
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  ipset:
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current vpn vserver
    type: str
  ipv46:
    description:
      - IPv4 or IPv6 address of the Citrix Gateway virtual server. Usually a public
        IP address. User devices send connection requests to this IP address.
    type: str
  l2conn:
    description:
      - Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition
        to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>)
        that is used to identify a connection. Allows multiple TCP and non-TCP connections
        with the same 4-tuple to coexist on the Citrix ADC.
    type: str
    choices:
      - true
      - false
  linuxepapluginupgrade:
    description:
      - Option to set plugin upgrade behaviour for Linux
    type: str
    choices:
      - Always
      - Essential
      - Never
  listenpolicy:
    description:
      - String specifying the listen policy for the Citrix Gateway virtual server.
        Can be either a named expression or an expression. The Citrix Gateway virtual
        server processes only the traffic for which the expression evaluates to true.
    type: str
    default: '"none"'
  listenpriority:
    description:
      - Integer specifying the priority of the listen policy. A higher number specifies
        a lower priority. If a request matches the listen policies of more than one
        virtual server, the virtual server whose listen policy has the highest priority
        (the lowest priority number) accepts the request.
    type: int
    default: 101
  loginonce:
    description:
      - This option enables/disables seamless SSO for this Vserver.
    type: str
    choices:
      - true
      - false
  logoutonsmartcardremoval:
    description:
      - Option to VPN plugin behavior when smartcard or its reader is removed
    type: str
    choices:
      - true
      - false
  macepapluginupgrade:
    description:
      - Option to set plugin upgrade behaviour for Mac
    type: str
    choices:
      - Always
      - Essential
      - Never
  maxaaausers:
    description:
      - Maximum number of concurrent user sessions allowed on this virtual server.
        The actual number of users allowed to log on to this virtual server depends
        on the total number of user licenses.
    type: int
  maxloginattempts:
    description:
      - Maximum number of logon attempts
    type: int
  name:
    description:
      - Name for the Citrix Gateway virtual server. Must begin with an ASCII alphabetic
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Can be changed after the virtual server is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
    type: str
  netprofile:
    description:
      - The name of the network profile.
    type: str
  newname:
    description:
      - 'New name for the Citrix Gateway virtual server. Must begin with an ASCII
        alphabetic or underscore (_) character, and must contain only ASCII alphanumeric,
        underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and
        hyphen (-) characters. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
    type: str
  pcoipvserverprofilename:
    description:
      - Name of the PCoIP vserver profile associated with the vserver.
    type: str
  port:
    description:
      - TCP port on which the virtual server listens.
    type: int
  range:
    description:
      - 'Range of Citrix Gateway virtual server IP addresses. The consecutively numbered
        range of IP addresses begins with the address specified by the IP Address
        parameter. '
      - In the configuration utility, select Network VServer to enter a range.
    type: int
    default: 1
  rdpserverprofilename:
    description:
      - Name of the RDP server profile associated with the vserver.
    type: str
  rhistate:
    description:
      - A host route is injected according to the setting on the virtual servers.
      - '            * If set to PASSIVE on all the virtual servers that share the
        IP address, the appliance always injects the hostroute.'
      - '            * If set to ACTIVE on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to ACTIVE on some virtual servers and PASSIVE on the
        others, the appliance injects even if one virtual server set to ACTIVE is
        UP.'
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  samesite:
    description:
      - SameSite attribute value for Cookies generated in VPN context. This attribute
        value will be appended only for the cookies which are specified in the builtin
        patset ns_cookies_samesite
    type: str
    choices:
      - None
      - LAX
      - STRICT
  servicetype:
    description:
      - Protocol used by the Citrix Gateway virtual server.
    type: str
    default: SSL
    choices:
      - SSL
      - DTLS
  state:
    description:
      - State of the virtual server. If the virtual server is disabled, requests are
        not processed.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tcpprofilename:
    description:
      - Name of the TCP profile to assign to this virtual server.
    type: str
  userdomains:
    description:
      - List of user domains specified as comma seperated value
    type: str
  vserverfqdn:
    description:
      - Fully qualified domain name for a VPN virtual server. This is used during
        StoreFront configuration generation.
    type: str
  windowsepapluginupgrade:
    description:
      - Option to set plugin upgrade behaviour for Win
    type: str
    choices:
      - Always
      - Essential
      - Never
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
