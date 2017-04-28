#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
module: netscaler_lb_monitor
short_description: Manage load balancing monitors
description:
    - Manage load balancing monitors
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance

version_added: 2.2.3

options:
    monitorname:
        description:
            - >
                Name for the monitor. Must begin with an ASCII alphanumeric or underscore (_) character,
                and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:),
                at (@), equals (=), and hyphen (-) characters.
            - Minimum length = 1

    type:
        choices:
            - 'PING'
            - 'TCP'
            - 'HTTP'
            - 'TCP-ECV'
            - 'HTTP-ECV'
            - 'UDP-ECV'
            - 'DNS'
            - 'FTP'
            - 'LDNS-PING'
            - 'LDNS-TCP'
            - 'LDNS-DNS'
            - 'RADIUS'
            - 'USER'
            - 'HTTP-INLINE'
            - 'SIP-UDP'
            - 'SIP-TCP'
            - 'LOAD'
            - 'FTP-EXTENDED'
            - 'SMTP'
            - 'SNMP'
            - 'NNTP'
            - 'MYSQL'
            - 'MYSQL-ECV'
            - 'MSSQL-ECV'
            - 'ORACLE-ECV'
            - 'LDAP'
            - 'POP3'
            - 'CITRIX-XML-SERVICE'
            - 'CITRIX-WEB-INTERFACE'
            - 'DNS-TCP'
            - 'RTSP'
            - 'ARP'
            - 'CITRIX-AG'
            - 'CITRIX-AAC-LOGINPAGE'
            - 'CITRIX-AAC-LAS'
            - 'CITRIX-XD-DDC'
            - 'ND6'
            - 'CITRIX-WI-EXTENDED'
            - 'DIAMETER'
            - 'RADIUS_ACCOUNTING'
            - 'STOREFRONT'
            - 'APPC'
            - 'SMPP'
            - 'CITRIX-XNC-ECV'
            - 'CITRIX-XDM'
            - 'CITRIX-STA-SERVICE'
            - 'CITRIX-STA-SERVICE-NHOP'
        description:
            - Type of monitor that you want to create.

    action:
        choices: ['NONE', 'LOG', 'DOWN']
        description:
            - >
                Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE)
                indicates that the service is down. A service monitored by an inline monitor is considered DOWN
                if the response code is not one of the codes that have been specified for the Response Code parameter.
            - Available settings function as follows.
            - >
                NONE - Do not take any action. However, the show service command and the show
                lb monitor command indicate the total number of responses that were checked and
                the number of consecutive error responses received after the last successful probe.
            -  LOG - Log the event in NSLOG or SYSLOG.
            -  >
                DOWN - Mark the service as being down, and then do not direct any traffic to the service
                until the configured down time has expired. Persistent connections to the service are
                terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.
            - Default value = DOWN

    respcode:
        description:
            - >
                Response codes for which to mark the service as UP.
                For any other response code, the action performed depends on the monitor type.
                HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE
                monitors perform the action indicated by the Action parameter.

    httprequest:
        description:
            - HTTP request to send to the server (for example, "HEAD /file.html").

    rtsprequest:
        description:
            - RTSP request to send to the server (for example, "OPTIONS *").

    customheaders:
        description:
            - Custom header string to include in the monitoring probes.

    maxforwards:
        description:
            - Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.
            - Default value = 1
            - Minimum value = 0
            - Maximum value = 255

    sipmethod:
        choices: ['OPTIONS', 'INVITE', 'REGISTER']
        description:
            - SIP method to use for the query. Applicable only to monitors of type SIP-UDP.

    sipuri:
        description:
            - "SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP."
            - Minimum length = 1

    sipreguri:
        description:
            - SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.
            - Minimum length = 1

    send:
        description:
            - String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.

    recv:
        description:
            - String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.

    query:
        description:
            - Domain name to resolve as part of monitoring the DNS service (for example, example.com).

    querytype:
        choices: ['Address', 'Zone', 'AAAA']
        description:
            - >
                Type of DNS record for which to send monitoring queries.
                Set to Address for querying A records, AAAA for querying AAAA records,
                and Zone for querying the SOA record.

    scriptname:
        description:
            - Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.
            - Minimum length = 1

    scriptargs:
        description:
            - String of arguments for the script. The string is copied verbatim into the request.

    dispatcherip:
        description:
            - IP address of the dispatcher to which to send the probe.

    dispatcherport:
        description:
            - Port number on which the dispatcher listens for the monitoring probe.

    username:
        description:
            - >
                User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED,
                MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED,
                CITRIX-XNC or CITRIX-XDM server.
            - Minimum length = 1

    password:
        description:
            - >
                Password that is required for logging on to the RADIUS, NNTP, FTP,
                FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC,
                CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server.
                Used in conjunction with the user name specified for the User Name parameter.
            - Minimum length = 1

    secondarypassword:
        description:
            - Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.

    logonpointname:
        description:
            - >
                Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software.
                Required if you want to monitor the associated login page or Logon Agent.
                Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.

    lasversion:
        description:
            - Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.

    radkey:
        description:
            - >
                Authentication key (shared secret text string) for RADIUS clients and servers to exchange.
                Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
            - Minimum length = 1

    radnasid:
        description:
            - NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.
            - Minimum length = 1

    radnasip:
        description:
            - >
                Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server.
                Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.

    radaccounttype:
        description:
            - Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.
            - Default value = 1
            - Minimum value = 0
            - Maximum value = 15

    radframedip:
        description:
            - Source ip with which the packet will go out . Applicable to monitors of type RADIUS_ACCOUNTING.

    radapn:
        description:
            - Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.
            - Minimum length = 1

    radmsisdn:
        description:
            - Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.
            - Minimum length = 1

    radaccountsession:
        description:
            - Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.
            - Minimum length = 1

    lrtm:
        choices: ['ENABLED', 'DISABLED']
        description:
            - >
                Calculate the least response times for bound services.
                If this parameter is not enabled, the appliance does not learn the response times of the bound services.
                Also used for LRTM load balancing.
            - Possible values = ENABLED, DISABLED

    deviation:
        description:
            - >
                Time value added to the learned average response time in dynamic response time monitoring (DRTM).
                When a deviation is specified, the appliance learns the average response time of bound services
                and adds the deviation to the average. The final value is then continually adjusted to accommodate
                response time variations over time. Specified in milliseconds, seconds, or minutes.
            - Minimum value = 0
            - Maximum value = 20939

    units1:
        choices: ['SEC', 'MSEC', 'MIN']
        description:
            - Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.
            - Default value = SEC

    interval:
        description:
            - Time interval between two successive probes. Must be greater than the value of Response Time-out.
            - Default value = 5
            - Minimum value = 1
            - Maximum value = 20940

    units3:
        choices: ['SEC', 'MSEC', 'MIN']
        description:
            - monitor interval units.
            - Default value = SEC

    resptimeout:
        description:
            - >
                Amount of time for which the appliance must wait before it marks a probe as FAILED.
                Must be less than the value specified for the Interval parameter.
            - >
                Note. For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply.
                For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.
            - Default value = 2
            - Minimum value = 1
            - Maximum value = 20939

    units4:
        choices: ['SEC', 'MSEC', 'MIN']
        description:
            - monitor response timeout units.
            - Default value = SEC
            - Possible values = SEC, MSEC, MIN

    resptimeoutthresh:
        description:
            - >
                Response time threshold, specified as a percentage of the Response Time-out parameter.
                If the response to a monitor probe has not arrived when the threshold is reached,
                the appliance generates an SNMP trap called monRespTimeoutAboveThresh.
                After the response time returns to a value below the threshold, the appliance
                generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated,
                the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.
            - Minimum value = 0
            - Maximum value = 100

    retries:
        description:
            - Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.
            - Default value = 3
            - Minimum value = 1
            - Maximum value = 127

    failureretries:
        description:
            - >
                Number of retries that must fail, out of the number specified for the Retries parameter,
                for a service to be marked as DOWN. For example, if the Retries parameter is set to 10
                and the Failure Retries parameter is set to 6, out of the ten probes sent, at least
                six probes must fail if the service is to be marked as DOWN.
                The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.
            - Minimum value = 0
            - Maximum value = 32

    alertretries:
        description:
            - Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.
            - Minimum value = 0
            - Maximum value = 32

    successretries:
        description:
            - Number of consecutive successful probes required to transition a service's state from DOWN to UP.
            - Default value = 1
            - Minimum value = 1
            - Maximum value = 32

    downtime:
        description:
            - Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.
            - Default value = 30
            - Minimum value = 1
            - Maximum value = 20939

    units2:
        choices: ['SEC', 'MSEC', 'MIN']
        description:
            - Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.
            - Default value = SEC
            - Possible values = SEC, MSEC, MIN

    destip:
        description:
            - >
                IP address of the service to which to send probes.
                If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.

    destport:
        description:
            - >
                TCP or UDP port to which to send the probe.
                If the parameter is set to 0, the port number of the service to which the monitor
                is bound is considered the destination port. For a monitor of type USER, however,
                the destination port is the port number that is included in the HTTP request sent to the dispatcher.
                Does not apply to monitors of type PING.

    state:
        choices: ['ENABLED', 'DISABLED']
        description:
            - >
                State of the monitor. The DISABLED setting disables not only the monitor being configured,
                but all monitors of the same type, until the parameter is set to ENABLED.
                If the monitor is bound to a service, the state of the monitor is not taken into account
                when the state of the service is determined.
            - Default value = ENABLED

    reverse:
        choices: ['YES', 'NO']
        description:
            - Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.
            - Default value = NO
            - Possible values = YES, NO

    transparent:
        choices: ['YES', 'NO']
        description:
            - >
                The monitor is bound to a transparent device such as a firewall or router.
                The state of a transparent device depends on the responsiveness of the services behind it.
                If a transparent device is being monitored, a destination IP address must be specified.
                The probe is sent to the specified IP address by using the MAC address of the transparent device.
            - Default value = NO
            - Possible values = YES, NO

    iptunnel:
        choices: ['YES', 'NO']
        description:
            - Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.
            - Default value = NO

    tos:
        choices: ['YES', 'NO']
        description:
            - Probe the service by encoding the destination IP address in the IP TOS (6) bits.

    tosid:
        description:
            - The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.
            - Minimum value = 1
            - Maximum value = 63

    secure:
        choices: ['YES', 'NO']
        description:
            - >
                Use a secure SSL connection when monitoring a service.
                Applicable only to TCP based monitors.
                The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.
            - Default value = NO

    validatecred:
        choices: ['YES', 'NO']
        description:
            - Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.
            - Default value = NO

    domain:
        description:
            - >
                Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or
                Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED
                monitors for logging on to the DDC servers and Web Interface servers, respectively.

    ipaddress:
        description:
            - Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.
            - Minimum length = 1

    group:
        description:
            - >
                Name of a newsgroup available on the NNTP service that is to be monitored.
                The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response.
                If the newsgroup is found on the server, the service is marked as UP.
                If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.
            - Minimum length = 1

    filename:
        description:
            - >
                Name of a file on the FTP server.
                The appliance monitors the FTP service by periodically checking the existence of the file on the server.
                Applicable to FTP-EXTENDED monitors.
            - Minimum length = 1

    basedn:
        description:
            - >
                The base distinguished name of the LDAP service, from where the LDAP server
                can begin the search for the attributes in the monitoring query.
                Required for LDAP service monitoring.
            - Minimum length = 1

    binddn:
        description:
            - The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.
            - Minimum length = 1

    filter:
        description:
            - Filter criteria for the LDAP query. Optional.
            - Minimum length = 1

    attribute:
        description:
            - >
                Attribute to evaluate when the LDAP server responds to the query.
                Success or failure of the monitoring probe depends on whether the attribute exists in the response.
                Optional.
            - Minimum length = 1

    database:
        description:
            - Name of the database to connect to during authentication.
            - Minimum length = 1

    oraclesid:
        description:
            - Name of the service identifier that is used to connect to the Oracle database during authentication.
            - Minimum length = 1

    sqlquery:
        description:
            - SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.
            - Minimum length = 1

    evalrule:
        description:
            - >
                Default syntax expression that evaluates the database server's response to
                a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result.
                The result determines the state of the server. If the expression returns TRUE, the probe succeeds.
            - >
                For example, if you want the appliance to evaluate the error message to
                determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").

    mssqlprotocolversion:
        choices: ['70', '2000', '2000SP1', '2005', '2008', '2008R2', '2012', '2014']
        description:
            - Version of MSSQL server that is to be monitored.
            - Default value = 70
            - Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014

    Snmpoid:
        description:
            - SNMP OID for SNMP monitors.
            - Minimum length = 1

    snmpcommunity:
        description:
            - Community name for SNMP monitors.
            - Minimum length = 1

    snmpthreshold:
        description:
            - Threshold for SNMP monitors.
            - Minimum length = 1

    snmpversion:
        choices: ['V1', 'V2']
        description:
            - SNMP version to be used for SNMP monitors.

    application:
        description:
            - Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.
            - Minimum length = 1

    sitepath:
        description:
            - >
                URL of the logon page.
                For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path,
                terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.
            - Minimum length = 1

    storename:
        description:
            - >
                Store Name.
                For monitors of type STOREFRONT, STORENAME is an optional argument
                defining storefront service store name. Applicable to STOREFRONT monitors.
            - Minimum length = 1

    storefrontacctservice:
        choices: ['YES', 'NO']
        description:
            - >
                Enable/Disable probing for Account Service.
                Applicable only to Store Front monitors.
                For multi-tenancy configuration users my skip account service.
            - Default value = YES

    netprofile:
        description:
            - Name of the network profile.
            - Minimum length = 1
            - Maximum length = 127

    originhost:
        description:
            - Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
            - Minimum length = 1

    originrealm:
        description:
            - Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
            - Minimum length = 1

    hostipaddress:
        description:
            - >
                Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to
                use for monitoring Diameter servers. If Host-IP-Address is not specified,
                the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address
                from which the CER request (the monitoring probe) is sent.
            - Minimum length = 1

    vendorid:
        description:
            - Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

    productname:
        description:
            - Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
            - Minimum length = 1

    firmwarerevision:
        description:
            - Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

    authapplicationid:
        description:
            - >
                List of Auth-Application-Id attribute value pairs (AVPs) for
                the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
                A maximum of eight of these AVPs are supported in a monitoring CER message.
            - Minimum value = 0
            - Maximum value = 4294967295

    acctapplicationid:
        description:
            - >
                List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message
                to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.
            - Minimum value = 0
            - Maximum value = 4294967295

    inbandsecurityid:
        choices: ['NO_INBAND_SECURITY', 'TLS']
        description:
            - Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.

    supportedvendorids:
        description:
            - >
                List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER)
                message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.
            - Minimum value = 1
            - Maximum value = 4294967295

    vendorspecificvendorid:
        description:
            - >
                Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message.
                To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id,
                use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively.
                Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.
            - Minimum value = 1

    vendorspecificauthapplicationids:
        description:
            - >
                List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER)
                message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.
                The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP
                in the CER monitoring message.
            - Minimum value = 0
            - Maximum value = 4294967295

    vendorspecificacctapplicationids:
        description:
            - >
                List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers.
                A maximum of eight of these AVPs are supported in a monitoring message.
                The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP
                in the CER monitoring message.
            - Minimum value = 0
            - Maximum value = 4294967295

    storedb:
        choices: ['ENABLED', 'DISABLED']
        description:
            - >
                Store the database list populated with the responses to monitor probes.
                Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV monitor is configured.
            - Default value = DISABLED

    storefrontcheckbackendservices:
        choices: ['YES', 'NO']
        description:
            - >
                This option will enable monitoring of services running on storefront server.
                Storefront services are monitored by probing to a Windows service that runs on the Storefront server
                and exposes details of which storefront services are running.
            - Default value = NO

    trofscode:
        description:
            - Code expected when the server is under maintenance.

    trofsstring:
        description:
            - String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.

extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
- name: Set lb monitor
  local_action:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
    ssl_cert_validation: no


    module: netscaler_lb_monitor
    operation: present

    monitorname: monitor_1
    type: HTTP-INLINE
    action: DOWN
    respcode: ['400']
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"

diff:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: failure
    type: dict
    sample: { 'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2' }
'''

import copy
from ansible.module_utils.basic import AnsibleModule


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled

    try:
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonbindings_service_binding import lbmonbindings_service_binding
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor_service_binding import lbmonitor_service_binding
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(

        monitorname=dict(type='str'),

        type=dict(
            type='str',
            choices=[
                'PING',
                'TCP',
                'HTTP',
                'TCP-ECV',
                'HTTP-ECV',
                'UDP-ECV',
                'DNS',
                'FTP',
                'LDNS-PING',
                'LDNS-TCP',
                'LDNS-DNS',
                'RADIUS',
                'USER',
                'HTTP-INLINE',
                'SIP-UDP',
                'SIP-TCP',
                'LOAD',
                'FTP-EXTENDED',
                'SMTP',
                'SNMP',
                'NNTP',
                'MYSQL',
                'MYSQL-ECV',
                'MSSQL-ECV',
                'ORACLE-ECV',
                'LDAP',
                'POP3',
                'CITRIX-XML-SERVICE',
                'CITRIX-WEB-INTERFACE',
                'DNS-TCP',
                'RTSP',
                'ARP',
                'CITRIX-AG',
                'CITRIX-AAC-LOGINPAGE',
                'CITRIX-AAC-LAS',
                'CITRIX-XD-DDC',
                'ND6',
                'CITRIX-WI-EXTENDED',
                'DIAMETER',
                'RADIUS_ACCOUNTING',
                'STOREFRONT',
                'APPC',
                'SMPP',
                'CITRIX-XNC-ECV',
                'CITRIX-XDM',
                'CITRIX-STA-SERVICE',
                'CITRIX-STA-SERVICE-NHOP'
            ]
        ),

        action=dict(
            type='str',
            choices=[u'NONE', u'LOG', u'DOWN']
        ),

        respcode=dict(type='list'),
        httprequest=dict(type='str',),
        rtsprequest=dict(type='str'),
        customheaders=dict(type='str'),
        maxforwards=dict(type='float'),
        sipmethod=dict(
            type='str',
            choices=[u'OPTIONS', u'INVITE', u'REGISTER']
        ),
        sipuri=dict(type='str'),
        sipreguri=dict(type='str'),
        send=dict(type='str'),
        recv=dict(type='str'),
        query=dict(type='str'),
        querytype=dict(
            type='str',
            choices=[u'Address', u'Zone', u'AAAA']
        ),
        scriptname=dict(type='str'),
        scriptargs=dict(type='str'),
        dispatcherip=dict(type='str'),
        dispatcherport=dict(type='int'),
        username=dict(type='str'),
        password=dict(type='str'),
        secondarypassword=dict(type='str'),
        logonpointname=dict(type='str'),
        lasversion=dict(type='str'),
        radkey=dict(type='str'),
        radnasid=dict(type='str'),
        radnasip=dict(type='str'),
        radaccounttype=dict(type='float'),
        radframedip=dict(type='str'),
        radapn=dict(type='str'),
        radmsisdn=dict(type='str'),
        radaccountsession=dict(type='str'),
        lrtm=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        deviation=dict(type='float'),
        units1=dict(
            type='str',
            choices=[u'SEC', u'MSEC', u'MIN']
        ),
        interval=dict(type='int'),
        units3=dict(
            type='str',
            choices=[u'SEC', u'MSEC', u'MIN']
        ),
        resptimeout=dict(type='int'),
        units4=dict(
            type='str',
            choices=[u'SEC', u'MSEC', u'MIN']
        ),
        resptimeoutthresh=dict(type='float'),
        retries=dict(type='int'),
        failureretries=dict(type='int'),
        alertretries=dict(type='int'),
        successretries=dict(type='int'),
        downtime=dict(type='int'),
        units2=dict(
            type='str',
            choices=[u'SEC', u'MSEC', u'MIN']
        ),
        destip=dict(type='str'),
        destport=dict(type='int'),
        state=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        reverse=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        transparent=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        iptunnel=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        tos=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        tosid=dict(type='float'),
        secure=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        validatecred=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        domain=dict(type='str'),
        ipaddress=dict(type='list'),
        group=dict(type='str'),
        filename=dict(type='str'),
        basedn=dict(type='str'),
        binddn=dict(type='str'),
        filter=dict(type='str'),
        attribute=dict(type='str'),
        database=dict(type='str'),
        oraclesid=dict(type='str'),
        sqlquery=dict(type='str'),
        evalrule=dict(type='str'),
        mssqlprotocolversion=dict(
            type='str',
            choices=[u'70', u'2000', u'2000SP1', u'2005', u'2008', u'2008R2', u'2012', u'2014']
        ),
        Snmpoid=dict(type='str'),
        snmpcommunity=dict(type='str'),
        snmpthreshold=dict(type='str'),
        snmpversion=dict(
            type='str',
            choices=[u'V1', u'V2']
        ),
        application=dict(type='str'),
        sitepath=dict(type='str'),
        storename=dict(type='str'),
        storefrontacctservice=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        netprofile=dict(type='str'),
        originhost=dict(type='str'),
        originrealm=dict(type='str'),
        hostipaddress=dict(type='str'),
        vendorid=dict(type='float'),
        productname=dict(type='str'),
        firmwarerevision=dict(type='float'),
        authapplicationid=dict(type='list'),
        acctapplicationid=dict(type='list'),
        inbandsecurityid=dict(
            type='str',
            choices=[u'NO_INBAND_SECURITY', u'TLS']
        ),
        supportedvendorids=dict(type='list'),
        vendorspecificvendorid=dict(type='float'),
        vendorspecificauthapplicationids=dict(type='list'),
        vendorspecificacctapplicationids=dict(type='list'),
        storedb=dict(
            type='str',
            choices=[u'ENABLED', u'DISABLED']
        ),
        storefrontcheckbackendservices=dict(
            type='str',
            choices=[u'YES', u'NO']
        ),
        trofscode=dict(type='float'),
        trofsstring=dict(type='str'),
    )

    hand_inserted_arguments = dict(
        servicegroupbindings=dict(type='list'),
        servicebindings=dict(type='list'),
    )

    argument_spec = dict()
    argument_spec.update(module_specific_arguments)
    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk', **module_result)

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    # Instantiate lb monitor object
    readwrite_attrs = [
        'monitorname',
        'type',
        'action',
        'respcode',
        'httprequest',
        'rtsprequest',
        'customheaders',
        'maxforwards',
        'sipmethod',
        'sipuri',
        'sipreguri',
        'send',
        'recv',
        'query',
        'querytype',
        'scriptname',
        'scriptargs',
        'dispatcherip',
        'dispatcherport',
        'username',
        'password',
        'secondarypassword',
        'logonpointname',
        'lasversion',
        'radkey',
        'radnasid',
        'radnasip',
        'radaccounttype',
        'radframedip',
        'radapn',
        'radmsisdn',
        'radaccountsession',
        'lrtm',
        'deviation',
        'units1',
        'interval',
        'units3',
        'resptimeout',
        'units4',
        'resptimeoutthresh',
        'retries',
        'failureretries',
        'alertretries',
        'successretries',
        'downtime',
        'units2',
        'destip',
        'destport',
        'state',
        'reverse',
        'transparent',
        'iptunnel',
        'tos',
        'tosid',
        'secure',
        'validatecred',
        'domain',
        'ipaddress',
        'group',
        'filename',
        'basedn',
        'binddn',
        'filter',
        'attribute',
        'database',
        'oraclesid',
        'sqlquery',
        'evalrule',
        'mssqlprotocolversion',
        'Snmpoid',
        'snmpcommunity',
        'snmpthreshold',
        'snmpversion',
        'application',
        'sitepath',
        'storename',
        'storefrontacctservice',
        'netprofile',
        'originhost',
        'originrealm',
        'hostipaddress',
        'vendorid',
        'productname',
        'firmwarerevision',
        'authapplicationid',
        'acctapplicationid',
        'inbandsecurityid',
        'supportedvendorids',
        'vendorspecificvendorid',
        'vendorspecificauthapplicationids',
        'vendorspecificacctapplicationids',
        'storedb',
        'storefrontcheckbackendservices',
        'trofscode',
        'trofsstring',
    ]

    readonly_attrs = [
        'lrtmconf',
        'lrtmconfstr',
        'dynamicresponsetimeout',
        'dynamicinterval',
        'multimetrictable',
        'dup_state',
        'dup_weight',
        'weight',
    ]

    lbmonitor_proxy = ConfigProxy(
        actual=lbmonitor(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
        json_encodes=['evalrule'],
    )

    def lbmonitor_exists():
        log('Entering lbmonitor_exists')
        if lbmonitor.count_filtered(client, 'monitorname:%s' % module.params['monitorname']) > 0:
            return True
        else:
            return False

    def lbmonitor_identical():
        log('Entering lbmonitor_identical')

        count = lbmonitor.count_filtered(client, 'monitorname:%s' % module.params['monitorname'])
        if count == 0:
            return False

        lbmonitor_list = lbmonitor.get_filtered(client, 'monitorname:%s' % module.params['monitorname'])
        diff_dict = lbmonitor_proxy.diff_object(lbmonitor_list[0])

        # Skipping hashed fields since the cannot be compared directly
        # TODO emulate the hash function for effective equality comparison
        hashed_fields = [
            'password',
            'secondarypassword',
            'radkey',
        ]
        for key in hashed_fields:
            if key in diff_dict:
                del diff_dict[key]

        if diff_dict == {}:
            return True
        else:
            return False

    def get_configured_service_bindings():

        readwrite_attrs = [
            'weight',
            'name',
            'passive',
            'monstate',
        ]
        readonly_attrs = []

        configured_bindings = {}
        if 'servicebindings' in module.params and module.params['servicebindings'] is not None:
            for binding in module.params['servicebindings']:
                attribute_values_dict = copy.deepcopy(binding)
                attribute_values_dict['monitor_name'] = module.params['monitorname']
                key = binding['name'].strip()
                configured_bindings[key] = ConfigProxy(
                    actual=lbmonbindings_service_binding(),
                    client=client,
                    attribute_values_dict=attribute_values_dict,
                    readwrite_attrs=readwrite_attrs,
                    readonly_attrs=readonly_attrs,
                )
        return configured_bindings

    def get_actual_service_bindings():
        log('entering get_actual_service_bindings')
        if lbmonbindings_service_binding.count(client, module.params['monitorname']) == 0:
            return {}
        bindigs_list = lbmonbindings_service_binding.get(client, module.params['monitorname'])
        bindings = {}
        for item in bindigs_list:
            key = item.servicename
            log('bound service name %s' % key)
            bindings[key] = item

        return bindings

    def service_bindings_identical():
        log('service_bindings_identical')

        # Compare servicegroup keysets
        configured_servicegroup_bindings = get_configured_servicegroup_bindings()
        servicegroup_bindings = get_actual_servicegroup_bindings()
        configured_keyset = set(configured_servicegroup_bindings.keys())
        service_keyset = set(servicegroup_bindings.keys())
        log('len %s' % len(configured_keyset ^ service_keyset))
        if len(configured_keyset ^ service_keyset) > 0:
            return False

        # Compare servicegroup item to item
        for key in configured_servicegroup_bindings.keys():
            conf = configured_servicegroup_bindings[key]
            serv = servicegroup_bindings[key]
            log('sg diff %s' % conf.diff_object(serv))
            if not conf.has_equal_attributes(serv):
                return False

        # Compare service keysets
        configured_service_bindings = get_configured_service_bindings()
        service_bindings = get_actual_service_bindings()
        configured_keyset = set(configured_service_bindings.keys())
        service_keyset = set(service_bindings.keys())
        if len(configured_keyset ^ service_keyset) > 0:
            return False

        # Compare service item to item
        for key in configured_service_bindings.keys():
            conf = configured_service_bindings[key]
            serv = service_bindings[key]
            log('s diff %s' % conf.diff_object(serv))
            if not conf.has_equal_attributes(serv):
                return False

        # Fallthrough to success
        return True

    def delete_all_svc_bindings():
        log('Entering delete_all_bindings')
        actual_bindings = get_actual_service_bindings()
        for binding in actual_bindings.values():
            lbmonitor_service_binding.delete(client, binding)

    def sync_svc_bindings():
        delete_all_svc_bindings()
        if 'servicebindings' in module.params and module.params['servicebindings'] is not None:
            for servicebinding in module.params['servicebindings']:
                attribute_values_dict = copy.deepcopy(servicebinding)
                readwrite_attrs = [
                    'servicename',
                    'servicegroupname',
                    'weight',
                    'monitorname',
                ]
                attribute_values_dict['monitorname'] = module.params['monitorname']
                readonly_attrs = []
                binding_proxy = ConfigProxy(
                    actual=lbmonitor_service_binding(),
                    client=client,
                    attribute_values_dict=attribute_values_dict,
                    readwrite_attrs=readwrite_attrs,
                    readonly_attrs=readonly_attrs,
                )
                binding_proxy.add()

    def get_configured_servicegroup_bindings():

        readwrite_attrs = [
            'servicegroupname',
            'port',
            'state',
            'hashid',
            'serverid',
            'customserverid',
            'weight',
            'passive',
            'monstate'
        ]
        readonly_attrs = []

        configured_bindings = {}
        if 'servicegroupbindings' in module.params and module.params['servicegroupbindings'] is not None:
            for binding in module.params['servicegroupbindings']:
                attribute_values_dict = copy.deepcopy(binding)
                attribute_values_dict['monitor_name'] = module.params['monitorname']
                key = binding['servicegroupname'].strip()
                configured_bindings[key] = ConfigProxy(
                    actual=servicegroup_lbmonitor_binding(),
                    client=client,
                    attribute_values_dict=attribute_values_dict,
                    readwrite_attrs=readwrite_attrs,
                    readonly_attrs=readonly_attrs,
                )
        return configured_bindings

    def diff_list():
        return lbmonitor_proxy.diff_object(lbmonitor.get_filtered(client, 'monitorname:%s' % module.params['monitorname'])[0]),

    try:
        ensure_feature_is_enabled(client, 'LB')

        #get_actual_servicegroup_bindings()
        if module.params['operation'] == 'present':
            if not lbmonitor_exists():
                if not module.check_mode:
                    log('Adding monitor')
                    lbmonitor_proxy.add()
                    lbmonitor_proxy.update()
                    sync_svc_bindings()
                    client.save_config()
                module_result['changed'] = True
            elif not lbmonitor_identical():
                if not module.check_mode:
                    log('Updating monitor')
                    lbmonitor_proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                log('Doing nothing for monitor')
                module_result['changed'] = False

            # Sanity check for result
            if not module.check_mode:
                if not lbmonitor_exists():
                    module.fail_json(msg='Monitor does not seem to exist', **module_result)
                if not lbmonitor_identical():
                    module.fail_json(
                        msg='Monitor is not configured according to parameters given',
                        diff=diff_list(),
                        **module_result
                    )
            get_actual_service_bindings()

        elif module.params['operation'] == 'absent':
            if lbmonitor_exists():
                if not module.check_mode:
                    lbmonitor_proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for result
            if not module.check_mode:
                if lbmonitor_exists():
                    module.fail_json(msg='Server seems to be present', **module_result)

        module_result['actual_attributes'] = lbmonitor_proxy.get_actual_rw_attributes(filter='monitorname')
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    client.logout()

    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
