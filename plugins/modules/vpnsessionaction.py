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
module: vpnsessionaction
short_description: Configuration for VPN session action resource.
description: Configuration for VPN session action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
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
  advancedclientlessvpnmode:
    type: raw
    choices:
      - ENABLED
      - DISABLED
      - STRICT
    description:
      - Option to enable/disable Advanced ClientlessVpnMode. Additionaly, it can be
        set to C(STRICT) to block Classic ClientlessVpnMode while in AdvancedClientlessMode.
  allowedlogingroups:
    type: raw
    description:
      - Specify groups that have permission to log on to Citrix Gateway. Users who
        do not belong to this group or groups are denied access even if they have
        valid credentials.
  allprotocolproxy:
    type: raw
    description:
      - IP address of the proxy server to use for all protocols supported by Citrix
        Gateway.
  alwaysonprofilename:
    type: raw
    description:
      - Name of the AlwaysON profile associated with the session action. The builtin
        profile named none can be used to explicitly disable AlwaysON for the session
        action.
  authorizationgroup:
    type: raw
    description:
      - Comma-separated list of groups in which the user is placed when none of the
        groups that the user is a part of is configured on Citrix Gateway. The authorization
        policy can be bound to these groups to control access to the resources.
  autoproxyurl:
    type: raw
    description:
      - URL to auto proxy config file
  citrixreceiverhome:
    type: raw
    description:
      - Web address for the Citrix Receiver home page. Configure Citrix Gateway so
        that when users log on to the appliance, the Citrix Gateway Plug-in opens
        a web browser that allows single sign-on to the Citrix Receiver home page.
  clientchoices:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Provide users with multiple logon options. With client choices, users have
        the option of logging on by using the Citrix Gateway Plug-in for Windows,
        Citrix Gateway Plug-in for Java, the Web Interface, or clientless access from
        one location. Depending on how Citrix Gateway is configured, users are presented
        with up to three icons for logon choices. The most common are the Citrix Gateway
        Plug-in for Windows, Web Interface, and clientless access.
  clientcleanupprompt:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Prompt for client-side cache clean-up when a client-initiated session closes.
  clientconfiguration:
    type: raw
    choices:
      - none
      - trace
    description:
      - Allow users to change client Debug logging level in Configuration tab of the
        Citrix Gateway Plug-in for Windows.
  clientdebug:
    type: raw
    choices:
      - debug
      - stats
      - events
      - 'OFF'
    description:
      - 'Set the trace level on Citrix Gateway. Technical support technicians use
        these C(debug) logs for in-depth debugging and troubleshooting purposes. Available
        settings function as follows:'
      - '* DEBUG - Detailed C(debug) messages are collected and written into the specified
        file.'
      - '* STATS - Application audit level error messages and C(debug) statistic counters
        are written into the specified file.'
      - '* EVENTS - Application audit-level error messages are written into the specified
        file.'
      - '* C(OFF) - Only critical C(events) are logged into the Windows Application
        Log.'
  clientidletimeout:
    type: raw
    description:
      - Time, in minutes, after which to time out the user session if Citrix Gateway
        does not detect mouse or keyboard activity.
  clientlessmodeurlencoding:
    type: raw
    choices:
      - TRANSPARENT
      - OPAQUE
      - ENCRYPT
    description:
      - 'When clientless access is enabled, you can choose to encode the addresses
        of internal web applications or to leave the address as clear text. Available
        settings function as follows:'
      - '* C(OPAQUE) - Use standard encoding mechanisms to make the domain and protocol
        part of the resource unclear to users.'
      - '* CLEAR - Do not encode the web address and make it visible to users.'
      - '* C(ENCRYPT) - Allow the domain and protocol to be encrypted using a session
        key. When the web address is encrypted, the URL is different for each user
        session for the same web resource. If users bookmark the encoded web address,
        save it in the web browser and then log off, they cannot connect to the web
        address when they log on and use the bookmark. If users save the encrypted
        bookmark in the Access Interface during their session, the bookmark works
        each time the user logs on.'
  clientlesspersistentcookie:
    type: raw
    choices:
      - ALLOW
      - DENY
      - PROMPT
    description:
      - 'State of persistent cookies in clientless access mode. Persistent cookies
        are required for accessing certain features of SharePoint, such as opening
        and editing Microsoft Word, Excel, and PowerPoint documents hosted on the
        SharePoint server. A persistent cookie remains on the user device and is sent
        with each HTTP request. Citrix Gateway encrypts the persistent cookie before
        sending it to the plug-in on the user device, and refreshes the cookie periodically
        as long as the session exists. The cookie becomes stale if the session ends.
        Available settings function as follows:'
      - '* C(ALLOW) - Enable persistent cookies. Users can open and edit Microsoft
        documents stored in SharePoint.'
      - '* C(DENY) - Disable persistent cookies. Users cannot open and edit Microsoft
        documents stored in SharePoint.'
      - '* C(PROMPT) - Prompt users to allow or deny persistent cookies during the
        session. Persistent cookies are not required for clientless access if users
        do not connect to SharePoint.'
  clientlessvpnmode:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
      - DISABLED
    description:
      - 'Enable clientless access for web, XenApp or XenDesktop, and FileShare resources
        without installing the Citrix Gateway Plug-in. Available settings function
        as follows:'
      - '* C(ON) - Allow only clientless access.'
      - '* C(OFF) - Allow clientless access after users log on with the Citrix Gateway
        Plug-in.'
      - '* C(DISABLED) - Do not allow clientless access.'
  clientoptions:
    type: raw
    choices:
      - none
      - all
      - services
      - filetransfer
      - configuration
    description:
      - Display only the configured menu options when you select the "Configure Citrix
        Gateway" option in the Citrix Gateway Plug-in system tray icon for Windows.
  clientsecurity:
    type: raw
    description:
      - Specify the client security check for the user device to permit a Citrix Gateway
        session. The web address or IP address is not included in the expression for
        the client security check.
  clientsecuritygroup:
    type: raw
    description:
      - The client security group that will be assigned on failure of the client security
        check. Users can in general be organized into Groups. In this case, the Client
        Security Group may have a more restrictive security policy.
  clientsecuritylog:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Set the logging of client security checks.
  clientsecuritymessage:
    type: raw
    description:
      - The client security message that will be displayed on failure of the client
        security check.
  defaultauthorizationaction:
    type: raw
    choices:
      - ALLOW
      - DENY
    description:
      - Specify the network resources that users have access to when they log on to
        the internal network. The default setting for authorization is to deny access
        to all network resources. Citrix recommends using the default global setting
        and then creating authorization policies to define the network resources users
        can access. If you set the default authorization policy to C(DENY), you must
        explicitly authorize access to any network resource, which improves security.
  dnsvservername:
    type: raw
    description:
      - Name of the DNS virtual server for the user session.
  emailhome:
    type: raw
    description:
      - Web address for the web-based email, such as Outlook Web Access.
  epaclienttype:
    type: str
    choices:
      - AGENT
      - PLUGIN
    description:
      - Choose between two types of End point Windows Client
      - a) Application Agent - which always runs in the task bar as a standalone application
        and also has a supporting service which runs permanently when installed
      - b) Activex Control - ActiveX control run by Microsoft Internet Explorer.
  forcecleanup:
    type: raw
    choices:
      - none
      - all
      - cookie
      - addressbar
      - plugin
      - filesystemapplication
      - application
      - applicationdata
      - clientcertificate
      - autocomplete
      - cache
    description:
      - Force C(cache) clean-up when the user closes a session. You can specify C(all),
        C(none), or any combination of the client-side items.
  forcedtimeout:
    type: raw
    description:
      - Force a disconnection from the Citrix Gateway Plug-in with Citrix Gateway
        after a specified number of minutes. If the session closes, the user must
        log on again.
  forcedtimeoutwarning:
    type: raw
    description:
      - Number of minutes to warn a user before the user session is disconnected.
  fqdnspoofedip:
    type: raw
    description:
      - Spoofed IP address range that can be used by client for FQDN based split tunneling
  ftpproxy:
    type: raw
    description:
      - IP address of the proxy server to be used for FTP access for all subsequent
        connections to the internal network.
  gopherproxy:
    type: raw
    description:
      - IP address of the proxy server to be used for GOPHER access for all subsequent
        connections to the internal network.
  homepage:
    type: raw
    description:
      - Web address of the home page that appears when users log on. Otherwise, users
        receive the default home page for Citrix Gateway, which is the Access Interface.
  httpport:
    type: raw
    description:
      - Destination port numbers other than port 80, added as a comma-separated list.
        Traffic to these ports is processed as HTTP traffic, which allows functionality,
        such as HTTP authorization and single sign-on to a web application to work.
  httpproxy:
    type: raw
    description:
      - IP address of the proxy server to be used for HTTP access for all subsequent
        connections to the internal network.
  icaproxy:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable ICA proxy to configure secure Internet access to servers running Citrix
        XenApp or XenDesktop by using Citrix Receiver instead of the Citrix Gateway
        Plug-in.
  iconwithreceiver:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Option to decide whether to show plugin icon along with receiver
  iipdnssuffix:
    type: raw
    description:
      - An intranet IP DNS suffix. When a user logs on to Citrix Gateway and is assigned
        an IP address, a DNS record for the user name and IP address combination is
        added to the Citrix Gateway DNS cache. You can configure a DNS suffix to append
        to the user name when the DNS record is added to the cache. You can reach
        to the host from where the user is logged on by using the user's name, which
        can be easier to remember than an IP address. When the user logs off from
        Citrix Gateway, the record is removed from the DNS cache.
  kcdaccount:
    type: raw
    description:
      - The kcd account details to be used in SSO
  killconnections:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Specify whether the Citrix Gateway Plug-in should disconnect all preexisting
        connections, such as the connections existing before the user logged on to
        Citrix Gateway, and prevent new incoming connections on the Citrix Gateway
        Plug-in for Windows and MAC when the user is connected to Citrix Gateway and
        split tunneling is disabled.
  linuxpluginupgrade:
    type: raw
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Linux
  locallanaccess:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
      - FORCED
    description:
      - Set local LAN access. If split tunneling is C(OFF), and you set local LAN
        access to C(ON), the local client can route traffic to its local interface.
        When the local area network switch is specified, this combination of switches
        is useful. The client can allow local LAN access to devices that commonly
        have non-routable addresses, such as local printers or local file servers.
  loginscript:
    type: raw
    description:
      - Path to the logon script that is run when a session is established. Separate
        multiple scripts by using comma. A "$" in the path signifies that the word
        following the "$" is an environment variable.
  logoutscript:
    type: raw
    description:
      - Path to the logout script. Separate multiple scripts by using comma. A "$"
        in the path signifies that the word following the "$" is an environment variable.
  macpluginupgrade:
    type: raw
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Mac
  name:
    type: raw
    description:
      - Name for the Citrix Gateway profile (action). Must begin with an ASCII alphabetic
        or underscore (_) character, and must consist only of ASCII alphanumeric,
        underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and
        hyphen (-) characters. Cannot be changed after the profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my action" or 'my action').
  netmask:
    type: raw
    description:
      - The netmask for the spoofed ip address
  ntdomain:
    type: raw
    description:
      - Single sign-on domain to use for single sign-on to applications in the internal
        network. This setting can be overwritten by the domain that users specify
        at the time of logon or by the domain that the authentication server returns.
  pcoipprofilename:
    type: raw
    description:
      - Name of the PCOIP profile associated with the session action. The builtin
        profile named none can be used to explicitly disable PCOIP for the session
        action.
  proxy:
    type: raw
    choices:
      - BROWSER
      - NS
      - 'OFF'
    description:
      - 'Set options to apply proxy for accessing the internal resources. Available
        settings function as follows:'
      - '* C(BROWSER) - Proxy settings are configured only in Internet Explorer and
        Firefox browsers.'
      - '* C(NS) - Proxy settings are configured on the Citrix ADC.'
      - '* C(OFF) - Proxy settings are not configured.'
  proxyexception:
    type: raw
    description:
      - Proxy exception string that will be configured in the browser for bypassing
        the previously configured proxies. Allowed only if proxy type is Browser.
  proxylocalbypass:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Bypass proxy server for local addresses option in Internet Explorer and Firefox
        proxy server settings.
  rdpclientprofilename:
    type: raw
    description:
      - Name of the RDP profile associated with the vserver.
  rfc1918:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'As defined in the local area network, allow only the following local area
        network addresses to bypass the VPN tunnel when the local LAN access feature
        is enabled:'
      - '* 10.*.*.*,'
      - '* 172.16.*.*,'
      - '* 192.168.*.*'
  securebrowse:
    type: raw
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow users to connect through Citrix Gateway to network resources from iOS
        and Android mobile devices with Citrix Receiver. Users do not need to establish
        a full VPN tunnel to access resources in the secure network.
  sesstimeout:
    type: raw
    description:
      - Number of minutes after which the session times out.
  sfgatewayauthtype:
    type: raw
    choices:
      - domain
      - RSA
      - domainAndRSA
      - SMS
      - smartCard
      - sfAuth
      - sfAuthAndRSA
    description:
      - The authentication type configured for the Citrix Gateway on StoreFront.
  smartgroup:
    type: raw
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
  socksproxy:
    type: raw
    description:
      - IP address of the proxy server to be used for SOCKS access for all subsequent
        connections to the internal network.
  splitdns:
    type: raw
    choices:
      - LOCAL
      - REMOTE
      - BOTH
    description:
      - Route the DNS requests to the local DNS server configured on the user device,
        or Citrix Gateway (remote), or both.
  splittunnel:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
      - REVERSE
    description:
      - Send, through the tunnel, traffic only for intranet applications that are
        defined in Citrix Gateway. Route all other traffic directly to the Internet.
        The C(OFF) setting routes all traffic through Citrix Gateway. With the C(REVERSE)
        setting, intranet applications define the network traffic that is not intercepted.
        All network traffic directed to internal IP addresses bypasses the VPN tunnel,
        while other traffic goes through Citrix Gateway. Reverse split tunneling can
        be used to log all non-local LAN traffic. For example, if users have a home
        network and are logged on through the Citrix Gateway Plug-in, network traffic
        destined to a printer or another device within the home network is not intercepted.
  spoofiip:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - IP address that the intranet application uses to route the connection through
        the virtual adapter.
  sslproxy:
    type: raw
    description:
      - IP address of the proxy server to be used for SSL access for all subsequent
        connections to the internal network.
  sso:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Set single sign-on (SSO) for the session. When the user accesses a server,
        the user's logon credentials are passed to the server for authentication.
      - "\t    NOTE : This configuration does not honor the following authentication\
        \ types for security reason. BASIC, DIGEST, and NTLM (without Negotiate NTLM2\
        \ Key or Negotiate Sign Flag). Use VPN TrafficAction to configure SSO for\
        \ these authentication types."
  ssocredential:
    type: raw
    choices:
      - PRIMARY
      - SECONDARY
    description:
      - Specify whether to use the primary or secondary authentication credentials
        for single sign-on to the server.
  storefronturl:
    type: raw
    description:
      - Web address for StoreFront to be used in this session for enumeration of resources
        from XenApp or XenDesktop.
  transparentinterception:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow access to network resources by using a single IP address and subnet
        mask or a range of IP addresses. The C(OFF) setting sets the mode to proxy,
        in which you configure destination and source IP addresses and port numbers.
        If you are using the Citrix Gateway Plug-in for Windows, set this parameter
        to C(ON), in which the mode is set to transparent. If you are using the Citrix
        Gateway Plug-in for Java, set this parameter to C(OFF).
  useiip:
    type: raw
    choices:
      - NOSPILLOVER
      - SPILLOVER
      - 'OFF'
    description:
      - 'Define IP address pool options. Available settings function as follows:'
      - '* C(SPILLOVER) - When an address pool is configured and the mapped IP is
        used as an intranet IP address, the mapped IP address is used when an intranet
        IP address cannot be assigned.'
      - '* C(NOSPILLOVER) - When intranet IP addresses are enabled and the mapped
        IP address is not used, the Transfer Login page appears for users who have
        used all available intranet IP addresses.'
      - '* C(OFF) - Address pool is not configured.'
  usemip:
    type: raw
    choices:
      - NS
      - 'OFF'
    description:
      - Enable or disable the use of a unique IP address alias, or a mapped IP address,
        as the client IP address for each client session. Allow Citrix Gateway to
        use the mapped IP address as an intranet IP address when all other IP addresses
        are not available.
      - When IP pooling is configured and the mapped IP is used as an intranet IP
        address, the mapped IP address is used when an intranet IP address cannot
        be assigned.
  useraccounting:
    type: raw
    description:
      - The name of the radiusPolicy to use for RADIUS user accounting info on the
        session.
  wihome:
    type: raw
    description:
      - Web address of the Web Interface server, such as http://<ipAddress>/Citrix/XenApp,
        or Receiver for Web, which enumerates the virtualized resources, such as XenApp,
        XenDesktop, and cloud applications. This web address is used as the home page
        in ICA proxy mode.
      - If Client Choices is ON, you must configure this setting. Because the user
        can choose between FullClient and ICAProxy, the user may see a different home
        page. An Internet web site may appear if the user gets the FullClient option,
        or a Web Interface site if the user gets the ICAProxy option. If the setting
        is not configured, the XenApp option does not appear as a client choice.
  wihomeaddresstype:
    type: str
    choices:
      - IPV4
      - IPV6
    description:
      - Type of the wihome address(C(IPV4)/V6)
  windowsautologon:
    type: raw
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable the Windows Auto Logon for the session. If a VPN session
        is established after this setting is enabled, the user is automatically logged
        on by using Windows credentials after the system is restarted.
  windowsclienttype:
    type: str
    choices:
      - AGENT
      - PLUGIN
    description:
      - Choose between two types of Windows Client\
      - a) Application Agent - which always runs in the task bar as a standalone application
        and also has a supporting service which runs permanently when installed\
      - b) Activex Control - ActiveX control run by Microsoft Internet Explorer.
  windowspluginupgrade:
    type: raw
    choices:
      - Always
      - Essential
      - Never
    description:
      - Option to set plugin upgrade behaviour for Win
  winsip:
    type: raw
    description:
      - WINS server IP address to add to Citrix Gateway for name resolution.
  wiportalmode:
    type: raw
    choices:
      - NORMAL
      - COMPACT
    description:
      - Layout on the Access Interface. The C(COMPACT) value indicates the use of
        small icons.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
