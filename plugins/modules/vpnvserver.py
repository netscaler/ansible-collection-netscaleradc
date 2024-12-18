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
module: vpnvserver
short_description: Configuration for VPN virtual server resource.
description: Configuration for VPN virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  accessrestrictedpageredirect:
    type: str
    choices:
      - CDN
      - NS
      - 'OFF'
    description:
      - By default, an access restricted page hosted on secure private access C(CDN)
        is displayed when a restricted app is accessed. The setting can be changed
        to C(NS) to display the access restricted page hosted on the gateway or C(OFF)
        to not display any access restricted page.
  advancedepa:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option tells whether advanced EPA is enabled on this virtual server
  appflowlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Log AppFlow records that contain standard NetFlow or IPFIX information, such
        as time stamps for the beginning and end of a flow, packet count, and byte
        count. Also log records that contain application-level information, such as
        HTTP web addresses, HTTP request methods and response status codes, server
        response time, and latency.
  authentication:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Require authentication for users connecting to Citrix Gateway.
  authnprofile:
    type: str
    description:
      - Authentication Profile entity on virtual server. This entity can be used to
        offload authentication to AAA vserver for multi-factor(nFactor) authentication
  certkeynames:
    type: str
    description:
      - Name of the certificate key that was bound to the corresponding SSL virtual
        server as the Certificate Authority for the device certificate
  cginfrahomepageredirect:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When client requests ShareFile resources and Citrix Gateway detects that the
        user is unauthenticated or the user session has expired, disabling this option
        takes the user to the originally requested ShareFile resource after authentication
        (instead of taking the user to the default VPN home page)
  comment:
    type: str
    description:
      - Any comments associated with the virtual server.
  deploymenttype:
    type: str
    choices:
      - NONE
      - ICA_WEBINTERFACE
      - ICA_STOREFRONT
      - MOBILITY
    description:
      - '0'
  devicecert:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Indicates whether device certificate check as a part of EPA is on or off.
  doublehop:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Use the Citrix Gateway appliance in a double-hop configuration. A double-hop
        deployment provides an extra layer of security for the internal network by
        using three firewalls to divide the DMZ into two stages. Such a deployment
        can have one appliance in the DMZ and one appliance in the secure network.
  downstateflush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Close existing connections when the virtual server is marked DOWN, which means
        the server might have timed out. Disconnecting existing connections frees
        resources and in certain cases speeds recovery of overloaded load balancing
        setups. Enable this setting on servers in which the connections can safely
        be closed when they are marked DOWN.  Do not enable DOWN state flush on servers
        that must complete their transactions.
  dtls:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option starts/stops the turn service on the vserver
  failedlogintimeout:
    type: float
    description:
      - Number of minutes an account will be locked if user exceeds maximum permissible
        attempts
  httpprofilename:
    type: str
    description:
      - Name of the HTTP profile to assign to this virtual server.
  icaonly:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - '- When set to C(ON), it implies Basic mode where the user can log on using
        either Citrix Receiver or a browser and get access to the published apps configured
        at the XenApp/XenDEsktop environment pointed out by the WIHome parameter.
        Users are not allowed to connect using the Citrix Gateway Plug-in and end
        point scans cannot be configured. Number of users that can log in and access
        the apps are not limited by the license in this mode.'
      - ''
      - '- When set to C(OFF), it implies Smart Access mode where the user can log
        on using either Citrix Receiver or a browser or a Citrix Gateway Plug-in.
        The admin can configure end point scans to be run on the client systems and
        then use the results to control access to the published apps. In this mode,
        the client can connect to the gateway in other client modes namely VPN and
        CVPN. Number of users that can log in and access the resources are limited
        by the CCU licenses in this mode.'
  icaproxysessionmigration:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option determines if an existing ICA Proxy session is transferred when
        the user logs on from another device.
  icmpvsrresponse:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - Criterion for responding to PING requests sent to this virtual server. If
        this parameter is set to C(ACTIVE), respond only if the virtual server is
        available. With the C(PASSIVE) setting, respond even if the virtual server
        is not available.
  ipset:
    type: str
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current vpn vserver
  ipv46:
    type: str
    description:
      - IPv4 or IPv6 address of the Citrix Gateway virtual server. Usually a public
        IP address. User devices send connection requests to this IP address.
  l2conn:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition
        to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>)
        that is used to identify a connection. Allows multiple TCP and non-TCP connections
        with the same 4-tuple to coexist on the Citrix ADC.
  linuxepapluginupgrade:
    type: str
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Linux
  listenpolicy:
    type: str
    description:
      - String specifying the listen policy for the Citrix Gateway virtual server.
        Can be either a named expression or an expression. The Citrix Gateway virtual
        server processes only the traffic for which the expression evaluates to true.
  listenpriority:
    type: float
    description:
      - Integer specifying the priority of the listen policy. A higher number specifies
        a lower priority. If a request matches the listen policies of more than one
        virtual server, the virtual server whose listen policy has the highest priority
        (the lowest priority number) accepts the request.
  loginonce:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option enables/disables seamless SSO for this Vserver.
  logoutonsmartcardremoval:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to VPN plugin behavior when smartcard or its reader is removed
  macepapluginupgrade:
    type: str
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Mac
  maxaaausers:
    type: float
    description:
      - Maximum number of concurrent user sessions allowed on this virtual server.
        The actual number of users allowed to log on to this virtual server depends
        on the total number of user licenses.
  maxloginattempts:
    type: float
    description:
      - Maximum number of logon attempts
  name:
    type: str
    description:
      - Name for the Citrix Gateway virtual server. Must begin with an ASCII alphabetic
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Can be changed after the virtual server is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
  netprofile:
    type: str
    description:
      - The name of the network profile.
  newname:
    type: str
    description:
      - New name for the Citrix Gateway virtual server. Must begin with an ASCII alphabetic
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
  pcoipvserverprofilename:
    type: str
    description:
      - Name of the PCoIP vserver profile associated with the vserver.
  port:
    type: int
    description:
      - TCP port on which the virtual server listens.
  quicprofilename:
    type: str
    description:
      - Name of the QUIC profile to assign to this virtual server.
  range:
    type: float
    description:
      - Range of Citrix Gateway virtual server IP addresses. The consecutively numbered
        range of IP addresses begins with the address specified by the IP Address
        parameter.
      - In the configuration utility, select Network VServer to enter a range.
  rdpserverprofilename:
    type: str
    description:
      - Name of the RDP server profile associated with the vserver.
  rhistate:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - A host route is injected according to the setting on the virtual servers.
      - '            * If set to C(PASSIVE) on all the virtual servers that share
        the IP address, the appliance always injects the hostroute.'
      - '            * If set to C(ACTIVE) on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to C(ACTIVE) on some virtual servers and C(PASSIVE)
        on the others, the appliance injects even if one virtual server set to C(ACTIVE)
        is UP.'
  samesite:
    type: str
    choices:
      - None
      - LAX
      - STRICT
    description:
      - SameSite attribute value for Cookies generated in VPN context. This attribute
        value will be appended only for the cookies which are specified in the builtin
        patset ns_cookies_samesite
  secureprivateaccess:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Configure secure private access
  servicetype:
    type: str
    choices:
      - SSL
      - DTLS
      - HTTP_QUIC
    description:
      - Protocol used by the Citrix Gateway virtual server.
  tcpprofilename:
    type: str
    description:
      - Name of the TCP profile to assign to this virtual server.
  userdomains:
    type: str
    description:
      - List of user domains specified as comma seperated value
  vserverfqdn:
    type: str
    description:
      - Fully qualified domain name for a VPN virtual server. This is used during
        StoreFront configuration generation.
  windowsepapluginupgrade:
    type: str
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Win
  vpnvserver_aaapreauthenticationpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_aaapreauthenticationpolicy_binding resource
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
  vpnvserver_analyticsprofile_binding:
    type: dict
    description: Bindings for vpnvserver_analyticsprofile_binding resource
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
  vpnvserver_appcontroller_binding:
    type: dict
    description: Bindings for vpnvserver_appcontroller_binding resource
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
  vpnvserver_appflowpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_appflowpolicy_binding resource
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
  vpnvserver_appfwpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_appfwpolicy_binding resource
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
  vpnvserver_auditnslogpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_auditnslogpolicy_binding resource
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
  vpnvserver_auditsyslogpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_auditsyslogpolicy_binding resource
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
  vpnvserver_authenticationcertpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationcertpolicy_binding resource
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
  vpnvserver_authenticationdfapolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationdfapolicy_binding resource
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
  vpnvserver_authenticationldappolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationldappolicy_binding resource
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
  vpnvserver_authenticationlocalpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationlocalpolicy_binding resource
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
  vpnvserver_authenticationloginschemapolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationloginschemapolicy_binding resource
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
  vpnvserver_authenticationnegotiatepolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationnegotiatepolicy_binding resource
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
  vpnvserver_authenticationoauthidppolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationoauthidppolicy_binding resource
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
  vpnvserver_authenticationpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationpolicy_binding resource
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
  vpnvserver_authenticationradiuspolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationradiuspolicy_binding resource
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
  vpnvserver_authenticationsamlidppolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationsamlidppolicy_binding resource
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
  vpnvserver_authenticationsamlpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationsamlpolicy_binding resource
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
  vpnvserver_authenticationtacacspolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationtacacspolicy_binding resource
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
  vpnvserver_authenticationwebauthpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_authenticationwebauthpolicy_binding resource
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
  vpnvserver_cachepolicy_binding:
    type: dict
    description: Bindings for vpnvserver_cachepolicy_binding resource
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
  vpnvserver_cspolicy_binding:
    type: dict
    description: Bindings for vpnvserver_cspolicy_binding resource
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
  vpnvserver_feopolicy_binding:
    type: dict
    description: Bindings for vpnvserver_feopolicy_binding resource
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
  vpnvserver_icapolicy_binding:
    type: dict
    description: Bindings for vpnvserver_icapolicy_binding resource
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
  vpnvserver_intranetip6_binding:
    type: dict
    description: Bindings for vpnvserver_intranetip6_binding resource
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
  vpnvserver_intranetip_binding:
    type: dict
    description: Bindings for vpnvserver_intranetip_binding resource
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
  vpnvserver_responderpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_responderpolicy_binding resource
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
  vpnvserver_rewritepolicy_binding:
    type: dict
    description: Bindings for vpnvserver_rewritepolicy_binding resource
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
  vpnvserver_secureprivateaccessurl_binding:
    type: dict
    description: Bindings for vpnvserver_secureprivateaccessurl_binding resource
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
  vpnvserver_sharefileserver_binding:
    type: dict
    description: Bindings for vpnvserver_sharefileserver_binding resource
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
  vpnvserver_staserver_binding:
    type: dict
    description: Bindings for vpnvserver_staserver_binding resource
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
  vpnvserver_vpnclientlessaccesspolicy_binding:
    type: dict
    description: Bindings for vpnvserver_vpnclientlessaccesspolicy_binding resource
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
  vpnvserver_vpnepaprofile_binding:
    type: dict
    description: Bindings for vpnvserver_vpnepaprofile_binding resource
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
  vpnvserver_vpneula_binding:
    type: dict
    description: Bindings for vpnvserver_vpneula_binding resource
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
  vpnvserver_vpnintranetapplication_binding:
    type: dict
    description: Bindings for vpnvserver_vpnintranetapplication_binding resource
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
  vpnvserver_vpnnexthopserver_binding:
    type: dict
    description: Bindings for vpnvserver_vpnnexthopserver_binding resource
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
  vpnvserver_vpnportaltheme_binding:
    type: dict
    description: Bindings for vpnvserver_vpnportaltheme_binding resource
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
  vpnvserver_vpnsessionpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_vpnsessionpolicy_binding resource
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
  vpnvserver_vpntrafficpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_vpntrafficpolicy_binding resource
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
  vpnvserver_vpnurl_binding:
    type: dict
    description: Bindings for vpnvserver_vpnurl_binding resource
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
  vpnvserver_vpnurlpolicy_binding:
    type: dict
    description: Bindings for vpnvserver_vpnurlpolicy_binding resource
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
- name: Sample vpnvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure vpnvserver
      delegate_to: localhost
      netscaler.adc.vpnvserver:
        state: present
        name: CitrixAccessCallback
        servicetype: SSL
        ipv46: 10.189.130.19
        port: 443
        downstateflush: DISABLED
        listenpolicy: NONE
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
