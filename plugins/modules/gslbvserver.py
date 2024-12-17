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
module: gslbvserver
short_description: Configuration for Global Server Load Balancing Virtual Server resource.
description: Configuration for Global Server Load Balancing Virtual Server resource.
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
  appflowlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging appflow flow information
  backupip:
    type: str
    description:
      - The IP address of the backup service for the specified domain name. Used when
        all the services bound to the domain are down, or when the backup chain of
        virtual servers is down.
  backuplbmethod:
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
    description:
      - Backup load balancing method. Becomes operational if the primary load balancing
        method fails or cannot be used. Valid only if the primary method is based
        on either round-trip time (C(RTT)) or static proximity.
  backupsessiontimeout:
    type: float
    description:
      - A non zero value enables the feature whose minimum value is 2 minutes. The
        feature can be disabled by setting the value to zero. The created session
        is in effect for a specific client per domain.
  backupvserver:
    type: str
    description:
      - Name of the backup GSLB virtual server to which the appliance should to forward
        requests if the status of the primary GSLB virtual server is down or exceeds
        its spillover threshold.
  comment:
    type: str
    description:
      - Any comments that you might want to associate with the GSLB virtual server.
  considereffectivestate:
    type: str
    choices:
      - NONE
      - STATE_ONLY
    description:
      - If the primary state of all bound GSLB services is DOWN, consider the effective
        states of all the GSLB services, obtained through the Metrics Exchange Protocol
        (MEP), when determining the state of the GSLB virtual server. To consider
        the effective state, set the parameter to C(STATE_ONLY). To disregard the
        effective state, set the parameter to C(NONE).
      - ''
      - The effective state of a GSLB service is the ability of the corresponding
        virtual server to serve traffic. The effective state of the load balancing
        virtual server, which is transferred to the GSLB service, is UP even if only
        one virtual server in the backup chain of virtual servers is in the UP state.
  cookie_domain:
    type: str
    description:
      - The cookie domain for the GSLB site. Used when inserting the GSLB site cookie
        in the HTTP response.
  cookietimeout:
    type: float
    description:
      - Timeout, in minutes, for the GSLB site cookie.
  disableprimaryondown:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Continue to direct traffic to the backup chain even after the primary GSLB
        virtual server returns to the UP state. Used when spillover is configured
        for the virtual server.
  dnsrecordtype:
    type: str
    choices:
      - A
      - AAAA
      - CNAME
      - NAPTR
    description:
      - DNS record type to associate with the GSLB virtual server's domain name.
  domainname:
    type: str
    description:
      - Domain name for which to change the time to live (TTL) and/or backup service
        IP address.
  dynamicweight:
    type: str
    choices:
      - SERVICECOUNT
      - SERVICEWEIGHT
      - DISABLED
    description:
      - Specify if the appliance should consider the service count, service weights,
        or ignore both when using weight-based load balancing methods. The state of
        the number of services bound to the virtual server help the appliance to select
        the service.
  ecs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If enabled, respond with EDNS Client Subnet (ECS) option in the response for
        a DNS query with ECS. The ECS address will be used for persistence and spillover
        persistence (if enabled) instead of the LDNS address. Persistence mask is
        ignored if ECS is enabled.
  ecsaddrvalidation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Validate if ECS address is a private or unroutable address and in such cases,
        use the LDNS IP.
  edr:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Send clients an empty DNS response when the GSLB virtual server is DOWN.
  iptype:
    type: str
    choices:
      - IPV4
      - IPV6
    description:
      - The IP type for this GSLB vserver.
  lbmethod:
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
    description:
      - Load balancing method for the GSLB virtual server.
  mir:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include multiple IP addresses in the DNS responses sent to clients.
  name:
    type: str
    description:
      - Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my vserver" or 'my vserver').
  netmask:
    type: str
    description:
      - IPv4 network mask for use in the SOURCEIPHASH load balancing method.
  newname:
    type: str
    description:
      - New name for the GSLB virtual server.
  order:
    type: float
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
  orderthreshold:
    type: float
    description:
      - This option is used to to specify the threshold of minimum number of services
        to be UP in an order, for it to be considered in Lb decision.
  persistenceid:
    type: float
    description:
      - The persistence ID for the GSLB virtual server. The ID is a positive integer
        that enables GSLB sites to identify the GSLB virtual server, and is required
        if source IP address based or spill over based persistence is enabled on the
        virtual server.
  persistencetype:
    type: str
    choices:
      - SOURCEIP
      - NONE
    description:
      - Use source IP address based persistence for the virtual server.
      - After the load balancing method selects a service for the first packet, the
        IP address received in response to the DNS query is used for subsequent requests
        from the same client.
  persistmask:
    type: str
    description:
      - The optional IPv4 network mask applied to IPv4 addresses to establish source
        IP address based persistence.
  rule:
    type: str
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - This field is applicable only if gslb method or gslb backup method are set
        to API.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character.'
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
  servicegroupname:
    type: str
    description:
      - The GSLB service group name bound to the selected GSLB virtual server.
  servicename:
    type: str
    description:
      - Name of the GSLB service for which to change the weight.
  servicetype:
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
    description:
      - Protocol used by services bound to the virtual server.
  sitedomainttl:
    type: float
    description:
      - TTL, in seconds, for all internally created site domains (created when a site
        prefix is configured on a GSLB service) that are associated with this virtual
        server.
  sobackupaction:
    type: str
    choices:
      - DROP
      - ACCEPT
      - REDIRECT
    description:
      - Action to be performed if spillover is to take effect, but no backup chain
        to spillover is usable or exists
  somethod:
    type: str
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
    description:
      - 'Type of threshold that, when exceeded, triggers spillover. Available settings
        function as follows:'
      - '* C(CONNECTION) - Spillover occurs when the number of client connections
        exceeds the threshold.'
      - '* C(DYNAMICCONNECTION) - Spillover occurs when the number of client connections
        at the GSLB virtual server exceeds the sum of the maximum client (Max Clients)
        settings for bound GSLB services. Do not specify a spillover threshold for
        this setting, because the threshold is implied by the Max Clients settings
        of the bound GSLB services.'
      - '* C(BANDWIDTH) - Spillover occurs when the bandwidth consumed by the GSLB
        virtual server''s incoming and outgoing traffic exceeds the threshold.'
      - '* C(HEALTH) - Spillover occurs when the percentage of weights of the GSLB
        services that are UP drops below the threshold. For example, if services gslbSvc1,
        gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and
        3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3
        or gslbSvc2 and gslbSvc3 transition to DOWN.'
      - '* C(NONE) - Spillover does not occur.'
  sopersistence:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - If spillover occurs, maintain source IP address based persistence for both
        primary and backup GSLB virtual servers.
  sopersistencetimeout:
    type: float
    description:
      - Timeout for spillover persistence, in minutes.
  sothreshold:
    type: float
    description:
      - Threshold at which spillover occurs. Specify an integer for the CONNECTION
        spillover method, a bandwidth value in kilobits per second for the BANDWIDTH
        method (do not enter the units), or a percentage for the HEALTH method (do
        not enter the percentage symbol).
  timeout:
    type: float
    description:
      - Idle time, in minutes, after which a persistence entry is cleared.
  toggleorder:
    type: str
    choices:
      - ASCENDING
      - DESCENDING
    description:
      - Configure this option to toggle order preference
  tolerance:
    type: float
    description:
      - Tolerance in milliseconds. Tolerance value is used in deciding which sites
        in a GSLB configuration must be considered for implementing the RTT load balancing
        method. The sites having the RTT value less than or equal to the sum of the
        lowest RTT and tolerance value are considered. NetScaler implements the round
        robin method of global server load balancing among these considered sites.
        The sites that have RTT value greater than this value are not considered.
        The logic is applied for each LDNS and based on the LDNS, the sites that are
        considered might change. For example, a site that is considered for requests
        coming from LDNS1 might not be considered for requests coming from LDNS2.
  ttl:
    type: float
    description:
      - Time to live (TTL) for the domain.
  v6netmasklen:
    type: float
    description:
      - Number of bits to consider, in an IPv6 source IP address, for creating the
        hash that is required by the SOURCEIPHASH load balancing method.
  v6persistmasklen:
    type: float
    description:
      - Number of bits to consider in an IPv6 source IP address when creating source
        IP address based persistence sessions.
  weight:
    type: float
    description:
      - Weight for the service.
  gslbvserver_domain_binding:
    type: dict
    description: Bindings for gslbvserver_domain_binding resource
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
  gslbvserver_gslbservice_binding:
    type: dict
    description: Bindings for gslbvserver_gslbservice_binding resource
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
  gslbvserver_gslbservicegroup_binding:
    type: dict
    description: Bindings for gslbvserver_gslbservicegroup_binding resource
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
  gslbvserver_lbpolicy_binding:
    type: dict
    description: Bindings for gslbvserver_lbpolicy_binding resource
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
  gslbvserver_spilloverpolicy_binding:
    type: dict
    description: Bindings for gslbvserver_spilloverpolicy_binding resource
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
- name: Sample gslbvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure gslbvserver
      delegate_to: localhost
      netscaler.adc.gslbvserver:

        state: present
        name: backup_gslb_portal.bx.com
        servicetype: SSL
        backuplbmethod: ROUNDROBIN
        tolerance: '0'
        appflowlog: DISABLED
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
