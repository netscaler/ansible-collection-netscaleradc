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
module: gslbvserver
short_description: Configuration for Global Server Load Balancing Virtual Server resource.
description: Configuration for Global Server Load Balancing Virtual Server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    description:
      - Enable logging appflow flow information
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  backupip:
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
    type: str
  backuplbmethod:
    description:
      - Backup load balancing method. Becomes operational if the primary load balancing
        method fails or cannot be used. Valid only if the primary method is based
        on either round-trip time (RTT) or static proximity.
    type: str
    choices:
      - ROUNDROBIN
      - LEASTCONNECTION
      - LEASTRESPONSETIME
      - SOURCEIPHASH
      - LEASTBANDWIDTH
      - LEASTPACKETS
      - STATICPROXIMITY
      - RTT
      - CUSTOMLOAD
      - API
  backupsessiontimeout:
    description:
      - A non zero value enables the feature whose minimum value is 2 minutes. The
        feature can be disabled by setting the value to zero. The created session
        is in effect for a specific client per domain.
    type: int
  backupvserver:
    description:
      - Name of the backup GSLB virtual server to which the appliance should to forward
        requests if the status of the primary GSLB virtual server is down or exceeds
        its spillover threshold.
    type: str
  comment:
    description:
      - Any comments that you might want to associate with the GSLB virtual server.
    type: str
  considereffectivestate:
    description:
      - 'If the primary state of all bound GSLB services is DOWN, consider the effective
        states of all the GSLB services, obtained through the Metrics Exchange Protocol
        (MEP), when determining the state of the GSLB virtual server. To consider
        the effective state, set the parameter to STATE_ONLY. To disregard the effective
        state, set the parameter to NONE. '
      - ''
      - The effective state of a GSLB service is the ability of the corresponding
        virtual server to serve traffic. The effective state of the load balancing
        virtual server, which is transferred to the GSLB service, is UP even if only
        one virtual server in the backup chain of virtual servers is in the UP state.
    type: str
    default: NONE
    choices:
      - NONE
      - STATE_ONLY
  cookie_domain:
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
    type: str
  cookietimeout:
    description:
      - Timeout, in minutes, for the GSLB site cookie.
    type: int
  disableprimaryondown:
    description:
      - Continue to direct traffic to the backup chain even after the primary GSLB
        virtual server returns to the UP state. Used when spillover is configured
        for the virtual server.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dnsrecordtype:
    description:
      - DNS record type to associate with the GSLB virtual server's domain name.
    type: str
    default: A
    choices:
      - A
      - AAAA
      - CNAME
      - NAPTR
  domainname:
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
    type: str
  dynamicweight:
    description:
      - Specify if the appliance should consider the service count, service weights,
        or ignore both when using weight-based load balancing methods. The state of
        the number of services bound to the virtual server help the appliance to select
        the service.
    type: str
    default: DISABLED
    choices:
      - SERVICECOUNT
      - SERVICEWEIGHT
      - DISABLED
  ecs:
    description:
      - If enabled, respond with EDNS Client Subnet (ECS) option in the response for
        a DNS query with ECS. The ECS address will be used for persistence and spillover
        persistence (if enabled) instead of the LDNS address. Persistence mask is
        ignored if ECS is enabled.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  ecsaddrvalidation:
    description:
      - Validate if ECS address is a private or unroutable address and in such cases,
        use the LDNS IP.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  edr:
    description:
      - Send clients an empty DNS response when the GSLB virtual server is DOWN.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  iptype:
    description:
      - The IP type for this GSLB vserver.
    type: str
    default: IPV4
    choices:
      - IPV4
      - IPV6
  lbmethod:
    description:
      - Load balancing method for the GSLB virtual server.
    type: str
    default: LEASTCONNECTION
    choices:
      - ROUNDROBIN
      - LEASTCONNECTION
      - LEASTRESPONSETIME
      - SOURCEIPHASH
      - LEASTBANDWIDTH
      - LEASTPACKETS
      - STATICPROXIMITY
      - RTT
      - CUSTOMLOAD
      - API
  mir:
    description:
      - Include multiple IP addresses in the DNS responses sent to clients.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  name:
    description:
      - Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my vserver" or 'my vserver').
    type: str
  netmask:
    description:
      - IPv4 network mask for use in the SOURCEIPHASH load balancing method.
    type: str
  newname:
    description:
      - New name for the GSLB virtual server.
    type: str
  order:
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
    type: int
  orderthreshold:
    description:
      - This option is used to to specify the threshold of minimum number of services
        to be UP in an order, for it to be considered in Lb decision.
    type: int
  persistenceid:
    description:
      - The persistence ID for the GSLB virtual server. The ID is a positive integer
        that enables GSLB sites to identify the GSLB virtual server, and is required
        if source IP address based or spill over based persistence is enabled on the
        virtual server.
    type: int
  persistencetype:
    description:
      - 'Use source IP address based persistence for the virtual server. '
      - After the load balancing method selects a service for the first packet, the
        IP address received in response to the DNS query is used for subsequent requests
        from the same client.
    type: str
    choices:
      - SOURCEIP
      - NONE
  persistmask:
    description:
      - The optional IPv4 network mask applied to IPv4 addresses to establish source
        IP address based persistence.
    type: str
  rule:
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - This field is applicable only if gslb method or gslb backup method are set
        to API.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character. '
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
    type: str
    default: '"none"'
  servicegroupname:
    description:
      - The GSLB service group name bound to the selected GSLB virtual server.
    type: str
  servicename:
    description:
      - Name of the GSLB service for which to change the weight.
    type: str
  servicetype:
    description:
      - Protocol used by services bound to the virtual server.
    type: str
    choices:
      - HTTP
      - FTP
      - TCP
      - UDP
      - SSL
      - SSL_BRIDGE
      - SSL_TCP
      - NNTP
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - RADIUS
      - RDP
      - RTSP
      - MYSQL
      - MSSQL
      - ORACLE
  sitedomainttl:
    description:
      - TTL, in seconds, for all internally created site domains (created when a site
        prefix is configured on a GSLB service) that are associated with this virtual
        server.
    type: int
  sobackupaction:
    description:
      - Action to be performed if spillover is to take effect, but no backup chain
        to spillover is usable or exists
    type: str
    choices:
      - DROP
      - ACCEPT
      - REDIRECT
  somethod:
    description:
      - 'Type of threshold that, when exceeded, triggers spillover. Available settings
        function as follows:'
      - '* CONNECTION - Spillover occurs when the number of client connections exceeds
        the threshold.'
      - '* DYNAMICCONNECTION - Spillover occurs when the number of client connections
        at the GSLB virtual server exceeds the sum of the maximum client (Max Clients)
        settings for bound GSLB services. Do not specify a spillover threshold for
        this setting, because the threshold is implied by the Max Clients settings
        of the bound GSLB services.'
      - '* BANDWIDTH - Spillover occurs when the bandwidth consumed by the GSLB virtual
        server''s incoming and outgoing traffic exceeds the threshold. '
      - '* HEALTH - Spillover occurs when the percentage of weights of the GSLB services
        that are UP drops below the threshold. For example, if services gslbSvc1,
        gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and
        3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3
        or gslbSvc2 and gslbSvc3 transition to DOWN. '
      - '* NONE - Spillover does not occur.'
    type: str
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
  sopersistence:
    description:
      - If spillover occurs, maintain source IP address based persistence for both
        primary and backup GSLB virtual servers.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sopersistencetimeout:
    description:
      - Timeout for spillover persistence, in minutes.
    type: int
    default: 2
  sothreshold:
    description:
      - Threshold at which spillover occurs. Specify an integer for the CONNECTION
        spillover method, a bandwidth value in kilobits per second for the BANDWIDTH
        method (do not enter the units), or a percentage for the HEALTH method (do
        not enter the percentage symbol).
    type: int
  state:
    description:
      - State of the GSLB virtual server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  timeout:
    description:
      - Idle time, in minutes, after which a persistence entry is cleared.
    type: int
    default: 2
  toggleorder:
    description:
      - Configure this option to toggle order preference
    type: str
    default: ASCENDING
    choices:
      - ASCENDING
      - DESCENDING
  tolerance:
    description:
      - Site selection tolerance, in milliseconds, for implementing the RTT load balancing
        method. If a site's RTT deviates from the lowest RTT by more than the specified
        tolerance, the site is not considered when the Citrix ADC makes a GSLB decision.
        The appliance implements the round robin method of global server load balancing
        between sites whose RTT values are within the specified tolerance. If the
        tolerance is 0 (zero), the appliance always sends clients the IP address of
        the site with the lowest RTT.
    type: int
  ttl:
    description:
      - Time to live (TTL) for the domain.
    type: int
  v6netmasklen:
    description:
      - Number of bits to consider, in an IPv6 source IP address, for creating the
        hash that is required by the SOURCEIPHASH load balancing method.
    type: int
    default: 128
  v6persistmasklen:
    description:
      - Number of bits to consider in an IPv6 source IP address when creating source
        IP address based persistence sessions.
    type: int
    default: 128
  weight:
    description:
      - Weight for the service.
    type: int
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
